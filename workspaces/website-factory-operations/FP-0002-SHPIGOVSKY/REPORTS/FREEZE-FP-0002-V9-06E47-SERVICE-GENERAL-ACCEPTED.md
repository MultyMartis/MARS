# FREEZE — FP-0002 V9-06E47 SERVICE GENERAL ACCEPTED

| Field | Value |
|-------|-------|
| **Date/time** | 2026-07-15 (local freeze; backup stamp `20260715-175228`) |
| **Base page** | Лечение алкогольной зависимости `#74` |
| **Local URL** | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ |
| **Editor role** | `service` / **Услуга** |
| **Effective layout** | `service_general` |
| **Render** | `alcohol-stack` → `alcohol-direct-v9` |
| **Accepted ACF groups** | Макет страницы услуги · Hero страницы услуги · Услуга — блоки страницы |
| **Service blocks group** | `group_fp02_service_general_parity` (68 fields) |
| **Accepted after** | E47 + E47-FIX01 + E47-FIX02 + E47-FIX03 + E47-FIX04 |
| **Operator acceptance** | E47-FIX04: «Да всё гуд.» |
| **Freeze statement** | Page type **Услуга** (`service_general`) is **frozen** pending an explicit change request |
| **Backup path** | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-service-general-freeze-accepted-before-next-phase-20260715-175228\` |
| **Architecture doc** | `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md` |
| **Task report** | `REPORTS/REPORT-FP-0002-V9-06E47-service-general-freeze.md` |

## Included accepted series

- `REPORT-FP-0002-V9-06E47-service-general-admin-parity-alcohol.md`
- `REPORT-FP-0002-V9-06E47-FIX01-service-general-admin-ux-cleanup.md`
- `REPORT-FP-0002-V9-06E47-FIX02-service-general-acf-render.md`
- `REPORT-FP-0002-V9-06E47-FIX03-service-signs-readmore.md`
- `REPORT-FP-0002-V9-06E47-FIX04-service-signs-readmore-toggle.md`

## Seeded media (base `#74`)

- team `#1238`
- landscape `#1239`
- corridor `#1709`

## Signs read-more (accepted)

- `.service-leaf-signs-v1__read-more`
- long text: 5-line clamp + «Читать больше»
- click → expand + «Скрыть»; second click → collapse + «Читать больше»
- short text: button hidden

## Non-claims

- **No production claim**
- **No hosting / preview claim**
- Local runtime backup and documentation only
- Git persistence remains a **separate** explicit task

## Explicit freeze boundaries

- Do **not** change Услуга admin/frontend model without an explicit charter
- Home remains frozen (E42) — untouched
- Services hub remains frozen (E44) — untouched
- Accepted Раздел model remains untouched
- Operator runtime `v9-style.css` drift preserved — do not overwrite from source

## Allowed next actions

- Representative services content rollout for other `Услуга` pages (`#314` / `#78` and peers) — without redesigning the accepted model
- Selective Git persistence charter for E47–E47-FIX04 + freeze artefacts
- Next page-type work only after explicit operator charter
