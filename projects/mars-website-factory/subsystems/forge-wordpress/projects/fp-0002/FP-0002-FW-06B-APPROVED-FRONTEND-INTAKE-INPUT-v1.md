# FP-0002 — FW-06B Approved Frontend Intake Input v1

**Version:** v1 | **Date:** 2026-06-23  
**Prerequisite:** FP-0002 Frontend Production Pass + operator visual approval

---

## Foundation status

Local WordPress foundation on `MLI-WP-FP0002-LOCAL` is **ready to receive** approved frontend. FW-06B **not executed**.

---

## FW-06B prerequisites

1. **Production Pass issued** for `workspaces/fp-0002-shpigovsky-v6/`
2. Operator final visual approval recorded
3. Approved commit/hash frozen in handoff manifest
4. No blocking SAFE UNKNOWN on forms, legal IA, messenger URLs

---

## Handoff manifest (to produce at FW-06B)

- Page list with static build evidence
- Block inventory → template partial map
- Asset manifest (fonts WOFF2, images, SVG policy)
- JS module inventory + data-attribute hooks
- Form endpoints + captcha decision

---

## Theme integration plan (outline)

1. Copy approved assets per media policy — not `dist` as SoT without charter
2. Port partials from V6 `src/partials/` to `theme-source/shpigovsky/template-parts/`
3. Port SCSS build pipeline per Forge Gulp integration model
4. Activate production templates per page type
5. Visual regression against Production Pass screenshots

---

## ACF finalization

- Resolve global options groups
- Section fields only after block mapping approved
- JSON sync via `WORDPRESS/acf-json/`

---

## Runtime target

```text
URL: http://shpigovsky.test
Runtime ID: MLI-WP-FP0002-LOCAL
Reset baseline: foundation-001
```

---

## Operator gates

1. Review foundation report
2. Approve FW-06B charter
3. Approve first integrated page/block
4. Rollback plan acknowledged (`RESET-FP-0002`)

---

## Rollback

Pre-integration state restored via `reset-to-foundation.ps1` + brain theme/plugin source revert.

---

*FW-06B intake input — issued because foundation is ready.*
