# REPAIR-DESIGN

## Before / after matrix

| Case | Input | Before (bug) | After (repair) |
|------|-------|--------------|----------------|
| A | Python `ONBOARDING_REQUIRED` + `SYNTHETIC_ONBOARDING_ACTION`, exit 0 | Runner defaults `NO_ACTION_REQUIRED` and overwrites | Preserve monitor class/action |
| B | Python `NO_ACTION_REQUIRED`, exit 0 | Accidental match / or overwrite with same | Preserve |
| C | Python `HYGIENE_REVIEW_REQUIRED` | Overwrite to `NO_ACTION_REQUIRED` | Preserve |
| D | Python `FAILURE_REVIEW_REQUIRED` present | May overwrite next_action text | Preserve monitor semantics |
| E | run-summary missing class; `monitor-classification.json` present | Invent `NO_ACTION_REQUIRED` | Prefer monitor-classification |
| E2 | Summary present, class missing everywhere | Invent `NO_ACTION_REQUIRED` | `FAILURE_REVIEW_REQUIRED` fail-safe |
| F | No monitor summary (failed before artifacts) | Runner failure defaults | Runner failure defaults OK; invariant N/A |

## Non-goals

- No Python classification logic change
- No scheduler/runtime architecture change
- No D4 adapter weakening
- No freshness threshold redesign

## Preferred semantic model (implemented)

If canonical run-summary already contains non-empty `classification` / `next_action` → preserve.  
Runner may enrich duration/timestamps/exit metadata.  
Never insert `NO_ACTION_REQUIRED` merely because runner-local classification was empty when Python already emitted a valid class.
