# SCHEDULER-OVERLAP-PROOF

1. Task XML `MultipleInstancesPolicy=IgnoreNew`
2. Producer lock probe: first acquire OK; second rejected `PRODUCER_LOCK_HELD`; lock released
3. No second full scheduled producer evaluation performed

Token: D6D3_SCHEDULER_AND_PRODUCER_OVERLAP_GUARDS_VERIFIED

