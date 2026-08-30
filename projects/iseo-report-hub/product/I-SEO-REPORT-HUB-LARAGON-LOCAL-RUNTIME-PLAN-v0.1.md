# I-SEO Report Hub — Laragon Local Runtime Plan v0.1

**Status:** PLANNING ONLY  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Runtime changes in this task:** **NONE**

**Authority:** [Platform Decision v0.1](I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Local runtime planning |
| Laragon | Available per operator statement |
| Exact Laragon inspection | **Not performed** in this task |
| Vhost / hosts / DB creation | **Not performed** |
| Application scaffold | **Not created** |

Planning only. No Laragon configuration, no Apache/Nginx edits, no hosts file edits, no database creation.

---

## 2. Assumed Local Runtime

Operator: Laragon is ready for local PHP + MySQL development.

Exact values remain **SAFE UNKNOWN** until verified in a future Phase 0 charter:

| Item | Status |
|------|--------|
| Laragon root path | **SAFE UNKNOWN** |
| PHP version | **SAFE UNKNOWN** |
| MySQL / MariaDB version | **SAFE UNKNOWN** |
| Web server (Apache / Nginx) | **SAFE UNKNOWN** |
| Vhost name | **SAFE UNKNOWN** |
| Database name (actual) | **SAFE UNKNOWN** |
| Docroot path | **SAFE UNKNOWN** |

Do not invent versions or paths in implementation docs.

---

## 3. Recommended Local Project Layout

**Do not create these paths in this task.** Candidates for a future implementation charter:

### Option A — under Active Brain project tree

```
X:\AI MARS\projects\iseo-report-hub\app\
```

Pros: colocated with product docs.  
Cons: risk of mixing docs WIP with runtime; scheduled jobs must not run from dirty Active Brain main.

### Option B — under MARS Localhost (preferred runtime candidate)

```
X:\MARS-Localhost\iseo-report-hub\
```

Pros: explicit local runtime root; aligns with MARS Localhost Infrastructure boundary.  
Cons: separate from docs tree; needs clear sync/checkout discipline.

### Recommendation

- Keep **documentation** in `X:\AI MARS\projects\iseo-report-hub\`.
- Prefer **runtime app** under `X:\MARS-Localhost\iseo-report-hub\` **or** a scoped `app\` folder only after an **explicit implementation charter**.
- Avoid dirty scheduled/runtime jobs from Active Brain working tree.
- Runtime checkout must be **explicit**, not accidental.

Exact choice: **SAFE UNKNOWN** until Phase 0 charter.

---

## 4. Local Domain Candidate

Examples only — **do not** create vhost or hosts entries in this task:

- `iseo-report-hub.test`
- `iseo-report.local`

Final local hostname: **SAFE UNKNOWN**.

---

## 5. Local DB Candidate

Suggested development database name (not created):

- `iseo_report_hub_dev`

Do not create the database in this task. Credentials must never appear in committed docs.

---

## 6. Local Secrets

| Rule | Detail |
|------|--------|
| Local secrets file | `.env.local` (or equivalent) |
| Commit | **Never** commit secrets |
| Contents (future) | DB credentials, app key, upload path, base URL |
| Template | Optional later `.env.example` with **empty/placeholder** values only |

No real credentials in this document.

---

## 7. Future Preflight Before Implementation

Before any scaffold or DB work, an implementation charter must confirm:

1. Laragon install path
2. PHP version
3. MySQL / MariaDB version
4. Web server in use (Apache / Nginx)
5. Docroot / vhost mapping
6. DB access (create DB / user capability)
7. Backup location for local data
8. Git ignore rules for env, uploads, vendor
9. Local secret file path
10. Whether runtime lives on `X:\MARS-Localhost\...` or project `app\`

---

## 8. Boundaries

- No Laragon changes performed here.
- No claim that local site or DB exists.
- MARS filesystem authority remains: writes only on `X:` under approved roots when an implementation charter allows them.
