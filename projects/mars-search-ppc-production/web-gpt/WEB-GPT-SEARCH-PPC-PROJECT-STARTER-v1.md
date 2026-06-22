# Web-GPT Search PPC Project Starter v1

**Status:** `CONTRACT INTEGRATION — NOT UI RUNTIME`  
**Honesty:** The repository cannot intercept every Web-GPT message. Enforcement is via contracts, handoff validation, and operator discipline.

---

## Canonical project starter (paste at chat open)

```text
MARS Search PPC — lifecycle-gated session
Project: <project_id>
Manifest: <manifest_path>
Gate check: node projects/mars-search-ppc-production/runtime/cli/search-ppc-gate.mjs --manifest <manifest_path> --action <lifecycle_action> --stage <SPPC-NN>
Validator: node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest_path>
Current stage: <from manifest>
Blockers: <from gate output>
Allowed work: <from gate output>
Forbidden: downstream stages, invented substitutes, diagnostic-as-production
```

## Lifecycle status handoff generator

```bash
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs report <manifest> --out-md handoff.md --out-json handoff.json
node projects/mars-search-ppc-production/runtime/cli/validate-webgpt-handoff.mjs handoff.md
```

## Blocked-response contract

If gate returns `BLOCKED`, first response must be exactly:

```text
BLOCKED — LIFECYCLE REQUIREMENT NOT MET
```

## Classification

| Layer | Status |
|-------|--------|
| Contract integration | **Approved** |
| Generated handoff | **Available** |
| Handoff validation | **Executable** (`validate-webgpt-handoff.mjs`) |
| UI/runtime enforcement | **NOT OPERATIONAL** |

## Chat resynchronization

On manifest or stage change: regenerate handoff, re-run gate, paste updated status block from [WEB-GPT-OPENING-STATUS-BLOCK-v1.md](./WEB-GPT-OPENING-STATUS-BLOCK-v1.md).
