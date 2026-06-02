# OCPilot — Quarantine Policy

**Purpose:** define how the [incoming/](incoming/README.md) zone acts as quarantine, what requires review, when OCPilot must stop, and when to emit **SAFE UNKNOWN**.

**Status:** documented policy only; **no** automated quarantine scanner; **no** runtime enforcement.

**Core safety principle:**

```
Incoming zone = quarantine
Nothing is trusted automatically
```

---

## Quarantine scope

Everything under `incoming/` is **quarantined** until:

1. Intake workflow completes — see [intake-workflow.md](intake-workflow.md)
2. Intake report is filled — see [templates/intake-report-template.md](templates/intake-report-template.md)
3. Operator approves recommended destination or rejection
4. No active **stop condition** below

Quarantine applies equally to baseline candidates and project site materials.

---

## Default assumptions (mandatory)

OCPilot **must assume** until proven otherwise:

| Assumption | Meaning |
|------------|---------|
| **Not clean** | Package may contain modifications, extensions, or live-site debris |
| **Not complete** | Archive may be truncated, partial export, or missing vendor dirs |
| **Label unreliable** | Filename and operator label may not match contents |
| **Secrets possible** | Configs, dumps, and logs may contain credentials and PII |
| **Wrong version possible** | Declared 3.0.3.7 may be 2.x, ocStore mix, or patched core |

---

## Examples requiring quarantine review

All items entering `incoming/` require review. The following **always** warrant elevated scrutiny:

| Example | Typical path | Primary risk |
|---------|--------------|--------------|
| **Unknown ZIP archives** | Either subfolder | Unknown content, malware, wrong platform |
| **Site backups** | `incoming/project-sites/` | Secrets, PII, full live tree |
| **Database dumps** | `incoming/project-sites/` | Credentials, customer data, destructive restore if misused |
| **Mixed packages** | Either subfolder | Baseline + DB + theme bundled; wrong routing |
| **Customer-provided archives** | Either subfolder | Low trust; customizations; mislabeling |
| **Hosting panel exports** | `incoming/project-sites/` | Often «full site» not vendor-clean |
| **«Clean install» without proof** | `incoming/baselines/` | Frequently contains modules or config |
| **Extension/theme-only ZIP** | Usually project-sites | Not baseline; may include encoded payloads |

---

## Risk levels

| Level | Meaning | Typical action |
|-------|---------|----------------|
| **Low** | Documentation-only, sanitized briefs, structure clearly vendor-like with no secret signals | Standard intake; operator approval before move |
| **Medium** | Partial exports, plausible vendor archive with gaps, Medium trust source | Intake report + explicit operator confirmation |
| **High** | Config secrets likely, DB dump present, heavy customization, unknown binaries | **Stop** — list suspicious items; no repo commit of raw material |
| **Critical** | Active credentials in repo path, malware suspicion, uncontrolled destructive SQL | **Halt task** — operator remediation; see SECURITY RISK in [access-and-safety.md](access-and-safety.md) |

Record risk level in intake report.

---

## When OCPilot should stop and ask for operator review

Stop intake progression and request operator decision when:

| # | Stop trigger |
|---|--------------|
| 1 | **Credentials detected** — `config.php` values, API keys, `.env`, connection strings in SQL |
| 2 | **PII / customer data** — orders, users, payment fields in dumps or exports |
| 3 | **Cannot determine platform or version** — and destination selection would guess |
| 4 | **Baseline candidate contains live-site artifacts** — cache, sessions, custom modules, uploads |
| 5 | **Wrong intake subfolder** — baseline labeled package in project-sites or vice versa with conflicting content |
| 6 | **Mixed package without decomposition plan** — operator must confirm split or reject |
| 7 | **Trust level Low** and operator has not acknowledged override |
| 8 | **Archive unreadable or empty** — missing expected structure |
| 9 | **Recommended action is Reject** — do not proceed to move without new package |
| 10 | **SECURITY RISK** — secret already committed or pasted; halt per [boundaries.md](boundaries.md) |

**Forbidden:** silently skipping quarantine because operator said «just use it» without documented approval in intake report sign-off.

---

## SAFE UNKNOWN triggers

Emit **SAFE UNKNOWN** (do not infer) when:

| Trigger | Example |
|---------|---------|
| Version not verifiable from available listing | Archive not extracted; operator has not provided tree list |
| Source not verifiable | «From old laptop» with no URL or checksum |
| Completeness unknown | Size suspiciously small; cannot confirm all vendor dirs |
| ocStore vs OpenCart unclear | Branding removed; hybrid patches |
| DB schema version unknown | Dump present but not safely inspected |
| Sanitization outcome unknown | Operator will strip secrets — until done, readiness unknown |
| Malware / integrity | No checksum; unknown binary — **do not execute** |

Each SAFE UNKNOWN must state **what would verify** the fact — see intake report template.

---

## Quarantine vs destination storage

| Zone | Trust | Retention |
|------|-------|-----------|
| `incoming/` | **None** by default | Temporary |
| `baselines/` | Trusted **only after** intake + readiness checklist | Long-term reference |
| `sites/<slug>/` | Project truth **after** intake + passport; still not vendor-clean | Per-project |

```
Incoming Material  ≠  Trusted Baseline
Incoming Material  ≠  Project Site
```

---

## Post-quarantine outcomes

| Outcome | Meaning |
|---------|---------|
| **Approve move** | Operator moves sanitized material to recommended destination |
| **Approve with conditions** | e.g. strip configs external; partial file set only |
| **Reject** | Package unsuitable; remains external or removed from incoming |
| **Hold** | Awaiting operator evidence (source URL, file list, checksum) |
| **Decompose mixed** | Split into baseline vs project tracks with separate intake reports |

No automatic transitions.

---

## Relation to runs

| Run | Role |
|-----|------|
| Run 2.5 | Quarantine policy defined |
| Run 3 / 4 | First real packages tested against this policy |

See [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).

---

## Related documents

| Doc | Role |
|-----|------|
| [incoming/README.md](incoming/README.md) | Zone layout |
| [intake-workflow.md](intake-workflow.md) | Review steps |
| [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) | Trust and rejection |
| [access-and-safety.md](access-and-safety.md) | Secrets handling |
| [boundaries.md](boundaries.md) | Operational prohibitions |
| [baseline-storage-model.md](baseline-storage-model.md) | What may enter baselines after quarantine |

---

## SAFE UNKNOWN

- Organization-wide retention policy for quarantined archives — not defined in OCPilot; operator policy TBD.
- Automated secret scanning — **not** claimed; filename and operator-assisted review only.
