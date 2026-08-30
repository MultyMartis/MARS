# I-SEO Report Hub — Model A Source Mirror Charter v0.1

**Status:** PLANNING / CHARTER ONLY  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator Model A source mirror + deploy/sync charter 01  
**Related:** [I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md](I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md), [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md), [I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md](I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Planning / charter only |
| `app-source/` created | **No** — not in this wave |
| Runtime sync performed | **No** |
| Phase 0 runtime scaffold | **Exists** at Localhost runtime path |
| Phase 1 implementation | **Blocked** until source mirror is created and committed |

This charter **selects Model A** for maintainability planning. It does **not** create the mirror or run sync.

Platform remains custom **PHP + SQL/MySQL**. WordPress is **not** runtime / SoT.

---

## 2. Decision

**Adopt Model A** for i-SEO Report Hub maintainability:

| Layer | Role |
|-------|------|
| Source-first mirror | Versioned code under Active Brain |
| Deploy / sync | Explicit procedure from source → Localhost runtime |
| Runtime | Runnable workspace only — **not** Git source of truth |

Runtime must **not** become a separate Git repository. Runtime files are **not** committed by normal Active Brain commits until they live under the versioned `app-source/` mirror.

---

## 3. Source Path

**Approved planned source (not created yet):**

`X:\AI MARS\projects\iseo-report-hub\app-source\`

Relative monorepo path:

`projects/iseo-report-hub/app-source/`

---

## 4. Runtime Path

**Approved runtime:**

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

Phase 0 scaffold already exists here (outside Active Brain Git).

---

## 5. Why Model A

Model A is preferred because it provides:

1. **Versioned code** — PHP/CSS/JS and source-safe config examples live in the MARS monorepo and are reviewable in normal commits.
2. **Reviewable diffs** — changes go through Active Brain Git history, not only Localhost filesystem edits.
3. **Rollback** — prior commits can restore known-good source; runtime can be regenerated from that source.
4. **Source can regenerate runtime** — Localhost tree is a deploy target, not an irreplaceable sole copy.
5. **Secrets / uploads / logs separation** — `.env`, `.env.local`, uploads, logs, and cache stay out of Git; only placeholders and `.keep` markers are mirrored.
6. **MARS monorepo alignment** — i-SEO Report Hub remains a folder inside one shared repo (`X:\AI MARS`), not a parallel product Git root.

Model B (runtime-first) remains documented in Source/Runtime Policy as a weaker temporary option and is **not** selected by this charter.

---

## 6. What Will Be Mirrored

From Phase 0 runtime into `app-source/` in a **later** chartered wave (not this task):

- `README.md`
- `.env.example`
- `.gitignore`
- `public/`
- `app/`
- `config/`
- `database/`
- `docs/`
- `storage/README.md`
- `storage/.gitignore`
- `storage/*/.keep` only — **not** generated contents of logs/uploads/cache

Exact path-level allowlist: [I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md](I-SEO-REPORT-HUB-SOURCE-MIRROR-FILE-MAP-v0.1.md).

---

## 7. What Must Never Be Mirrored

- `.env`
- `.env.local`
- production credentials
- DB dumps with private data
- uploads (except empty folder markers via `.keep`)
- logs (except `.keep`)
- cache (except `.keep`)
- generated reports with private metrics unless sanitized and explicitly chartered
- `vendor/` / `node_modules/` unless a future charter explicitly approves dependency vendoring

---

## 8. Sync Direction

| Direction | Rule |
|-----------|------|
| **Default** | `app-source` → runtime |
| Runtime → `app-source` | Allowed **only** through an explicit review/import charter |

Casual “edit runtime then copy back” without charter is **forbidden**.

Detailed sync rules: [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md).

---

## 9. Phase 1 Gate

Before Phase 1 (app skeleton / config / auth baseline):

1. Create `app-source/` mirror from Phase 0 scaffold using the approved file map.
2. Commit the source mirror into Active Brain (exact-path staging only).
3. Define and accept the sync procedure (policy already drafted; execution charter next).
4. Verify runtime can be regenerated from source (dry-run comparison acceptable).
5. Define `.env.local` (or `.env`) location **outside** Git on Localhost only.
6. Decide DB creation under a separate charter (`iseo_report_hub_dev` remains candidate only).

Until those gates are met, Phase 1 remains **blocked**.

---

## 10. SAFE UNKNOWN

- Whether `iseo-report-hub.test` already exists in hosts / Laragon vhost (not inspected in this charter wave).
- Whether MySQL already contains database `iseo_report_hub_dev` (not queried).
- Exact future sync tooling (PowerShell script vs manual allowlisted copy) — policy allows either; automation deferred.
- Operator timing for approving the next wave that **creates** and **commits** `app-source/`.
- Whether any Localhost-only files appear after this charter and before the mirror wave (must be re-validated against the file map).
