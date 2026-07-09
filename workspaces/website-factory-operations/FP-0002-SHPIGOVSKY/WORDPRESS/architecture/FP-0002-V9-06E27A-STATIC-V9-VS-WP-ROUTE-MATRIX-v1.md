# FP-0002 V9-06E27A Static V9 vs WP Route Matrix v1

**Evidence:** `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/static-v9-vs-wp-route-matrix.json`

## Matrix summary

| Classification | Count | Notes |
|---|---:|---|
| MATCH | 12 | Canonical approved routes aligned |
| PLACEHOLDER | 17 | V9 placeholder routes with WP objects |
| STATIC_ONLY | 2 | `/uslugi/genotipirovanie/`, `/uslugi/zavisimosti/specialistam/` |
| WP_ONLY | 4 | `/glavnaya/`, `/specyalisty/`, `/o-centre/intervyu-i-smi/`, `/privacy-policy-page/` |
| OBSOLETE_CANDIDATE | 4 | Overlap with cleanup candidate pages |

## Notable gaps

- **STATIC_ONLY:** genotipirovanie not published in V9 manifest; WP page #9 returns 404.
- **STATIC_ONLY:** `/uslugi/zavisimosti/specialistam/` in V9 manifest; no WP service/page owner.
- **WP_ONLY:** Services #314–316 (narcotic, medication, behavioral dependencies) added in WP skeleton; not in static V9 manifest.
- **Route ownership:** Pages #6/#7/#8 still publish at service subdivision paths while service CPT objects exist at same URLs.
