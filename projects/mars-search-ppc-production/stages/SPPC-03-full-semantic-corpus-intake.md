# SPPC-03 — Full Semantic Corpus Intake

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-03-full-semantic-corpus-intake.md`

---

## Stage ID

SPPC-03

## Name

Full Semantic Corpus Intake

## Purpose

Ingest the complete semantic demand corpus for the scoped geography and language. Production lifecycle requires full corpus intake — no pilot row-cap substitution.

## Owning system

MIG / ORCA (joint)

## Participating systems

- MIG (ingestion)
- ORCA (corpus binding)
- Operator (scope witness)

## Required inputs

- SPPC-02 sources_registered token
- Full Wordstat or equivalent demand export for scoped market
- Registered source manifest with valid checksums
- Intake geography and language binding

## Optional inputs

- Supplementary long-tail exports
- Seasonal adjustment notes from operator
- Legacy corpus for diff-only analysis (not substitution)

## Source-of-truth rules

- Committed full corpus artifact is SoT for raw demand rows entering normalization.
- Row count and checksum must match registered sources — no partial silent drops.
- 200-row pilot slices are explicitly prohibited as production corpus substitutes.

## Required processing

- Ingest 100% of registered demand rows for scoped market.
- Reject or quarantine rows outside geography/language scope.
- Record corpus statistics: row count, unique queries, date range.
- Bind corpus to source registry and intake version.
- Emit corpus intake receipt for SPPC-04.

## Required outputs

- Full semantic corpus artifact (JSON or canonical table)
- Corpus intake receipt with row count, checksum, and scope binding
- Quarantine log for out-of-scope rows

## Prohibited outputs

- 200-row or other pilot-substitution corpora labeled as production
- Normalized or classified keyword registry
- Campaign-ready keyword lists
- Silent truncation without operator waiver on record

## Validation rules

- Row count matches sum of registered source rows minus documented quarantine.
- No pilot slice filename or metadata present.
- Corpus checksum stable across re-ingest of same sources.
- Geography and language filters documented.

## Blocking conditions

- SPPC-02 incomplete
- Corpus row count below registered source total without waiver
- Pilot slice detected in production path
- Checksum mismatch

## Completion status

COMPLETE when full corpus committed and `corpus_intake_complete` token issued.

## Evidence requirements

- Committed corpus artifact path and size
- Intake receipt with explicit full-corpus row count
- REPORT confirming no pilot substitution

## Next allowed stages

- SPPC-04

## Rollback / reopen behavior

Corpus replacement reopens SPPC-03 through all semantic stages. Operator must acknowledge row-count delta.

## Responsible role

MIG ingestion lead with ORCA corpus binding witness

## Operator approval required

yes — witness sign-off that full corpus, not pilot, was ingested

## Charter notes

**Charter rule:** Full corpus only. The 200-row P0-I pilot pattern is integration evidence, not a production intake substitute. Any waiver for partial corpus requires explicit operator charter amendment.
