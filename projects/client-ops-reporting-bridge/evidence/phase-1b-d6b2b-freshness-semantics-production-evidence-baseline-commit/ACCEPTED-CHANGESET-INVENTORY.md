# ACCEPTED-CHANGESET-INVENTORY — D6B2B

## Isolation verdict

`D6B2B_ACCEPTED_CHANGESET_ISOLATED`

## Classification of Client Ops porcelain

| Class | Content | Action |
|-------|---------|--------|
| A | D6B offline implementation (delivery_eligibility + producer/normalizer/envelope/pipeline/adapter/errors + fixtures/tests/harness) | INCLUDE |
| B | D6B phase doc + evidence pack | INCLUDE |
| C | D6B2 verification tooling/evidence (PRODUCER_ONLY; byte mutations=0) | INCLUDE |
| D | D6B2B baseline docs/evidence (this pack + phase doc) | INCLUDE |
| E | Previously committed A-workstream materials showing inverse cache only (D6/D6A/D6A2/D6A2B staged deletes + WT untracked mirrors; activation-client inverse) | EXCLUDE |
| F | Unrelated/newer Client Ops WIP (D5R-MONCLEAN / MOND / MONRESTORE) | EXCLUDE |
| G | unknown | none in allowlist |

## Candidate count (pre-D6B2B-doc creation)

79 accepted A+B+C paths (implementation + D6B/D6B2 evidence), plus D6B2B phase + evidence files created by this phase.

## Explicit exclusions

- SITE-002 source under `projects/ocpilot/sites/site-002/` → **0**
- MetaBOT / iSEO / FP-0002 / Website Factory → **0**
- Workstream A inverse-cache paths → **0** (already in `12e4c6ad…`)
- MONCLEAN / MOND / MONRESTORE → **0**
- Workstream C/E/D → not started
