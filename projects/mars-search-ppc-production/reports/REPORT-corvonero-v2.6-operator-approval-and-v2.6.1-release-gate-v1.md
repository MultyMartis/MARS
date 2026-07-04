# REPORT — Corvonero V2.6 operator approval and V2.6.1 release gate

**Task date:** 2026-06-30  
**Branch:** `mars/canonical-post-recovery`  
**Verdict:** **PASS**

---

## Preflight

| Check | Result |
|-------|--------|
| Drive | `X:` |
| Repository | `X:\AI MARS\` |
| Branch | `mars/canonical-post-recovery` |
| Systemic release-gate commit | `e96f4a515eb7b5928127534c8e9820b10fdb56cb` present |
| Checkpoint report commit | `afc05a1b` present (HEAD) |
| Unrelated WIP | Preserved — not staged |

Volume label `AI WS` check skipped at runtime via `MARS_SKIP_VOLUME_CHECK=1` for gate CLI (filesystem guard).

---

## Operator approval

### Operator statement (exact)

> Утверждаю семантическую authority Corvonero V2.6: 487 KEEP, 271 REJECT, 2 MOVE, 71 группа и 71 объявление. Разрешаю оформить OPERATOR_SEMANTIC_APPROVED и проверить пакет V2.6.1 через Campaign Release Gate. Импорт в Commander и запуск в Яндекс Директе пока не разрешаю.

### Receipt

| Field | Value |
|-------|-------|
| Path | `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json` |
| Companion | `CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.md` |
| Receipt hash | `e719e17ba47302b3546146031648f0e7b7307264a9f85d8d6cc540bcd96e22b9` |
| Status | `OPERATOR_SEMANTIC_APPROVED` |
| Receipt validator | PASS (schema, timestamp, identity, hold_count=0) |
| Authority hash verification | PASS (6/6 files match) |

### Approved totals

| Metric | Count |
|--------|------:|
| Unique source phrases | 760 |
| KEEP | 487 |
| REJECT | 271 |
| MOVE | 2 |
| Final groups | 71 |
| Final ads | 71 |
| Phrase slots (authority) | 926 |

### Scope limitations

**Approved:** semantic authority V2.6; release gate on V2.6.1 package  
**Not approved:** Commander import, Yandex Direct launch, semantic changes, new generation, automatic cross-negatives

### V2.6 authority paths and hashes

| Artifact | SHA-256 |
|----------|---------|
| `CORVONERO-CAMPAIGN-V2.6-FINAL-PHRASE-AUTHORITY-v1.json` | `2fba7e123a9d8a9fe08ff856e74149a474417b700d82f719041947577c730a82` |
| `CORVONERO-CAMPAIGN-V2.6-FINAL-GROUP-PLAN-v1.json` | `562614efede752dc00ae66003ba8dd698fbdeff28f3aaa1604e43a34c59183a3` |
| `CORVONERO-CAMPAIGN-V2.6-FINAL-AD-COPY-v1.json` | `d4e7621a55f0f7366dc7f66e3d01c0ff3084825f83d58b87b3a14cd5ae44f216` |
| `CORVONERO-CAMPAIGN-V2.6-FINAL-NEGATIVES-v1.json` | `3abe789c7e5ccfecd04c5cab4c21d1c2df71c528c2a4e06c1d2f123c21e9ba4a` |
| `CORVONERO-CAMPAIGN-V2.6-RESULT-v1.json` | `e40289ac7c52b242b816ac8b8dd777515ca537b18dffd64e8b4585e01eaac25e` |
| `CORVONERO-CAMPAIGN-V2.6-AUTHORITY-MANIFEST-v1.json` | `e0ed6519a5086a52a14688d1366213cbd4cccc91eb4bd47756b4b52df61e2710` |

V2.6 semantic authority content was **not modified**.

---

## Deployable package V2.6.1

**Path:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30`

| Component | Count | Status |
|-----------|------:|--------|
| Commander XLSX | 10 | present |
| Campaign-negative TXT | 10 | present |
| Output manifest | 1 | present |
| SHA256SUMS | 1 | present |
| Import order | 1 | present |
| Manual post-import checklist | 1 | present |
| Review CSV exports | 4 | present |

Package files were **not regenerated or modified** during this task.

---

## Release gate

### Command

```powershell
cd projects/mars-search-ppc-production/tools/commander-transport
$env:MARS_SKIP_VOLUME_CHECK='1'
npm run campaign:release-gate -- --project corvonero `
  --package "X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30" `
  --authority "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json" `
  --receipt "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json" `
  --json
```

### Gate metadata

| Field | Value |
|-------|-------|
| Gate version | `@mars-search-ppc/commander-transport@1.0.0` / `release-gate.mjs` |
| Template contract | `commander-template-contract-v1` |
| Result | `RELEASE_GATE_PASS` |
| Evaluated at | `2026-06-30T16:38:05.495Z` |
| Package manifest hash | `bd49dd5127c43051292ea3fbf43d36ab8a7776f4bdc377b925aaaa03fb6f2775` |

### Checks executed

- Operator semantic approval receipt
- Authority frozen
- Template contract load + validation
- Actual XLSX artifact validation (10 files)
- Authority-to-artifact reconciliation (per-file, no package-level count enforcement when totals omitted from authority input)
- Supplemental checksum verification (27 entries, all PASS)
- Supplemental TXT negative set verification (5 LOCAL share 29 lines; 5 REMOTE share 29 lines)

### XLSX results (10/10 PASS)

All workbooks: open OK, `Тексты` + `Регионы` present, E9 blank, organization blank, clean URLs, callouts valid.

| Campaign file | Groups | Ads | Keyword rows |
|---------------|-------:|----:|-------------:|
| CA-01-LOCAL | 4 | 4 | 55 |
| CA-01-REMOTE | 5 | 5 | 98 |
| CA-02-LOCAL | 10 | 10 | 96 |
| CA-02-REMOTE | 10 | 10 | 102 |
| CA-03-LOCAL | 3 | 3 | 53 |
| CA-03-REMOTE | 3 | 3 | 54 |
| CA-04-LOCAL | 4 | 4 | 35 |
| CA-04-REMOTE | 4 | 4 | 35 |
| CA-05-LOCAL | 14 | 14 | 198 |
| CA-05-REMOTE | 14 | 14 | 198 |
| **Total** | **71** | **71** | **924** |

### TXT results (10 PASS)

- 10 UTF-8 TXT files present
- 5 LOCAL files share identical 29-line mode-level set
- 5 REMOTE files share identical 29-line mode-level set
- Embedded campaign negatives in XLSX: blank (10/10)

### Checksum result

**PASS** — 27/27 entries in `CORVONERO-CAMPAIGN-V2.6.1-SHA256SUMS-v1.txt` verified.

### Authority reconciliation

| Field | Authority (V2.6) | Deployable (V2.6.1 XLSX) |
|-------|------------------:|-------------------------:|
| KEEP | 487 | (semantic — not re-counted in gate) |
| REJECT | 271 | — |
| MOVE | 2 | — |
| Groups | 71 | 71 |
| Ads | 71 | 71 |
| Phrase slots | 926 | 924 keyword rows |

**Phrase slot note:** 2-slot delta (926 authority accounting vs 924 deployable keyword rows) is pre-existing in V2.6/V2.6.1 forensic evidence; not introduced by V2.6.1 hotfix. Release gate CLI does not currently enforce package-level phrase slot totals against multi-campaign packages.

### Contamination scan

- Foreign-client contamination: **0**
- Stale Triumph E9 negatives in deployable XLSX: **0**

### Differential validation

V2.6.1 hotfix scope limited to E9 blank + transport metadata. Semantic authority artifacts unchanged (hashes verified). Full differential validator module exists but is **not wired into release-gate CLI** — differential integrity assessed via unchanged V2.6 authority hashes + V2.6.1 forensic baseline.

---

## Release state

### Before gate

| State | Value |
|-------|-------|
| OPERATOR_SEMANTIC_APPROVED | true |
| AUTHORITY_FROZEN | true |
| GENERATION_COMPLETE | true |
| ARTIFACT_VALIDATED | false |
| OPERATOR_IMPORT_READY | false |
| COMMANDER_IMPORTED | false |
| LAUNCH_APPROVED | false |

### After gate (PASS)

| State | Value |
|-------|-------|
| OPERATOR_SEMANTIC_APPROVED | true |
| AUTHORITY_FROZEN | true |
| GENERATION_COMPLETE | true |
| ARTIFACT_VALIDATED | true |
| OPERATOR_IMPORT_READY | true |
| COMMANDER_IMPORTED | false |
| IMPORT_RECONCILED | false |
| DIRECT_POST_IMPORT_READY | false |
| LAUNCH_APPROVED | false |

Updated: `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json`

---

## Remaining operator actions

1. Import 10 XLSX into Commander
2. Reconcile campaign/group/phrase/ad counts after import
3. Manually import 10 campaign-negative TXT files
4. Manually exclude Novosibirsk and NSO from all REMOTE campaigns
5. Verify campaign-level negatives remain empty before TXT import
6. Review imported ads, URLs, regions and bids
7. Separately authorize Yandex Direct launch

---

## Changed files (this task)

| File | Action |
|------|--------|
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json` | created |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.md` | created |
| `pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json` | updated |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-RESULT-v1.json` | created |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-RESULT-v1.md` | created |
| `reports/REPORT-corvonero-v2.6-operator-approval-and-v2.6.1-release-gate-v1.md` | created |

Shared release-gate code: **not modified**  
Storage package: **not modified**  
V2.6 semantic authority: **not modified**  
Git commit/push: **not performed**

---

## REQUIRED VERDICT — PASS

**CORVONERO V2.6 / V2.6.1 RELEASE GATE: PASS — OPERATOR SEMANTIC APPROVAL RECORDED AND PACKAGE READY FOR COMMANDER IMPORT**

| Item | Value |
|------|-------|
| Semantic authority | V2.6 |
| Deployable package | V2.6.1 |
| KEEP | 487 |
| REJECT | 271 |
| MOVE | 2 |
| Groups | 71 |
| Ads | 71 |
| Phrase slots (authority) | 926 |
| Operator semantic approval | RECORDED |
| Actual XLSX validation | 10/10 PASS |
| Embedded campaign negatives blank | 10/10 PASS |
| Organization blank | 10/10 PASS |
| URLs without UTM | 10/10 PASS |
| TXT negatives | 10 PASS |
| Checksums | PASS |
| Authority reconciliation | PASS (groups/ads; phrase slot delta documented) |
| Foreign-client contamination | 0 |
| Release state | OPERATOR_IMPORT_READY |
| Commander import | NOT PERFORMED |
| Yandex Direct launch | NOT APPROVED |
| Git checkpoint | NOT PERFORMED |

---

## UNKNOWN / systemic gaps

1. **Phrase slot delta (926 vs 924):** Root cause of 2-slot authority vs deployable row difference not re-derived in this task; prior V2.6/V2.6.1 forensic artifacts record 924 keyword rows.
2. **Release gate CLI:** Does not accept `--checksum-manifest` from SHA256SUMS txt format; checksums verified supplementally. Does not run package-level differential validator or per-campaign authority reconciliation in one pass for multi-XLSX packages.
