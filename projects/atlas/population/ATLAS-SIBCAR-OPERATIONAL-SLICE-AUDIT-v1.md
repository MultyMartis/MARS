# ATLAS SIBCAR Operational Slice Expansion Audit v1

**Status:** **documented** — operational expansion audit (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Subject contour:** ORG-0006 **SIBCAR** · LE-0005 ООО «СибКар» · REL-0041 **CLIENT_OF** → ORG-0001 Полигон  
**Parent:** [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) · [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) · [ATLAS-COVERAGE-AUDIT-v1.md](../audit/ATLAS-COVERAGE-AUDIT-v1.md) · [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](../audit/ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md)  
**Companion:** [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md)  
**Is not:** population pass, attestation act, entity creation, relationship creation, Foundation amendment, runtime export, OCPilot execution, EAR acquisition.

**Restrictions observed:** No entities created. No relationships created. No lifecycle changes. No graph mutations. No Foundation changes.

---

# REPORT — ATLAS SIBCAR Operational Slice Expansion Audit

## 0. Purpose and scope

### 0.1 Question

Какое **доказательное основание** уже существует для расширения operational slice **SIBCAR** за пределы текущего attested minimum:

| Layer | Current state |
|-------|---------------|
| Organization ORG-0006 | **active** — AT-W1C-01 |
| Legal Entity LE-0005 | **active** — AT-W1C-01 |
| Commercial REL-0041 CLIENT_OF → ORG-0001 | **active** — AT-W6B-02 |

…и какова **готовность** к population следующих классов:

- **Project**
- **Website**
- **Domain**
- **OCPilot linkage** (SITE-001 crosswalk)
- **EAR linkage** (snapshot / acquisition path)

### 0.2 Authority baseline reviewed

| Anchor | ID | Lifecycle | Attestation | Primary source |
|--------|-----|-----------|-------------|----------------|
| Organization | ORG-0006 SIBCAR | **active** | AT-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) |
| Legal Entity | LE-0005 ООО «СибКар» | **active** | AT-W1C-01 | Same; INN 5405512542, OGRN 1265400004220 |
| Commercial edge | REL-0041 ORG-0006 → ORG-0001 | **active** | AT-W6B-02 | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) |

### 0.3 Cross-program references reviewed

| Program | Artifact | Role in this audit |
|---------|----------|-------------------|
| **OCPilot** | [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | EV-W1C-02 — Website / engagement context |
| **OCPilot** | [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | EV-W1C-03 — TEST URL, business goal, planned work |
| **OCPilot** | [AUDIT-CHARTER.md](../../../projects/ocpilot/sites/site-001/AUDIT-CHARTER.md), [materials/INTAKE-COMPLETE.md](../../../projects/ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | Run 5 authorization context |
| **OCPilot** | [project-site-registry.md](../../../projects/ocpilot/project-site-registry.md) | SITE-001 registry row |
| **OCPilot** | [freeze/site-001-pre-runtime-bridge/](../../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Run 5 blockers — acquisition path |
| **EAR** | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../../shared/external-access-runtime/EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | Theoretical acquisition channels |
| **EAR** | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) | Run 5 Level 1+ workflow target |
| **EAR** | [EAR-OCPILOT-INTEGRATION-v1.md](../../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) | Consumer boundary — OCPilot reads published snapshots only |
| **Atlas audit** | [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](../audit/ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) §7.6 | SIBCAR org-only tranche — no contradictions |
| **Atlas audit** | [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](../audit/ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) | SUB-06 slice score 2.0/7; MISS-PRJ-01, MISS-WEB-08, MISS-DOM-08 |

### 0.4 Method

Evidence-first cross-read of attested registers, population plans, OCPilot SITE-001 package, EAR SITE-001 documentation, and Wave 6B commercial attestation. Classify readiness **READY / PARTIAL / BLOCKED** per expansion target. Recommend execution sequence across Waves 3–5B. **No** `PRJ-*`, `WEB-*`, `DOM-*`, or relationship ids minted in this audit.

**Governance applied:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-01..06 · [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 class boundaries.

---

## 1. Existing evidence inventory

### 1.1 Primary legal identity (E1)

| Ref | Artifact | Tier | Path / link | Role |
|-----|----------|------|-------------|------|
| **EV-W1C-CC-01** | «Карточка предприятия» | **E1** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | ORG-0006 / LE-0005 identity; OKVED 45.11 auto trade; **no** website/domain on CC |
| EV-W1B-CC-01 | BZPM CC compare | E1 | `bzpm\Реквизиты.docx` | Proves ORG-0006 ≠ ORG-0005 (COR-W1B-05) |

### 1.2 OCPilot operational context (E0+)

| Ref | Artifact | Tier | Key facts extracted |
|-----|----------|------|---------------------|
| **EV-W1C-02** | OCPilot site-passport | E0 operational | SITE-001; name **Автосалон СИБКАР**; ocStore 3.0.3.8 (rs.2); baseline `ocstore-3038-rs2`; env **TEST**; test URL `https://sibcar.new-site.space/`; **READY FOR RUN 5** |
| **EV-W1C-03** | OCPilot project-access-brief | E0 operational | Same test URL; business goal — rebranding, catalog import, SEO, Yandex Direct, OpenCart dev; backup Beget 31.05.2026; public URL **SAFE UNKNOWN**; domain/DNS **SAFE UNKNOWN** |
| EV-OCP-01 | INTAKE-COMPLETE | E0 | Materials accepted; read-only audit approved; Run 5 requested |
| EV-OCP-02 | AUDIT-CHARTER | E0 | READ ONLY audit mode; Run 5 authorized at charter level |
| EV-OCP-03 | project-site-registry | E0 | SITE-001 registered; storage `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` |
| EV-OCP-04 | project-access-brief § Business Goal | E0 | First combat OCPilot pilot for audit/baseline/compare workflow |

### 1.3 EAR documentation context (design / consumer contract)

| Ref | Artifact | Tier | Key facts |
|-----|----------|------|-----------|
| EV-EAR-01 | EAR-SITE-001-ACQUISITION-OPTIONS | design doc | Channels theoretically YES (FTP/SFTP/SSH/PMA/admin/ZIP); **none confirmed executed**; Beget backup referenced |
| EV-EAR-02 | EAR-SITE-001-WORKFLOW-EXAMPLE | design doc | Run 5 minimum Level **1+** with `file-manifest` |
| EV-EAR-03 | site-001-pre-runtime-bridge freeze | operational freeze | Run 5 **paused** pending acquisition path; no published `snapshot_id` |

### 1.4 Commercial corroboration (attested)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **AT-W6B-02** | REL-0041 attestation | attestation | ORG-0006 **CLIENT_OF** ORG-0001 — vendor relationship **active**; OCPilot SITE-001 cited **informational only** |
| EV-W6B-01 | Wave 6B population basis | E1 + operator | SIBCAR purchases services from Polygon; CC + CLIENT role sufficient for REL-0041 |

### 1.5 Evidence gaps (explicit SAFE UNKNOWN)

| gap_id | Topic | Impact on expansion |
|--------|-------|---------------------|
| SU-ORG-02 / ME-W1C-02 | Production public URL | Blocks production Website / Domain |
| ME-W1C-05 | Corporate domain not on CC | Domain OWNS / PRIMARY_DOMAIN defer |
| SU-W6B-04 | Project-level COMMISSIONED_BY / EXECUTES corroboration | Wave 3 — **does not invalidate** REL-0041; closes at Wave 3 |
| SU-W6B-05 | SIBCAR production Website / Domain stack | Waves 4–5 separate from CLIENT_OF |
| W1C-D-05 | Site title «Автосалон СИБКАР» vs CC «СибКар» | Website intake disambiguation — **not** org alias |
| EV-OCP-GAP-01 | Credential channel confirmation | EAR Run 5 execution blocked |
| EV-EAR-GAP-01 | No published EAR snapshot for SITE-001 | OCPilot structural audit blocked |

---

## 2. Current slice completeness

### 2.1 Attested subgraph (present)

```text
LE-0005 ◄──bound── ORG-0006 SIBCAR ──CLIENT_OF──► ORG-0001 Полигон
                                              [REL-0041 active]
```

### 2.2 Missing subgraph (target of this audit)

```text
ORG-0006 ──COMMISSIONED_BY──◄ PRJ-* (candidate)
ORG-0001 ──EXECUTES──────────► PRJ-* (candidate)

WEB-* ──BELONGS_TO──► PRJ-* (candidate)
ORG-0006 ──OWNS──► WEB-* (candidate)

DOM-* ──PRIMARY_DOMAIN──► WEB-* (candidate)
ORG-0006 ──OWNS──► DOM-* (candidate — registrar gate)

SITE-001 (OCPilot) ──crosswalk──► PRJ-* / WEB-* (documentation linkage — not necessarily graph edge)
EAR snapshot ──feeds──► OCPilot Run 5 (consumer path — external to Atlas graph)
```

### 2.3 Slice score

| Metric | Value | Source |
|--------|-------|--------|
| SUB-06 coverage (Method A) | **2.0 / 7** → est. **~5.0 / 7** after Project + Website + Domain + structural edges | [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](../audit/ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) |
| Post-expansion uplift | +Project, +Website, +Domain, +4–6 structural relationships | [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](../audit/ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md) §1.2 |

---

## 3. Candidate Project roster

### 3.1 Classification summary

| Class | Count | Verdict |
|-------|-------|---------|
| **Current active project candidates** | **1** | Accept for Wave 3 proposal |
| Historical / deprecated project candidates | **0** | No second delivery phase evidenced (contrast: ZPM PRJ-0009 + PRJ-0010) |
| Future candidates (hold) | **3+** | SEO-only, Yandex-only, custom module — not separate approved projects without boundary evidence |
| Rejected | **4+** | See register §5 |

### 3.2 Primary candidate — SIBCAR-INTAKE-CAND-A01

| Field | Value |
|-------|-------|
| **Intake label** | SIBCAR-INTAKE-CAND-A01 |
| **Proposed canonical name** | **Автосалон СИБКАР — OpenCart dealership** *(steward may refine: «OpenCart-пилот OCPilot SITE-001»)* |
| **Class** | Current active project candidate → target lifecycle **active** |
| **Population slice** | **client_delivery** |
| **Commissioning org** | ORG-0006 SIBCAR |
| **Execution org** | ORG-0001 Полигон *(inferred from REL-0041 + OCPilot operator context — not substitute for Wave 3B edges)* |
| **Related property** | `sibcar.new-site.space` — Website candidate (Wave 4); **not** Project substitute |
| **OCPilot crosswalk** | SITE-001 — engagement container; **distinct entity class** from Project |
| **Delivery state** | **Active WIP** — rebranding, catalog, SEO prep per EV-W1C-03 planned work checklist |
| **Evidence** | **E0** EV-W1C-02, EV-W1C-03, EV-OCP-01..04; **E1** EV-W1C-CC-01 (org anchor only); **attestation** REL-0041 (commercial, not project boundary) |
| **Attestation readiness** | **PARTIAL** — sufficient for **population proposal** at E0; steward project-boundary statement recommended to close SU-W6B-04 |

**Claim → evidence:**

- «OpenCart dealership engagement for SIBCAR client» → EV-W1C-03 Business Goal + Planned Work
- «Polygon vendor context» → REL-0041 + Wave 6B attestation basis
- «TEST environment property» → EV-W1C-02 test URL — Website class, not auto-Project (EFV-03)

### 3.3 Rejected project candidates

| Rejected | Basis |
|----------|-------|
| OCPilot Run 5 read-only audit as Atlas Project | MARS program context — Wave 3 §5.1 E-17 excluded (ZPM precedent REJ-ZPM-PRJ-02) |
| SITE-001 site_id as Project row | Class boundary — site_id ≠ initiative ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3) |
| BZPM / ORG-0005 engagement | COR-W1B-03 — identity pollution |
| Separate PRJ per planned-work checkbox (SEO, Yandex, theme…) | Single engagement narrative in EV-W1C-03 — split forbidden without distinct delivery evidence (EFV-03) |
| Future custom module development | Not started — hold |

### 3.4 Wave 3 readiness — Project

| Criterion | Assessment |
|-----------|------------|
| ORG-0006 **active** | **Pass** |
| Commercial vendor context | **Pass** — REL-0041 |
| Operator / OCPilot engagement narrative | **Pass** — E0 |
| Explicit project boundary statement (operator) | **Partial** — SU-W6B-04 |
| Contract / SOW artifact | **SAFE UNKNOWN** — not required at E0 tier (ZPM analog) |
| **Classification** | **PARTIAL** → ready for population **proposal**; attestation after mint |

---

## 4. Candidate Website roster

### 4.1 Primary candidate — SIBCAR-INTAKE-WEB-01

| Field | Value |
|-------|-------|
| **Intake label** | SIBCAR-INTAKE-WEB-01 |
| **Proposed canonical name** | **sibcar.new-site.space** *(or display: «Автосалон СИБКАР TEST»)* |
| **website_kind** | **test_deployment** *(operator: TEST env)* |
| **URL** | `https://sibcar.new-site.space/` |
| **primary_org_candidate** | ORG-0006 |
| **primary_project_candidate** | SIBCAR-INTAKE-CAND-A01 |
| **Platform** | ocStore 3.0.3.8 (rs.2) — consumer metadata only |
| **Evidence** | **E0** EV-W1C-02, EV-W1C-03 |
| **Attestation readiness** | **PARTIAL** — TEST URL corroborated; **not** registrant / production proof |

### 4.2 Production candidate — SIBCAR-INTAKE-WEB-02

| Field | Value |
|-------|-------|
| **Intake label** | SIBCAR-INTAKE-WEB-02 |
| **URL** | **SAFE UNKNOWN** |
| **Evidence** | **None** in repo or CC |
| **Attestation readiness** | **BLOCKED** — ME-W1C-02 |

### 4.3 Alias / display disambiguation

| Signal | Resolution |
|--------|------------|
| «Автосалон СИБКАР» (OCPilot site title) | Website display context — **not** attested ORG-0006 alias (W1C-D-05; EFV-01) |
| «СибКар» (CC legal short) | ORG alias only — via LE-0005 |

### 4.4 Wave 4 readiness — Website

| Criterion | TEST property | Production property |
|-----------|---------------|---------------------|
| URL known | **Pass** | **Fail** — SAFE UNKNOWN |
| Org anchor active | **Pass** | **Pass** |
| Environment declared | **Pass** — TEST | N/A |
| Registrant / client ownership corroboration | **Partial** — operator TEST deployment | **BLOCKED** |
| **Classification** | **PARTIAL** | **BLOCKED** |

---

## 5. Candidate Domain roster

### 5.1 Primary candidate — SIBCAR-INTAKE-DOM-01

| Field | Value |
|-------|-------|
| **Intake label** | SIBCAR-INTAKE-DOM-01 |
| **FQDN** | `sibcar.new-site.space` |
| **Class note** | Subdomain on operator/hosting namespace — **not** corporate registrant domain |
| **Evidence** | **E0** hostname from EV-W1C-02/03 |
| **Attestation readiness** | **PARTIAL** — hostname derivable from Wave 4; Domain OWNS / registrant likely **SAFE UNKNOWN** (ZPM precedent SU-DOM-01, ME-W5-ZPM-01) |

### 5.2 Production candidate — SIBCAR-INTAKE-DOM-02

| Field | Value |
|-------|-------|
| **FQDN** | **SAFE UNKNOWN** |
| **Attestation readiness** | **BLOCKED** |

### 5.3 Excluded

| Item | Reason |
|------|--------|
| `mail.ru` (email domain from CC) | Consumer mail — not corporate domain candidate |

### 5.4 Wave 5 / 5B readiness — Domain

| Criterion | TEST hostname | Production apex |
|-----------|---------------|-----------------|
| FQDN from Website | **Partial** — after Wave 4 | **BLOCKED** |
| Registrar E1 | **SAFE UNKNOWN** | **BLOCKED** |
| PRIMARY_DOMAIN target | **Partial** — policy decision on TEST subdomain | **BLOCKED** |
| ORG → Domain OWNS | **Partial / defer** | **BLOCKED** |
| **Classification** | **PARTIAL** | **BLOCKED** |

---

## 6. Candidate relationships

*Draft relationship **types** and **endpoints** for future population — **no ids minted**, **no attestation performed**.*

### 6.1 Wave 3B — Project ↔ Organization

| draft_slot | source | target | type | evidence_basis | readiness |
|------------|--------|--------|------|----------------|-----------|
| REL-SIBCAR-PJ-01 *(draft)* | PRJ-* candidate A01 | ORG-0006 | **COMMISSIONED_BY** | EV-W1C-03; ORG-0006 active | **PARTIAL** |
| REL-SIBCAR-PJ-02 *(draft)* | ORG-0001 Полигон | PRJ-* candidate A01 | **EXECUTES** | REL-0041; EV-W1C-03; ZPM analog REL-ZPM-PJ-02 | **PARTIAL** |

### 6.2 Wave 4B — Website family

| draft_slot | source | target | type | evidence_basis | readiness |
|------------|--------|--------|------|----------------|-----------|
| REL-SIBCAR-WB-01 *(draft)* | WEB-* TEST | PRJ-* candidate A01 | **BELONGS_TO** | EV-W1C-02; single-project single-property case | **PARTIAL** |
| REL-SIBCAR-WB-02 *(draft)* | ORG-0006 | WEB-* TEST | **OWNS** | Operator TEST deployment; CC silent on domain | **PARTIAL** |

### 6.3 Wave 5B — Domain family

| draft_slot | source | target | type | evidence_basis | readiness |
|------------|--------|--------|------|----------------|-----------|
| REL-SIBCAR-DM-01 *(draft)* | DOM-* TEST | WEB-* TEST | **PRIMARY_DOMAIN** | Hostname co-terminous; ZPM DOM-ZPM-01 analog | **PARTIAL** |
| REL-SIBCAR-DM-02 *(draft)* | ORG-0006 | DOM-* TEST | **OWNS** (domain) | Registrar E1 absent | **BLOCKED** or **defer** |

### 6.4 Already attested (not in expansion queue)

| relationship_id | Endpoints | Type | Status |
|-----------------|-----------|------|--------|
| **REL-0041** | ORG-0006 → ORG-0001 | **CLIENT_OF** | **active** — Wave 6B complete |

### 6.5 OCPilot linkage (cross-program — not Atlas graph edge)

| Link | From | To | Mechanism | readiness |
|------|------|-----|-----------|-----------|
| **LK-OCP-01** | SITE-001 | SIBCAR-INTAKE-CAND-A01 | Documentation crosswalk in Project / Website registers | **PARTIAL** — no formal `site_id` field in Foundation graph |
| **LK-OCP-02** | SITE-001 | ORG-0006 | Informational — W1C-D-04 class boundary | **READY** at documentation level |

### 6.6 EAR linkage (cross-program — not Atlas graph edge)

| Link | From | To | Mechanism | readiness |
|------|------|-----|-----------|-----------|
| **LK-EAR-01** | EAR published snapshot | OCPilot Run 5 | Consumer contract — [EAR-OCPILOT-INTEGRATION-v1.md](../../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) | **BLOCKED** — no snapshot published |
| **LK-EAR-02** | SITE-001 | EAR Request / Evidence Package | Operator Mode 0/1 path per EV-EAR-01 | **PARTIAL** — channels theoretically available; not executed |
| **LK-EAR-03** | EAR snapshot metadata | Atlas WEB-* evidence enrichment | Optional future — not normative in v1 | **SAFE UNKNOWN** |

---

## 7. Evidence readiness matrix

| Expansion target | READY | PARTIAL | BLOCKED | Primary blocker |
|------------------|-------|---------|---------|-----------------|
| **Wave 3 Project** | — | **✓** | — | SU-W6B-04 — operator project boundary narrative thin vs ZPM E0 blocks |
| **Wave 3B Project ↔ Org** | — | **✓** | — | Depends on Wave 3 mint |
| **Wave 4 Website (TEST)** | — | **✓** | — | TEST-only; not production registrant proof |
| **Wave 4 Website (production)** | — | — | **✓** | ME-W1C-02 — public URL SAFE UNKNOWN |
| **Wave 4B Website relationships** | — | **✓** | — | Sequential on Wave 3 + 4 |
| **Wave 5 Domain (TEST hostname)** | — | **✓** | — | Registrar / OWNS defer (ZPM precedent) |
| **Wave 5 Domain (production)** | — | — | **✓** | No FQDN evidence |
| **Wave 5B PRIMARY_DOMAIN** | — | **✓** | — | Policy: TEST subdomain vs production apex |
| **OCPilot SITE-001 linkage** | doc crosswalk | **✓** | — | Run 5 execution blocked on EAR path |
| **EAR SITE-001 linkage** | — | channels documented | **✓** | No published snapshot; file-manifest gap |
| **Wave 2C Person (optional)** | CC signatory fields | **✓** | — | Карандашов М.П. on CC; PER-* not required for Waves 3–5 |

---

## 8. Recommended execution sequence

Precedent: ZPM tranche (ORG-0005) — Wave 3 → 3B → 4 → 4B → 5 → 5B; Wave 6B CLIENT_OF may precede or follow structural stack (SIBCAR: **already attested**).

### 8.1 Wave 3 — Project population

| Step | Action | Prerequisite | readiness |
|------|--------|--------------|-----------|
| W3-SIBCAR-01 | Operator project-boundary statement (closes SU-W6B-04) | Optional but recommended | PARTIAL without |
| W3-SIBCAR-02 | Mint **1** Project (SIBCAR-INTAKE-CAND-A01) | ORG-0006 active | PARTIAL → proposal ready |
| W3-SIBCAR-03 | Project attestation act | Population complete | Pending execution |

**Suggested id slot at population (not assigned here):** next sequential after PRJ-0010 → **PRJ-0011** *(documentation estimate only)*.

### 8.2 Wave 3B — Project ↔ Organization relationships

| Step | Action | readiness |
|------|--------|-----------|
| W3B-SIBCAR-01 | COMMISSIONED_BY PRJ → ORG-0006 | PARTIAL |
| W3B-SIBCAR-02 | EXECUTES ORG-0001 → PRJ | PARTIAL |
| W3B-SIBCAR-03 | Attestation | Pending Wave 3 |

### 8.3 Wave 4 — Website population

| Step | Action | readiness |
|------|--------|-----------|
| W4-SIBCAR-01 | Mint WEB-* for `sibcar.new-site.space` (TEST) | PARTIAL |
| W4-SIBCAR-02 | Record W1C-D-05 disambiguation in Website register | READY |
| W4-SIBCAR-03 | **Defer** production WEB until URL known | BLOCKED |
| W4-SIBCAR-04 | Website attestation | Pending population |

**Suggested id slot:** **WEB-0010** or **WEB-SIBCAR-01** *(steward choice at population)*.

### 8.4 Wave 4B — Website relationships

| Step | Action | readiness |
|------|--------|-----------|
| W4B-SIBCAR-01 | BELONGS_TO WEB → PRJ | PARTIAL |
| W4B-SIBCAR-02 | OWNS ORG-0006 → WEB | PARTIAL |
| W4B-SIBCAR-03 | Attestation | Pending Wave 4 |

### 8.5 Wave 5 — Domain population

| Step | Action | readiness |
|------|--------|-----------|
| W5-SIBCAR-01 | Mint DOM-* for TEST hostname | PARTIAL |
| W5-SIBCAR-02 | Document registrar SAFE UNKNOWN | Expected — ZPM analog |
| W5-SIBCAR-03 | **Defer** production domain | BLOCKED |
| W5-SIBCAR-04 | Domain attestation | Pending Wave 4 |

### 8.6 Wave 5B — Domain relationships

| Step | Action | readiness |
|------|--------|-----------|
| W5B-SIBCAR-01 | PRIMARY_DOMAIN DOM → WEB | PARTIAL |
| W5B-SIBCAR-02 | OWNS ORG-0006 → DOM — **defer** if no registrar E1 | PARTIAL / defer |
| W5B-SIBCAR-03 | Attestation | Pending Wave 5 |

### 8.7 Parallel cross-program tracks (non-Atlas graph)

| Track | Sequence | Blocker |
|-------|----------|---------|
| **EAR** | Operator Request → Mode 0/1 evidence → Validate → Publish snapshot | No snapshot; channel confirmation |
| **OCPilot** | Intake published snapshot → Run 5 resume | EAR LK-EAR-01 |
| **Atlas ↔ OCPilot** | Document SITE-001 crosswalk in Wave 3/4 registers | None — documentation only |

### 8.8 Optional — Wave 2C Person

Not on critical path for operational slice. CC provides Карандашов Максим Петрович — queue when steward prioritizes contact graph.

---

## 9. Duplicate and integrity review

| review_id | Signal | Verdict |
|-----------|--------|---------|
| SIBCAR-OS-D-01 | SIBCAR vs BZPM / SITE-001 on ORG-0005 | **Distinct** — COR-W1B-03; INN mismatch |
| SIBCAR-OS-D-02 | SITE-001 vs ORG-0006 | **Class boundary** — Pass |
| SIBCAR-OS-D-03 | «Автосалон СИБКАР» vs «СибКар» | **Open — low** — Website intake note |
| SIBCAR-OS-D-04 | REL-0041 vs future COMMISSIONED_BY | **Complementary** — org commercial vs project structural |
| SIBCAR-OS-D-05 | Single vs multi-project on TEST hostname | **Single project** — no second delivery phase evidenced |

**Integrity vs attested graph:** **Pass** — no contradiction with [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](../audit/ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) §7.6.

---

## 10. Audit verdict

```text
SIBCAR OPERATIONAL SLICE EXPANSION — PARTIALLY READY
```

**Meaning:**

1. **Attested anchor complete** — ORG-0006, LE-0005, REL-0041 provide legal + commercial foundation.
2. **Structural stack (Project → Website → Domain)** evidenced at **E0** for **TEST** property only — sufficient for **population proposals** across Waves 3–5B with ZPM precedent.
3. **Production** Website / Domain remain **BLOCKED** until public URL and registrar evidence arrive.
4. **OCPilot linkage** document-ready; **EAR linkage** blocked on published snapshot.
5. **No Foundation amendment** required for recommended sequence.

**Not selected:**

| Verdict | Why not |
|---------|---------|
| **READY FOR FULL EXECUTION** | Production URL unknown; EAR snapshot absent; SU-W6B-04 open |
| **BLOCKED — NO EVIDENCE** | Substantial E0 OCPilot + E1 CC + attested CLIENT_OF exist |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md) | Tabular register |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md) | Executive summary |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | Org tranche lineage §9–11 |
| [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) | Structural stack precedent |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | REL-0041 act |

---

*ATLAS SIBCAR Operational Slice Expansion Audit v1 — documentation only.*
