# MARS Localhost — Data and Secrets Policy v1

**Document type:** Data and secrets policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Control data classification, secrets handling, and leakage risk across brain and runtime zones.

---

## Data preference

| Priority | Data type |
|----------|-----------|
| **1 (preferred)** | Synthetic fixtures, generated content, public OSS assets |
| **2** | Sanitized exports with operator approval |
| **3** | Full client data — **explicit charter only** |

---

## Client data

- Permitted in `projects\` class sites **only when explicitly approved**
- Must be recorded in manifest + project passport
- Prefer sanitized dumps over live production copies

---

## Database dumps

| Rule | Policy |
|------|--------|
| Storage | `E:\MARS-Localhost\databases\dumps\` |
| Large retention | Optional `C:\AI MARS STORAGE\{consumer}\` |
| Git | **Never** commit dumps |
| Production imports | Operator approval + sanitization review |
| Naming | Per [database naming standard](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |

---

## Uploads

| Rule | Policy |
|------|--------|
| Runtime | Site `uploads` or `storage\uploads\` staging |
| Git | **No** media uploads in MARS Git |
| Client media | Only with approval; scan for credentials in filenames/metadata |

---

## Secrets

| Item | Policy |
|------|--------|
| **Git** | Secrets **outside** Git |
| **MARS docs** | **No** credentials in markdown |
| **Manifests** | Secrets **location** only — never values |
| **`.env`** | Local only under D: site or `C:\AI MARS\local\mli\{slug}\` |
| **Production credentials** | **Prohibited by default** in local configs |

---

## Backup encryption

- If dumps or backups contain sensitive client data, encrypt at rest (operator tool of choice)
- Document encryption method in backup manifest note — not keys in repo

---

## Log sanitization

- Redact passwords, tokens, API keys before attaching logs to brain reports
- Store raw logs only on D: under `logs\` with restricted access

---

## Data deletion

| Class | Policy |
|-------|--------|
| Synthetic | Reset permitted after evidence archived to brain |
| Projects | Delete only per passport + operator sign-off |
| Sandboxes | Delete on experiment end; wipe DB + files |
| Operator request | Full removal of D: path + manifest `archived` status |

---

## Related

- [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md)
- [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md)

---

*Data and secrets policy v1 — MLI-00.*
