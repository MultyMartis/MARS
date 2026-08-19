# FP-0002 — Architecture Decision Journal

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Format:** ADR (Architecture Decision Record)  
**Created:** 2026-06-11  

---

## Purpose

Journal for **operator-declared** architectural and production decisions during the Factory track.

This file is **not** a substitute for Playbook 04 declarations (POC-06) or Engine state indexes. ADRs here capture rationale; authoritative Factory truth lives in the RT-G04 substrate after onboarding.

---

## ADR template

Each decision uses the following structure:

```markdown
### ADR-XXX — [Short title]

**Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-YYY]

**Decision:**  
[What was decided.]

**Reason:**  
[Why this decision was made.]

**Evidence:**  
[Evidence references — EV-*, AT-*, file paths, operator attestation.]

**Impact:**  
[What this affects — scope, lanes, dependencies, SAFE UNKNOWN resolution.]
```

---

## Decisions

### ADR-001 — Cookie consent evidence store remains browser-foundation-only in P18E-A/B

**Status:** Accepted

**Decision:**  
P18E-A/B implements the browser consent-state foundation only. No new server-side visitor-consent evidence table, audit stream, or shadow tracking store is introduced in this wave.

**Reason:**  
Fresh legal/provider recheck did not surface a direct blocker that would force immediate server-side consent evidence for this specific site. The approved architecture already marked evidence storage as a legal/operator decision gate, and the current wave was explicitly bounded to foundation work without expanding tracking scope.

**Evidence:**  
`REPORTS/evidence/prod-p18e-ab-consent-foundation/LEGAL-PROVIDER-RECHECK.md`  
`REPORTS/evidence/prod-p18e-ab-consent-foundation/POST-DEPLOY-QA.json`

**Impact:**  
`PrivacyConsent` owns machine state, version, browser contract, Admin settings, and integration mapping. Future server-side evidence retention, retention windows, and related privacy policy wording remain open decisions.

### ADR-002 — Consent lifetime defaults to configurable product value, not legal hardcode

**Status:** Accepted

**Decision:**  
The consent lifetime is implemented as a bounded configurable Admin value with default `365` days, explicitly treated as a product default rather than a legal requirement.

**Reason:**  
The approved P18E design left lifetime as a product/legal policy decision. Shipping a configurable bounded value lets the foundation work proceed without hardcoding legal copy or pretending a statutory period exists.

**Evidence:**  
`REPORTS/evidence/prod-p18e-ab-consent-foundation/ADMIN-SAVE.json`  
`REPORTS/evidence/prod-p18e-ab-consent-foundation/POST-DEPLOY-QA.json`

**Impact:**  
Future legal/operator review can change the value without re-architecting the consent module or public UI.

---

## Index

| ADR | Title | Status |
|-----|-------|--------|
| ADR-001 | Browser-only consent evidence in P18E-A/B | Accepted |
| ADR-002 | Configurable consent lifetime default | Accepted |

---

*Append-only discipline recommended. Supersede, do not silently overwrite.*
