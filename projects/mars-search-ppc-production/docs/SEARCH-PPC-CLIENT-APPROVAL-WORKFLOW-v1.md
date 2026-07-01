# Search PPC client approval workflow v1

## Generated artifacts

| Artifact | Audience |
|----------|----------|
| Ad approval workbook | Client |
| Strategy/research document | Client |
| Semantic appendix | Client |
| Commercial claims register | Internal + client confirmation |
| Launch-readiness register | Internal |
| Client approval receipt | Evidence |
| Feedback intake | Operator |

## Artifact edit states

GENERATED → MANUALLY_EDITED → MANUAL_STABLE → SUPERSEDED → ARCHIVED

See `GENERATED-ARTIFACT-MANUAL-STABLE-POLICY-v1.md`.

## Client lifecycle states

After artifact validation:

`CLIENT_APPROVAL_PENDING` → `CLIENT_APPROVED` → (import gates)

Corvonero current: **CLIENT_FEEDBACK_PENDING** — materials sent 2026-07-01, no response recorded.

## Change policy

Classify feedback via `CORVONERO-CLIENT-FEEDBACK-INTAKE-v1` change classes. Commercial claim changes require client reconfirmation.

## Blocks

- No Commander import while CLIENT_FEEDBACK_PENDING on ads/commercial claims
- No launch implied in client-facing materials
