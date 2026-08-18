# WP Forge — Redirect manifest template v1

Project:  
Host at rule install:  
Final host (do not hardcode until live):

| # | Match path (exact) | Trailing slash variant | Target (path-relative unless post-cutover) | Query | Notes |
|---|--------------------|------------------------|--------------------------------------------|-------|-------|
| 1 | /old-path | yes | /new-path | preserve | |
| 2 | | | | | |

**Negative tests:** prefixes that must 404 / not redirect.

**Placement:** before WordPress rewrite block.

**Post-cutover:** optional host-conditional 301 from temporary host → final HTTPS URL.

Do not paste client-specific legacy lists into this template.

---

*Template v1.*
