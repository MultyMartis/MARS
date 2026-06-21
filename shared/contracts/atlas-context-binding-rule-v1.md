# ATLAS Context Binding Rule v1

**Status:** **documented** — formal ecosystem rule (audit verdict: Namespace Collision Risk).  
**Not:** schema, registry, API, synchronization workflow, runtime policy, integration architecture, or enforcement engine.

**Verdict (normative):**

> Consumer systems **may reference** ATLAS canonical ids **without owning** business reality.  
> Consumer-local ids **must not** substitute for ATLAS ids when active canonical exists.

**Canonical boundary:**

> **ATLAS holds business structure. MIG holds market groundtruth. ORCA holds interpretation.**  
> Binding is **pointer discipline** — not ownership transfer.

---

## 1. Purpose

The ATLAS / MIG / ORCA Relationship Audit confirmed that **ownership boundaries are valid** ([groundtruth-ownership-rule-v1.md](groundtruth-ownership-rule-v1.md)) but identified **Entity Binding** as the remaining gap:

| System | Example local id | Same business subject |
|--------|------------------|------------------------|
| ATLAS | `ORG-0004`, `WEB-0008`, `PRJ-0005` | Триумф / Грузотакси |
| MIG | `session-mig-20260606-kwrd01` | Market capture for that subject |
| ORCA | `triumph-manipulator-krasnodar` | PPC interpretation lane |

Each namespace is legitimate. **No formal binding** lets operators treat slugs, session folders, and display names as interchangeable canonical keys — **Namespace Collision Risk**.

This rule defines **what may be referenced**, **who owns what**, and **what must not be duplicated** — without integration, runtime, or synchronization.

---

## 2. Definitions

| Term | Meaning |
|------|---------|
| **Business reality** | Canonical structural truth: organizations, projects, websites, domains, people, typed relationships — **ATLAS-owned**. |
| **Market groundtruth** | Evidence-grade market observations: SERP, competitors, captures, keyword tables — **MIG-owned**. |
| **Interpretation** | Semantic clustering, PPC architecture, campaign artifacts, LRL — **ORCA-owned**. |
| **Binding** | A **durable pointer** from a consumer artifact to an ATLAS canonical id. Binding **does not** copy canonical fields or transfer ownership. |
| **Consumer-local id** | Id minted and owned by the consumer (`session_id`, `pack_id`, `project_id`, `route_id`, `FP-*`, …). **Not** an ATLAS id. |
| **Subject context** | The business subject a consumer artifact is **about** — may span one or more ATLAS entities (typically `ORG-*` + `PRJ-*`, optionally `WEB-*` / `DOM-*`). |

---

## 3. Canonical reference convention (RC-01)

Normative field naming follows Website Factory **RC-01** ([WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](../../workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md)) and ATLAS Consumer Contracts **CC-01** ([ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md)):

| Field name | ATLAS id pattern | When to bind |
|------------|------------------|--------------|
| `atlas_client_org_ref` | `ORG-*` | Client / commissioning organization — **primary subject anchor** |
| `atlas_project_ref` | `PRJ-*` | Structural ATLAS project the work serves — **not** consumer `project_id` |
| `atlas_website_ref` | `WEB-*` | When work is scoped to a specific web property |
| `atlas_domain_ref` | `DOM-*` | When hostname identity matters independently of website |
| `atlas_person_ref` | `PER-*` | When a person is charter-bound to the artifact |
| `atlas_relationship_ref` | `REL-*` | When a specific structural edge is material to the artifact (informational) |

**Rule BIND-01:** Use **full ATLAS id strings** (`ORG-0004`) — not display names, domains alone, or invented UUIDs ([ATLAS-CONSUMER-MAPPING-RULES-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-MAPPING-RULES-v1.md) §7.2).

**Rule BIND-02:** ATLAS refs are **pointers** — consumers **must not** restate legal name, INN, ownership graph, or lifecycle state as if locally authoritative.

**Rule BIND-03:** Only **active** or explicitly **proposed** ATLAS ids may appear in durable bindings. **Disputed** or **deprecated** ids require successor/redirect handling per [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md).

**Conceptual alias:** Documentation may say `atlas_org_id` — semantically equivalent to `atlas_client_org_ref` when context is unambiguous. **RC-01 field names are preferred** in new bindings.

---

## 4. Binding inventory (audit snapshot)

### 4.1 MIG

| Location | Explicit ATLAS refs | Implicit subject | Missing binding |
|----------|---------------------|------------------|-----------------|
| `session_manifest.json` | **None** today | `scope.niche`, `scope.region`, queries | `atlas_client_org_ref`, `atlas_project_ref` |
| Research Pack metadata (contract §2.1) | **None** in v0 schema | Scope mirrors session | Same — optional `atlas_context` block recommended at human bind time |
| `downstream_context.orca_project_id` | N/A — **ORCA-local** | Links to interpretation lane | Not an ATLAS substitute |
| `entity-classification-proposal.md` | Explicitly **no ATLAS dependency** | Domains, market classes | Competitor domains **≠** `ORG-*` until attest proposal |
| Pilot folder `triumph-gruzotaxi-krasnodar/` | **None** | Triumph / грузотакси / Краснодар | Should bind to `ORG-0004` + `PRJ-0005` when operator confirms subject |
| Research Request intake | **None** | `scope`, `queries` | Optional passthrough of ATLAS refs in `downstream_context` — **not** canonical intake fields today |

### 4.2 ORCA

| Location | Explicit ATLAS refs | Implicit subject | Missing binding |
|----------|---------------------|------------------|-----------------|
| `PROJECT.md` (contract) | **Not required** by v0 template | `brand`, `geo`, `domain (declared)` | Triumph container uses `manipulator-triumph.ru` — maps to `WEB-0009` / `PRJ-0008` in ATLAS but **unbound** |
| `project_id` slug | N/A — **ORCA-local** | Stable slug | **Must not** be treated as `PRJ-*` |
| LRC / landing contracts | `project_id` (ORCA) | URL, route | Optional `atlas_website_ref` when route maps to attested site |
| MIG handoff consumption | `session_id` / pack pointer (optional) | Approved Research Pack | `atlas_*` refs should align with pack subject when both exist |
| `ppc/triumph-manipulator/` legacy pack | **None** | Brand + geo in pack docs | Legacy — bind on migration or charter refresh |

### 4.3 Precedent (Website Factory)

| Location | Status |
|----------|--------|
| `MOC-12-external-refs.md` (FP-0001) | **Bound** — `ORG-0004`, `PRJ-0008`, `WEB-0009`, `DOM-0004` |

Website Factory demonstrates **target posture** for MIG and ORCA: RC-01 fields in human-maintained charter surfaces.

---

## 5. Binding ownership

| Entity / id | Owner | Others may |
|-------------|-------|------------|
| `ORG-*`, `PER-*`, `PRJ-*`, `WEB-*`, `DOM-*`, `REL-*` | **ATLAS** | **Reference** only; **suggest** corrections via attest path |
| `session_id`, `pack_id`, Research Pack lifecycle | **MIG** | ORCA **consumes** approved pack — does not own session |
| `project_id`, `route_id`, LRC, PPC exports | **ORCA** | MIG may record `orca_project_id` in passthrough — does not own ORCA project |
| `FP-*` Factory Project | **Website Factory** | Distinct from `atlas_project_ref` |
| Market competitor domains in MIG captures | **MIG evidence** | Propose new `ORG-*` / `WEB-*` to ATLAS — **not** auto-canonical ([ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) CC-P06, MAP-B08) |

**Rule OWN-01:** Referencing `ORG-0004` in a MIG session **does not** make MIG the owner of that organization.

**Rule OWN-02:** Referencing `PRJ-0005` in ORCA **does not** merge ORCA `project_id` with ATLAS project identity.

**Rule OWN-03:** One business **organization** may have **multiple** ATLAS projects (`PRJ-0005` Грузотакси vs `PRJ-0008` Манипулятор under `ORG-0004`). Bind **the project that matches the artifact scope** — not “the client slug” alone.

---

## 6. Allowed references

### 6.1 Required posture (normative intent)

When **active attested canonical** exists for the artifact's subject ([WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](../../workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md) ADOPT-01, CC-01):

| Consumer | Minimum binding surface | Minimum fields |
|----------|-------------------------|----------------|
| **MIG** Research Session / Pack (human-maintained) | Session README, pack front matter, or operator bind note | `atlas_client_org_ref` + `atlas_project_ref` when subject is a known client initiative |
| **ORCA** managed project | `PROJECT.md` — **ATLAS context** section | Same minimum when subject is a known client initiative |
| **Website Factory** | MOC-12 / charter | Already normative per RC-01 |

### 6.2 Optional references (recommended, not blocking)

| Field | Consumer | Use |
|-------|----------|-----|
| `atlas_website_ref` | MIG, ORCA, Factory | Session scoped to one site; LRC route; landing capture target |
| `atlas_domain_ref` | MIG, ORCA, Factory | DNS/hostname discipline when distinct from website record |
| `atlas_person_ref` | Any | Charter names a responsible person |
| `atlas_relationship_ref` | Any | Informational — e.g. `COMMISSIONED_BY` edge already attested |
| `mig_session_id` / `pack_id` | ORCA | After approved handoff — **consumption pointer**, MIG-owned |
| `orca_project_id` | MIG | In `downstream_context` — **interpretation lane pointer**, ORCA-owned |

### 6.3 Cross-consumer pointer discipline

```text
ATLAS (structure)          MIG (groundtruth)           ORCA (interpretation)
ORG-0004, PRJ-0005    ←── atlas_* refs ──→    session-mig-*     ←── pack handoff ──→    triumph-* / makita-*
     ↑                          │                              │
     └──────── atlas_* refs ─────┴──────────────────────────────┘
```

Pointers are **documentation fields** maintained by operators. No implied sync, API, or registry write.

---

## 7. What must not be duplicated

| Do not duplicate in MIG / ORCA | ATLAS owns |
|--------------------------------|------------|
| Canonical organization legal identity | Names, aliases, lifecycle |
| Parallel org/project/website registries | Full entity graph |
| Structural relationships as local truth | `REL-*` edges |
| Market discovery → silent `ORG-*` promotion | Competitor attestation path |
| Domain string as durable primary key | `DOM-*` / `WEB-*` ids |
| Consumer `project_id` as `PRJ-*` | Project namespace separation ([ATLAS-IDENTIFIER-MODEL-v1.md](../../projects/atlas/foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.3) |

**Rule DUP-01:** If ATLAS has **no** canonical id yet, mark **SAFE UNKNOWN** — do not invent parallel canonical ids ([ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) CC-02).

**Rule DUP-02:** MIG **entity classification** (SERVICE_BRAND, AGGREGATOR, …) is **market taxonomy** — not ATLAS entity class.

---

## 8. Legacy situations

| Situation | Posture |
|-----------|---------|
| **Triumph ORCA** (`triumph-manipulator-krasnodar`, `ppc/triumph-manipulator/`) | Operational without ATLAS refs until operator adds **ATLAS context** section — **not** blocking legacy export work |
| **Triumph MIG pilot** (`incoming/mig/pilots/triumph-gruzotaxi-krasnodar/`) | Sessions valid as groundtruth; bind to `ORG-0004` + `PRJ-0005` when steward confirms — **retroactive bind allowed**, no re-capture required |
| **Triumph-era ORCA capture trees** | Legacy interpretation/evidence per [groundtruth-ownership-rule-v1.md](groundtruth-ownership-rule-v1.md) §6 — **not** ATLAS binding substitutes |
| **Website Factory FP-0001** | **Reference implementation** — already bound |
| **Pre-ATLAS population work** | Absent `atlas_*` fields = **SAFE UNKNOWN**, not proof that subject lacks ATLAS ids |
| **Makita (prep only)** | No ATLAS population in repo at rule authoring — bindings **deferred** until registration |

Legacy absence of bindings **does not** invalidate consumer artifacts. New work **should** bind when canonical ids exist.

---

## 9. Makita illustration (hypothetical — no entities created)

If Makita enters the ecosystem tomorrow:

| Layer | What should exist | Binding |
|-------|-------------------|---------|
| **ATLAS** | `ORG-*` Makita client org; `WEB-*` (+ optional `DOM-*`) for existing client site; `PRJ-*` for Makita PPC initiative — **human attested** | ATLAS owns ids |
| **MIG** | Research Session + Pack **only if** market research is chartered | `atlas_client_org_ref`, `atlas_project_ref`; optional `atlas_website_ref` |
| **ORCA** | `projects/orca/projects/<project-id>/` + `PROJECT.md` per [makita-lrl-pilot-v1.md](../../projects/orca/pilots/makita-lrl-pilot-v1.md) | Same RC-01 fields in **ATLAS context** section; `project_id` remains ORCA-local |
| **Cross** | ORCA LRL pilot may skip MIG if `landing_source = existing_client_website` | ORCA still binds ATLAS **business subject**; MIG binding **optional** unless groundtruth chartered |

Makita LRL pilot **does not require** MIG session for architectural validation — but **does require** ATLAS subject registration before durable cross-system references are meaningful.

---

## 10. Operator bind checklist

When creating or refreshing a consumer artifact:

1. Confirm ATLAS population docs for subject — active ids only, or SAFE UNKNOWN.
2. Set `atlas_client_org_ref` + `atlas_project_ref` matching **artifact scope** (not merely client brand).
3. Add `atlas_website_ref` / `atlas_domain_ref` when URL-scoped.
4. Record consumer-local ids (`session_id`, `project_id`) separately — never alias to `PRJ-*`.
5. For MIG → ORCA handoff, preserve both **pack pointer** and **aligned atlas_* refs**.
6. Do not copy legal/org graph into consumer docs.

---

## Related (non-normative detail)

| Topic | Document |
|-------|----------|
| Groundtruth ownership | [groundtruth-ownership-rule-v1.md](groundtruth-ownership-rule-v1.md) |
| ATLAS consumer permissions | [ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) |
| RC-01 field convention | [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](../../workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md) |
| MIG Research Pack | [mig-research-pack-contract-v0.md](../../projects/mig/contracts/mig-research-pack-contract-v0.md) |
| MIG → ORCA handoff | [mig-orca-handoff-contract-v0.md](../../projects/mig/contracts/mig-orca-handoff-contract-v0.md) |
| ORCA PROJECT.md | [project-md-contract-v0.md](../../projects/orca/projects/project-md-contract-v0.md) |
| Triumph ATLAS population | [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](../../projects/atlas/population/ATLAS-WAVE3-PROJECT-POPULATION-v1.md), [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](../../projects/atlas/population/ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) |

---

## Changelog

| Version | Date | Notes |
|---------|------|--------|
| v1 | 2026-06-07 | Initial rule from ATLAS / MIG / ORCA Relationship Audit — Entity Binding gap. |
