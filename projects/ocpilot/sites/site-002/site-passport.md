# SITE-002 — Site Passport

**Status:** **STABLE LIVE CHECKPOINT**  
**Run:** 4.139 — Stable Live PDP V5.1 Checkpoint (2026-06-14)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | SAFE UNKNOWN |
| **Baseline Match** | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| **Hosting** | SAFE UNKNOWN |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Environment** | TEST |
| **Test URL** | https://zpm.new-site.space/ |
| **Current Status** | **STABLE LIVE CHECKPOINT** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| **Rollback source** | Beget global backup + operator live state |
| **Notes** | TEST площадка PDP / Catalog UX. Live hosting — source-of-truth after PDP V5.1 (specs collapse, scroll UX, scroll offset), Category V2.3.1, and operator manual polish. Checkpoint is metadata-only; no site files in repo. Registry: [project-site-registry.md](../../project-site-registry.md). |

---

## SAFE UNKNOWN

- ocStore / OpenCart exact version and release line
- Baseline match candidate
- Hosting provider
- Admin URL (non-secret)
- Credential storage paths (external only; not in repo)
- Catalog scale, extensions, theme, custom modules
- FTP host, phpMyAdmin URL, database name (pending operator credentials)
- Formal quarantine intake report artifact in repo

---

## Security notes

| Check | Value |
|-------|-------|
| No secrets recorded | **yes** |
| PII exposure risk | SAFE UNKNOWN — no bulk materials placed yet |
| Access closeout needed | Per default policy: no access runs until charter |

---

## Stable checkpoint (active)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Registered | 2026-06-14 21:00:00 |
| Type | Metadata-only — live source-of-truth |
| Supersedes | `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14` (historical) |
| Active passes | PDP V5.1 (specs collapse, scroll UX, scroll offset) · Category V2.3.1 · operator manual polish |

## Next work rule

Before any file-touching task: live-capture **only** the specific files to be changed. Do not rely on pre-manual-edit work copies.

## Next planned run

| Run # | Name | Blocked by |
|-------|------|------------|
| — | Next scoped live-file task | Operator charter for specific pass; mandatory pre-task live capture |
