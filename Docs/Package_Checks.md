# Starter package checks

Checked 2026-11-03:

- Fresh ZIP extraction and local document links passed.
- Configuration setup creates private files and preserves existing values on rerun.
- Project creation builds the expected folders, chooses the next unused number and refuses an existing destination without changing its contents.
- All three skill files passed the skill format validator.
- Python syntax, transcription help and missing-input rejection passed.
- Git exclusions cover private configuration, local tools/models, assets and production projects; public templates remain included.
- The payload contains no production media, identity assets, credentials, voice IDs, installed binaries or model weights.

Dependency download/install, real Whisper inference, live EffectCraft production and paid narration were not run for this package. They must be verified on the recipient's machine. Official download locations and the EffectCraft portable package contents were checked; that does not certify compatibility with every machine or future release.
