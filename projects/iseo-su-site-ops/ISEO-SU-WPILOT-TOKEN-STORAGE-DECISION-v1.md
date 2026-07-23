# ISEO-SU WPILOT TOKEN STORAGE DECISION v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B  
**Date:** 2026-07-24  
**Status:** **DECISION RECORDED / TOKEN NOT CREATED**

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

## 2. Selected future local path

| Field | Value |
|-------|-------|
| **Classification** | **CONFIRMED BY POLICY** (path pattern) / **PROPOSED** filename for this site |
| **Path** | `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` |
| **Site alias** | `prod-iseo-su` |
| **Format** | Single-line plaintext token only (no JSON wrapper), per MARS token standard examples |

Rationale: mirrors DEV naming (`wpilot-dev-gktriumph.token`) with `prod` + site slug.

---

## 3. Site profile reference (future)

Local site metadata under `X:\AI MARS\local\sites\iseo-su-production\` may store:

- `token_file` / `token_ref` path string  
- site URL, REST namespace `wpilot/v1`  
- sanitized status timestamps  

Must **not** store the token value in `secrets.local.md` unless operator later explicitly chooses that additional copy — **default is dedicated token file only**.

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
- No token creation in Phase 4B  
- No shared generic secrets dump as primary store  

---

## 6. Current status

| Item | Status |
|------|--------|
| Local token file | **NOT CREATED** |
| WordPress token hash | **N/A** (plugin absent) |
| GATE 6C | **NOT AUTHORIZED** |

---

*Token storage decision v1 · 2026-07-24 · no token created.*
