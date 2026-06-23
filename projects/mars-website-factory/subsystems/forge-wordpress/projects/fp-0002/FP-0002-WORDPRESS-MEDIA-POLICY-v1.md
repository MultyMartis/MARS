# FP-0002 — WordPress Media Policy v1

**Version:** v1 | **Date:** 2026-06-23

## FW-06A rule

**Do not upload unfinished frontend assets** from `workspaces/fp-0002-shpigovsky-v6/src/` or `dist/` into Media Library.

## Source classes

| Class | Location | WP uploads |
|-------|----------|------------|
| Approved design exports | Operations / design folders | After handoff only |
| Frontend implementation assets | V6 `src/img`, `src/svg`, fonts | **At FW-06B integration** |
| Temporary operator assets | Local only | Case-by-case |
| Client production media | Production | **Forbidden** without charter |

## Technical policy

| Topic | Policy |
|-------|--------|
| Original preservation | No destructive overwrite of sources |
| Generated sizes | WP defaults until theme registers sizes at integration |
| SVG | Deferred — security review at integration |
| WebP/AVIF | Follow frontend build handoff — not pre-imported |
| Alt text | Required at content entry — not FW-06A |
| Filenames | Kebab-case preferred at integration |

## Handoff boundary

Approved assets manifest from Production Pass is SoT for media import sequence.

---

*FP-0002 media policy — FW-06A.*
