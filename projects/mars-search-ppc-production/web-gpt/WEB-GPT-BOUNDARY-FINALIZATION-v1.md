# MARS Search PPC — Web-GPT Boundary Finalization v1

**Date:** 2026-06-23  
**Wave:** 1.2  
**Maturity:** `IMPLEMENTED — REPOSITORY ENFORCEMENT`  
**UI runtime:** `UNAVAILABLE`

---

## Implemented repository enforcement

| Capability | Path | Status |
|------------|------|--------|
| Execution contract | `web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md` | Implemented |
| Opening status block | `web-gpt/WEB-GPT-OPENING-STATUS-BLOCK-v1.md` | Implemented |
| Project starter | `web-gpt/WEB-GPT-SEARCH-PPC-PROJECT-STARTER-v1.md` | Implemented |
| Handoff validator CLI | `runtime/cli/validate-webgpt-handoff.mjs` | Implemented |
| Sync pack reference | `web-gpt-sources/WEB-GPT-CHAT-SYNC-PACK.md` | Updated (Wave 1.1 checkpoint) |

---

## Not implemented (platform boundary)

Web-GPT UI runtime interception is **unavailable**. Chat output cannot be blocked at the UI layer from this repository.

Classification: `PLATFORM BOUNDARY — CONTROLLED`

---

## Authority registration rule (Wave 1.2)

Web-GPT outputs **cannot** become project authority until:

1. Saved as a repository artifact (file with declared path)  
2. Validated against the handoff contract (`validate-webgpt-handoff.mjs`)  
3. Registered in the project PPC state manifest with correct `output_class`

Until all three conditions are met, chat output remains **`proposal`** only.

---

## Resynchronization procedure

1. Read project manifest and run lifecycle validator  
2. Paste opening status block from `WEB-GPT-OPENING-STATUS-BLOCK-v1.md`  
3. Confirm current SPPC stage and blockers  
4. Execute only allowed work per contract  
5. Write handoff artifact; run `validate-webgpt-handoff.mjs` before manifest registration  

---

## Required blocker response

```text
BLOCKED — LIFECYCLE REQUIREMENT NOT MET
```

Follow with exact missing evidence, owner, and forbidden downstream work.

---

## Wave 2 impact

Does **not** block Wave 2 authorization when repository-side handoff validation is mandatory before authority registration.
