# ORCA Campaign Mode Architecture v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — mode separation for PPC operational design.

**Critical:** Search and RSYA are **not** one system. Shared intake and evidence layers do not imply shared campaign logic, validation, or landing contracts.

## Purpose

Define modular **campaign mode packs** so ORCA can route normalized intelligence to the correct operational shape without mixing Yandex Search doctrine with Display Network / RSYA assumptions.

## Mode Registry

| Mode | Folder | Primary intent surface | Maturity in repo (2026-05-21) |
|------|--------|------------------------|-------------------------------|
| `search` | `campaign-modes/search/` | Query-level commercial intent | **Operational** — Triumph Manipulator pack |
| `rsya` | `campaign-modes/rsya/` | Audience + placement + creative | **Foundation only** |
| `retarget` | `campaign-modes/retarget/` | Return visits, list-based | **Foundation only** |
| `brand` | `campaign-modes/brand/` | Brand defense / navigational | **Foundation only** |
| `local` | `campaign-modes/local/` | Geo-local service delivery | **Partial** — overlaps Search geo |
| `experimental` | `campaign-modes/experimental/` | Bounded tests | **Foundation only** |

Populate only modes in active scope per `PROJECT.md`.

## Shared vs Mode-Specific

| Layer | Shared across modes | Mode-specific |
|-------|---------------------|---------------|
| Intake / manifest | yes | — |
| Evidence classification | yes | minimum bar may differ |
| Research (SERP) | partial | RSYA: placement/context research, not query architecture |
| Keyword model | partial | Search: query groups; RSYA: interests/remarketing keys differ |
| Ad logic | no | format, limits, intent rules differ |
| Landing expectations | partial | Search: query continuation; RSYA: visual/offer hook |
| Validation rules | partial | separate rule packs per mode |
| Export transport | partial | Commander sheets differ by campaign type |

## Mode Specifications

### Search (`search/`)

**Intent model**

- One ad group = one semantic intent (Triumph doctrine).
- Query-driven: keyword, headline, landing route alignment.
- Negative keyword discipline central.

**Landing expectations**

- Exact-fit continuation: ad promise → hero → CTA → trust.
- Capability / use-case / B2B page routes per intent tier.
- Mobile-first qualification.

**Artifact types**

- Intent tier maps, keyword packs, ad copy sets, landing briefs, Commander XLSX, validation reports.

**Validation differences**

- Intent purity, anti-garbage, symbol limits, Yandex bold-highlight rules, semantic continuation.
- Reference: `projects/orca/ppc/triumph-manipulator/validation/`

**Research differences**

- SERP snapshots per query/region/device.
- Competitor ad copy in search results.
- Aggregator / marketplace pressure in SERP.

**Ad logic differences**

- Text ads, extensions (sitelinks, callouts), phrase match discipline.
- Search-only negatives and geo modifiers.

---

### RSYA (`rsya/`)

**Intent model**

- Audience, interest, placement, and creative hook — **not** query-level intent purity.
- Offer and visual pattern matter more than keyword symmetry.

**Landing expectations**

- Faster visual comprehension; broader offer framing acceptable vs Search exact-fit.
- CTA may differ (callback vs calculate) — still evidence-backed.

**Artifact types**

- Creative briefs, image/copy pairs, placement notes, frequency caps doc, RSYA-specific export sheets.

**Validation differences**

- Creative policy, image ratios, claim support, brand safety.
- **No** Search "one group one query intent" rule imported blindly.

**Research differences**

- Placement observations, network context, competitor display creatives.
- Less SERP-query architecture; more feed/placement snapshots.

**Ad logic differences**

- Display formats, image assets, audience targeting documentation.
- Separate from Search keyword generation prompts.

---

### Retarget (`retarget/`)

**Intent model**

- List-based return intent; prior visit or engagement assumed.
- Message ladder: reminder → offer → urgency (evidence-gated).

**Landing expectations**

- Shorter path to CTA; consistency with prior acquisition source.

**Artifact types**

- List definitions (human-maintained), sequence briefs, creative variants.

**Validation**

- List freshness, frequency, offer truth, exclusion rules.

**Research**

- Funnel step observations — **SAFE UNKNOWN** if conversion data not provided.

---

### Brand (`brand/`)

**Intent model**

- Navigational and brand defense; competitor brand bidding policy human-decided.

**Landing expectations**

- Brand-truth homepage or dedicated brand page.

**Artifacts**

- Brand keyword list, ad variants, legal/trademark notes.

**Validation**

- Trademark policy, official name spelling, misrepresentation checks.

---

### Local (`local/`)

**Intent model**

- Geo-service delivery; maps/local pack pressure (see local heuristics in ORCA tree).

**Landing expectations**

- City/region visible above fold; call-first vs form-first per evidence.

**Overlap**

- Often implemented **inside** Search campaigns for service businesses — `local/` folder holds geo-specific supplements, not duplicate Search pack.

---

### Experimental (`experimental/`)

**Intent model**

- Bounded hypothesis tests with explicit stop rules.

**Requirements**

- Document hypothesis, evidence basis, budget risk cap, rollback plan.
- Never mixed into production-ready exports without relabel.

## Mode Pack Internal Shape (recommended)

```
campaign-modes/<mode>/
  MODE.md              # scope, status, boundaries
  intent-model.md      # optional detail
  validation-rules.md  # or pointer to ppc pack rules
  artifacts/           # mode-local drafts
```

## Transport Layer Isolation

Commander XLSX and sheet patches are **transport** — mode-specific export contracts must not become semantic SoT (Triumph precedent).

## Triumph Manipulator

Active Search implementation:

`projects/orca/ppc/triumph-manipulator/` ≡ operational `search` mode pack.

Do not refactor Triumph in v0. New projects use `projects/orca/projects/<id>/campaign-modes/search/` alongside canonical tree.

## SAFE UNKNOWN

- RSYA validation CLI / export rules — **not present** in repo at v0 time.
- Retarget list automation — **not claimed**.
- Whether `local/` merges into Search for all service niches — operator decision per project.

## Related Documents

- [orca-universal-intake-architecture-v0.md](../intake/orca-universal-intake-architecture-v0.md)
- [project-structure-contract-v0.md](../projects/project-structure-contract-v0.md)
- [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md)
- Triumph Search pack: `projects/orca/ppc/triumph-manipulator/OPERATIONAL-INDEX.md`
