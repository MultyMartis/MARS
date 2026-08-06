# PRE-ACTIVATION-PREFLIGHT

**Token:** `D6C_PRE_ACTIVATION_PREFLIGHT_DEFINED` · `D6C_INITIAL_INACTIVE_INVARIANT_DEFINED` · `D6C_FRESHNESS_GATE_PRECEDES_ACTIVATION` · `D6C_DEDUPE_PRECHECK_BEFORE_ACTIVATION`

Gates: allowlisted workflow_id; active=false; version pin; running=0; charter valid; budget>0; retries=0; concurrency=1; FRESH_AND_ELIGIBLE; event_id; unseen for FIRST_SEEN; webhook/auth structural; no conflicting lock.

Unexpected active before charter → fail/stop or explicit recontain then restart — never silent inherit.
