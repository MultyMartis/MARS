# ORCA Validation CLI Hardening v0.1

**Status:** Local human-operated prototype · **NOT** production runtime.

**Prior:** Phase 7 prototype v0 → hardened v0.1 (self-validating report, deterministic output, golden fixture).

## Purpose

Minimal Node.js CLI for Triumph Manipulator PPC survivability:

1. Load `OrcaPpcDocument` JSON  
2. **Validate input** against `orca-ppc-document-v1.schema.json` (AJV)  
3. Run deterministic rule subset (v0.1)  
4. Build `ValidationReport` JSON  
5. **Validate output** against `validation-report-v1.schema.json` (AJV)  
6. Write `output/validation-report.output.json`  

The validator validates **both** the PPC document **and** its own artifact. Invalid reports → `export_allowed: false` (fail-closed).

## What this is NOT

- Not a service, API, daemon, watcher, scheduler, or auto-validator  
- Not exporter, Direct API, or launch orchestration  
- Not full rule registry (75 rules) — subset only  
- Not semantic AI — deterministic checks only  
- **Does not emit `launch_allowed: true`** — launch is human-only (see below)  

## export_allowed ≠ launch approval

| Field | Who sets | Meaning |
|-------|----------|---------|
| `export_allowed` | Validator (boolean) | No blocking errors + valid schemas → may proceed to **export prep** |
| `launch_allowed` | **Human only** | Never set automatically by this CLI |

`meta.launch_allowed` is always `null` in output to document that the validator does not approve launch.

Even `export_allowed: true` requires operator HITL before Commander import or campaign launch.

## Survivability philosophy

- **Fail-closed** — blocking errors or invalid ValidationReport → `export_allowed: false`  
- **Self-check** — report must pass `validation-report-v1.schema.json`  
- **Deterministic ordering** — stable sorts for `rule_results`, `blocking_errors`, `warnings` (regression-safe)  
- **Human-triggered** — one `node validate.js <file>` per check  
- **Local-only** — no background process  

## Supported rules (v0.1 subset)

| Rule ID | Class | Check |
|---------|-------|--------|
| ST-01 | structural | Required top-level + `schema_version: v1` |
| ST-02 | structural | `search_only_scope: true` |
| SY-01 | symbol | `headline_1` length |
| SY-02 | symbol | `description` length |
| SY-03 | symbol | Non-empty fastlink titles |
| SY-04 | symbol | Non-empty callout text |
| SE-05 | semantic | Primary keyword in `headline_1` |
| SE-07 | semantic | Generic phrase blacklist |
| SE-08 | semantic | Generic CTA blacklist |
| LM-01 | landing_mismatch | Бытовка → `bytovka` route (heuristic) |
| LM-02 | landing_mismatch | Master/fallback + specific intent (warn) |
| CM-02 | commercial | CTA clarity |
| SV-03 | survivability | Duplicate `headline_1` in group |
| SV-04 | survivability | Mixed intent markers in group |
| SV-05 | survivability | Duplicate keyword phrases in group |

Registry SoT: [validation/rule-registry-v1.md](../../validation/rule-registry-v1.md) — v0.1 may simplify semantics per rule ID.

## Exit codes

| Code | When |
|------|------|
| **0** | `export_allowed === true` (no blocking errors, valid input + output schema) |
| **1** | Blocking rule failures, invalid PPC JSON schema, or invalid ValidationReport schema |

Warnings alone do not force exit 1 unless they are the only issue and policy blocks export — blocking errors always exit 1.

## Prerequisites

- Node.js ≥ 18  
- `npm install` in this directory  

## Setup & run

```bash
cd projects/orca/ppc/triumph-manipulator/tools/validation-cli
npm install
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
```

```bash
npm run validate:sample
```

Optional fixed timestamp (golden fixture / diff):

```bash
# PowerShell
$env:ORCA_VALIDATOR_FIXED_TIMESTAMP="2026-05-20T12:00:00.000Z"
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
```

## Outputs

- Console summary (status, schema validity, blocking, warnings)  
- **`output/validation-report.output.json`**  
- Golden reference: [fixtures/validation-report.triumph-s-tier.expected.json](fixtures/validation-report.triumph-s-tier.expected.json)  

## Regression fixture

See [fixtures/README.md](fixtures/README.md) — manual diff vs golden; deterministic sort + fixed timestamp.

## Related docs

- [validation/validation-report-generation-v1.md](../../validation/validation-report-generation-v1.md)  
- [sample-run.md](sample-run.md)  
- [future-expansion-notes-v0.md](future-expansion-notes-v0.md)
