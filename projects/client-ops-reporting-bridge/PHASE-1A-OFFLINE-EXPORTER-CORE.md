# Phase 1A — Offline Exporter Core

**Status:** COMPLETE (offline implementation + automated tests)  
**Date:** 2026-07-23  
**Locus:** `projects/client-ops-reporting-bridge/`  
**Production / Storage / n8n / Telegram:** UNCHANGED — not in scope

---

## 1. Implemented scope

Phase 1A delivers an **offline, fixture-driven exporter core** in Python 3 (stdlib only):

1. Load sanitized local fixture artifacts (read-only).
2. Validate required artifact set and fields.
3. Parse each JSON independently.
4. Apply frozen artifact authority / precedence.
5. Detect malformed, missing, stale, invalid, and contradictory sources.
6. Normalize to `OK` / `ATTENTION` / `FAILED` / `BLOCKED`.
7. Build `mars.client_ops.report` v1 envelope when contract-complete.
8. Deterministic envelope security validation.
9. Deterministic UUID v5 `event_id`.
10. Offline CLI modes: `validate-only`, `build-envelope`.
11. Offline `unittest` suite + synthetic fixtures.
12. Writes only under the project locus or system temp (explicit `--output`).

---

## 2. Source layout

```text
projects/client-ops-reporting-bridge/
  src/client_ops_reporting_bridge/
    __init__.py
    __main__.py
    cli.py
    constants.py
    models.py
    errors.py
    artifact_loader.py
    source_validation.py
    normalizer.py
    envelope_builder.py
    security_validator.py
    event_identity.py
    simple_formatter.py
    pipeline.py
  tests/
  fixtures/
  PHASE-1A-OFFLINE-EXPORTER-CORE.md
```

---

## 3. CLI modes

```text
set PYTHONPATH=projects/client-ops-reporting-bridge/src

python -m client_ops_reporting_bridge.cli validate-only --fixture <path>
python -m client_ops_reporting_bridge.cli build-envelope --fixture <path> --output <path>
```

| Mode | Behavior |
|------|----------|
| `validate-only` | Load → normalize → security; print sanitized JSON; **no** envelope file write |
| `build-envelope` | Same pipeline; write distributable envelope only to an **approved** local path |

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success (OK/ATTENTION/FAILED with distributable envelope, or validate success) |
| 2 | Source blocked/invalid or security rejection / non-distributable |
| 3 | Usage/config error |
| 4 | Unsafe output path |
| 5 | Internal unexpected error |

Default diagnostics do not print stack traces. `--debug` may add **redacted** issue details.

### Output path boundary (Phase 1A)

Approved write targets:

- under `projects/client-ops-reporting-bridge/`
- under the process temporary directory

Denied: Storage roots, deprecated C/D/E roots, arbitrary system paths.

---

## 4. Fixture layout

```text
fixtures/
  fixture-ok/
  fixture-attention-onboarding/
  fixture-attention-hygiene/
  fixture-failed-execution/
  fixture-blocked-stale/
  fixture-blocked-missing-artifact/
  fixture-blocked-malformed-json/
  fixture-blocked-classification-conflict/
  fixture-blocked-metric-conflict/
  fixture-blocked-missing-baseline/
  fixture-blocked-invalid-time/
  fixture-blocked-unknown-status/
  fixture-security-secret-detected/
  fixture-dedupe-repeat/
```

Each fixture is **synthetic** (not live production evidence). Optional `fixture-meta.json` pins `now_utc` / `generated_at` / test-only `action_text_override` for security probes.

---

## 5. Test command

```text
set PYTHONPATH=projects/client-ops-reporting-bridge/src;projects/client-ops-reporting-bridge/tests
python -m unittest discover -s projects/client-ops-reporting-bridge/tests -v
```

No internet. No third-party packages required.

---

## 6. Known limitations

- No live Storage run discovery.
- No exporter lock files.
- No promoted publication / `publish-file`.
- No webhook / `push-webhook`.
- No retry queues / n8n state.
- No Telegram delivery.
- No scheduler integration.
- No production configuration.
- Frozen Phase 0A metrics are **integers only**; when metrics are missing/untrusted, the core returns an internal BLOCKED result **without** a distributable envelope (does not invent zeros or change the contract to allow nulls).
- Display timezone default `Europe/Moscow` uses `zoneinfo` when available, else fixed UTC+3 (stdlib-safe on Windows without `tzdata`).

---

## 7. No production / runtime claims

Phase 1A does **not** claim:

- a production exporter service;
- Storage promotion;
- n8n workflow existence;
- Telegram connectivity;
- SITE-002 monitor changes.

---

## 8. Phase 1B blockers

Phase 1B transport/publication remains **NOT STARTED / BLOCKED** pending:

1. Evidence whether n8n can read `X:\AI MARS STORAGE` (PROFILE A vs B).
2. Dedicated Client Ops Telegram bot approval.
3. Exact internal test chat approval.
4. External sandbox / credential creation approval.
5. Explicit Phase 1B charter.

**Do not begin Phase 1B from this document alone.**
