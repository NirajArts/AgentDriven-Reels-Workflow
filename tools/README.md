# Local tools setup for the agent

Run this only when the user requests setup. Keep downloads, environments and caches under this `tools/` folder. Check existing usable tools first; preserve them. Do not install globally, change system PATH, use administrator privileges or launch/close EffectCraft automatically. No binaries or model weights are included in this starter.

## EffectCraft

The user downloads/extracts and opens the app using [connection instructions](../Docs/EffectCraft.md). Verify both executables and the selected bridge. Record actual paths/version in `.env` and `installed.local.json`. Never select a different running instance because its port responds.

## FFmpeg and FFprobe (Windows x64)

[FFmpeg's download page](https://ffmpeg.org/download.html) links to the [Gyan Windows builds](https://www.gyan.dev/ffmpeg/builds/). Use its release essentials ZIP, which includes both executables. Run from the workspace root, using unused destinations:

```powershell
Invoke-WebRequest https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -OutFile tools/downloads/ffmpeg-essentials.zip
Invoke-WebRequest https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip.sha256 -OutFile tools/downloads/ffmpeg-essentials.zip.sha256
$expectedHash = ((Get-Content tools/downloads/ffmpeg-essentials.zip.sha256 -Raw).Trim() -split '\s+')[0]
$actualHash = (Get-FileHash tools/downloads/ffmpeg-essentials.zip -Algorithm SHA256).Hash
if ($expectedHash -notmatch '^[0-9a-fA-F]{64}$' -or $actualHash -ne $expectedHash) { throw 'FFmpeg checksum mismatch' }
Expand-Archive -LiteralPath tools/downloads/ffmpeg-essentials.zip -DestinationPath tools/ffmpeg/package
```

Do not overwrite these names on a repeat setup; inspect the existing archive/install or choose a new versioned destination. Locate `ffmpeg.exe` and `ffprobe.exe` inside the extracted `bin/` directory, and update `.env` to their **actual** paths (the template paths are examples). Keep the accompanying license files. Run each executable with `-version`; record the download URL, archive SHA256 and reported versions. For another architecture/OS, choose a compatible build from the official download page and record the change.

## Local Whisper

Use [faster-whisper](https://github.com/SYSTRAN/faster-whisper), a local Whisper implementation. CPU/int8 is the baseline; GPU support is a separate optional setup. This environment is separate from the agent's Python. Use Python 3.11:

```powershell
python -m venv tools/whisper/.venv
.\tools\whisper\.venv\Scripts\python.exe -m pip install -r tools/requirements-whisper.txt
.\tools\whisper\.venv\Scripts\python.exe -c "from faster_whisper.utils import download_model; download_model('small', output_dir='tools/whisper/models/small', cache_dir='tools/whisper/cache')"
.\tools\whisper\.venv\Scripts\python.exe -m pip freeze > tools/whisper/requirements-installed.txt
```

Skip environment creation if it already exists. The model download requires internet and disk space; later transcription uses its local directory with downloads disabled. `small` is a starter choice, not a quality guarantee. Choose a different multilingual model deliberately if the material needs it. Do not change GPU drivers to make setup work. Faster-whisper can decode through PyAV; the separate FFmpeg executables are used for independent media checks and extraction.

Record package versions, model ID, model file hashes, device/compute type and successful local load in `installed.local.json`. Then run [transcription](../Docs/Word_Timing.md) on user-provided audio when available. Dependency installation is not evidence that transcription, live editing or final rendering has passed.

## Readiness record

Record Python, EffectCraft, FFmpeg/FFprobe and faster-whisper versions; local paths; checksums; the chosen port and verified instance; model-load result; and any remaining gaps. Keep credentials and voice IDs out of this record. If setup fails, report the specific failed step and continue independent documentation work; do not silently substitute a cloud service.
