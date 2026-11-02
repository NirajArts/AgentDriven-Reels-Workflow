# Independent word timing

Use local Whisper on the actual selected waveform, independent of the speech provider. See [tool setup](../tools/README.md). Do not upload audio or invent timestamps from the script. Keep raw recognition, corrections and provider alignments separate.

The [transcription helper](../scripts/transcribe_audio.py) accepts an already downloaded local faster-whisper model and writes word-level JSON. It does not download models or call a cloud API. Example after creating a project and supplying audio:

```powershell
.	ools\whisper\.venv\Scripts\python.exe scripts/transcribe_audio.py Projects/Project001/Audio/Working/Narration_v001.wav --model-dir tools/whisper/models/small --output Projects/Project001/Audio/Transcripts/Raw/Words_v001.json
```

Select language explicitly with `--language` when known. Inspect recognition against script and audio; preserve omissions, repetitions and uncertain boundaries in the review record. Keep [word timings](../Templates/Word_Timings.csv) and take mappings with source hashes. A missing confidence value stays blank.

Validate finite nonnegative times, end >= start, chronological order and audio bounds. Preserve full precision; quantize visual events to the chosen frame grid with a recorded rounding rule. For edited takes: timeline time = source time - trim-in + clip offset. Re-transcribe the final assembly when edits change boundaries. Silent content uses editorial timing, labeled accordingly.
