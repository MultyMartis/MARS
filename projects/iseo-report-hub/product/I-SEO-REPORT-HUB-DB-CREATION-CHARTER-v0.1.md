# I-SEO Report Hub — DB Creation Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no database created  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub DB Creation + Schema Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md), [I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md), [I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md](I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | DB creation **charter / policy** only |
| Database created | **No** |
| SQL executed | **No** |
| Scope | **Local dev DB target only** |
| Production DB | **Out of scope** |

This charter authorizes planning for a future local MySQL database. It does **not** authorize `CREATE DATABASE`, grants, dumps, or schema apply in this wave.

---

## 2. Target DB

| Field | Value |
|-------|-------|
| **DB name** | `iseo_report_hub_dev` |
| **Engine** | MySQL **8.4.3** (Laragon Localhost; previously verified in preflight 01) |
| **Host** | `127.0.0.1` |
| **Port** | `3306` |
| **Charset** | `utf8mb4` |
| **Collation** | Prefer `utf8mb4_unicode_ci` or a compatible MySQL 8 default (`utf8mb4_0900_ai_ci` may be server default) — **final collation must be confirmed before SQL** |
| **App URL context** | `http://iseo-report-hub.test/` |
| **Runtime path** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| **Source path** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |

---

## 3. DB Creation Boundary

| Allowed (future wave, when chartered) | Forbidden (always / this wave) |
|---------------------------------------|--------------------------------|
| Local Laragon MySQL on `127.0.0.1:3306` | Production / remote hosting DBs |
| Empty or demo-sanitized local data | Real private client metrics |
| Dev reset under explicit HITL | Real client PII dumps in Git |
| Evidence of create/connect PASS/FAIL | Credentials in reports or commits |
| Schema via reviewed migrations | Ad-hoc undocumented SQL as SoT |

Additional boundaries:

- **local dev only**;
- **no production**;
- **no real client data**;
- **no private metrics**;
- **no DB dumps in Git**;
- **no schema execution in this task**.

---

## 4. Required Before Creation

Before any future DB creation wave may proceed, confirm:

1. **MySQL access method** — which local account / socket-or-TCP path the operator will use (Laragon root or dedicated app user); do not publish credentials.
2. **User credentials** — stored only in local-only `.env.local` (see secrets policy); placeholders remain `CHANGE_ME` in Git.
3. **`.env.local` path** — recommended: runtime `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\.env.local` (not committed).
4. **Migration runner model** — accept [Migration Policy v0.1](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md) (SQL files + ledger; no auto-run on HTTP).
5. **Rollback / drop policy** — accept section 6 below for `iseo_report_hub_dev` only.
6. **Backup / export policy** — before destructive reset, export if the operator cares about current local rows (mysqldump or equivalent); dumps stay outside Git (Storage/incoming or Localhost-only).

---

## 5. Proposed Creation Procedure for Next Wave

**Do not execute in this charter wave.** Next wave (recommended) should:

1. Check whether `iseo_report_hub_dev` already exists (safe read-only existence check).
2. If absent, create database `iseo_report_hub_dev`.
3. Set charset `utf8mb4` and the **confirmed** collation.
4. Create local `.env.local` in the **runtime** location (Git-ignored); keep source `.env.example` as the committed template.
5. After operator review, apply **initial migration files only** (DB-01 + minimal DB-02 per schema plan) — not the full report schema.
6. Verify DB connection via CLI and/or a future health check that reports PASS/FAIL without printing credentials.
7. Record evidence in an Active Brain result + REPORT (no secrets).

---

## 6. Drop / Reset Policy

| Rule | Statement |
|------|-----------|
| Dev reset | `iseo_report_hub_dev` may be dropped/recreated **only** with explicit operator approval |
| Production | **Never** drop or mutate a production DB from this programme’s local charters |
| Backup | Before destructive reset, backup/export if local data matters to the operator |
| Git | Dumps and exports **must not** be committed to Active Brain |
| Scope | Drop/reset language in docs applies to **named local candidate only** |

---

## 7. SAFE UNKNOWN

- Exact Laragon MySQL **application** username/password to be used (not inspected; must not be recorded).
- Final **collation** choice between `utf8mb4_unicode_ci` and MySQL 8 `utf8mb4_0900_ai_ci` — confirm at SQL authoring time.
- Whether a dedicated MySQL user (vs Laragon root) will be created for the app — decide in the DB creation apply wave.
- Whether Phase 1A `/health` will gain a real DB probe in the same wave as creation, or later — **SAFE UNKNOWN** until that charter.
