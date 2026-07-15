# FREEZE — FP-0002 V9-06E50 SERVICE SECTIONS DEMO ACF SOT ACCEPTED

| Field | Value |
|-------|-------|
| **Date/time** | 2026-07-15 (local freeze; backup stamp `20260715-230201`) |
| **Page type** | Раздел / рубрика услуг (`service_editor_role=section` → `subdivision`) |
| **Targets** | `#73` Зависимости · `#77` Психическое здоровье · `#84` Расстройства пищевого поведения |
| **Local URLs** | `/uslugi/zavisimosti/` · `/uslugi/psihicheskoe-zdorovie/` · `/uslugi/rasstroystva-pischevogo-povedeniya/` |
| **Accepted ACF group** | `group_fp02_service_section_parity` (55 fields) |
| **Also visible** | Service — Layout · Hero страницы услуги |
| **Hidden on sections** | `group_fp02_service_general_parity` (Услуга blocks) |
| **Normal FE text SoT** | Page ACF only (seeded/demo/current) |
| **Empty optional field** | Hide / empty-safe — **no** normal hardcoded demo inject |
| **Emergency fallback** | PHP `*_fallback()` technical/legacy only |
| **Accepted after** | V9-06E46 + FIX01–FIX05 + **V9-06E50** |
| **Operator acceptance** | E50: «Всё гуд!» |
| **Freeze statement** | Page type **Раздел** is **frozen** pending an explicit change request |
| **Backup path** | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e50-service-sections-demo-acf-sot-freeze-accepted-before-next-phase-20260715-230201\` |
| **Architecture doc** | `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md` |
| **Task report** | `REPORTS/REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot-freeze.md` |

## Accepted series included

- `REPORT-FP-0002-V9-06E46-service-section-admin-parity-zavisimosti.md` (+ FIX01–FIX05)
- `REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot.md`

## Operator values preserved

- `#73`: `ТЕСТ` / `000101` retained in ACF
- `#77` / `#84`: section-specific headings (no dependency copy-paste)

## Non-claims

- **No production claim**
- **No hosting / preview claim**
- Local runtime backup and documentation only
- Git persistence remains a **separate** explicit task

## Explicit freeze boundaries

- Do **not** change Раздел admin/frontend SoT model without an explicit charter
- Do **not** reintroduce normal hardcoded demo injection on empty optional fields
- Home remains frozen (E42) — untouched
- Services hub remains frozen (E44) — untouched
- Услуга model remains frozen (E47) / E48–E49 rollout preserved — do not mutate service pages here
- Operator runtime `v9-style.css` drift preserved — do not overwrite from source

## Allowed next actions

- Full service rollout freeze for E49 (`CREATE_V9_06E49_FULL_SERVICE_ROLLOUT_FREEZE_TASK`)
- Selective Git persistence charter for E46–E50 + freeze artefacts
- Next page-type work only after explicit operator charter
