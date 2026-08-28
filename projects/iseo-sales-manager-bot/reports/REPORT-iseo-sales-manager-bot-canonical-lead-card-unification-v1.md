# REPORT — ISEO Sales Manager Bot: Canonical Lead Card Unification v1

**Task:** Canonical lead card UX unification on Admin.dev  
**Closeout:** 2026-08-28 (no further live bot traffic per operator)  
**Verdict:** **CANONICAL LEAD CARD LIVE PASS — MOD_B RESTORED — OLYA PRODUCTION STATE PRESERVED — ACCEPTANCE PARTIAL (operator: no further test traffic)**

---

## 1. Executive summary

Admin.dev (`wLrLp4WQHm1VJmxz`) was patched to unify pending lead card rendering across **queue_open** (`sm:q:`) and **`/leads N`**. Deploy succeeded with OPS nodes unchanged. Core UX acceptance **passed** for both charter defect areas. Full harness `all_pass` is **false** due to two deferred sections; operator forbade additional live tests. MOD_B (Olya) was temporarily revoked, then **restored to active**.

---

## 2. Scope

| In scope | Out of scope |
|---|---|
| Admin.dev card render paths | Operational.dev permanent change |
| Handle Callback Action, Recent Leads | New soak window |
| MOD_B isolation + restore | Re-run acceptance after stop |
| Evidence + report | Traffic to Olya/customers |

---

## 3. Defects addressed

| Entry | Problem | Fix status |
|---|---|---|
| Reminder / `sm:q:` | Reduced card; standalone `Лид` | **Fixed** — full card, `Карточка`, actions |
| `/leads N` | Archival header; no actions on pending | **Fixed** — `📋 Лид` + keyboard |
| Multiple render paths | Entry-driven | **Partial** — two nodes unified; full renderer refactor not claimed |

---

## 4. Deploy

- **When:** 2026-08-28T11:09:44Z  
- **Patches:** `HandleCallbackAction.canonical-card-unification.js`, `RecentLeads.canonical-card-unification.js`  
- **OPS unchanged:** 45 nodes, connection hash match  
- **Backups:** PRE/POST under STORAGE `canonical-card-unification-local/backups/`

---

## 5. MOD_B isolation

| Phase | Time | Status |
|---|---|---|
| Initial | 11:00:46Z | active |
| Revoked | 11:07:19Z | revoked |
| Restored | 11:38:55Z | **active** |

**MOD_B_ACCESS_FINAL == active:** 1

---

## 6. Olya integrity

- Post-restore baseline: **14** leads (1 pending, 13 spam)  
- Production pending lead not used in tests  
- Pre-revoke snapshot: **SAFE UNKNOWN** (overwritten)

---

## 7. Acceptance (last run @ 12:04:51Z)

| Section | Result |
|---|---|
| leads | PASS |
| queue_open | PASS |
| clean_dedup | PASS |
| mod_b isolation | PASS |
| status_callbacks | FAIL (harness) |
| reminder_group | FAIL (harness) |

**No further runs** after operator stop.

---

## 8. Core UX proof

- Pending `/leads 3`: all `📋 Лид`, buttons present, `incorrectly_archival: 0`  
- `queue_open`: `answer_text: Карточка`, `pending_actions`, `standalone_lid: 0`

---

## 9. Deferred verification

1. **status_callbacks** — OPS synth inject HTTP 500; harness fix prepared, not re-run  
2. **reminder_group** — digest probe showed digest works (19 pending); acceptance parse issue

---

## 10. Operator constraint

All closeout after stop uses forensic artifacts only. **Zero** new bot messages.

---

## 11. Operational.dev

Not permanently modified. `ops_nodes_unchanged: true` on Admin.dev deploy.

---

## 12. SOAK

**SOAK RESET REQUIRED** — do not continue prior soak without reset (see `SOAK-RESET-REQUIRED-v1.md`).

---

## 13. Artifacts

**Evidence:** `evidence/current-stabilization/canonical-lead-card-unification/` (20 × `.md` + `forensic/*.json`)  
**Patches:** `implementation/patches/*.canonical-card-unification.js`  
**Worktree:** `git-sync-iseo-sm-canonical-card-unification-20260828-180215`

---

## 14. Counters

| Metric | Value |
|---|---|
| Evidence files | 20 |
| MOD_B revoked / restored | 1 / 1 |
| Olya baseline (post-restore) | 14 |
| Standalone `Лид` post-fix | 0 |
| acceptance all_pass | false |

---

## 15. UNKNOWN

See `UNKNOWN-v1.md` — pre-revoke Olya diff; live status_callbacks; reminder_group formal pass.

---

## 16. SECURITY

See `SECURITY-RISK-v1.md` — no open critical risk; MOD_B restored.

---

## 17. Git (pre-reconcile)

Patches and evidence copied to main repo tree. Initial closeout had **no commit**. Git reconcile task (2026-08-28) canonicalized allowlisted artifacts only — see §22.

---

## 18. Recommended follow-up

1. Optional acceptance re-run for `status_callbacks` + `reminder_group` only (ADMIN_A, MOD_B active)  
2. Soak reset per charter  
3. Commit evidence + patches when operator authorizes

---

## 19. Changed files (this closeout)

**Created/updated under `projects/iseo-sales-manager-bot/`:**

- `implementation/patches/HandleCallbackAction.canonical-card-unification.js`
- `implementation/patches/RecentLeads.canonical-card-unification.js`
- `evidence/current-stabilization/canonical-lead-card-unification/*.md` (20)
- `evidence/.../forensic/*.json` (copies)
- `reports/REPORT-iseo-sales-manager-bot-canonical-lead-card-unification-v1.md`

---

## 20. Git status

Foreign WIP elsewhere in repo unchanged. This task scope: `projects/iseo-sales-manager-bot/**` only.

---

## 21. Final verdict line

**CANONICAL LEAD CARD LIVE PASS — MOD_B RESTORED — OLYA PRODUCTION STATE PRESERVED — ACCEPTANCE PARTIAL (operator: no further test traffic)**

Core card UX fixes are **live and proven** on Admin.dev for `/leads` and queue_open. Full charter acceptance is **partial**; operator explicitly stopped all further bot traffic. MOD_B is **restored active** per forensic. **SOAK RESET REQUIRED.**

---

## 22. Git reconciliation closeout

**When:** 2026-08-28 (Git reconcile task — zero bot traffic)

### Production before Git

- Canonical card patch **already deployed** on Admin.dev (`wLrLp4WQHm1VJmxz`) @ `2026-08-28T11:09:44Z`
- This Git task made **no new production change** (read-only live verification only)

### Live vs repo

- Handle Callback Action hash16: `509559A2821A2D13` — live == local patch artifact
- Recent Leads hash16: `4B432EE2655ABD44` — live == local patch artifact
- Evidence: `evidence/current-stabilization/canonical-lead-card-unification/GIT-RECONCILIATION-v1.md`

### Git wave

- Worktree: `git-sync-iseo-sm-canonical-card-git-reconcile-20260828-201448`
- Base: `origin/mars/canonical-post-recovery` @ `4daeb3b2`
- Commits: see `GIT-RECONCILIATION-v1.md` for SHAs after push
- **No force push**; foreign WIP on dirty main not staged

### Zero-traffic / access

| Counter | Value |
|---|---|
| Telegram messages sent | 0 |
| ACCESS mutations | 0 |
| Admin.dev modifications | 0 |
| Operational.dev modifications | 0 |

Olya (MOD_B) **ACTIVE** — untouched in Git task.

### Soak

**SOAK RESET REQUIRED** — not started; separate operator approval required before next soak.

### Acceptance limitations (unchanged)

- `status_callbacks` — not re-tested after harness fix prep
- `reminder_group` — not re-tested
- Operator stopped further live test traffic
- Verdict remains: **ACCEPTANCE PARTIAL (NO FURTHER TEST TRAFFIC)**

### Git task verdict

**GIT RECONCILIATION PASS — LIVE CANONICAL CARD PATCH NOW CANONICALIZED — ZERO BOT TRAFFIC**
