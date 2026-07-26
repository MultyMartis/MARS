# METALLKA — WPilot Token Local Storage Plan v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A — documentation only  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Policy authority:** `projects/wpilot/local-storage-policy.md`

```text
Phase 4A does NOT create a token file and does NOT generate a token.
Do not alter X:\AI MARS\local\sites\metallka-ru-production\secrets.local.md for token content.
```

---

## 1. Canonical local storage (existing policy)

| Field | Value |
|-------|-------|
| Canonical tokens root | `X:\AI MARS\local\tokens\` |
| Git | `/local/` is ignored — **must not** be committed |
| File content | Plaintext token only (single value) |
| Auth header (future use) | `X-WPilot-Token` |

---

## 2. Exact metallka production token destination

Follow existing programme naming (`wpilot-prod-<site-slug>.token`), as used for i-seo.su:

| Field | Value |
|-------|-------|
| **Canonical path** | `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |
| Site alias | `prod-metallka-ru` |
| Site URL | `https://metallka.ru` |
| REST namespace | `wpilot/v1` |
| Environment class | PRODUCTION |
| Phase 4A file status | **NOT CREATED** (correct) |

Do **not** invent a parallel scheme under `local/sites/...` for the token value.

Optional non-secret metadata may later reference the token **filename only** under `local/sites/metallka-ru-production/` — never the token value; not required in Phase 4A.

---

## 3. Phase 4B creation rules

1. Verify safe defaults first (`bridge` / `write` / `dev_confirmed` all false).  
2. Generate exactly one token via WPilot admin UI.  
3. Operator copies plaintext once into `wpilot-prod-metallka-ru.token`.  
4. Re-verify safe defaults after generation.  
5. Do **not** paste token into REPORT, chat lasting records intended for git, screenshots for evidence packs, or tracked markdown.  
6. Do **not** test the token against REST in Phase 4B.  
7. Do **not** enable bridge.

---

## 4. Persistence validation (post-token)

| Check | Required |
|-------|----------|
| Local file exists | YES (local-only) |
| Tracked repo contains token | NO |
| `bridge_enabled` | false |
| `write_enabled` | false |
| `dev_confirmed` | false |
| WPilot REST request count | **0** |
| Unrelated connection metadata corrupted | NO |

Source behavior (RC6): `generate_token()` updates only token-related option fields and does not toggle the three safety flags.

---

## 5. Redaction / evidence

Allowed in tracked evidence:

- path class / filename  
- created (yes/no)  
- revoked (yes/no)  
- UTC created-at if shown in admin without revealing token  

Forbidden:

- plaintext token  
- hash dumps that could assist offline attack beyond operational need  
- Authorization / `X-WPilot-Token` header values  

See [METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md](METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md).

---

## 6. Missing / failed token flow

If generation fails with safe defaults intact: leave plugin active (preferred) or remove per rollback plan Case D — **no** local token file.

If token shown once but local write fails: treat as operational incident — revoke in admin if possible; do not leave plaintext in chat/logs; retry only under explicit re-approval if required.

---

## 7. Explicit non-actions (Phase 4A)

- No placeholder token file with fake contents (unnecessary).  
- No secrets.local.md mutation for WPilot token.  
- No REST authentication rehearsal.

---

*METALLKA WPilot Token Local Storage Plan v1 · destination prepared · token not created.*
