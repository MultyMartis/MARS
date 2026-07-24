# I-SEO Report Hub — Source / Runtime Policy v0.1

**Status:** ACTIVE POLICY (Phase 0 post-scaffold)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator Phase 0 runtime review + source/runtime policy charter

---

## 1. Status

| Fact | State |
|------|-------|
| Phase 0 runtime scaffold | **Exists** |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| Active Brain docs path | `X:\AI MARS\projects\iseo-report-hub\` |
| Source preservation model | **Not finalized as implementation** — this policy defines the decision frame |
| Database | **Not created** |
| Vhost / hosts | **Not configured by MARS agents in Phase 0** |
| Secrets / `.env` | **None** in runtime or docs |

WordPress is **not** the runtime. Platform remains custom **PHP + SQL/MySQL**.

---

## 2. Active Brain Authority

`X:\AI MARS\projects\iseo-report-hub\` contains:

- product documentation;
- architecture and technical decisions;
- operational index;
- closeout reports.

It is the **committed documentation authority** inside the shared MARS monorepo (`X:\AI MARS`).

It **must not** hold:

- local secrets;
- uploads;
- cache;
- logs;
- live `.env` / `.env.local`;
- production credentials.

---

## 3. Runtime Workspace

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` contains the **runnable local app** (Phase 0 scaffold today).

| Property | Rule |
|----------|------|
| Role | Localhost runtime workspace |
| Separate Git repository | **No** — do not `git init` here |
| Production | **No** |
| Committed by normal Active Brain commit | **No** — path is outside the MARS monorepo |
| Future local artefacts | May include `.env`, uploads, logs, cache — **must not** leak into versioned source |

---

## 4. Current Phase 0 State

Documented and reviewed:

- scaffold tree exists under Localhost;
- `public/index.php` and `public/health.php` present;
- config examples (`config/app.example.php`, `config/database.example.php`);
- `.env.example` placeholders only (`CHANGE_ME`);
- storage folders (`logs/`, `uploads/`, `cache/`) with `.keep`;
- schema reminder is markdown draft, **not** executable SQL;
- DB **not** created;
- vhost/hosts **not** configured by Phase 0;
- no secrets, no nested `.git`, no WordPress, no `vendor` / `node_modules`.

---

## 5. Versioning Problem

Runtime lives **outside** the MARS Git monorepo. Therefore:

- normal Active Brain commits **do not** version runtime PHP/CSS/JS files;
- Phase 0 docs commits record **documentation and decisions**, not the runnable tree;
- this split is **acceptable only temporarily** after Phase 0 review;
- before Phase 1 implementation work, a **source preservation model** must be chosen.

Leaving runnable code only on Localhost without a versioned mirror risks loss of history, weak review, and hard rollback.

---

## 6. Allowed Future Models

### Model A — Source-first mirror

| Layer | Path |
|-------|------|
| Versioned source | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |

Sync/deploy from source to runtime by **explicit** scripts/procedure (separate charter).

**Pros:**

- versioned code in monorepo;
- cleaner review;
- monorepo source of truth;
- runtime can be regenerated.

**Risks:**

- needs sync discipline;
- must protect `.env`, uploads, logs, cache from mirroring into Git.

### Model B — Runtime-first local app

Runtime remains the primary working copy. Active Brain stores reports, snapshots, and exports only.

**Pros:**

- simpler initially;
- direct Laragon editing.

**Risks:**

- weak version control;
- easy to lose code history;
- harder review/rollback;
- **not recommended long-term**.

---

## 7. Recommended Direction

**Recommend Model A before Phase 1.**

Constraints for this task / current wave:

- **do not** create `app-source/` yet;
- create a **separate charter** for source mirror + deploy/sync policy;
- only then proceed to Phase 1 code/auth/config work.

Current Phase 0 runtime scaffold remains a **local runtime artifact** until that charter.

---

## 8. Secrets / Generated Files Policy

**Never commit:**

- `.env`
- `.env.local`
- DB dumps with real data
- uploads
- logs
- cache
- production credentials
- client private metrics unless sanitized and explicitly chartered

`.env.example` and `*.example.php` may hold placeholders only (`CHANGE_ME`, candidate DB name, local domain intent).

---

## 9. Phase 1 Gate

Phase 1 **must not** proceed until:

1. source preservation model confirmed (prefer Model A);
2. vhost/domain strategy confirmed;
3. DB creation charter confirmed;
4. `.env.local` / local env location confirmed;
5. backup/export (or sync) policy confirmed.

---

## 10. SAFE UNKNOWN

- Whether `iseo-report-hub.test` already exists in hosts/vhost (not inspected in this policy task).
- Whether MySQL already has database `iseo_report_hub_dev` (not queried).
- Exact sync tooling for Model A (robocopy script, manual copy, other) — deferred to source-mirror charter.
- Operator final sign-off timing for Model A vs temporary Model B exception.
