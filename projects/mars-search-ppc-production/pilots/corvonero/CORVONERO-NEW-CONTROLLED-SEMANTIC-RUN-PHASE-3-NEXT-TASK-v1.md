# CORVONERO NEW CONTROLLED SEMANTIC RUN — PHASE 3 NEXT TASK v1

**Status:** **BLOCKED** — prerequisite Gate B SPPC-05 pass not met  
**Run ID (current):** `corv-semantic-v2-20260626-002`  
**Current lifecycle:** `BLOCKED_AT_SPPC_05`

---

## Prerequisite (not met)

```text
SPPC-05: PASS — OPERATOR REVIEW REQUIRED
Project: FROZEN_PENDING_CANARY_AUTHORIZATION
```

Current state:

```text
SPPC-05: FAILED
Project: BLOCKED_AT_SPPC_05
```

---

## Blocked until operator resolves

1. Review `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.md`
2. Decide on ORCA Wave 3.1F repair scope (product SAP update false accept; problem-query ABSTAIN policy)
3. Authorize **new SPPC-05 attempt** after repair (may require new run ID if authority mismatch)

---

## Phase 3 scope (when authorized)

**Task ID (future):** `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-3-CANARY`

| Parameter | Planned value |
|-----------|---------------|
| Canary size | 120 phrases |
| Review sample | 30 |
| Provider | openrouter |
| Model | openai/gpt-5-mini |
| Gate | C — operator review before full corpus |

**Explicitly forbidden without separate authorization:** full 2368 corpus, Wave 5, strategy, Campaign Architecture, Commander, import, launch.

---

## Entry criteria (future)

- Gate B = `PASS — OPERATOR REVIEW REQUIRED` with operator sign-off
- Same or new approved run ID per repair outcome
- Active lock on STORAGE root
- Cost cap confirmed for canary batch

---

## Expected outputs (future)

- Canary batch receipt (STORAGE)
- Canary class distribution report (Git sanitized)
- Operator review sample manifest
- Gate C decision record

**Next gate after Phase 3 (if pass):** Gate C operator review → Phase 5 bounded batches (separate authorization).
