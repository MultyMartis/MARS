# ATLAS ZPM Website Model Consistency Audit v1

**Status:** **documented** — audit findings only; no entity or register modifications executed.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Scope:** WEB-ZPM-01 · WEB-ZPM-02 · PRJ-0009 · PRJ-0010 · ORG-0005  
**Trigger:** Operator decision — Website = real web property; delivery generations belong in Project layer.  
**Parent:** [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) · [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) · [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md)  
**Is not:** correction execution, attestation act, register write, Foundation amendment.

---

# REPORT — ATLAS ZPM Website Model Consistency Audit

**Audit date:** 2026-06-07  
**Auditor posture:** Documentation review against operator canonical model and attested Triumph precedent.  
**Entity state at audit:** WEB-ZPM-01/02 **proposed** (attestation act pending); PRJ-0009/0010 attested; ORG-0005 **active**.

---

## 1. Audit scope and question

**Operator canonical model (binding for this audit):**

```text
Domain
  ↓
Website        ← one real web property per hostname identity
  ↓
Projects       ← redesigns, rebuilds, platform migrations
```

**Audit question:** Does WEB-ZPM-02 (`bzpm.ru` исходная версия, **deprecated**) violate Website identity boundaries when PRJ-0010 already represents the same historical delivery?

**Operator answer (pre-declared):** One hostname may hold **1 Website entity** and **multiple historical Projects**. Preferred model.

---

## 2. Entity state reviewed

| Entity | canonical_name | lifecycle *(current)* | lifecycle *(planned)* | Role in dispute |
|--------|----------------|----------------------|----------------------|-----------------|
| **ORG-0005** | ЗПМ | **active** | — | Client org anchor |
| **PRJ-0009** | Каталог-платформа bzpm.ru | **active** | — | Current delivery initiative |
| **PRJ-0010** | Сайт bzpm.ru (исходная версия) | **deprecated** | — | Historical delivery initiative |
| **WEB-ZPM-01** | bzpm.ru | **proposed** | **active** | Current web property — **aligned** |
| **WEB-ZPM-02** | bzpm.ru (исходная версия) | **proposed** | **deprecated** | Historical delivery as Website — **conflict** |

**Evidence chain (unchanged by audit):**

| Ref | Tier | Supports |
|-----|------|----------|
| EV-ZPM-OP-ACT-01 | E0 | PRJ-0009 · WEB-ZPM-01 |
| EV-ZPM-OP-HIST-01 | E0 | PRJ-0010 · *(incorrectly also WEB-ZPM-02)* |
| EV-W1B-CC-01 §17 | E1 | ORG-0005 hostname **Bzpm.ru** — generation-agnostic |
| AT-W3-ZPM-01..02 | attestation | PRJ-0009 **active** · PRJ-0010 **deprecated** |

---

## 3. Audit findings

### 3.1 Finding summary

| ID | Severity | Finding | Blocks attestation? |
|----|----------|---------|---------------------|
| **AUD-ZPM-WEB-01** | **High** | WEB-ZPM-02 mints a second Website for the same real property `bzpm.ru` | **Yes** — block AT-W4-ZPM-02 |
| **AUD-ZPM-WEB-02** | **High** | Website layer duplicates Project layer for historical delivery (PRJ-0010) | **Yes** |
| **AUD-ZPM-WEB-03** | **Medium** | ZPM-WEB-POL-01 / dual-generation Website policy contradicts EIR-W01 and Triumph precedent | **Yes** |
| **AUD-ZPM-WEB-04** | **Medium** | Local misuse of «EFV-03» label in Wave 4 ZPM docs — extended from Project two-phase rule to Website mint | **Yes** — documentation only |
| **AUD-ZPM-WEB-05** | **Low** | Wave 5 PRIMARY_DOMAIN cardinality unresolved while two Websites share one hostname (SU-W4-ZPM-03) | **Yes** — resolved by correction |
| **AUD-ZPM-WEB-06** | **Info** | PRJ-0009/0010 and ORG-0005 are **correct** under operator model — no Project-layer conflict | **No** |

### 3.2 AUD-ZPM-WEB-01 — Website identity boundary violation

**Foundation rule** ([ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) §6.4):

> **EIR-W01** — One canonical website per **business web property identity**

**Observation:** `bzpm.ru` is a single production hostname for ORG-0005. CC §17 lists one corporate website field (**Bzpm.ru**). Operator narrative describes **replacement** of an older site generation by a catalog-platform generation on the **same** hostname — not coexistence of two distinct web properties.

**Conflict:** WEB-ZPM-02 models a **completed delivery generation** as a separate Website entity with the same URL `https://bzpm.ru`. That conflates **delivery artifact / rebuild lineage** with **web property identity**.

**Verdict:** **Fail** — WEB-ZPM-02 violates Website identity boundaries.

### 3.3 AUD-ZPM-WEB-02 — Website vs Project separation violation

**Foundation rule** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project, §4 Website):

- **Project** — structural container for related work / initiative grouping.
- **Website** — registered **web property** identity; not deploy/CMS generation alone.

**Observation:** PRJ-0010 already attests «Сайт bzpm.ru (исходная версия)» as **deprecated** `client_delivery`. Minting WEB-ZPM-02 creates a **parallel 1:1 mirror** of the same historical fact at Website class — redundant and class-blurring.

**Operator rule:** Historical redesigns and rebuilds **must** be represented by Projects; they **must not** automatically create new Website entities.

**Verdict:** **Fail** — WEB-ZPM-02 violates Website vs Project separation.

### 3.4 AUD-ZPM-WEB-03 — Triumph precedent mismatch

**Attested canonical pattern** (ORG-0004 / `gktriumph.ru`):

| Layer | Entity | Lifecycle | Hostname |
|-------|--------|-----------|----------|
| Website | WEB-0006 gktriumph.ru | **active** | `gktriumph.ru` |
| Project | PRJ-0004 Редизайн gktriumph.ru | **deprecated** | same property context |
| Project | PRJ-0006 SEO gktriumph.ru | **active** | same property context |
| Relationship | REL-0027, REL-0028 | **active** | WEB-0006 **BELONGS_TO** both projects |

**Source:** [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) §3.1.

**ZPM documented pattern** (conflicting):

| Layer | Entity | Lifecycle | Hostname |
|-------|--------|-----------|----------|
| Website | WEB-ZPM-01 bzpm.ru | **active** | `bzpm.ru` |
| Website | WEB-ZPM-02 bzpm.ru (исходная версия) | **deprecated** | `bzpm.ru` |
| Project | PRJ-0009 | **active** | `bzpm.ru` |
| Project | PRJ-0010 | **deprecated** | `bzpm.ru` |

ZPM Wave 4 documentation explicitly **extends** Triumph to «two Websites per steward policy» ([ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) §6). That extension is **not** supported by EIR-W01 and **contradicts** the operator decision under audit.

**Verdict:** **Fail** — ZPM dual-Website policy is inconsistent with attested registry precedent.

### 3.5 AUD-ZPM-WEB-04 — EFV-03 label misuse (documentation)

Normative **EFV-03** in [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) governs **Organization** equivalence — not Website cardinality.

Wave 3 ZPM correctly applied the **two-phase delivery** principle at **Project** layer (PRJ-0009 + PRJ-0010). Wave 4 ZPM documentation **relabelled** the same principle as «EFV-03» to justify **two Website records** — a scope error.

**Verdict:** **Fail** — documentation inference chain invalid at Website layer.

### 3.6 AUD-ZPM-WEB-05 — Wave 5 Domain model impact

**Foundation rules:**

- **EIR-D01** — One canonical domain id per hostname identity.
- Wave 5B — At most one canonical active **PRIMARY_DOMAIN** per Website ([ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md) §1).

**Observation:** With two Website entities on one apex hostname, Wave 5 documentation already flags **SU-W4-ZPM-03** — «Single DOM-* vs dual generation for `bzpm.ru`» as **SAFE UNKNOWN**.

**Verdict:** **Fail** — dual-Website model creates unnecessary Domain→Website ambiguity; corrected single-Website model aligns with Triumph DOM-0001 → WEB-0006 pattern.

### 3.7 AUD-ZPM-WEB-06 — Project and Organization layers pass

| Check | Result |
|-------|--------|
| ORG-0005 **active** · canonical **ЗПМ** | **Pass** |
| PRJ-0009 **active** — current catalog-platform delivery | **Pass** |
| PRJ-0010 **deprecated** — historical delivery ~5y | **Pass** |
| Two Projects on same hostname allowed (W3-ZPM-LC-04) | **Pass** |
| PRJ-0009 vs PRJ-0010 not duplicates (ZPM-PRJ-D-01) | **Pass** |
| SIBCAR / SITE-001 excluded (COR-W1B-03) | **Pass** |

**No correction required** at Project or Organization layer.

---

## 4. Model comparison

### 4.1 Documented model (pre-audit — Wave 4 ZPM packages)

```text
bzpm.ru
├── WEB-ZPM-01 (active)     ← current generation
├── WEB-ZPM-02 (deprecated) ← historical generation  ⚠ CONFLICT
├── PRJ-0009 (active)
└── PRJ-0010 (deprecated)

Policy: ZPM-WEB-POL-01 — one Website per delivery generation
```

### 4.2 Operator canonical model (approved)

```text
DOM-* bzpm.ru
  └── WEB-ZPM-01 (active)   ← single real property
        ├── BELONGS_TO → PRJ-0009 (active)    current catalog platform
        └── BELONGS_TO → PRJ-0010 (deprecated) historical original site

Policy: one Website per hostname property; generations live in Project layer
```

### 4.3 Attested Triumph reference model

```text
DOM-0001 gktriumph.ru
  └── WEB-0006 (active)
        ├── BELONGS_TO → PRJ-0004 (deprecated) redesign
        └── BELONGS_TO → PRJ-0006 (active)     SEO
```

**Alignment:** Operator canonical model = Triumph reference. Documented ZPM Wave 4 model = **misaligned**.

---

## 5. Conflict analysis

| Conflict axis | WEB-ZPM-02 posture | Operator / Foundation posture | Resolution |
|---------------|-------------------|------------------------------|------------|
| **Property identity** | Two Websites = two «properties» on one URL | One property; rebuilds are not new properties | Retire WEB-ZPM-02 |
| **Class assignment** | Delivery generation → Website | Delivery generation → Project | Keep PRJ-0010 only |
| **Lifecycle pairing** | PRJ-0010 deprecated ↔ WEB-ZPM-02 deprecated | PRJ-0010 deprecated ↔ WEB-ZPM-01 **active** (W3-LC-05 pattern) | Adopt Triumph W3-LC-05 |
| **BELONGS_TO** | One edge per generation Website | Multiple Projects → one Website | REL-ZPM-WB-01 + new REL-ZPM-WB-03 |
| **PRIMARY_DOMAIN** | Ambiguous target Website | DOM-* → WEB-ZPM-01 only | Single edge at Wave 5B |
| **Evidence routing** | EV-ZPM-OP-HIST-01 → WEB-ZPM-02 | EV-ZPM-OP-HIST-01 → PRJ-0010 (already) | Re-route; no Website mint |

**Cross-generation BELONGS_TO rejection** in current Wave 4 ZPM attestation plan (WEB-ZPM-01 → PRJ-0010 marked «generation mismatch») is itself a **symptom** of the incorrect dual-Website model. Under corrected model, WEB-ZPM-01 → PRJ-0010 is **required** (analog REL-0027).

---

## 6. Downstream impact assessment

| Wave / artifact | Current ZPM plan impact if uncorrected | Impact after correction |
|-----------------|----------------------------------------|-------------------------|
| **Wave 4 ZPM** | AT-W4-ZPM-02 would attest WEB-ZPM-02 | **Block** AT-W4-ZPM-02; execute AT-W4-ZPM-01 only |
| **Wave 4B ZPM** | REL-ZPM-WB-02 (WEB-ZPM-02 → PRJ-0010); dual OWNS | **Cancel** REL-ZPM-WB-02; add WEB-ZPM-01 → PRJ-0010 BELONGS_TO; single OWNS target |
| **Wave 5 ZPM** | SU-W4-ZPM-03 dual DOM policy | **Resolve** — one DOM-* `bzpm.ru` |
| **Wave 5B ZPM** | PRIMARY_DOMAIN cardinality conflict | **Resolve** — DOM-* → WEB-ZPM-01 singleton |
| **Backup snapshot** | WEB-ZPM-* not yet in [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) | Baseline refresh: 1 Website not 2 |
| **Integrity audit** | No WEB-ZPM rows in [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](../audit/ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) | Add post-correction consistency note |
| **Wave 3 / 3B ZPM** | PRJ-0009/0010 · REL-ZPM-PJ-01..04 | **No change** |
| **Wave 1B / 2 / 2B ZPM** | ORG-0005 · Persons · REL-ZPM-01/02 | **No change** |

**Attestation timing advantage:** WEB-ZPM-01/02 remain **proposed** — correction can be applied **before** any Website attestation act, avoiding merge/deprecation of attested entities.

---

## 7. SAFE UNKNOWN disposition

| ID | Topic | Audit disposition |
|----|-------|-------------------|
| SU-ZPM-PRJ-03 | Deployment replace vs coexistence | **Resolved structurally** — single Website; operational detail remains unknown |
| SU-W3B-ZPM-01 | Dual BELONGS_TO steward policy | **Resolved** — multi-Project BELONGS_TO on WEB-ZPM-01 (Triumph analog) |
| SU-W4-ZPM-03 | Single DOM vs dual generation | **Resolved** by correction |
| SU-W4-ZPM-02 | OWNS on deprecated WEB-ZPM-02 | **Obviated** — WEB-ZPM-02 retired |
| SU-ZPM-PRJ-01/02 | Historical contract precision | **Unchanged** — PRJ-0010 narrative sufficient |

---

## 8. Audit verdict

```text
PASS WITH CORRECTION
```

| Criterion | Result |
|-----------|--------|
| ORG-0005 · PRJ-0009 · PRJ-0010 | **Pass** — no entity conflict |
| WEB-ZPM-01 | **Pass** — aligns with operator model |
| WEB-ZPM-02 | **Fail** — violates Website identity, class separation, EIR-W01, Triumph precedent |
| Downstream waves | **Pass with correction package** — see [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md) |
| Foundation amendment required? | **No** — population-layer correction only |
| Corrections executed in this audit? | **No** — audit and recommendation only |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md) | Required correction package |
| [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) | Operator decision record |
| [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) | Triumph single-Website precedent §3.1 |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Multi-Project BELONGS_TO precedent REL-0027/0028 |

---

*ATLAS ZPM Website Model Consistency Audit v1 — documentation only; no entities or registers modified.*
