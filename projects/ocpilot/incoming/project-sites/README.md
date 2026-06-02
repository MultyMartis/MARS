# OCPilot — Incoming Project Sites

**Purpose:** quarantine dropzone for **external project / dealership** materials before assignment to `sites/<site-slug>/`.

**Parent:** [../README.md](../README.md)

---

## What belongs here

| Allowed drop | Examples |
|--------------|----------|
| Site file tree archive (FTP export, hosting backup) | `dealership-export-2026.zip` |
| Partial materials bundle | Theme pack + brief + path list |
| Database dump (prefer external; if present — quarantine review) | `backup.sql` — **high risk** |
| Mixed handoff package | Files + docs + screenshots — document as mixed in intake report |
| Sanitized operator briefs | PDF/MD without secrets |

---

## What does NOT belong here

| Forbidden drop | Route instead |
|----------------|---------------|
| Claimed clean OpenCart vendor ZIP only | [incoming/baselines/](../baselines/README.md) |
| Approved site materials already assigned to a slug | `sites/<site-slug>/materials/` after intake |
| Credentials files for repo storage | External secure storage; reference class only in passport |

---

## Workflow (summary)

1. Operator places materials in this folder.
2. OCPilot runs **project site intake** — see [intake-workflow.md](../../intake-workflow.md).
3. OCPilot identifies platform, version, archive type, risks.
4. OCPilot fills [intake-report-template.md](../../templates/intake-report-template.md).
5. Operator approves recommended `sites/<site-slug>/` (create from `_template-site/` if new).
6. Operator moves sanitized materials into site folder structure — **human-operated** (Run 4+).

**No automatic moves. No automatic imports.**

---

## Risk reminder

Project site packages often contain:

- `config.php` secrets
- Customer / order data in DB dumps
- Custom modules, ocMod, vQmod
- Cache, logs, uploads

Treat all drops as **untrusted** until [quarantine-policy.md](../../quarantine-policy.md) review completes.

---

## Related documents

- [project-sites-workflow.md](../../project-sites-workflow.md)
- [templates/project-site-passport-template.md](../../templates/project-site-passport-template.md)
- [access-and-safety.md](../../access-and-safety.md)
- [quarantine-policy.md](../../quarantine-policy.md)
