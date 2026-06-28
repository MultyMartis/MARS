# CORVONERO NEW CONTROLLED SEMANTIC RUN — PREFLIGHT v1

**Date:** 2026-06-26  
**Repository:** `C:\MARS Phenix\AI MARS`  
**Branch:** `mars/canonical-post-recovery` @ `ebc65acd`  
**Verdict:** `READY_FOR_OPERATOR_CHARTER_APPROVAL`

---

## 1. Scope

Read-only preflight and operator charter preparation. **No semantic run started.** No model calls on project corpus. No runtime locks/checkpoints. No ORCA/MIG code changes. No Wordstat/SERP collection.

## 2. Git preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD | `ebc65acd4087fa9d180bb2a50921027fde51e3b7` ✓ exact match |
| Recovery branch | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` ✓ |
| Corvonero dirty paths | **None** (unrelated untracked WIP only) |

## 3. Canonical project locus

| Role | Path |
|------|------|
| **New preflight/charter docs** | `projects/mars-search-ppc-production/pilots/corvonero/` *(created this task)* |
| Operational state / freeze | `projects/orca/projects/corvonero-direct-v2-clean-room/` |
| MIG session | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| ATLAS | `projects/atlas/population/` |
| Search PPC lifecycle | `projects/mars-search-ppc-production/` |

Preferred locus `pilots/corvonero/` did not exist; created as authoritative documentation home per task spec.

## 4. ATLAS authority

| Entity | Present | State | Authority file |
|--------|---------|-------|----------------|
| ORG-0009 | Yes | Registered | `projects/atlas/population/ATLAS-CORVONERO-*` |
| LE-0006 | Yes | Registered | same |
| PRJ-0013 | Yes | Registered | same |
| WEB-CORV-01 | Yes | Owner **SAFE UNKNOWN** | `ATLAS-CORVONERO-WEBSITE-REGISTER-v1.md` |
| DOM-CORV-01 | Yes | Secondary domain correction applied | `ATLAS-CORVONERO-DOMAIN-REGISTER-v1.md` |
| REL-0042 | Yes | Active commercial rel | `ATLAS-CORVONERO-RELATIONSHIP-*` |
| Incorrect OWNS | Removed | Deprecated per Variant B | `CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md` |

## 5. Business authority

Source: `corvonero-direct-v2-business-intake-v1.json`

| Field | Classification |
|-------|----------------|
| Service scope (34 services) | CONFIRMED |
| Geography (NSO primary) | OPERATOR_APPROVED |
| Customer type (ЮЛ/ИП) | CONFIRMED |
| Remote/on-site model | CONFIRMED |
| Contract/cashless | CONFIRMED |
| Conversion goals | SAFE_UNKNOWN |
| NDS | SAFE_UNKNOWN |
| Operating hours | SAFE_UNKNOWN |
| Budget (100k RUB/mo) | CONFIRMED |
| Acceptable lead cost | SAFE_UNKNOWN |
| Landing pages (Tilda) | CONFIRMED |
| Measurement (Metrika) | CONFIRMED |
| Service priority | DECISION_REQUIRED — operator: «Без приоритета» |

**No new Business Intake required** for semantic admission.

## 6. Raw Wordstat

`RAW_WORDSTAT_AUTHORITY = VERIFIED`

- Path: `C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\`
- Count: **18 XLSX**
- SHA-256 prefixes match `keyword_registry.json` source_hash entries
- 2 no-result seeds documented: ws-p2-003, ws-p2-006

## 7. Dataset authority

| Dataset | Count | Path | SHA-256 prefix |
|---------|------:|------|----------------|
| Normalized | 2399 | `incoming/.../wordstat-pass-a-normalized.json` | `fbeb1b65d4a90cb0` |
| Canonical semantic | 2368 | `.../corvonero-canonical-phrase-registry-v1.json` | `eaa09b8450f82738` |

## 8. 2399→2368 lineage

**PROVEN** via clean-room pipeline report §9–10:

- 2399 raw ledger rows
- 31 duplicate clusters (deterministic dedup key)
- 2368 canonical entities with stable `CR2-PHR-*` / `CR2-LED-*` IDs
- Tool: `normalize-mig-corpus.mjs` — reproducible, not silently rebuilt

## 9. MIG handoff

**MIG session: COMPLETE**  
**MIG handoff: READY FOR ORCA REVIEW**

Key artefacts verified present: session manifest, normalized corpus, demand surface, keyword registry, Research Pack, SERP indexes, `orca-evidence-handoff-v1.json`.

## 10. SERP authority

**Classification:** `SERP_PARTIAL_BUT_NON_BLOCKING`

| Query | Grade (zpm latest) | Needed for semantic run |
|-------|-------------------|------------------------:|
| r1q01–r1q05 | B | Supporting evidence |
| r1q06, r1q07 | C (CAPTCHA) | Non-blocking — accepted limitation |
| r1q08, r1q10 | B (completed in throttled resume) | Supporting evidence |
| r1q09 | C / not captured | Non-blocking — TS PIOT defer |

7 Grade B supersedes historical 5-item summary. q08/q10 **completed**; q09 **not** completed.

## 11. ORCA Wave 3.1F

**ORCA_WAVE_3_1F_AUTHORITY_VERIFIED**

Wave 3.1F files present with Wave 3.1F headers; `run-wave31f-bypass-audit.mjs` exists. Wave 3.1F > 3.1E. No unresolved merge blocker observed.

## 12. Deep research

**DEEP_RESEARCH_AUTHORITY_VERIFIED**

Path verified; SHA-256 prefix `984192DA` matches recorded authority.

## 13. Old run boundary

**OLD_CORVONERO_RUN_NON_RESUMABLE** — see `CORVONERO-OLD-RUN-NON-RESUMABLE-v1.md`

## 14. Project lifecycle

| State | Value |
|-------|-------|
| Corvonero | **FROZEN** |
| Resume readiness | **READY_AFTER_OPERATOR_CHARTER** |
| Wave 5 | **BLOCKED** |
| SPPC-05 (old) | **FAILED** |

## 15–24. Design summaries

Detailed in Operator Charter v1: run identity, model policy, SPPC-05, canary, batch/checkpoint, gates, outputs, Git/STORAGE boundaries, stop conditions, test plan.

## 25. Preliminary verdict

**`READY_FOR_OPERATOR_CHARTER_APPROVAL`**

---

Companion JSON: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PREFLIGHT-v1.json`
