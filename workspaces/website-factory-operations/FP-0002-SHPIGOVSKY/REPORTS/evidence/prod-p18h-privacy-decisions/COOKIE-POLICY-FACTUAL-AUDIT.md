# Cookie Policy — Factual Audit vs Live Runtime

**Page:** `/cookie-files-policy/` (ID 24)  
**Live fetch:** 2026-08-19  
**Editorial:** Olya/Admin production DB — unchanged in P18H

## Statement audit

| Topic | Classification | Notes |
|-------|----------------|-------|
| `fp02_cookie_consent` first-party cookie + record fields | **FACTUALLY CORRECT** | Matches `PrivacyConsent::COOKIE_NAME` and `build_record_for_state()` |
| Metrika consent-gated load | **FACTUALLY CORRECT** | Public pages show no Metrika loader without consent |
| Form Metrika goals consent-gated | **FACTUALLY CORRECT** | `v9-shell.js` + `PrivacyConsent` API |
| «Настройки cookie» reopen | **FACTUALLY CORRECT** | Present on public pages |
| Form personal-data consent separate | **FACTUALLY CORRECT** | Separate checkbox + `/consent-personal-data/` |
| `sessionStorage['fp02_utm']` + five UTM keys | **FACTUALLY CORRECT** | Matches `readUtmState()` in `v9-shell.js` |
| Session UTM not storing name/phone/email | **FACTUALLY CORRECT** | Only whitelisted keys, 120-char slice |
| Contact map not auto-embedded | **FACTUALLY CORRECT** | Runtime behavior |
| Legal finality / operator sign-off | **LEGAL REVIEW NEEDED** | Factual copy aligned; counsel sign-off still open |
| Named Metrika cookie inventory (`_ym_uid`, etc.) | **GENERIC** | Policy describes behavior; optional future enhancement to name provider cookies explicitly — not a runtime mismatch |

## Cookie Policy final status

**Classification: B — FACTUALLY COMPLETE / OPERATOR-READY**

**Legal sign-off:** **PENDING FINAL LEGAL REVIEW** (wording interpretation, not factual/runtime gap)

**Action:** No bounded factual rewrite required in P18H. Operator/legal may approve as-is or add provider cookie names in a future editorial pass.

**COOKIE POLICY FINAL STATUS EXPLICITLY CLASSIFIED**

**CURRENT LEGAL COPY FACTUALLY MATCHED AGAINST LIVE RUNTIME**
