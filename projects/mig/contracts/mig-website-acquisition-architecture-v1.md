# MIG Website Acquisition Architecture v1

**Status:** **documented** — domain-level architecture for MIG Website Acquisition (Phase 3 acquisition channel).  
**Not:** implementation, JSON Schema registry, crawler product, Playwright deployment, OpenRouter integration, landing **analysis** methodology, ORCA semantics, or runtime product.

**Supersedes:** Implicit «site capture» mentions in [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) §Website Acquisition Layer (this contract is the **normative** design for that channel).  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); Research Session; [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) (`competitors.json`).  
**Downstream:** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) (`landing_observations`, `offer_observations`, `cta_observations`, `trust_observations`); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).

**Consumers (future, by reference only):** MIG Worker (website acquisition pass), session spine, operator HITL UX, ORCA, future MARS runtime observers.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

Website Acquisition **captures visible page facts and structure**. It **must not** rank sites, score UX, judge conversion quality, recommend improvements, or create strategy.

---

## 1. Website Acquisition — definition

### 1.1 What Website Acquisition is

**Website Acquisition** is the MIG acquisition channel that **physically obtains public web page evidence** for URLs tied to a Research Session, **deterministically extracts observable facts** from the captured representation, and **persists versioned artifacts** that downstream normalization and Research Pack assembly **project** into pack observation sections.

```text
Research Request
    ↓
Research Session
    ↓
Search Acquisition (SERP)
    ↓
Competitor Discovery
    ↓
competitors.json
    ↓
Website Acquisition Pass          ← this architecture
    ↓
website_snapshots.json + snapshots/sites/*
    ↓
Research Pack (landing / offer / CTA / trust projections)
    ↓
ORCA (R2) — interprets captured facts
```

| Concern | Website Acquisition owns |
|---------|---------------------------|
| HTTP fetch (or operator import) of allowed URLs | **Yes** |
| Raw/archived page body storage | **Yes** |
| Response metadata (status, redirects, headers summary) | **Yes** |
| Deterministic extraction: title, meta, headings, links, visible text blocks | **Yes** |
| Observable contacts (phones, emails, visible addresses) | **Yes** — pattern extraction only |
| Visible offer/pricing **strings** (not validated commercial truth) | **Yes** |
| CTA elements (visible label + href) | **Yes** |
| Form surfaces (action, method, field names/labels as visible) | **Yes** |
| Per-URL capture status and SAFE UNKNOWN | **Yes** |
| Evidence grade at capture time | **Yes** |

### 1.2 What Website Acquisition is not

| Anti-pattern | Owner / reason |
|--------------|----------------|
| Landing **analysis** (positioning, funnel quality, persuasion) | **ORCA** — interpretation |
| UX scoring, conversion judgment, «best CTA» | **ORCA** — excluded |
| Site strategy, content architecture, semantic locks | **ORCA** |
| Unbounded site crawl / sitemap discovery | **Out of scope** — charter required for crawl products |
| LLM-invented page content at capture stage | **Forbidden** |
| Playwright/browser farm (MVP) | **Deferred** — Phase 2 selective only |
| OpenRouter / deep research synthesis | **Phase 4** — separate channel |
| Competitor **discovery** (who exists on SERP) | **Competitor Discovery** — upstream |
| Keyword strategy, intent clustering | **ORCA** |

### 1.3 Acquisition vs interpretation

| Layer | Question answered |
|-------|-------------------|
| **Acquisition (MIG)** | What was **visible** on the page at capture time? What structure existed (headings, forms, links)? What HTTP outcome occurred? |
| **Interpretation (ORCA)** | What does it **mean** for positioning, offers, trust, campaigns, and Factory-bound strategy? |

**Normative:** extracted `offers[]` and `pricing_signals[]` are **text observations**, not confirmed commercial offers. ORCA validates meaning; MIG does not.

### 1.4 Relationships

| Related capability | Relationship |
|--------------------|--------------|
| **Competitor Discovery** | **Upstream** — supplies `competitor_id`, domains, SERP URLs; Website Acquisition **does not** discover new market entities in MVP except via explicit operator URL seeds |
| **Research Pack** | **Downstream projection** — pack sections are **views**; artifacts remain SoT |
| **Landing Analysis** | **Downstream** — [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md); consumes `website_snapshot` artifacts; MIG-side **structuring** only (not strategy) |
| **Future Deep Research** | **Phase 4** — may **cite** snapshots; must not replace snapshot SoT or browse the open web by default |

---

## 2. Acquisition targets — evaluation and MVP scope

### 2.1 Page-type evaluation

| Target | Typical value | MVP | Phase 2 | Phase 3+ | Notes |
|--------|---------------|-----|---------|----------|-------|
| **Homepage** (`/` or registrable domain root) | Positioning hub, nav, primary CTA | **In** — **primary** | ✓ | ✓ | One per competitor domain default |
| **SERP landing URL** | Ad/organic destination | **In** — when distinct from homepage | ✓ | ✓ | Capture **instead of** or **in addition to** homepage only when operator/config allows; MVP default: **one URL per entity** |
| **Service pages** | Offer detail | **Out** | Selective (1–2 links from homepage) | Deeper link follow | Only URLs explicitly listed in acquisition plan |
| **Category pages** | Catalog breadth | **Out** | Optional niche charter | ✓ | E-commerce heavy niches |
| **Dedicated landing pages** | Campaign LPs | **Out** | If URL on SERP | ✓ | Same pipeline as any allowed URL |
| **Contact pages** | Contacts, forms | **Out** | Heuristic link from homepage nav | ✓ | Extraction often duplicated on homepage in RU sites |
| **Pricing pages** | Price tables | **Out** | If visible nav link text matches config patterns | ✓ | MVP: pricing **signals** on homepage only |

### 2.2 MVP scope (ruthless)

| Rule | Value |
|------|--------|
| **URLs per session (hard cap)** | **5** default; **10** maximum with operator charter flag on request |
| **URLs per competitor entity** | **1** — canonical entry URL (see §2.3) |
| **Crawl depth** | **0** — no link following in MVP |
| **Page roles captured** | `homepage` \| `serp_landing` \| `operator_seed` only |
| **Aggregators / informational entities** | **Skipped by default** — configurable; if captured, typed as observation only |

### 2.3 Canonical URL selection (per competitor)

Priority order — **first resolvable wins**; no guessing if ambiguous:

1. Operator `signals.capture_urls[]` entry matching `competitor_id` or domain  
2. Best SERP evidence `surface_detail.url` for that entity (normalized, same registrable domain)  
3. `https://{primary_domain}/` when `primary_domain` present  
4. If none: **no fetch** — `status: skipped` + SAFE UNKNOWN (no invented URL)

### 2.4 Phase 2+ expansion (non-MVP)

- Optional **second URL** per entity: `pricing` or `contact` only when discovered via **static** homepage link list (max +1 per entity, session cap still applies).  
- Operator multi-URL plan file in session folder (explicit list).  
- **Not** automatic sitemap or site-wide crawl.

---

## 3. Acquisition methods — evaluation matrix

Methods are **composable stages** in a pipeline, not mutually exclusive product names.

| Method | Advantages | Limitations | Cost | Complexity | MVP | Phase 2 | Long-term |
|--------|------------|-------------|------|------------|-----|---------|-----------|
| **A. HTTP fetch** | Cheap, fast, VPS-friendly, easy to archive | No JS rendering; bot blocks | Low | Low | **Primary** | Primary | Primary tier |
| **B. HTML parsing** | Robust structural parse (parse5/cheerio) | Invalid HTML, mixed encodings | Low | Low–medium | **Required** | ✓ | ✓ |
| **C. DOM extraction** | Selectors for title, meta, h1–h6, links, forms | Breaks on SPAs; layout-dependent | Low | Medium | **Required** (static DOM) | ✓ | ✓ |
| **D. Readability extraction** | Cleaner main text for excerpts | May drop pricing tables/nav | Low | Medium | **Out** | Optional enhancement | Default for text excerpts |
| **E. Playwright** | JS-rendered DOM; real user view | RAM, captcha, maintenance, timeouts | High (infra + ops) | High | **Out** | **Selective** (`render_required` only) | Hybrid tier 2 |
| **F. Screenshots** | Strong HITL evidence | Storage; not machine-searchable | Medium | Medium | **Out** | Optional per URL | Approved-pack audit |
| **G. Hybrid** | Static first; escalate on flags | Two pipelines to test | Mixed | High | **Out** (design only) | **Recommended** | **Default** |

### 3.1 MVP pipeline (normative)

```text
URL plan (from competitors + seeds)
    → HTTP GET (follow redirects, max 5)
    → store headers + raw HTML (artifact)
    → HTML parse + DOM extraction
    → Website Snapshot object + status
```

**No Playwright in MVP.** If body is empty or SPA shell detected → `render_status: js_shell` + SAFE UNKNOWN — **not** silent retry with browser.

### 3.2 Method selection rules (future)

| Condition | Next step |
|-----------|-----------|
| `http_status` 2xx + substantive static body | Snapshot complete |
| Empty body or root-only `<div id="app">` | `render_status: js_shell`; Phase 2: operator or Playwright charter |
| 403/429/503 | `status: blocked` — no guess content |
| Timeout | `status: timeout` |
| Redirect to different registrable domain | Record `final_url` + flag cross-domain redirect in SAFE UNKNOWN |

---

## 4. Website Snapshot — canonical object

Logical object persisted per captured URL. Future schema: `schemas/website-snapshot-v0.1.schema.json`.

### 4.1 Identity and linkage

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `snapshot_id` | **Yes** | string | `{session_id}-ws{seq}` e.g. `mig-20260601-a1b2c3-ws001` |
| `session_id` | **Yes** | string | Owning session |
| `competitor_id` | **O** | string \| null | Link to `competitors.json` entity; null for operator-only URLs |
| `domain` | **Yes** | string | Registrable domain of `final_url` |
| `requested_url` | **Yes** | string | URL before fetch |
| `final_url` | **Yes** | string | URL after redirects |
| `page_role` | **Yes** | enum | `homepage` \| `serp_landing` \| `contact` \| `pricing` \| `service` \| `category` \| `landing` \| `operator_seed` \| `unknown` |
| `capture_time` | **Yes** | ISO-8601 UTC | Fetch completion time |

### 4.2 Acquisition outcome

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `status` | **Yes** | enum | `success` \| `failed` \| `blocked` \| `timeout` \| `empty` \| `skipped` \| `render_required` |
| `acquisition_method` | **Yes** | enum | `http_get` \| `http_get_dom` \| `playwright` \| `manual_import` |
| `http_status` | **O** | integer \| null | Final response status |
| `redirect_chain` | **O** | string[] | Ordered URLs visited |
| `content_type` | **O** | string | Final `Content-Type` |
| `charset` | **O** | string | Detected/declared charset |
| `render_status` | **Yes** | enum | `static_ok` \| `static_empty` \| `js_shell` \| `unknown` |
| `fetch_duration_ms` | **O** | number | Observability |
| `robots_hint` | **O** | string | Only if `meta name=robots` or obvious header — **no** robots.txt fetch in MVP |

### 4.3 Extracted visible facts (deterministic only)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `title` | **O** | string \| null | `<title>` text |
| `meta_description` | **O** | string \| null | `meta description` content |
| `canonical_url` | **O** | string \| null | `link rel=canonical` href if absolute/resolvable |
| `lang` | **O** | string \| null | `<html lang>` |
| `headings` | **Yes** | array | `{level: 1–6, text, order}` — document order, capped (e.g. 50) |
| `contacts` | **Yes** | object | See §4.4 |
| `offers` | **Yes** | array | See §4.5 |
| `pricing_signals` | **Yes** | array | See §4.6 |
| `cta_elements` | **Yes** | array | See §4.7 |
| `forms` | **Yes** | array | See §4.8 |
| `links` | **Yes** | object | `{internal: [], external: []}` capped (e.g. 200 each) |
| `trust_signals_visible` | **Yes** | array | Visible badge/review **text** snippets — not sentiment |
| `visible_text_excerpt` | **O** | string | First N chars of body text — optional MVP |

**Normative:** all string fields are **verbatim or normalized whitespace only** — no summarization, no translation, no «cleaned marketing copy» at acquisition.

### 4.4 `contacts` object

| Subfield | Type | Extraction rule |
|----------|------|-----------------|
| `phones` | string[] | Regex / `tel:` href — dedupe |
| `emails` | string[] | Regex / `mailto:` — dedupe |
| `addresses` | string[] | Visible `<address>` or schema.org PostalAddress text only — **no** geocoding |
| `messengers` | object[] | `{type, handle}` for visible `t.me`, `wa.me`, viber links |

Empty arrays are valid — **not** failure unless capture was required and contacts were operator-critical (then SAFE UNKNOWN only).

### 4.5 `offers[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `text` | **Yes** | Visible offer phrase (heading, list item, card title) |
| `context` | **O** | Nearest heading or section id/class — audit only |
| `source_selector_hint` | **O** | Non-stable hint for re-fetch debug |

### 4.6 `pricing_signals[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `text` | **Yes** | Visible price string as on page |
| `currency_hint` | **O** | `RUB`, `USD`, etc. — regex only, no FX |
| `context` | **O** | Surrounding visible label |

**Missing pricing** is **not** an error — record empty array + optional SAFE UNKNOWN «no pricing visible on captured page».

### 4.7 `cta_elements[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `text` | **Yes** | Visible label |
| `href` | **O** | Resolved href if `<a>` or button-associated link |
| `element_type` | **O** | `link` \| `button` \| `input` |
| `position_hint` | **O** | `header` \| `hero` \| `footer` \| `unknown` — heuristic only |

### 4.8 `forms[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `form_id` | **O** | DOM id |
| `action` | **O** | action URL |
| `method` | **O** | get/post |
| `fields` | **Yes** | `{name, type, label, required}` from visible labels/placeholders |
| `visible_purpose` | **O** | Nearest heading text — **not** «lead gen quality» |

### 4.9 Evidence and artifacts

| Field | Required | Meaning |
|-------|----------|------|---------|
| `artifact_refs` | **Yes** | Map keys → paths under session (§5) |
| `evidence_grade` | **Yes** | A \| B \| C \| D \| X per Research Pack §4 |
| `safe_unknown` | **O** | Snapshot-level gaps |
| `acquisition_notes` | **O** | Operator notes |

### 4.10 Evidence grades (website capture)

| Grade | When |
|-------|------|
| **A** | `manual_import` — operator pasted HTML or uploaded capture with attestation |
| **B** | Successful HTTP with archived raw HTML in `snapshots/sites/` |
| **C** | Successful HTTP but raw archive omitted (extract-only mode — discouraged) |
| **D** | Partial extract on error body / degraded parse |
| **X** | `skipped`, `failed`, `blocked`, `timeout` with no usable body |

### 4.11 Session-level index: `website_snapshots.json`

Wrapper persisted at session root:

| Field | Required | Meaning |
|-------|----------|------|---------|
| `schema_version` | **Yes** | `"0.1"` |
| `session_id` | **Yes** | Session |
| `generated_at` | **Yes** | ISO-8601 |
| `acquisition_phase` | **Yes** | `3` for this architecture |
| `url_plan` | **Yes** | Ordered list `{snapshot_id, competitor_id, requested_url, page_role}` |
| `snapshots` | **Yes** | Array of **summary** or embedded full snapshots (implementation choice; full objects may live only under `snapshots/sites/{snapshot_id}/website_snapshot.json`) |
| `session_coverage` | **Yes** | `complete` \| `partial` \| `minimal` \| `unknown` |
| `section_evidence_grade` | **Yes** | Worst grade among snapshots |
| `safe_unknown` | **O** | Session-level gaps |

---

## 5. Acquisition artifacts — strategy

**Principle:** Artifacts = **source of truth**. Research Pack = **projection**.

### 5.1 Required (MVP)

| Artifact | Path | Role |
|----------|------|------|
| Session index | `website_snapshots.json` | Snapshot list, coverage, grades |
| Canonical snapshot | `snapshots/sites/{snapshot_id}/website_snapshot.json` | Full Website Snapshot object |
| Raw page body | `snapshots/sites/{snapshot_id}/page.html` | Audit / re-parse |
| Response metadata | `snapshots/sites/{snapshot_id}/headers.json` | Status, headers subset, redirect chain, timing |

### 5.2 Optional (MVP)

| Artifact | Path | When |
|----------|------|------|
| Extracted links | `snapshots/sites/{snapshot_id}/links.json` | When link count > threshold for pack excerpt |
| Operator import bundle | `snapshots/sites/{snapshot_id}/manual_import.json` | `acquisition_method: manual_import` |
| Fetch log | `snapshots/sites/{snapshot_id}/fetch.log` | Debug |

### 5.3 Future (Phase 2+)

| Artifact | Path | When |
|----------|------|------|
| Screenshot | `snapshots/sites/{snapshot_id}/page.png` | Playwright or operator capture |
| Rendered DOM | `snapshots/sites/{snapshot_id}/dom.html` | Post-Playwright |
| Readability text | `snapshots/sites/{snapshot_id}/readable.txt` | Phase 2 extract |
| MHTML/PDF archive | `snapshots/sites/{snapshot_id}/archive.mhtml` | Long-term audit |
| Per-domain rate-limit state | `acquisition_state.json` | Cross-session politeness (optional service) |

### 5.4 Naming and registry

- Register in `session_manifest.artifacts.website_snapshots` → `website_snapshots.json`.  
- Per-snapshot folder registered in snapshot’s `artifact_refs`.  
- **No duplication** of full `page.html` inside pack markdown.

### 5.5 Retention

- Raw HTML retained for session lifetime; archival policy = operator/MIG Admin — **not** defined here.

---

## 6. Research Pack integration

### 6.1 Projection model

Website Acquisition **does not** introduce a separate top-level pack section id in v0. It **feeds** existing Phase 3 sections:

| Pack section | Projected from snapshot fields |
|--------------|-------------------------------|
| `landing_observations` | `title`, `meta_description`, `headings`, `visible_text_excerpt`, `page_role`, `final_url` |
| `offer_observations` | `offers[]` |
| `cta_observations` | `cta_elements[]` |
| `trust_observations` | `trust_signals_visible`, visible review widget text |

**Human-readable umbrella (markdown only):** `## Website capture summary` — table of `snapshot_id`, competitor, URL, status, grade — **not** SoT.

### 6.2 What enters the pack

| Enters pack (excerpt) | Stays in artifacts only |
|-----------------------|-------------------------|
| Snapshot summary table | Full `page.html` |
| Top N headings per entity | Full `links` lists |
| Offer/CTA/pricing **strings** (capped) | Raw headers dump |
| Contact phones/emails (deduped session-level) | Selector hints |
| Per-entity `snapshot_id` refs | Fetch logs |
| Session `section_evidence_grade` | |

**Cap guidance (MVP):** max **5** offer strings, **5** CTA items, **5** pricing signals per snapshot in pack projection — full arrays remain in artifact.

### 6.3 Competitor cross-links

Per [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) §10.2:

| Competitor field | Value |
|------------------|-------|
| `landing_evidence_refs[]` | `{snapshot_id, url, page_role, evidence_grade}` |

Discovery contract fields are **appended** after acquisition pass — discovery pass does not wait for snapshots.

### 6.4 `mig_phase` and section presence

| Condition | Pack behavior |
|-----------|---------------|
| ≥1 snapshot `status: success` with grade ≤ C | `mig_phase` ≥ `3`; populate landing/offer/cta sections with refs |
| All snapshots X/D or skipped | Sections absent or minimal + **mandatory** SAFE UNKNOWN |
| Mixed success/failure | Partial sections + per-entity gaps in SAFE UNKNOWN |

### 6.5 Duplication avoidance

1. **SERP snippets** stay in `serp_observations` — pack may **reference** SERP url; do not copy full SERP body into landing section.  
2. **Competitor names/domains** stay in `competitor_observations` — landing section references `competitor_id`.  
3. Pack markdown **must** include `artifact_registry.website_snapshots` when acquisition ran.

### 6.6 LLM enrichment (out of scope for acquisition)

Pack builder or Worker may **narrate** existing snapshot JSON in draft markdown — **must not** add facts not in artifacts. LLM output grade capped at **C** derivative per Research Pack §4.

---

## 7. SAFE UNKNOWN — behavior (no guessing)

### 7.1 Capture outcome → status mapping

| Situation | `status` | `render_status` | Pack / SAFE UNKNOWN action |
|-----------|----------|-----------------|----------------------------|
| DNS / connection error | `failed` | `unknown` | «Site unreachable: {url}» |
| HTTP 403/429/451 | `blocked` | `unknown` | «Blocked or forbidden: {http_status}» |
| HTTP 5xx | `failed` | `unknown` | «Server error: {http_status}» |
| Timeout | `timeout` | `unknown` | «Fetch timeout: {url}» |
| 2xx but zero-length body | `empty` | `static_empty` | «Empty response body» |
| SPA shell / no text | `render_required` | `js_shell` | «JavaScript-rendered page — static capture insufficient» — **no** Playwright in MVP |
| No URL for competitor | `skipped` | `unknown` | «No resolvable URL for competitor {id}» |
| Pricing not on page | `success` | `static_ok` | Optional entry: «No pricing signals visible» — **not** «no pricing exists» |
| Contacts not on page | `success` | `static_ok` | Optional entry: «No contacts visible on captured page» |
| Redirect off-domain | `success` or `failed` | per body | «Redirected to {final_url} — different registrable domain» |
| Charset garbage | `success` | `unknown` | «Encoding ambiguous — extract may be incomplete» |

### 7.2 Forbidden inference

| Forbidden | Required instead |
|-----------|------------------|
| Invent phone/email not in HTML | Empty `contacts` + SAFE UNKNOWN |
| Infer «from» price from stale JSON-LD if parse fails | Omit or D-grade with note |
| Assume homepage is `/` when domain unknown | `skipped` |
| Mark acquisition success when `http_status` is 4xx | `failed` unless operator override import |
| Fill offer section from SERP snippet alone | SERP stays in SERP section; website section X until fetch |

### 7.3 Session-level mandatory entries

| Case | Example SAFE UNKNOWN string |
|------|------------------------------|
| Website pass not run | «Website acquisition not executed — Phase 3 capture pending» |
| Partial URL plan | «Website capture partial: 2/5 competitors skipped (no URL)» |
| All blocked | «All website fetches blocked — no landing observations captured» |
| Rate limit halted session | «Acquisition halted after 429 — remaining URLs not fetched» |

---

## 8. MVP execution model

Aligned with [REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) and existing session spine.

### 8.1 Runs in n8n (orchestration)

| Concern | Role |
|---------|------|
| **MIG Worker route** | Trigger website pass after `competitors.json` exists |
| **Stage updates** | `session_manifest.stage` → `acquiring_sites` → `draft_complete` |
| **Telegram / Sheets** | Status messages, operator approval to proceed with N URLs |
| **Locks / caps** | Enforce max URLs before spawn |
| **Thin Code node** | `require()` spine module; pass `sessionRoot` |

### 8.2 Runs in JS modules (`projects/mig/lib/`)

| Module (proposed) | Responsibility |
|-------------------|----------------|
| `website-acquisition/build-url-plan.js` | Deterministic URL plan from `competitors.json` + request `signals` |
| `website-acquisition/fetch-page.js` | HTTP GET, redirect policy, rate delay |
| `website-acquisition/extract-snapshot.js` | Parse HTML → Website Snapshot fields |
| `website-acquisition/write-artifacts.js` | Persist §5 layout |
| `website-acquisition/run-website-pass.js` | Orchestrate plan → fetch → extract → index |
| `session-spine/build-research-pack.js` | **Extend** — project snapshot index into pack sections |

**Pattern:** same as `competitor-discovery/` — unit-testable, invoked from CLI (`node run-website-pass.js {session}`) and n8n.

### 8.3 Runs outside n8n

| Concern | Where |
|---------|--------|
| **Task File Adapter** | Intake only — may declare `request_type` implying website pass later |
| **Operator manual import** | Drop `page.html` + `manual_import.json` into snapshot folder |
| **Playwright service (Phase 2+)** | Optional `127.0.0.1` microservice — **not** MVP |
| **ORCA** | Read-only consumption after approval |

### 8.4 n8n anti-patterns (website)

| Do not | Why |
|--------|-----|
| Long fetch loops in graph nodes | Timeouts; no tests |
| HTML parsing in Code node | Memory; versioning |
| Playwright in n8n | Process isolation failure |
| OpenRouter on raw HTML | Violates acquisition boundary |

### 8.5 Request types (intake)

| `request_type` | Website pass |
|----------------|--------------|
| `serp_capture` | **Off** |
| `competitor_discovery` | **Off** (MVP) — optional Phase 2 flag `acquire_websites: false` |
| `groundtruth_run` | **On** when SERP + competitors complete |
| Future `website_capture` | **On** — primary |

---

## 9. Operator workflow — canonical flow

```text
1. Submit Research Request
      (scope, seeds, request_type: groundtruth_run)
        ↓
2. Capture SERP
      (provider or manual_serp → serp_result.json)
        ↓
3. Review SERP coverage (HITL)
        ↓
4. Competitor Discovery (automatic)
      → competitors.json
        ↓
5. Review competitor set (HITL)
      optional: signals.capture_urls[], exclude entities
        ↓
6. Website Acquisition (automatic, capped)
      → website_snapshots.json + snapshots/sites/*
        ↓
7. Review capture summary (HITL)
      flag render_required URLs for Phase 2; manual_import if blocked
        ↓
8. Research Pack draft
      → research_pack.draft.md (projections + SAFE UNKNOWN)
        ↓
9. review → approved → ORCA handoff (human)
```

### 9.1 MVP shortcut path

```text
task file → spine (SERP fallback) → competitors (may be empty)
  → skip website pass OR 1 manual import snapshot
  → draft pack with explicit SAFE UNKNOWN
```

### 9.2 Workload controls

| Control | Default |
|---------|---------|
| Max URLs / session | 5 |
| Inter-request delay same host | 3 s |
| Global concurrent fetches per session | 1 (sequential MVP) |
| Timeout per URL | 30 s |

---

## 10. Implementation roadmap

### 10.1 MVP (build first)

| # | Deliverable | Acceptance |
|---|-------------|------------|
| 1 | `build-url-plan.js` | Plan from competitors + seeds; skips documented |
| 2 | `fetch-page.js` + `extract-snapshot.js` | HTTP + DOM; no Playwright |
| 3 | Artifact writer §5 | Index + per-snapshot folder |
| 4 | `verify-website-acquisition-v0.mjs` | Golden HTML fixtures |
| 5 | Spine hook after competitor discovery | `groundtruth_run` only |
| 6 | Pack projection (landing/offer/cta/trust excerpts) | No invented facts |
| 7 | Operator doc: manual_import path | Blocked-site workaround |

**MVP success:** One session with ≥1 successful snapshot linked to a competitor, draft pack shows projected sections + grades + SAFE UNKNOWN for failures.

### 10.2 Phase 2

| Item | Notes |
|------|-------|
| Selective **Playwright** | Only `render_status: js_shell` from MVP |
| Optional **screenshot** | `page.png` per snapshot |
| **Readability** extract | `readable.txt` |
| Second URL (pricing/contact) | Static homepage link discovery |
| `keyword_surface` from `page_visible` | Feeds keyword surface channel |
| n8n Worker production route | Wired with caps + Telegram |

### 10.3 Phase 3

| Item | Notes |
|------|-------|
| Hybrid default pipeline | HTTP → Playwright escalation service |
| Multi-page plans per entity | Explicit operator plan file |
| Full-page archive (MHTML/PDF) | High-value approved sessions |
| Cross-session rate-limit service | Politeness registry |
| Landing Analysis Phase 2+ blocks | See [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md) §10.2 |

### 10.4 Explicitly out of scope (all phases unless new charter)

- Site-wide crawl, sitemap bots, SEO spider APIs  
- UX/conversion scoring in MIG  
- OpenRouter content extraction at capture  
- ORCA handoff automation changes  
- Website Factory direct consumption of snapshots  

---

## 11. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **WA-01** | Website Acquisition is a **channel**, not Landing Analysis | Separates fetch from ORCA interpretation |
| **WA-02** | **One URL per competitor** in MVP | Ruthless scope; avoids crawl creep |
| **WA-03** | **HTTP + DOM only** in MVP | Matches data acquisition report; VPS-friendly |
| **WA-04** | **No Playwright in MVP** | Cost/complexity; `render_required` flags Phase 2 |
| **WA-05** | **Website Snapshot** is artifact SoT; pack sections are projections | Research Pack contract layering |
| **WA-06** | No new entities from website pass in MVP | Discovery stays SERP-derived |
| **WA-07** | Empty pricing/contacts = valid success + optional UNKNOWN | No guessing missing facts |
| **WA-08** | Sequential fetch, per-host delay | Politeness + debuggability |
| **WA-09** | JS modules acquire; n8n orchestrates | MetaBOT / spine pattern |
| **WA-10** | Competitor `landing_evidence_refs[]` populated post-acquisition | Stable competitor_id |

---

## 12. Risks

| Risk | Mitigation |
|------|------------|
| Bot blocking / 403 | Status `blocked` + manual_import; no fake body |
| SPA-heavy sites | `render_required`; Phase 2 Playwright selective |
| Legal/ToS for automated fetch | Human charter; public pages only; operator accountability |
| Storage growth (HTML) | Per-session caps; optional gzip (implementation) |
| Extract false phones (IDs as phones) | Conservative regex; operator review at HITL |
| Duplication SERP vs landing | Projection rules §6.5 |
| Agent drift (invented offers) | Schema validation; verify script; no LLM on capture |

---

## 13. Implementation readiness — proposed artifacts

| Artifact | Path (proposed) |
|----------|-----------------|
| Website Snapshot JSON Schema | `schemas/website-snapshot-v0.1.schema.json` |
| Session index schema | `schemas/website-snapshots-v0.1.schema.json` |
| Acquisition config | `config/website-acquisition-rules-v0.json` (caps, delays, skip types) |
| Library | `lib/website-acquisition/*` |
| Verifier | `tools/verify-website-acquisition-v0.mjs` |
| Test fixtures | `test/fixtures/website-html/*.html` |
| Pack builder extension | `lib/session-spine/build-research-pack.js` |

**Not required before coding MVP slice:** Playwright, screenshots, OpenRouter, n8n export.

---

## 14. Explicit non-goals

- Implementation, deployment, provider API keys  
- Playwright installation or browser farm  
- OpenRouter / LLM extraction at capture  
- Landing Analysis methodology or ORCA redesign  
- Crawling framework or sitemap products  
- Website scoring, ranking, strategy generation  
- Proof that website pass exists in repo  

---

## Related

| Document | Path |
|----------|------|
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| Competitor Discovery | [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) |
| Data Acquisition (overview) | [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) |
| Runtime design | [REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |
| Session spine | [../lib/session-spine/](../lib/session-spine/) |

---

*Architecture v1 — documentation only. No implementation. No git commit by default.*
