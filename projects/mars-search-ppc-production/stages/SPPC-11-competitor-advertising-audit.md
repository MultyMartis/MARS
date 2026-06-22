# SPPC-11 — Competitor Advertising Audit

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-11-competitor-advertising-audit.md`

---

## Stage ID

SPPC-11

## Name

Competitor Advertising Audit

## Purpose

Audit competitor advertising presence, messaging patterns, and offer positioning using MIG research outputs to inform strategy without copying non-compliant claims.

## Owning system

MIG

## Participating systems

- ORCA (strategy consumption)
- Operator (compliance review)

## Required inputs

- SPPC-02 sources_registered token
- Competitor domain / advertiser list
- SPPC-10 SERP pack (when available)
- Intake compliance boundaries

## Optional inputs

- Historical competitor exports
- Operator anecdotal notes

## Source-of-truth rules

- Competitor audit artifact is SoT for observed competitor ads at audit time.
- Audit is observational — not authorization to copy claims.
- Compliance filter from intake overrides attractive competitor copy.

## Required processing

- Identify competitor ads for scoped queries and domains.
- Extract themes, offers, CTAs, and landing patterns (observational).
- Flag compliance risks vs intake prohibited claims.
- Summarize whitespace and saturation signals.
- Emit audit pack for SPPC-12.

## Required outputs

- Competitor advertising audit document
- Domain-level summary tables
- Compliance risk flags

## Prohibited outputs

- Plagiarized ad copy ready for paste
- Unauthorized trademark use recommendations
- Campaign export artifacts

## Validation rules

- Competitor list matches intake scope.
- Compliance flags present for risky patterns.
- Audit date stamped.

## Blocking conditions

- SPPC-02 incomplete
- Empty competitor list without SAFE UNKNOWN waiver

## Completion status

COMPLETE when audit committed and `competitor_audit_ready` token issued.

## Evidence requirements

- Audit artifact path
- Competitor list version
- Compliance review note

## Next allowed stages

- SPPC-12

## Rollback / reopen behavior

Competitor list change reopens audit; SPPC-12 pack section must refresh.

## Responsible role

MIG competitive research lead

## Operator approval required

no
