# FP-0002 V9-06D.3 Page Migration Plan v1

**Phase:** V9-06D.3 — PLANNING ONLY
**Runtime writes:** 0

## Decisions

- All page-owned V9 routes remain Pages.
- Services Hub `/uslugi/` remains **PAGE_OWNED** (ID 5).
- Front page remains Page ID 4 (`show_on_front=page`).
- Posts page remains Page ID 19.
- `/specyalisty/` Page ID 10 is **LEGACY_DEFERRED** — do not delete in D.3/D.4.
- Canonical specialist service path: `/uslugi/zavisimosti/specialistam/`.
- Legal pages are **LEGAL_DEMO** blockers for production copy.

## Page-owned routes

| ID | Path | Template | Wave | Action | Legal blocker |
|---:|---|---|---|---|---|
| 4 | / | `front-page.php` | WAVE_1_VISUAL_MINIMUM | FILL_ACF_MINIMAL | NO |
| 5 | /uslugi/ | `page-templates/services-hub.php` | WAVE_1_VISUAL_MINIMUM | FILL_ACF_MINIMAL | NO |
| 11 | /o-centre/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | FILL_ACF_FULL_LATER | NO |
| 12 | /o-centre/o-nas/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | CREATE_PLACEHOLDER_ONLY | NO |
| 13 | /o-centre/programma-lecheniya/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | CREATE_PLACEHOLDER_ONLY | NO |
| 14 | /o-centre/galereya-o-dome/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | CREATE_PLACEHOLDER_ONLY | NO |
| 15 | /o-centre/specialistam/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | CREATE_PLACEHOLDER_ONLY | NO |
| 16 | /o-centre/rodstvennikam/ | `page-templates/institutional.php` | WAVE_3_INSTITUTIONAL_CONTENT | CREATE_PLACEHOLDER_ONLY | NO |
| 18 | /otzyvy/ | `page-templates/reviews.php` | WAVE_3_INSTITUTIONAL_CONTENT | FILL_ACF_FULL_LATER | NO |
| 19 | /blog/ | `home.php` | WAVE_4_BLOG_LEGAL_REVIEW | KEEP_EXISTING | NO |
| 20 | /kontakty/ | `page-templates/contacts.php` | WAVE_1_VISUAL_MINIMUM | FILL_ACF_MINIMAL | NO |
| 3 | /privacy-policy/ | `page-templates/legal.php` | WAVE_4_BLOG_LEGAL_REVIEW | DEFER_LEGAL | YES |
| 22 | /user-agreement/ | `page-templates/legal.php` | WAVE_4_BLOG_LEGAL_REVIEW | DEFER_LEGAL | YES |
| 23 | /consent-personal-data/ | `page-templates/legal.php` | WAVE_4_BLOG_LEGAL_REVIEW | DEFER_LEGAL | YES |
| 24 | /cookie-files-policy/ | `page-templates/legal.php` | WAVE_4_BLOG_LEGAL_REVIEW | DEFER_LEGAL | YES |

## First-wave Pages

- Home (4): minimal hero + service nav + CTA
- Services Hub (5): intro + query mode + show placeholders
- Contacts (20): address + one phone + form intro

## Preserve / overwrite

- Preserve current `post_content` during WAVE_1 (foundation placeholder bodies).
- Later waves may overwrite body only when ACF-driven templates fully own presentation.
- Legal bodies must not be overwritten with DEMO tokens as production.

## Legacy / source Pages

| ID | Path/slug | Role | Action |
|---:|---|---|---|
| 6 | /uslugi/zavisimosti/ | PAGE_TO_SERVICE_SOURCE | RETIRE_AFTER_SERVICE_CONTENT_VALIDATED |
| 7 | /uslugi/psihicheskoe-zdorovie/ | PAGE_TO_SERVICE_SOURCE | RETIRE_AFTER_SERVICE_CONTENT_VALIDATED |
| 8 | /uslugi/rasstroystva-pischevogo-povedeniya/ | PAGE_TO_SERVICE_SOURCE | RETIRE_AFTER_SERVICE_CONTENT_VALIDATED |
| 9 | /uslugi/genotipirovanie/ | LEGACY_ONLY | RETIRE_AFTER_MIGRATION |
| 10 | /specyalisty/ | LEGACY_ONLY | DEFER_REDIRECT |
| 17 | /o-centre/intervyu-i-smi/ | LEGACY_ONLY | RETIRE_AFTER_MIGRATION |
| 21 | /pravovaya-informaciya-pilzovatelyu/ | LEGACY_ONLY | RETIRE_AFTER_MIGRATION |
| 25 | /privacy-policy-page/ | LEGACY_ONLY | RETIRE_AFTER_MIGRATION |

## Rollback

Restore affected Pages from pre-wave DB dump. Do not delete Pages as rollback.

## Result

COMPLETE — planning only.
