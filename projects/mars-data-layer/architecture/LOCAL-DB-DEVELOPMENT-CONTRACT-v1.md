# Local DB Development Contract v1

**Document:** `LOCAL-DB-DEVELOPMENT-CONTRACT-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Status:** Normative for local development contour (no install executed in Architecture V1 wave)

---

## 1. Purpose

Separate **Git source authority** from **disposable local PostgreSQL runtime** for MARS Bot Data Platform development.

This contract does **not** authorize production VPS PostgreSQL installation.

---

## 2. Evidence: existing MARS/Laragon conventions

Observed (2026-09-03):

| Fact | Evidence |
|------|----------|
| Canonical local runtime root | `X:\MARS-Localhost` (AI WS / `X:`) |
| Existing databases zone | `X:\MARS-Localhost\databases\` with `active/`, `baselines/`, `dumps/`, `temp/` |
| MLI focus today | MySQL 8.4 under Laragon for WordPress/CMS consumers |
| MLI docs | `projects/mars-localhost-infrastructure/MARS-LOCALHOST-DATABASE-STANDARD-v1.md` (MySQL) |
| Brain vs runtime split | Documented in `X:\MARS-Localhost\README.md` |

**Decision:** Prefer a **sibling contour** under the existing databases root rather than inventing a new top-level runtime tree:

```text
X:\MARS-Localhost\databases\mars-bot-data\
```

This keeps MLI MySQL paths intact and places bot-data local runtime where operators already look for DB artefacts.

---

## 3. Authority split

| Path | Role |
|------|------|
| `X:\AI MARS\projects\mars-data-layer\` | **Source authority** — Git, specs, migrations, fixtures, toolkit |
| `X:\MARS-Localhost\databases\mars-bot-data\` | **Disposable/reproducible local runtime** — data dirs, compose/state, local dumps |
| `X:\AI MARS\local\` (existing private secret conventions) | Local credentials — **never** commit |

Runtime directories are **not** authoritative. If runtime drifts from Git migrations, **rebuild from source**.

---

## 4. Proposed local runtime layout

```text
X:\MARS-Localhost\databases\mars-bot-data\
  README.md                 # operator pointer (optional; out of Git)
  pgdata\                   # PostgreSQL data directory (local only)
  dumps\                    # local dumps
  logs\                     # local logs
  compose\ or runtime\      # local orchestration files if chartered
```

Exact compose/engine choice (native PostgreSQL vs Docker Desktop vs other) is a **later local enablement charter**. Architecture V1 only locks the **path contract**.

---

## 5. Source → runtime sync model

```text
projects/mars-data-layer/database/**/migrations/
  → applied by migrator tooling into local DB `mars`

projects/mars-data-layer/fixtures/
  → test-only data loads (never production)

projects/mars-data-layer/toolkit/   (future)
  → code under test against local DB

tools/ (future under this project or MLI tools)
  → migrate / smoke / reset helpers
```

Rules:

1. Migrations are Git-versioned SQL only.
2. No secrets in Git.
3. Local reset = drop/recreate schema or database from migrations + optional fixtures.
4. Do not treat local `pgdata` as backup of record for production.

---

## 6. Credentials

- Follow existing MARS local/private secret conventions (`X:\AI MARS\local\…`).
- **Do not** create real credentials in Architecture V1 documentation wave.
- Local roles mirror conceptual names (`mars_migrator`, `iseo_runtime`, …) with local-only passwords.

---

## 7. Non-goals for this contract

- Installing PostgreSQL in this wave;
- Binding Laragon MySQL to bot data;
- Making `X:\MARS-Localhost` a second Git root;
- Claiming production parity from local alone.

---

## 8. Next local enablement gate

When chartered: choose engine, create `mars-bot-data` directory, apply `mars_core` migrations, smoke Toolkit against local `mars`.
