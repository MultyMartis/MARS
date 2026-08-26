# REPORT — ISEO Sales Manager Bot — group filter + legacy test cleanup v1

## 1. Verdict

**`GROUP FILTER LIVE PASS — PROVEN LEGACY TEST POLLUTION REMOVED`**

## 2. Natural 2026-08-26 evidence

Exec **40846** at `2026-08-26T07:00:52Z` (10:00 Europe/Moscow). Digest: pending **22**, Audit **14**, SEO **1**, Other **7**, older **18**. Keyboard callbacks: `sm:g:c:aa2771a403` / `ade3cbdc59` / `e130bfb8c3` / `o24` / `all`.

## 3. Scheduled keyboard acceptance

`NATURAL SCHEDULED INLINE KEYBOARD DELIVERY = PASS`

## 4. Group filter defect

Live SEO click (`sm:g:c:ade3cbdc59`) returned **27** leads (expected 1). Audit/All similarly inflated. Callbacks not collapsed (Audit ≠ SEO titles), but sets wrong vs digest.

## 5. Exact root cause

1. **`AUTHORITATIVE_SELECTOR_DIVERGENCE`** — `group_open` lacked reminder `isTest`/archive/unique-bkey selection.  
2. **`FALLBACK_TO_GENERIC_GROUP`** — Aggregate collapsed `reply_text` to `answer_text` (`Группа`).  
3. Ambiguous verify on synthetic duplicate `lead_synth_p3b1_c01`.

Repaired on Admin.dev (`wLrLp4WQHm1VJmxz`): `AUTHORITATIVE_GROUP_PENDING`, `DIGEST_GROUP_PRESERVE_REPLY`, `readOnlyAmbiguous`. `sha16_nodes=62CB6CEC5ED92C86`, nodes=111.

## 6. Generic Group responses

Proven Aggregate overwrite; fixed; post-accept `generic_gruppa_replies = 0`.

## 7. Lead verification error

Exec 40889 / `sm:q:…` → ambiguous synthetic duplicates. Cleanup + read-only pick-latest.

## 8. Synthetic/test inventory

CLEAN 155 rows / 112 unique. Suspected artificial ≈80+ PROVEN_SYNTHETIC row hits; SAFE_UNKNOWN ≈12–13; PRODUCTION_REAL 62.

## 9. Provenance classification

| Class | Count (approx) |
|-------|---------------:|
| PROVEN_SYNTHETIC | 80 |
| PROVEN_TEST | (included in proven via PROBE_/msg_probe_) |
| PRODUCTION_REAL | 62 |
| SAFE_UNKNOWN | 12–13 |

## 10. SAFE_UNKNOWN

Left untouched (mutations = 0). Name-only candidates not deleted.

## 11. Backup

Private PRE/POST Admin raw JSON under wave `backups\`; manifests in evidence. No secrets in Git.

## 12. Cleanup execution

Pass1 by `lead_id` + Pass2 by `row_number`. **proven_pending_after = 0**. Artificial rows archived/excluded from production pending: unique proven pending 49 + 23 duplicate rows.

## 13. Post-cleanup authoritative pending

All **22** / Audit **14** / SEO **1** / Other **7** / older24 **19**. Proven artificial pending **0**.

## 14. Group set-equality proof

`group_set_mismatches = 0` for Audit/SEO/Other/older24/All (ID sets, not counts alone).

## 15. ADMIN_A acceptance

`2026-08-26T10-00-11Z` — digest + SEO/Audit/Other groups + SEO lead; claims/`last_window` untouched; mods/customers/AI = 0; `Группа` = 0; ok.

## 16. Reminder subsystem status

Keyboard delivery PASS. Group filter correctness PASS post-fix. **Not** fully closed: no 48h soak; soak explicitly out of scope.

## 17. Remaining CLEAN duplicate forensic

Real/unknown CLEAN duplicates deferred to next phase: `CLEAN DUPLICATE SOURCE FORENSIC / FIX`.

## 18. Production invariants

ACCESS unchanged; AI OFF; schedule/dedupe/`last_window` not altered by acceptance; Operational.dev cadence unchanged.

## 19. Git

Worktree: `X:\AI MARS STORAGE\git-sync-iseo-sm-group-filter-test-cleanup-20260826-162215\repo`  
Branch wave → push `origin/mars/canonical-post-recovery` (no force). Dirty main foreign WIP untouched. Scope: `projects/iseo-sales-manager-bot/**` evidence + report.

## 20. Next stabilization gate

Start dedicated CLEAN duplicate source forensic when chartered. Reminder final closure after soak only if separately authorized.

---

## Counters

| Counter | Value |
|---------|------:|
| suspected artificial records | ~80+ |
| PROVEN_SYNTHETIC | 80 |
| PROVEN_TEST | folded into proven |
| PRODUCTION_REAL | 62 |
| SAFE_UNKNOWN | 12–13 |
| artificial removed/archived/excluded | 49 unique + 23 rows |
| proven artificial pending after cleanup | **0** |
| Audit expected / actual | 14 / 14 |
| SEO expected / actual | 1 / 1 |
| Other expected / actual | 7 / 7 |
| older24 expected / actual | 19 / 19 |
| All expected / actual | 22 / 22 |
| group set mismatches | **0** |
| generic Группа after fix | **0** |
| lead verify errors after fix (acceptance) | **0** |
| wrong lead resolutions (acceptance) | **0** |
| production-real mutated by cleanup | **0** |
| SAFE_UNKNOWN mutated | **0** |
| moderator messages | **0** |
| customer messages | **0** |
| AI calls | **0** |
