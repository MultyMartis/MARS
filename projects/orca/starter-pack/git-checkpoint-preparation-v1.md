# ORCA Git Checkpoint Preparation v1

## Status

Checkpoint preparation note only.

This document does not stage, commit, push, or require a checkpoint by itself.

## Recommended Checkpoint Scope

Recommended scope for a future checkpoint:

- first operational pilot simulation;
- operational friction review;
- real operator value review;
- immediate prune candidates;
- starter-pack extraction;
- starter-pack stabilization;
- future testing boundaries;
- milestone summary.

The checkpoint should represent:

`ORCA first usable operational starter-core for manual PPC testing.`

## Review Before Commit

Before committing, review:

- all new files under `projects/orca/reality-consolidation/`;
- all new files under `projects/orca/starter-pack/`;
- whether filenames match the intended milestone;
- whether each document avoids architecture, automation, governance, and runtime claims;
- whether SAFE UNKNOWN is preserved;
- whether wording avoids fake market certainty;
- whether the starter stack remains small.

## Should Remain Excluded

Do not include unrelated work unless intentionally reviewed:

- runtime folders;
- generated artifacts;
- unrelated cleanup;
- unrelated governance expansion;
- unrelated registry or log changes;
- experimental files outside the current ORCA pilot/starter-pack scope;
- secrets, credentials, local environment files, or tool caches.

## Risks Of Checkpointing Too Early

- fictional pilot findings may be mistaken for validated market evidence;
- starter-pack choices may appear final before live use;
- optional layers may look approved by association;
- weak wording could freeze accidental overclaims;
- unrelated dirty files could enter the milestone.

## Risks Of Waiting Too Long

- the usable starter core may drift;
- new documents may expand ORCA before testing;
- anti-bloat lessons may weaken;
- future operators may not know which subset to use;
- milestone context may become harder to recover.

## Safe Checkpoint Criteria

A checkpoint is safer when:

- the scope is limited to ORCA pilot and starter-pack docs;
- no files are staged blindly;
- unrelated changes are excluded;
- the commit message states operational starter-core, not system completion;
- the checkpoint does not imply live validation;
- the next step remains real manual testing.

## Suggested Commit Message Shape

If a human later chooses to commit, a safe message shape would be:

`Stabilize ORCA starter pack for manual PPC testing`

Reason:

it describes a documentation milestone without claiming automation, runtime, launch readiness, or proven market performance.
