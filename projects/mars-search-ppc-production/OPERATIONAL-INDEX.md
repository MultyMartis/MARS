# MARS Search PPC Production — Operational Index

## 0. Status

| Item | Value |
|---|---|
| Programme | `mars-search-ppc-production` |
| Status | `OPERATIONAL` |
| Current mode | Documentation-first / human-supervised PPC production lifecycle |
| Platform scope | Yandex Direct — search campaigns (cross-system SPPC-01–23) |
| Registry | `registry/project-registry.md` — row `mars-search-ppc-production` |

This programme is not an autonomous campaign engine, bidding system, scheduling product, or Commander/Direct automation layer.

This file is an operational navigation index: it routes operators to authority documents, pilot lanes, evidence classes, and persistence boundaries. It is not campaign authority by itself and does not authorize import, launch, UTM creation, or account mutation.

Indexed import, launch, and client states below are evidence-indexed audit snapshots, not execution actions performed by this file or by repo presence alone.

## 1. Authority chain

Resolve authority in this order:

1. `README.md` — programme entry, structure map, validation entry point.
2. `MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md` — binding cross-system lifecycle (SPPC-01–23), operator gates, degraded-evidence rules.
3. `registry/project-registry.md` — MARS project_id registration and programme boundaries.
4. Machine-readable contract layer — `contracts/`, `schemas/`, `validators/validate-search-ppc-lifecycle.mjs`, `state/project-ppc-state-manifest-template-v1.json`.
5. Execution contracts — `web-gpt/`, `cursor/`, `docs/release-gate/`, `tools/commander-transport/` (transport-only; not live import authority).
6. Pilot / client lanes (subordinate evidence) — paths under `pilots/` and `projects/` inside this programme root. These hold lane-specific manifests, reports, and import candidates; they do not supersede lifecycle or registry authority.
7. Consumer systems (boundary only) — ORCA, MIG, ATLAS consume or feed evidence per their own operational indexes; Search PPC does not replace subsystem ownership.

When subordinate pilot evidence conflicts with lifecycle gates, stop and treat the state as `BLOCKED` until operator reconciliation.

## 2. Operational boundaries

Human-supervised discipline applies to all Search PPC work:

- No Yandex Direct account mutation without explicit operator charter naming target account, action class, and rollback.
- No campaign launch without operator approval recorded per SPPC-21 / SPPC-22 gates.
- No UTM creation or URL mutation without operator approval and registered correction artifacts.
- No import to Commander or Direct from repo state, manifests, or this index alone — import remains operator-executed platform work.
- Commander Export (SPPC-20) is transport-only — it must not admit phrases, change semantics, move keywords, modify negatives, invent structure, or rewrite strategy.
- XLSX/CSV import packages default to Storage-backed bulk (`X:\AI MARS STORAGE\`) unless an explicit scoped task authorizes repo persistence.
- Secrets and tokens must not be committed, pasted into chat, or printed — metadata flags only when already present in safe artifacts.
- Generated and test outputs such as `.tools-test-output/` are diagnostic evidence, not campaign authority.
- Dirty / untracked WIP remains protected until classified and persisted through scoped MASTER-15 waves — do not mass-commit or cleanup without charter.
- Absence of a negative claim in repo does not prove live platform state — verify with operator attestation before any platform action.

## 3. Active lanes

Evidence snapshot as of MASTER-15 classification (2026-07-05). Re-verify before operator action.

| Lane | Programme path | Lane status (evidence) | Commander import | Campaign launch | UTM | Advertising | Owner |
|---|---|---|---|---|---|---|---|
| Corvonero / Корво Неро | `pilots/corvonero/` | Pilot evidence WIP; deployable candidate V2.6.2; client feedback `CLIENT_FEEDBACK_PENDING` | `NOT PERFORMED` | `NOT STARTED` | Not in scope of current snapshot | `NOT STARTED` | Search PPC / Corvonero PPC lane |
| Drive Avenue | `projects/drive-avenue-yandex-direct/` | `READY_FOR_OPERATOR_IMPORT_CHECK` (phase 4c checklist evidence) | `NOT PERFORMED` | `NOT PERFORMED` | `NOT CREATED` — `NO_UTM_BY_OPERATOR_DECISION` | Not started | Search PPC / Drive Avenue PPC lane |

Corvonero notes (evidence-indexed):

- Import-candidate XLSX, DOCX client packs, and bulky exports are Storage-backed pointers, not repo-default authority.
- Lifecycle doc marks Corvonero `FROZEN PENDING SEARCH PPC PRODUCTION LIFECYCLE IMPLEMENTATION AND GAP CLOSURE`; pilot WIP and lifecycle gate must be reconciled before launch claims.
- Client approval is pending — no client approval claim from repo state alone.

Drive Avenue notes (evidence-indexed):

- Search/RSYA packages were unchanged in phase 4c relative to prior draft waves; operator import check is the next human gate.
- Final launch checklist and Commander draft artifacts may exist as markdown/validation docs in repo; live XLSX/CSV mirrors default to Storage.

## 4. Evidence and storage policy

### Repo-suitable when scoped and classified

- Markdown strategy docs, stage contracts, operator decision records.
- JSON authority / state manifests and validation results (human-attested).
- Human-readable REPORT artifacts under `reports/`.
- Small reconciliation CSV where justified, bounded, and reviewed, such as phrase-slot reconciliation extracts.
- Source scripts under `tools/` and lane `tools/` only in a separate tooling persistence wave — not mixed with campaign authority commits by default.

### Storage-suitable (`X:\AI MARS STORAGE\` — pointers only in repo)

- Commander import XLSX and multi-sheet campaign packages.
- Final launch checklist XLSX.
- Large CSV mirrors and export dumps.
- Client DOCX packs and approval deliverables.
- Bulky exports, screenshots, and binary evidence unless an explicit repo scope is chartered.

Repo references to Storage paths are navigation pointers only. They do not mutate Storage and do not prove Storage layout without operator verification.

### Do not commit by default

- `.tools-test-output/` — synthetic validator / release-gate outputs.
- `.tools/node-portable/` and `.tools/node-runtime/` — portable runtime bundles.
- Caches, temp dirs, generated build outputs, and unclassified pilot noise.
- Secrets, tokens, credentials, or live account identifiers beyond safe metadata flags.

## 5. Current dirty / WIP map

Audit snapshot — MASTER-15 evidence classification (2026-07-05).

This section is an evidence map, not final authority. Live git status counts may differ until persistence waves complete.

| Cluster | Approx. scale | Class | Notes |
|---|---:|---|---|
| `pilots/corvonero/` | ~161 untracked (MASTER-15); ~137 live preflight | E2 / E3 | Campaign V2.1–V2.6.2 manifests, Commander readiness, `client-approval/`, `landing-pages/`, lane tools |
| `projects/drive-avenue-yandex-direct/` | ~45 untracked | E2 / E3 | Phases 2b–4c drafts, launch checklists, Commander import drafts |
| `.tools-test-output/` | ~68 generated | E4 / H | Release-gate pass/fail fixtures, purity XLSX — no commit now |
| `reports/REPORT-corvonero-*` | 11 untracked | E2 | Wave reports for semantic cleanup, Commander recovery, client packs, release gates |
| `.tools/corvonero-*` (repo root) | 10 helpers | Helper / checkpoint | Export, checkpoint, template-recovery scripts — classify in tooling wave |
| Programme total (MASTER-15) | ~271 untracked | Mixed | Foreign WIP preserved; not auto-staged |

Explicitly out of scope for this index unless separately chartered:

- `projects/projects/` duplicate tree.
- ORCA live-model staged/noise reports unless ORCA-scoped.
- ATLAS modified Corvonero registers unless ATLAS-scoped.
- Unrelated FP/BZPM/recovery WIP elsewhere in `X:\AI MARS\`.
- `X:\AI MARS STORAGE\` artifacts — read/copy-in only with operator authorization.

Dirty WIP remains protected until scoped persistence waves (§7). This index does not authorize implicit cleanup or mass persistence.

## 6. Do-not-touch list

Unless a future task supplies an exact path list, operator charter, and rollback plan:

| Cluster | Reason |
|---|---|
| `.tools-test-output/` | Generated / synthetic — not campaign authority |
| `.tools/node-portable/` | Portable runtime bundle |
| `.tools/node-runtime/` | Portable runtime bundle |
| `projects/projects/` | Duplicate tree — inventory only |
| `X:\AI MARS STORAGE\` | Bulk layer — no agent mutation; pointer references only |
| ORCA live-model reports | Noise/staging unless ORCA-scoped task |
| ATLAS modified Corvonero registers | External registry lane unless ATLAS-scoped |
| Unrelated FP / BZPM / recovery WIP | Foreign programme scope |
| Live Yandex Direct / Commander / account surfaces | Platform mutation requires explicit operator charter |

## 7. Recommended persistence waves

Ordered human-operated waves — design targets only. No wave authorizes live import, launch, cleanup, or Storage mutation by itself.

| Wave | Purpose |
|---|---|
| MASTER-15C | Corvonero evidence — scoped commit-candidate audit (classify E2/E3, separate authority manifests from noise, Storage pointer reconciliation for XLSX/DOCX) |
| MASTER-15D | Drive Avenue — launch checklist and Commander draft persistence audit (`READY_FOR_OPERATOR_IMPORT_CHECK` lane) |
| MASTER-15E | Generated outputs / noise register — `.tools-test-output/`, duplicate-tree inventory, helper tool classification |
| MASTER-15F | Storage pointer reconciliation — document canonical Storage paths for import packages without moving bulk into git |
| MASTER-17 | Recovery / temp cleanup charter — design only; no cleanup authorization until operator-approved charter |

After MASTER-15C, update this index §3 and §5 with persisted paths and revised evidence classes.

## 8. Revision log

| Date | Wave | Change |
|---|---|---|
| 2026-07-05 | MASTER-15C | Created Search PPC operational index after MASTER-15B read-only design approval. |
