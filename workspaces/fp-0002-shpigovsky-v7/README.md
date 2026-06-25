# FP-0002 Shpigovsky — Workspace V7

| Field | Value |
|-------|-------|
| **Project** | FP-0002 Shpigovsky |
| **Workspace version** | V7 |
| **Status** | ACTIVE DEVELOPMENT |
| **Parent workspace** | `workspaces/fp-0002-shpigovsky-v6/` |
| **Parent release** | `FP-0002-V6-FINAL-BEFORE-V7-OPERATOR-STABLE-01` |
| **Parent tag** | `fp-0002-v6-final-before-v7-operator-stable-01` |

## Parity requirements at bootstrap

| Check | Requirement |
|-------|-------------|
| Initial source parity | REQUIRED |
| Initial visual parity | REQUIRED |
| Initial functional parity | REQUIRED |

## Design authority

| Source | Role | SHA-256 |
|--------|------|---------|
| `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` | **ACTIVE** — primary for all new work | `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041` |
| `Шпиговский.fig` | **HISTORICAL — DO NOT USE FOR NEW WORK** | `D25A13617664040045A88AE9B804FEB737076007CB317D49699196F92232B64B` |

## Package #001

```text
package_001: IN_PROGRESS
package_001_phase_1_figma_rules: COMPLETE
package_001_phase_2_head: COMPLETE_PENDING_OPERATOR_REVIEW
```

See `foundation/FP-0002-V7-FIGMA-AUTHORITY-RULES.md` and `reviews/package-001/head/`.

## URL policy

V7 is an internal workspace version. User-facing URLs remain unchanged (`/`, `/uslugi/`, `/o-centre/`, etc.). Do not add `/v7/` to public links.

Production host: `shpigovsky.ru` (DOM-SHPIG-01).

## Build

```bash
npm ci
npm run build
```

Outputs: `dist/index.html`, `dist/uslugi.html`

## Historical V6 artefacts

V6 reports, reviews, releases, and capture history remain under the parent workspace. Refer to V6 paths for history; do not treat copied V6 reports as V7 source of truth.
