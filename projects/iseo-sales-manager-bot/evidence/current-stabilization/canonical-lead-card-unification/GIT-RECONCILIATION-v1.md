# GIT-RECONCILIATION-v1

**Task:** Canonical lead card patch — Git reconcile / commit / push only  
**Date:** 2026-08-28  
**Verdict:** **GIT RECONCILIATION PASS — LIVE CANONICAL CARD PATCH NOW CANONICALIZED — ZERO BOT TRAFFIC**

---

## Live vs local patch reconciliation

| Node | Live hash16 | Live code_len | Local file hash16 | Local file bytes | Match |
|---|---|---|---|---|---|
| Handle Callback Action | `509559A2821A2D13` | 49417 | `509559A2821A2D13` | 51574 | **YES** |
| Recent Leads | `4B432EE2655ABD44` | 10061 | `4B432EE2655ABD44` | 10595 | **YES** |

- Live snapshot source: `forensic/live-admin-snapshot.json` @ `2026-08-28T11:42:48.429Z`
- Local sources: `implementation/patches/HandleCallbackAction.canonical-card-unification.js`, `RecentLeads.canonical-card-unification.js`
- Hash algorithm: SHA-256 first 8 bytes → uppercase hex (16 chars), same as `run-01-live-admin-snapshot.mjs`
- Byte length differs from live `code_len` because live measures n8n node `parameters.jsCode` only; local patch files include full file bytes
- Live markers: `has_queue_open_compact: false` on Handle Callback Action; Recent Leads `has_archive_marker: true` (expected for closed/archival paths)

**Reconciliation result:** `LIVE PATCH == LOCAL PATCH ARTIFACTS` (hash match YES)

---

## Production state (read-only)

| Target | ID | Modified this task |
|---|---|---|
| Admin.dev | `wLrLp4WQHm1VJmxz` | **0** (patch already live before Git task) |
| Operational.dev | `xSnXPy8cEHoZw6xG` | **0** |
| MOD_B / Olya ACCESS | active | **0 mutations** |

---

## Worktree

- Path: `X:\AI MARS STORAGE\git-sync-iseo-sm-canonical-card-git-reconcile-20260828-201448\repo`
- Branch: `iseo/sm-canonical-card-git-reconcile-20260828-201448`
- Base: `origin/mars/canonical-post-recovery` @ `4daeb3b26cde30cbd50a538f14c953b057dfffc6`
- Dirty main `X:\AI MARS` **not used** for staging (foreign WIP excluded)

---

## Secret / PII audit (pre-stage)

| Check | Result |
|---|---|
| API keys / tokens in patches | none |
| n8n credentials in staged scope | none |
| Raw Telegram user IDs | none (only `user_hash12` in forensic JSON) |
| Customer phone/email | none raw; acceptance JSON uses synthetic fixture + redacted `+7***` / `[email]` |
| Private workflow backups | not staged |
| `private/`, `runtime/`, env files | not staged |

**secrets staged = 0**  
**PII staged = 0**

---

## Staged paths (exact allowlist)

1. `projects/iseo-sales-manager-bot/implementation/patches/HandleCallbackAction.canonical-card-unification.js`
2. `projects/iseo-sales-manager-bot/implementation/patches/RecentLeads.canonical-card-unification.js`
3. `projects/iseo-sales-manager-bot/evidence/current-stabilization/canonical-lead-card-unification/**` (31 files incl. this doc)
4. `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-canonical-lead-card-unification-v1.md`

---

## Commits and push

*(filled after commit/push wave)*

| Wave | SHA | Message |
|---|---|---|
| implementation | TBD | `fix(iseo-sales-manager-bot): unify canonical lead cards across entry points` |
| evidence/docs | TBD | `docs(iseo-sales-manager-bot): record canonical card production reconcile` |

**Final canonical SHA after push:** TBD  
**Push target:** `origin/mars/canonical-post-recovery` (no force)

---

## Zero-traffic and access counters

| Counter | Value |
|---|---|
| active test jobs at start | 0 |
| test jobs stopped before reconcile | 0 |
| Telegram messages sent | 0 |
| ADMIN_A test messages | 0 |
| MOD_B/Olya test messages | 0 |
| other moderator test messages | 0 |
| customer test messages | 0 |
| ACCESS mutations | 0 |
| Admin.dev modifications | 0 |
| Operational.dev modifications | 0 |
| live/local patch mismatches | 0 |
| secrets staged | 0 |
| PII staged | 0 |
| unrelated files staged | 0 |

---

## Soak

**SOAK RESET REQUIRED — CANONICAL CARD UNIFICATION PATCH** — not started in this task.

---

## Acceptance truth preserved

Partial acceptance remains: `status_callbacks` and `reminder_group` not re-tested; operator stopped further traffic. See `ACCEPTANCE-RESULTS-v1.md`, `UNKNOWN-v1.md`.
