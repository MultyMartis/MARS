# SITE-002 — 1C Import Contract

## Filename families (canonical)

| Phase | Expected family | Notes |
|-------|-----------------|-------|
| Catalog | `import0_*.xml` | e.g. `import0_1.xml` |
| Offers | `offers0_*.xml` | e.g. `offers0_1.xml` |

**Literal `offer.xml` is NOT the canonical expected filename.**

`import0_*.xml` ≠ `offers0_*.xml`.

## Processing order

1. Acquire singleton import lock (`MAX_SAFE_IMPORT_CONCURRENCY=1`).
2. Catalog phase against present `import0_*.xml`.
3. Offers phase against present `offers0_*.xml`.
4. Write terminal run state (classification, timestamps, trigger_source, run_id).
5. Completion dispatcher may fire (if enabled).

## Trigger sources

- `SCHEDULED` — Beget import cron / wrapper
- `ADMIN_MANUAL` — OpenCart admin button

## Terminal classifications (conceptual)

| Outcome | Meaning |
|---------|---------|
| Success | Catalog + offers inputs present and processed per accepted rules |
| ATTENTION / `OFFERS_INPUT_MISSING` | Catalog present; offers input absent; prices/stock may not update |
| Failure | Hard import/runner/wrapper failure |

**Absence of offers input must NOT be labeled full success.**

## No-offers behavior

- Catalog phase may PASS.
- Offers phase formally runs with no input.
- Do **not** disable products merely because offers input is absent.
- Client Ops must emit ATTENTION (not success).

## Locking / concurrency

- One import at a time.
- Manual + scheduled overlap: second waits or is rejected by lock — do not run parallel imports.

## Ownership boundary

| Concern | Owner |
|---------|-------|
| Generating/uploading CommerceML files | External 1C / exchange process |
| Detecting files, running importer, terminal classification | Site / server wrapper |
| Operator notification | Client Ops (dispatcher → n8n → Telegram) |
| Why offers file is missing | OPEN forensic (1C vs upload vs naming vs race) |

## Wrapper ownership

Canonical runner ownership is **server-side** via `mars_1c_import_wrapper.php` (live under `/storage/mars-tools/cron/`). Repo copies under `projects/ocpilot/sites/site-002/tools/` are source mirrors for ops/docs — deploy carefully under separate charter.

## Cleanup / file lifecycle

Document only proven behavior from evidence; do not invent cleanup semantics. Historical wrapper versions may move/archive exchange files after run — verify live config before documenting new claims.
