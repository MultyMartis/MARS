# Web-GPT Opening Status Block v1

**Authority:** [WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md](./WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md)  
**Lifecycle status:** `APPROVED — IMPLEMENTATION AUTHORIZED`

Copy into the start of every Search PPC project chat:

```text
Project: <project_id>
Manifest: <path to project-ppc-state-manifest.json>
Lifecycle version: 1.0.0
Current stage: <SPPC-NN>
Completed approved stages: <list>
Authoritative inputs: <artifact paths>
Blocking gaps: <none | list>
Allowed work: <stage-bounded work only>
Forbidden work: <e.g. Commander Export, Campaign Architecture>
Expected output: <artifact_type per lifecycle contract>
Validation required: node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>
```

If any blocking gap exists, first response must be:

```text
BLOCKED — LIFECYCLE REQUIREMENT NOT MET
```

---

## MARS synchronization instruction (paste into Web-GPT source/sync pack refresh)

```text
MARS Search PPC sync — lifecycle v1 APPROVED.
Authority: projects/mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md
Every search PPC chat MUST read project PPC state manifest before work.
Validator: node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>
Rules: no stage skipping; full production corpus only; human review is not default classification engine;
missing evidence → BLOCKED — LIFECYCLE REQUIREMENT NOT MET; no invented substitutes.
Corvonero: FROZEN — read-only manifest only.
P0-I pilot: DIAGNOSTIC EVIDENCE only.
Do not duplicate 23 stage contracts into chat — link canonical paths.
```
