# ORCA Lessons Learned v1

**Source:** First real Commander import battle — Triumph Manipulator Search PPC  
**Date:** 2026-05-30  
**Type:** Deep post-battle analysis — human-operated review

---

## 1. Semantic packs

### What worked

- **12-route family freeze** (`7666829`) gave stable semantic foundation before any export attempt  
- Per-route packs with differentiation matrices (density, trust mode, CTA hierarchy) prevented generic ad copy  
- `PACK-STATUS.md` + `SAFE-UNKNOWN.md` per pack enforced honest maturity signaling  
- Logistics family batch coordination kept sibling routes distinct without semantic bleed  

### Why Final Website Copy Pack needs separation from semantic preparation

Semantic preparation packs define **intent, positioning, qualification, and Factory constraints**. They are **not** final landing copy. Battle showed:

- Factory implementation adds layout, visual semantics, and frontend constraints semantic packs don't carry  
- PPC ad copy derives from semantic intent but must be **validated against live landing URLs** — a step semantic packs alone can't gate  
- Drift between semantic pack hero and deployed page breaks ad↔landing continuity  

**Rule going forward:** Semantic pack → Factory handoff → **Final Website Copy Pack** (approved deployed copy) → PPC JSON generation. No PPC export without Final Website Copy Pack gate.

### How to use further

1. Route family freeze remains SoT for semantic differentiation  
2. Add explicit Final Website Copy Pack per route before PPC JSON update  
3. Calibration loop: deployed page → copy pack → JSON instance sync  

---

## 2. Website Factory bridge

### ORCA = semantic authority

ORCA owns intent tiers, route differentiation, cross-route negatives, bid priority logic, and landing routing schema. Meaning layer is **never** in Factory.

### Factory = implementation

Factory owns HTML/CSS/JS, visual semantics execution, form wiring, analytics hooks. Factory **must not** invent semantic claims outside ORCA lock.

### STOP-gates encountered

| Gate | Where | Battle outcome |
|------|-------|----------------|
| Route family complete | Before export | PASS — 12/12 |
| Semantic lock on handoff | Factory rollout | PASS per route |
| URL registry sync | Before export | PASS after `f235bf1` |
| Final copy vs deployed page | Implicit gap | **Needs formal gate** (P0) |
| PPC JSON validation | Before export | PASS — 345 rules |

**Lesson:** Factory can ship pages while PPC transport is still calibrating. URL registry sync gate must run **after every Factory route deployment**, not once.

---

## 3. URL system

### Legacy URLs

Pre-sync JSON used trailing-slash slug paths. Commander import would route clicks to wrong or non-existent pages. **164 replacements** required.

### Registry sync

Three layers must stay aligned:

1. `landing-route-registry.json` (project registry)  
2. `triumph-s-tier-draft-v1.json` (PPC instance)  
3. `mapping.js` PRODUCTION_LANDING_SLUGS (exporter)

Battle fix: single sync commit + validation gate. **Lesson:** URL changes are **never** exporter-only edits.

### Commander export sync

Exporter fastlinks, display paths, and `final_url` must all reference same canonical `.html` set. Post-sync audit: 12/12 PASS.

**Upgrade needed:** Automated URL registry/export sync gate (P0).

---

## 4. Exporter transport

### Ad × keyword bug

Most critical battle failure. Nested loop produced 108 rows where 84 expected. Commander would show 5× duplicate ads per group.

**Lesson:** Transport model must be **explicitly designed** — never assume row-per-entity without matrix audit.

### Transport split v1.2

Separate row types: GROUP → AD → KEYWORD. Each entity type gets its own row pattern. Validated by `validate:no-duplicate-ads-v1.2`.

### No duplicate ads

Automated signature check became mandatory export READY gate. Human Commander import confirmed 20 unique ads.

**Upgrade needed:** Commander Export no-duplicate transport model as permanent architecture pattern (P0).

---

## 5. Commander template

### Template v1 as SoT

`triumph-manipulator-commander-template-v1.xlsx` is the **only** approved Search Manual Bids transport template. All metadata, column mapping, and fidelity checks derive from it.

### What XLSX can transport

- Campaign metadata (6 keys at v1.4)  
- Group / ad / keyword entity rows  
- Bid values (col 54) + autobid flag (col 53)  
- Group negatives (col 68)  
- Landing URLs, display paths, fastlinks, callouts  
- Region, ad type, match types  

### What XLSX cannot transport

- Weekly / daily budget  
- Ad schedule (hours/days)  
- Campaign strategy UI activation state  
- Smart bidding configuration  
- Account-level settings  

**Lesson:** Template SoT defines **transport ceiling**. Don't attempt to encode UI-only settings in exporter patches.

---

## 6. Campaign settings

Strategy, budget, and schedule require **post-import human setup** in Commander UI.

Battle sequence:
1. Import v1.4 XLSX — structural PASS  
2. Bids not visible in UI  
3. Operator manually set «ручное управление ставками»  
4. Bids appeared (400–600 ₽)  

**Lesson:** Export READY ≠ Launch READY. Post-import checklist is **mandatory separate gate** — [CAMPAIGN-SETTINGS-LAYER-v1.md](CAMPAIGN-SETTINGS-LAYER-v1.md).

---

## 7. Cross-negatives

### Mandatory

Route-family cross-negative matrix is **not optional**. Without it, sibling groups compete on each other's intent (e.g. «бытовки» queries hitting «заказ» group).

### Wildcard prohibited

Commander rejects `*` in minus phrases. v1.3 failed 12/12 groups. v1.4 expanded stems to full word forms.

### Commander-safe syntax

Allowed: letters, digits, spaces, `+`, `-`, `()`, quotes, `[]`.  
Forbidden: `*`, regex chars.

**Upgrade needed:** Commander-safe negative syntax as permanent validation rule + automated matrix builder (P0/P1).

---

## 8. Bid management

| Rule | Value | Battle result |
|------|-------|---------------|
| Default range | 400–600 ₽ | Exported correctly |
| Within-group spread | 10–90 ₽ | Variation confirmed |
| Zero bids | **Prohibited** | Validation gate blocks |
| UI visibility | Requires strategy setup | PASS after manual activation |

**Lesson:** Bid export and bid visibility are **two different gates**. Document both.

**Upgrade needed:** Bid priority model linking intent tier to bid weight (P1).

---

## 9. Hygiene

### Old gruzotaxi tails

Legacy project references to `gruzotaxi-triumph.ru` survived in draft history. Hygiene audit gate now catches these pre-export.

### Legacy negatives

Old campaign-level negatives from prior project iterations. Template v1 carries 9 canonical campaign negatives — exporter must not merge stale lists.

### Old project tails

Stale template rows (rows 31+) from prior export experiments. Cleanup rules neutralize before patch.

**Upgrade needed:** Commander hygiene scanner as automated pre-export tool (P1).

---

## 10. Launch readiness

### What still needs verification before real start

| Item | Status |
|------|--------|
| Commander import structural | **Done** |
| Post-import strategy/budget/schedule | **Pending operator** |
| Conversion tracking / analytics | **SAFE UNKNOWN** |
| Landing page load speed on mobile | **SAFE UNKNOWN** — Factory QA separate |
| Form submission end-to-end | **SAFE UNKNOWN** |
| Search terms review baseline | **Not started** — needs 2–4 weeks post-launch |
| Moderation compliance | **Human review required** |
| Operator launch sign-off | **Not granted** |

**Lesson:** Battle pilot proves **export + import path**. Launch readiness is a **separate checklist** with additional gates.

---

## Meta-lessons

1. **Incremental exporter versions beat big-bang** — v1.2 → v1.3 → v1.4 each fixed one battle failure  
2. **Automated QA gates saved re-import cycles** — validate before Commander, not after  
3. **Human UI steps are architecture, not bugs** — document them as gates  
4. **Documentation freeze is survivability** — without freeze, battle knowledge evaporates between chats  
