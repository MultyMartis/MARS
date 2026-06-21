# ATLAS Identity Governance v1

**Status:** **documented** — Phase 3 normative governance for entity identity.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) · [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)  
**Is not:** merge bot, deduplication ML, CRM sync job, approval UI, RBAC implementation.

---

## 1. Purpose

Define **how humans govern identity** when business reality is ambiguous — duplicate candidates, merge and split events, domain ownership uncertainty, person homonyms, and consumer import conflicts.

Governance only. No implementation.

Aligned with Phase 1–2: human-supervised, documentation-first, **SAFE UNKNOWN** over silent invention.

---

## 2. Governance roles

Roles align with [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §2 — extended for identity.

| Role | Identity authority |
|------|-------------------|
| **Program owner / operator** | Final merge/split; dispute resolution; namespace policy |
| **Registry steward** | Intake, duplicate triage, alias attestation, propose → active |
| **Consumer proposer** | Propose entity / alias mapping (future) — not canonical alone |
| **Agent proposer** | Proposal only |
| **Auditor (read-only)** | Flag duplicates; no attestation |

### 2.1 Authority matrix

| Action | Owner | Steward | Consumer | Agent |
|--------|-------|---------|----------|-------|
| Create **proposed** entity | Yes | Yes | Yes (future) | Propose |
| Promote to **active** canonical | Yes | Delegated | **No** | **No** |
| Add attested **alias** | Yes | Delegated | No | No |
| Initiate **merge** | Yes | Propose | No | No |
| Approve **merge** | Yes | Delegated | No | No |
| Initiate **split** | Yes | Propose | No | No |
| Approve **split** | **Owner only** | No | No | No |
| Mark **disputed** | Yes | Yes | Flag | Flag |
| Declare **SAFE UNKNOWN** | Yes | Yes | No | No |
| Deprecate without merge | Yes | Yes | No | No |

**Rule IGV-01:** No autonomous promotion to canonical entity.

**Rule IGV-02:** Split requires program owner approval (IGV-S01).

---

## 3. Duplicate handling

### 3.1 What is a duplicate?

| Class | Definition |
|-------|------------|
| **D1 — True duplicate** | Two **active** canonical records for the **same** business subject |
| **D2 — Suspected duplicate** | High likelihood same subject; not yet attested |
| **D3 — Homonym** | Same name string; **different** subjects |
| **D4 — Import duplicate** | Consumer system has two keys; ATLAS has zero or one |
| **D5 — Cross-type mistake** | Person recorded as Organization |

### 3.2 Detection sources (conceptual)

| Source | Output |
|--------|--------|
| Steward intake | Manual flag |
| Alias collision report | Disputed alias |
| Consumer import | Mapping proposal |
| Relationship inconsistency | Two OWNER graphs implying one org — review entities first |
| Agent suggestion | **proposed** only |

**Rule IGV-D01:** String similarity alone is **insufficient** for merge.

### 3.3 Duplicate handling workflow

```text
Detect (D1–D5)
  → Halt second canonical if D1
  → Classify: true duplicate | homonym | unknown
  → Gather evidence (§5)
  → Resolve:
        merge (same subject)
     OR maintain separate (different subject)
     OR SAFE UNKNOWN (insufficient evidence)
  → Update aliases / redirects
  → Reconcile relationships (§8)
```

### 3.4 Duplicate handling strategy (summary)

| Situation | Strategy |
|-----------|----------|
| Attested same org | **Merge** — one survivor `ORG-*` |
| Attested different orgs, similar names | **Separate ids** + disambiguation in canonical name or note |
| Uncertain | **proposed** + **SAFE UNKNOWN** for consumer canonical use |
| CRM double | Map both to proposed; steward decides |
| Placeholder invented earlier | Deprecate placeholder; merge or archive — never canonical |

**Prohibition IGV-D02:** Create `org-unknown-*` as permanent canonical ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10).

---

## 4. Merge rules

### 4.1 When merge is appropriate

| Criterion | Required |
|-----------|----------|
| Same business subject (org, person, site, domain, project) | **Yes** |
| Human attestation | **Yes** |
| Evidence tier | ≥ E1 (E2 for org legal merge) |
| Survivor selected | **Yes** |
| Relationship impact reviewed | **Yes** |

### 4.2 Survivor selection

| Entity type | Default survivor preference |
|-------------|------------------------------|
| Organization | Older id **or** id already referenced by most consumers — **owner decides** |
| Person | Id with most attested relationships |
| Website / Domain | Id linked to primary production consumer |
| Project | Id referenced in active Factory/ORCA packs |
| Relationship | Phase 2 supersession — not entity merge |

**Rule IGV-M01:** Survivor id **never** changes on merge.

### 4.3 Merge procedure (conceptual)

| Step | Action |
|------|--------|
| 1 | Freeze new canonical use of absorbed ids |
| 2 | Set absorbed state → `merged_into` + `redirect_to` survivor |
| 3 | Union alias sets ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) §5.5) |
| 4 | Reconcile relationships — deprecate duplicates, retain history |
| 5 | Publish attestation note + evidence_ref |
| 6 | Notify consumers: redirect table update (future) |

### 4.4 Merge forbidden cases

| Case | Why forbidden |
|------|---------------|
| Same Business Scope only | Scope ≠ sameness |
| Same domain TLD pattern | Coincidence |
| Same person name | Homonym |
| Convenience to reduce row count | Audit integrity |
| Different legal entities post-acquisition without legal review | May need **relationship** only |

### 4.5 Program exemplar: Polygon

If `ORG-0001` Polygon and proposed `ORG-0042` “ООО Полигон” are attested **same unit**:

- Survivor: `ORG-0001`
- `ORG-0042` → `merged_into` → `ORG-0001`
- Aliases: Полигон, WSP, Web Studio Polygon on survivor

---

## 5. Split rules

### 5.1 When split is appropriate

**Rare.** Use when a **single** canonical record incorrectly combined **two or more** distinct subjects.

| Criterion | Required |
|-----------|----------|
| Evidence of distinct subjects | **Yes** (E2 typical) |
| Owner approval | **Yes** (IGV-S01) |
| New ids for children | **Yes** |
| Source id deprecated | **Yes** |

### 5.2 Split procedure (conceptual)

| Step | Action |
|------|--------|
| 1 | Deprecate combined record (source id) |
| 2 | Mint **new** active ids for each child subject |
| 3 | Partition aliases by attestation |
| 4 | Partition relationships — human review per edge |
| 5 | Document lineage `split_from` on children |

### 5.3 Split vs alias correction

| Problem | Remedy |
|---------|--------|
| Wrong alias on correct entity | Remove/fix alias |
| Two brands one org | Aliases, not split |
| Two legal entities wrongly one org | **Split** |
| Merger created holding company | Often **new org** + PARENT_OF relationship, not split |

**Rule IGV-S01:** Only program owner approves split.

---

## 6. Conflict resolution

### 6.1 Conflict classes

| Class | Example | Resolution owner |
|-------|---------|------------------|
| **C1 — Dual canonical** | Two active Polygon orgs | Owner — merge or deprecate one |
| **C2 — Disputed sameness** | Import says merge; steward disagrees | Disputed until evidence |
| **C3 — Alias collision** | WSP on two orgs | Disambiguation notes; may drop alias |
| **C4 — Consumer map fight** | CRM A and B map to different `ORG-*` | Steward + owner |
| **C5 — Person homonym** | Two Andrey, one email proposed | Separate PER or UNKNOWN |
| **C6 — Domain ownership** | Uncertain org owns `DOM-*` | SAFE UNKNOWN ownership relationship |
| **C7 — Website relatedness** | Two sites “look related” | Separate `WEB-*` unless attested same property |

### 6.2 Resolution principles

| Principle | Application |
|-----------|-------------|
| **Prefer UNKNOWN** | Over false merge |
| **Prefer merge** | Only with positive evidence of same subject |
| **Preserve history** | Never delete ids |
| **Identity before relationship** | Fix entities before canonical OWNER ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) A4) |

### 6.3 Disputed coexistence

| Record state | Allowed count |
|--------------|---------------|
| **active** canonical per subject | **1** |
| **proposed** / **disputed** candidates | **Many** |

---

## 7. Evidence requirements

### 7.1 Evidence tiers (identity)

Reuses tier vocabulary from Phase 2 ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §3.1).

| Tier | Identity use |
|------|----------------|
| **E0** | Operator direct knowledge — alias, canonical name |
| **E1** | Email, informal doc, chat export — merge proposal |
| **E2** | Corporate registry, contract party, registrar — org merge, split |
| **E3** | Consumer foreign key snapshot — mapping hint only |

### 7.2 Minimum tier by action

| Action | Minimum tier |
|--------|--------------|
| proposed → active (new entity) | E0 (operator) or E1 (steward) |
| Merge Organization | E1 (E2 if legal entity dispute) |
| Merge Person | E2 (identity sensitivity) |
| Split | E2 |
| Declare SAFE UNKNOWN | None — document reason |
| Absorb CRM duplicate | E1 + consumer export reference |

### 7.3 Insufficient evidence

| Situation | Action |
|-----------|--------|
| Below tier | Remain **proposed** |
| No evidence | **SAFE UNKNOWN** — no new active canonical |
| Fabricated evidence ref | Reject; incident log |

---

## 8. Uncertainty handling

### 8.1 Uncertainty classes (identity)

| Class | Example | Default |
|-------|---------|---------|
| **I1 — Unknown sameness** | MetaCode vs Метакод vendor? | proposed + investigation |
| **I2 — Unknown entity existence** | Is “Web Studio Polygon” separate org? | SAFE UNKNOWN or proposed |
| **I3 — Unknown person** | Which Andrey? | SAFE UNKNOWN slot |
| **I4 — Unknown domain owner** | Who owns `DOM-*`? | No canonical OWNS; UNKNOWN |
| **I5 — Unknown website sameness** | Landing vs main site | Separate WEB unless attested same |
| **I6 — Import unmappable** | CRM id orphan | proposed mapping; not auto entity |

### 8.2 Uncertainty workflow

```text
Detect I1–I6 → Block canonical promotion
            → Document intake log
            → Gather evidence OR SAFE UNKNOWN
            → Human resolve → active | merge | split | separate
```

### 8.3 Relationship interaction after identity events

| Event | Relationship action |
|-------|---------------------|
| Merge org | Duplicate OWNS/CLIENT edges reviewed; deprecate redundant |
| Split org | Edges partitioned to child orgs |
| SAFE UNKNOWN org | No new canonical OWNS to that org |
| Merge person | Multiple OWNER edges may collapse to one person id |

Detail remains Phase 2 lifecycle; identity governance **triggers** review, does not redefine types.

---

## 9. Scenario playbooks (program exemplars)

### 9.1 Two organizations appear identical

| Step | Action |
|------|--------|
| 1 | List aliases, legal refs, CRM ids |
| 2 | If same tax id / same operator attestation → merge |
| 3 | If different clients of same holding → **separate** + PARENT_OF (future relationship) |
| 4 | If unclear → **disputed** + SAFE UNKNOWN for new canonical refs |

### 9.2 Two websites appear related

| Step | Action |
|------|--------|
| 1 | Attest: same **property** vs separate properties |
| 2 | Same property → one `WEB-*`, aliases for titles |
| 3 | Separate → two `WEB-*`, RELATED_VIA relationship if taxonomy adds (else notes) |
| 4 | Do not merge because same org owns both |

### 9.3 Domain ownership uncertain

| Step | Action |
|------|--------|
| 1 | `DOM-*` may exist with attested hostname |
| 2 | OWNS relationship → **SAFE UNKNOWN** until E1/E2 |
| 3 | Allow **proposed** OWNS candidates |
| 4 | Website Factory must not assume owner org |

### 9.4 Person identity ambiguous

| Step | Action |
|------|--------|
| 1 | Separate `PER-*` per attested human |
| 2 | Homonym → disambiguate canonical name (“Andrey Ivanov” vs “Andrey Petrov”) |
| 3 | Email conflict → UNKNOWN; do not merge |
| 4 | Link operational logins in consumer systems — not in ATLAS core |

---

## 10. Consumer and import governance

| Rule | Detail |
|------|--------|
| **IGV-C01** | Bulk import creates **proposed** only |
| **IGV-C02** | Import must not deprecate canonical without owner |
| **IGV-C03** | Consumer id map is versioned metadata |
| **IGV-C04** | Downstream must honor SAFE UNKNOWN |

---

## 11. Prohibitions

| # | Prohibition |
|---|-------------|
| **IGV-X01** | Auto-merge on name match |
| **IGV-X02** | Business Scope driven merge |
| **IGV-X03** | Deleting entity ids without archive state |
| **IGV-X04** | Split without owner approval |
| **IGV-X05** | Canonical entity to unblock relationship export |
| **IGV-X06** | Reusing merged id |

---

## 12. Required architectural analysis (governance lens)

| Question | Decision |
|----------|----------|
| Duplicate entities? | Detect early; **one** active canonical per subject; merge or separate with evidence |
| Merge allowed? | **Yes** — survivor + redirect + alias union |
| Split allowed? | **Yes** — rare, owner-only |
| Historical identity? | `merged_into`, `former` aliases, archived states |
| Business Scope? | **Never** merge driver; entities must exist before scope tags |

---

## 13. Phase 3 governance checklist

- [ ] Duplicate classes and workflow defined
- [ ] Merge and split rules with evidence tiers
- [ ] Conflict resolution aligned with Phase 2
- [ ] SAFE UNKNOWN postures for I1–I6
- [ ] Scenario playbooks for program exemplars
- [ ] No implementation claims

---

## 14. Related documents

| Document | Role |
|----------|------|
| [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) | Lifecycle states |
| [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) | Non-reuse, redirect |
| [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) | Alias union on merge |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | A4, evidence tiers |
| [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) | Deprecation over proliferation |

**Deferred:** automated deduplication, CRM sync, registry storage of redirect table.
