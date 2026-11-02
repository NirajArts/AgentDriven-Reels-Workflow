# Folder conventions

```text
AGENTS.md / START_HERE.md / HANDOFF.md  Agent entry points
.env.example                         Blank local configuration template
elevenlabs_voice_id.example.txt       Blank voice selection template
Docs/                                Shared production process
skills/                              Portable agent skills
scripts/                             Small local helpers
tools/                               Locally downloaded software and models
Assets/                              User-provided reusable media
Templates/Project/                   Reusable project skeleton
Projects/ProjectNNN/                 Created only on a user's video request
```

Project folders contain `Docs`, `Audio/Originals`, `Audio/Working`, `Audio/Transcripts/Raw`, `Audio/Transcripts/Working`, `Media`, `EffectCraft`, `Previews`, `Exports`, `QA`, `Publishing` and `Delivery`. Reusable assets are separated into Graphics, Footage, Fonts, Audio/SFX and Audio/Music. Keep source/licensing notes beside any added assets.

Use `Project001`, `Project002`, and onward; never reuse an existing project directory. Use descriptive versioned filenames such as `Narration_v001.wav`, `Scene_Plan_v002.csv` and `Video_v003.mp4`. A suffix does not prove approval or QA. Record exact dependencies and paths in project status.

Run helpers from the workspace root. Scripts resolve their own workspace location; they do not depend on another machine's drive letters. `.env` is configuration, not a shell script. Your agent must parse it as data, resolve relative paths from this root and avoid printing values. No helper automatically loads or uses an API key.

This starter excludes production projects, binaries, models and user assets from Git by default. Add selected public artifacts intentionally only after a privacy, size and license review. `.gitignore` does not sanitize manually created ZIPs or old Git history.
