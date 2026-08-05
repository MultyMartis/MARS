# REQUEST AMPLIFICATION ROOT CAUSE v1

## Confirmed BEFORE

- Empty poll wrote one CONFIG runtime key every ~30 seconds: about 120 writes/hour.
- Full delivery performed multiple broad reads before claim.
- LEAD_DELIVERIES was read as a full tab (roughly 52 observed rows).
- Success processing amplified CONFIG writes.
- No workflow-level single-flight guard existed.

## Confirmed AFTER

- Empty poll Sheets writes: 0.
- Final schedule: `minutesInterval=2`. The attempted `secondsInterval=120` form was rejected by n8n as an invalid interval.
- Bounded ledger read returned one item for the proof lead.
- CONFIG, ACCESS_CONTROL and ledger were each read once.
- Two claims and two delivered stamps succeeded without quota.
- Two recipient fallback guards were reconciled after the synthetic Gmail failure.

Root-cause mitigation is live-proven. Google Sheets still has no atomic transaction; fail-closed/reconciliation semantics remain required.
