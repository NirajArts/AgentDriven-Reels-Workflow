---
name: audio-word-timing
description: Independently transcribe local video narration with Whisper and prepare reviewed word-level timing for scenes and captions. Use when actual audio needs timing; do not infer timestamps from scripts or provider alignment alone.
---

# Audio word timing

Read [Word timing](../../Docs/Word_Timing.md) and the selected take/assembly record. Preserve the source waveform and hash. For dependency setup follow [tools](../../tools/README.md) only within the user's setup scope. Prefer CPU/int8 local processing before introducing GPU dependencies.

Use the root `scripts/transcribe_audio.py` with an already downloaded local model and a new versioned output path. It must not download unexpectedly or upload audio. Keep raw recognition separate from corrected working timings and provider alignments.

Compare exact words against the script and available listening. Flag omissions, repetitions, uncertain names and nonverbal sounds. Validate finite times, ordering, source bounds and any intended overlap. Record engine/model/settings, source hash, raw output and corrections; do not fabricate confidence or claim listening based on text.

Map edited source takes using source time minus trim-in plus timeline offset. Re-transcribe changed assemblies when cuts affect boundaries. Preserve precise seconds and record fps/rounding when creating frame events. Only reviewed timing governs the scene plan and subtitles; silent videos require editorial timing instead.
