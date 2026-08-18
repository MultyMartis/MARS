# Forge WordPress — ADR pack (production, FP-0002-derived) v1

**Date:** 2026-08-18  
**Format:** concise ADR. Status: ACCEPTED unless noted.  
**Caveat:** one production case — optional modules remain WITH CAVEATS / J.

---

## ADR-P01 — Dedicated CPT vs generic Page

**Context:** Hub URL looks hierarchical; child Pages seem enough.  
**Decision:** If independent lifecycle + Admin list + template + search/sitemap type → CPT; keep hub as Page; `has_archive=false`.  
**Consequences:** Migration must preserve IDs/URLs.  
**See:** [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md)

## ADR-P02 — Native permalink UI

**Context:** Editors need slug control on CPTs.  
**Decision:** WordPress native permalink row only.  
**Rejected:** Custom slug metabox / cloned sample HTML.  
**See:** AP-002; P13-FU01

## ADR-P03 — Site Settings source of truth

**Context:** Header/footer/mobile/contacts duplicated.  
**Decision:** One options SoT; templates consume helpers.  
**See:** [SITE-SETTINGS](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md)

## ADR-P04 — Render-time typography

**Context:** Russian NBSP/quotes needed.  
**Decision:** One HTML-aware render-time owner; no mass DB rewrite.  
**See:** [TYPOGRAPHY](../standards/FORGE-WORDPRESS-TYPOGRAPHY-PIPELINE-STANDARD-v1.md)

## ADR-P05 — Native WP sitemap extension

**Context:** Need Google/Yandex XML.  
**Decision:** Extend `wp_sitemaps_*`. Do not invent a Yandex page/service feed.  
**See:** [SEO](../standards/FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md)

## ADR-P06 — Dedicated Activity Log table

**Context:** Need editor audit without post revisions noise.  
**Decision:** Custom table; suppress autosave; no full content.  
**See:** [ACTIVITY-LOG spec](../standards/FORGE-WORDPRESS-ACTIVITY-LOG-MODULE-SPEC-v1.md)

## ADR-P07 — Dashboard widget for operational status

**Context:** Env/debug notices on every Admin screen.  
**Decision:** One Dashboard widget; no global developer notices.  
**See:** [ADMIN-UX](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md)

## ADR-P08 — Explicit production drift canonization

**Context:** Operators edit CSS on production.  
**Decision:** Intake+hash+classify+canonize before next deploy.  
**See:** [AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md)

## ADR-P09 — Exact-file deploy

**Context:** Shared hosting; operator drift; dirty monorepo.  
**Decision:** Allowlisted files only; SHA before/after.  
**See:** [DEPLOY SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-DEPLOYMENT-SOP-v1.md)

## ADR-P10 — Indexing gate after SMTP

**Context:** Temporary host can look “done”.  
**Decision:** Indexing opens only after HTTPS, canonical, sitemap-final, smoke, Admin, forms, SMTP, redirects.  
**See:** [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md)

## ADR-P11 — Physical-device acceptance

**Context:** iOS compositor bugs pass in Chrome emulation.  
**Decision:** Physical iPhone/Android/trackpad gates for device-specific behavior.  
**See:** [REAL-DEVICE-QA](../standards/FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md)

---

*ADR pack v1. Historical FW-01 ADRs remain in [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md).*
