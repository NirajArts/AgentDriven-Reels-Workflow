# EffectCraft connection and production

[Official repository](https://github.com/storytold/effectcraft) · [Releases](https://github.com/storytold/effectcraft/releases/latest) · [Agent docs](https://github.com/storytold/effectcraft/blob/main/docs/agents.md) · [Control protocol](https://github.com/storytold/effectcraft/blob/main/docs/control-protocol.md).

Windows x64 download checked 2026-11-03: [v0.20.0 portable ZIP](https://github.com/storytold/effectcraft/releases/download/v0.20.0/effectcraft-0.20.0-windows-x64-portable.zip). It includes the desktop app and CLI, as shown in the [official packaging script](https://github.com/storytold/effectcraft/blob/v0.20.0/packaging/windows/package.ps1). SHA256: `90c01550cf3ba798af294d2913d6e757ba179013a1292c5d257a401341a0b680`. Use the matching architecture; keep its license/notice files. Newer versions may have different commands, so inspect installed help and schemas.

The user opens the app. A PowerShell example after extraction is below; replace the path and `9890` with the actual executable and a verified free local port. This number is an example, not a reserved assignment. Save the same values in `.env`.

```powershell
& ".\tools\effectcraft\effectcraft-0.20.0-windows-x64-portable\effectcraft.exe" --control 9890
```

For help, run **effectcraft-cli.exe**, never the GUI executable. Read-only preflight examples (adapt to installed syntax):

```powershell
& ".\tools\effectcraft\effectcraft-0.20.0-windows-x64-portable\effectcraft-cli.exe" --help
& ".\tools\effectcraft\effectcraft-0.20.0-windows-x64-portable\effectcraft-cli.exe" info --bridge 9890 --json
& ".\tools\effectcraft\effectcraft-0.20.0-windows-x64-portable\effectcraft-cli.exe" exec project.summary --bridge 9890 --json
& ".\tools\effectcraft\effectcraft-0.20.0-windows-x64-portable\effectcraft-cli.exe" exec renderQueue.list --bridge 9890 --json
```

Verify listener/process ownership, executable/version, loaded path, dirty state and queue. A blank window or open port does not prove ownership. Do not overwrite unsaved work or manipulate another user's project. Save a new native checkpoint before edits. If no bridge is available, have the user save work and open the intended instance with control enabled; do not close or restart it automatically.

Discover commands through CLI help and command schemas. Use supported live layer/property/key/save commands. Native `.ecproj` JSON may be inspected read-only, never rewritten as an editing shortcut. Do not assume headless commands mutate the live app. For live export, discover the installed render-queue commands, queue only the intended composition/output, wait for completion and retain its receipt. Keep older queue entries and files.

No desktop automation is needed for this workflow. MCP is optional when supported direct commands meet the task. Inspect actual encoded frames/playback/audio and record which methods were available. No installed-version production compatibility is claimed by this template alone.
