# Final Evidence Audit — Корво Неро MIG Session

**Session:** `mig-20260622-corv01`  
**Project:** PRJ-0013  
**Audit date:** 2026-06-22  
**Auditor:** Cursor agent (operator-delegated final sync)

---

## Scope

Audit of all Corvonero MIG evidence layers before Research Pack publication and ORCA handoff.

---

## Layer checklist

| # | Layer | Status | Grade | Notes |
|---|-------|--------|-------|-------|
| 1 | Business Intake | **OK** | B | `workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md` |
| 2 | ATLAS bindings | **OK** | — | ORG-0009, LE-0006, PRJ-0013, WEB-CORV-01, DOM-CORV-01 in manifest |
| 3 | Research Request | **OK** | — | `CORVONERO-MIG-RESEARCH-REQUEST-v1.md` approved for execution |
| 4 | Stage 1 SERP | **OK** | C | 9 queries; af-004 historical; preserved |
| 5 | Stage 2 SERP | **OK** | C | 27 live queries; synthesis grade C |
| 6 | Wordstat Pass A | **OK** | B_semantic | 18 Excel + 2 no-result; 2399 rows; MARS Storage provenance |
| 7 | R1 Grade B SERP | **PARTIAL OK** | B_partial | 7/10 zpm-workflow; PNG+HTML+JSON present for Grade B |
| 8 | Competitor shortlist | **OK** | B | 9 objects; 7 confirmed + 2 pattern refs |
| 9 | Website Intelligence | **OK** | B | 7 shortlist domains fetched (Shift timeout noted) |
| 10 | Landing Intelligence v2 | **OK** | B | 5 landing cards + Corvonero current page |
| 11 | Corvonero site intelligence | **OK** | B | `website-corvonero-intelligence.json` |
| 12 | Demand Surface | **OK** | finalized | 13 cluster verdicts; layers separated |
| 13 | Keyword Registry | **OK** | draft→reviewed | rev 2; R1 layer propagated to seed entries |
| 14 | Source registry | **OK** | — | af-004..af-009 lifecycle updated |
| 15 | Evidence review | **OK** | — | `evidence/review.md` superseded by Human Review Gate |
| 16 | Session manifest | **OK** | — | Status aligned post-audit |

---

## Issues found (pre-fix)

| ID | Severity | Issue | Resolution |
|----|----------|-------|------------|
| AUD-01 | **Fixed** | Keyword Registry R1 evidence only at `updated_at` | `finalize-mig-research-pack-corv01.mjs` propagated `r1_regional_serp` to seed entries |
| AUD-02 | **Fixed** | Demand Surface clusters still stated `wordstat_not_collected` | Pass A complete; verdicts added; status finalized |
| AUD-03 | **Fixed** | Manifest `keyword_pass: false` contradicted operator Pass A approval | Set `keyword_pass: true` with Pass B not required note |
| AUD-04 | **Accepted** | R1 7/10 coverage | Operator decision — explicit limitation preserved |
| AUD-05 | **Accepted** | r1q06, r1q07 CAPTCHA Grade C | af-009 accepted limitation |
| AUD-06 | **Accepted** | r1q09 not captured | Operator accepted — defer verdict on TS PIOT |
| AUD-07 | **Accepted** | Shift Company website timeout | SERP-only evidence; SAFE UNKNOWN |
| AUD-08 | **Info** | kw-corv01-001 geography still mentions Pass B pending | Pass B superseded at registry root; seed geo string legacy — non-blocking |

---

## Reference resolution

| Reference class | Result |
|-----------------|--------|
| Session manifest → artifacts | **All resolve** |
| serp_r1_index → zpm captures | **7 Grade B + 2 CAPTCHA + 1 no capture** |
| Wordstat file index → MARS Storage | **18 files hashed** |
| No-result seeds | **ws-p2-003, ws-p2-006 — `not_available` not zero** |
| Superseded routes | **af-004, af-008 preserved traceable** |

---

## Layer separation verified

| Layer | Geography | Must not merge with |
|-------|-----------|-------------------|
| Wordstat Pass A | All Russia broad | Novosibirsk SERP volumes |
| Stage 1/2 SERP | Novosibirsk (synthesis C) | Wordstat frequencies |
| R1 zpm-workflow | Novosibirsk lr=65 mobile | Pass A national counts |

---

## Blockers

**None.** Operator-approved limitations are explicit; no silent contradictions remain for Research Pack publication.

---

*Audit complete — supports Human Review Gate APPROVED state.*
