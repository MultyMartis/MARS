# D6D-FAIL-CLOSED-BEHAVIORS

| Case | Behavior |
|------|----------|
| No candidate | success/no candidate; no activation; no request |
| SENT | already handled; no resend |
| PENDING | reconciliation/operator review; no activation; no resend |
| FAILED | terminal/recovery charter; no automatic resend |
| STALE_REVIEW_REQUIRED | no activation; no request |
| NOT_SAFE_TO_SEND / BLOCKED | no activation; no request |
| Artifact conflict | no activation; no request; operator review |
| Ambiguous request | no second POST; reconciliation; re-contain |
| Containment failure | highest severity; stop producer; block future sends pending recovery |
