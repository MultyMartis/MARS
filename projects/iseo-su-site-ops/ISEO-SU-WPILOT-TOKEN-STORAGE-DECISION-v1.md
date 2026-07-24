# ISEO-SU WPILOT TOKEN STORAGE DECISION v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B (decision) · **PHASE 6C RETRY (token present)**  
**Date:** 2026-07-24  
**Status:** **DECISION RECORDED / TOKEN PRESENT LOCAL-ONLY** · Phase 6C RETRY **COMPLETE**

---

## 1. Canonical policy

Authority: `projects/wpilot/local-storage-policy.md`

| Rule | Requirement |
|------|-------------|
| Token location root | `X:\AI MARS\local\tokens\` |
| Git | Must remain ignored (`/local/`) |
| WordPress DB | Store **hash only** (`token_hash` via `wp_hash_password`) |
| Docs / REPORT / chat | **No plaintext token** |
| Site metadata | Store **path/reference only**, never secret value |
| REST header | `X-WPilot-Token` |

---

## 2. Selected local path

| Field | Value |
|-------|-------|
| **Classification** | **CONFIRMED** |
| **Path** | `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` |
| **Site alias** | `prod-iseo-su` |
| **Format** | Single-line plaintext token only (no JSON wrapper), per MARS token standard |

Rationale: mirrors DEV naming (`wpilot-dev-gktriumph.token`) with `prod` + site slug.

---

## 3. Site profile reference

Local site metadata under `X:\AI MARS\local\sites\iseo-su-production\` stores:

- `token_file_path` / path reference string  
- sanitized status timestamps  
- plugin/bridge/write/DEV status metadata  

Must **not** store the token value in `secrets.local.md` — **dedicated token file only**.

---

## 4. Rotation

1. Revoke/generate in WordPress Admin (HITL).  
2. Overwrite local token file.  
3. Update sanitized metadata timestamps.  
4. Never commit rotation artifacts.

---

## 5. Prohibitions

- No token in `projects/iseo-su-site-ops/` docs  
- No token in REPORT  
- No token in git  
- No token in Storage  
- No shared generic secrets dump as primary store  

---

## 6. Current status

| Item | Status |
|------|--------|
| Local token file | **PRESENT** (Git-ignored) |
| WordPress token hash | **Present** (Admin indicates token generated) |
| GATE 6C (RC5 historical) | **BLOCKED** — bridge+DEV gate |
| GATE 6C RETRY (RC6) | **COMPLETE** — token created with bridge/writes/DEV off |
| Canonical path (unchanged) | `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` |

---

*Token storage decision v1 · 2026-07-24 · path decided; token present local-only after 6C retry.*
