# Failures and Fixes v1

**Source:** ORCA Battle Pilot — Triumph Manipulator Search PPC  
**Date:** 2026-05-30

---

## Failure register

| # | Failure | Severity | Version fixed | Status |
|---|---------|----------|---------------|--------|
| F1 | Keyword×ad row multiplication → duplicate ads | **Critical** | v1.2 | **Fixed** |
| F2 | Legacy slug URLs (not `.html`) | **Critical** | URL sync | **Fixed** |
| F3 | Cross-negative wildcards rejected by Commander | **Critical** | v1.4 | **Fixed** |
| F4 | Promotion URL = first group landing (not root) | **High** | v1.4 | **Fixed** |
| F5 | Bids not visible until strategy UI setup | **High** | Documented | **Mitigated** (checklist) |
| F6 | Budget / schedule not in XLSX | **Medium** | Documented | **Accepted limit** |
| F7 | Legacy `gruzotaxi-triumph.ru` hygiene tails | **Medium** | Hygiene audit | **Fixed** |
| F8 | Stale template rows from prior exports | **Low** | v0 cleanup | **Fixed** |
| F9 | Metadata diff vs template (1 cell) | **Low** | v1.4 | **Fixed** |

---

## F1 — Duplicate ads (keyword×ad bug)

**Symptom:** Commander showed 108 ad-equivalent rows instead of 20. Same ad repeated per keyword.

**Root cause:** `mapTemplateFillRows()` nested loops — Source C in [DUPLICATE-ADS-AUDIT-v1.md](../commander-url-sync-v1/DUPLICATE-ADS-AUDIT-v1.md).

**Fix:** Transport split v1.2 — separate AD rows (20) and KEYWORD rows (64).

**Verification:** `validate:no-duplicate-ads-v1.2` — PASS · Commander import — PASS

---

## F2 — Legacy URLs

**Symptom:** 11/12 routes had legacy trailing-slash slug URLs, not canonical `.html`.

**Root cause:** Pre-sync JSON and exporter slug table used old URL format.

**Fix:** URL sync commit `f235bf1` — 164 string replacements in JSON, mapping.js, landing-routing-schema, draft builder.

**Verification:** URL-EXPORT-VALIDATION — PASS · Commander spot-check — PASS

---

## F3 — Cross-negative wildcard syntax

**Symptom:** Commander rejected all 12 group negatives with syntax error. Tokens like `бытовк*`, `контейнер*`.

**Root cause:** `cross-negative-matrix-v1.3.js` used wildcard stems assuming regex-like matching.

**Fix:** v1.4 — `COMMANDER_NEGATIVE_FORBIDDEN_RE` bans `*`; stem expansion to full word forms; phrase-level route discriminators.

**Verification:** `commander_negative_syntax_pass` — PASS · Commander import — PASS

---

## F4 — Wrong promotion URL

**Symptom:** R11C5 pointed to `5-tonn.html` instead of site root.

**Root cause:** v1.3 derived promotion URL from first group landing.

**Fix:** v1.4 `buildTemplateFidelityMetadataPatches()` — always template root `https://manipulator-triumph.ru/`.

**Verification:** CAMPAIGN-FIDELITY-QA — PASS (0 metadata diff cells)

---

## F5 — Bids not visible post-import

**Symptom:** Keyword bid column empty in Commander UI immediately after import.

**Root cause:** Commander requires explicit campaign strategy activation; XLSX carries values but UI gate is separate.

**Fix:** Documented post-import checklist — [CAMPAIGN-SETTINGS-LAYER-v1.md](CAMPAIGN-SETTINGS-LAYER-v1.md). Operator manually activated manual bid strategy → bids appeared.

**Status:** **Mitigated** — not an exporter bug; architectural boundary.

---

## F6 — Budget / schedule not transportable

**Symptom:** No budget or schedule fields in Commander template v1.

**Root cause:** Template SoT designed for Search Manual Bids entity transport only.

**Fix:** Accepted limit + post-import checklist. Not an exporter failure.

---

## F7 — Legacy hygiene tails

**Symptom:** Old `gruzotaxi-triumph.ru` references and stale project negatives in draft history.

**Fix:** [COMMANDER-HYGIENE-AUDIT-v1.md](../ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md) — pre-export READY gate.

---

## Fix velocity summary

| Phase | Duration | Outcome |
|-------|----------|---------|
| URL sync | 1 session | 11 routes corrected |
| Transport split | 1 session | Duplicate ads eliminated |
| v1.3 launch export | 1 session | Bids + negatives added |
| v1.4 syntax fix | 1 session | Commander import PASS |
| Post-import setup | 1 session | Bids visible, strategy confirmed |

---

## Residual risks

| Risk | Mitigation |
|------|------------|
| Over-minus from expanded stems | Human search terms review after 2–4 weeks |
| Morphological coverage gaps (Russian) | Operator trim post-import |
| Live CPC vs 400–600 ₽ default | Market calibration — SAFE UNKNOWN |
| Re-import drift if JSON edited | Re-run full validation + export pipeline |
