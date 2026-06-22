# ORCA Semantic Contract Runtime Lock v1

**Lock ID:** `orca-semantic-contract-runtime-lock-v1`  
**Generated:** 2026-06-22  
**Source charter commit:** `3a5ec5d`  
**Machine-readable:** [`orca-semantic-contract-runtime-lock-v1.json`](orca-semantic-contract-runtime-lock-v1.json)

## Purpose

Pin checksums and fixture-compatible operator scope for integration core without modifying the authority manifest.

## Distinction

| Artifact | Role |
|----------|------|
| Authority manifest (`integration/contracts/`) | Operator-approved contract loading specification |
| Runtime lock (`runtime/config/`) | Implementation pinning generated from approved authority + measured checksums |

## Pinned at implementation

- `orca-semantic-intelligence-quality-gates` — `5F05F72F87007D3B6A43CED4D98B07A390DC0CEDBD5CA7A6131981B4FF98186B`
- `project-operator-scope` (fixture) — `AC6A25B5C80C61F7C7D546CEDFB57FE123E6471C578EF503A47AA718290073BA`

All other required contract checksums match authority manifest v1 values.
