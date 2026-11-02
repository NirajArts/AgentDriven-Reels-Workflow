# Video Workflow

A reusable workspace for making videos with an AI agent and EffectCraft. You choose the topic, audience, style, format and voice. Includes docs, skills and blank project templates; no example video or media is bundled.

## Set up (Windows)

1. Extract this folder and open it in your coding agent. Install [Python 3.11](https://www.python.org/downloads/) if needed.
2. Download [EffectCraft for Windows x64 — portable ZIP](https://github.com/storytold/effectcraft/releases/download/v0.20.0/effectcraft-0.20.0-windows-x64-portable.zip). Extract it into `tools/effectcraft/`. It includes **effectcraft.exe** and **effectcraft-cli.exe**. For other machines or newer versions, use the [official GitHub releases](https://github.com/storytold/effectcraft/releases/latest).
3. Run `python scripts/setup_workspace.py`. Edit the new `.env`: add your `ELEVENLABS_API_KEY`, executable paths and a free `EFFECTCRAFT_PORT`. Put your chosen voice ID on one line in `elevenlabs_voice_id.txt`. Leave ElevenLabs blank if you will supply recorded audio. Never upload these private files.
4. Open **effectcraft.exe** yourself. For agent control, start it with `--control YOUR_PORT` (replace `YOUR_PORT` with your chosen number). Keep this instance open. See [connection setup](Docs/EffectCraft.md) for the PowerShell command.
5. Give your agent this prompt:

> Read AGENTS.md and tools/README.md. Set up local Whisper and FFmpeg under tools/, verify the EffectCraft connection I opened, and record readiness. Then help me fill the brief for my video. Ask for my creative choices; do not generate paid audio yet.

The agent should download dependencies only during this setup step. Tool binaries and model files stay local, outside Git.

## Make a video

Tell your agent what you want to make. It creates `Projects/Project001/`, drafts a script, prepares narration, measures words, plans shots, builds visuals, reviews and fixes them, then exports and packages the result. Review the script and a short visual proof before a full build. Paid generation and publishing require your instruction.

Start with [AGENTS.md](AGENTS.md). See [the workflow](Docs/Workflow.md), [folders](Docs/Workspace.md), and [skills](skills/README.md). The agent can read the skills directly; no plugin installation is required.
