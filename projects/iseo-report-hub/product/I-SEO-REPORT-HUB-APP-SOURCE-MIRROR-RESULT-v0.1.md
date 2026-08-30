# I-SEO Report Hub — App Source Mirror Result v0.1

**Status:** APP-SOURCE MIRROR CREATED  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator create app-source mirror from Phase 0 scaffold 01; Model A charter + file map + deploy/sync policy

---

## 1. Status

| Fact | State |
|------|-------|
| app-source mirror | **Created** |
| Source path | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Copied from | Phase 0 runtime scaffold (allowlist only) |
| Source → runtime sync | **Not executed** |
| Runtime edits | **None** |
| DB / vhost / hosts | **Not created / not edited** |
| Secrets | **None** — examples / placeholders only |

Platform remains custom **PHP + SQL/MySQL**. WordPress is **not** runtime / SoT.

---

## 2. Source Path

`X:\AI MARS\projects\iseo-report-hub\app-source\`

Relative monorepo path: `projects/iseo-report-hub/app-source/`

---

## 3. Runtime Path

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

Runtime remains the Localhost deploy target. It was **not** modified by this wave. Bootstrap copy direction for this one-time import was **runtime → app-source** (chartered). Ongoing sync direction after this wave is **source → runtime**.

---

## 4. Files Mirrored

Exact files under `app-source/`:

- `README.md` (includes Source Mirror Note added in app-source only)
- `.env.example`
- `.gitignore`
- `public/index.php`
- `public/health.php`
- `public/assets/css/app.css`
- `public/assets/js/app.js`
- `app/README.md`
- `app/Controllers/.keep`
- `app/Models/.keep`
- `app/Views/.keep`
- `app/Services/.keep`
- `app/Support/.keep`
- `config/README.md`
- `config/app.example.php`
- `config/database.example.php`
- `storage/README.md`
- `storage/.gitignore`
- `storage/logs/.keep`
- `storage/uploads/.keep`
- `storage/cache/.keep`
- `database/README.md`
- `database/schema-draft-not-migration.md`
- `database/seeds/README.md`
- `docs/README.md`
- `docs/SOURCE-RUNTIME-POLICY.md`

Total: **26** files.

**Source-only adjustment:** `app-source/storage/.gitignore` was updated to add `!README.md` so the allowlisted `storage/README.md` can be versioned. Runtime `storage/.gitignore` was **not** modified.

---

## 5. Files Excluded

| Category | Observed on runtime before copy | Copied |
|----------|----------------------------------|--------|
| `.env` | **Absent** | No |
| `.env.local` | **Absent** | No |
| uploads/logs/cache payloads (beyond `.keep`) | **Absent** — only `.keep` present | No (only `.keep` mirrored) |
| `vendor/` | **Absent** | No |
| `node_modules/` | **Absent** | No |
| DB dumps | **Absent** | No |
| Private client data / report exports | **Absent** | No |
| Production credentials | **Absent** | No |
| Nested `.git` | **Absent** | No |

Nothing outside the approved file-map allowlist was copied.

---

## 6. Validation

| Check | Result |
|-------|--------|
| Secrets in mirror | **None** — `.env.example` / `*.example.php` placeholders only (`CHANGE_ME`) |
| Nested git under app-source | **None** |
| Generated logs/uploads/cache payloads | **None** — `.keep` markers only |
| Executable SQL migrations | **None** — schema draft is markdown only |
| Examples only for env/config | **Yes** |
| Runtime modified | **No** |
| Source → runtime sync | **No** |

---

## 7. Source/Runtime Policy

| Topic | State |
|-------|-------|
| Source of truth | **`app-source/`** (versioned Active Brain mirror) |
| Runtime role | Deploy / runnable Localhost target |
| Sync direction (ongoing) | **source → runtime** |
| Runtime → source | Only by **explicit import charter** after human review |
| Related docs | Source/Runtime Policy v0.1; Model A Charter v0.1; Deploy/Sync Policy v0.1; File Map v0.1 |

---

## 8. Phase 1 Readiness

| Gate | State |
|------|-------|
| `app-source/` mirror exists | **Yes** (this wave) |
| Mirror committed | See closeout report / commit wave |
| Phase 1 can be chartered | **After operator review** of this mirror |
| DB creation (`iseo_report_hub_dev`) | Still **separate charter** — not done |
| Vhost / hosts (`iseo-report-hub.test`) | Still **separate charter** — not done |
| `.env.local` / live `.env` | Still **local-only / separate** — not created; never commit |

---

## 9. SAFE UNKNOWN

- Whether `iseo-report-hub.test` already exists in hosts / Laragon vhost (not inspected this wave).
- Whether MySQL already contains database `iseo_report_hub_dev` (not queried).
- Exact future source → runtime sync tooling (script not written in this wave).
