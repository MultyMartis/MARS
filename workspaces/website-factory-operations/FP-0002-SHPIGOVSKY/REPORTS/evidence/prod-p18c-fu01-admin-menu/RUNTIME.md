# RUNTIME STATE — P18C-FU01

| Surface | State |
|---------|--------|
| SMTP | **NOT CONFIGURED** |
| Password | not stored |
| Mail suppression | **ON** (`MailOps::should_suppress`, `pre_wp_mail` present) |
| Delivery active | 0 |
| Indexing | **CLOSED** `blog_public=0` |
| robots (WP origin) | `User-agent: *` / `Disallow: /` |
| Form persist | accepted; `MAIL_SUPPRESSED`; QA row deleted |
| Public apex | still observed as legacy Craftum (unchanged launch tail) |

Dashboard: **SMTP SETTINGS READY — CREDENTIALS REQUIRED** is now valid because the Admin page is discoverable.
