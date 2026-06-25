# ORCA Benchmark Versioning Policy v1

**Policy ID:** `orca-benchmark-versioning-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Version benchmark **packages**, **splits**, and **gold records** without silent mutation.

---

## Version dimensions

| Dimension | Field | Rule |
|-----------|-------|------|
| Charter | `benchmark/charters/*-vN` | Semver in filename |
| Package | `benchmark_version` | Major bump on stratum/split policy change |
| Record | `semantic_record.record_version` | Bump on gold relabel |
| Taxonomy | `versioning.taxonomy_version` | Pin to P0-B release |
| Guideline | `versioning.rule_version` | Pin to P0-C release |

---

## Supersession

New package version → old package `SUPERSEDED` — not deleted. Blind pack hash archived.

---

## Contamination

Leakage or protocol breach → `CONTAMINATED` — evaluation forbidden until operator withdraws or rebuilds.
