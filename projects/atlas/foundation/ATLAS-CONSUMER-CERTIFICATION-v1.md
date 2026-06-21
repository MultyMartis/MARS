# ATLAS Consumer Certification v1

**Status:** **documented** — Phase 6 documentation-level readiness model (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md)  
**Is not:** runtime certification, automated compliance scanner, ISO audit, penetration test, API conformance suite.

**Phase 1–5 constraint:** No changes to approved Phase 1–5 documents unless contradictions are discovered. None identified at Phase 6 authoring.

---

## 1. Purpose

Provide a **governance readiness model** (levels **C0–C3**) measuring whether a consumer **correctly adopts** ATLAS semantics before claiming cross-program reliance on canonical structure.

**This is not runtime certification.** No service, badge API, or CI gate is defined in Phase 6.

---

## 2. Certification philosophy

| Principle | Statement |
|-----------|-----------|
| **Evidence-based** | Level claimed only with documented artifacts |
| **Self-assess + review** | Consumer prepares; ATLAS program owner or steward validates C2+ |
| **Consumer-agnostic criteria** | Same rubric for MIG and Secretary |
| **Progressive** | Higher levels add structural reliance requirements |

---

## 3. Level overview

| Level | Name | Summary |
|-------|------|---------|
| **C0** | **Aware** | Acknowledges ATLAS; no canonical reliance |
| **C1** | **Aligned** | Charters + semantic contract acknowledged |
| **C2** | **Mapped** | Published mapping; UNKNOWN discipline |
| **C3** | **Reliant** | Durable references; governance hooks active |

**Rule CERT-01:** Levels are **cumulative** — C2 requires C1 criteria met.

**Rule CERT-02:** Certification **expires** on Semantic Contract amendment until re-review (minimum C1).

---

## 4. Level requirements

### 4.1 C0 — Aware

| Criterion | Evidence |
|-----------|----------|
| Program listed as ATLAS consumer (or planned) | Registry row or charter mention |
| No parallel canonical org/person list marketed | Charter attestation |
| Team aware ATLAS ≠ ops system | Onboarding note |

**May:** Use local-only data without ATLAS ids.  
**May not:** Claim “ATLAS-certified” or “canonical via [Consumer]”.

---

### 4.2 C1 — Aligned

**Requires C0 +**

| Criterion | Evidence |
|-----------|----------|
| Adoption owner named | Charter § or ROLE.md |
| [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md) accepted | Signed compliance checklist §9 |
| Phase 4 contracts acknowledged | Link in charter |
| No MAP-B01–B09 in documented design | Design review note |
| Business Scope not used as identity partition | Charter rule |

**May:** Read ATLAS when available; reference with risk flags on **proposed**.  
**May not:** Production campaigns **requiring** unresolved UNKNOWN without exception process.

---

### 4.3 C2 — Mapped

**Requires C1 +**

| Criterion | Evidence |
|-----------|----------|
| Published mapping table (versioned) | `*-atlas-mapping.md` or appendix |
| All high-traffic ops states classified M-DISP / M-SUGG / M-NONE / M-BAN | Mapping table complete |
| SAFE UNKNOWN surfaced in UX/docs | Screenshot or copy spec |
| **merged** / **replaced** redirect handling documented | Integration note |
| Dispute/challenge path documented | Links to Consumer Governance |
| Certification review by steward | Review date + reviewer |

**May:** Durable `atlas_*` foreign keys on new artifacts.  
**May not:** Auto-attest; auto-map completed→deprecated.

---

### 4.4 C3 — Reliant

**Requires C2 +**

| Criterion | Evidence |
|-----------|----------|
| New durable cross-system artifacts require **active** canonical ids (or explicit UNKNOWN exception) | Published policy |
| Cache invalidation policy documented | Local doc |
| Remediation playbook for merge/replace notifications | Runbook |
| No open S3+ governance violations | Audit log |
| Annual re-certification scheduled | Calendar / registry note |

**May:** Market program claims “structural truth via ATLAS” for covered entity types.  
**May not:** Override ATLAS on conflict without challenge path.

---

## 5. Evaluation rubric (scoring aid)

Optional scoring for reviews — not required for compliance:

| Dimension | Weight | C1 min | C2 min | C3 min |
|-----------|--------|--------|--------|--------|
| Semantic contract | 30% | 70% | 85% | 95% |
| Mapping discipline | 25% | — | 85% | 95% |
| Governance hooks | 20% | 60% | 80% | 90% |
| UNKNOWN handling | 15% | 70% | 85% | 95% |
| Reference integrity | 10% | — | 70% | 90% |

---

## 6. Downgrade and revocation

| Trigger | Action |
|---------|--------|
| Parallel registry discovered | Drop to C0 until merge plan |
| Auto-attest path deployed | Drop to C1 until removed |
| Semantic fork in production | Drop to C1; S4 incident |
| Ignored merge redirect | Drop to C2 until remap complete |
| Refusal to update mapping after ATLAS amend | Hold level; block upgrade |

---

## 7. Example consumer targets (illustrative)

Status below is **not assessed** in Phase 6 — targets for future reviews:

| Consumer | Likely current band | Notes |
|----------|---------------------|-------|
| **MIG** | C0→C1 | Heavy market layer; strict MAP-B08 |
| **ORCA** | C0→C1 | Interpretation; needs CLIENT_OF discipline |
| **Website Factory** | C1→C2 | Site/org references when packs exist |
| **WPilot / OCPilot** | C1→C2 | WEB-* reliance; no OWNER from CMS role |
| **HomeGateway** | C1→C2 | Broad read; must not become shadow registry |
| **Secretary** (future) | C0 at charter | Party ids only; doc workflow M-NONE |

---

## 8. Certification artifacts (documentation pack)

Recommended file set per consumer:

```text
projects/<consumer>/governance/
  ATLAS-ADOPTION-STATEMENT.md      # level claimed + owner
  ATLAS-MAPPING-TABLE.md           # C2+
  ATLAS-SEMANTIC-CHECKLIST.md      # SC-* sign-off
  ATLAS-REMEDIATION-RUNBOOK.md     # C3
```

Phase 6 does **not** create these files — consumers produce during adoption.

---

## 9. Relationship to implementation

| Level | Implementation required? |
|-------|-------------------------|
| C0–C1 | **No** — documentation only |
| C2 | **No** — may use manual id lookup |
| C3 | **Recommended** — mechanical enforcement; not defined here |

Implementation planning is a **separate package** ([ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md) §12).

---

## 10. Compliance checklist (reviewer)

- [ ] Level claimed matches evidence?
- [ ] Cumulative criteria satisfied?
- [ ] Mapping table covers CRM/PM/SEO/CMS domains in scope?
- [ ] No forbidden lifecycle codes in ATLAS-shaped fields?
- [ ] Challenge path exists?
- [ ] Business Scope independence confirmed?

---

*ATLAS Consumer Certification v1 — Phase 6 Foundation. Documentation only.*
