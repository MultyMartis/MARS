# RAW-KILL-SWITCH-FIX-BASELINE

Token: **D6D3B_RAW_KILL_SWITCH_FIX_EVIDENCE_SANITIZED**

Canonical fix (runtime-state only; live wrapper **not** committed):

1. Wrapper reads raw kill-switch JSON
2. Wrapper may validate separately
3. Producer receives exact raw contract expected by committed parser (includes `site_id`)
4. Wrapper no longer passes reduced parsed object without `site_id`
5. `site_id=SITE-002`; identity matches; mode remains DRY_RUN; ENABLED rejected

Commit contains sanitized contract/diff evidence only (see D6D3R `RAW-KILL-SWITCH-WRAPPER-FIX.md`).
