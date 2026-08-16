# PROD-P07-FU01 / CONT2 — Mutation map

## Production (CONT2)

| Kind | Count | Note |
|------|-------|------|
| Production file writes | **3** | Exact SFTP put of the three theme `inc/*.php` files only |
| DB/Admin writes | **0** | `NO DB/ADMIN MUTATION — HISTORICAL NON-RENDERED PLACEHOLDERS LEFT UNCHANGED` |
| WPilot business writes | **0** | `write_enabled=false` |
| Theme-editor upload | not used | `DISALLOW_FILE_EDIT=true` (P04 baseline) |

Exact files:

1. `wp-content/themes/shpigovsky/inc/v9-static-content.php`
2. `wp-content/themes/shpigovsky/inc/services-hub-helpers.php`
3. `wp-content/themes/shpigovsky/inc/service-general-helpers.php`

SHA256 (local = production-after):

| File | SHA256 | bytes |
|------|--------|-------|
| `inc/v9-static-content.php` | `3471898fa12c253f97820a7c33754524d2d0e9cab1c50f2aa222755901e55604` | 29428 |
| `inc/services-hub-helpers.php` | `6e11bbc453d33f395d8bdfe7f6a00e913ce3ee0777c66d46942ff2aca391e305` | 24442 |
| `inc/service-general-helpers.php` | `b4ac89d7d9e67d7cfabe3c06b3f9ab617863b512b3e0bf210936e73b8eb74293` | 19440 |

## DB objects

**None mutated.** Historical ACF Lorem/DEMO rows may still exist in Admin and are **not** rendered on the approved FE surfaces.

## Rollback

* Layer A: operator-confirmed post-P07 Beget backup.
* Layer B CONT2: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-fu01-cont2-layer-b-pre\` (exact 3 production-before files + SHA manifest).
* Historical P07 Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-layer-b-pre\`.
