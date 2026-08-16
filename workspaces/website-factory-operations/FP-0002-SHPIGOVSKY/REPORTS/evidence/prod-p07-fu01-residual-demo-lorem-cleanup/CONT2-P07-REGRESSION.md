# PROD-P07-FU01-CONT2 — P07 regression smoke

All routes HTTP **200**. No PHP notices. CSS/JS not redeployed (P07 visual layer unchanged).

| Route | Result |
|-------|--------|
| `/uslugi/zavisimosti/` | 200; approach cards `.service-subdivision-team-stats-v1__approach-card` ×3; stages CTA «Остались вопросы?»; Guest Visit later on page |
| `/o-centre/programma-lecheniya/` | 200; `generic-content-page` long-form ACF SoT + `__reusable` block |
| `/o-centre/` | 200; `program-approach-band` visible |
| `/` | 200; out-of-scope `demo-pagination-article-*` slugs **unchanged** (not this wave) |
| `/kontakty/` | 200 |

Guest Visit contextual CTA on alcohol / comfort / guest helper: **preserved**.  
Generic «Остались вопросы?» on subdivision stages: **preserved**.  
Desktop program-card 2×2 alignment: **preserved** (screenshot).  
Mobile card flow: **preserved** (no overflow, no malformed cards).
