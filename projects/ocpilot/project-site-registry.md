# OCPilot — Project Site Registry

**Run:** 4 — First Project Site Intake  
**Purpose:** canonical registry of all sites managed by OCPilot.  
**Status:** human-maintained documentation — **not** an automated registry engine.

---

## Registry rules

| Rule | Detail |
|------|--------|
| One row per site | Site ID is stable; slug may be refined after intake |
| No secrets | URLs and hosting recorded only when operator supplies sanitized facts |
| Metadata in repo | Passports, audits, reports under `projects/ocpilot/sites/<slug>/` |
| Bulk external | Archives and snapshots under `X:\AI MARS STORAGE\ocpilot\project-sites\<slug>\` |
| SAFE UNKNOWN | Use when evidence is missing — do not invent |

---

## Sites

| Site ID | Slug | Platform | Version | Baseline | Status | Storage Location | Last Intake | Notes |
|---------|------|----------|---------|----------|--------|------------------|-------------|-------|
| SITE-001 | site-001 | ocStore | 3.0.3.8 (rs.2) | `ocstore-3038-rs2` (approved) | **READY FOR AUDIT** | `X:\AI MARS STORAGE\ocpilot\project-sites\site-001\` | 2026-06-01 (Run 4.99 — intake closed) | Intake complete; baseline approved; read-only audit chartered. Passport: [sites/site-001/site-passport.md](sites/site-001/site-passport.md). Charter: [sites/site-001/AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md). |
| SITE-002 | site-002 | ocStore / OpenCart | SAFE UNKNOWN | SAFE UNKNOWN | **AWAITING INTAKE** | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\` | 2026-06-09 (Run 4.113 — registration) | ЗПМ TEST `zpm.new-site.space`; PDP/Catalog UX pilot. Passport: [sites/site-002/site-passport.md](sites/site-002/site-passport.md). Credentials pending in external `secrets/`. |

---

## Status vocabulary

| Status | Meaning |
|--------|---------|
| AWAITING INTAKE | Folder and passport exist; site not yet identified or materials not received |
| INTAKE IN PROGRESS | Materials under quarantine review |
| READY FOR AUDIT | Intake complete; baseline selected; Run 5 allowed per [intake-readiness-review.md](intake-readiness-review.md) |
| AUDIT IN PROGRESS | Run 5 or later read-only work active |
| BLOCKED | SAFE UNKNOWN or risk gate blocks progress |
| ARCHIVED | Site work closed; folder retained for reference |

---

## Adding a site (after SITE-001)

1. Assign next Site ID (`SITE-002`, …).
2. Copy [sites/_template-site/](sites/_template-site/) → `sites/<site-slug>/`.
3. Create external root: `X:\AI MARS STORAGE\ocpilot\project-sites\<site-slug>\`.
4. Fill [site-passport-standard.md](site-passport-standard.md) fields in `site-passport.md`.
5. Append row to this registry.
6. Record intake date in **Last Intake** when operator materials are accepted.

---

## Related documents

- [project-sites-workflow.md](project-sites-workflow.md)
- [site-passport-standard.md](site-passport-standard.md)
- [baseline-match-workflow.md](baseline-match-workflow.md)
- [intake-readiness-review.md](intake-readiness-review.md)
- [external-storage-registry.md](external-storage-registry.md)
