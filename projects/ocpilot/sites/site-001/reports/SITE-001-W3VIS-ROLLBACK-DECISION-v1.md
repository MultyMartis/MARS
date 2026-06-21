# SITE-001 W3VIS Rollback Decision v1

**Type:** Post-rollback decision — W3VIS-01A + W3VIS-01B reversal  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`

**Inputs:** [SITE-001-W3VIS-01A-EXECUTION-v1.md](SITE-001-W3VIS-01A-EXECUTION-v1.md) · [SITE-001-W3VIS-01B-EXECUTION-v1.md](SITE-001-W3VIS-01B-EXECUTION-v1.md) · [SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md](SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md)

---

## Verdict

**PASS** — W3VIS T1 rollback **COMPLETE** on TEST.

Pre-W3VIS-01A CSS state restored from OCPilot backup `pre-w3vis-01a-20260609-0517`. PDP hero returned to pre-W3VIS baseline. W3UX-C1 used catalog density **preserved**. **9/9** verification URLs pass.

---

## Operator decision

| Field | Value |
|-------|--------|
| Rollback approved | **YES** |
| Waves rejected | **W3VIS-01A** · **W3VIS-01B** |
| Reason | **Task drift** — operator requested global palette / visual tone refresh across whole site; execution incorrectly scoped PDP hero hierarchy changes |
| Tier executed | **T1** — incremental file restore |
| Beget global backup used | **NO** |

---

## Criteria assessment

| Criterion | Result |
|-----------|--------|
| Rollback package located | **PASS** — `pre-w3vis-01a-20260609-0517` |
| Backup integrity verified | **PASS** — manifest + 2 CSS files + SHA-256 |
| Only CSS scope restored | **PASS** — `main.css`, `media.css` only |
| Phase 1 / DB / Twig / PHP / JS / admin / SEO untouched | **PASS** |
| Caches cleared + modification refresh | **PASS** — 4/4 HTTP 200 |
| W3VIS-01A marker absent (live) | **PASS** |
| W3VIS-01B marker absent (live) | **PASS** |
| PDP hero pre-W3VIS state | **PASS** — no W3VIS hero surface rules |
| No broken layout | **PASS** — 9/9 HTTP 200 |
| W3UX-C1 preserved | **PASS** — marker + `/cars/` probes |
| W3-V / W3V2 preserved | **PASS** — markers present in live CSS |
| No PHP / Twig errors | **PASS** |

---

## Authorization state after rollback

| Gate | Status |
|------|--------|
| W3VIS-01A execution | **ROLLED BACK** — 2026-06-09 |
| W3VIS-01B execution | **ROLLED BACK** — 2026-06-09 |
| W3VIS-01A / 01B on TEST | **INACTIVE** |
| W3VIS-01 discovery | **DONE** — reference only; superseded for execution direction |
| W3UX-C1 | **ACTIVE** — unchanged |
| W3-V · W3V2 | **ACTIVE** — unchanged |
| Phase 1 stable checkpoint | **ACTIVE** — unchanged |
| **Global Palette Refresh** | **NEXT** — discovery/charter **NOT AUTHORIZED** until operator scopes site-wide tone (not PDP-only hierarchy) |
| W3VIS-01A / 01B re-execution | **NOT AUTHORIZED** |
| Production | **FORBIDDEN** |

---

## Recommended next steps

1. **Global Palette Refresh** — new discovery scoped to site-wide color/tone tokens (`:root`, surfaces, typography rhythm) without PDP hero restructuring.
2. Issue separate write charter + CR for palette wave; do **not** re-apply rolled-back W3VIS-01A/01B diffs.
3. Operator visual spot-check on PDP (used + new) to confirm hero matches pre-W3VIS expectation.
4. Preserve W3UX-C1 density on `/cars/` during any future CSS waves — append-only discipline.

---

## Decision record

| Field | Value |
|-------|--------|
| Decision | **PASS** |
| Date | 2026-06-09 |
| Wave | W3VIS-01A + W3VIS-01B — **ROLLBACK** |
| Tier | T1 |
| Backup used | `pre-w3vis-01a-20260609-0517` |
