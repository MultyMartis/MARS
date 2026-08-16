# PROD-P12 — Operator/Olya production preservation

## Operator fresh Beget backup

**ACKNOWLEDGED** — operator-provided full Beget backup created immediately before PROD-P12.

Exact-file / exact-object rollback still used for every mutation.

## File drift intake

- Inspected **21** source-owned production files (theme+plugin).
- Drift vs local: **1** file — `assets/css/v9-style.css` (1 trailing-byte operator drift).
- Canonized: production bytes → local source (`SHA256 4CC114FD…` then P12 additive phone-note selectors).
- Lifebuoy CSS/JS matched local pre-P12 (no operator lifebuoy overrides in `v9-style.css`).

OPERATOR PRODUCTION FILE DRIFT INTAKE COMPLETE  
OPERATOR CSS/FILE DRIFT PRESERVED AND CANONIZED

## Olya Admin/content

- Fresh DB read for post `#73` nature metas before any content mutation.
- `section_nature_text_blocks` repeater = **empty** (Admin SoT).
- Legacy dormant metas still contained demo headings (`Нейробиология`, `Генотипирование`, link label) — **not deleted**.
- P12 stopped FE fallthrough to legacy metas; legacy rows remain in DB.
- No broad ACF option sync; no demo re-seed; no mass postmeta overwrite.
- CTA option `cta_band_phone_hint` left as Admin-owned; hub templates stopped forcing empty hint.

OLYA CURRENT ADMIN/CONTENT STATE PRESERVED  
OPERATOR/OLYA CURRENT PRODUCTION STATE PRESERVED
