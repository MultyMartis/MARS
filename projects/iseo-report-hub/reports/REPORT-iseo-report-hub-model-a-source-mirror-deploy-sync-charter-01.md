# REPORT — I-SEO REPORT HUB MODEL A SOURCE MIRROR + DEPLOY SYNC CHARTER 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-24  
**Branch:** `mars/canonical-post-recovery`  
**HEAD at start:** `6031557dafed42596cb62046757aa6c5c4581c47`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (start) | `6031557dafed42596cb62046757aa6c5c4581c47` |
| Staged / index before writes | **Empty** |
| Foreign WIP | **Preserved** (unrelated `M` / `??` not staged / restored / cleaned) |
| Runtime scaffold | **Present** at `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| `app-source/` | **Absent** (`Test-Path` = False) — not created |
| Write scope | Allowlisted Active Brain i-SEO docs only |

Note: charter listed a prior known HEAD `fddf8780…`; session start HEAD was `6031557d…` (later monorepo commits present). Work continued on current HEAD.

---

## 2. Runtime Read-only Inspection

| Check | Result |
|-------|--------|
| Files checked | `README.md`, `.env.example`, `.gitignore`, `public/index.php`, `public/health.php`, `public/assets/css/app.css`, `public/assets/js/app.js`, `app/**` placeholders, `config/*`, `storage/*` markers, `database/*`, `docs/README.md`, `docs/SOURCE-RUNTIME-POLICY.md` |
| Copying | **None** |
| Runtime edits | **None** |
| Secrets in inspected examples | **None** — `.env.example` uses `CHANGE_ME` placeholders only |
| `.env` / `.env.local` | **Absent** |
| Nested `.git` | **Absent** |
| `vendor/` / `node_modules/` | **Absent** (not observed in tree listing) |

---

## 3. Model A Decision

| Topic | Decision |
|-------|----------|
| Model | **Model A selected** (planning / charter) |
| Source path (planned) | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Sync direction | **source → runtime** (default) |
| Rationale | Versioned monorepo source, reviewable diffs, rollback, regenerable runtime, secrets/uploads/logs separation |
| Phase 1 gate | Blocked until `app-source/` created + committed, sync procedure accepted, runtime regenerable from source, `.env.local` outside Git, DB creation charter decided |

---

## 4. Deploy/Sync Policy Summary

| Topic | Summary |
|-------|---------|
| Source / target | `app-source/` → Localhost runtime |
| Include | Code, config examples, docs, static assets, `.keep` / `.gitignore` markers |
| Exclude | `.env`, `.env.local`, uploads/logs/cache contents, DB data, Laragon/hosts/vhost, service restarts |
| Pre-sync | Source/target exist; no env overwrite; no generated files in source; backup if destructive; empty/valid index; foreign WIP preserved |
| Post-sync | Allowlist match; env intact; health page present; no secrets in source; no DB mutation |
| Future automation | Deferred (PowerShell / dry-run / manifest / hashes / backup) |

---

## 5. Source Mirror File Map Summary

| Category | Content |
|----------|---------|
| Include | Phase 0 README, `.env.example`, `.gitignore`, `public/*`, `app` placeholders, `config` examples, `storage` markers/docs, `database` docs/draft, `docs` including `SOURCE-RUNTIME-POLICY.md` |
| Exclude | `.env` / `.env.local`, generated storage contents, vendor/node_modules, SQL dumps, private reports, credentials, OS/editor temp, nested `.git` |
| Validation | No secrets; no nested git; no generated payloads; allowlist-only copy |

---

## 6. Files Created

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md`

---

## 7. Files Modified

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 8. Validation

| Check | Result |
|-------|--------|
| `app-source/` created | **No** |
| Runtime copy | **No** |
| Sync executed | **No** |
| Runtime edits | **No** |
| DB created/mutated | **No** |
| SQL executed | **No** |
| Vhost / hosts | **No** |
| Service restart | **No** |
| Secrets | **No** |
| Demo workspace edits | **No** |
| Registry changes | **No** |
| push / fetch / pull / reset / clean / stash | **No** |

---

## 9. Commit

| Field | Value |
|-------|-------|
| Exact-path `git add` | **Yes** (allowlisted Active Brain paths only) |
| Commit | **Yes** |
| Message | `docs(iseo-report-hub): add source mirror sync charter` |
| Commit hash | `PENDING_POST_COMMIT` |
| HEAD verification | Pending post-commit `git show` |
| Push | **No** |

Staged allowlist (expected):

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md`

---

## 10. SAFE UNKNOWN

- Whether `iseo-report-hub.test` exists in hosts / Laragon vhost (not inspected this wave).
- Whether MySQL already has `iseo_report_hub_dev` (not queried).
- Exact future sync tooling implementation (script not written).
- Whether runtime tree will diverge before the mirror-creation wave.

---

## 11. Recommended Next Action

Create and commit `app-source` mirror from Phase 0 scaffold using the approved file map.

---

## 12. Files Changed

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-model-a-source-mirror-deploy-sync-charter-01.md`

---

## 13. Git Actions

| Action | Done |
|--------|------|
| Exact-path `git add` | **yes** |
| commit | **yes** |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
