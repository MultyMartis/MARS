# Commander Transport Tooling

Project-local safe Commander transport layer for MARS Search PPC Production.

## Purpose

Consumes **explicit frozen Search PPC authority only**. Performs validation before any payload build or generation. Contains **no strategy logic**, no semantic dependency, no external API, no Git operations.

## Components

| Module | Role |
|--------|------|
| `filesystem-guard.mjs` | X: / AI WS boundary, approved write roots, FAIL_IF_OUTPUT_EXISTS |
| `template-validator.mjs` | Authentic Triumph template SHA + sheet structure |
| `authority-loader.mjs` | Manifest + SHA-256 + role policy |
| `transport-validator.mjs` | Pre-generation integrity (200-phrase limit, region, org, negatives, ads, UTM, bid ladder) |
| `bid-ladder.mjs` | Selectable bid policies: Triumph v1.3 (`TRIUMPH_DYNAMIC_SPREAD_V1_3`) and Corvonero cyclic (`CORVONERO_BALANCED_CYCLIC_10_RUB_V1`) |
| `payload-builder.mjs` | Per-campaign transport payloads with phrase-level bids |
| `commander-patcher-adapter.mjs` | CT-1 wrapper around Triumph exporter-cli ZIP patch |
| `cli.mjs` | Modes: validate, build-payload, generate, verify-output |

## Modes

```powershell
# Explicit mode required — default is STOP
node src/cli.mjs validate --manifest <path>
node src/cli.mjs validate --corvonero-frozen
node src/cli.mjs build-payload --manifest <path> --payload-out <dir>
```

`generate` and `verify-output` exist but are **not authorized** for real Corvonero authority in CT-1/CT-2.

## Security

- Writes allowed only under `projects/mars-search-ppc-production/`
- No `--force`; future overwrite requires `--overwrite-exact <absolute-file-path>`
- Forbidden authority roles: semantic_cache, semantic_run, generated_commander_xlsx, etc.
- Legacy `.tools/corvonero-commander-*.py` — **do not execute** (retired)

## Tests

```powershell
npm test
```

## Release gate

```powershell
npm run campaign:release-gate -- --project <id> --package <path> --authority <path> --receipt <path> --json
```

See `docs/release-gate/SEARCH-PPC-OPERATOR-RELEASE-WORKFLOW-v1.md`.

Synthetic XLSX patch tests write only to `projects/mars-search-ppc-production/.tools-test-output/`.

## Known Corvonero state

Validation against frozen authority **fails** on:

- `ca-01-specialist-search` — 384 > 200
- `ca-05-direct-service-order` — 201 > 200

CA-01 V2 regrouping (CT-4) required before generation.

## Template

`projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx`

SHA-256: `1112793a888ac2e0762317fa0bf728a116e36a143fc72fa0f5fe729c56c3f1fa`
