# RUN-5 — Data Request (SITE-001)

**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST  
**Run:** 5 — First Read-Only Site Audit (initialization)  
**Mode:** READ ONLY — operator-supplied evidence only  
**Baseline:** `baselines/ocstore-3038-rs2/`

**Purpose:** minimum evidence set to unblock baseline comparison. Do **not** supply full site dumps unless listed below.

---

## Delivery rules

| Rule | Detail |
|------|--------|
| **No secrets in git** | Place bulk under `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` (e.g. `materials/`, `snapshots/files/`) |
| **Forbidden in any artifact** | Passwords, API keys, live `config.php` / `admin/config.php` values, session cookies, customer PII exports |
| **Sanitize** | Redact host credentials; path constants and `DB_PREFIX` only where noted |
| **Label files** | `site-001-run5-p1-<short-name>.<ext>` etc. |

Notify OCPilot with: path to external file + one-line description (no secrets in chat).

---

## Priority 1 — Blocks version check and file comparison

### P1-A — Version verification (platform + build)

| Field | Value |
|-------|-------|
| **Why needed** | Audit objective #1: confirm site is ocStore **3.0.3.8 (rs.2)** before any baseline diff. Operator brief alone is insufficient per [baseline-match-workflow.md](../../../baseline-match-workflow.md). |
| **Acceptable evidence** | (a) Sanitized excerpt: first ~30 lines of site root `index.php` and `admin/index.php` showing `VERSION` constant only; or (b) Admin login footer screenshot (version string visible, no session token); or (c) `grep`/select-string output: `define('VERSION'` from both files. |
| **Not acceptable** | Full `config.php`; unrelated controller dumps. |

### P1-B — OpenCart root layout confirmation

| Field | Value |
|-------|-------|
| **Why needed** | Baseline uses package root `admin/`, `catalog/`, `system/`, `image/`, `index.php`. Live sites may relocate `storage/` or remove `install/`. Wrong root → false diffs. |
| **Acceptable evidence** | (a) Directory listing of site document root (names only): top-level entries + whether `install/` exists; or (b) Sanitized note: web root path on host + path to `system/storage/` if outside docroot. |
| **Not acceptable** | Full recursive tree in chat; zip of entire site (defer to P2-C if needed). |

### P1-C — File inventory manifest (comparison input)

| Field | Value |
|-------|-------|
| **Why needed** | Objective #2–#3: first baseline comparison requires path-level inventory vs baseline **4055** vendor files ([baseline-manifest-v1.md](../../../baselines/ocstore-3038-rs2/manifest/baseline-manifest-v1.md)). |
| **Acceptable evidence** | (a) Text manifest: relative path + file size (and optional SHA256 for `system/`, `catalog/controller`, `admin/controller` only); or (b) `Get-ChildItem -Recurse` / `find` output saved to external `materials/run5-file-manifest.txt`; or (c) Read-only FTP export listing. |
| **Minimum scope** | All paths under `admin/`, `catalog/`, `system/` (exclude `system/storage/cache/*`, `session/*`, `logs/*` if huge). |
| **Not acceptable** | `image/catalog/` product media bulk; vendor `node_modules`; database dumps. |

---

## Priority 2 — Unblocks extensions, theme, and ocMod layers

### P2-A — Active theme identification

| Field | Value |
|-------|-------|
| **Why needed** | Objective #5: theme architecture unknown in passport. Required before Layer 3 comparison ([baseline-comparison-methodology.md](../../../baseline-comparison-methodology.md)). |
| **Acceptable evidence** | (a) Admin → System → Settings → Store → Theme field (screenshot, store name redacted OK); or (b) Listing of `catalog/view/theme/` directory names; or (c) Row from `oc_setting` where `key` = `config_theme` (value only, no other settings). |
| **Not acceptable** | Full theme ZIP unless separately chartered; binary asset bulk. |

### P2-B — Extension and modification inventory

| Field | Value |
|-------|-------|
| **Why needed** | Objectives #4–#5: extensions/ocMod drive most post-baseline deltas on ocStore sites. |
| **Acceptable evidence** | (a) Admin → Extensions → Extensions (installed modules list screenshot); (b) Admin → Extensions → Modifications (ocMod list); (c) File listing: `system/*.ocmod.xml`, `system/storage/modification/` (presence/count only OK for first pass); (d) Paths under `catalog/controller/extension/`, `admin/controller/extension/` (directory names). |
| **Not acceptable** | Modification cache full extract unless diff required; license keys. |

### P2-C — Optional compact file snapshot (external only)

| Field | Value |
|-------|-------|
| **Why needed** | If P1-C manifest generation is difficult on host, one sanitized archive enables offline diff. **Optional** for Run 5 phase 1 if P1-C delivered. |
| **Acceptable evidence** | ZIP under `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\snapshots/files/` excluding: `image/catalog/`, cache, logs, sessions, `config.php` bodies. Include empty `config.php` redacted stub or omit configs entirely. |
| **Not acceptable** | Production DB; customer exports; secrets folder. |

---

## Priority 3 — SEO, database metadata, operational context

### P3-A — SEO URL structure (metadata)

| Field | Value |
|-------|-------|
| **Why needed** | Objective #6: SEO structure for Yandex Direct / promotion prep (business goal in access brief). |
| **Acceptable evidence** | (a) Admin → System → Settings → Server tab: SEO URL enabled yes/no (screenshot); (b) Sample of 10–20 public URLs (product, category, information) from TEST storefront; (c) Listing of `oc_seo_url` **structure only** — e.g. `DESCRIBE oc_seo_url` + `SELECT COUNT(*)` — no keyword/content dump required in pass 1. |
| **Not acceptable** | Full `oc_seo_url` table export with all keywords if large; analytics tokens. |

### P3-B — Database schema metadata (no row data)

| Field | Value |
|-------|-------|
| **Why needed** | Objective #2–#4: extensions add tables; baseline documents **136** core tables ([database-metadata-v1.md](../../../baselines/ocstore-3038-rs2/database/database-metadata-v1.md)). |
| **Acceptable evidence** | (a) `SHOW TABLES` output or table list file; (b) Confirmed `DB_PREFIX` (e.g. `oc_`); (c) `information_schema` table count by prefix. |
| **Not acceptable** | Full mysqldump; `oc_customer`, `oc_order` row data; passwords. |

### P3-C — Access path confirmation (non-secret)

| Field | Value |
|-------|-------|
| **Why needed** | Stale gates in [project-access-brief.md](../project-access-brief.md) vs charter; supervised read-only access must be explicit before live inspection. |
| **Acceptable evidence** | (a) Which channel operator authorizes for Run 5 phase 2: SFTP / SSH / hosting file manager / evidence-only; (b) Confirm TEST URL still valid: `https://sibcar.new-site.space/`; (c) Admin URL path pattern (no credentials). |
| **Not acceptable** | Passwords in repo or chat; `secrets.md` content in git. |

---

## Explicitly not requested in Run 5 initialization

- Full production or TEST database dump  
- Complete `image/` tree  
- Write access or cache flush  
- Live `config.php` / `admin/config.php` file upload  
- Customer/order CSV exports  
- Penetration or malware scan  

---

## Operator checklist

- [ ] P1-A Version excerpts delivered  
- [ ] P1-B Root layout confirmed  
- [ ] P1-C File manifest delivered (or P2-C snapshot + manifest from extract)  
- [ ] P2-A Theme identified  
- [ ] P2-B Extension/ocMod inventory delivered  
- [ ] P3-A SEO metadata delivered  
- [ ] P3-B DB table list + prefix delivered  
- [ ] P3-C Access channel confirmed  

**When P1 complete:** OCPilot may begin Phase 2 (version verification) and Phase 3 (file comparison).  
**When P1–P2 complete:** Layers 3–4 (theme, extensions).  
**When P3 complete:** SEO and DB schema reports.

---

## Related documents

- [AUDIT-CHARTER.md](../AUDIT-CHARTER.md)  
- [reports/RUN-5-AUDIT-PLAN.md](../reports/RUN-5-AUDIT-PLAN.md)  
- [reports/RUN-5-SCOPE.md](../reports/RUN-5-SCOPE.md)  
- [baseline-comparison-methodology.md](../../../baseline-comparison-methodology.md)
