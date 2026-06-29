# REPORT — Corvonero Commander CT-5 orchestrator and reproducibility v1

**Date:** 2026-06-30  
**Scope:** CT-5 orchestrator security review, output integrity, isolated reproducibility, selective Git checkpoint

## Executive summary

The CT-5 orchestrator `execute-ct5-commander-generation-v1.mjs` is a read-mostly, storage-scoped generation pipeline with zero network, Direct, Commander import, semantic or Git mutation capability. Five Commander import candidate workbooks in Storage were independently reopened, hash-verified against on-disk receipts, and reproduced into an isolated directory with **identical normalized workbook content**.

**Note on task binding hashes:** the SHA-256 values listed in the CT-5 task binding block do **not** match files on disk or any attested receipt in Storage/repository. Recalculated on-disk hashes **do** match `CORVONERO-COMMANDER-CT5-MANIFEST-v1.json` and generation receipts. Treat task binding hashes as **SAFE UNKNOWN / unattested**; operational truth is the manifest-attested set below.

## Preflight

| Check | Result |
|-------|--------|
| Drive X: | OK |
| Volume label AI WS | OK |
| Repository | `X:\AI MARS\` |
| Branch | `mars/canonical-post-recovery` @ `8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86` |

## Authority and template

- CT-4 authority commit: `8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86`
- Safe tooling commit: `c81aadda412b473e99660605b38209e74cd683e9`
- Template SHA-256: `1112793a888ac2e0762317fa0bf728a116e36a143fc72fa0f5fe729c56c3f1fa` — verified
- Sheet `Тексты`, header row 14, 78 columns — verified

## On-disk XLSX hashes (manifest-attested)

| File | SHA-256 |
|------|---------|
| CA-01 | `6b0894fbd49f19c20b9b10de830d2ab6ce4a675b0cb61603c1f0d1d5ebb24cd2` |
| CA-02 | `5938c31485f91ec7816c32af8fa58eebee154a6dc54953368c5d22d3ff29e30c` |
| CA-03 | `3757acacc35f9262ac8b14ea52e6c2fcfc5910fc35053f1e7ccac086a6a88726` |
| CA-04 | `c2689e23736d91c65eb76bd72beb8984a0d8b82d352a8e42ac6755d5e9af37c1` |
| CA-05 | `8a39b1a280e7ef16b7420ddaa850e1dae1c14bf2fc58e7b6b9d7860beacfa129` |

## Reproducibility

Isolated repro directory: `CORVONERO-COMMANDER-CT5-REPRO-CHECK-2026-06-30`

- Binary SHA-256: differs (ZIP timestamps)
- Normalized workbook content: **IDENTICAL**
- Forensic totals: 5 campaigns, 21 groups, 833 keywords, 21 primary ads

## Orchestrator classification

**SAFE FOR THIS FROZEN CT-5 OUTPUT BUT REQUIRES BASE TOOLING PATCH BEFORE REUSE**

Four CT-5-only fixes (row extension, metadata translation, fastlink clearing, organization blanking) should migrate into `tools/commander-transport/` before general reuse. Base tooling was not modified in this task.

## Checkpoint scope

Committed: orchestrator, CT-5 receipts, review/repro receipts, reports.  
Excluded: all XLSX, Storage paths, legacy Commander artifacts, semantic material.

## Authorization state

- Commander import: **NOT PERFORMED**
- Server upload: **NOT AUTHORIZED**
- Yandex Direct: **NOT ACCESSED**
- CT-6 local import test: **READY FOR SEPARATE OPERATOR AUTHORIZATION**
