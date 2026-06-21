# ATLAS Next Expansion Decision Summary v1

**Status:** **documented** — expansion-direction decision summary (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Parent:** [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md) · [ATLAS-NEXT-EXPANSION-DECISION-REGISTER-v1.md](ATLAS-NEXT-EXPANSION-DECISION-REGISTER-v1.md)  
**Is not:** population pass, attestation act, runtime export, git commit.

---

## Final verdict

```text
RECOMMENDED NEXT PHASE ORDER:

P0 → Direction C (ZPM CLIENT_OF)
P1 → Direction A (SIBCAR Project → Website → Domain)
P2 → Direction B (Makita assets) + remaining commercial edges
P3 → Direction D (Moscow SERM, Metallka — evidence-gated)
```

**Lead act:** **ORG-0005 ЗПМ CLIENT_OF ORG-0001 Полигон** — наименьшие усилия, наивысшая готовность evidence, закрытие критического commercial gap (**14%**) на полностью аттестированном стеке.

**Second wave:** **SIBCAR structural stack** — наибольший прирост multi-class coverage с E1 CC и OCPilot consumer.

**Validation:** No entities created. No relationships created. No lifecycle changes. No graph mutations. No Foundation changes.

---

## 1. Baseline (authority)

| Class | Attested | Coverage |
|-------|----------|----------|
| Organization | 7 | 70% |
| Legal Entity | 5 | 56% |
| Person | 15 | 88% |
| Project | 8 | 80% |
| Website | 5 | 36% |
| Domain | 5 | 36% |
| Commercial rel. | 1 | **14%** |
| **Aggregate** | — | **~55%** |

---

## 2. Direction scores (compact)

| Direction | Orgs | LE | Per | Prj | Web | Dom | Rel | Effort | Evidence | Value | **Priority** |
|-----------|------|-----|-----|-----|-----|-----|-----|--------|----------|-------|--------------|
| **A** SIBCAR | 0 | 0 | 0–1 | 1 | 1 | 1 | 4–6 | Medium | **High** | **High** | **P1** |
| **B** Makita | 0 | 0 | 1 | 1 | 2 | 2 | 5–7 | Med–High | Medium | Med–High | **P2** |
| **C** Commercial | 0 | 0 | 0 | 0 | 0 | 0 | 3 | **Low** | **High** | **High** | **P0** |
| **D** New contours | 2 | 0–2 | 0 | 0 | 0 | 0 | 4–6 | **High** | Low–Med | Medium | **P3** |

---

## 3. Why this order (not coverage-audit P0 for partners)

Coverage audit ставил Moscow SERM / Metallka в P0 из‑за partner isolation. Decision audit **переранжирует** Direction D в P3:

- PER-0002 и PER-0003 **уже attested** — изоляция Person-class снята.
- Org/LE для D требуют **discovery** без web/project evidence.
- A, B, C продвигают **документированные операции** (OCPilot, i-SEO, ЗПМ catalog) с более сильными evidence trails.

---

## 4. Recommended execution sequence

| # | Priority | Action |
|---|----------|--------|
| 1 | **P0** | **C-01:** ORG-0005 CLIENT_OF ORG-0001 |
| 2 | **P1** | **A:** SIBCAR Wave 3 Project (OCPilot SITE-001) |
| 3 | **P1** | **A:** SIBCAR Wave 4 Website + Wave 5 Domain |
| 4 | **P2** | **B:** Makita Websites ×2 + Domains ×2 |
| 5 | **P2** | **B:** Makita Person + Project |
| 6 | **P2** | **C-03:** ORG-0007 CLIENT_OF ORG-0003 |
| 7 | **P2** | **C-02:** ORG-0006 CLIENT_OF ORG-0001 |
| 8 | **P3** | **D:** Moscow SERM Organization wave |
| 9 | **P3** | **D:** Metallka Organization wave |

---

## 5. Phase map

```text
Phase 1 (P0)  Commercial quick win
              └── ZPM CLIENT_OF

Phase 2 (P1)  SIBCAR structural
              └── Project → Website → Domain

Phase 3 (P2)  Makita assets + commercial closure
              └── Sites → Domains → Person → Project
              └── Makita CLIENT_OF i-SEO
              └── SIBCAR CLIENT_OF Polygon

Phase 4 (P3)  Partner contours (CC/E1 gated)
              └── Moscow SERM, Metallka
```

---

## 6. Expected coverage uplift (cumulative, est.)

| After phase | Commercial | Website/Domain | SIBCAR slice | Makita slice | ZPM commercial |
|-------------|------------|----------------|--------------|--------------|----------------|
| Phase 1 | **~29%** | 36% | 2.0/7 | 0.5/7 | **7.0/7** |
| Phase 2 | ~29% | **~43%** | **~5.0/7** | 0.5/7 | 7.0/7 |
| Phase 3 | **~43%** | **~57%** | ~5.0/7 | **~4.5/7** | 7.0/7 |
| Phase 4 | ~57%+ | ~57%+ | ~5.0/7 | ~4.5/7 | 7.0/7 |

*Estimates — documentation-level; not attested until population waves execute.*

---

## 7. Explicit deferrals

| Item | Reason |
|------|--------|
| Makita LE | E1+ CC absent |
| Operator WEB-0001..0005 | Out of A–D scope |
| ZPM Wave 5B PRIMARY_DOMAIN | Registrar E1 gate |
| D commercial edges | Org prerequisite |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md) | Full analysis |
| [ATLAS-NEXT-EXPANSION-DECISION-REGISTER-v1.md](ATLAS-NEXT-EXPANSION-DECISION-REGISTER-v1.md) | Tabular register |
| [ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md](ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md) | Prior coverage baseline |

---

*ATLAS Next Expansion Decision Summary v1 — audit only; no commit.*
