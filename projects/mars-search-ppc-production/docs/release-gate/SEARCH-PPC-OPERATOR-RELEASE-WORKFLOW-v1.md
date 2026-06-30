# Search PPC Operator Release Workflow v1

**Status:** OPERATIONAL ENTRY POINT  
**Release gate:** `tools/commander-transport` → `npm run campaign:release-gate`

## Workflow (13 steps)

1. **Collect source phrases** — MIG/ORCA intake (SPPC-01..04)
2. **Classify** — commercial intent admission (SPPC-05)
3. **Resolve HOLD** — operator adjudication; zero unresolved HOLD before approval
4. **Operator semantic approval** — create/sign `OPERATOR_SEMANTIC_APPROVED` receipt
5. **Freeze authority** — manifest + SHA-256 hashes locked (`AUTHORITY_FROZEN`)
6. **Generate from sanitized template** — `patchCommanderWorkbook` with sanitization phase
7. **Reopen actual XLSX** — artifact validator on every output file
8. **Run release gate** — `npm run campaign:release-gate -- --project <id> --package <path> --authority <path> --receipt <path>`
9. **Operator review package** — manifest, checksums, manual checklist
10. **Import into Commander** — operator only; set `COMMANDER_IMPORTED`
11. **Reconcile imported counts** — campaigns, groups, phrases, ads, metadata
12. **Apply manual negatives and region exclusions** — post-import operator actions
13. **Approve Direct launch** — explicit `LAUNCH_APPROVED` only

## Commands

```powershell
cd projects/mars-search-ppc-production/tools/commander-transport

# Pre-generation validation
node src/cli.mjs validate --manifest <authority-manifest.json>

# Build transport payloads
node src/cli.mjs build-payload --manifest <path> --payload-out <dir>

# Release gate (mandatory before import)
npm run campaign:release-gate -- --project corvonero --package <pkg> --authority <auth> --receipt <receipt.json> --json

# All tests
npm test
```

## Expected artifacts per release

- Frozen authority manifest + role JSON files
- Operator approval receipt
- Generated XLSX (per campaign) + TXT negatives (if policy)
- Package manifest + checksum manifest
- Release state file
- Release gate result JSON
- Validation evidence (cell-level for metadata)

## Bypass policy

No project-specific generator may skip sanitization, artifact validation, or release gate without an explicit exception record.

## Package immutability

Never overwrite existing release directories (V2.6, V2.6.1, etc.). New version = new directory.
