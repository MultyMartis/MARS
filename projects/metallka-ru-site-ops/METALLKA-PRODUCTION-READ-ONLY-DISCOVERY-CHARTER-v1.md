# METALLKA — Production Read-Only Discovery Charter v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 2A — preparation)  
**Date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  
**Environment (future target):** PRODUCTION  

---

## 0. Normative non-authorization

```text
THIS DOCUMENT DOES NOT ITSELF AUTHORIZE ACCESS.
```

Phase 2A **prepares** the charter, plan, intake, evidence rules, and stop conditions for a **later** operator-approved read-only production discovery.

| This document authorizes | This document does **not** authorize |
|--------------------------|--------------------------------------|
| Documentary preparation of Gate A | HTTP/API requests to metallka.ru |
| Planning of future read-only stages R0–R12 | WP Admin login |
| Non-secret intake requirements | FTP/SFTP connection |
| Evidence / redaction / STOP rules | Hosting panel access |
| Definition of Gate A approval string | DB access |
| | WPilot install / activation / token / bridge |
| | REST smoke |
| | Local mirror |
| | Production backup execution |
| | Production file read |
| | Credentials request or secret creation |
| | ATLAS / registry mutation |
| | Any production mutation |

**Phase 2B must not start automatically** after Phase 2A closeout.

---

## 1. Purpose

Authorize **preparation** for a later operator-approved **read-only production discovery** of `metallka.ru`, so that Gate A can be executed under an exact HITL approval with known scope, evidence rules, and stop conditions.

Related:

- Plan: [METALLKA-READ-ONLY-DISCOVERY-PLAN-v1.md](METALLKA-READ-ONLY-DISCOVERY-PLAN-v1.md)
- Intake: [METALLKA-ACCESS-INTAKE-REQUIREMENTS-v1.md](METALLKA-ACCESS-INTAKE-REQUIREMENTS-v1.md)
- Evidence: [METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md](METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md)
- STOP: [METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md](METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md)
- Programme charter: [METALLKA-SITE-OPS-CHARTER-v1.md](METALLKA-SITE-OPS-CHARTER-v1.md)

---

## 2. Future target

| Field | Value |
|-------|-------|
| **Site** | `https://metallka.ru/` |
| **Environment** | PRODUCTION |
| **Risk class** | **C3** — external production access / read-only discovery |
| **Programme gate** | **Gate A** — Production read-only discovery |
| **Future phase when approved** | PHASE 2B — production read-only discovery (not auto-started) |

Precedents (patterns only — **not** metallka facts):

- ISEO-SU Phase 2A local-access bootstrap + Phase 2B read-only audit (`projects/iseo-su-site-ops/`)
- WPilot site-passport template + local-storage policy (`projects/wpilot/`)
- Forge WordPress source/runtime/admin methodology (patterns only)
- MLI mirror infrastructure — **DEFER** for metallka

Do **not** transfer site IDs, paths, theme options, tokens, shortcodes, or architecture facts from precedents.

---

## 3. Allowed future access classes (only after explicit operator approval)

When Gate A is separately approved, and only within the accepted read-only scope:

| Class | Intent |
|-------|--------|
| Public HTTP / browser inspection | Surface mapping without auth abuse |
| WordPress Admin **read-only** inspection | Versions, plugins, themes, settings screens — no saves |
| Hosting metadata **read-only** | Provider / PHP / backup / staging facts without mutation |
| SFTP / FTP **read-only** listing / download | Inventory and bounded file reads |
| DB metadata / read-only | Only if separately needed and authorized |
| WPilot **presence inspection only** | Detect install / ghost dirs / options — **no** REST connection |

Access classes remain **capability ≠ authorization**. Local secret files (later) do **not** authorize use.

---

## 4. Forbidden even after Phase 2A (unless separately chartered)

Forbidden under Gate A / Phase 2B read-only discovery unless a **separate** exact charter authorizes them:

| Forbidden action |
|------------------|
| File upload |
| File edit |
| Plugin install |
| Plugin activation / deactivation |
| Theme / plugin updates |
| Option writes |
| DB writes |
| WPilot token generation |
| Bridge enable |
| REST smoke |
| Write enable |
| Cache purge |
| Backup creation that mutates production state (unless separately approved) |
| Local mirror import |
| Account / user changes |

Also remain blocked by programme HOLDs until later gates: WPilot install, controlled writes, ATLAS mint, registry mutation.

---

## 5. Gate A — first future access gate

### 5.1 Gate identity

| Field | Value |
|-------|-------|
| **Gate** | **GATE A — PRODUCTION READ-ONLY DISCOVERY** |
| **Requires** | Operator confirmation **after** Phase 2A closeout |
| **Phase unlocked** | PHASE 2B (manual start only) |

### 5.2 Recommended approval statement (use later)

```text
APPROVE METALLKA GATE A — PRODUCTION READ-ONLY DISCOVERY
```

This authorizes **only** the exact read-only scope in the accepted charter + discovery plan.

It does **not** authorize: writes · install · activation · token · bridge · smoke · backup creation · cache purge.

### 5.3 Vocabulary note

This exact approval string is a **project-local convention** for METALLKA-RU-SITE-OPS unless a canonical higher-authority vocabulary already exists and is separately adopted. It does not replace MARS X-drive / git preflight or destructive-charter rules.

---

## 6. Risk and HITL posture

| Item | Posture |
|------|---------|
| Production identity | Must be confirmed before any authenticated access |
| Credentials | Never in chat / tracked files; future local contour only |
| Backup | Restore model must be understood before mutation gates; Gate A itself does not require backup creation unless separately directed |
| Protected zones | Remain PROTECTED-BY-DEFAULT until mapped ([METALLKA-PROTECTED-ZONES-v1.md](METALLKA-PROTECTED-ZONES-v1.md)) |
| SAFE UNKNOWN | No analogy fill ([METALLKA-SAFE-UNKNOWN-REGISTER-v1.md](METALLKA-SAFE-UNKNOWN-REGISTER-v1.md)) |
| Stop conditions | Mandatory — [METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md](METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md) |
| Fix-while-discovering | **Forbidden** |

---

## 7. Future discovery output artefacts (populate later — do not create filled now)

| Artifact |
|----------|
| `METALLKA-SITE-PASSPORT-v1.md` |
| `METALLKA-ACCESS-MODEL-v1.md` |
| `METALLKA-WP-ENTITY-MAP-v1.md` |
| `METALLKA-THE7-WPBAKERY-MAP-v1.md` |
| `METALLKA-PAGE-INVENTORY-v1.md` |
| `METALLKA-PLUGIN-INVENTORY-v1.md` |
| `METALLKA-FORM-MAP-v1.md` |
| `METALLKA-CUSTOM-CODE-MAP-v1.md` |
| `METALLKA-CACHE-MAP-v1.md` |
| `METALLKA-BACKUP-ROLLBACK-MODEL-v1.md` |
| `METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md` |
| `METALLKA-LOCAL-MIRROR-DECISION-v1.md` |

---

## 8. Explicit exclusions (Phase 2A)

- Claiming Gate A is approved by virtue of this document  
- Starting Phase 2B without the approval string above  
- Requesting or storing credentials in this phase  
- Creating `X:\AI MARS\local\sites\metallka-ru-production\` or token files in this phase  
- Mutating WPilot / ISEO / Forge / FP-0002 materials  

---

*Production Read-Only Discovery Charter v1 · Phase 2A preparation · access NOT AUTHORIZED.*
