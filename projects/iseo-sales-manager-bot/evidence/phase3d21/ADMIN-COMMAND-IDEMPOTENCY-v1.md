# ADMIN COMMAND IDEMPOTENCY v1

**Phase:** 3D.2.1  
**Decision:** **NO PATCH**

## Rationale

Forensic classification for the observed double `/start` panel was **expected_harness_overlap** (two intentional harness executions), not same-update reprocessing.

Requirements for an idempotency guard (stable update/message key, bounded retention, no long-term block of legitimate repeats) are therefore **not required** for this defect class.

## Behavior retained

- A genuinely new `/start` still receives exactly one reply per execution.
- Unauthorized `/start` still returns `Доступ запрещён.`
- Optional future guard may be chartered separately if a real Trigger same-`update_id` duplicate is observed.

## Explicitly not done

- No Static Data / CONFIG command lock table
- No new workflow
- No private ID storage in Git evidence
