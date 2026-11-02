# Scene planning and implementation

Plan after audio and independent timing are ready. Each shot specifies exact words/time cue, starting state, visible action, result, heading motion, reading hold, transition, assets, cursor interaction if relevant, sound and evidence. Use [Scene plan](../Templates/Project/Docs/Scene_Plan.md) and its CSV. Choose dimensions and fps from the user's output needs.

Verify claims, process reproducibility, media rights, timing feasibility and tool ownership. Establish a short editable visual proof, inspect it, then extend the accepted direction. Keep related objects continuous across promised transformations. A cut to a title does not demonstrate a change.

Keep text, imagery, footage, narration, effects and music editable. Use supported native commands and versioned checkpoints. Check shape bounds, stacking, parent transforms and child lifetimes on actual frames. Intersect group visibility with existing typing/replacement intervals; do not make every partial string visible at once.

Test whether null/controller opacity propagates in the installed app version. If it does not, animate drawing descendants. A caption's normal/highlighted word must occupy the same position without simultaneous duplicates. Check both entry and exit paths, not just settled endpoints. Follow [Motion](Visual_and_Motion.md) and [QA](QA_and_Export.md).
