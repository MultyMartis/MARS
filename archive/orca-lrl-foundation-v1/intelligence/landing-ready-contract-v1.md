# ORCA Landing Ready Contract v1

## Status

**ARCHITECTURE FOUNDATION** — human-readable contract only (2026-05-30).

Part of [Landing Readiness Layer v1](landing-readiness-layer-v1.md).

**Not** JSON schema. **Not** automated validation. **Not** launch approval.

## Purpose

Define the **Landing Ready Contract (LRC)** — the single operator-maintained record that declares a landing route is **verified and eligible** for PPC URL assignment and ad ↔ landing continuity checks.

The LRC binds **identity**, **URL**, **deployed copy**, **CTA/forms**, **PPC alignment**, **readiness status**, and **provenance** in one human-readable document.

PPC JSON and export artifacts must reference an LRC in `approved` readiness status — not a semantic pack alone.

---

## Contract Shape

One LRC per **route** (one primary landing URL per PPC route). Recommended path:

```text
projects/orca/projects/<project-id>/artifacts/landing-readiness/lrc-<route_id>-v1.md
```

Alternative: section block in project `LANDING-ROUTES.md` if operator prefers single file — same fields required.

---

## Section 1 — Identity

**Purpose:** Stable reference for cross-layer linking (registry, PPC JSON, semantic pack, copy pack).

### Required fields

| Field | Description |
|-------|-------------|
| `contract_id` | Stable id, e.g. `lrc-<route_id>-v1` |
| `project_id` | Canonical ORCA project slug |
| `route_id` | Stable route slug (aligns with [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md)) |
| `route_label` | Human-readable route name |
| `page_type` | `master` \| `capability` \| `use-case` \| `b2b` \| `geo` \| `other` |
| `intent_group` | Intent tier / cluster from semantic strategy |
| `campaign_modes` | Which modes may use this route, e.g. `search` |

### Recommended fields

| Field | Description |
|-------|-------------|
| `semantic_pack_ref` | Path to upstream semantic content pack (if exists) |
| `copy_pack_ref` | Path to [Final Website Copy Pack](final-website-copy-pack-v1.md) |
| `family_id` | Route family label when part of multi-route set |
| `locale` | Primary language, e.g. `ru-RU` |

---

## Section 2 — URL

**Purpose:** Canonical click destination — the URL ads must use.

### Required fields

| Field | Description |
|-------|-------------|
| `landing_url` | Full HTTPS URL (production or declared staging) |
| `url_slug` | Path segment(s) without domain |
| `url_verified_at` | Date operator confirmed URL loads |
| `url_verified_by` | Operator identifier |

### Recommended fields

| Field | Description |
|-------|-------------|
| `display_url` | Yandex display path if different from landing path — **not** a substitute for `landing_url` |
| `registry_ref` | Link to `landing-route-registry.json` record if registry exists |
| `redirect_chain_notes` | If redirects exist — document final destination |
| `staging_url` | If production not yet live |

### Rules

- **Landing URL ≠ Display URL** — per [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md).
- URL changes require LRC update **before** PPC JSON / exporter update.
- If registry exists, `landing_url` must match registry `url` or document explicit divergence with operator rationale.

---

## Section 3 — Copy

**Purpose:** Approved **deployed** copy snapshot — what the user actually sees after click.

### Required fields

| Field | Description |
|-------|-------------|
| `copy_source` | `final_website_copy_pack` — path required |
| `hero_h1` | Live page H1 as verified |
| `hero_lead` | First-screen supporting copy (lead / subhead) |
| `primary_offer_framing` | Price / scope / capability framing visible on page |
| `copy_verified_at` | Date operator confirmed against live page |
| `copy_verified_by` | Operator identifier |

### Recommended fields

| Field | Description |
|-------|-------------|
| `section_snapshots` | Key sections (tasks, FAQ headline, trust block) — brief quotes or refs |
| `qualification_blocks` | Anti-junk / anti-broad copy present (yes/no + note) |
| `forbidden_claims_check` | Operator confirms no invented stats / fleet / guarantees |
| `copy_capture_method` | `manual_review` \| `screenshot_archive` \| `copy_pack_export` |

### Rules

- Copy fields reflect **deployed page**, not semantic pack draft.
- Semantic pack is traceability upstream — **not** SoT for this section.
- If copy pack and live page diverge, status cannot be `approved`; fix page or update copy pack first.

---

## Section 4 — CTA / Forms

**Purpose:** Verify click path and conversion surface match PPC and semantic CTA strategy.

### Required fields

| Field | Description |
|-------|-------------|
| `primary_cta_type` | `call` \| `form` \| `messenger` \| `mixed` |
| `primary_cta_label` | Visible label on primary CTA |
| `phone_visible` | yes / no / SAFE UNKNOWN |
| `form_present` | yes / no |
| `cta_verified_at` | Date verified |
| `cta_verified_by` | Operator identifier |

### Recommended fields

| Field | Description |
|-------|-------------|
| `secondary_cta` | Secondary action if present |
| `form_fields_summary` | Required fields count / types |
| `messenger_channels` | WhatsApp, Telegram, etc. |
| `mobile_cta_visible` | Primary CTA visible without excessive scroll on mobile (pass/fail/UNKNOWN) |

---

## Section 5 — PPC Alignment

**Purpose:** Explicit ad ↔ landing continuity declaration before export cites this route.

### Required fields

| Field | Description |
|-------|-------------|
| `ad_headline_alignment` | pass / fail / partial — hero H1 aligns with approved ad headline intent |
| `intent_tier_match` | pass / fail — page supports query intent tier from semantic strategy |
| `negative_space_respected` | pass / fail — page does not promise excluded scopes |
| `ppc_json_ref` | Path to PPC JSON instance when assigned (may be pending at draft) |
| `alignment_verified_by` | Operator identifier |

### Recommended fields

| Field | Description |
|-------|-------------|
| `target_ad_group_ids` | Group refs in PPC JSON |
| `approved_ad_headlines` | List or ref to ad copy artifact |
| `landing_qa_ref` | Link to [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md) QA record |
| `continuity_notes` | Known acceptable variance (semantic match, not byte-equal) |

### Rules

- **PPC must not rely on semantic pack alone** — alignment section cites copy pack + live verification.
- `partial` alignment requires explicit operator note and cannot combine with `approved` readiness unless note documents accepted variance.

---

## Section 6 — Readiness Status

**Purpose:** Gate PPC and launch consumers.

### Required fields

| Field | Description |
|-------|-------------|
| `readiness_status` | See status table below |
| `status_updated_at` | ISO date |
| `status_updated_by` | Operator identifier |
| `blocking_items` | List of open blockers (empty if `approved`) |

### Readiness statuses

| Status | Meaning | PPC may cite URL? |
|--------|---------|-------------------|
| `draft` | Contract started; verification incomplete | No |
| `needs_fix` | Verification failed; landing or copy fix required | No |
| `reviewed` | Human read; minor items may remain | No — unless explicitly noted partial |
| `approved` | All required sections verified; eligible for PPC JSON | Yes |
| `archived` | Superseded by newer LRC | Traceability only |

**Promotion to `approved`:** human only. All required fields in sections 1–5 must be populated or explicitly marked SAFE UNKNOWN where policy allows.

**Export READY vs Launch READY:**

- LRC `approved` satisfies **landing readiness for PPC URL assignment**.
- Launch still requires separate gates (campaign settings, tracking, operator sign-off) — see battle pilot launch checklist.

---

## Section 7 — Provenance

**Purpose:** Source-agnostic traceability — how this landing entered ORCA.

### Required fields

| Field | Description |
|-------|-------------|
| `landing_source` | Source type (see [landing-readiness-layer-v1.md](landing-readiness-layer-v1.md)) |
| `source_description` | Brief human description, e.g. client domain, Factory workspace path |
| `contract_created_at` | ISO date |
| `contract_version` | e.g. `v1` |

### Recommended fields

| Field | Description |
|-------|-------------|
| `factory_handoff_ref` | If source = `website_factory` — handoff doc path |
| `implementation_owner` | Who maintains the live page (client, agency, Factory, operator) |
| `last_deployment_date` | When page last changed |
| `supersedes` | Prior LRC id if replaced |
| `evidence_refs` | Screenshots, QA logs, capture session notes |

### Supported `landing_source` values (v1)

`website_factory` · `existing_client_website` · `existing_landing_page` · `wordpress` · `wpilot` · `tilda` · `manual_html`

---

## Ownership Model

| Role | Responsibility |
|------|----------------|
| **Operator (ORCA)** | Creates LRC, verifies sections, sets readiness status, blocks PPC if incomplete |
| **Semantic layer** | Provides upstream pack / brief — does not own LRC approval |
| **Landing source owner** | Client, Factory, or dev — maintains live page; notified when copy/URL drift breaks LRC |
| **PPC layer** | Consumes LRC in `approved` status; updates JSON refs; does not invent landing truth |
| **AI assist** | May draft LRC from capture session — default status `draft`; human promotes |

**Rule:** One named operator signs `approved`. No anonymous or AI-only approval.

---

## Evidence Expectations

LRC claims must be backed by capturable evidence or SAFE UNKNOWN — not inference.

| Claim type | Minimum evidence |
|------------|------------------|
| URL loads | Operator visit + date (`url_verified_at`) |
| Copy matches | Final Website Copy Pack + live page check |
| CTA / form | Operator visual check or QA checklist ref |
| PPC alignment | Explicit pass/fail against ad headlines / intent tier |
| Factory semantic lock | QA record when source = `website_factory` |

Recommended evidence storage:

```text
projects/orca/projects/<project-id>/artifacts/landing-readiness/evidence/<route_id>/
```

Evidence grades follow [evidence/evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md) when cross-referenced in project docs.

---

## SAFE UNKNOWN Policy

SAFE UNKNOWN is **valid** in LRC when verification is genuinely incomplete — not when the operator skipped review.

| Field state | Allowed? | Effect on readiness |
|-------------|----------|---------------------|
| Required field missing | No | Status stays `draft` or `needs_fix` |
| Recommended field UNKNOWN | Yes | Document in `blocking_items` if PPC-relevant |
| `phone_visible = SAFE UNKNOWN` | Yes | Cannot reach `approved` for call-first campaigns until resolved |
| `mobile_cta_visible = SAFE UNKNOWN` | Yes | Document risk; operator decides if `approved` acceptable |
| Analytics / conversion rate | Yes | Out of scope — do not invent |
| WPilot source semantics | Yes | Use `landing_source = wpilot` only with explicit future pilot charter |

**Forbidden:** Guessing hero copy from semantic pack without live page check. Filling `landing_url` from memory without load verification. Setting `approved` to unblock export when section 5 alignment is `fail`.

---

## Relationship to Other Contracts

| Document | Relationship |
|----------|--------------|
| [final-website-copy-pack-v1.md](final-website-copy-pack-v1.md) | Copy section cites approved copy pack |
| [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md) | URL section aligns with registry |
| [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md) | QA output feeds alignment and CTA sections |
| [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md) | Applies when `landing_source = website_factory` |
| [artifacts/approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md) | Launch gates remain separate from LRC `approved` |

---

## Boundary

Human-readable contract only. **No** JSON schema in v1. **No** automated enforcement. **No** runtime registry service.

PPC JSON structure changes, exporter patches, and validation-cli rules are **out of scope** for this document — they consume LRC status in future chartered work.
