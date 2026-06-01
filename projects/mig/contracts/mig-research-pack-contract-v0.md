# MIG Research Pack Contract v0

**Status:** **documented** — domain-level Source of Truth for MIG primary output.  
**Not:** workflow spec, JSON Schema registry, markdown template lock-in, ORCA analysis schema, or runtime product.

**Supersedes:** Treating `research_pack.draft.md`, Telegram summaries, or session folders as the domain object.  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) (intake); Research Session (execution unit — manifest + spine).  
**Downstream:** [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) (consumption minimum).

**Consumers (future, by reference only):** MIG Worker, MIG Admin, operator HITL UX, ORCA, future MARS runtime observers.

---

## 1. Purpose — What Research Pack is

### Definition

**Research Pack** is the **canonical domain object** that aggregates **evidence-grade market groundtruth** produced by a **Research Session**, with an **independent lifecycle**, explicit **SAFE UNKNOWN**, and **human approval** before downstream interpretation.

It is the **primary product of MIG (R1)** — not a side effect of capture tooling.

```text
Research Request
    ↓
Research Session
    ↓
Research Pack          ← this contract
    ↓
ORCA (R2)
```

| Layer | Role |
|-------|------|
| **Research Request** | Declares intent — **no** pack content |
| **Research Session** | Executes capture, normalization, draft assembly; owns `session_id`, manifest, raw artifacts |
| **Research Pack** | Versioned groundtruth product bound to one session (or explicit pack revision); **output** of session work |
| **ORCA** | Consumes **approved** pack via human handoff — **interprets**; does **not** own acquisition |

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

Research Pack carries **observations and evidence discipline** — not semantic clusters, campaign architecture, or site strategy.

### What Research Pack is not

| Anti-pattern | Why excluded |
|--------------|--------------|
| `research_pack.draft.md` (file alone) | **Representation** of pack content — not the object |
| `research_pack.json` (future file) | **Serialization** — not the object unless designated canonical form in a later schema version |
| Telegram message / chunk summary | **UX transport** — ephemeral |
| OpenRouter response body | **Synthesis transport** — never groundtruth SoT |
| Markdown session report | **Human report** — separate from pack contract |
| Session folder path | **Storage container** — not identity |
| `session_manifest.json` (whole file) | **Session execution SoT** — coordinates pack lifecycle but is not interchangeable with pack content |
| `serp_result.json` (alone) | **Normalized capture artifact** — pack **references** it |
| ORCA analysis output | **Downstream interpretation** — separate domain |
| Website Factory blueprint input | **Out of scope** — Factory consumes interpreted strategy via ORCA chain, not raw MIG sessions by default |

### Relationship to Research Request

- One **capture-type** Research Request binds to **one primary Research Session**, which produces **one primary Research Pack** (revision rules in §12).
- Request **`completed`** means session pipeline terminal success (e.g. `draft_complete`) — **not** pack **`approved`**.
- Request fields (`scope`, `queries`, `request_type`) **inform** pack scope and phase expectations; they are **copied or referenced** in pack metadata, not re-validated as intake at handoff.

### Relationship to Research Session

| Concern | Research Session | Research Pack |
|---------|------------------|---------------|
| Identity | `session_id` | `pack_id` (= `session_id` in v0; optional revision suffix in future) |
| Execution stage | `session_manifest.stage` (`intake_complete`, `collecting`, …) | `pack_state` (`draft`, `review`, …) — **independent** |
| SoT role | Execution, artifact paths, capture metadata | Groundtruth product semantics |
| Terminal (v0.1) | `draft_complete` | `draft` (auto-generated; HITL not automated) |

Session **creates** the pack. Pack **outlives** session execution in lifecycle terms (`approved` → `consumed` → `archived`).

### Relationship to ORCA

- ORCA receives **approved** Research Pack (logical object + required representations) via **human handoff only**.
- ORCA **must not** treat draft or review packs as production input.
- ORCA **must preserve** SAFE UNKNOWN and evidence grades through analysis — see [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) and §10.

### Relationship to Website Factory

- **No direct consumption** of Research Pack by Website Factory in bootstrap v1.
- Factory path: MIG → ORCA → strategy artifacts → Factory (R3).
- Factory **must not** read unapproved session folders or infer missing groundtruth from pack gaps.

### Relationship to future MARS Runtime

- Runtime may **submit** Research Requests and **observe** pack lifecycle flags — **must not** auto-approve packs or replace human `Approved By`.
- Runtime **must not** claim pack existence without MIG Worker / session folder evidence.
- Pack contract version (`pack_schema_version: "0"`) is the interoperability anchor — not runtime task envelopes.

---

## 2. Pack structure — canonical sections

Logical sections of the Research Pack object. A section may be **empty** only when explicitly allowed; gaps **must** appear in **SAFE UNKNOWN**, not as silent omission.

**Legend:** **R** = required when pack state ≥ `draft` for that phase · **O** = optional · **F** = future phase · **—** = not applicable in phase

| Section | Phase 1 (SERP) | Phase 2 (Competitors) | Phase 3 (Landing) | Phase 4 (Deep) | Notes |
|---------|----------------|-------------------------|-------------------|----------------|-------|
| **Pack Metadata** | R | R | R | R | Identity, version, phase, timestamps, linkage |
| **Scope** | R | R | R | R | From accepted request / manifest |
| **Query Set** | R | R | R | R | Seed + executed queries |
| **SERP Observations** | R | R | R | R | Normalized SERP groundtruth |
| **Competitor Observations** | — | R | R | R | Not designed in this contract — section **reserved** |
| **Landing Observations** | O¹ | O | R | R | ¹SERP-derived stubs only in Phase 1 |
| **Offer Observations** | O¹ | O | R | R | ¹Pattern lists from SERP normalization |
| **CTA Observations** | O¹ | O | R | R | ¹Pattern lists from SERP normalization |
| **Trust Observations** | — | O | R | R | Reviews, badges, policies — capture-time only |
| **Evidence Grades** | R | R | R | R | Session + per-section minimum |
| **SAFE UNKNOWN** | R | R | R | R | **Never empty** in `approved` state |
| **Artifact Registry** | R | R | R | R | Pointers to session files |
| **Approval Metadata** | —² | —² | —² | —² | ²Required when `pack_state ≥ approved` |
| **Consumption Metadata** | —³ | —³ | —³ | —³ | ³Required when `pack_state ≥ consumed` |

### 2.1 Pack Metadata (required)

| Field | Required | Meaning |
|-------|----------|---------|
| `pack_schema_version` | **Yes** | Contract version — `"0"` for this document |
| `pack_id` | **Yes** | Stable id — v0: same as `session_id` (`mig-YYYYMMDD-{hex6}`) |
| `session_id` | **Yes** | Owning session |
| `request_id` | **O** | Upstream intake id when persisted (v0.2+ target) |
| `request_type` | **O** | e.g. `serp_capture` — sets phase expectations |
| `mig_phase` | **Yes** | `1` \| `2` \| `3` \| `4` — highest phase **represented** in pack body |
| `pack_state` | **Yes** | Lifecycle state (§8) |
| `created_at` | **Yes** | Pack first materialized (ISO-8601 UTC) |
| `updated_at` | **O** | Last pack-affecting change |
| `operator_id` | **Yes** | Session operator |
| `source_summary` | **O** | Human-readable capture mode summary (e.g. SERP fallback) |

### 2.2 Scope (required)

Mirrors session scope — **not** reinterpreted by ORCA at intake:

| Field | Required |
|-------|----------|
| `niche` | **Yes** |
| `region` | **Yes** |
| `business_type` | **Yes** |
| `search_engine` | **Yes** |
| `device` | **Yes** |
| `city` | **O** |

### 2.3 Query Set (required)

| Field | Required |
|-------|----------|
| `seed_queries` | **Yes** — non-empty array |
| `queries_executed` | **Yes** — v0.1: single `query_used`; Phase 4: multi-query list |
| `query_notes` | **O** — locale, intent surface, operator notes (**no** semantic clustering) |

### 2.4 SERP Observations (required Phase 1+)

Structured groundtruth from normalized SERP — primary source: `serp_result.json`.

Minimum conceptual fields (v0.1 evidenced in spine):

- capture timestamp, `source_mode` (`manual` \| `provider` \| `fallback`)
- query, serp type, maps/local pack, ads summary
- aggregators, marketplaces, organic results (normalized list)
- embedded or referenced `safe_unknown` from capture

**Rule:** SERP body **must not** be invented by LLM at capture stage. Enrichment may **narrate** existing JSON — not replace missing fields.

### 2.5 Competitor Observations (required Phase 2+)

Competitor sets, domains, discovery audit, and snapshot references — methodology and object shape: [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md).  
Section appears when Phase 2 discovery pass exists; until then **must not** be fabricated in Phase 1 packs.

Phase 1: section **absent** or explicitly listed in SAFE UNKNOWN as «not in scope for Phase 1».

### 2.6 Landing / Offer / CTA / Trust Observations

| Section | Phase 1 | Later phases |
|---------|---------|--------------|
| **Landing** | Optional SERP-derived bullet stubs only (`landing_observations` in `serp_result.json`) | Required dedicated capture + snapshots (Phase 3) |
| **Offer** | Optional pattern list from SERP normalization | Required with evidence sources (Phase 3) |
| **CTA** | Optional pattern list from SERP normalization | Required with evidence sources (Phase 3) |
| **Trust** | **Future** — not required Phase 1–2 | Required Phase 3+ when trust capture implemented |

### 2.7 Evidence Grades (required)

See §5. Session-level grade **required** at `draft`. Per-section grades **required** for Phase 2+ when section is present.

### 2.8 SAFE UNKNOWN (required)

See §6. Standalone section — **mandatory** in every pack from `draft` onward.

### 2.9 Artifact Registry (required)

Machine-readable map of linked files — see §9. Minimum v0.1 entries:

| Artifact key | Typical path |
|--------------|--------------|
| `session_manifest` | `session_manifest.json` |
| `serp_result` | `serp_result.json` |
| `research_pack_draft` | `research_pack.draft.md` |
| `research_pack_review` | `research_pack.review.md` (when exists) |
| `research_pack_approved` | `research_pack.approved.md` (when exists) |
| `snapshots` | `snapshots/` directory (Phase 2+) |

### 2.10 Approval Metadata (required when `pack_state ≥ approved`)

| Field | Required |
|-------|----------|
| `approved_by` | **Yes** — human identifier |
| `approved_at` | **Yes** — ISO-8601 UTC |
| `approval_notes` | **O** |
| `reviewed_sections` | **O** — checklist of section ids human confirmed |

### 2.11 Consumption Metadata (required when `pack_state ≥ consumed`)

| Field | Required |
|-------|----------|
| `consumed_by` | **Yes** — ORCA operator or role id |
| `consumed_at` | **Yes** |
| `orca_project_ref` | **O** — opaque downstream handle |
| `consumption_notes` | **O** |

---

## 3. Phase evolution — section presence

Design goal: **stable section ids across phases** — new phases **populate** sections; they do **not** rename or replace the contract each wave.

| Section id | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|------------|---------|---------|---------|---------|
| `pack_metadata` | ✓ | ✓ | ✓ | ✓ |
| `scope` | ✓ | ✓ | ✓ | ✓ |
| `query_set` | ✓ | ✓ | ✓ | ✓ expanded |
| `serp_observations` | ✓ primary | ✓ | ✓ | ✓ |
| `competitor_observations` | — | ✓ | ✓ | ✓ |
| `landing_observations` | stub/O | O | ✓ | ✓ |
| `offer_observations` | stub/O | O | ✓ | ✓ |
| `cta_observations` | stub/O | O | ✓ | ✓ |
| `trust_observations` | — | O | ✓ | ✓ |
| `evidence_grades` | ✓ session | ✓ + sections | ✓ + sections | ✓ + sections |
| `safe_unknown` | ✓ | ✓ | ✓ | ✓ |
| `artifact_registry` | ✓ | ✓ + snapshots | ✓ | ✓ + memory refs |
| `approval_metadata` | on approve | on approve | on approve | on approve |
| `consumption_metadata` | on consume | on consume | on consume | on consume |

**Phase 1 v0.1 reality:** Worker produces `draft` pack with SERP section + SAFE UNKNOWN; competitor/trust sections absent; offer/CTA/landing may be «SAFE UNKNOWN» stubs when fallback mode — evidenced in session outputs.

**Phase 4 note:** Deep research **extends** query set, artifact registry, and SAFE UNKNOWN — **does not** introduce a separate «Deep Research Pack» type. Same object, higher `mig_phase`.

---

## 4. Evidence model

### 4.1 Philosophy

- Evidence describes **how** groundtruth was obtained — not how confident ORCA should be in a campaign bet.
- Grades are **coarse** — no fake numeric precision (no «0.87 confidence» at MIG layer).
- **LLM output is never evidence grade A.** Synthesis may assist narrative; it does **not** upgrade capture grade.
- When capture did not happen, grade is **`X` (not captured)** and item **must** appear in SAFE UNKNOWN — not omitted.

### 4.2 Evidence Grade (enum)

| Grade | Label | Meaning | Typical source |
|-------|-------|---------|----------------|
| **A** | `direct_observation` | Human observed surface directly; snapshot or reproducible note | Manual SERP, operator screenshot |
| **B** | `provider_capture` | Third-party SERP/crawl provider returned verifiable payload | SERP API with stored raw |
| **C** | `normalized_derivative` | Deterministic normalization of A/B payload | `serp_result.json` from provider/manual |
| **D** | `template_placeholder` | Spine/template filled without underlying capture | Fallback mode, empty organic list |
| **X** | `not_captured` | Explicit gap — no groundtruth | Must pair with SAFE UNKNOWN entry |

**Session-level grade** = **lowest** grade among **required** sections for that phase (pessimistic aggregate).

**Per-section grade** = worst grade of observations in that section.

### 4.3 Evidence Source

Structured attribution — **names and refs only**, no automation claims:

| Field | Meaning |
|-------|---------|
| `source_type` | `human` \| `serp_provider` \| `snapshot` \| `filesystem_artifact` \| `unknown` |
| `source_label` | Human-readable (e.g. «Yandex mobile SERP», operator id) |
| `artifact_ref` | Registry key or path |
| `observed_at` | ISO-8601 when observation occurred |

### 4.4 Evidence Confidence

**Excluded at MIG v0** as a numeric field. Use **grade + SAFE UNKNOWN** instead.  
ORCA may apply **analysis-time confidence** — separate layer; **must not** overwrite MIG grades in source artifacts.

### 4.5 Evidence Coverage

Qualitative enum — **not** percentage precision:

| Coverage | Meaning |
|----------|---------|
| `complete` | All required sections for phase captured at grade ≥ C |
| `partial` | Some required sections at D or X |
| `minimal` | Phase 1 fallback-only — draft for human capture planning |
| `unknown` | Operator has not assessed — use sparingly; prefer `partial` + SAFE UNKNOWN |

---

## 5. SAFE UNKNOWN model

### 5.1 Purpose

**SAFE UNKNOWN** is the **explicit gap register** — unknowns, blocked pages, inconclusive captures, and out-of-phase sections. It prevents silent inference downstream.

**Normative rule:**

> If groundtruth was not captured, the pack **must say so** in SAFE UNKNOWN — not leave empty sections or implied facts.

### 5.2 When required

| Pack state | Requirement |
|------------|-------------|
| `draft` | **Required** — non-empty array when any section is D/X or absent |
| `review` | **Required** — operator may add/clarify |
| `approved` | **Required** — ORCA handoff **rejects** if missing or empty while gaps exist |
| `published` / `consumed` | **Preserved** — must not be stripped |

### 5.3 What belongs

| Belongs | Does not belong |
|---------|-----------------|
| Uncaptured SERP/competitor/landing fields | ORCA semantic hypotheses |
| Provider failures, fallback mode | Campaign recommendations |
| Blocked URLs, consent walls | «Probably» market conclusions |
| Out-of-phase sections (Phase 1: no competitors) | LLM-filled placeholder facts |
| Operator notes on what to capture next | Intent cluster labels |

Each entry: **short declarative string** — optional `entry_id` in future schema.

**v0.1 evidenced pattern:** manifest `safe_unknown[]` + pack markdown section mirrored from `serp_result.safe_unknown`.

### 5.4 Who may edit

| Actor | `draft` | `review` | `approved`+ |
|-------|---------|----------|-------------|
| **MIG Worker** | Append (capture gaps) | — | — |
| **Operator** | — | Add, clarify, resolve→capture | Add **only** via revoke→review |
| **MIG Admin** | — | — | Revoke to `review` (audit) |
| **ORCA** | — | — | **Read-only** — never edit MIG artifacts |
| **LLM (Worker enrichment)** | Suggest gap **wording** only into `draft` | — | — |

Resolving an unknown: **new capture or human observation** → update observation section **and** remove or strike through unknown in `review` → re-approve.

### 5.5 How ORCA must treat SAFE UNKNOWN

1. **Preserve** all entries through R2 analysis — cite in output.
2. **Must not** collapse into confident marketing claims.
3. **Must not** infer missing SERP/competitor/landing facts to «complete» strategy.
4. **Must** escalate to human when analysis requires groundtruth in X/D sections marked critical.
5. May tag analysis-time «assumptions» — **separate** from MIG SAFE UNKNOWN list.

---

## 6. Pack lifecycle

### 6.1 States (validated)

Independent from `session_manifest.stage` and Research Request status.

```text
(none)
  ↓
draft          ← Worker auto-generates pack content
  ↓
review         ← Operator HITL edit / completeness check
  ↓
approved       ← Approved By recorded (mandatory for ORCA)
  ↓
published      ← Handoff marker — operator released bundle to ORCA pickup
  ↓
consumed       ← ORCA operator acknowledged intake
  ↓
archived       ← Retention / cold storage
```

**Terminal / branch states:**

| State | Meaning |
|-------|---------|
| `failed` | Pack assembly unrecoverable — session may partial |
| `revoked` | Approval withdrawn — returns to `review` (audit trail preserved) |

**v0.1 implemented today:** `draft` only (session `stage=draft_complete`). `review` → `approved` → … are **contract targets** — not automated in spine v0.1.

### 6.2 State definitions

| State | Entry | Owner | Allowed actions |
|-------|-------|-------|-----------------|
| `draft` | Worker finishes draft assembly | **MIG Worker** | Operator → promote to `review`; Admin → `failed` |
| `review` | Operator opens HITL | **Operator** | Edit representations; update SAFE UNKNOWN; → `approved` or back to `draft` (regenerate) |
| `approved` | Human `Approved By` | **Operator** | → `published`; Admin → `revoked` |
| `published` | Operator marks handoff ready | **Operator** | Deliver bundle to ORCA; → `consumed` when acknowledged |
| `consumed` | ORCA intake confirmed | **ORCA operator** (flag) / **Operator** (writes manifest) | → `archived` |
| `archived` | Retention policy | **MIG Admin** / operator | Read-only |
| `failed` | Pipeline error | **MIG Worker** / **Admin** | Retry via new session/request |
| `revoked` | Approval withdrawn | **MIG Admin** / approving operator | → `review` only |

### 6.3 Transition rules

| From | To | Authority | Condition |
|------|-----|-----------|-----------|
| `draft` | `review` | Operator | Session artifacts present |
| `draft` | `failed` | Worker/Admin | Unrecoverable assembly |
| `review` | `approved` | **Human operator only** | `approved_by` + `approved_at`; SAFE UNKNOWN present if gaps remain |
| `review` | `draft` | Operator | Regenerate from capture |
| `approved` | `published` | Operator | Handoff checklist complete |
| `published` | `consumed` | Operator + ORCA ack | Manual Phase 5 |
| `*` | `archived` | Admin/operator | After consumption or policy |
| `approved` | `revoked` | Admin / approver | Audit reason recorded |
| `revoked` | `review` | Admin / operator | Re-HITL |

**Forbidden transitions:**

- Worker → `approved` (never auto-approve)
- ORCA → any MIG pack state write
- `consumed` → `approved` without new approval cycle
- Request `completed` → skip to `approved` without HITL

### 6.4 SoT for `pack_state`

| Priority | Location |
|----------|----------|
| **Primary (target)** | `session_manifest.pack_state` |
| **Mirror** | Google Sheets `pack_state` column (runtime design — not v0.1) |
| **Representation hint** | Filename prefix `research_pack.{state}.md` |

On conflict: **manifest wins** over Sheets and filename alone.

**v0.1 gap:** manifest schema v0.1 lacks `pack_state` — implied `draft` when `research_pack.draft.md` exists and session `stage=draft_complete`.

---

## 7. Ownership model

| Stage / concern | Content owner | Approval owner | Consumption owner |
|-----------------|---------------|----------------|-------------------|
| `draft` | **MIG Worker** | — | — |
| `review` | **Operator** | — | — |
| `approved` | **Operator** (human-finalized) | **Operator** (`Approved By`) | — |
| `published` | **Operator** | **Operator** | — |
| `consumed` | **MIG** (immutable archive) | **Operator** (historical) | **ORCA operator** (ack) |
| `archived` | **MIG Admin** / retention policy | Historical record | Read-only all |
| SERP/competitor snapshots | **MIG** filesystem | — | ORCA read-only |
| Evidence grades at capture | **MIG** | Operator confirms at review | ORCA references |
| Semantic interpretation | — | — | **ORCA** only |
| Future MARS runtime | Submits requests; **observes** | **Never** auto-approves | **Never** consumes without ORCA charter |

**ORCA never owns:** pack content before consumption ack, capture artifacts, or approval authority.

---

## 8. Artifact model

### 8.1 Layering

```text
Research Pack (logical object)
    ├── references → session_manifest.json     (session + pack lifecycle SoT)
    ├── references → serp_result.json          (normalized SERP)
    ├── references → snapshots/*               (Phase 2+)
    └── represented as → research_pack.*.md    (human-readable)
                      → research_pack.json     (future canonical serialization)
```

### 8.2 Source of truth by concern

| Concern | SoT |
|---------|-----|
| Session execution stage | `session_manifest.stage` |
| Pack lifecycle state | `session_manifest.pack_state` (target) |
| SERP normalized body | `serp_result.json` |
| Pack narrative body (v0.1) | `research_pack.{state}.md` |
| Pack logical aggregate (future) | `research_pack.json` derived from sections §2 |
| SAFE UNKNOWN (authoritative list) | **Union** of manifest `safe_unknown[]` and pack section — **must stay in sync** at approval |
| Approval facts | manifest `approved_by`, `approved_at` + Approval Metadata section |
| Intake intent | Research Request (adapter/registry) — **not** rewritten in pack |

### 8.3 Artifact registry structure

Logical registry embedded in pack (future JSON) and mirrored in manifest `artifacts` (v0.1):

```json
{
  "session_manifest": { "path": "session_manifest.json", "role": "session_sot" },
  "serp_result": { "path": "serp_result.json", "role": "serp_normalized", "grade": "C" },
  "research_pack_draft": { "path": "research_pack.draft.md", "role": "representation_draft" },
  "snapshots": { "path": "snapshots/", "role": "evidence_files", "optional": true }
}
```

**Rules:**

- Registry lists **pointers** — not duplicated blob content.
- Each entry **may** carry `content_hash` (future) for handoff verification — not required v0.
- ORCA handoff bundle **includes** registry-listed files for approved state.

### 8.4 Revisions

- **Default:** one primary pack per `session_id`.
- **Revision (future):** `pack_revision` integer increment on re-capture within same session — requires operator charter; prior representations **archived**, not deleted silently.

---

## 9. ORCA consumption rules

Aligns with [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).

### 9.1 What ORCA receives

Minimum **handoff bundle** (human-delivered):

| Deliverable | Form |
|-------------|------|
| Approved pack representation | `research_pack.approved.md` |
| Session manifest | `session_manifest.json` with `pack_state=approved` |
| Normalized SERP | `serp_result.json` |
| Snapshots | `snapshots/` when present |
| SAFE UNKNOWN | Manifest + pack section |
| Evidence grades | Session + section grades per §4 |
| Approved By | Approval Metadata |

Logical Research Pack object = **aggregate** of the above — ORCA should treat bundle as one intake unit.

### 9.2 What ORCA may modify

| Allowed | Location |
|---------|----------|
| ORCA workspace analysis artifacts | ORCA-owned paths only |
| Consumption ack flag | Operator writes MIG manifest `consumed_*` — **not** ORCA writing into MIG session dir |

### 9.3 What ORCA must never modify

- `serp_result.json`, snapshots, draft/review/approved pack files in MIG session folder
- MIG evidence grades in source artifacts
- SAFE UNKNOWN entries in MIG artifacts

### 9.4 What ORCA must never infer

- Missing SERP rows, competitor sets, landing facts
- Semantic clusters or intent labels **as if** they were MIG observations
- Upgrade of evidence grade D/X to A/B without new MIG capture
- That `draft` or `review` packs are production-ready

### 9.5 Evidence grades at intake

- ORCA **reads** MIG grades — does **not** re-grade capture retroactively in MIG files.
- ORCA may map to analysis confidence — **downstream only**, clearly labeled.

### 9.6 SAFE UNKNOWN at intake

- Copy forward into R2 deliverables.
- Flag strategy gaps when critical unknowns block recommended actions.

---

## 10. Representations — not the object

| Artifact | What it is | Relationship |
|----------|------------|--------------|
| **Research Pack (object)** | Logical domain aggregate §1 | **Canonical** identity — `pack_id`, sections §2, lifecycle §6 |
| **Research Pack markdown** | `research_pack.{draft\|review\|approved}.md` | **Human-readable projection** — v0.1 primary editable form |
| **Research Pack JSON** | `research_pack.json` (future) | **Machine serialization** — target canonical interchange; generated from object |
| **Research Pack archive** | `.zip` / folder copy | **Distribution snapshot** — immutable at publish time |
| **Research Pack handoff bundle** | Curated file set for ORCA | **Consumption package** — subset per §9.1 |
| **Telegram summary** | Short message | **Notification only** |
| **Session folder** | `{MIG_SESSION_ROOT}/{session_id}/` | **Storage container** — holds representations + capture artifacts |

**Rules:**

1. Changing markdown **must** update logical sections or SAFE UNKNOWN consistently before `approved`.
2. Filename suffix `.draft` / `.approved` **reflects** `pack_state` — does not **define** it alone.
3. Future tooling may generate markdown **from** JSON — JSON becomes interchange SoT when schema v1 ships; **this contract v0** remains semantic authority until superseded.

**v0.1 evidenced mapping:** `buildResearchPackDraft()` produces markdown projection from manifest + `serp_result` — object is **implicit**, not serialized as JSON.

---

## 11. Compatibility

### 11.1 Research Request Contract

| Aspect | Alignment |
|--------|-----------|
| Chain | Request → Session → **Pack** → ORCA |
| Request `completed` | Does **not** imply pack `approved` |
| `request_type` | Sets phase and required sections §3 |
| Fields | Scope/queries copied into pack Scope / Query Set |

### 11.2 Task File Adapter

| Aspect | Alignment |
|--------|-----------|
| Output | Session folder with draft representation — pack `draft` state |
| Registry | `request_id` ↔ `session_id` links intake to `pack_id` |
| ORCA submit | Request only — not pack consumption |

### 11.3 Session Spine v0.1

| Aspect | Alignment |
|--------|-----------|
| Artifacts | manifest + serp + `research_pack.draft.md` |
| Stage | `draft_complete` → pack `draft` |
| SAFE UNKNOWN | `serp_result.safe_unknown` + manifest mirror |
| Gap | No `pack_state`, approval, or JSON serialization — contract targets |

### 11.4 ORCA Handoff Contract

| Handoff field | Pack section |
|---------------|--------------|
| Research Scope | Scope |
| Region | Scope.region |
| Date | Pack Metadata / SERP captured_at |
| Queries | Query Set |
| Evidence Sources | Evidence Source + Artifact Registry |
| Snapshots | Artifact Registry |
| Observations | SERP (+ future sections) |
| Evidence Grade | §4 |
| SAFE UNKNOWN | §5 |
| Approved By | Approval Metadata |

### 11.5 Runtime design report

Lifecycle states `draft` → `review` → `approved` → `published` → `consumed` → `archived` and filesystem layout **aligned** — this contract **normativizes** them as domain rules, not design suggestions.

### 11.6 Future MARS Runtime

- May observe `pack_state` read-only.
- Must use adapters for new requests — not direct session folder mutation.
- Pack approval remains **human** until explicit future charter says otherwise.

---

## 12. Explicit non-goals

This contract is **not**:

- Competitor discovery **implementation** (methodology: [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md))
- Deep research pipeline or memory schema
- ORCA automation or R2 methodology
- JSON Schema file for Research Pack (may follow in v0.1 schema wave)
- Markdown template lock-in — spine template is **one v0.1 representation**
- LLM enrichment rules (Worker concern — bounded by §4 grade caps)
- Website Factory or CMS integration
- Proof that approval workflow is implemented

---

## Related

| Document | Path |
|----------|------|
| Research Request | [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) |
| Competitor Discovery | [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) |
| Website Acquisition | [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) |
| Landing Analysis | [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md) |
| ORCA handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| Task File Adapter | [mig-task-file-adapter-spec-v0.1.md](mig-task-file-adapter-spec-v0.1.md) |
| Session manifest schema (v0.1) | [../schemas/session-manifest-v0.1.schema.json](../schemas/session-manifest-v0.1.schema.json) |
| SERP result schema (v0.1) | [../schemas/serp-result-v0.1.schema.json](../schemas/serp-result-v0.1.schema.json) |
| Session spine | [../lib/session-spine/](../lib/session-spine/) |
| Runtime design | [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| Runtime Assembly | [mig-runtime-assembly-v1.md](mig-runtime-assembly-v1.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |

---

*Contract v0 — documentation only. No implementation. No git commit by default.*
