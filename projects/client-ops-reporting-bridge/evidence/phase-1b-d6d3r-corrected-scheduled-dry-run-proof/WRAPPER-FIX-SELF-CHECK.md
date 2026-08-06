# Wrapper Fix Self-Check R1–R10

Source: `logs/d6d3r-wrapper-fix-self-check.json` — **PASS**

| ID | Expectation | Result |
|----|-------------|--------|
| R1 | raw KS → SITE-002 accepted; wrapper passes `killSwitchRaw` | PASS |
| R2 | former parsed-object shape → SITE_MISMATCH | PASS |
| R3 | missing site_id → fail closed | PASS |
| R4 | wrong site_id → fail closed | PASS |
| R5 | missing mode → fail closed | PASS |
| R6 | ENABLED rejected by D6D3R charter | PASS |
| R7 | malformed JSON → fail closed | PASS |
| R8 | correct DRY_RUN raw → gate pass, no delivery | PASS |
| R9 | request path prohibited | PASS |
| R10 | activation/Telegram/DT mutation methods prohibited | PASS |

Token: `D6D3R_WRAPPER_FIX_SELF_CHECK_PASS`
