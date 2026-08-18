# FP-0002 — `.htaccess` ownership and legacy redirects v1

**Wave:** PROD-P17 CONT1  
**Charter override:** P01/P02 protected-zone default «never agent-edit `.htaccess`» is **narrowly lifted** for the approved legacy-redirect block only.

---

## Canonical owner

| Layer | Owner |
|-------|--------|
| Custom FP-0002 redirect **fragment** | **SOURCE** — `DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment` |
| Full production `.htaccess` | **RUNTIME / PRODUCTION-OWNED** — Beget `public_html/.htaccess` |
| WordPress markers `# BEGIN WordPress` … `# END WordPress` | **WordPress-managed** — do not put custom rules inside |

The full file is **not** stored under `WORDPRESS/` (WordPress regenerates its section). Ambiguous production-only redirects are forbidden: the seven rules live in the fragment **and** in production, byte-identical as a block.

Token: `LEGACY REDIRECT CONFIG HAS A CANONICAL OWNER`

---

## Production facts (CONT1)

- Pre-change SHA-256: `eb8dff1ac965306bd374b5604032c0f1ee51a35f209fc18ee5878250f7258bf6`
- Snapshot: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-cont1-layer-b-pre\htaccess.production.before`
- Post-change SHA-256: `ec8f06028d3ecde7442701ed09fce3aa107fc74a41434647e413f4a0088d9f38`
- WordPress section preserved byte-for-byte after the custom block
- Targets are **path-relative** (current host `shpigovsky.beget.tech`; future host inherits the same paths)

---

## Rollback

Restore `htaccess.production.before` to `public_html/.htaccess`.
