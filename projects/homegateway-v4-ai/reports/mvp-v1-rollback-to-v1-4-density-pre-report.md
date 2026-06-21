# REPORT — HomeGateway v4.ai MVP v1 Rollback to v1.4 Density Pre

## Rollback Reason

The active MVP v1 workspace was rolled back because the later visual experiments did not produce the desired result:

- `v1.4 density pass`
- `v1.4 row rebalance`
- `v1.5 left sidebar quality pass`
- `v1.6 sidebar telemetry metaline pass`

The task goal was restoration only. No redesign, no new layout work, and no architecture-doc edits were performed.

## Safety Snapshot Path

- Snapshot created at: `workspaces/homegateway-v4-ai/archive/v1.6-failed-sidebar-experiments-snapshot/`
- Snapshot label: `v1.6 failed sidebar experiments snapshot`
- Snapshot reason: `preserve failed density/row/sidebar/telemetry experiments before rollback`

## Rollback Source Archive

- Source of truth used for restore: `workspaces/homegateway-v4-ai/archive/v1.4-density-pass-pre/`

## Restored Paths

The active workspace restored into `workspaces/homegateway-v4-ai/v1/` now matches the source archive contents, excluding archive metadata that must remain inside the archive.

Restored top-level paths:

- `src/`
- `dist/`
- `README.md`
- `RHYTHM-NOTES.md`
- `package.json`
- `package-lock.json`
- `gulpfile.js`
- `.gitignore`
- `archive-manifest-v0.md`
- `OPERATIONAL-DOCS-REFERENCES.md`

Not restored into active `v1/` root:

- `ARCHIVE-README.md`

## Build Result

Command run:

```bash
cd workspaces/homegateway-v4-ai/v1
npm run build
```

Result:

- Build succeeded.
- Build tool: `gulp build`
- Observed warnings:
  - Dart Sass legacy JS API deprecation warning
  - Node `fs.Stats` deprecation warning

## Verification

- Active `workspaces/homegateway-v4-ai/v1/` was compared against `workspaces/homegateway-v4-ai/archive/v1.4-density-pass-pre/` with file-hash verification and matched the source archive tree, excluding `ARCHIVE-README.md`.
- `#main_area` is present in the restored workspace.
- No `letter-spacing` declarations were found in `src/`.
- No `text-transform` declarations were found in `src/`.
- The 4px radius law remains represented by `$hg-radius: 4px;` and its reuse across restored SCSS.
- Desktop shell centering remains present through restored viewport-shell centering rules and shell width constraints.
- No replacement-character findings were detected in text-source files scanned under `src/`, so UTF-8 Russian content appears preserved.

## Remaining Issues

- No restore blocker remains.
- Build warnings remain from existing toolchain deprecations and were not changed in this rollback task.

## Remaining Notes

- The failed experimental state was preserved before rollback in the safety snapshot archive.
- The active `v1/` no longer contains experimental-only top-level items that were absent from the source archive, including local `node_modules/` and temporary helper scripts from the failed state snapshot.

## SAFE UNKNOWN

- Visual verification in a browser was not performed in this task, so centered-shell appearance and Russian rendering were verified from restored source/build state rather than a live manual UI check.
- This report does not claim any redesign or new implementation beyond the archive-based rollback.

## Git Status Summary

- No staging, commit, or push was performed.
- Repository git status is already noisy outside this rollback scope; this report only records that the rollback work was completed without staging.
