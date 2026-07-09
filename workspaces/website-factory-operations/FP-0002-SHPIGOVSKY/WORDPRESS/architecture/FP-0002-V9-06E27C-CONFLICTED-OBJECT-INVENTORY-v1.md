# FP-0002 V9-06E27C — Conflicted Object Inventory

**Task:** V9-06E27C Page Service Ownership Decision  
**Mode:** Read-only audit  
**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/conflicted-object-inventory.json`

## Summary

Three legacy **pages** under hub `#5` shadow three **service CPT** subdivision objects at identical paths. Service CPT objects carry ACF fixture content and own child service trees; legacy pages carry generic pre-CPT copy with no ACF.

## Shadow legacy pages

| ID | Title | Path | Status | Content | ACF | Menu | Role |
|---:|---|---|---|---|---|---|---|
| 6 | Зависимости | `/uslugi/zavisimosti/` | publish | 431 B generic | 0 | Primary `#301` | shadow_legacy_page |
| 7 | Психическое здоровье | `/uslugi/psihicheskoe-zdorovie/` | publish | 431 B generic | 0 | — | shadow_legacy_page |
| 8 | Расстройства пищевого поведения | `/uslugi/rasstroystva-pischevogo-povedeniya/` | publish | 431 B generic | 0 | — | shadow_legacy_page |

## Canonical service subdivision owners

| ID | Title | Path | Status | Content | ACF meta | Children | Role |
|---:|---|---|---|---:|---:|---:|---|
| 73 | Зависимости | `/uslugi/zavisimosti/` | publish | 140 B + excerpt | 75 | 5 | canonical_route_owner |
| 77 | Психическое здоровье | `/uslugi/psihicheskoe-zdorovie/` | publish | 140 B + excerpt | 77 | 6 | canonical_route_owner |
| 84 | Расстройства пищевого поведения | `/uslugi/rasstroystva-pischevogo-povedeniya/` | publish | 140 B + excerpt | 76 | 3 | canonical_route_owner |

## Service #73 child tree

| ID | Title | Path | Parent |
|---:|---|---|---:|
| 74 | Лечение алкогольной зависимости | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 73 |
| 314 | Наркотическая зависимость | `/uslugi/zavisimosti/narkoticheskaya-zavisimost/` | 73 |
| 315 | Лекарственная зависимость | `/uslugi/zavisimosti/lekarstvennaya-zavisimost/` | 73 |
| 316 | Поведенческие зависимости | `/uslugi/zavisimosti/povedencheskie-zavisimosti/` | 73 |
| 75 | Профилактический анализ | `/uslugi/zavisimosti/profilakticheskiy-analiz/` | 73 |

## Source authority

- Service CPT rewrite claims child `/uslugi/{segment}/` paths (`ServicePermalinks.php`, priority `top`).
- Hub `/uslugi/` remains page `#5` with `services-hub.php` — **no conflict**.
