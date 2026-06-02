# OCPilot — Run 3 Preparation

**Purpose:** document operator and OCPilot expectations for **Run 3 — First Baseline Acquisition** using real operator baseline archives.

**Status:** preparation only (Run 2.7); **no** archive import, extraction, or baseline population yet.

**Previous run:** Run 2.7 — Archive Intake & Storage Policy (**DONE**)

**Next run:** Run 3 — First Baseline Acquisition

---

## Run 3 goal

Perform first real baseline acquisition: inspect operator-supplied ocStore archives, produce intake report and passport drafts, validate readiness path — **without automatic baseline promotion**.

Human approval required for all moves from `incoming/baselines/` to `baselines/<version-folder>/`.

---

## Expected operator action (before Run 3)

Copy these ZIP files into the baseline dropzone:

| File | Destination |
|------|-------------|
| `opencart-3.0.3.8-rs.zip` | `projects/ocpilot/incoming/baselines/` |
| `opencart-3.0.3.9-rs.zip` | `projects/ocpilot/incoming/baselines/` |

### Operator rules

| Rule | Meaning |
|------|---------|
| **No extraction required** | Place ZIP as-is; OCPilot inspects structure first |
| **No preprocessing required** | Do not rename internal folders; do not repackage |
| **Do not unpack** | Extraction is OCPilot/operator step during intake if needed |
| **Do not rename after intake begins** | Filename is intake evidence |
| **Do not move during intake** | Keep archives in dropzone until intake report complete and operator approves next step |

---

## Expected archive structure (operator-provided)

OCPilot **must not** assume OpenCart files at ZIP root.

### opencart-3.0.3.8-rs.zip

```
upload-3038-rs2/
  admin/
  catalog/
  image/
  system/
  config.php
  index.php
  ...
```

### opencart-3.0.3.9-rs.zip

```
upload-3039-rs1/
  admin/
  catalog/
  image/
  system/
  config.php
  index.php
  ...
```

See [archive-intake-rules.md](archive-intake-rules.md) for Archive Root → Package Root → OpenCart Root workflow.

---

## Priority order (Run 3)

Acquire and process in this order unless operator directs otherwise:

| Priority | Archive | Package Root | Target baseline |
|----------|---------|--------------|-----------------|
| **1** | `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` | `baselines/ocstore-3038-rs2/` |
| **2** | `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` | `baselines/ocstore-3039-rs1/` |

---

## Expected OCPilot tasks during Run 3

Human-supervised; agent assists; operator approves.

| Task | Output |
|------|--------|
| **Archive inspection** | Archive Root listing documented |
| **Package root detection** | Package Root path recorded |
| **OpenCart root detection** | OpenCart Root path recorded |
| **Precheck** | [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md) completed |
| **Intake report generation** | [templates/intake-report-template.md](templates/intake-report-template.md) filled |
| **Passport generation** | Draft per [templates/versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md) |
| **Readiness validation** | Pre-placement review; full [baseline-readiness-checklist.md](baseline-readiness-checklist.md) after operator-approved placement |

### Explicitly out of scope for automatic execution

| Forbidden automatic action | Reason |
|----------------------------|--------|
| Automatic baseline promotion | Human approval gate — [intake-workflow.md](intake-workflow.md) |
| Automatic extraction to `baselines/.../files/` | Sanitization and operator confirmation required |
| Automatic commit of large binaries | Operator repo policy |
| Declaring baseline **READY** without readiness checklist | [baseline-readiness-checklist.md](baseline-readiness-checklist.md) |

---

## Run 3 workflow (summary)

```
Operator copies ZIPs → incoming/baselines/
        ↓
OCPilot: precheck + archive intake rules
        ↓
OCPilot: intake report + draft passport
        ↓
Operator review (HITL)
        ↓
Operator approves sanitization + placement
        ↓
Populate baselines/ocstore-3038-rs2/ (then ocstore-3039-rs1/)
        ↓
Passport final + readiness checklist
        ↓
# REPORT — OCPilot Run 3 First Baseline Acquisition
```

Repeat per archive in priority order.

---

## Storage policy reminder

| Class | Run 3 handling |
|-------|----------------|
| ZIP in `incoming/baselines/` | Canonical source during quarantine |
| Temporary extract | For inspection/manifest only; do not keep duplicate copies unnecessarily |
| `passports/`, `manifest/`, `comparison-notes/` | Permanent metadata after approved placement |

See [baselines/storage-policy.md](baselines/storage-policy.md).

---

## Run 3 entry documents

| Doc | Role |
|-----|------|
| [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md) | First gate |
| [archive-intake-rules.md](archive-intake-rules.md) | Structure detection |
| [intake-workflow.md](intake-workflow.md) | Full intake steps |
| [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) | Trust and rejection |
| [quarantine-policy.md](quarantine-policy.md) | Stop conditions |
| [incoming/baselines/README.md](incoming/baselines/README.md) | Dropzone |

---

## SAFE UNKNOWN

- Exact archive sizes and checksums — until operator places files.
- Whether both archives will be processed in one Run 3 session or split — operator decision.
- Final storage of canonical ZIP after intake (repo vs external) — operator policy.

---

## After Run 3

| Run | Focus |
|-----|-------|
| Run 4 | First Project Site Intake |
| Run 5 | Read-Only Audit |

See [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).
