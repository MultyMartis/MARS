# MIG Reality Acquisition Model v1

**Status:** **documented** — normative design for MIG Enhancement Charter (Reality Acquisition Model).  
**Not:** runtime implementation, Playwright deployment, SERP provider integration, or automated review generation.

**Date:** 2026-06-04  
**Lane:** B — MIG Reality / Evidence Architecture  
**Supersedes:** Implicit trust/evidence layering scattered across acquisition reports and pilot checklists (this contract is the **normative** reality stack).  
**Related:** [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) (channel topology); [mig-deep-research-architecture-v1.md](mig-deep-research-architecture-v1.md) (R4-aligned synthesis rules); pilot [pilot-serp-capture-checklist.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/pilot-serp-capture-checklist.md) (R1 operator practice).

**Canonical boundary (unchanged):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 0. Terminology — two “R” namespaces

| Namespace | Meaning | Example |
|-----------|---------|---------|
| **MARS layer** | Ecosystem role | **MIG = MARS R1** (Market Groundtruth Research) |
| **MIG Reality Layer** | Trust / fidelity stack **inside** MIG acquisition | **R1–R4** in this document |

**Rule:** In MIG docs, prefix **“Reality Layer R*n*”** when referring to this model. Use **“MARS R1”** only for ecosystem placement (MIG vs ORCA vs Factory).

---

## 1. Purpose

The **Reality Acquisition Model** defines **how** MIG obtains market evidence, **in what order of trust** layers may be combined, and **what artifacts** prove each claim. It answers:

1. Which acquisition modes produce **groundtruth** vs **structured proxies** vs **derived intelligence**?
2. Which layer is **canonical** when layers disagree?
3. How does **Human Review Mode** package evidence for operator sign-off?

This model does **not** replace domain contracts (Research Request, Research Pack, Website Acquisition, etc.). It **classifies** acquisition paths and binds them to **evidence discipline**.

---

## 2. Reality layers — overview

```text
Trust (highest ▲)
│
│  R1  Human Reality          manual browser, human screenshots, validation
│  R2  Browser Groundtruth    Playwright — PRIMARY automated acquisition
│  R3  Structured Search      APIs, SERP vendors, XML feeds — scale mode
│  R4  Intelligence Reality     interpretation — MUST cite R1–R3 evidence
│
▼ Fidelity to live SERP UI (highest ▲)
```

| Layer | ID | Role | Primary artifacts | Default trust |
|-------|-----|------|-------------------|---------------|
| **Human Reality** | **R1** | Real human browser sessions; manual validation; human screenshots | PNG screenshots, operator notes, signed `review.md` | **Highest** |
| **Browser Groundtruth** | **R2** | Playwright/browser acquisition; full-page capture; DOM + HTML | `screenshots/`, `html/`, DOM JSON, capture manifest | **Canonical automated source** |
| **Structured Search Reality** | **R3** | Search APIs, SERP APIs, XML feeds; large-scale acquisition | `serp_result.json`, API payloads, feed snapshots | **Lower visual fidelity**; scale |
| **Intelligence Reality** | **R4** | Pattern extraction, competitive notes, strategic **recommendations** (evidence-bound) | `research_memo.json`, cited synthesis blocks | **Derived only** — never primary capture |

---

## 3. Layer definitions

### 3.1 R1 — Human Reality

**Definition:** Evidence obtained through a **real human** operating a **real browser session** (not headless automation), with explicit operator attestation.

| Owns | Does not own |
|------|----------------|
| Manual SERP observation per chartered query/region/device | Bulk API SERP at scale (→ R3) |
| Human-taken screenshots (full SERP, blocks, maps, ads) | Unattested LLM-generated SERP JSON |
| Manual validation of anomalies (personalization, geo, captcha) | ORCA campaign / semantic strategy |
| Highest-trust override when R2/R3 disagree with lived UI | Replacing structured normalization — R1 **feeds** normalization |

**Acquisition signals:**

- Operator identity and timestamp recorded in `review.md` and session manifest.
- Capture environment documented (engine, region, device, logged-in state).
- Ambiguity explicitly routed to **SAFE UNKNOWN** — never silently resolved.

**Relationship to pilots:** Manual SERP capture checklists are **R1-first** workflows. Automated spine may ingest R1 drops as **manual override** channel per [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md).

---

### 3.2 R2 — Browser Groundtruth

**Definition:** **Evidence-first** acquisition using **browser automation** (Playwright or equivalent) that reproduces a deterministic capture profile: viewport, geo, engine URL, wait conditions, and full-page render.

| Owns | Does not own |
|------|----------------|
| Full-page and block screenshots | Keyword volume strategy |
| DOM snapshot (structured tree or accessibility snapshot) | Intent labels, clustering |
| HTML capture (rendered document at capture time) | Facts not visible in captured DOM/HTML |
| Capture manifest linking query → artifacts | Human attestation without R1 review when charter requires HITL |

**Primary MIG acquisition mode (automated):**

- When automation is enabled, **R2 is the canonical browser-evidence source** for “what the SERP/page looked like” at capture time.
- R3 may run in parallel for scale; on conflict with **visual** features (ads layout, maps block, rich snippets), **R2 prevails** over R3 unless **R1** human review overrides.

**Minimum R2 artifact set (per capture unit):**

| Artifact | Path (under session evidence root) | Required |
|----------|--------------------------------------|----------|
| Full-page screenshot | `evidence/screenshots/<capture_id>-full.png` | Yes |
| HTML (rendered) | `evidence/html/<capture_id>.html` | Yes |
| DOM / structure JSON | `evidence/json/<capture_id>-dom.json` | Yes |
| Capture manifest | `evidence/json/<capture_id>-manifest.json` | Yes |

**Status:** **Planned** — no Playwright acquisition module is normatively implemented in MIG v0.1 spine; this layer is **design authority** for Enhancement Charter work.

---

### 3.3 R3 — Structured Search Reality

**Definition:** Acquisition through **structured interfaces**: official search APIs, third-party SERP APIs (SerpApi, DataForSEO, Yandex Search API, etc.), and **XML/feed** exports where the vendor returns pre-parsed blocks.

| Owns | Does not own |
|------|----------------|
| Normalized organic/ad/local fields at scale | Pixel-perfect ad creative fidelity |
| Reproducible machine-readable `serp_result.json` | Claims about UI not represented in API schema |
| Scheduled / batch query execution | Browser-only features invisible to API |

**Posture:**

- **Large-scale acquisition mode** — many queries, regions, devices (as API supports).
- **Lower visual fidelity** than R1/R2 — document provider gaps in SAFE UNKNOWN.
- Consumed by normalization and competitor discovery; **must not** be labeled “browser groundtruth” without R2 corroboration.

**Mapping to existing architecture:** Aligns with **Search Acquisition Layer** in [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md). v0.1 spine **fallback/manual/provider stub** is predominantly **R3-shaped JSON** with optional **R1** operator import.

---

### 3.4 R4 — Intelligence Reality

**Definition:** **Interpretation layer** inside the MIG session boundary: pattern extraction, competitive analysis notes, and strategic **recommendations** that are **explicitly derived** from R1–R3 artifacts.

| Owns | Does not own |
|------|----------------|
| Cited synthesis over existing session evidence | Primary SERP or page capture |
| Competitive **observation patterns** (e.g. “3/10 organic show phone CTA in snippet”) when tied to evidence refs | ORCA-owned campaign architecture, LRL, PPC exports |
| Session-scoped research memos with `evidence_ref[]` | Invented URLs, ranks, or features |

**Hard rules (normative):**

1. **R4 never replaces R1–R3.** No intelligence output may substitute for missing screenshots, HTML, DOM, or structured SERP JSON.
2. **All intelligence must reference evidence.** Every non-trivial claim carries at least one `evidence_ref` (see §5).
3. **Browser evidence remains canonical acquisition source** — for automated paths, **R2** (when implemented) anchors visual truth; **R3** supplements scale.
4. **Human verification remains highest trust source** — **R1** overrides R2/R3/R4 on dispute.

**Mapping:** Partial overlap with [mig-deep-research-architecture-v1.md](mig-deep-research-architecture-v1.md) — Deep Research is an **R4 channel** only when citations and SAFE UNKNOWN discipline are satisfied. **ORCA** remains the **MARS R2** interpreter for approved handoff packs; MIG R4 is **pre-handoff, evidence-bound session intelligence**, not ORCA replacement.

---

## 4. Normative rules (summary)

| ID | Rule |
|----|------|
| **RAM-01** | Reality layers are **ordered by trust**: R1 > R2 > R3 for visual/UI truth; R4 is always last. |
| **RAM-02** | **R4 never replaces R1–R3** — missing capture cannot be backfilled by synthesis. |
| **RAM-03** | **All R4 claims require `evidence_ref`** pointing into R1–R3 artifacts. |
| **RAM-04** | **Browser evidence (R2) is canonical** for automated visual acquisition when R1 is absent. |
| **RAM-05** | **Human verification (R1) is highest trust** and wins on conflict. |
| **RAM-06** | **R3** must declare `provider`, `schema_version`, and known fidelity limits in manifest or SAFE UNKNOWN. |
| **RAM-07** | Pack assembly and ORCA handoff **project** only approved, graded observations — not raw R4 alone. |

---

## 5. Evidence references

**`evidence_ref`** — stable pointer from any observation, JSON row, or R4 memo line to a physical artifact.

**Format (v1):**

```text
evidence_ref := <layer>:<artifact_path>#<optional_anchor>
```

| Prefix | Layer | Example |
|--------|-------|---------|
| `r1:` | Human Reality | `r1:evidence/screenshots/serp-20260604-full.png` |
| `r2:` | Browser Groundtruth | `r2:evidence/html/cap-001.html#organic-3` |
| `r3:` | Structured Search | `r3:serp_result.json#/organic_results/2` |
| `r4:` | Intelligence (derived) | `r4:research_memo.json#/findings/1` — must cite upstream r1–r3 |

**Validation (future runtime):** Every `r4:` ref must resolve to at least one `r1:` / `r2:` / `r3:` ref in the same session. **Documentation-only in v1.**

---

## 6. Layer composition per session

```text
Research Request
       │
       ├─► [R3] Structured search pass ──► serp_result.json
       │
       ├─► [R2] Browser groundtruth pass ──► evidence/{screenshots,html,json}
       │
       ├─► [R1] Human review / override ──► evidence/ + review.md
       │
       ├─► Derived passes (competitor, website) ──► consume R1–R3 refs
       │
       └─► [R4] Intelligence pass (optional) ──► cited memo only
                 │
                 ▼
         Normalization + Research Pack (draft → review → approved)
                 │
                 ▼
              ORCA (MARS R2)
```

**Coverage metadata (session manifest — future fields):**

| Field | Meaning |
|-------|---------|
| `reality_layers_present` | Subset of `{r1,r2,r3,r4}` |
| `canonical_visual_layer` | `r1` \| `r2` \| `r3` \| `none` |
| `r4_citation_complete` | `true` \| `false` \| `unknown` |

---

## 7. Human Review Mode

### 7.1 Definition

**Human Review Mode** is an operator workflow that **prioritizes R1 attestation** while **reconciling** automated captures (R2/R3) into a single **review package** suitable for promotion to `pack_state: review` and eventual ORCA handoff.

**Triggers (charter):**

- Pilot/manual SERP capture complete.
- R2 capture finished and needs operator sign-off.
- Discrepancy between R2 and R3 (operator resolves or marks SAFE UNKNOWN).
- Pre-approval gate before `research_pack.approved.md`.

**Not:** automated LLM review; approval workflow engine (still **not implemented** in v0.1).

### 7.2 Output package layout

Per capture unit or per query (operator choice; document in manifest):

```text
<session_or_capture_root>/
  evidence/
    screenshots/     # R1 human PNG and/or R2 full-page PNG
    html/            # R2 rendered HTML (optional for pure R1 if not collected)
    json/            # R3 serp_result.json, R2 dom/manifest, normalized extracts
    review.md        # Human Review Mode summary (required in this mode)
```

**`review.md` location:** `evidence/review.md` (session-level) **or** `evidence/<capture_id>/review.md` (per-query). Session manifest must record which convention applies.

### 7.3 `review.md` — required sections

| Section | Required content |
|---------|------------------|
| **Query** | Exact query string observed or validated |
| **Timestamp** | UTC ISO-8601 at observation or review completion |
| **Ads detected** | `yes` \| `no` \| `unknown` + count/pattern notes + `evidence_ref` |
| **Maps detected** | `dominant` \| `present` \| `absent` \| `unknown` + `evidence_ref` |
| **Organic results detected** | Count recorded; top-N listed or pointer to JSON + `evidence_ref` |
| **Local pack detected** | Same vocabulary as Maps; clarify if merged with maps block |
| **Evidence references** | Bulleted list of all `r1:` / `r2:` / `r3:` refs used in this review |
| **SAFE UNKNOWN** | Explicit unknowns — personalization, blocked capture, API gap, position ambiguity |

### 7.4 `review.md` — template (normative skeleton)

```markdown
# MIG Evidence Review

## Query
<exact query string>

## Timestamp
<YYYY-MM-DDTHH:MM:SSZ>

## SERP feature detection

| Feature | Detected | Notes | Evidence ref |
|---------|----------|-------|--------------|
| Ads | yes / no / unknown | | r1:... or r2:... or r3:... |
| Maps | dominant / present / absent / unknown | | |
| Organic results | <count> | top-N summary or see JSON | |
| Local pack | dominant / present / absent / unknown | | |

## Evidence references
- r1:evidence/screenshots/...
- r2:evidence/html/...
- r3:serp_result.json#/...

## Operator attestation
- Reviewer: <operator_id>
- Layers reviewed: R1, R2, R3 (strike unused)
- Conflicts resolved: <none | describe>

## SAFE UNKNOWN
- <bullet: what could not be confirmed and why>
```

### 7.5 Distinction from `research_pack.review.md`

| Artifact | Scope | Layer focus |
|----------|-------|-------------|
| `evidence/review.md` | **Capture-grade** evidence sign-off (Human Review Mode) | R1–R3 |
| `research_pack.review.md` | **Pack-grade** operator edit of draft Research Pack | Normalized observations |

A session may have **both**. Human Review Mode **must complete** (or explicitly waive R1 in manifest with charter exception) before pack approval when `request_type: groundtruth_run` and pilot rules apply.

---

## 8. Mapping — reality layers vs acquisition channels

| Acquisition channel (existing docs) | Primary reality layer | Secondary |
|------------------------------------|------------------------|-----------|
| Manual SERP import / pilot checklist | **R1** | R3 JSON if operator also files structured extract |
| Playwright SERP / site capture (planned) | **R2** | R1 review overlay |
| SERP API / feed (Search Acquisition) | **R3** | R2 corroboration when chartered |
| Website HTTP/DOM capture (v0.1 MVP) | **R2-ish** (HTTP, not full browser) — grade as **partial R2** until Playwright; disclose in SAFE UNKNOWN |
| Competitor Discovery | **Derived** — refs R3/R2/R1 only | — |
| Keyword Intelligence | **R3** (+ `page_visible` from site capture) | — |
| Deep Research / session memos | **R4** | Must cite R1–R3 |
| ORCA analysis | **Outside MIG** (MARS R2) | Consumes approved pack |

---

## 9. Conflict resolution

| Situation | Resolution |
|-----------|------------|
| R3 JSON shows ads; R2 screenshot shows none | Prefer **R2**; mark API gap in SAFE UNKNOWN; escalate to **R1** if high-stakes |
| R2 and R1 disagree | **R1 wins**; document reason in `review.md` |
| R4 pattern contradicts R3 row | **Invalidate R4 claim** or fix citation; never auto-update R3 |
| Only R3 present, no R2/R1 | Allowed for scale sessions; `canonical_visual_layer: r3`; pack must grade visual claims **down** |

---

## 10. Implementation posture (explicit non-goals)

| Item | v1 charter status |
|------|-------------------|
| Playwright worker | **Not implemented** — design only |
| Human Review Mode folder writer | **Not implemented** — operator manual layout per §7.2 |
| `evidence_ref` validator | **Not implemented** |
| Auto-merge R2 → `serp_result.json` | **Not implemented** |

**UNKNOWN until proven in repo:** production VPS browser pool, captcha policy, and n8n node ownership for R2 — verify against future `projects/mig/lib/` and workflow exports.

---

## 11. Related documents

| Document | Relationship |
|----------|--------------|
| [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) | Channel topology; hybrid SERP recommendation |
| [mig-operational-runtime-architecture-v1.md](mig-operational-runtime-architecture-v1.md) | Session storage, pack states |
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Output SoT |
| [mig-deep-research-architecture-v1.md](mig-deep-research-architecture-v1.md) | R4 synthesis constraints |
| [boundaries.md](../boundaries.md) | MIG vs ORCA |
| [../../shared/contracts/groundtruth-ownership-rule-v1.md](../../shared/contracts/groundtruth-ownership-rule-v1.md) | MARS R1 ownership |

---

## 12. Versioning

| Version | Date | Change |
|---------|------|--------|
| **v1** | 2026-06-04 | Initial Reality Acquisition Model + Human Review Mode package |
