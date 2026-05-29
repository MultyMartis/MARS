# ORCA Route Family Freeze v1

**Project:** Triumph Manipulator (`triumph-manipulator-krasnodar`)  
**Freeze date:** 2026-05-28  
**Lane:** B — ORCA Freeze + Survivability  
**Status:** **FROZEN** (semantic production baseline) — **not** launch, **not** rollout, **not** runtime

---

## Purpose

Зафиксировать production semantic system Triumph Manipulator как **завершённое семейство из 12 маршрутов** с стабилизированной дифференциацией, форматом production copy pack и разделением ORCA ↔ Website Factory — до этапа implementation rollout.

Этот freeze **не** меняет copy, semantics, V6 HTML или governance. Он документирует **текущее стабилизированное состояние** для survivability и human-operated checkpoint.

---

## Freeze scope

| In scope | Out of scope |
|----------|--------------|
| 12 PPC landing routes + registry alignment | Новые routes / ad groups |
| Production semantic packs (`*-pack-v1`) | Переписывание copy |
| Semantic classes, differentiation locks | V6 implementation edits |
| ORCA ↔ Factory coordination model | Rollout / deploy / live launch |
| Calibration posture (documented, not extended) | Новые calibration loops |
| Survivability checkpoint recommendation | `governance/*`, `mars-runtime/*`, `workspaces/*` edits |

---

## Route family — complete (12/12)

| # | Route slug | `route_id` (registry) | Semantic class | Pack artifact |
|---|------------|----------------------|----------------|---------------|
| 1 | `/` (zakaz) | `zakazat-manipulyator` | **master** | `triumph-manipulyator-zakaz-pack-v1/` |
| 2 | `/manipulyator-5-tonn/` | `manipulyator-5-tonn` | **capability** | `triumph-manipulyator-5-tonn-pack-v1/` |
| 3 | `/perevozka-bytovok/` | `perevozka-bytovok` | **use-case** (logistics) | `triumph-bytovki-pack-v1/` |
| 4 | `/dostavka-stroymaterialov/` | `dostavka-stroymaterialov` | **use-case** | `triumph-stroymaterialy-pack-v1/` |
| 5 | `/manipulyator-dlya-yurlic/` | `manipulyator-dlya-yurlic` | **b2b** | `triumph-yurlic-pack-v1/` |
| 6 | `/manipulyator-vezdehod/` | `manipulyator-vezdehod` | **capability** (6×6) | `triumph-vezdehod-pack-v1/` |
| 7 | `/perevozka-oborudovaniya/` | `perevozka-oborudovaniya` | **use-case** | `triumph-oborudovanie-pack-v1/` |
| 8 | `/perevozka-konteynerov/` | `perevozka-konteynerov` | **use-case** | `triumph-konteynery-pack-v1/` |
| 9 | `/perevozka-armatury/` | `perevozka-armatury` | **use-case** | `triumph-armatura-pack-v1/` |
| 10 | `/dostavka-kirpicha-blokov/` | `dostavka-kirpicha-blokov` | **use-case** | `triumph-kirpich-bloki-pack-v1/` |
| 11 | `/perevozka-fbs-zhbi/` | `fbs-zhbi` | **use-case** (heavy logistics) | `triumph-fbs-zhbi-pack-v1/` |
| 12 | `/manipulyator-krasnodarskiy-kray/` | `manipulyator-krasnodarskiy-kray` | **geo** (intercity) | `triumph-kray-pack-v1/` |

**Family completeness:** все 12 маршрутов имеют production semantic pack v1 под `projects/orca/content-packs/examples/`. Blueprints: `projects/orca/ppc/triumph-manipulator/landing-pages/`. Registry: `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`.

---

## Semantic classes (frozen taxonomy)

| Class | Count | Role | Anti-pattern |
|-------|-------|------|--------------|
| **master** | 1 | Hot general entry, capability-first filtering | Copy-paste на siblings |
| **capability** | 2 | Machine story (5 т / 6×6) | Master-hot H1 «Аренда» на capability |
| **use-case** | 7 | Cargo/scenario logistics | Generic manipulator landing |
| **b2b** | 1 | Юрлица, документы, объект | Consumer-only CTA framing |
| **geo** | 1 | Маршрут / край | Overclaim geo без operator lock |

Дифференциация зафиксирована на уровне: H1, lead, tasks, denied tasks, cargo cards, trust emphasis, pricing framing (`по задаче`), FAQ intent — см. [ROUTE-FAMILY-INDEX-v1.md](ROUTE-FAMILY-INDEX-v1.md).

**Logistics sub-batch (semantic prep):** `projects/orca/coordination/logistics-family-batch-v1/` — konteynery, oborudovanie, fbs-zhbi — differentiation locks **done** (documentation).

---

## Differentiation — stabilized

| Layer | Stabilized artifact | Evidence |
|-------|---------------------|----------|
| Route identity | Registry `page_type` + pack `route_id` | `landing-route-registry.json` |
| H1 / intent | Per-route hero H1 ≠ zakaz default | Each `*-pack-v1/hero.md` or `content/hero.md` |
| Machine locks | 5/3/14 standard; 6×6 on vezdehod | Pack specs blocks |
| Denied / anti-junk | Route-specific qualification | Pack `tasks.md`, factory semantic-lock |
| Trust mode | Per-route emphasis (operational / handling / B2B / geo) | Visual-semantics (full packs) + logistics batch |
| Visual semantics | Full bundle: zakaz, 5-tonn, bytovki | `visual-semantics/` folders |
| Drift control | `factory/forbidden-drift.md` pattern | Reference packs + coordination protocol |

**Calibration freeze note:** `5-tonn` — production-calibrated baseline ([calibration/triumph-manipulator/5-tonn-stabilized-v1.md](../../calibration/triumph-manipulator/5-tonn-stabilized-v1.md)). `zakaz` — first visual-aware pack; open D2 H1 multi-ad (documented, not re-opened in this freeze). Sibling routes: **pack-frozen**; implementation calibration deferred to Factory pilots.

---

## Production copy pack format — stabilized

Два допустимых профиля v1 (оба — human-authored, **not** HTML):

### Profile A — Full semantic pack (reference)

**Examples:** `triumph-manipulyator-zakaz-pack-v1/`, `triumph-manipulyator-5-tonn-pack-v1/`, `triumph-bytovki-pack-v1/`

| Layer | Contents |
|-------|----------|
| Metadata | `PACK-METADATA.md`, `PACK-STATUS.md`, `APPROVALS.md` |
| Content slots | `content/` — hero, specs, tasks, pricing, trust, b2b, faq, final_cta |
| PPC | `ppc/` — intent-continuity, ad-alignment, CTA alignment |
| Visual semantics | `visual-semantics/` — trust_mode, cta_priority, density, mobile_critical |
| Factory | `factory/` — semantic-lock, forbidden-drift, frontend-hints |
| Calibration | `calibration/` (where applicable) |
| Gates | `approved_for_*` — human only |

### Profile B — Website copy pack (rollout wave)

**Examples:** remaining `triumph-*-pack-v1/` (flat layout)

| Layer | Contents |
|-------|----------|
| Slots | `hero.md`, `specs.md`, `tasks.md`, `pricing.md`, `faq.md`, `forms-cta.md`, … |
| Status | `PACK-STATUS.md` — `production_copy_ready: true`, `allowed_for_factory: yes` |
| Scope | `website_copy_only: true` — semantics locked in copy; visual-semantics folder optional |

**Canonical system:** [content-packs/content-pack-system-v0.md](../../content-packs/content-pack-system-v0.md)  
**Pipeline:** [coordination/semantic-pack-generation-system-v1.md](../../coordination/semantic-pack-generation-system-v1.md)

---

## ORCA → Factory separation — stabilized

| Authority | Owner |
|-----------|--------|
| Semantic meaning, PPC continuity, locks, drift class | **ORCA** |
| HTML, SCSS, responsive, build, UX wiring | **Website Factory** |
| `approved_for_factory`, launch, Commander import | **Human operator** |

**Contracts:**

- [intelligence/orca-website-factory-semantic-lock-v0.md](../../intelligence/orca-website-factory-semantic-lock-v0.md)
- [coordination/orca-factory-coordination-protocol-v1.md](../../coordination/orca-factory-coordination-protocol-v1.md)
- [coordination/factory-handoff-minimum-contract-v1.md](../../coordination/factory-handoff-minimum-contract-v1.md)

**Frontend baseline (reference only — not modified in freeze):** `workspaces/triumph-manipulator-landing-v6/` — V6 `zakaz` built; 11 sibling scaffolds.

---

## Production baseline posture

| Dimension | Freeze verdict |
|-----------|----------------|
| Route family | **Complete** (12/12 packs) |
| Semantic differentiation | **Stabilized** (documentation + pack copy) |
| Pack format | **Stabilized** (Profile A + B) |
| ORCA ↔ Factory | **Stabilized** (coordination protocol v1) |
| Rollout-ready | **Semantic baseline yes** · **Implementation rollout no** |
| Runtime / autonomy | **None claimed** |

---

## Related freeze artifacts

| Doc | Role |
|-----|------|
| [ROUTE-FAMILY-INDEX-v1.md](ROUTE-FAMILY-INDEX-v1.md) | Per-route operational table |
| [ROLLUP-STATUS-v1.md](ROLLUP-STATUS-v1.md) | READY / PENDING rollup |
| [FACTORY-HANDOFF-STATE-v1.md](FACTORY-HANDOFF-STATE-v1.md) | Role split at handoff |
| [KNOWN-OPEN-ITEMS-v1.md](KNOWN-OPEN-ITEMS-v1.md) | Open items + SAFE UNKNOWN |
| [SURVIVABILITY-CHECKPOINT-v1.md](SURVIVABILITY-CHECKPOINT-v1.md) | Git/backup checkpoint |

---

## Honesty boundary

ORCA Route Family Freeze v1 is **documentation-only** human discipline. It does **not** prove live URLs, deployed pages, ad launch, automated validation, or multi-agent runtime. Evidence is limited to committed artifacts in `projects/orca/` and referenced workspace paths.
