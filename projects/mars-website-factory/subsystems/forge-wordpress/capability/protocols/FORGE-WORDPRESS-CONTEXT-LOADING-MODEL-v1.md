# Forge WordPress Context Loading Model v1

**Document type:** Context authority and loading protocol  
**Version:** v1  
**Stage:** FW-04

---

## Tier order

Load context in this order. Higher tiers override lower tiers on conflict.

| Tier | Authority | Examples |
|------|-----------|----------|
| **T1 — MARS authority** | Governance, AGENTS.md, execution model | `AGENTS.md`, `governance/execution-model.md` |
| **T2 — Forge WordPress subsystem** | Subsystem contracts, standards, capability pack | `subsystems/forge-wordpress/contracts/`, `capability/` |
| **T3 — Project authority** | Project intake, passport, operator decisions | Project intake, WAD, content model |
| **T4 — Approved frontend** | Handoff package, block inventory, assets | Approved `dist/` or equivalent |
| **T5 — Environment evidence** | Local tooling audit, env profile | FW-05 env docs when available |
| **T6 — Task-specific files** | Current task inputs only | Diff, spec section, single template |

**Rule:** Do not load entire MARS tree. Load only tiers required for the task class.

---

## Minimum context by task class

### Architecture (WAD, theme architecture)

| Tier | Required |
|------|----------|
| T1 | AGENTS.md (truth boundaries) |
| T2 | FW-01 architecture, FW-S-03, FW-S-04, execution contract, specialist profile |
| T3 | Project intake, implementation mode |
| T4 | Frontend handoff manifest, block/section inventory |
| T5 | Local environment decision (if implementation planned) |
| T6 | Prior WAD draft if revision |

### Content model

| Tier | Required |
|------|----------|
| T2 | FW-S-01, FW-S-02, content model template |
| T3 | Project intake, content evidence |
| T4 | Page list, editable region candidates from frontend |
| T6 | WAD if exists |

### ACF design

| Tier | Required |
|------|----------|
| T2 | FW-S-02, ACF schema template |
| T3 | Approved content model |
| T4 | Block-to-field mapping inputs |
| T6 | CPT map if exists |

### Theme implementation

| Tier | Required |
|------|----------|
| T2 | FW-S-03, FW-S-07, FW-SK-10, safe command policy, filesystem scope |
| T3 | Approved WAD, implementation spec, template map |
| T4 | Approved frontend source (read-only) |
| T5 | Tool registry, env profile |
| T6 | Current implementation diff scope |

### Validation

| Tier | Required |
|------|----------|
| T2 | FW-S-08, validation standard, validator profiles, independence policy |
| T3 | Validation plan |
| T4 | Frontend baselines for visual parity |
| T5 | Validation runner architecture |
| T6 | Implementation artifacts under test |

### Packaging / release

| Tier | Required |
|------|----------|
| T2 | Packaging design, release manifest template, git workflow |
| T3 | Validation reports (pass or documented waivers) |
| T6 | Built theme/plugin paths |

### WPilot handoff

| Tier | Required |
|------|----------|
| T2 | FW-C-03, handoff template, WPilot boundary docs |
| T3 | Release manifest, validation evidence |
| T6 | Handoff checklist |

---

## Anti-overload rules

1. **Load only relevant documents** — use OPERATIONAL-INDEX routing, not directory walks.
2. **Summarize large packs** — if a frontend package exceeds practical context, produce a structured inventory first (FW-SK-01).
3. **Do not infer absent facts** — use **SAFE UNKNOWN** and list what would verify the fact.
4. **Preserve project authority order** — T3 project decisions beat generic subsystem defaults.
5. **No stale chat memory** — re-read canonical files for the active task.
6. **No cross-project leakage** — never load FP-0002 or other project artifacts unless task explicitly targets that project.

---

## Context load manifest (required in reports)

```text
Tiers loaded: T1, T2, T3, T4
Files read:
  - <path> — <purpose>
Skipped (not required for this task):
  - <path> — <reason>
SAFE UNKNOWN:
  - <item> — <what would verify>
```

---

## Related

- [FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md)
- [../../FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](../../FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)
- [../../registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md](../../registries/FORGE-WORDPRESS-CONTRACTS-AND-STANDARDS-REGISTER-v1.md)

---

*Context loading model v1.*
