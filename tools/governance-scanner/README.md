# Governance scanner — PILOT 01 (experimental)

**Status:** narrow **local-only** operational experiment. **Not** governance enforcement, **not** CI, **not** a runtime or orchestration component.

## What it does

- **Human-operated:** you run `node governance-scanner.js` explicitly when you want a pass.
- **Read-only:** reads markdown files and prints matches; **does not** modify the repository.
- **Transparent:** rules live in `forbidden-phrases.json`; no hidden caches or background watchers.
- **Non-persistent:** no state files, no telemetry.

The pilot helps operators spot **suspicious wording** aligned with themes in:

- `governance/enforcement/forbidden-runtime-claims.md`
- `governance/tooling-boundary-rules.md`
- `governance/operationalization-drift-warnings.md`

Matches are **hints for human review**, not proof of a policy violation.

## What it is not

- Not an autonomous validator, control plane, or daemon.
- Not automatic enforcement, auto-fix, or auto-patch.
- Not runtime monitoring or orchestration.

## Limitations and false positives

- Substring search only: **no** NLP, negation detection, or “this is a quote” analysis.
- Governance docs that **define** forbidden patterns may still **contain** those strings — expect noise; triage with context.
- Severity labels are **heuristic** labels on phrases, not a product risk score.

## SAFE UNKNOWN

Whether a hit is a real drift claim depends on **human** judgment and evidence paths in-repo. If unclear, use **SAFE UNKNOWN** and record what would verify.

## Governance alignment

- [operational-tooling-overview.md](../../governance/operational-tooling-overview.md) — S5 tooling role and boundaries.
- [experimental-tooling-status.md](../../governance/experimental-tooling-status.md) — experimental vs runtime capability.
- [operational-experiments-overview.md](../../governance/operational-experiments-overview.md) — narrow pilots and evidence discipline.

## Example

From repository root (`C:\MARS Phenix\AI MARS`):

```bash
node tools/governance-scanner/governance-scanner.js --root governance
```

Default root is the **current working directory**:

```bash
cd tools/governance-scanner
node governance-scanner.js --root ../..
```
