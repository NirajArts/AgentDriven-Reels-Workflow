"""Transcribe local audio with a pre-downloaded faster-whisper model; no cloud."""
import argparse
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def inside_workspace(value):
    candidate = Path(value)
    path = (candidate if candidate.is_absolute() else ROOT / candidate).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Audio, model and output must be inside this workspace.')
    return path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('audio')
    parser.add_argument('--model-dir', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--language', default=None)
    args = parser.parse_args()
    try:
        source, model, output = map(inside_workspace, (args.audio, args.model_dir, args.output))
    except ValueError as error:
        parser.error(str(error))
    if not source.is_file() or not model.is_dir():
        parser.error('Supply an existing audio file and downloaded local model directory.')
    if output.exists():
        parser.error('Output exists; choose a new versioned filename.')
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        parser.error('Use the Python environment configured in tools/README.md.')
    recognizer = WhisperModel(str(model), device='cpu', compute_type='int8', local_files_only=True)
    segments, info = recognizer.transcribe(str(source), language=args.language,
                                          word_timestamps=True, beam_size=5)
    rows, words = [], []
    previous = 0.0
    for segment in segments:
        rows.append({'id': segment.id, 'start': segment.start, 'end': segment.end,
                     'text': segment.text})
        for word in segment.words or []:
            start, end = float(word.start), float(word.end)
            if not (math.isfinite(start) and math.isfinite(end) and
                    0 <= start <= end <= info.duration + 0.1 and start >= previous):
                raise ValueError('Invalid/overlapping recognition timing; inspect audio and engine output.')
            previous = end
            words.append({'word': word.word, 'start': start, 'end': end,
                          'probability': word.probability, 'review': 'raw_unreviewed'})
    result = {'source': source.relative_to(ROOT).as_posix(),
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'engine': 'faster-whisper',
              'engine_version': importlib.metadata.version('faster-whisper'),
              'model_dir': model.relative_to(ROOT).as_posix(),
              'device': 'cpu', 'compute_type': 'int8', 'word_timestamps': True,
              'language': info.language, 'duration_seconds': info.duration,
              'segments': rows, 'words': words, 'review': 'raw_unreviewed'}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
    print(f'Saved {len(words)} raw words. Compare with the script and actual audio before scene timing.')

if __name__ == '__main__':
    main()
