# PROVENANCE-MATRIX-v1

Sanitized matrix (no phone/email). Classification requires corroborating evidence — name alone → SAFE_UNKNOWN.

| Lead stable ID (prefix) | Display (sanitized) | Source identity (prefix) | Status (pre) | Category hint | Classification | Action |
|-------------------------|---------------------|--------------------------|--------------|---------------|----------------|--------|
| lead_synth_p3b1_c01 | (empty)/test-like | msg_synth_C01_* | pending/new | Audit-ish | PROVEN_SYNTHETIC | archive by row |
| lead_synth_p3b1_c02 | Синтетик* | msg_synth_C02_named_seo | pending | SEO | PROVEN_SYNTHETIC | archive |
| lead_synth_p3b1_c08 | (empty) | msg_synth_C08_* | pending | — | PROVEN_SYNTHETIC | archive |
| lead_synth_p3b2_TG1 | (empty) | msg_synth_p3b2_TG1 | pending | — | PROVEN_SYNTHETIC | archive |
| lead_msg_synth_3d8_* / 3e1* / 3e2* / 3e21* / 3e22* | various | msg_synth_* | pending | — | PROVEN_SYNTHETIC | archive |
| PROBE_phase3e22-* | probe | msg_probe_* | pending | — | PROVEN_TEST | archive |
| name-only `test` / Synth* without synth id | candidate | (no synth marker) | pending | — | SAFE_UNKNOWN | **no mutate** |
| production lead_* | real | gmail/other | pending | Audit/SEO/Other | PRODUCTION_REAL | untouched |

## Provenance rules applied

PROVEN only if ≥1 of: `SYNTHETIC_TEST` text, `lead_synth_` / `msg_synth_`, `PROBE_` / `msg_probe_`, `is_probable_test`, fixture flags, PHASE_3 marker.

Counts pre-cleanup (unique-ish dry): PROVEN pending unique **49**; row-level pass1+pass2 archived **49 + 23** row updates covering remaining duplicate copies → **proven_pending_after = 0**.
