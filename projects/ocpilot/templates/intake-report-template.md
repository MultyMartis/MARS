# OCPilot — Intake Report

**Purpose:** standard record for reviewing a package in [incoming/](../incoming/README.md) — used for **baseline packages** and **project site packages**.

**Usage:** OCPilot fills during intake; operator reviews before approving any move.

**Store completed copies:** operator choice — e.g. run `# REPORT — …`, destination `notes/`, site `reports/`, or baseline `passports/` adjunct; **not** auto-committed unless operator requests.

**Naming suggestion:** `intake-report-<package-label>-<YYYY-MM-DD>.md`

---

## Report metadata

| Field | Value |
|-------|-------|
| **Report ID** | e.g. `intake-baseline-opencart-3037-2026-05-30` |
| **Intake type** | Baseline / Project site / Mixed (explain) |
| **Package filename** | |
| **Incoming path** | e.g. `incoming/baselines/` or `incoming/project-sites/` |
| **Review date** | YYYY-MM-DD |
| **Reviewer (operator / agent)** | |

---

## Source

| Field | Value |
|-------|-------|
| **Declared source** | URL, vendor, operator handoff description |
| **Declared by** | Operator / filename / unknown |
| **Verification performed** | e.g. matched official release page / GitHub tag / none |
| **Verification evidence** | Links, checksum label, or **SAFE UNKNOWN** |

---

## Package Type

| Field | Value |
|-------|-------|
| **Primary type** | Official vendor release / site backup / partial export / DB dump / theme pack / extension pack / documentation / mixed |
| **Archive format** | ZIP / TAR / directory / other |
| **Approximate size** | |
| **Mixed package notes** | If multiple concerns bundled, list components |

---

## Detected Platform

| Field | Value |
|-------|-------|
| **Platform** | OpenCart / ocStore / unknown / not applicable |
| **Detection method** | Directory layout / version file / operator brief / inconclusive |
| **Confidence** | high / medium / low / **SAFE UNKNOWN** |

---

## Detected Version

| Field | Value |
|-------|-------|
| **Version string** | e.g. 3.0.3.7 / 2.3.0 / 4.0.x |
| **Detection method** | |
| **Confidence** | high / medium / low / **SAFE UNKNOWN** |
| **Version mismatch risk** | none / possible / likely — explain |

---

## Trust Level

Per [baseline-acquisition-strategy.md](../baseline-acquisition-strategy.md):

| Level | Selected | Rationale |
|-------|----------|-----------|
| **High** | ☐ | |
| **Medium** | ☐ | |
| **Low** | ☐ | |

---

## Risk Level

Per [quarantine-policy.md](../quarantine-policy.md):

| Level | Selected | Rationale |
|-------|----------|-----------|
| **Low** | ☐ | |
| **Medium** | ☐ | |
| **High** | ☐ | |
| **Critical (stop)** | ☐ | |

---

## Contents Summary

Brief inventory of what appears present (directories, notable files, sidecars):

```
(e.g. admin/, catalog/, system/ present; config.php present with values — NOT FOR REPO)
```

| Area | Observed | Notes |
|------|----------|-------|
| Core vendor dirs | | |
| Config / secrets | | |
| Extensions / custom | | |
| Uploads / cache / logs | | |
| Database files | | |
| Other | | |

---

## Missing Items

Expected content absent or incomplete:

| Item | Expected for | Status |
|------|--------------|--------|
| | | missing / partial / n/a |

---

## Suspicious Items

Files, patterns, or findings requiring attention:

| Item | Concern | Action |
|------|---------|--------|
| e.g. `config.php` with DB password | Credential exposure | Strip before repo; external only |
| e.g. `vqmod/` cache | Not vendor-clean | Reject as baseline |
| e.g. unknown `.exe` in archive | Malware / tool unknown | Stop; operator review |

---

## Recommended Destination

| Field | Value |
|-------|-------|
| **Recommended path** | e.g. `baselines/opencart-3037/` or `sites/dealership-alpha/` |
| **Target subfolders** | e.g. `files/`, `materials/`, `backups/files/` (metadata only) |
| **Create new site slug?** | yes / no — proposed slug: |
| **Reject package?** | yes / no — reason: |
| **Sanitization required before move** | List steps |

**Reminder:** recommendation only — operator executes move after approval.

---

## SAFE UNKNOWN

List everything that could not be verified without additional operator input or safe inspection:

| # | Unknown | What would verify |
|---|---------|-------------------|
| 1 | | |
| 2 | | |

---

## Recommendation

| Field | Value |
|-------|-------|
| **Overall recommendation** | Approve move / Approve with conditions / Reject / Hold for operator |
| **Conditions** | |
| **Next run** | e.g. Run 3 First Baseline Acquisition / Run 4 First Project Site Intake |
| **Blockers** | |

---

## Operator sign-off

| Field | Value |
|-------|-------|
| **Approved** | yes / no / deferred |
| **Approved by** | |
| **Approval date** | |
| **Notes** | |

---

## Related documents

- [intake-workflow.md](../intake-workflow.md)
- [baseline-acquisition-strategy.md](../baseline-acquisition-strategy.md)
- [quarantine-policy.md](../quarantine-policy.md)
- [baseline-readiness-checklist.md](../baseline-readiness-checklist.md)
- [templates/versioned-baseline-passport-template.md](versioned-baseline-passport-template.md)
- [templates/project-site-passport-template.md](project-site-passport-template.md)
