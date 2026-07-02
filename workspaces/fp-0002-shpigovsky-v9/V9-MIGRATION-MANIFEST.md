# V9 Migration Manifest — Phase V9-01

**Date:** 2026-07-02  
**Source V8:** `X:\AI MARS\workspaces\fp-0002-shpigovsky-v8`  
**Destination V9:** `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9`  
**Method:** robocopy `/E` excluding `node_modules`, `dist`, `.git`

## Excluded from copy

- `node_modules/`
- `dist/`
- `.git/`
- `*.log`

## Snapshot

- ZIP: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-01-workspace-creation\snapshot-before\FP-0002-V9-01-PRE-MIGRATION-SNAPSHOT.zip`
- SHA-256: `572729C8865C80406646F46DC6CC6AB8511561F563767C258FE0A4B8976DFED1`

## V9 authority statement

V9 was copied from V8 approved source, then modified for:

- clean-route `dist/` architecture
- root-relative `/assets/...` URLs
- route manifest-driven emission
- navigation / home accordion operator corrections
- placeholder service pages
- genotyping route unpublished

V8 was **not modified** by migration (copy-only).

## Intentional post-copy changes

See git-untracked V9 workspace files and modified V9 `src/`, `tools/`, `gulpfile.js`, `package.json`.

## Build validation

- `npm run build` — PASS (31 routes emitted)
- Asset path validation — PASS
- Internal link validation — PASS
- HTTP route validation — 31/31 HTTP 200
