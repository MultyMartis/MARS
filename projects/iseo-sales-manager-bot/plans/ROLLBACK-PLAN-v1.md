# ROLLBACK PLAN v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented rollback discipline  
**Aligns with:** MetaBOT safe-workflow-patch-protocol · MARS Survivability / GitGuard selective ops

---

## 1. Scope

Rollback covers future sandbox/production n8n + Sheets schema experiments. **Phase 2 creates docs only** — no runtime rollback action now.

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
