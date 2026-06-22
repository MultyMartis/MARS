# Validation Plan — {PROJECT_NAME}

**Template ID:** FW-T-16  
**Version:** v1  
**Artifact:** VALIDATION-PLAN  
**Authority:** WordPress Validator

---

## Profiles

| Profile | Value |
|---------|-------|
| production_mode | |
| a11y_profile | baseline \| enhanced |
| perf_profile | baseline \| enhanced |
| visual_threshold | TBD at pilot calibration |

---

## WV schedule

| WV | Runner | Blocking | Owner | Evidence path |
|----|--------|----------|-------|---------------|
| WV0 | wv0-manifest-lint | Yes | | |
| WV1 | wv1-architecture-compliance | Yes | | |
| WV2 | wv2-phpcs | Yes | | |
| WV3 | wv3-wp-correctness | Yes | | |
| WV4 | wv4-security-scan | Yes | | |
| WV5 | wv5-playwright-smoke | Yes | | |
| WV6 | wv6-visual-diff | Yes (PIXEL_PERFECT) | | STORAGE/.../visual-baselines/ |
| WV7 | wv7-admin-ux-review | Yes | | |
| WV8 | wv8-a11y-perf | Advisory | | |
| WV9 | wv9-package-lint | Yes | | |

---

## Viewport matrix (WV6)

| Page | 1440 | 1024 | 390 |
|------|------|------|-----|
| Home | | | |

---

## Smoke paths (WV5)

1. 
2. 

---

*Template — pilot use only.*
