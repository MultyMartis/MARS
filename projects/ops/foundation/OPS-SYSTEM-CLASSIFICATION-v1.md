# OPS — System Classification v1

**Status:** **documented** — classification analysis for governance.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [OPS-SYSTEM-POSITIONING-v1.md](OPS-SYSTEM-POSITIONING-v1.md) · [../../../governance/system-entity-model.md](../../../governance/system-entity-model.md)  
**Is not:** registry row, topology edit, or naming authority for `project_id`.

---

## 1. Purpose

Determine **what OPS actually is** in MARS entity vocabulary, evaluate alternative labels, and state **what OPS is not** — to inform a future registration row and topology blurb.

---

## 2. Classification candidates

### 2.1 Business Operations Domain

| | |
|--|--|
| **Pros** | Matches pack README and OPERATIONAL-INDEX; plain language for operators; distinguishes from product lanes (ORCA, WPilot) |
| **Cons** | Not a literal row in [system-entity-model.md](../../../governance/system-entity-model.md) enum — needs mapping to “Program / Operational System” |
| **Fit score** | **9/10** |

### 2.2 Operational Support System

| | |
|--|--|
| **Pros** | Emphasizes support (not authority); aligns with mission “operational support, not authority domain” |
| **Cons** | Generic — could describe GitGuard, survivability, or ORCA support functions |
| **Fit score** | **7/10** |

### 2.3 Cross-Cutting Operational Layer

| | |
|--|--|
| **Pros** | Reflects consumption of ATLAS and citation of ORCA/MIG/etc. |
| **Cons** | Collides with **GitGuard** / IdeaBox patterns (registered cross-cutting **without** full program lifecycle); OPS has MVP, workflows, and case model — heavier than a layer |
| **Fit score** | **5/10** |

### 2.4 Program

| | |
|--|--|
| **Pros** | Exact [system-entity-model.md](../../../governance/system-entity-model.md) type **Program / Operational System**; consistent with `projects/ops/` layout |
| **Cons** | In MARS, “program” sometimes implies delivery factory (Factory, NOVA) — needs registry note clarifying back-office scope |
| **Fit score** | **8/10** (registry taxonomy) |

### 2.5 Infrastructure

| | |
|--|--|
| **Pros** | None material for OPS v1 |
| **Cons** | Implies shared runtime, APIs, or enforcement — **false** for documentation-only OPS |
| **Fit score** | **1/10** |

### 2.6 Service

| | |
|--|--|
| **Pros** | None for v1 |
| **Cons** | Implies deployable service, SLA, endpoints — contradicts README honesty |
| **Fit score** | **0/10** |

---

## 3. Final recommendation

| Field | Recommended value |
|-------|-------------------|
| **Human-facing classification** | **Business Operations Domain** |
| **MARS entity model mapping** | **Program / Operational System** |
| **Registry narrative (future)** | Human-supervised **operational back-office** documentation pack — reporting, document, approval, deadline workflows; **not** runtime, **not** CRM/ERP, **not** business identity SoT |
| **Suggested `phase` label (future row)** | **FOUNDATION** — Phases 1–4 complete; implementation **not started** |
| **Suggested `status` (future row)** | `planned` (align ATLAS/GitGuard doc-only precedent until pilot elevates operational claim) |

### 3.1 What OPS actually is

OPS is a **documentation-first program pack** that defines **human-supervised operational workflows and tracking semantics** for studio back-office work (monthly reporting MVP, expanded WF families, operational data model), **consuming** ATLAS for business identity and **referencing** product lanes only via operator-attested evidence.

### 3.2 What OPS is not

| OPS is not | Why |
|------------|-----|
| **ATLAS** or sub-registry of business reality | Identity and structure SoT remain ATLAS intent |
| **HomeGateway** or UI product | Cockpit surface ≠ workflow domain |
| **Cross-cutting survivability layer** | Not GitGuard/mars-survivability; different charter |
| **Infrastructure / Service / Runtime** | No in-repo execution engine claimed |
| **MetaBOT / ORCA / MIG / WPilot / OCPilot** | Does not own their execution or evidence domains |
| **CRM / ERP / Accounting / Legal system** | Hard exclusions in boundaries |
| **Orchestration platform** | Workflows are runbooks, not engines |

---

## 4. Registration shape (if Option A proceeds)

| Shape | Recommendation |
|-------|----------------|
| **`project_id`** | `ops` (stable, short, matches folder) |
| **Separate from ATLAS row** | Required — different SoT question (operational case vs business entity) |
| **GitGuard-style no-row** | **Not recommended** — OPS has bounded MVP and pack identity deserving `project_id` |

---

## 5. Answer to charter questions

| Question | Answer |
|----------|--------|
| Independent registered system? | **Yes — when registered** (preferred shape) |
| Internal domain under another system? | **No** |
| Deferred / not registered? | **Yes — current state** until pilot + registration execution pass |

---

*OPS System Classification v1 — classification only.*
