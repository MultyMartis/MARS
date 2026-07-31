# ROLLBACK PLAN v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented rollback discipline  
**Aligns with:** MetaBOT safe-workflow-patch-protocol · MARS Survivability / GitGuard selective ops

---

## 1. Scope

Rollback covers sandbox/production n8n + Sheets schema experiments.  
**Phase 3C facts (2026-07-31):** production intake owner is `i-SEO Sales Manager - Operational.dev` (`xSnXPy8cEHoZw6xG`, active, AI OFF). Rollback source is inactive `Sales-Manager-v2` (`h8I2Tl2yl4uzhUnB`). Admin.dev (`wLrLp4WQHm1VJmxz`) remains active. Pre-cutover raw backups under Storage `incoming/iseo-sales-manager-bot/phase3c-local/backups/`. Synthetic `SYNTHETIC_TEST` rows in v2 tabs remain sandbox evidence (preserve unless a destructive charter names exact rows).

---

## 2. Backup before any live/sandbox graph replace

| Artifact | Action |
|----------|--------|
| Operational.dev JSON | Export full workflow; store under gitignored `raw/` or Storage incoming; sanitize before commit |
| Admin.dev JSON | Same |
| CONFIG tab | Snapshot values |
| CLEAN/RAW headers | Snapshot schema |
| Credential mapping notes | Names only — no secrets |

Naming: `backup-YYYYMMDD-HHMM-operational.dev.json` (local).

---

## 3. Rollback triggers

- Telegram spam / entity crash storm
- Gmail label loops (re-processing flood)
- Sheets corruption / `#ERROR!` mass writes
- AI cost spike (unexpected multi-calls)
- Accidental client messaging path
- Wrong chat_id fan-out

---

## 4. Rollback steps (n8n) — Phase 3C production cutover

If Operational.dev must be rolled back after Phase 3C:

1. **Disable** Operational.dev (`xSnXPy8cEHoZw6xG`, active=false); verify inactive.
2. Restore CONFIG: `environment=dev` (or rollback marker), `ai_enabled=false`, `operational_workflow_active=false`, keep `admin_workflow_active=true`.
3. **Reactivate** Sales-Manager-v2 (`h8I2Tl2yl4uzhUnB`); verify active.
4. Verify only Sales-Manager-v2 processes Gmail (Operational.dev inactive).
5. Keep Admin.dev active.
6. Record failure + `evidence/phase3c/PHASE3C-ROLLBACK-RECEIPT-v1.md`.
7. Do **not** retry cutover automatically.

General sandbox restore (non-cutover):

1. **Disable** broken .dev workflow (active=false).
2. Re-import **last known good** export (or restore prior version in n8n UI).
3. Verify credentials still attached (active state drift check).
4. Confirm CONFIG `ai_enabled=false` until stable.
5. Smoke: `/health` (+ deferred `/test_lead` only when explicitly gated).
6. Record LEAD_EVENTS / REPORT evidence.

Do **not** `robocopy /MIR` or wipe Sheets. Prefer forward-fix schema with legacy tabs retained.

---

## 5. Sheets rollback

| Situation | Action |
|-----------|--------|
| Bad v2 tab | Point CONFIG/graph back to previous tab names |
| Bad rows | Soft-delete marker / filter — avoid mass delete without destructive charter |
| CONFIG wrong | Restore from snapshot values via Admin or manual |

---

## 6. Git / MARS

- Docs rollback = normal git revert **only** when chartered; default no commit in Phase 2.
- Never stage foreign WIP.
- Never `git clean` / hard reset for this product.

---

## 7. Communication

Notify Admin chat: rollback executed, AI forced OFF, intake paused if needed.

---

*Related: N8N-CHANGE-PLAN-v1 · CONFIGURATION-MODEL-v1.*


## Phase 3B.4 activation note

Admin.dev may be temporarily activated with Telegram Trigger enabled for operator-private command acceptance. Always deactivate Admin.dev after the window. Do not activate Operational.dev for that test. Production Sales-Manager-v2 remains the sole active intake owner until an explicit cutover charter.

## Phase 3B.5 note

Admin.dev may remain **active** after polish acceptance (ops surface). Prefer deactivate → code-only PUT → reactivate when patching an active Admin graph; restore pre-patch export if Telegram Trigger registration fails.

## Phase 3C note

Operational.dev is the sole Gmail intake owner after cutover. Sales-Manager-v2 must remain inactive unless this rollback sequence is executed. **Never activate Sales-Manager-v2 while Operational is active.** Do not run both operational workflows active in parallel. Recommended later display names (after stable acceptance): `i-SEO Sales Manager - Operational` / `i-SEO Sales Manager - Admin` — deferred while references remain clear with `.dev` suffixes.

## Phase 3C.1 note

First real website test was **delivered** but **not eligible** (Trash + missing incoming label). Do not untrash/relabel broadly. Prefer a new website test after confirming Gmail incoming-label automation. Observability patches on OPS/Admin are forward-compatible; rollback still follows Phase 3C cutover steps if intake must revert to Sales-Manager-v2.

## Phase 3C.2 note

Gmail filter audit: **0** Trash filters; incoming-label filters already correct (no Gmail filter mutation). Historical Trash actor remains SAFE UNKNOWN (external/manual). OPS repairs (Classify base lead, Format from Classify, Telegram chatId from CONFIG, Gmail messageId refs) stopped reprocess flood and enabled first real lead finalization. Pre-patch backups under Storage `incoming/iseo-sales-manager-bot/phase3c2-local/backups/`. Rollback still follows Phase 3C cutover steps if intake must revert to Sales-Manager-v2.

## Phase 3D note

Telegram delivery idempotency + bounded retry (max 5) patched on Operational.dev (`IF Need Telegram Send`, `Telegram Skip Pass`, CONFIG keys `tg_delivered:*` / `tg_attempts:*`). Exact DEDUP normalized_value matching restored in Classify. Pre-patch backup: Storage `incoming/iseo-sales-manager-bot/phase3d-local/backups/OPS.before-phase3d-idempotency.raw.json`. Rollback of intake still follows Phase 3C cutover (deactivate Operational → activate Sales-Manager-v2 only after dual-active check). Do not remove idempotency nodes during emergency rollback unless reverting to a known pre-3D export intentionally.

## Phase 3D.3 note

Callback rollback (inline lead-action buttons / `/leads` / `sm-msg-v2` formatter/keyboard) = **restore the pre-3D.3 Admin.dev and Operational.dev exports from their Storage backups**, not an invented alternate workflow or ad hoc node deletion. Do not hand-patch the callback graph or lifecycle Sheets columns as a "rollback" — restore from backup, verify credentials still attached, and confirm CONFIG `ai_enabled=false` before resuming. Intake-owner rollback (Operational.dev ↔ Sales-Manager-v2) is unaffected and still follows the Phase 3C cutover sequence above.
