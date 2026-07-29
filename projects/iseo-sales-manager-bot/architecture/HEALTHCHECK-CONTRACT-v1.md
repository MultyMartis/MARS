# HEALTHCHECK CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Entry:** Admin `/health`  
**Status:** documented — non-destructive probes only

---

## 1. Principles

- Healthcheck **observes**; it does not process real unread leads.
- No Gmail label mutations.
- No production CLEAN/RAW lead appends.
- No client contact.
- No AI call when AI is OFF.
- No AI call when `health_ai_probe_enabled=false` even if AI ON (unless both true).
- Never expose credentials, tokens, or spreadsheet secrets beyond “reachable”.

---

## 2. Checks (ordered)

| # | Check | Pass criteria | Failure code |
|---|-------|---------------|--------------|
| 1 | CONFIG readable | Tab read returns keys including `ai_enabled` | `cfg_read` |
| 2 | Gmail credential/path available | Credential resolves / lightweight metadata probe **without** fetching lead bodies | `gmail_cred` |
| 3 | RAW sheet readable | Header row readable | `raw_read` |
| 4 | CLEAN sheet readable | Header row readable | `clean_read` |
| 5 | ERRORS / diagnostics available | Tab readable | `err_read` |
| 6 | Telegram admin send | Send short “health ok probe” to admin chat **or** dry validate chat id presence (prefer actual short ping in .dev) | `tg_admin` |
| 7 | Last operational success | `last_success_at` present and within SLO window (e.g. 24–48h) — **warn** if stale, not hard fail if schedule idle | `ops_stale` (warn) |
| 8 | Last processed lead | `last_processed_lead_id` readable | info |
| 9 | AI provider probe | **Only if** `ai_enabled=true` **AND** `health_ai_probe_enabled=true` — minimal models list or tiny JSON ping | `ai_probe` |

---

## 3. Forbidden actions

- Gmail search for unread/incoming lead labels that then get processed.
- Remove/add PROCESSED/incoming labels.
- Append to production RAW/CLEAN lead tabs.
- Call OpenRouter while AI OFF.
- Dump CONFIG secrets (there should be none) or credential IDs beyond boolean ok.
- Full-sheet scans for health (MetaBOT quota failure mode).

---

## 4. Response format (Telegram)

```
Healthcheck

CONFIG: OK
Gmail: OK
RAW: OK
CLEAN: OK
ERRORS: OK
Telegram admin: OK
Last success: 30.07.2026 12:40
Last lead: lead_…
AI probe: SKIPPED (AI off)
```

Use `FAIL (code)` / `WARN (code)` lines. End with overall `Итог: OK | WARN | FAIL`.

---

## 5. Relation to Operational

Operational writes `last_success_at`, `last_processed_*`, `last_error_*` into CONFIG (ops keys) so Admin health stays read-mostly.

---

## 6. SAFE UNKNOWN

- Whether Gmail “credential available” can be probed without any message list in the specific n8n node version — confirm in sandbox.
- Exact SLO for `ops_stale` warning threshold — operator may set later.

---

*Related: ADMIN-COMMAND-CONTRACT-v1 · CONFIGURATION-MODEL-v1.*
