# ORCA Final Website Copy Pack v1

## Status

**ARCHITECTURE FOUNDATION** — artifact type definition (2026-05-30).

Part of [Landing Readiness Layer v1](landing-readiness-layer-v1.md).

**Not** runtime. **Not** export automation. **Not** a semantic pack replacement.

## Purpose

Define the **Final Website Copy Pack (FWCP)** — an ORCA artifact that captures **approved deployed landing copy** as the user sees it after click.

FWCP is the mandatory bridge between semantic preparation and PPC work. It answers:

> What copy is **actually live** on this landing URL?

---

## Semantic Pack ≠ Final Website Copy Pack

These are **different artifact types** with different jobs. Confusing them caused the primary landing-readiness gap in Triumph Search Battle v1.

| Dimension | Semantic Content Pack | Final Website Copy Pack |
|-----------|----------------------|-------------------------|
| **When** | Before or during page creation | After page exists and is reviewable (live or staging) |
| **Content** | Intent, positioning, qualification, Factory constraints, differentiation | Deployed hero, sections, CTA labels, offer framing as verified |
| **Authority** | Semantic layer — ORCA meaning SoT for **creation** | Landing Readiness layer — deployed copy SoT for **PPC alignment** |
| **Source** | ORCA research + strategy | Live page capture (+ optional Factory build) |
| **PPC may cite?** | **No** — upstream input only | **Yes** — with human `approved` status |
| **Factory** | Primary input to MODE 1 build | Output of build **or** capture from any landing source |

```text
Semantic Pack          →  defines what SHOULD be built
Final Website Copy Pack →  records what IS deployed
```

**Battle rule (mandatory):**

> **PPC must not rely on semantic pack alone.** PPC should rely on **approved deployed copy** captured in Final Website Copy Pack and summarized in [Landing Ready Contract](landing-ready-contract-v1.md).

---

## Artifact Definition

### Type label

`final_website_copy_pack`

### Recommended location

```text
projects/orca/projects/<project-id>/artifacts/landing-readiness/copy-pack-<route_id>-v1/
```

Minimum files:

| File | Role |
|------|------|
| `COPY-PACK.md` | Structured copy snapshot (primary artifact) |
| `PACK-STATUS.md` | Lifecycle status + blockers |
| `SAFE-UNKNOWN.md` | Optional — unverified fields |

Optional: screenshot archive, capture session notes under `evidence/`.

### COPY-PACK.md minimum sections

1. **Meta** — `route_id`, `project_id`, `landing_url`, `landing_source`, `capture_date`
2. **Hero** — H1, lead, primary offer framing
3. **Qualification** — tasks / denied / scope blocks if present
4. **Trust** — review sources, ratings text, legal refs as visible
5. **CTA** — primary and secondary labels + types
6. **FAQ** — questions visible on page (headlines + brief answer refs)
7. **Footer / legal** — entity name, region, contacts if material to ads
8. **Drift notes** — explicit diff vs semantic pack if any (productive vs destructive)

---

## Inputs

| Input | Required? | Role |
|-------|-----------|------|
| Live or staging landing URL | **Yes** | Capture target |
| `route_id` + `project_id` | **Yes** | Identity |
| Semantic content pack (if exists) | Recommended | Traceability + drift comparison |
| [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md) output | Recommended when Factory built | QA evidence |
| Operator capture session | **Yes** | Human verification |
| Website Factory handoff | When `landing_source = website_factory` | Build provenance |

### Capture methods (v1 — human-operated)

| Method | When |
|--------|------|
| `manual_review` | Operator reads live page and transcribes key copy |
| `screenshot_archive` | Visual evidence stored alongside COPY-PACK.md |
| `copy_pack_export` | Structured export from Factory dist review (human-validated) |

Automated crawl / scrape helpers — **deferred** post-pilot. v1 is human capture only.

---

## Outputs

| Output | Consumer |
|--------|----------|
| Approved FWCP (`COPY-PACK.md` + `PACK-STATUS.md`) | [Landing Ready Contract](landing-ready-contract-v1.md) copy section |
| Drift notes vs semantic pack | Calibration layer, operator review |
| CTA / hero snapshot | PPC ad ↔ landing continuity checks |
| Evidence refs | QA records, launch gates |

FWCP does **not** directly produce XLSX or Commander rows. PPC JSON generation **reads** approved FWCP via LRC — not the semantic pack.

---

## Ownership

| Role | Owns |
|------|------|
| **Operator (ORCA)** | Capture, verification, `PACK-STATUS` promotion |
| **Semantic layer** | Upstream pack — may flag expected copy but does not approve FWCP |
| **Website Factory** | Implementation when engaged — produces page FWCP captures |
| **Client / site owner** | Live page when source ≠ Factory — operator coordinates access |
| **PPC layer** | Consumes via LRC — must not bypass FWCP gate |

---

## Lifecycle / Approval Expectations

Follows [artifacts/orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md) statuses:

```text
draft → reviewed → approved → production-ready → archived
```

| Status | Meaning for FWCP |
|--------|------------------|
| `draft` | Capture in progress; not cited by LRC |
| `reviewed` | Operator read; drift notes may remain |
| `approved` | Copy snapshot matches live page — may feed LRC |
| `production-ready` | Cleared for PPC JSON generation via LRC `approved` |
| `archived` | Superseded after page redeploy — new FWCP required |

### PACK-STATUS.md gates (recommended)

| Gate | Criterion |
|------|-----------|
| URL reachable | Landing URL loads |
| Hero captured | H1 + lead match live page |
| CTA captured | Primary CTA verified |
| Drift classified | Diff vs semantic pack noted or N/A |
| Human sign-off | Named operator + date |

**Redeploy rule:** Any material page change (hero, URL, CTA, offer framing) **invalidates** current FWCP. Create new version; archive prior pack.

---

## Relationship with Landing Ready Contract

| FWCP | LRC |
|------|-----|
| Artifact — detailed copy snapshot | Contract — gate record across URL, copy, CTA, PPC, provenance |
| `copy_pack_ref` in LRC points here | `copy_source` in LRC must reference approved FWCP |
| One per route per deployment generation | One per route; updated when FWCP superseded |

Workflow:

```text
FWCP approved → LRC sections 3–5 populated → LRC approved → PPC may cite route
```

LRC cannot reach `approved` without an FWCP at `approved` or `production-ready`.

---

## Relationship with PPC JSON

| Rule | Detail |
|------|--------|
| SoT hierarchy | FWCP (via LRC) > semantic pack for ad ↔ landing copy |
| JSON refs | PPC JSON should record `lrc_ref` and/or `copy_pack_ref` per route (field naming — future chartered) |
| URL assignment | `final_url` / landing URL must match LRC section 2 |
| Headline continuity | Ad headlines validated against FWCP hero — not semantic pack hero draft |
| Export gate | No export READY on route until LRC `approved` exists |

Triumph legacy JSON may lack explicit refs until migration — treat as **SAFE UNKNOWN** and do not assume parity for new projects.

**This document does not change** existing Triumph exporter or validation-cli behavior.

---

## Relationship with Website Factory

| Scenario | FWCP role |
|----------|-----------|
| Factory builds from semantic pack | After MODE 1 build reaches reviewable dist/staging, operator creates FWCP from **built page** |
| Factory not used | FWCP captured directly from client site — semantic pack optional |
| Factory drift | FWCP drift notes document destructive vs productive changes per calibration rules |
| Factory handoff | Handoff doc is **input** to build; FWCP is **output** verification |

Factory remains **implementation authority** when engaged. FWCP is how ORCA records that implementation landed correctly — regardless of whether Factory was the builder.

**Website Factory is not required** to produce FWCP. Any deployable URL with human-verified copy suffices.

---

## Battle Lesson (Canonical)

From [ORCA-LESSONS-LEARNED-v1.md](../freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md):

1. Semantic preparation packs define intent — they are **not** final landing copy.
2. Factory adds layout and visual constraints semantic packs don't carry.
3. PPC ad copy must be **validated against live landing URLs**.
4. Drift between semantic pack hero and deployed page breaks ad ↔ landing continuity.

**Operational sequence (v1):**

```text
Semantic pack → [landing source] → FWCP (approved) → LRC (approved) → PPC JSON
```

Skipping FWCP was acceptable only as battle-debt on frozen Triumph routes. **New work** (starting Makita pilot) must not skip.

---

## SAFE UNKNOWN

- Exact COPY-PACK.md template file layout beyond minimum sections — operator may extend per project
- Automated diff tooling — deferred
- Triumph route backfill schedule — deferred ([landing-readiness-layer-v1.md](landing-readiness-layer-v1.md))
- JSON field names for `copy_pack_ref` in PPC instance — deferred to PPC chartered task

---

## Related Documents

- [landing-readiness-layer-v1.md](landing-readiness-layer-v1.md) — layer architecture
- [landing-ready-contract-v1.md](landing-ready-contract-v1.md) — gate contract
- [content-packs/README.md](../content-packs/README.md) — semantic pack layer (upstream)
- [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md) — Factory lock when applicable
- [ORCA-LESSONS-LEARNED-v1.md](../freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md) — battle source

## Boundary

Artifact type definition only. **No** new exporters, **no** validation-cli rules, **no** content-pack schema changes in this v1 foundation package.
