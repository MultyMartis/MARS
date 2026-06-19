# WF-R01 — Registry Expansion Program Charter v1

**Program ID:** WF-R01 — FOUNDRY Registry Expansion Program  
**Status:** **CHARTERED** — human sign-off on scope and exit criteria; execution **not started**  
**Date:** 2026-06-19  
**Charter Pass:** [wf-r01-charter-pass-implementation-v1.md](wf-r01-charter-pass-implementation-v1.md)

**Honesty boundary:** WF-R01 — **documentation and reference-implementation program** (human-operated charters, registry hygiene, controlled partial expansion). **Not** runtime, **not** orchestration, **not** agent automation, **not** machine-enforced validation.

**Terminology:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## 1. Program authority

| Field | Value |
|-------|-------|
| **Authority status** | **CHARTERED** |
| **Prior status** | PROPOSAL — [wf-r01-program-authority-pass-v1.md](wf-r01-program-authority-pass-v1.md) |
| **Scope SoT** | [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) |
| **Charter Pass design** | [wf-r01-charter-pass-design-v1.md](wf-r01-charter-pass-design-v1.md) |
| **Roadmap registration** | [roadmap.md](../projects/mars-website-factory/roadmap.md) § Factory architecture items |
| **Operator entry** | [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) Core Run |

**CHARTERED means:** scope and exit criteria **accepted**; program **registered** in roadmap and OPERATIONAL-INDEX. **Does not** mean ACTIVE (subprogram execution) and **does not** authorize WF-R01.2 or registry content changes.

---

## 2. Scope affirmation

Full program scope, exclusions, subprograms (WF-R01.1–R01.8 + R01.X), success metrics, and boundary conditions are defined in [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md). This charter **affirms** that design as program scope SoT until superseded by explicit program charter v2 with human sign-off.

**Program goal:** Close the **Registry Implementation Cliff** — one canonical namespace, structural blocks for catalog surfaces, reference implementation expansion, minimal pattern/SEO slices, honest Template-Art multi-site-type policy.

---

## 3. Exit criteria affirmation

Program **COMPLETE** requires exit criteria E1–E9 per program design § Success Metrics (WF-R01.1 ACCEPTED through program completion REPORT). **Not** required for CHARTERED: WF-A03 start; 100% reference coverage; ECOMMERCE legal E1–E4; machine validation automation.

---

## 4. Authority chain

```
WF-A01  Production Modes Contract          ✅ Complete
WF-A02  Validation Architecture             ✅ Complete (+ VL3 Pass 02)
   ↓
WF-R01  Registry Expansion Program         ◆ CHARTERED (this charter)
   ↓
WF-A03  Pixel Factory Expansion             ⏸ DEFERRED
```

WF-R01 **links** upstream charters; **does not amend** WF-A01, WF-A02, or VL3 scope.

---

## 5. Subprogram entry gate

**WF-R01.1 binding charter:** **ACCEPTED** — [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) (T0 = 2026-06-19; design: [wf-r01-1-v0-v1-binding-charter-design-v1.md](wf-r01-1-v0-v1-binding-charter-design-v1.md); implementation pass: [wf-r01-1-accepted-charter-implementation-v1.md](wf-r01-1-accepted-charter-implementation-v1.md)). **B1 satisfied.** B3–B8 — implementation phase P2–P5.

**Next execution step:** WF-R01.1 charter pass P2–P5 (banner, STOP rule, onboarding, T_cutover, pilot audit).

**WF-R01.2 and all registry content expansion remain forbidden** until authorization gates B1 + B3 minimum per [wf-r01-charter-pass-design-v1.md](wf-r01-charter-pass-design-v1.md) § WF-R01.2 Authorization Conditions.

---

## 6. Explicit non-goals at CHARTERED

- No new `block_id` entries
- No reference partial expansion in `website-factory-reference-v1/src/`
- No new site types
- No WF-A03 auto-start
- No governance wave expansion

---

*Charter artifact: `reports/wf-r01-registry-expansion-program-charter-v1.md`*
