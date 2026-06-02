# OCPilot — Incoming Zone

**Purpose:** temporary **quarantine / intake** area for external OpenCart-related packages before OCPilot treats them as baselines or project site materials.

**Status:** documented intake zone only; **no** automation; **no** trusted storage.

---

## Core safety principle

```
Incoming Material  ≠  Trusted Baseline
Incoming Material  ≠  Project Site
```

Incoming material **must pass intake** before it belongs anywhere else in OCPilot.

See [intake-workflow.md](../intake-workflow.md), [quarantine-policy.md](../quarantine-policy.md), [baseline-acquisition-strategy.md](../baseline-acquisition-strategy.md).

---

## What incoming is

| Property | Meaning |
|----------|---------|
| **Temporary** | Packages stay here only until intake completes and operator approves next step |
| **Quarantine** | Nothing is trusted automatically — assume incomplete, mislabeled, or contaminated |
| **Human gate** | All moves out of incoming require operator approval |
| **External entry point** | First repo-adjacent location for operator-dropped archives |

---

## What incoming is NOT

| Not this | Why |
|----------|-----|
| **Baseline storage** | Trusted baselines live under [baselines/](../baselines/README.md) after intake + readiness |
| **Project storage** | Site materials live under [sites/](../sites/README.md) after project site intake |
| **Working storage** | No editing, unpacking for production use, or long-term retention here |
| **Credential store** | Secrets must not be committed; see [access-and-safety.md](../access-and-safety.md) |
| **Automatic pipeline** | OCPilot does not auto-import, auto-move, or auto-commit incoming files |

---

## Subzones

| Path | Purpose |
|------|---------|
| [incoming/baselines/](baselines/README.md) | Candidate **clean vendor** packages for versioned baselines |
| [incoming/project-sites/](project-sites/README.md) | Candidate **dealership / project** exports, backups, and handoff materials |

Keep baseline candidates and project site materials **separate**. Do not mix in one archive folder without documenting as mixed package in intake report.

---

## Operator rules

1. **Drop only** — place archive or material bundle in the correct subfolder; do not manually move to `baselines/` or `sites/` without intake.
2. **Name clearly** — use descriptive filenames (version hint, date, source); no secrets in names.
3. **One package per intake report** — or one report covering a clearly defined bundle with operator confirmation.
4. **Request intake** — ask OCPilot to run intake workflow; review [templates/intake-report-template.md](../templates/intake-report-template.md) output.
5. **Approve moves** — OCPilot **recommends** destination; operator **executes** move after approval.
6. **Clean up** — after successful intake and move, remove or archive external copies per operator policy; incoming should not accumulate indefinitely.

---

## Forbidden in incoming (repo commit)

- Live credentials and unsanitized `config.php`
- Full production DB dumps with PII (prefer external storage; metadata-only in repo)
- Binaries without operator charter and intake report

If sensitive material is required for review, keep **external** and reference path/class in intake report only.

---

## Related documents

- [intake-workflow.md](../intake-workflow.md)
- [quarantine-policy.md](../quarantine-policy.md)
- [baseline-acquisition-strategy.md](../baseline-acquisition-strategy.md)
- [project-sites-workflow.md](../project-sites-workflow.md)
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)

---

## SAFE UNKNOWN

- Maximum retention time for items in incoming — operator policy TBD; OCPilot recommends review before Run 3/4 execution.
- Git tracking of large binaries in incoming — prefer `.gitignore` for actual archives when added; placeholders (`.gitkeep`) mark structure only in Run 2.5.
