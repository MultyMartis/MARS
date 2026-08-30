# I-SEO Report Hub — Client Report Export Immutability Policy v0.1

**Status:** CHARTER / POLICY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

---

## 1. Core rule

**Exports are immutable once created and marked ready.**

- Do not overwrite artifact files for existing export ids.
- Do not UPDATE checksum / storage_path / file_size for issued rows to “refresh” visuals.
- Visual upgrades create a **new** export version / new id.

---

## 2. Frozen baseline (current local)

| Export id | Role | Policy |
|-----------|------|--------|
| 1 | HTML v1 | Frozen |
| 2 | PDF v1 | Frozen |
| 3 | HTML v2 styled | Frozen |
| 4 | PDF v2 styled | **Frozen** — checksum prefix `a8c4d61c6216e8d70b19`; size `117055` |

Export **4** remains the active public-share PDF baseline until an explicit share cutover charter.

---

## 3. Future visual exports

| Rule | Value |
|------|--------|
| New client-styled HTML | New export id / higher `vN` key |
| New client-styled PDF | New export id from that HTML; **never** rewrite id **4** |
| DB | INSERT only for new rows; no mutation of old rows’ file fields |
| Evidence under Storage | Not a product export; not in `report_exports` |

---

## 4. Shares

| Rule | Value |
|------|--------|
| Active share | Stays on current PDF unless operator-approved new share |
| Token print | Forbidden in docs/agent output |
| Create/revoke in Export HTML Alignment waves | Forbidden unless a later share charter says otherwise |
| Public route | Continues static PDF attachment stream |

---

## 5. What “alignment” must not do

- Regenerate export 4 “in place”.
- Point share 7 (or current active share) at a new file without a handoff charter.
- Treat Storage evidence HTML as client delivery.
- Rewrite historical HTML 1/3 to client template.

---

## 6. Rollback

If a future create wave mistakes a path: stop; do not delete foreign WIP; restore from backup/evidence; leave frozen ids intact. Preview-only code rollback does not affect issued PDFs.
