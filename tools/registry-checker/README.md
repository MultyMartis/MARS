# PILOT 02 — Registry consistency checker (experimental)

**What this is:** a **narrow**, **local-only**, **human-invoked** helper that prints **heuristic hints** about registry-adjacent wording and identifiers. It supports **evidence-oriented drift triage**, not automated truth.

**What this is not:** runtime development, orchestration, a governance enforcement engine, registry synchronization, hidden automation, background validation, or autonomous consistency management.

## Principles

1. **Human interpretation is primary** — output is triage, not verdicts.
2. **Hints, not truth** — expect **false positives** and **SAFE UNKNOWN** until a human reconciles sources.
3. **Read-only** — scans files under `--root`; **no writes**, **no caches**, **no watchers**, **no daemons**.
4. **Explicit execution** — run Node locally when you choose; nothing runs in the background.

## Governance alignment (documentation)

- [governance/registry-source-of-truth.md](../../governance/registry-source-of-truth.md) — human precedence; no sync engine claims.
- [governance/registry-architecture.md](../../governance/registry-architecture.md) — registry documentation role.
- [governance/identity-and-naming-rules.md](../../governance/identity-and-naming-rules.md) — adapter vs system vocabulary.
- [governance/operational-experiments-overview.md](../../governance/operational-experiments-overview.md) — S7 operational experiment framing.

## Usage

From the repository root (paths adjusted for your machine):

```bash
node tools/registry-checker/registry-checker.js --root governance
```

Include selected JavaScript and JSON (optional):

```bash
node tools/registry-checker/registry-checker.js --root governance --scan-js-json
```

Dry-run (lists scan configuration only; **no rule evaluation**):

```bash
node tools/registry-checker/registry-checker.js --root governance --dry-run
```

Help:

```bash
node tools/registry-checker/registry-checker.js --help
```

## Rule dataset

`registry-rules.json` holds a **small**, **transparent** set of:

- **line hints** — single-line pattern checks (e.g. registry path without an on-line SoT cue).
- **file hints** — whole-file heuristics for narrow paths (e.g. `mars-runtime` adapter JS missing experimental tokens).
- **collectors** — cross-file duplicate **hints** for repeated backticked identifiers.

Edit rules deliberately; keep the dataset **lightweight** (no large schemas).

## Limitations and SAFE UNKNOWN

- **No** claim of completeness, uniqueness proof, or drift detection certainty.
- **No** understanding of Markdown tables, negated prose, or quoted counterexamples beyond simple regex.
- Cross-file “duplicates” may be **intentional** (examples, mirrors, legacy packs).

## Non-goals

- Automatic registry reconciliation, normalization, or rewriting.
- Policy enforcement, CI gating, or telemetry.
- Defining canonical IDs — canonicality remains in governance tables and human review per SoT rules.
