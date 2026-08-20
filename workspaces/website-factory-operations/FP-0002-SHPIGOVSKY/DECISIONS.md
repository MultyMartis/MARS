# FP-0002 — Architecture Decision Journal

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Format:** ADR (Architecture Decision Record)  
**Created:** 2026-06-11  
**Updated:** 2026-08-20 (native form anti-spam v1)

---

## Purpose

Journal for **operator-declared** architectural and production decisions during the Factory track.

---

## Decisions (Native Anti-Spam v1)

### ADR-AS-001 — First-party layered anti-spam (no external CAPTCHA)

**Status:** Accepted

**Decision:** Public lead forms use layered first-party controls (honeypot, server-signed timing, rate limit, replay/idempotency, conservative heuristics). Do **not** integrate Google reCAPTCHA, Yandex SmartCaptcha, or other external CAPTCHA providers in v1.

**Evidence:** `REPORTS/REPORT-FP-0002-PROD-MAINT-NATIVE-ANTISPAM-V1.md`

---

## Decisions (P18I)

### ADR-P18I-A — Launch closeout against live editorial truth

**Status:** Accepted

**Decision:** Final crawl and closeout use **current production DB/editorial state** after Olya/Admin edits, not a frozen implementation inventory.

**Evidence:** `REPORTS/evidence/prod-p18i-final-launch-closeout/01-olya-admin-intake.json`

---

### ADR-P18I-B — Staging URL normalization (bounded)

**Status:** Accepted

**Decision:** Rewrite legacy `shpigovsky.beget.tech` / `.test` hosts at render time via `shpigovsky_normalize_public_url()` and public HTML output buffer; do not mass-rewrite editorial DB in P18I.

**Evidence:** `REPORTS/evidence/prod-p18i-final-launch-closeout/11-deploy-fix-manifest.json`

---

### ADR-P18I-C — Maintenance transition

**Status:** Accepted

**Decision:** FP-0002 enters **PRODUCTION / MAINTENANCE** after P18I CLEAN crawl; launch runbooks stop mutating production defaults.

**Evidence:** `REPORTS/FP-0002-FINAL-LAUNCH-CLOSEOUT-v1.md`

---

## Decisions (P18H)

### ADR-P18H-A — Cookie Policy factual status

**Status:** Accepted (factual); legal sign-off pending

**Decision:** Live Cookie Policy at `/cookie-files-policy/` is **factually complete** vs current runtime. Final legal sign-off remains operator/legal.

**Reason:** P18H audit matched all consent, Metrika, UTM, and form-separation statements to deployed code.

**Evidence:** `REPORTS/evidence/prod-p18h-privacy-decisions/COOKIE-POLICY-FACTUAL-AUDIT.md`

---

### ADR-P18H-B — Consent evidence model

**Status:** Accepted

**Decision:** Retain **browser-only** consent record (`fp02_cookie_consent`). Do not add server-side consent event store in P18H.

**Reason:** 152-FZ Art. 9 confirmation burden does not mandate server DB for this analytics model in bounded review; server log adds PD surface.

**Evidence:** `REPORTS/evidence/prod-p18h-privacy-decisions/CONSENT-EVIDENCE-COMPARISON.md`

---

### ADR-P18H-C — Consent lifetime

**Status:** Accepted

**Decision:** **365 days** product lifetime; re-prompt on version bump, expiry, tampered state, or material provider/purpose change.

**Reason:** No statutory exact period; 365 matches Admin default and balances UX vs refresh.

**Evidence:** `REPORTS/evidence/prod-p18h-privacy-decisions/DECISION-MATRIX.md`

---

### ADR-P18H-D — UTM sessionStorage

**Status:** Accepted

**Decision:** Document `sessionStorage['fp02_utm']` in Cookie Policy (done); treat as bounded session attribution; submit to lead registry on form post.

**Reason:** Matches `v9-shell.js` implementation; whitelisted keys + 120-char cap.

**Evidence:** `REPORTS/evidence/prod-p18h-privacy-decisions/UTM-SESSION-STORAGE-ANALYSIS.md`

---

### ADR-P18H-E — Form lead retention

**Status:** Accepted (recommendation); production config pending operator

**Decision:** Recommend **730 days** default retention for consultation leads. P18H does **not** change production `lead_retention_days` (remains 0) and does **not** purge historical leads.

**Reason:** 152-FZ Art. 5 p.7 purpose limitation; indefinite storage is not neutral.

**Evidence:** `REPORTS/evidence/prod-p18h-privacy-decisions/LEAD-RETENTION-ANALYSIS.md`

---

## Index

| ADR | Title | Status |
|-----|-------|--------|
| P18H-A | Cookie Policy factual status | Accepted / legal pending |
| P18H-B | Consent evidence browser-only | Accepted |
| P18H-C | Consent lifetime 365d | Accepted |
| P18H-D | UTM sessionStorage disclosure | Accepted |
| P18H-E | Lead retention 730d recommend | Accepted / config pending |

---

*Append-only discipline. Supersede, do not silently overwrite.*
