# SPPC-01 — Business Intake and Operator Authority

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-01-business-intake.md`

---

## Stage ID

SPPC-01

## Name

Business Intake and Operator Authority

## Purpose

Establish operator authority, commercial scope, risk posture, and project charter before any semantic or campaign work begins. ATLAS owns the intake record and binds who may advance the lifecycle.

## Owning system

ATLAS

## Participating systems

- Operator
- MIG (read-only context)
- ORCA (read-only context)

## Required inputs

- Operator identity and authority declaration
- Client or brand identifier and commercial objective
- Geography, language, and platform targets (e.g. Yandex Direct Search)
- Budget envelope and timeline constraints
- Known constraints: legal, compliance, brand voice, prohibited claims
- Pointer to prior campaigns or SAFE UNKNOWN declaration

## Optional inputs

- Historical performance exports
- Existing site or landing inventory
- Competitor shortlist from operator
- CRM or lead-routing notes

## Source-of-truth rules

- ATLAS intake record is SoT for operator authority and scope boundaries.
- No downstream system may override intake scope without a documented ATLAS reopen.
- Commercial claims not captured in intake are SAFE UNKNOWN until explicitly added.

## Required processing

- Validate operator authority and signing role.
- Capture commercial objective, KPI intent, and failure tolerance.
- Record geography, platform, and budget envelope.
- Declare prohibited topics, claims, and out-of-scope services.
- Issue intake completion token for SPPC-02.

## Required outputs

- ATLAS business intake record (versioned markdown or JSON)
- Operator authority statement with effective date
- Scope boundary manifest (in-scope / out-of-scope / SAFE UNKNOWN)
- Risk and compliance notes

## Prohibited outputs

- Keyword lists or semantic classifications
- Campaign structure or ad copy
- Pilot corpus substitutions framed as production intake
- Implicit launch authorization

## Validation rules

- All required intake fields populated or explicitly marked SAFE UNKNOWN.
- Operator role and approval chain documented.
- No downstream artifact references without intake version binding.

## Blocking conditions

- Missing operator authority declaration
- Undefined geography or platform target
- Conflicting scope statements without resolution
- Intake record not versioned or not written to project path

## Completion status

COMPLETE when intake record is approved and version-stamped; status token `intake_approved`.

## Evidence requirements

- Committed intake file under project intake path
- REPORT or audit line referencing intake version ID
- Operator sign-off timestamp

## Next allowed stages

- SPPC-02

## Rollback / reopen behavior

Reopen intake invalidates all downstream stage tokens. Operator must re-approve scope changes; MIG/ORCA artifacts remain read-only until new intake version is bound.

## Responsible role

Operator (primary); ATLAS maintainer (documentation)

## Operator approval required

yes
