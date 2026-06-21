# SITE-001 W3-C Rollback Decision v1

**Type:** Post-rollback decision — W3-C Footer Reduction reversal  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`

**Inputs:** [SITE-001-W3C-ROLLBACK-PLAN-v1.md](SITE-001-W3C-ROLLBACK-PLAN-v1.md) · [SITE-001-W3C-ROLLBACK-EXECUTION-v1.md](SITE-001-W3C-ROLLBACK-EXECUTION-v1.md) · [SITE-001-W3C-EXECUTION-v1.md](SITE-001-W3C-EXECUTION-v1.md)

---

## Verdict

**PASS** — W3-C T1 rollback **COMPLETE** on TEST.

Pre-W3C visual state restored from OCPilot backup `pre-w3c-20260609-0259`. Footer, contacts, legal content, and link inventory match pre-change baseline. **7/7** verification URLs pass.

---

## Operator decision

| Field | Value |
|-------|--------|
| Rollback approved | **YES** |
| Reason | Visual direction not accepted |
| Tier executed | **T1** — incremental file restore |
| Beget global backup used | **NO** |

---

## Criteria assessment

| Criterion | Result |
|-----------|--------|
| Rollback package located | **PASS** — `pre-w3c-20260609-0259` |
| Backup integrity verified | **PASS** — manifest + 3 files + SHA-256 |
| Only W3-C scope restored | **PASS** — `footer.twig`, `main.css`, `media.css` only |
| DB / logos / SEO / YML / SMTP untouched | **PASS** |
| Caches cleared + modification refresh | **PASS** — 4/4 HTTP 200 |
| Footer restored | **PASS** — 11 080 bytes; no `wsp_footer__legal_details` |
| No broken layout | **PASS** |
| No missing links / contacts / legal | **PASS** — 89 links; all markers present |
| No PHP / Twig errors | **PASS** |
| Pre-W3C visual baseline | **PASS** — matches W3-C execution pre-change metrics |

---

## Authorization state after rollback

| Gate | Status |
|------|--------|
| W3-C execution | **ROLLED BACK** — 2026-06-09 |
| W3-C changes on TEST | **INACTIVE** |
| Phase 1 stable checkpoint | **ACTIVE** — unchanged |
| W3-A, W3-B, W3-D…F | **NOT AUTHORIZED** |
| W3-C re-execution | **NOT AUTHORIZED** — requires new operator decision + CR |
| Production | **FORBIDDEN** |

---

## Recommended next steps

1. Operator visual spot-check on desktop + mobile to confirm footer height acceptable.
2. If footer work resumes, revise W3-C approach per operator feedback; issue **new CR** (do not re-apply rolled-back diff).
3. Proceed **W3-A** (catalog tokens) or alternate Phase 2 wave per roadmap — separate authorization each.
4. Resolve **C-04** WhatsApp before any URL changes in later waves.

---

## Decision record

| Field | Value |
|-------|--------|
| Decision | **PASS** |
| Date | 2026-06-09 |
| Wave | W3-C — Footer Reduction **ROLLBACK** |
| Tier | T1 |
| Backup used | `pre-w3c-20260609-0259` |
