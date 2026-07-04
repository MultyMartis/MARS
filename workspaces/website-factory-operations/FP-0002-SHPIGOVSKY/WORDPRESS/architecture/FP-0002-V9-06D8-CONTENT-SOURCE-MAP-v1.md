# FP-0002 V9-06D8 Content Source Map v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8-content-seed-planning/content-source-map.json`

**V9 static root:** `workspaces/fp-0002-shpigovsky-v9/src/`  
**V9 dist root:** `workspaces/fp-0002-shpigovsky-v9/dist/`

---

## Source classification key

| Code | Use |
|---|---|
| V9_STATIC_SOURCE | HTML partials/pages in V9 src |
| V9_DIST_TEXT | Rendered text from dist (secondary) |
| EXISTING_WP_TITLE | post_title / CPT query |
| EXISTING_ACF_VALUE | keep D4 minimal seed |
| STATIC_FALLBACK_ALREADY_IN_TEMPLATE | theme partial without ACF |
| SITE_OPTION_REQUIRED | D8-A options |
| OPERATOR_SUPPLIED_REQUIRED | real org data |
| MEDIA_REQUIRED | upload wave |
| DEFERRED | post-MVP |
| DO_NOT_SEED | no ACF / blocked |

---

## Summary by area

| Area | Source candidates | Operator needed | Media needed | Do not seed |
|---|---|---:|---:|---|
| Site Options | V9 kontakty + header; **operator phones/email** | yes | no | consent ref until legal |
| Home hero/CTA | V9 `index.html`, final-form partial | no | hero images | — |
| Home advantages/FAQ | V9 `home-why-us`, `home-faq` sections | no | gallery images | reviews/blog |
| Services Hub | V9 `uslugi-v2.html` | no | category heroes | genotyping block |
| Service 74 | V9 `usluga-konechnaya-v1.html` | **medical review** | hero image | invented claims |
| Services 73/77/84 | V9 subdivision/placeholder pages | **clinical scope** | optional | — |
| Contacts | V9 `kontakty.html` | **phones, map URL** | map/rehab photo | live endpoint |
| Shared blocks | theme static only | no | various | all unmapped blocks |

---

## V9 reference snippets (short)

- **Home CTA title:** «Остались вопросы?» — `index.html` final-form (`headingText`).
- **Home CTA text:** «Опишите вашу ситуацию…» — same section (`leadText`).
- **Hub intro:** shortened from `uslugi-v2.html` hero lead (already in D4 seed).
- **Service 74 signs/programme:** map from `usluga-konechnaya-v1.html` section partials — **operator must approve medical wording**.

---

## Placeholder / demo content warning

D4 minimal seed includes explicit «минимальное наполнение» markers. D8 waves should replace markers with V9-derived copy but flag **production_final: false** until operator sign-off.

Do **not** invent legal identifiers, license numbers, or clinical claims.

---

## Result

**COMPLETE**
