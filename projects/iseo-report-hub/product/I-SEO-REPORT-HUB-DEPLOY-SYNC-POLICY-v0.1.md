# I-SEO Report Hub — Deploy / Sync Policy v0.1

**Status:** POLICY ONLY — NO SYNC PERFORMED  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator Model A source mirror + deploy/sync charter 01  
**Related:** [I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md](I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md](I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md), [I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md](I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Deploy / sync **policy** only |
| Sync executed | **No** |
| Runtime modified by this policy wave | **No** |
| `app-source/` created | **No** (planned; separate wave) |

This document defines safe rules for future sync. It does **not** copy files, overwrite runtime, or mutate Localhost services.

---

## 2. Source and Target

| Role | Path |
|------|------|
| **Source** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| **Target** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |

Source is inside Active Brain Git. Target is Localhost runtime outside the monorepo and is **not** a separate Git repo.

---

## 3. Sync Direction

| Direction | Policy |
|-----------|--------|
| **Primary** | source → runtime |
| Runtime → source | Only via **explicit import charter** after human review |

Default operator workflow: edit/version in `app-source`, then sync allowlisted files to runtime.

---

## 4. Sync Rules

**May copy (when chartered):**

- application code under `app/`, `public/`
- config **examples** (`*.example.php`, similar placeholders)
- documentation under `docs/`, root `README.md`
- static assets under `public/assets/`
- source-safe markers: `.gitignore`, `storage/.gitignore`, `*/.keep`
- schema/docs drafts that are not executable migrations unless a migration charter says otherwise

**Must not copy / must not overwrite:**

- `.env`
- `.env.local`
- uploads contents (`storage/uploads/*` except preserving `.keep` policy)
- logs contents (`storage/logs/*` except `.keep`)
- cache contents (`storage/cache/*` except `.keep`)
- DB data, dumps, or live MySQL contents
- Laragon Apache/Nginx config, hosts file, vhosts
- service restarts — unless a **future** explicit charter authorizes them

Sync must not invent WordPress, Laravel, Composer, npm, or package downloads as side effects.

---

## 5. Pre-sync Checks

Before any sync wave:

1. Confirm `app-source/` exists and is the intended committed tree.
2. Confirm runtime target path exists under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`.
3. Confirm sync will **not** overwrite `.env` / `.env.local` (exclude them from copy set).
4. Confirm source does **not** contain generated files, secrets, uploads, logs, or cache payloads.
5. If sync could be destructive (overwrite divergent runtime files), take a runtime backup/snapshot first.
6. Confirm Active Brain staged index is empty (or only contains the charter’s allowlisted paths).
7. Preserve foreign WIP in the monorepo — do not stage, restore, clean, or reset unrelated paths.
8. Confirm volume/workspace identity (`X:`, label `AI WS`, branch `mars/canonical-post-recovery` unless another branch is explicitly authorized).

---

## 6. Post-sync Checks

After a sync wave:

1. File list on runtime matches the allowlist / expected tree for that charter.
2. If `.env.local` or `.env` exists on runtime, it remains intact and was not replaced from source.
3. Health page path (`public/health.php`) still present and usable under the chosen local review method.
4. No secrets landed in `app-source/` or Active Brain commits.
5. No generated runtime artefacts were copied **into** source.
6. No DB creation or mutation occurred unless a separate DB charter ran (default: none).

---

## 7. Initial Phase 0 Mirror Strategy

**Next wave** (not this task) should:

1. Create `projects/iseo-report-hub/app-source/`.
2. Copy Phase 0 scaffold **source-safe** files from runtime → `app-source` using the file map.
3. Exclude secrets and generated files.
4. Commit `app-source` with exact-path staging only.
5. Optionally run source → runtime **dry-run comparison** (no overwrite required if trees match origin).
6. Avoid destructive overwrite of the existing Phase 0 runtime because it is currently the same origin as the planned mirror.

Direction note for the first mirror: the **bootstrap** copy is runtime → `app-source` (one-time import under charter). After that, ongoing direction returns to source → runtime.

---

## 8. Future Automation

Possible later (explicit future charters only):

- PowerShell sync script
- dry-run mode
- allowlist manifest
- hash / diff report
- automatic runtime backup before overwrite

**Not in this task.** No scripts created or executed here.

---

## 9. SAFE UNKNOWN

- Exact command syntax of a future sync script (not written yet).
- Whether operator prefers robocopy, `Copy-Item` allowlist loops, or another tool.
- Whether runtime will diverge from Phase 0 before the first mirror wave.
- Hosts/vhost readiness for `iseo-report-hub.test` at sync time.
- Whether `.env` / `.env.local` will already exist when the first source → runtime sync runs.
