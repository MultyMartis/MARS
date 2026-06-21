# ATLAS ZPM Website Model Correction v1

**Status:** **documented** — binding correction package (population layer); **not executed**.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Trigger:** [ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md](ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md) — AUD-ZPM-WEB-01..05  
**Operator authority:** Website = real web property; delivery generations → Project layer only.  
**Parent:** [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md)  
**Is not:** attestation execution, register write, entity deletion runtime, Foundation amendment.

---

## 1. Prior incorrect conclusion

| Source | Claim | Verdict recorded |
|--------|-------|------------------|
| [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) §6 | Same hostname `bzpm.ru` · different delivery generations → **two** Website entities; **do not merge** | ZPM-WEB-POL-01 **Pass** |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) §4 | Dual-generation pairing: WEB-ZPM-01 + WEB-ZPM-02 | **documented** |
| [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) §15 | READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — both websites | **Pass** both |
| Population §10.1 | REL-ZPM-WB-02 WEB-ZPM-02 → PRJ-0010; cross-link WEB-ZPM-01 → PRJ-0010 **Rejected** | Generation mismatch rule |

**Error class:** Class boundary pollution — **delivery generation treated as Website identity** when Project layer (PRJ-0010) already holds the same historical fact.

**Contrast — correct layer (unchanged):**

| Layer | Historical delivery | Current delivery |
|-------|--------------------|------------------|
| **Project** | PRJ-0010 **deprecated** | PRJ-0009 **active** |
| **Website** *(incorrect prior)* | WEB-ZPM-02 **deprecated** | WEB-ZPM-01 **active** |
| **Website** *(corrected)* | *(none — history via Project)* | WEB-ZPM-01 **active** only |

---

## 2. Binding corrections (enforced when executed)

| ID | Correction | Applies to |
|----|------------|------------|
| **COR-ZPM-WEB-01** | **Retire** WEB-ZPM-02 — do **not** attest; do **not** promote to **deprecated** or **active**; mark population intent **rejected** / **not minted** | WEB-ZPM-02 |
| **COR-ZPM-WEB-02** | **Revoke** ZPM-WEB-POL-01 (one Website per delivery generation) | Wave 4 ZPM population + register + attestation packages |
| **COR-ZPM-WEB-03** | **Adopt** Triumph single-property model: one **active** Website per `bzpm.ru` hostname | WEB-ZPM-01 |
| **COR-ZPM-WEB-04** | **Re-route** EV-ZPM-OP-HIST-01 — evidence supports PRJ-0010 only; not a Website mint basis | Evidence index |
| **COR-ZPM-WEB-05** | **Cancel** attestation tranche AT-W4-ZPM-02 (WEB-ZPM-02) | Attestation sequence |
| **COR-ZPM-WEB-06** | **Cancel** REL-ZPM-WB-02 (WEB-ZPM-02 → PRJ-0010) | Wave 4B-ZPM queue |
| **COR-ZPM-WEB-07** | **Add** REL-ZPM-WB-03 draft: WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** (historical grouping — analog REL-0027) | Wave 4B-ZPM queue |
| **COR-ZPM-WEB-08** | **Retain** REL-ZPM-WB-01: WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** | Wave 4B-ZPM queue |
| **COR-ZPM-WEB-09** | **Simplify** OWNS: ORG-0005 → WEB-ZPM-01 only; remove WEB-ZPM-02 OWNS candidate | Wave 4B-ZPM |
| **COR-ZPM-WEB-10** | **Resolve** SU-W4-ZPM-03: single DOM-* `bzpm.ru` → WEB-ZPM-01 **PRIMARY_DOMAIN** at Wave 5B | Wave 5 / 5B ZPM |
| **COR-ZPM-WEB-11** | **Downgrade** ZPM-WEB-D-01 verdict from «Not duplicate — two Website records» → **Fail** (reopened) | Duplicate review |
| **COR-ZPM-WEB-12** | **Clarify** local «EFV-03 two-phase» label — valid for **Project** layer only; **not** a Website cardinality rule | Documentation hygiene |

---

## 3. Target state (post-correction)

### 3.1 Entity roster

| Entity | canonical_name | lifecycle | Action |
|--------|----------------|-----------|--------|
| **WEB-ZPM-01** | bzpm.ru | **active** *(on attestation)* | **Keep** — attest via AT-W4-ZPM-01 only |
| **WEB-ZPM-02** | bzpm.ru (исходная версия) | — | **Retire** — never attest |
| **PRJ-0009** | Каталог-платформа bzpm.ru | **active** | **Unchanged** |
| **PRJ-0010** | Сайт bzpm.ru (исходная версия) | **deprecated** | **Unchanged** |
| **ORG-0005** | ЗПМ | **active** | **Unchanged** |

### 3.2 Target relationship graph (Wave 4B-ZPM+)

```text
ORG-0005 ЗПМ ──OWNS──► WEB-ZPM-01 bzpm.ru (active)
WEB-ZPM-01 ──BELONGS_TO──► PRJ-0009 Каталог-платформа bzpm.ru (active)
WEB-ZPM-01 ──BELONGS_TO──► PRJ-0010 Сайт bzpm.ru исходная версия (deprecated)

Wave 5B:
DOM-* bzpm.ru ──PRIMARY_DOMAIN──► WEB-ZPM-01
```

### 3.3 Retired artifacts (do not create)

| Artifact | Reason |
|----------|--------|
| WEB-ZPM-02 | Historical delivery — PRJ-0010 sufficient |
| AT-W4-ZPM-02 | No Website to attest |
| REL-ZPM-WB-02 | Source Website retired |
| ORG-0005 OWNS WEB-ZPM-02 | Target entity retired |
| Dual DOM / dual PRIMARY_DOMAIN for generations | Single hostname property |

---

## 4. Required documentation updates (execution queue)

**Not performed in this package.** Steward or population pass should update:

| # | Document | Change |
|---|----------|--------|
| 1 | [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Remove §6 dual-generation Website policy; single Website roster; update §10 relationships |
| 2 | [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Remove WEB-ZPM-02 row; update summary counts; revise §4 pairing index |
| 3 | [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) | Remove AT-W4-ZPM-02; revise verdict to single-Website attestation; update 4B queue |
| 4 | Future Wave 4B-ZPM population package | REL-ZPM-WB-01 + REL-ZPM-WB-03; no REL-ZPM-WB-02 |
| 5 | Future Wave 5 / 5B ZPM packages | DOM-* → WEB-ZPM-01 only |
| 6 | [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) | On next refresh — ZPM Website count = 1 |

**Documents that require no entity-level change:**

- [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md)
- [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md)
- [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md)
- Wave 1B / 2 / 2B ZPM packages

---

## 5. Attestation gate changes

| Gate | Prior | Corrected |
|------|-------|-----------|
| W4-ZPM-EG-03 | PRJ-0010 **deprecated** before WEB-ZPM-02 **deprecated** | **Obviated** — no WEB-ZPM-02 |
| W4-ZPM-EG-07 | EFV-03 — no merge two Websites | **Replaced** — COR-ZPM-WEB-12: only one Website minted |
| W4-ZPM-LC-05 | PRJ-0010 + WEB-ZPM-02 deprecated pair | **Replaced** — W3-LC-05: PRJ-0010 deprecated + WEB-ZPM-01 **active** |
| AT-W4-ZPM-01 | Proceed | **Proceed** — unchanged |
| AT-W4-ZPM-02 | Proceed | **Blocked** — COR-ZPM-WEB-05 |

**Revised attestation verdict (target):**

```text
READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)
```

---

## 6. Evidence re-index

| Ref | Prior routing | Corrected routing |
|-----|---------------|-------------------|
| EV-ZPM-OP-ACT-01 | WEB-ZPM-01 · PRJ-0009 | **Unchanged** |
| EV-ZPM-OP-HIST-01 | WEB-ZPM-02 · PRJ-0010 | **PRJ-0010 only**; supports BELONGS_TO context for WEB-ZPM-01 |
| EV-W1B-CC-01 §17 | Both websites (indirect) | **WEB-ZPM-01** org hostname corroboration |

**Platform metadata** (WP + The7 on historical generation) — remains **consumer metadata** on PRJ-0010 narrative; not a Website lifecycle field.

---

## 7. Downstream wave correction matrix

| Wave | Prior plan element | Corrected plan |
|------|-------------------|----------------|
| **Wave 4** | 2 Website mints | 1 Website mint (WEB-ZPM-01) |
| **Wave 4B** | REL-ZPM-WB-01 + REL-ZPM-WB-02; 2× OWNS | REL-ZPM-WB-01 + **REL-ZPM-WB-03**; 1× OWNS |
| **Wave 5** | 1 DOM-* (already planned); ambiguity SU-W4-ZPM-03 | 1 DOM-* `bzpm.ru` — unambiguous |
| **Wave 5B** | PRIMARY_DOMAIN target unclear if 2 Websites | DOM-* → WEB-ZPM-01 singleton |
| **Wave 6** | CLIENT_OF ORG-0005 → ORG-0001 | **Unchanged** |
| **Backup** | Not yet counting WEB-ZPM-* | Count 1 Website when refreshed |
| **Integrity audit** | Pre–Wave 4 ZPM baseline | Add COR-ZPM-WEB-* to finding register on sync pass |

---

## 8. What remains valid

| Item | Status |
|------|--------|
| PRJ-0009 + PRJ-0010 two-Project model on `bzpm.ru` | **Valid** — correct layer |
| ORG-0005 **active** · canonical **ЗПМ** | **Valid** |
| REL-ZPM-PJ-01..04 commissioning / execution edges | **Valid** |
| WEB-ZPM-01 as sole `bzpm.ru` web property | **Valid** |
| Triumph analog (WEB-0006 multi-Project BELONGS_TO) | **Valid** precedent |
| Namespace WEB-ZPM-* distinct from WEB-0006..0009 | **Valid** |

---

## 9. Execution constraints

| Constraint | Value |
|------------|-------|
| Execute corrections in this session? | **No** — audit directive |
| Modify entities / registers now? | **No** |
| Foundation amendment required? | **No** |
| Block Wave 4 attestation until docs updated? | **Recommended** — prevent AT-W4-ZPM-02 |
| WEB-ZPM-02 id reuse? | **Forbidden** per IDP-03 — id retired unused if ever assigned |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md](ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md) | Audit findings source |
| [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) | Operator decision record |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Reference correction pattern |

---

*ATLAS ZPM Website Model Correction v1 — documented correction package only; not executed.*
