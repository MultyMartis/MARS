# FP-0002 V9-04 ACF Ownership and Sync Policy v1

**Date:** 2026-07-02

- **Source of truth:** Git-tracked `acf-json/` in theme
- **Registration:** theme `inc/acf-json.php` load/save paths
- **UI creation:** allowed in local dev; export to JSON before commit
- **Field keys:** stable — never regenerate keys on production
- **Pro requirement:** evaluate before repeater-heavy groups finalized
- **No runtime creation in V9-04**
