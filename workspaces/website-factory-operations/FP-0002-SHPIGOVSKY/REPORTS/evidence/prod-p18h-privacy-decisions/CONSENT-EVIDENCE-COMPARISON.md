# Consent Evidence Model — Comparison

**Current production:** browser-only (`fp02_cookie_consent` first-party cookie)

| Model | Evidentiary value | Data minimization | Privacy impact | Retention burden | Cost | New PD risk | Legal certainty |
|-------|-------------------|-------------------|----------------|------------------|------|-------------|-----------------|
| **A Browser-only** | Proves choice on device; weak if cookie cleared | **High** | **Lowest** | Cookie lifetime only | **Low** | **None added** | Sufficient for many operators; Art. 9 confirmation is operator-process question |
| **B Server event log** | Stronger audit trail | Low | Stores consent events (may be PD if tied to IP/UA) | Requires retention policy for log | Medium | **Creates new PD processing** | Not mandated for this analytics model in bounded review |
| **C Hybrid** | Mixed | Medium | Medium | Two systems | High | Partial | Overkill unless legal requires |

## Recommendation

**browser-only** — retain current architecture.

152-FZ Art. 9 requires ability to confirm consent when consent is the basis; it does **not** prescribe server-side storage in bounded primary-source review. Additional server logging would increase personal-data surface without proven necessity.

**CONSENT EVIDENCE MODEL RECOMMENDATION GROUNDED IN AUTHORITATIVE EVIDENCE**

Deferred: optional minimal server log (consent version + timestamp hash, no IP) only if operator/legal requires stronger posture.
