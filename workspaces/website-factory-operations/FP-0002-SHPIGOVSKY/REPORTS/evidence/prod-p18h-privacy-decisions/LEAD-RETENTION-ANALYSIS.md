# Lead Retention Analysis

**Current config:** `lead_retention_days = 0` (auto-deletion **disabled**)

## Stored lead fields (schema v1)

`visitor_name`, `phone`, `email`, `message`, `source_url`, `source_path`, `utm_*`, `referrer`, `delivery_status`, `smtp_status`, `created_at`, `is_qa`

## Processing purposes

1. Processing inbound consultation requests (primary)
2. Operational follow-up by clinic staff
3. Delivery troubleshooting (SMTP status, error codes)
4. Limited operational history / dispute response

## Legal basis (152-FZ Art. 5 p.7)

- No universal “730 days” or “365 days” statute for consultation web forms
- Storage must be limited to stated purposes
- Indefinite retention without documented purpose is **not** a neutral default (**REGULATOR signal**)

## Recommended FP-0002 default

**730 days (2 years)**

**Rationale:**

- Covers typical operational follow-up and civil claim limitation planning horizon (3-year general limitation — 730 is conservative-minimal middle ground)
- Aligns with purpose limitation better than `0` (indefinite)
- Less aggressive than 1095 for a healthcare-adjacent contact form context
- Allows operator to shorten to 365 if legal prefers

## Implementation policy (P18H)

| Rule | P18H action |
|------|-------------|
| Set Admin `lead_retention_days` | **Prepare only** — document 730; production stays **0** until operator saves |
| Purge historical leads | **FORBIDDEN** in P18H |
| Privacy Policy «неограничен» | Flag for operator/legal alignment when retention enabled |
| QA leads (`is_qa=1`) | Manual exclusion from business retention policy |

**FORM LEAD RETENTION RECOMMENDATION PRODUCED**

**NO HISTORICAL REAL LEADS DELETED WITHOUT EXPLICIT AUTHORITY**
