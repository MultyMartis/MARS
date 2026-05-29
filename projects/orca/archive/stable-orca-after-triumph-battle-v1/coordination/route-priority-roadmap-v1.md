# Route Priority Roadmap v1

**Purpose:** human-operated generation order for 11 remaining semantic packs + Factory pilots  
**Baseline:** V6 zakaz (`index.html`) production-stable; siblings scaffold-only  
**Not:** a schedule commitment or automated queue

---

## Priority tiers

### HIGH — generate and pilot first

| Order | Route / slug | Blueprint | Why HIGH |
|-------|--------------|-----------|----------|
| H1 | `5-tonn` | `05-capability-5-ton.md` | S-tier capability anchor; existing pack v0 + handoff; PPC group 01; highest spend risk if semantics wrong; registry shows strongest Factory history |
| H2 | `bytovki` | `02-use-case-bytovka.md` | Distinct use-case intent — validates differentiation pipeline vs zakaz; common junk-lead risk if hero stays generic |
| H3 | `stroymaterialy` | `03-use-case-stroymaterialy.md` | High-volume use-case; cargo/pricing semantics differ; tests density caps on task grid |
| H4 | `vezdehod` | `07-capability-6x6-vezdekhod.md` | Different machine story (6×6) — catches «copy 5т specs» failure early |

**Rationale block:**

1. **5-tonn** — Only route with partial ORCA pack + handoff artifact; closes registry/PROJECT.md «page 01» narrative for V6; capability PPC is structurally different from master hot — must be proven before scaling use-cases.
2. **bytovki / stroymaterialy** — Represent the bulk of use-case groups in Full Cycle v1.1; errors here look like «another zakaz page» — highest semantic drift risk for Factory if packs are lazy.
3. **vezdehod** — Forces alternate spec locks; if generated late, team may default 5/3/14 on wrong route — expensive rework.

**Pilot gate:** After H1, Factory completes **one** V6 page build + QA before H2 pack authoring accelerates (per `V6-PAGE-ROLLOUT-PLAN.md`).

---

### MEDIUM — after first 2 Factory pilots pass HITL

| Order | Route / slug | Blueprint | Why MEDIUM |
|-------|--------------|-----------|------------|
| M1 | `oborudovanie` | `04-use-case-oborudovanie.md` | Specialized cargo; FAQ/evidence sensitivity |
| M2 | `konteynery` | `10-use-case-konteynery.md` | Structural FAQ; registry blueprint path was incomplete — verify before pack |
| M3 | `armatura` | `11-use-case-armatura.md` | Long-load semantics; typography overflow risk in Factory |
| M4 | `kirpich-bloki` | `12-use-case-kirpich-bloki.md` | Similar to stroymaterialy — can reuse patterns after M1–M3 |

**Rationale:** Still revenue-relevant use-cases but lower immediate PPC exposure than S-tier capability + top use-cases. Benefit from lessons learned in HIGH tier density and handoff format.

---

### LOWER — after batch unlock (2 pilots + operator sign-off)

| Order | Route / slug | Blueprint | Why LOWER |
|-------|--------------|-----------|-----------|
| L1 | `yurlic` | `06-b2b-yurlica.md` | B2B semantics overlap shared `v5-page01` B2B block — needs pack to own payment story, not just hero |
| L2 | `kray` | `08-intercity-krai.md` | Geo framing easy to overclaim; depends on service-area locks from operator |
| L3 | `fbs-zhbi` | `09-use-case-fbs-zhb.md` | Niche; heavy FAQ UNKNOWNs; URL slug nuance (`perevozka-fbs-zhbi`) |

**Rationale:** Fewer groups or higher claim risk; mistakes less likely to pollute the core zakaz + capability funnel if generated last.

---

## Parallel work allowed (documentation only)

| Parallel safe | Parallel unsafe |
|---------------|-----------------|
| ORCA drafts two packs while Factory builds one | Factory builds 2+ new routes before first pilot QA |
| Research/calibration for M-tier while H1 in Factory | Changing zakaz hero without pack bump during pilots |
| Matrix + registry updates | Commander import before `approved_for_ads` |

---

## Master hot (`zakaz`) — parallel track

| Action | Priority |
|--------|----------|
| Sign `triumph-manipulyator-zakaz-pack-v1` | **Now** — baseline SoT for all siblings |
| Formal handoff MD | Before declaring any sibling «aligned to zakaz» |
| Resolve D1 qualification + D2 multi-ad H1 | Blocks PPC QA on homepage |

Not counted in «11 remaining» but **blocks** semantic authority for entire rollout.

---

## Success criteria per tier

| Tier | Done when |
|------|-----------|
| HIGH | 4 packs `approved_for_factory` + ≥2 V6 pages built with REPORT + matrix updated |
| MEDIUM | 4 packs approved + Factory drift patterns documented once |
| LOWER | 3 packs approved + launch prep review (human) |

---

## Related

- [route-pack-generation-rules-v1.md](route-pack-generation-rules-v1.md)
- [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md)
- `projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md`
