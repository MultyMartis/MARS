# FP-0002 V9-06D.6 Integration Wave Plan v1

**Date:** 2026-07-04

Implementation waves are labeled **D7-*** (source implementation after this planning phase).

| Wave | Scope | Allowed (summary) | Runtime delivery later | DB checkpoint later | Gate |
|---|---|---|---:|---:|---|
| D7-A | Global shell and assets source integration | theme/shpigovsky/template-parts/layout/*, theme/shpigovsky/template-parts/navigation/*, theme/shpigovsky/inc/assets.php… | True | False | php lint |
| D7-B | Home template source integration | theme/shpigovsky/front-page.php, theme/shpigovsky/template-parts/home/**, theme/shpigovsky/template-parts/components/final-form.php… | True | False | php lint |
| D7-C | Services Hub template source integration | theme/shpigovsky/page-templates/services-hub.php, theme/shpigovsky/template-parts/**… | True | False | php lint |
| D7-D | Service template source integration | theme/shpigovsky/single-service.php, theme/shpigovsky/inc/service-template-loader.php, theme/shpigovsky/template-parts/service/**… | True | False | php lint |
| D7-E | Contacts template source integration | theme/shpigovsky/page-templates/contacts.php, theme/shpigovsky/template-parts/contacts/**… | True | False | php lint |
| D7-F | Runtime delivery and cross-route visual QA | manifests/packages, validation evidence, reports… | True | True | dry-run delivery |

Order rationale: unstyled chrome and missing assets block all route visuals → D7-A first.

Each wave: source-only micro-task → validation → optional runtime delivery under separate gate → rollback via source revert and runtime backup.

## Result

COMPLETE
