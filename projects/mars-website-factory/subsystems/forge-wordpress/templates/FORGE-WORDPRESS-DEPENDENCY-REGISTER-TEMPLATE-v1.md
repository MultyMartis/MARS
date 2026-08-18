# {PROJECT-ID} — Dependency register

**Artifact ID:** DEPENDENCY-REGISTER  
**Project:**  
**Date:**  

Every production WP Forge project tracks runtime dependencies. Update when versions change. Fake versions are forbidden.

| Component | Version | Owner | Purpose | Update policy | Criticality |
|-----------|---------|-------|---------|---------------|-------------|
| WordPress | | technical operator | CMS core | [FW-RB-10](../runbooks/FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md) | critical |
| PHP | | host / operator | runtime | major = HIGH change | critical |
| Theme | | theme specialist | presentation | exact-file deploy | critical |
| Child / custom theme | | | | | |
| Custom functionality plugin | | plugin owner | business model | | critical |
| MU plugins | | operator | infrastructure-critical only | temporary-tool rows | high |
| ACF | | | fields | pin major | critical if used |
| Third-party plugins | *(one row each)* | | | | |
| External APIs | | | | | |

Also list: SMTP, cache/CDN, analytics IDs (not secrets), WPilot.

---

*Template v1 — see PLUGIN-GOVERNANCE and CHANGE-RELEASE versioning.*
