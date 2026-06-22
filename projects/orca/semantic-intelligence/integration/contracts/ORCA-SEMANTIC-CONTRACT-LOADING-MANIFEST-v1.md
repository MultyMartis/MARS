# ORCA Semantic Contract Loading Manifest v1

**Manifest ID:** `orca-semantic-contract-loading-manifest`  
**Bundle:** `p0-i-bundle-v1`  
**Machine-readable:** [`orca-semantic-contract-loading-manifest-v1.json`](orca-semantic-contract-loading-manifest-v1.json)

---

## Purpose

Machine-readable registry of canonical semantic contracts, their consumers, load order, version pins, and blocking failure modes for P0-I admission integration.

---

## Global failure modes

| Condition | Message | Severity |
|-----------|---------|----------|
| Missing required contract | `BLOCKED — REQUIRED SEMANTIC CONTRACT NOT LOADED` | FATAL |
| Version mismatch | `BLOCKED — SEMANTIC CONTRACT VERSION MISMATCH` | FATAL |
| Checksum mismatch | `BLOCKED — SEMANTIC CONTRACT VERSION MISMATCH` | FATAL |

---

## Load order summary

1. Version authority + ADR  
2. Admission policy + quality gates  
3. Taxonomy family (7 files)  
4. Schema + decision trace  
5. Invariants  
6. Annotation guideline  
7. Project operator scope (pilot-bound)  
99. Legacy regex (optional, diagnostic only)

---

## Integration status labels

| Label | Meaning |
|-------|---------|
| `INTEGRATED` | Consumer loaded, version matched, fields consumed, blocking active |
| `REGISTERED — NOT INTEGRATED` | Listed in README/manifest only |
| `LOADED — NOT CONSUMED` | File read but rules not applied to output |

---

## Maintenance

Checksums for contracts without pinned hash must be set during implementation task **I-01 Contract loader** before pilot execution.
