# OCPilot — Site Passport Standard

**Run:** 4 — First Project Site Intake  
**Purpose:** define mandatory and optional fields for every project site passport (`sites/<slug>/site-passport.md`).  
**Extends:** [templates/site-passport-template.md](templates/site-passport-template.md), [templates/project-site-passport-template.md](templates/project-site-passport-template.md).

---

## Passport location

| Artifact | Path |
|----------|------|
| Canonical passport | `projects/ocpilot/sites/<site-slug>/site-passport.md` |
| Registry link | [project-site-registry.md](project-site-registry.md) |
| Bulk storage | `C:\AI MARS STORAGE\ocpilot\project-sites\<site-slug>\` |

One passport per site. Do not store secrets in the passport.

---

## Standard fields

| Field | Required | Description |
|-------|----------|-------------|
| **Site ID** | **Yes** | Stable ID from registry (e.g. `SITE-001`) |
| **Site Name** | **Yes** when known | Sanitized dealership or client label; `SAFE UNKNOWN` until supplied |
| **Slug** | **Yes** | Folder name under `sites/` (e.g. `site-001`) |
| **Platform** | **Yes** when known | `OpenCart` / `ocStore` / `SAFE UNKNOWN` |
| **Version** | **Yes** when known | Exact release line (e.g. `3.0.3.8`, `rs.2`) / `SAFE UNKNOWN` |
| **Baseline Match** | **Yes** when selected | e.g. `baselines/ocstore-3038-rs2/` / `SAFE UNKNOWN` |
| **Hosting** | No | Provider name only — no account IDs or credentials |
| **Access Methods** | No | Access *class* per channel (read-only / write / none) — see [access-and-safety.md](access-and-safety.md) |
| **Storage Location** | **Yes** | External bulk path for this site |
| **Environment** | **Yes** when known | `test` / `staging` / `production` / `SAFE UNKNOWN` |
| **Current Status** | **Yes** | Registry-aligned status (e.g. `AWAITING INTAKE`) |
| **SAFE UNKNOWN** | **Yes** | Bulleted list of unresolved facts blocking progress |
| **Notes** | No | Operator context, intake run reference, non-secret reminders |

---

## Mandatory fields (minimum viable passport)

These must be present on every passport, even at container-only intake:

1. **Site ID**
2. **Slug**
3. **Storage Location**
4. **Current Status**
5. **SAFE UNKNOWN** (explicit list — may be “all site facts pending”)

Until intake completes, **Site Name**, **Platform**, **Version**, **Baseline Match**, and **Environment** may legitimately read `SAFE UNKNOWN`.

---

## Forbidden in passports

- Passwords, API keys, tokens
- Full `config.php` contents
- Live database connection strings
- Customer PII exports
- Unsanitized production URLs if operator policy forbids

---

## Status alignment

**Current Status** must match [project-site-registry.md](project-site-registry.md) for the same Site ID. Update both when status changes.

---

## Baseline match reference

After version evidence exists, record **Baseline Match** per [baseline-match-workflow.md](baseline-match-workflow.md). Do not assign a baseline before validated version evidence.

---

## Run 5 gate

Passport completeness alone does not authorize audit. Use [intake-readiness-review.md](intake-readiness-review.md) for Run 5 **YES/NO**.
