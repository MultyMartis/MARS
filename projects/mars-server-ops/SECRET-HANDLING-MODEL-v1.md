# MARS Server Ops — Secret Handling Model v1

**Status:** **documented** boundary model  
**Not:** secret manager, vault product, or credential sync engine

---

## 1. Purpose

Define where server infrastructure secrets **may** live in the MARS ecosystem and what **must never** enter Git.

Reuses patterns from:

- Root [.gitignore](../../.gitignore) — `/local/`, `.env`, `.secrets/`  
- [MLI WordPress runtime profile](../mars-localhost-infrastructure/MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md) — `X:\AI MARS\local\mli\{slug}\runtime.env`  
- Site Ops — `X:\AI MARS\local\sites\<site-alias>-production\secrets.local.md`  
- [EAR Security Model](../../shared/external-access-runtime/EAR-SECURITY-MODEL-v1.md) — secret_ref, read-only default  
- [EAR Credential Boundary](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) — separation of concerns  
- MetaBOT / n8n — credential store stays outside Git  

**Phase 1A:** establishes pattern only — **no local secret files created**.

---

## 2. Three-layer model

| Layer | Path (canonical proposal) | Content |
|-------|---------------------------|---------|
| **Git (Active Brain)** | `X:\AI MARS\projects\mars-server-ops\` | Docs, schemas, sanitized templates, `secret_ref` identifiers |
| **Local-only** | `X:\AI MARS\local\infrastructure\<server-or-passport-ref>\` | Live credentials, keys, tokens, runtime env |
| **Bulk Storage** | `X:\AI MARS STORAGE\mars-server-ops\` | Raw exports, configs, backups, evidence — out of Git |

```text
Git knows THAT a secret exists and WHERE the operator stores it.
Git never contains the secret VALUE.
```

---

## 3. Recommended local-only layout

Per server or passport ref (create only when operator charters intake — **not in Phase 1A**):

```text
X:\AI MARS\local\infrastructure\<server-or-passport-ref>\
  secrets.local.md      # operator-filled; markdown sections by surface
  runtime.env           # optional; KEY=VALUE for tools — gitignored via /local/
```

**Alternative (site-adjacent):** If a server primarily serves one Site Ops site, existing  
`X:\AI MARS\local\sites\<site-alias>-production\secrets.local.md` may remain authoritative — Server Ops links via `secret_ref` rather than duplicating.

**MLI separation:** Local WordPress/Laragon secrets stay under `local/mli/` — not Server Ops.

---

## 4. secrets.local.md section pattern

Align with Site Ops templates (structure only):

- Provider panel  
- SSH  
- SFTP / FTP  
- VPN / 3X-UI  
- Docker / compose env (reference only — prefer `runtime.env` for values)  
- Reverse proxy admin  
- n8n (UI + API — not workflow credential exports)  
- Database (host, user, password, DSN — **local only**)  
- Monitoring / DNS  
- Notes / rotation dates  

Use `SECRET_REFERENCE_PRESENT: yes` in docs — never the value.

---

## 5. secret_ref in Git-safe documents

Acceptable in inventory, passport, access model:

```text
secret_ref: local/infrastructure/PASS-SRV-OPS-001/secrets.local.md → SSH
```

Optional indirection:

```text
secret_ref: local/sites/example-production/secrets.local.md → FTP
```

---

## 6. Explicitly prohibited in Git

Never commit:

| Category | Examples |
|----------|----------|
| Passwords | Panel, SSH, DB, n8n |
| Private keys | SSH, TLS, VPN |
| API / bot tokens | Provider API, Telegram, n8n API |
| Raw DSN with credentials | `postgresql://user:pass@...` |
| Live `.env` | Docker compose production env |
| n8n credential exports | JSON credential dumps |
| Private TLS material | keys, full cert chains with private key |
| VPN client private material | Xray client configs with secrets |
| 3X-UI / Xray exports | Files containing client UUIDs/keys if sensitive |

If historical leak suspected → classify per Site Ops `HISTORICAL_REVOKED_SECRET` pattern; rotation + local authority — no history rewrite by agent default.

---

## 7. Storage sensitivity

| Artifact | Location | Git |
|----------|----------|-----|
| Sanitized nginx snippet | Storage `configs/` | Reference only |
| Full config with secrets | Storage `configs/` or local | **Never Git** |
| DB dump | Storage `backups/` | **Never Git** |
| n8n export | Storage `incoming/` | **Never Git** |

Encryption at rest: **operator responsibility** — **SAFE UNKNOWN** for global MARS policy.

---

## 8. Agent / Cursor rules

| Rule | Detail |
|------|--------|
| **No default read** | Agents do not read `local/` or Storage secrets unless explicit charter |
| **No commit** | Never stage secret files |
| **No chat paste** | Do not echo credentials into reports destined for Git |
| **EAR alignment** | Snapshots contain `secret_ref`, not values |

---

## 9. MetaBOT / n8n boundary

| Owner | Secrets |
|-------|---------|
| **Server Ops (host)** | OS, SSH, Docker host, PostgreSQL **instance** access, reverse proxy TLS **host** level |
| **MetaBOT (product)** | Workflow credentials inside n8n — documented in MetaBOT programme |
| **n8n runtime** | Credential store on server — **never exported to Git** |

Server Ops runbooks may reference **that** credentials exist — not their values.

---

## 10. Phase 1A state (historical)

| Item | Status |
|------|--------|
| Local secret files (Phase 1A) | **NOT CREATED** in that wave |
| Storage directories (Phase 1A) | **NOT CREATED** in that wave |
| Git secret values | **NONE** (standing rule) |

**Update (2026-08-25):** Server B planning local contour may exist at  
`X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md` — **LOCAL-ONLY**, never Git.

---

## 11. Related documents

- [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md)  
- [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md)  
- [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md)  
- [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md)  

---

## 12. MARS-generated production secrets (approved build charters)

For future **controlled** Server B (and similar) build waves, MARS/Cursor **MAY** generate production secrets when the build charter **explicitly** authorizes generation.

Examples (non-exhaustive):

- operator SSH key material  
- 3X-UI admin username / password  
- 3X-UI random panel base path  
- panel port (when randomly selected)  
- VLESS identities  
- WebSocket secret/path  
- Reality keypair / ShortID  
- subscription/client credentials  
- backup encryption secret if introduced  

### Mandatory handling

| Rule | Detail |
|------|--------|
| **Write locus** | Secret **values** MUST be written directly to the asset’s **LOCAL-ONLY** secret contour |
| **Current Server B locus** | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md` (until an authorized migration preserves locality) |
| **Git** | Documentation may record only: secret reference name; **PRESENT / ABSENT**; public component where inherently public; fingerprint where appropriate; creation timestamp; rotation status; recovery reference |
| **REPORT / chat** | **Never** print actual secret values |
| **Placeholders in reports** | e.g. `<SSH_OPERATOR_KEY>`, `<3XUI_ADMIN_PASSWORD>`, `<3XUI_PANEL_PATH>`, `<VLESS_CLIENT_ID>`, `<REALITY_PRIVATE_KEY>`, `<REALITY_SHORT_ID>` |
| **Generate / store / reference / rotate** | Allowed **only** under an approved build charter |
| **Phase 3B** | **No** secret generation — intake/read-only only |

Future asset-ID migration must keep secrets local and must **not** expose values through Git.

---

*Secret Handling Model v1 · local-only values · charter-gated generation · no secrets in Git.*
