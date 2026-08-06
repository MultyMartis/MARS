# LOCK-OVERLAP-BASELINE

Token: **D6D3B_OVERLAP_EVIDENCE_ACCURATE**

Two protection layers:

1. Task Scheduler: `MultipleInstancesPolicy=IgnoreNew`
2. Producer: singleton lock

Accepted proof (D6D3R): first lock acquisition succeeded; second lock probe returned `PRODUCER_LOCK_HELD`; no second full producer run; lock released; no residual lock/process (locks count=0 at D6D3B reconfirm).
