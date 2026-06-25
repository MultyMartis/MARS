# Keyword Production Registry — Корво Неро v1

**Source SoT:** `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json`  
**Total MIG phrases:** 2 384 (20 seeds + 2 364 discovered)  
**Stage:** 2A boundary — full phrase assignment in Stage 2B

---

## Phrase classification pipeline

| Class | Action | Est. count |
|-------|--------|------------|
| **Commercial service** | Assign to ad group | ~1 400–1 600 |
| **Task-specific commercial** | Assign to matching task group | ~300 |
| **Configuration-specific** | Assign with config mention in ad | ~150 |
| **Problem/troubleshooting commercial** | C07 groups | ~50 |
| **Integration commercial** | C05 groups | ~80 |
| **Marking commercial** | C06 groups | ~400 |
| **Product marking commercial** | C06 product groups | ~50 |
| **Informational** | **Reject** — no ad group | ~200 |
| **Regulatory non-service** | Reject or Tier 4 only | ~150 |
| **Employment** | **Reject** + global negative | ~100 |
| **Educational** | **Reject** | ~80 |
| **Download/software** | **Reject** | ~40 |

*Counts approximate — exact assignment in Stage 2B script.*

---

## Seed phrases (operator matrix — all assigned)

| Seed | keyword_id | Assigned group |
|------|------------|----------------|
| программист 1С | kw-corv01-001 | CORV-G01-01 |
| программист 1С Новосибирск | kw-corv01-002 | CORV-G01-02 |
| сопровождение 1С | kw-corv01-003 | CORV-G01-05 |
| доработка 1С | kw-corv01-004 | CORV-G02-01 |
| интеграция 1С с сайтом | kw-corv01-005 | CORV-G05-01 |
| интеграция 1С Битрикс | kw-corv01-006 | CORV-G05-02 |
| маркировка в 1С | kw-corv01-007 | CORV-G06-01 |
| Честный знак 1С | kw-corv01-008 | CORV-G06-03 |
| доработка отчёта 1С | kw-corv01-009 | CORV-G03-01 |
| доработка печатной формы 1С | kw-corv01-010 | CORV-G03-04 |
| доработка РМК 1С | kw-corv01-011 | CORV-G03-06 |
| настройка синхронизации 1С | kw-corv01-012 | CORV-G05-04 |
| обновление доработанной 1С | kw-corv01-013 | CORV-G02-04 |
| срочно программист 1С | kw-corv01-014 | **REJECT** (no-result) — route urgent to G07-01 |
| 1С не работает | kw-corv01-015 | CORV-G07-01 |
| маркировка пива 1С | kw-corv01-016 | CORV-G06-05 |
| маркировка воды 1С | kw-corv01-017 | CORV-G06-06 |
| маркировка лекарств 1С | kw-corv01-018 | CORV-G06-08 |
| ТС ПИОТ 1С | kw-corv01-019 | CORV-G08-01 |
| маркировка автозапчастей 1С | kw-corv01-020 | CORV-G06-10 |

---

## Ownership rules

1. **One phrase → one group** — no duplicate ownership.  
2. Closest intent wins; tie-break by campaign isolation rules.  
3. If phrase fits two groups — lower-priority group gets cross-negative, not duplicate keyword.  
4. Phrase rejection logged in `production/keyword-reject-log-v1.json` (Stage 2B).

---

## Match strategy

| Default | «Фраза (с минус-словами)» with inline group negatives |
| Primary seeds | Exact/phrase encoding per Commander template practice |
| Broad | **Avoid** on head programmer — noise risk |

---

## Per-group keyword target

| Tier | Phrases per group |
|------|-------------------|
| T1 | 15–25 |
| T2 | 10–20 |
| T3 | 8–15 |
| T4 | 5–10 |

**Total planned at production:** ~600–900 active phrases (subset of 2384 — remainder rejected).

---

## Evidence reference

Each assigned phrase retains:
- `keyword_id` from MIG registry  
- `query_id` / Wordstat ref where present  
- `evidence_grade` preserved in export metadata (not Commander column)

---

## Stage 2B deliverable

`production/keyword-production-registry-v1.json` — full phrase-to-group mapping with reject log.
