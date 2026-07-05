# FP-0002 V9-06D9D ACF Admin Editability Follow-up Map v1

**Date:** 2026-07-05

D9-D uses static V9 fallbacks. D9-E should wire ACF/options per area.

| Area | D9-D | Future | Wave |
|------|------|--------|------|
| Hero media/title | STATIC_OK | ACF_IMAGE_FIELD, ACF_TEXT | D9-E |
| Recovery intro | STATIC_OK | ACF_TEXT_FIELD | D9-E |
| Founder quote | STATIC_OK | ACF_IMAGE_FIELD | D9-E |
| Gallery | STATIC_OK | ACF_REPEATER | D9-E |
| Reviews | STATIC_OK | ACF_REPEATER | D9-E |
| Articles | STATIC_OK | WP_POST_QUERY | D9-E |
| Footer contacts | STATIC_OK | WP_MENU_OR_OPTION | D9-E |

Evidence: `validation/v9-06d9d-home-main-footer-static-v9-transplant/acf-admin-editability-followup-map.json`
