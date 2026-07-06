# FP-0002 V9-06E10 Operator Screenshot Diff Analysis v1

**Route focus:** `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`  
**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/operator-screenshot-diff-analysis.json`

## Operator evidence

Operator supplied `вёрстка.png` (static V9) and `Вордпресс.png` (WP runtime) via Web-GPT chat. **Not found in local workspace** at audit time. Fresh E10 screenshots captured under `validation/v9-06e10-full-backup-wp-port-root-cause-audit/screenshots/`.

## Structural comparison (E10 read-only probe)

| Metric | Static V9 dist | WordPress runtime |
|--------|----------------|-------------------|
| Main section/nav class stack | 18 items, ordered | 18 items, **same order** |
| Missing sections | — | None at class level |
| Extra sections | — | None at class level (breadcrumbs/subnav are nav, present in both) |

**Critical finding:** Operator visual drift is **not explained by missing/extra section classes**. Drift is explained by **inner markup differences** inside matched sections — especially home partials reused on the alcohol leaf stack.

## Likely visual drift sources

| Area | Static V9 | WordPress | Difference | Likely source |
|------|-----------|-----------|------------|---------------|
| Specialists / reviews / comfort | Service-leaf section ids and copy from `specialists.html`, `reviews.html`, `comfort.html` | Same section classes via `template-parts/home/*` | Home context defaults, slider vs static markup | `alcohol-stack.php` home partial includes |
| Program block | V9 fixture lorem + 4 image cards | Same fixture via `v9-static-content.php` | Operator may perceive lorem as "wrong content" | Static + WP both use fixture |
| Signs / FAQ | Static partial copy | ACF seed or helper fallback may differ | Text/layout drift | D8-C seed + `service/signs.php`, `service/faq.php` |
| Hero / intro | Static hero copy | ACF hero_media + alcohol fallbacks | Image/title source mix | E7B hero seed + `inner-hero.php` |
| Overall architecture | Direct HTML includes | PHP orchestration + helpers | Cumulative micro-differences | D7-D semantic port model |

## Conclusion

E9 DOM-level PASS was **insufficient**. Operator concern is **validated**: WP is not a pixel/HTML-faithful port of static V9 even when section stacks align.
