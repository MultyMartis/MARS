# FP-0002 — Architecture Decision Journal

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Format:** ADR (Architecture Decision Record)  
**Created:** 2026-06-11  
**Updated:** 2026-08-20 (P18H privacy/retention decisions)

---

## Purpose

Journal for **operator-declared** architectural and production decisions during the Factory track.

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
