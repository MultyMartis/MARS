# UTM Session Storage — Runtime Analysis

**Implementation:** `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js` — `readUtmState()`

## Technical facts

| Property | Value |
|----------|--------|
| Storage API | `window.sessionStorage` |
| Key | `fp02_utm` |
| Value format | JSON object |
| Allowed keys | `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` |
| Max length per value | 120 characters (`String(value).slice(0, 120)`) |
| Lifetime | Browser session (tab/sessionStorage semantics) |
| Population | URL query params on page load; merged into stored object |
| Leaves browser? | **Yes** — on form submit via hidden fields → backend → `wp_fp02_form_leads` columns |
| Personal data? | Not designed for PII; arbitrary query strings truncated/bounded; marketing attribution |
| Cookie Policy | §2.3 documents behavior |

## Classification

- **Purpose:** functional attribution for inbound consultation requests within session
- **Cookie Policy disclosure:** **FACTUALLY CORRECT** (present)
- **Privacy Policy disclosure:** generic analytics/cookie reference — sufficient at high level; optional cross-link only
- **Sanitization:** whitelist keys + 120-char cap — adequate for current threat model

## Recommendation

**UTM SESSION STORAGE TREATMENT IS FACTUALLY DEFINED**

No code change required in P18H. Optional future hardening: reject non-printable characters in UTM values (not proven necessary).
