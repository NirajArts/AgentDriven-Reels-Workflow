# Narration

The user chooses recorded audio or a synthetic voice. For ElevenLabs, load only the local `ELEVENLABS_API_KEY` from `.env` and the single ID in `elevenlabs_voice_id.txt`. Never log either. Confirm the chosen model's current availability, voice/account access, endpoint and direction syntax through [official documentation](https://elevenlabs.io/docs/overview) at production time. Do not assume a model label, version or audio tag is supported.

Keep clean spoken copy separate from tagged/directed submissions. Match delivery to context: curiosity, precision, urgency, warmth, pauses and emphasis should serve the line. Do not attach the same emotion tag to every sentence. Check that directions are not spoken aloud.

Generate only within the user's authorized scope and budget. Start with a short useful audition where needed; reuse successful takes. Bound retries; reconcile uncertain timeouts before another paid request. Preserve original takes and record script IDs, model/settings, exact submitted text, duration, source hash and non-secret usage receipt. Never silently switch voices or models.

Listen for words, pronunciation, expression, clean starts/tails and clipping. Transcription is a coverage check, not a substitute for listening. Do not stretch speech or remove meaningful breaths just to meet guessed timing. After selecting the audio, follow [Word timing](Word_Timing.md).
