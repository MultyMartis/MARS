# SITE-001 W1 Backup Procedure v1

**Type:** Pre-write backup checklist — **procedure only**; **do not** execute backup during document authoring  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Trigger:** Execute **immediately before** first W1 write session (W1A), not earlier than same calendar day as writes

**Binding documents:** [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) · [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md)

---

## 1. Purpose

Create a **validated, dated, restorable** file + database snapshot of the TEST instance so W1 brand replacement can roll back via T1/T2 in [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md).

**Not sufficient:** Operator-claimed Beget backup dated **2026-05-31** — planning reference only.

---

## 2. Timing requirements

| Rule | Detail |
|------|--------|
| **When** | Immediately before W1A — same day as first write; maximum gap **4 hours** between backup completion and first admin save |
| **Re-backup** | New full backup before **each** write day if prior backup > 24 h old or any write occurred since last backup |
| **Timezone** | Record timestamps in **local operator time** + UTC offset in manifest |
| **Order** | Backup **before** any W1 change; never after partial W1A |

---

## 3. Naming convention

**Root folder (external):**

```
C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups/pre-w1-<YYYYMMDD-HHMM>/
```

| Component | Pattern | Example |
|-----------|---------|---------|
| **Backup set ID** | `pre-w1-<YYYYMMDD-HHMM>` | `pre-w1-2026-06-08-1430` |
| **Files archive** | `pre-w1-<YYYYMMDD-HHMM>-files.zip` (or `.tar.gz`) | `pre-w1-2026-06-08-1430-files.zip` |
| **Database dump** | `pre-w1-<YYYYMMDD-HHMM>-db.sql.gz` | `pre-w1-2026-06-08-1430-db.sql.gz` |
| **Manifest** | `BACKUP-MANIFEST.md` | Inside backup root folder |
| **Validation record** | `validation-checklist.md` | Inside backup root folder |
| **Evidence note (repo)** | Optional pointer only — **no dumps in git** | Session REPORT references external path |

**Subfolders:**

```
pre-w1-<YYYYMMDD-HHMM>/
├── files/              ← extracted tree or archive staging
├── database/           ← SQL dump
├── BACKUP-MANIFEST.md
└── validation-checklist.md
```

---

## 4. Files backup

### 4.1 Scope

Full TEST site document root as hosted on Beget — minimum paths required for W1 rollback:

| Path class | Include |
|------------|---------|
| **OpenCart core** | `admin/`, `catalog/`, `system/`, `image/` |
| **Theme W1B** | `catalog/view/theme/auto/` |
| **W1C controllers** | `catalog/controller/information/about.php`, `contact.php` |
| **W1D assets** | `img/`, `favicon/`, `image/catalog/logo*` |
| **Config** | `config.php` — **store in backup only**; never commit to git |
| **Storage** | `system/storage/` — include if size permits; minimum `modification/`, `cache/` note |

**Exclude from git copies:** secrets; only external encrypted storage per operator policy.

### 4.2 Methods (operator chooses one)

| Method | Steps |
|--------|-------|
| **L1-D — Beget panel** *(preferred)* | Panel → backup/download full site archive → save to external `files/` with naming convention |
| **L1-B — FTP/SFTP** | Recursive download of document root to external `files/` → compress to `-files.zip` |
| **L1-A — ZIP drop** | Operator-provided archive placed directly in backup folder |

### 4.3 Files checklist

| # | Check | Done |
|---|-------|------|
| F-01 | Confirmed host = TEST (`sibcar.new-site.space`) | ☐ |
| F-02 | Archive size > 0; extract test on one sample file (`catalog/view/theme/auto/template/common/header.twig`) | ☐ |
| F-03 | `config.php` present in archive (not copied to repo) | ☐ |
| F-04 | Archive checksum recorded in manifest (SHA-256 optional) | ☐ |
| F-05 | Archive stored under `backups/pre-w1-<timestamp>/` | ☐ |

---

## 5. Database backup

### 5.1 Scope

Full MySQL dump of TEST database used by SITE-001 (single store, store_id 0).

**Critical tables for W1:** `oc_setting`, `oc_information_description` — full dump preferred over partial.

### 5.2 Methods

| Method | Steps |
|--------|-------|
| **Beget panel** | Export DB → download `.sql` or `.sql.gz` |
| **phpMyAdmin** | Export → custom → gzip → save to `database/` |
| **CLI** | `mysqldump` if SSH available — operator only |

### 5.3 Database checklist

| # | Check | Done |
|---|-------|------|
| D-01 | Dump file size > 0 | ☐ |
| D-02 | Header contains database name matching TEST instance | ☐ |
| D-03 | Spot-check: `oc_setting` row for `config_name` = `АЦ Хмельницкий` (pre-W1 expected) | ☐ |
| D-04 | Gzip integrity verified (decompress test) | ☐ |
| D-05 | Dump stored as `pre-w1-<timestamp>-db.sql.gz` | ☐ |

---

## 6. Timestamp requirements

Record in `BACKUP-MANIFEST.md`:

| Field | Required |
|-------|----------|
| Backup set ID | `pre-w1-YYYYMMDD-HHMM` |
| Start time (local + offset) | yes |
| End time (local + offset) | yes |
| Operator name | yes |
| TEST URL confirmed | yes |
| Beget account / site identifier (non-secret label) | yes |
| Files method (L1-D / L1-B / L1-A) | yes |
| DB method | yes |
| Prior backup superseded | 2026-05-31 claim → superseded by this set when complete |

---

## 7. Validation checklist

Complete **before** marking C-08 execution **PASS**:

| # | Validation | Pass |
|---|------------|------|
| V-01 | Files archive opens without error | ☐ |
| V-02 | DB dump opens/decompresses without error | ☐ |
| V-03 | Sample file from archive matches live TEST file (size/hash spot-check on `header.twig`) | ☐ |
| V-04 | Sample SQL contains `oc_setting` and expected pre-W1 `config_name` | ☐ |
| V-05 | Backup path written to Change Request «Backup gate» section | ☐ |
| V-06 | Rollback plan pre-change snapshot table updated | ☐ |
| V-07 | Operator acknowledges Beget restore path (panel) — drill optional | ☐ |
| V-08 | `# REPORT — SITE-001 W1 Pre-Backup` or equivalent session note in external `reports/` | ☐ |

**Restore drill:** Optional but recommended. If not performed, record **SAFE UNKNOWN — restore drill** in manifest.

---

## 8. Evidence requirements

| Evidence | Storage | In git? |
|----------|---------|---------|
| Files archive | External `backups/pre-w1-<timestamp>/` | **No** |
| DB dump | External `backups/pre-w1-<timestamp>/database/` | **No** |
| `BACKUP-MANIFEST.md` | External backup folder | **No** — optional sanitized summary in repo REPORT only |
| `validation-checklist.md` | External backup folder | **No** |
| Sanitized settings export (recommended) | External `materials/phase1-pre-change-freeze/` | **No** |
| Pre-change screenshots (C-09, recommended) | External `materials/phase1-pre-change-freeze/` | **No** |
| Session REPORT pointer | External `reports/` or repo session REPORT | Summary only |

**Forbidden in repo:** `config.php`, DB dumps, credentials, full archives.

---

## 9. Post-backup gates

When all checklists **PASS**:

1. Update [SITE-001-W1-CHANGE-REQUEST-v1.md](SITE-001-W1-CHANGE-REQUEST-v1.md) — Backup gate → **confirmed** + path.
2. Update [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) — Pre-change snapshot → **confirmed**.
3. Operator may authorize W1A start per [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) §8.

---

## 10. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact Beget backup retention policy | **SAFE UNKNOWN** |
| SSH/mysqldump availability | **SAFE UNKNOWN** |
| Full dump duration / size | **SAFE UNKNOWN** until first execution |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **CREATED** — W1 pre-write backup procedure v1 |

*SITE-001 W1 Backup Procedure v1 — procedure only; no backup executed in authoring.*
