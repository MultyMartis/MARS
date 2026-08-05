# REPORT — ISEO SALES MANAGER BOT PHASE 3G.2.2 UNIFIED REPLY PROFILE RESOLVER AND CONFIG TRUTH REPAIR

**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED
**Forbidden in this report:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Verdict

`COMPLETE — PROFILE RESOLVER UNIFIED; OPERATOR ACCEPTANCE PENDING`

ADMIN_A and MOD_A reply-profile columns were found to be silently wiped by routine `/start`/`/my_status` traffic on Admin.dev. Root cause proven from live execution on both actors. A single unified resolver contract (`iseo-reply-profile-resolver-v1.0`) now backs all eight profile read/write paths, with an anti-wipe projection fix and an auto-rehydrate mechanism that restores approved seed values the next time a covered command runs. CONFIG truth was separately corrected: a stale parser-version key and an ambiguous reporting-sync display were fixed. Offline harness `phase3g22-harness.mjs` **53/53 PASS**; regression `phase3g2-harness.mjs` **42/42 PASS**. AI OFF · reminders OFF · workflows created=0. Storage restore of ADMIN_A/MOD_A's live Sheets cells fires on the next covered Telegram command from each actor; the agent could not directly write Sheets or inject a Telegram update this session (no Sheets API token from n8n management API; webhook inject returned 404). Operator live Telegram acceptance is the remaining gate.

## 2. Scope

This phase repairs the reply-profile read/write architecture on Admin.dev (root cause + fix + rehydrate) and corrects `/config` display truth (parser version, resolver version, reporting-sync honesty, active-recipient count). It does not change access roles/status, does not restore MOD_B_REVOKED/MOD_C_REVOKED access, does not enable AI or reminders, and does not create or activate any workflow.

## 3. Starting live state

| Contour | State |
|---------|-------|
| Operational.dev | active, 45 nodes, sole Gmail intake |
| Admin.dev | active, 85 nodes, same workflow patched in place |
| Sales-Manager-v2 | inactive |
| Profiles (pre-forensic observation) | 1 ADMIN_A intermittently blank · 2 MOD_B_REVOKED Оля disabled/revoked (intact) · 3 MOD_A intermittently blank · 4 MOD_C_REVOKED Никита disabled/revoked (intact) |
| AI | OFF |
| Reminders | OFF |

## 4. Operator-observed symptom

`/reply_profile 3` and moderator `/start` could still show «Михаил» from pre-wipe reads within the same operator window; `/my_reply_profile` issued after the wipe on the same identity showed blanks. This apparent inconsistency is the finding that triggered the forensic in §5–§10.

## 5. Authoritative profile storage forensic

Single authoritative store confirmed: `ACCESS_CONTROL`, additive columns, one row per stable identity. 4 authoritative profile rows, 0 duplicate rows. No secondary or shadow profile table exists. Full detail: `evidence/phase3g2-2/AUTHORITATIVE-PROFILE-STORAGE-FORENSIC-v1.md`.

## 6. Profile read-path matrix

Eight distinct code paths read or project ACCESS_CONTROL profile fields: `Check User Authorization`, `/reply_profiles`, `/reply_profile N`, `/my_reply_profile`, `/start` reply-name line, `/start`/`/my_status` upsert, Operational recipient expansion, `/config` Config Summary. Pre-patch, 6 of 8 used their own field mapping (divergent); post-patch, 8 of 8 resolve through one contract. Full detail: `evidence/phase3g2-2/PROFILE-READ-PATH-MATRIX-v1.md`.

## 7. ADMIN_A profile loss — root cause

Proven from live execution: `Check User Authorization`'s `rowFromSheet()` projection used a fixed field allowlist that excluded `reply_profile_*` columns; the subsequent `/start`/`/my_status` last-seen upsert wrote ACCESS_CONTROL via `appendOrUpdate` using a mapping that mixed top-level core fields with `access_upsert.*` profile fields but did not carry the actual profile values forward — so the same execution that authenticated ADMIN_A also wiped ADMIN_A's own profile columns on that row. No duplicate row, no renumbering; `reply_profile_number=1` remained intact throughout. Full detail: `evidence/phase3g2-2/ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md`.

## 8. MOD_A self-profile root cause

Identical mechanism, proven separately from MOD_A's own live execution: the defect is role-agnostic (lives in shared `Check User Authorization` and the shared last-seen upsert), so any active Admin or moderator sending `/start`/`/my_status` triggers the same wipe on their own row. `reply_profile_number=3` remained intact. Full detail: `evidence/phase3g2-2/MOD-A-SELF-PROFILE-ROOT-CAUSE-v1.md`.

## 9. Why revoked profiles kept their numbers

MOD_B_REVOKED (2) and MOD_C_REVOKED (4) kept their full profile data intact because they do not run an active, authenticated `/start`/`/my_status` upsert in the current window — the wipe is triggered only on rows that actually execute that command path. This is consistent with the numbering contract (numbers are immutable and independent of upsert activity), not a separate repair.

## 10. Point-in-time read ordering explanation

`/reply_profile 3` and moderator `/start` showing «Михаил» within the same operator session as a subsequent blank `/my_reply_profile` is explained by each Telegram command performing its own fresh Sheets read at dispatch time: a read before the wiping upsert executed against that row returns the intact value; a read after returns the wiped value. This is a single-storage, point-in-time ordering artifact — not evidence of two storage locations, a resolver race, or values shifting between rows.

## 11. Unified resolver contract

`resolveReplyProfile(row)` (`implementation/runtime-libs/reply-profile-resolver-v1.mjs`, `resolver_version=iseo-reply-profile-resolver-v1.0`) is now the single authoritative resolution function backing all eight read paths, directly or via the compatible `resolveRecipientReplyProfile` alias in `reply-profile-lib.mjs`. Full contract: `architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md`; implementation notes: `implementation/REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md`; evidence: `evidence/phase3g2-2/UNIFIED-RESOLVER-CONTRACT-v1.md`.

## 12. Anti-wipe fix

`REPLY_PROFILE_ACCESS_FIELDS` is the explicit allowlist of profile columns that must survive any ACCESS_CONTROL row projection (`pickReplyProfileFields`). `Check User Authorization` now includes this allowlist in its output instead of the fixed field set that previously omitted it — closing the read-side half of the defect.

## 13. Auto-rehydrate mechanism

`buildProfileRehydratePatch` / `mergeRehydrateIntoUpsert` resolve the current row, and if profile number/name/enabled-flag are missing, fill only the missing fields from the approved seed for that stable identity (matched by known display cue, never invented), stamped `reply_profile_updated_by=system_rehydrate`. Invoked before formatting `/reply_profiles`, `/reply_profile N`, `/my_reply_profile`, the `/start` reply-name line, and before every `/start`/`/my_status` upsert — closing the write-side half of the defect.

## 14. Fail-closed guarantee

Rehydrate never creates a new row, never changes `role`/`status`, and never invents a name for an identity with no approved seed match. Proven under nickname-only, display-name-only, and username-only fallback attempts — all resolve to `reply_sender_name=''`, `personalization_ready=false`. Harness checks #11–14, #51–53 PASS.

## 15. ADMIN_A restore status

Patch deployed; offline harness proves rehydrate restores «Андрей», `reply_sender_enabled=true` for the exact wiped-row shape captured in the forensic. Direct Google Sheets API restore (n8n management API token) was **not available** to the agent this session; a Telegram webhook inject attempt returned **404**. Authoritative live restore of ADMIN_A's actual ACCESS_CONTROL cells fires automatically the next time ADMIN_A sends `/reply_profiles`, `/reply_profile 1`, `/my_reply_profile`, or `/start`. Full detail: `evidence/phase3g2-2/ADMIN-A-RESTORE-v1.md`.

## 16. MOD_A self-profile acceptance

Offline acceptance criteria (client name «Михаил» never «Мопс», enabled state, role label, resolver-version consistency, no false-disabled, no blank after rehydrate, no «Мопс» in client copy) — **8/8 PASS** offline. Live Telegram confirmation from MOD_A remains **PENDING**. Full detail: `evidence/phase3g2-2/MOD-A-SELF-PROFILE-ACCEPTANCE-v1.md`.

## 17. Profile number invariants

`reply_profile_number` proven immutable through the wipe/rehydrate cycle, not only at initial seed time: 4 authoritative rows, 0 duplicates, 0 renumbering, numbers independent of Sheets row order and stable identity value. Revoked profiles (2, 4) remain disabled/ineligible after rehydrate. Full detail: `evidence/phase3g2-2/PROFILE-NUMBER-INVARIANTS-v1.md`.

## 18. Config truth forensic

CONFIG sheet key held a stale parser version (`sm-parser-v3.2`) while the live Operational.dev `Parse Lead` node stamps `sm-parser-v3.3` — no automatic re-sync exists for this cell when the live parser version changes without a matching CONFIG write. Reporting-sync display is corrected to state honestly that no active reporting-sync nodes exist in Operational.dev (**выключена**), rather than being silently omitted. Stats timestamp conversion verified: ISO `2026-08-05T13:02:57.000Z` → `05.08.2026 16:02 МСК`. Full detail: `evidence/phase3g2-2/CONFIG-TRUTH-FORENSIC-v1.md`.

## 19. Config human display

`/config` (Admin) now displays: contour state, stats start date, live parser version (`sm-parser-v3.3`), card format version, personalization version, resolver version (`iseo-reply-profile-resolver-v1.0`), AI state, reminder state, reporting-sync state (explicit «выключена»), and active-recipient count (2). No Telegram IDs, workbook IDs, or secrets in any line; unavailable values render as «не задано». Full detail: `evidence/phase3g2-2/CONFIG-HUMAN-DISPLAY-v1.md`.

## 20. Operational personalization regression

Operational.dev required no structural node changes for the resolver unification — its recipient-personalization logic already read ACCESS_CONTROL profile fields directly rather than through the Admin.dev `Check User Authorization` path that caused the wipe. Regression-checked: personalized intro sentences for ADMIN_A/MOD_A unchanged and correct, no «Мопс» in client copy, node count unchanged (45), `Parse Lead` version unchanged (`sm-parser-v3.3`). A version-stamp field (`resolver_version=iseo-reply-profile-resolver-v1.0`) was added to `Expand Delivery Recipients` for traceability only. Full detail: `evidence/phase3g2-2/OPERATIONAL-PERSONALIZATION-REGRESSION-v1.md`.

## 21. Repair deployed (workflow patch summary)

Admin.dev (same workflow, 85 nodes retained): `Check User Authorization` anti-wipe + rehydrate; `Reply Profile Commands` unified resolver v1.0 + auto-rehydrate on profile commands; `Config Summary` Moscow timestamp + parser truth `sm-parser-v3.3` + resolver-version line; `Start` fail-closed reply-name line; last-seen upsert profile fields sourced from top-level Prepare output. Operational.dev (same workflow, 45 nodes retained): `Expand Delivery Recipients` resolver-version label `iseo-reply-profile-resolver-v1.0`; `Parse Lead` remains `sm-parser-v3.3`. Sales-Manager-v2 inactive. Workflows created = 0. AI OFF. Reminders OFF.

## 22. Production invariants

| Invariant | Value |
|-----------|-------|
| Operational.dev | active, 45 nodes |
| Admin.dev | active, 85 nodes, same workflow |
| Sales-Manager-v2 | inactive |
| AI | OFF |
| Reminders | OFF |
| Workflows created | 0 |
| Access-role changes | 0 |
| Production leads modified | 0 |
| Historical drafts modified | 0 |

Full detail: `evidence/phase3g2-2/PRODUCTION-INVARIANTS-v1.md`.

## 23. Final workflow state

Admin.dev nodes touched: Check User Authorization, Reply Profile Commands, Config Summary, Start, last-seen upsert. Operational.dev: `Expand Delivery Recipients` version label only, no structural change. Runtime libraries: `reply-profile-resolver-v1.mjs` (new), `reply-profile-lib.mjs` (updated), `reply-profile-commands-v1.mjs` (updated), `phase3g22-harness.mjs` (new). Full detail: `evidence/phase3g2-2/FINAL-WORKFLOW-STATE-v1.md`.

## 24. Harness results

`implementation/harness/phase3g22-harness.mjs` — **53/53 PASS** (row/identity integrity, name/enabled restoration, fail-closed fallback rejection, command surfaces, resolver-version consistency, config truth, AI/reminders OFF, no secrets, mutation regression, contour invariants, personalization draft correctness, rehydrate stable-identity keying, name validation). Regression `implementation/harness/phase3g2-harness.mjs` — **42/42 PASS** (Phase 3G.2 numbering/text-contract baseline unaffected). Combined: **95/95 PASS**. Full detail: `evidence/phase3g2-2/HARNESS-RESULTS-v1.md`.

## 25. Safety counters

| Counter | Value |
|---------|------:|
| authoritative profile rows | 4 |
| duplicate profile rows | 0 |
| stable profile numbers | 4 |
| blank active profile numbers (after rehydrate contract) | 0 |
| blank active reply names (after rehydrate) | 0 |
| divergent profile read paths | 0 (unified contract) |
| unsafe fallbacks | 0 |
| active personalized profiles | 2 |
| revoked personalized profiles enabled | 0 |
| config values verified | 1 (verified set: parser / resolver / reporting sync / active recipients / stats epoch) |
| AI state | OFF |
| reminders state | OFF |
| access changes | 0 |
| production leads modified | 0 |
| historical drafts modified | 0 |
| workflows created | 0 |
| real leads lost | 0 |
| real leads duplicated | 0 |

## 26. Files changed — evidence

Under `projects/iseo-sales-manager-bot/evidence/phase3g2-2/`: `AUTHORITATIVE-PROFILE-STORAGE-FORENSIC-v1.md`, `PROFILE-READ-PATH-MATRIX-v1.md`, `ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md`, `MOD-A-SELF-PROFILE-ROOT-CAUSE-v1.md`, `UNIFIED-RESOLVER-CONTRACT-v1.md`, `ADMIN-A-RESTORE-v1.md`, `MOD-A-SELF-PROFILE-ACCEPTANCE-v1.md`, `PROFILE-NUMBER-INVARIANTS-v1.md`, `CONFIG-TRUTH-FORENSIC-v1.md`, `CONFIG-HUMAN-DISPLAY-v1.md`, `OPERATIONAL-PERSONALIZATION-REGRESSION-v1.md`, `PRODUCTION-INVARIANTS-v1.md`, `HARNESS-RESULTS-v1.md`, `FINAL-WORKFLOW-STATE-v1.md`, `PHASE3G2-2-ACCEPTANCE-RECEIPT-v1.md` (15 files, new).

## 27. Files changed — architecture, implementation, runtime

New: `architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md`, `implementation/REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md`, `implementation/runtime-libs/reply-profile-resolver-v1.mjs`, `implementation/harness/phase3g22-harness.mjs`. Updated (already in working tree prior to this session, left intact): `implementation/runtime-libs/reply-profile-lib.mjs`, `implementation/runtime-libs/reply-profile-commands-v1.mjs`.

## 28. Files changed — documentation (additive notes)

`README.md`, `OPERATIONAL-INDEX.md`, `product/CURRENT-PRODUCTION-BASELINE-v1.md`, `product/KNOWN-LIMITATIONS-v1.md`, `architecture/REPLY-PROFILE-CONTRACT-v1.md`, `architecture/REPLY-PROFILE-NUMBERING-v1.md`, `architecture/RECIPIENT-PERSONALIZED-REPLIES-v1.md`, `architecture/TELEGRAM-TEXT-CONTRACT-v2.md`, `implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md`, `implementation/USER-VISIBLE-TEXT-REGISTRY-v1.md`, `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`, `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`, `guides/TELEGRAM-COMMAND-REFERENCE-v1.md`, `guides/OPERATOR-RUNBOOK-v1.md` — all additive Phase 3G.2.2 sections; no prior content rewritten.

## 29. Report

This file: `reports/REPORT-iseo-sales-manager-bot-phase3g2-2-profile-resolver-and-config-truth-v1.md`.

## 30. Security validation

No Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw Telegram updates, or credentials appear in any file created or modified this phase. Sanitized actor labels (ADMIN_A / MOD_A / MOD_B_REVOKED / MOD_C_REVOKED) used throughout. Node-level internal hashes and workflow IDs were intentionally omitted from all new evidence, architecture, and implementation files in this phase (stricter sanitization than some historical phase documents, which predate this instruction).

## 31. Commit — resolver unification

`d2665fac` — `fix(iseo-sales-manager-bot): unify reply profile resolution`

## 32. Commit — config truth alignment

This commit — `fix(iseo-sales-manager-bot): align config with live baseline` (config evidence + report tip).

## 33. Push

Pushed to `origin/mars/canonical-post-recovery` without force (see closeout after push).

## 34. Remaining operator actions / stop condition

**Operator actions:**

1. As ADMIN_A: send `/start`, then `/my_reply_profile` — confirm name «Андрей», «Персональный ответ: включён».
2. As MOD_A: send `/start`, then `/my_reply_profile` — confirm name «Михаил», «Персональный ответ: включён», and confirm «Мопс» does not appear.
3. As Admin: send `/config` — confirm parser version `sm-parser-v3.3`, resolver-version line present, reporting-sync state shown explicitly.
4. Record visual sign-off in `evidence/phase3g2-2/PHASE3G2-2-ACCEPTANCE-RECEIPT-v1.md`.

**Stop condition:** Engineering stop reached — root causes proven from live execution for both ADMIN_A and MOD_A; unified resolver contract deployed across all 8 read paths; anti-wipe + auto-rehydrate fix live on the same Admin.dev workflow; CONFIG truth corrected; offline harness 53/53 PASS plus 42/42 regression PASS; AI/reminders OFF; production invariants hold; zero access changes; zero lead impact. Awaiting operator Telegram confirmation for ADMIN_A, MOD_A, and `/config` before closing Phase 3G.2.2 as fully operator-accepted.
