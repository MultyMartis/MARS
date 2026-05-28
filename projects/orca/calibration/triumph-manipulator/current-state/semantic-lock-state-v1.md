# Semantic Lock State v1 — master hot (zakaz)

**Contract reference:** `projects/orca/intelligence/orca-website-factory-semantic-lock-v0.md`

## Lock activation checklist

| Precondition | Status |
|--------------|--------|
| Approved ORCA artifact for **this URL** | **FAIL** — no zakaz handoff; blueprint only |
| Handoff references ORCA SoT | N/A |
| Operator MODE 1 | **Assumed** for production intent; not formally logged for zakaz |
| Content pack for route | **FAIL** — only `triumph-manipulyator-5-tonn-pack-v0` exists |

**Verdict:** Semantic lock is **partially active by doctrine**, not fully active by artifact trail.

## Locks preserved in v5 (evidence)

| Lock domain | Status | Evidence |
|-------------|--------|----------|
| One machine / 5 т · 3 т · 14 м | **preserved** | Hero specs + specs block |
| No fleet «5–10 т» / «автопарк» in hero | **preserved** | vs legacy v4 index hero |
| No fake hero hourly price | **preserved** | v4 `hero__rate` removed |
| Geo Краснодар + край | **preserved** | H1, lead, specs ops line |
| Price honesty (по задаче) | **preserved** | pricing factors section; no «от 1000» |
| Anti-evacuation / filtering | **partial** | Denied tasks section exists; **hero notice removed** in v5 |
| Messenger order MAX→TG→WA | **UNKNOWN in hero** | Footer/modal — verify in footer partial |
| Reviews sources Яндекс + Авито | **preserved** | trust partial (below fold) |

## Locks weakened or drifted

| Lock domain | Issue | Class |
|-------------|-------|-------|
| Trust strip in hero (4.9 ★) | Replaced by operational proof | ambiguous / productive |
| Blueprint primary CTA wording | «Узнать…» → «Рассчитать…» | minor lexical |
| Multi-ad H1 strategy | Landing H1 «Аренда» vs ad «Заказать» | PPC design gap, not Factory alone |
| Call-first in instance vs form-first hero | Hierarchy tension | ambiguous |

## MODE 1 violations avoided (major)

Legacy v4 index hero would have violated:

- fleet framing
- fake pricing
- broad tonnage claim

v5 zakaz hero is **MODE-1-aligned** on capability numbers and honesty vs that baseline.

## Operator actions to fully activate lock

1. Author `triumph-manipulator-v5-master-hot-handoff.md` (mirror 5-ton handoff structure).
2. Create `triumph-manipulyator-zakaz-pack-v0.md` or extend pack template for `master_hot`.
3. Set `approval_gates.approved_for_factory: true` with human sign-off.
4. Register route in project `landing-route-registry.json` if not present — **UNKNOWN** without registry read in this pass.

## Calibration use

Treat **5-ton pack** as **pattern donor**, not as SoT for master hot H1 or ad mapping.
