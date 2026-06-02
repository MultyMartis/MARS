# EAR OpenCart Consumer Guide v1

**Purpose:** Document how **OCPilot** (primary consumer) should consume OpenCart Snapshot Packages produced under [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md).  
**Status:** consumer contract — **no** OCPilot implementation claimed.  
**Phase:** 2A

---

## Scope

| In scope | Out of scope |
|----------|--------------|
| Intake rules, assumptions, prohibitions | OCPilot code, scripts, diff tools |
| SAFE UNKNOWN handling for Run 5 | Live connector configuration |
| Quality level gating for audit phases | EAR acquisition implementation |

Other consumers (e.g. future Website Factory) may adopt this guide by charter — **SAFE UNKNOWN** until explicitly mapped.

---

## Consumer role in the stack

```
Operator → EAR → Snapshot Package → OCPilot (this guide) → Reports
```

OCPilot is a **read-only analysis** system. It consumes snapshots; it does **not** acquire evidence from live sites by default when a snapshot path is chartered.

---

## Intake procedure (conceptual)

1. **Receive** published snapshot reference (logical package + optional bulk ref).
2. **Verify** `snapshot_contract` = `ear-opencart-snapshot-v1` (or documented successor).
3. **Read** declared **quality level** in metadata — gate audit phases accordingly.
4. **Read** `safe-unknown` **before** starting dependent phases.
5. **Corroborate** metadata claims using file-manifest and version proof files — never trust claims alone.
6. **Run** audit phases allowed for quality level; **halt** with explicit report when blocked.
7. **Record** `snapshot_id` on every report artifact.

---

## What OCPilot may assume

Assumptions are **conditional** on a valid published package at the stated quality level.

| Assumption | Condition |
|------------|-----------|
| **Snapshot is point-in-time** | Evidence reflects acquisition date, not live site now |
| **Site ID is stable** | `site_id` matches registry (e.g. SITE-001) |
| **Read-only charter** | Analysis does not require write access to external site |
| **Baseline reference is intentional** | `baseline_approved` in metadata selects comparison target (e.g. `ocstore-3038-rs2`) |
| **Environment enum is operator-asserted** | `environment_class` is safety input, not cryptographic proof |
| **Manifest paths are relative to site root** | Unless `safe-unknown` says otherwise |
| **Extension list is good-faith** | At Level 2+, suitable for risk **indicators**, not legal compliance proof |
| **No PII in database-metadata** | If package violated this, operator error — consumer should still refuse to ingest row dumps into git |
| **Acquisition mode is recorded** | Mode 0 packages may be noisier than future Mode 2 |

---

## What OCPilot must not assume

| Prohibition | Reason |
|-------------|--------|
| **Completeness** | Empty section without `safe-unknown` entry is a contract defect — treat as unknown |
| **Platform version from metadata alone** | Use `Detected version` + file-manifest version files |
| **PRODUCTION vs TEST from URL** | URLs can mislead; honor `environment` + operator assertion |
| **All extensions discovered** | Partial scans and Mode 0 drops leave gaps |
| **OCMOD list is conflict-free** | v1 inventory is mapping, not static analysis |
| **Database-metadata implies data parity** | Schema only — no row counts for business logic |
| **SEO section replaces crawl** | Metadata indicators only |
| **Snapshot includes file contents** | v1 manifest may be paths/hashes only |
| **Live site matches snapshot** | No silent re-fetch from hosting without new charter |
| **Credentials in package** | Must not use embedded secrets; use operator `secret_ref` outside git if ever needed for human steps |

---

## Quality level → OCPilot phase gating

Map OCPilot Run 5-style phases to minimum snapshot level (conceptual — exact phase names live in OCPilot docs).

| Minimum level | Typical OCPilot work allowed |
|---------------|------------------------------|
| **0** | Register snapshot; document blockers only |
| **1** | Version proof attempt; baseline file manifest diff (if manifest adequate); schema summary |
| **2** | Extension risk analysis; ocMod customization map |
| **3** | Full read-only audit per charter, subject to residual `safe-unknown` |

If charter demands Level 3 work but package is Level 1, OCPilot **halts** and reports **acquisition gap** — not “best effort” completion.

---

## Section-by-section consumer usage

| Section | OCPilot use |
|---------|-------------|
| **metadata** | Report header, baseline id, acquisition date, mode |
| **file-manifest** | Diff vs `baselines/ocstore-3038-rs2/` or approved baseline |
| **theme-info** | Theme override and template audit |
| **extension-inventory** | Risk register, unknown surface |
| **ocmod-inventory** | Link mods to manifest deltas |
| **database-metadata** | Compare to baseline `database-metadata` artifacts |
| **seo-structure** | SEO URL / rewrite chapter in audit report |
| **environment** | Halt or watermark reports for PRODUCTION; caution banner for UNKNOWN |
| **safe-unknown** | Phase block list with unblock hints for operator |
| **acquisition-log** | Reproducibility footnote in reports |

---

## SAFE UNKNOWN rules (mandatory)

1. **Propagate** — Report must list consumer-relevant `safe-unknown` topics; do not hide behind “partial success.”
2. **Do not hallucinate** — Missing version proof → report UNKNOWN, do not guess ocStore build.
3. **Do not fill from baseline** — Baseline informs diff; it is not site truth.
4. **Do not fill from charter** — Charter says what audit is allowed; snapshot says what evidence exists.
5. **Unblock path** — When `safe-unknown` includes unblock hint, cite it in DATA-REQUEST style notes to operator — **no** automatic acquisition.
6. **New snapshot required** — After operator acquires more evidence, new `snapshot_id` — do not mutate old package analysis in place without explicit supersession note.

---

## SITE-001 / Run 5 alignment (documentation)

| Fact | Consumer behavior |
|------|-------------------|
| Run 5 paused pending snapshot path | Do not claim Run 5 complete without Level 1+ `file-manifest` minimum |
| Approved baseline `ocstore-3038-rs2` | Use for diff when `baseline_approved` true |
| Freeze [site-001-pre-runtime-bridge](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Blockers B-EV-* remain until snapshot sections exist |

---

## Handoff from EAR

| EAR delivers | OCPilot accepts |
|--------------|-----------------|
| Published snapshot per lifecycle | Yes |
| Candidate unpublished package | No — Validate stage incomplete |
| Raw WinSCP folder without spec wrap | No — operator must wrap or EAR must assemble (Mode 0 wrap still applies contract) |
| Credentials file | **Reject** for git; operator-only external storage |

---

## Reports and artifacts

- All OCPilot reports reference `snapshot_id` and quality level.
- Findings live under OCPilot `reports/` — not in EAR folder.
- EAR does not edit consumer reports.

---

## Future consumers

| Consumer | Note |
|----------|------|
| **WPilot** | WordPress-specific spec TBD — do not reuse OpenCart section names blindly |
| **Website Factory** | **SAFE UNKNOWN** — may need unified contract Phase 4 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | Package definition |
| [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md) | When intake is valid |
| [projects/ocpilot/OPERATIONAL-INDEX.md](../../projects/ocpilot/OPERATIONAL-INDEX.md) | Run 5 status |
| [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Blockers |

---

## SAFE UNKNOWN

- Exact OCPilot phase ID → quality level matrix in OCPilot repo — may differ in naming; this guide sets minimum evidence rules only.
- Whether OCPilot ingests from zip vs folder — consumer storage choice, not EAR v1.
