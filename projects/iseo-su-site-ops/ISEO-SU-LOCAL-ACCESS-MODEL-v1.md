# ISEO-SU LOCAL ACCESS MODEL v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-2A-WAVE-A-REVIEW-AND-LOCAL-ACCESS-BOOTSTRAP  
**Status:** ACCEPTED as Phase 2A local-access bootstrap model  
**Date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Production connection:** **NOT AUTHORIZED**

This document describes **where** access metadata and secrets live.  
It does **not** authorize login, FTP/SFTP, panel use, WordPress admin use, REST, WPilot, or mutation.

---

## 1. Selected pattern

**Hybrid of WPilot local storage + OCPilot SITE-002 secret separation**, adapted for this programme because:

| Source | Adopted element |
|--------|-----------------|
| `projects/wpilot/local-storage-policy.md` | Canonical local roots `X:\AI MARS\local\sites\` and `X:\AI MARS\local\tokens\`; Git ignore `/local/` |
| `projects/wpilot/runtime-local.example/sites.example.json` | Non-secret site metadata + `token_ref` / path references only |
| OCPilot SITE-002 `project-access-brief.md` / `production-profile.md` | Tracked docs hold capability inventory and path references — **never** passwords |
| OCPilot SITE-002 secrets practice | Separate secrets file with empty operator-fill fields; connection ≠ registration |
| Remote Operations Layer | Credentials remain operator-managed; never requested into chat |
| Decision D-008 | No credentials in project docs or Git locus |

**Not used for this Phase 2A bootstrap:**

- OCPilot Storage secrets path under `X:\AI MARS STORAGE\…` — Storage writes are **not** authorized in this task.
- Creating a WPilot token file — WPilot token generation remains a **later gate**.
- Putting credentials into tracked programme markdown.

---

## 2. Site alias

| Field | Value |
|-------|-------|
| **Stable alias** | `iseo-su-production` |
| **Filename style** | hyphenated; no dots in the alias segment |
| **Environment** | production |

---

## 3. Local paths (operator machine)

| Role | Path | Contents |
|------|------|----------|
| Site directory | `X:\AI MARS\local\sites\iseo-su-production\` | Local-only profile bundle |
| Non-secret metadata | `X:\AI MARS\local\sites\iseo-su-production\site-profile.json` | URL, Beget, WP admin URL, capability flags, secret path refs |
| Secrets template | `X:\AI MARS\local\sites\iseo-su-production\secrets.local.md` | Empty fields for Beget / FTP|SFTP / WordPress admin |
| Future WPilot token (reserved only) | `X:\AI MARS\local\tokens\wpilot-iseo-su-production.token` | **Do not create in Phase 2A**; reserved path documented in profile |

---

## 4. Separation rules

| Layer | May contain | Must not contain |
|-------|-------------|------------------|
| Tracked programme docs | Non-secret Wave A facts; path references; access class status | Passwords, tokens, cookies, fingerprints if treated as secrets in chat |
| `site-profile.json` | Site URL, environment, provider, WP admin URL, empty panel URL, capability flags, secret **path** refs | Passwords, tokens, cookies, 2FA codes |
| `secrets.local.md` | Operator-entered credentials locally | Cookies; sessions; 2FA backup codes; wp-config; DB password (unless later DB charter); WPilot token |
| Future token file | Plaintext WPilot token only (when separately authorized) | Hosting/FTP/WP passwords |

---

## 5. Access classes (capability vs authorization)

Operator Wave A confirmed **capability existence** for:

- hosting panel access;
- FTP or SFTP access;
- WordPress administrator access.

Programme access classes **A3–A8** remain **NOT AUTHORIZED**.  
Local file preparation **does not** authorize use.

---

## 6. Git-ignore proof basis

Root `.gitignore` contains:

```text
/local/
```

Therefore everything under `X:\AI MARS\local\` is ignored by Git. Phase 2A verified `git check-ignore` for the created paths before treating them as safe secret containers.

---

## 7. Rotation expectations

| Secret class | Expectation |
|--------------|-------------|
| Beget password | Operator-managed rotation; update local secrets file only |
| FTP/SFTP password | Operator-managed rotation; update local secrets file only |
| WordPress password | Prefer dedicated MARS admin account (recommended, not created in Phase 2A); rotate if exposed |
| Future WPilot token | Generate/rotate in WP admin; store only under `local\tokens\`; never in `secrets.local.md` or chat |

If any secret is pasted into chat or committed: treat as incident — stop, rotate, replace local value, do not re-paste.

---

## 8. Authoritative policies used

1. `projects/wpilot/local-storage-policy.md`
2. `projects/wpilot/runtime-local.example/sites.example.json`
3. `projects/ocpilot/templates/project-access-brief-template.md`
4. `projects/ocpilot/sites/site-002/project-access-brief.md` (path/reference pattern only; secrets not read)
5. `projects/remote-operations-layer/OPERATIONAL-INDEX.md` + credential boundary language in ROL contracts
6. Root `.gitignore` (`/local/`)
7. Programme Decision Register D-007 / D-008

---

## 9. Phase 2A decision note

Exact generic credential path for hybrid WordPress+static Beget sites was not previously defined inside `projects/iseo-su-site-ops/`.  

**Phase 2A decision:** use `X:\AI MARS\local\sites\iseo-su-production\` as the site-specific local bundle, aligned with WPilot `local\sites\` policy and proven `/local/` Git ignore — **not** Storage, **not** Localhost, **not** tracked docs.

---

*ISEO-SU LOCAL ACCESS MODEL v1 · 2026-07-22 · no secrets · connection NOT AUTHORIZED.*
