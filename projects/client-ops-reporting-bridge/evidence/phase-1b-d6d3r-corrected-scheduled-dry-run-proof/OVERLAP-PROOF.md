# Overlap Guards

1. Task Scheduler: `MultipleInstancesPolicy=IgnoreNew` (reconfirmed on task definition)
2. Producer singleton lock probe (`lock-probe` mode):
   - first acquire: OK
   - second acquire: `PRODUCER_LOCK_HELD` rejected
   - lock released after probe
   - token: `D6D3R_PRODUCER_LOCK_OVERLAP_REJECTED`

No second full scheduled run launched.

Token: `D6D3R_OVERLAP_GUARDS_RECONFIRMED`
