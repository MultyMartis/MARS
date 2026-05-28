# Route Alignment v1

## Campaign routing

| Field | Value |
|-------|--------|
| `final_url` | `https://manipulator-triumph.ru/` |
| `blueprint_id` | `01-master-hot-general` |
| `display path` | `zakaz-manip` |
| `fallback_allowed` | false |

## Factory routing

| Field | Value |
|-------|--------|
| Workspace page | `src/pages/index.html` |
| `data-page-type` | `ppc-zakaz-manip` |
| Partial family | `v5-ppc/zakaz/` |
| Dist | `dist/index.html` (baseline) |

## Alignment

| Check | Result |
|-------|--------|
| URL `/` | **pass** |
| Blueprint id | **pass** (doctrine) |
| Page type marker | **pass** — enables PPC SCSS |
| 5-ton slug not used | **pass** — no capability URL bleed |

## Cross-route leakage risks

| Risk | Status |
|------|--------|
| User on `/` confused with `/manipulyator-5-tonn/` | Mitigated by specs copy «5 т» on both — OK for master hot |
| Fastlinks point to other slugs | By design in ads — not page nav |
| Shared trust partial mentions wrong machine | **UNKNOWN** — review `screen-03-trust-reviews.html` before launch |

## Registry

`projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` — **not verified in this pass**.

**Action:** confirm master hot route entry exists with `blueprint_id: 01-master-hot-general`.

## v4 vs v5 route note

Bridge index still references v4 for 5-ton — zakaz calibration confirms **v5** for `/`. Update bridge index in separate ORCA maintenance task (out of scope here).
