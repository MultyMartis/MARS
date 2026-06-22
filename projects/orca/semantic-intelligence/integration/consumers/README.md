# ORCA Semantic Contract Consumers — Index v1

**Date:** 2026-06-22

| # | Consumer | Specification |
|---|----------|---------------|
| 1 | Taxonomy | [`ORCA-TAXONOMY-CONSUMER-v1.md`](ORCA-TAXONOMY-CONSUMER-v1.md) |
| 2 | Semantic record schema | [`ORCA-SEMANTIC-RECORD-SCHEMA-CONSUMER-v1.md`](ORCA-SEMANTIC-RECORD-SCHEMA-CONSUMER-v1.md) |
| 3 | Annotation policy | [`ORCA-ANNOTATION-POLICY-CONSUMER-v1.md`](ORCA-ANNOTATION-POLICY-CONSUMER-v1.md) |
| 4 | Invariant | [`ORCA-INVARIANT-CONSUMER-v1.md`](ORCA-INVARIANT-CONSUMER-v1.md) |
| 5 | Risk mode | [`ORCA-RISK-MODE-CONSUMER-v1.md`](ORCA-RISK-MODE-CONSUMER-v1.md) |
| 6 | Operator scope | [`ORCA-OPERATOR-SCOPE-CONSUMER-v1.md`](ORCA-OPERATOR-SCOPE-CONSUMER-v1.md) |
| 7 | Version authority | [`ORCA-VERSION-AUTHORITY-CONSUMER-v1.md`](ORCA-VERSION-AUTHORITY-CONSUMER-v1.md) |

**Machine-readable index:** [`orca-semantic-consumers-index-v1.json`](orca-semantic-consumers-index-v1.json)

Every required semantic contract in the loading manifest must map to exactly one primary consumer. Secondary readers (e.g. validator) must declare dependency on primary consumer output.
