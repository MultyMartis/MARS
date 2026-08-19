# Decision Matrix — FP-0002 PROD-P18H

| Decision | Current state | Legal/regulator evidence | Technical fact | Recommendation | Risk | Auto-resolve? | Operator required? | Proposed final |
|----------|---------------|--------------------------|----------------|----------------|------|---------------|-------------------|----------------|
| **A Cookie Policy** | Live page matches P18E-F factual runtime copy; legal sign-off pending | 152-FZ disclosure principles; no exact cookie-policy template in law | Consent UI, Metrika gating, UTM, reopen — all deployed | **FACTUALLY COMPLETE**; proceed to legal sign-off | Low factual; medium if signed without counsel | **Yes** (factual) | **Yes** (legal sign-off only) | Status **B** + legal review |
| **B Consent evidence** | Browser-only `fp02_cookie_consent` JSON cookie | Art. 9 confirmation burden exists; no statute mandating server DB for this analytics model | No server consent DB; Admin shows deferred model | **browser-only**; document optional minimal server log as future upgrade only if legal demands | Medium if challenged without server log; low if policy+UI accurate | **Yes** | No (unless legal rejects browser-only) | **browser-only** |
| **C Consent lifetime** | Admin `consent_lifetime_days=365` | No mandatory exact period in bounded 152-FZ review | `PrivacyConsent` min 30 / max 730; version re-prompt implemented | **365 days** + re-prompt on version/expiry/tamper/new provider | Low | **Yes** | No | **365 days** |
| **D UTM sessionStorage** | `fp02_utm` in sessionStorage; submitted with leads | Disclosure required when storage affects user-visible processing — covered in Cookie Policy §2.3 | Keys: utm_* (5); max 120 chars; session lifetime; copied to lead row on submit | **Disclose in Cookie Policy (done)**; treat as attribution/functional session data | Low | **Yes** | No | **Disclosed + bounded session attribution** |
| **E Lead retention** | `lead_retention_days=0` (no auto-delete) | Art. 5 p.7 purpose limitation; no universal statutory day count | Table `wp_fp02_form_leads`; fields include PII + UTM + delivery state | **730 days** default policy; operator sets Admin value; **no historical purge in P18H** | Medium if left at 0 indefinitely; low with documented 730 + Privacy Policy alignment | **Yes** (recommendation) | **Yes** (apply Admin value + Privacy Policy retention sentence) | **730 days recommended; production config stays 0 until operator applies** |

## Re-prompt triggers (Decision C)

- `consent_version` increase in Admin
- Record older than `consent_lifetime_days`
- Invalid/tampered JSON in cookie
- Material new analytics provider or purpose (manual version bump)

## Lead retention semantics (Decision E)

- **Purpose:** inbound request handling, operational follow-up, dispute/quality review
- **Auto-delete:** only when `lead_retention_days > 0` and cron/job implemented (future); P18H does not enable
- **QA rows:** exclude from business retention where `is_qa=1` (manual cleanup allowed)
- **Aggregates:** anonymized counts may remain after row deletion (not implemented yet)
- **Privacy Policy:** section «неограничен» should be aligned when retention is applied — **operator/legal**
