# FWS-0001 — ACF Compatibility Live Validation v1

**Document type:** ACF compatibility validation report  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R  
**Runtime:** MLI-WP-SYN-001

---

## ACF profile

| Field | Value |
|-------|-------|
| **Plugin** | Advanced Custom Fields (Free) |
| **Version** | 6.8.4 |
| **JSON sync path** | `wp-content/acf-json/` |
| **Field groups discovered** | **3** |

---

## Checks

| ID | Check | Result |
|----|-------|--------|
| ACF-01 | Plugin active | **PASS** |
| ACF-02 | JSON field groups load from acf-json | **PASS** — 3 groups |
| ACF-03 | Field groups attach to expected post types | **PASS** |
| ACF-04 | Options page (if designed) | **PASS WITH LIMITATION** — Settings API deviation documented in FW-05 |
| ACF-05 | ACF Pro features required | **N/A** — Free tier by design |

---

## Field groups (summary)

Three field groups synced from `acf-json` — no sync conflicts observed on live runtime.

---

## Limitations

- ACF Pro not available on MLI synthetic profile; Free + Settings API fallback remains documented deviation.
- Full options-page editor walkthrough not separately recorded in this pass.

---

## Verdict

**PASS WITH DOCUMENTED LIMITATIONS** — ACF Free compatibility proven for FWS-0001 synthetic case.

---

## Related

- [FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md](FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md)
- [FWS-0001-FW-V-03-WORDPRESS-CORRECTNESS-LIVE-v1.md](FWS-0001-FW-V-03-WORDPRESS-CORRECTNESS-LIVE-v1.md)

---

*ACF compatibility live validation v1 — FWS-0001.*
