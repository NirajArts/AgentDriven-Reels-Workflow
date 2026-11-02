# QA, fixes and final export

Use the project QA record. Check meaning first: does each planned action visibly produce its result? Check claims, real UI causality, typography, heading animation, captions, safe areas, asset crops, stacking, reading time and transitions. Inspect first/last frames and dense boundaries; use adjacent frames and enlarged details for fast motion.

Play the whole video at normal speed and listen where tools allow. Record sampled-frame review, playback, listening and numerical checks separately. Stills do not establish real-time pacing; waveforms do not establish voice performance. Keep unavailable checks explicitly pending.

For each defect, record timestamp, cause, fix, corrected source/output version and recheck evidence. Preserve previous outputs. Test affected transitions and dependencies after changes.

Before export, verify disk space, linked media, target dimensions/fps, audio routing, final hold, saved source and owned queue. Wait for the native render to report completion. File existence is not completion. Probe the output with local FFprobe for dimensions, duration, fps/frame count and audio codec/rate/channels. Decode the entire file with local FFmpeg and retain errors or a clean result. Check finite samples, clipping, truncation and unintended silence; listen to judge the mix.

Inspect the delivered encode after fixes. Record SHA256 hashes, native completion evidence, exact export settings and remaining review in the publishing manifest. Choose export specifications for the user's destination; do not upscale a small proof and call it a full-resolution native render.
