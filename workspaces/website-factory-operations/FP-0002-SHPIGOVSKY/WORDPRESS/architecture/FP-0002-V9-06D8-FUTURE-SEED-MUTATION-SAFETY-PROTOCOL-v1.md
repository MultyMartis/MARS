# FP-0002 V9-06D8 Future Seed Mutation Safety Protocol v1

**Date:** 2026-07-05  
**Applies to:** D8-A through D8-G execution tasks  
**Evidence:** `validation/v9-06d8-content-seed-planning/future-seed-mutation-safety-protocol.json`

---

## Mandatory gates (every seed task)

1. **HEAD gate** — exact commit named in task charter (baseline: `d257fbe7ee8db4a099b6599e2c7c66fdc326fa21`).
2. **Branch sync** — `mars/canonical-post-recovery`; ahead=0, behind=0 before start.
3. **Runtime identity** — `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`, `shpigovsky.test`, theme `shpigovsky`, `SHPIGOVSKY_CORE_MODE=content_model`.
4. **WPilot** — `write_enabled` must be **false** unless separately authorized.
5. **Foreign WIP** — unstaged; never `git add .`.

---

## Pre-mutation checklist

- [ ] Operator authorization document with wave ID and allowlist
- [ ] DB checkpoint (operator-managed; **not** committed to Git)
- [ ] Dry-run JSON with planned values and hashes
- [ ] Rollback procedure documented
- [ ] `no-mutation-audit.json` baseline captured

---

## During mutation

- Write **only** allowlisted object IDs and field keys
- No rewrite flush unless separate charter
- No `wp post create/delete`, menu changes, redirects
- No plugin install/update/delete
- No media upload unless media charter attached
- No ACF Extended PRO features
- No external API keys or live form endpoints

---

## Post-mutation

- Pre/post value diff per field
- Route smoke (minimum: 7 first-wave URLs HTTP 200)
- Update wave evidence under `validation/v9-06d8*`
- Operator acceptance before next wave
- `no-mutation-audit.json` post snapshot

---

## Rollback

1. Restore DB checkpoint from operator storage
2. Or per-field restore using dry-run `rollback_value_hash` from D4/D8 evidence
3. Document rollback in wave report
4. Re-run read-only route QA

---

## Git evidence rules

- Stage **exact paths only** — never broad staging
- No DB dumps, runtime snapshots, secrets, or license files in Git
- Documentation/evidence under `WORDPRESS/reports|architecture|validation/` only

---

## Result

**COMPLETE**
