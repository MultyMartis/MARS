# ROLLBACK PLAN v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented rollback discipline  
**Aligns with:** MetaBOT safe-workflow-patch-protocol · MARS Survivability / GitGuard selective ops

---

## 1. Scope

Rollback covers sandbox/production n8n + Sheets schema experiments.  
**Phase 3B–3B.2 facts:** production rollback source remains live `Sales-Manager-v2` (`h8I2Tl2yl4uzhUnB`, active). Dev copies: `i-SEO Sales Manager - Operational.dev` (`xSnXPy8cEHoZw6xG`) and `i-SEO Sales Manager - Admin.dev` (`wLrLp4WQHm1VJmxz`) — both inactive after Phase 3B.2 acceptance. Phase 3B.2 refreshed native Sheets mappings, removed the Parse Lead crypto runtime dependency, and closed Telegram sandbox acceptance; it performed no production cutover. Pre-dev raw backup under Storage `incoming/iseo-sales-manager-bot/backups/pre-dev-copy/`. Synthetic `SYNTHETIC_TEST` rows in v2 tabs are sandbox evidence (preserve unless a destructive charter names exact rows).

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

## 4. Rollback steps (n8n)

1. **Disable** broken .dev/prod workflow (active=false).
2. Re-import **last known good** export (or restore prior version in n8n UI).
3. Verify credentials still attached (active state drift check).
4. Confirm CONFIG `ai_enabled=false` until stable.
5. Smoke: `/health` + one synthetic `/test_lead` in dev only.
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

Admin.dev may remain **active** after polish acceptance (ops surface). Prefer deactivate → code-only PUT → reactivate when patching an active Admin graph; restore pre-patch export if Telegram Trigger registration fails. Production Sales-Manager-v2 remains sole intake owner until Phase 3C.
