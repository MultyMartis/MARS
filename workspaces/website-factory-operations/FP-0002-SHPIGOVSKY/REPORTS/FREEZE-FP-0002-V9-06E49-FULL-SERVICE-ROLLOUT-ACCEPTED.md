# FREEZE — FP-0002 V9-06E49 FULL SERVICE ROLLOUT ACCEPTED

| Field | Value |
|-------|-------|
| **Date/time** | 2026-07-16 (local freeze; backup stamp `20260716-021704`) |
| **Mode** | Full individual **Услуга** (`service` / `service_general`) ACF content rollout freeze |
| **Accepted after** | V9-06E49 Full Service Rollout (21/21 targets seeded; no alcohol copy-paste) |
| **Operator acceptance** | E49 Full Service Rollout accepted; operator requested **E49 Full Service Rollout Freeze** |
| **Final #78** | `#78` Депрессия — **Услуга** / `service` / `service_general` (full service FE; not placeholder) |
| **Freeze statement** | Full service (Услуга) individual-page rollout is **frozen pending operator review of post-E49 drift on `#315`** |
| **Known exception** | `#315` Лечение лекарственной зависимости — currently `placeholder`/`placeholder` (was `service`/`service_general` at E49). ACF content preserved. Freeze task did **not** restore layout (charter: no layout-mode mutation). |
| **Backup path** | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-freeze-accepted-before-next-phase-20260716-021704\` |
| **Task report** | `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze.md` |
| **Evidence** | `REPORTS/evidence/v9-06e49-freeze-*.csv` |

## Accepted series included

- `REPORT-FP-0002-V9-06E49-full-service-rollout.md`
- Prior: E47 Услуга field model freeze; E48 representatives; E50 section freeze; E51 Placeholder Mode freeze

## Accepted model

| Area | Accepted value |
|------|----------------|
| Publish service CPT | 29 |
| Sections excluded from Услуга rollout | `#73` / `#77` / `#84` → Раздел / `subdivision` |
| Accepted base | `#74` Лечение алкогольной зависимости |
| E48 representatives | `#314` / `#78` / `#81` / `#85` |
| E49 targets | 21 remaining `service_general` pages |
| Individual service layout | `service` / `service_general` |
| Admin model | Макет → Hero → Услуга — блоки страницы |
| Content SoT | ACF (`group_fp02_service_general_parity`); no alcohol copy-paste |
| Placeholder Mode | E51 frozen; available but not selected on accepted Услуга pages (#78 remains Услуга) |

## Operator values preserved

- `#78` remains **Услуга** after E51 freeze
- Home (E42) and `/uslugi/` (E44) untouched
- Sections `#73/#77/#84` remain Раздел (E50)
- Controls `#74/#314/#81/#85` remain full service
- Operator runtime `v9-style.css` drift preserved (`11A45ABE…`)

## Known freeze exception (#315)

| Item | Value |
|------|-------|
| Post | `#315` Лечение лекарственной зависимости |
| E49 accepted state | `service` / `service_general` |
| Freeze-observed state | `placeholder` / `placeholder` (+ FE `placeholder-stack`) |
| ACF content | Still present (content validation PASS) |
| Freeze action | Documented only — **no restore** (charter forbids layout-mode mutation) |
| Recommended | Operator decides restore-to-Услуга micro-fix vs intentional placeholder |

## Non-claims

- **No production claim**
- **No hosting / preview claim**
- Local runtime backup and documentation only
- Git persistence remains a **separate** explicit task

## Explicit freeze boundaries

- Do **not** re-seed or redesign Услуга ACF field definitions without charter
- Do **not** alcohol-copy into non-alcohol services
- Do **not** switch `#78` to placeholder without explicit charter
- Do **not** mutate Home / `/uslugi/` / section pages `#73/#77/#84`
- Do **not** overwrite operator runtime `v9-style.css` from source
- Resolve `#315` only via explicit operator charter

## Allowed next actions

- Operator review / restore `#315` to Услуга (preferred micro-charter before next page type)
- Selective Git persistence charter for E38–E51 (+ this freeze) artefacts (`CREATE_V9_06E38_E51_PERSISTENCE_TASK`)
- Next page-type work only after `#315` decision + explicit operator charter
