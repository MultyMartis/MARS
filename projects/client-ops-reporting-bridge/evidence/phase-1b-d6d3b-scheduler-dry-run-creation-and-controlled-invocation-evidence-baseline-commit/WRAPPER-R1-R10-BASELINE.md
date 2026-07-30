# WRAPPER-R1-R10-BASELINE

Token: **D6D3B_WRAPPER_SELF_CHECK_BASELINE_ACCURATE**

| ID | Result | Summary |
|----|--------|---------|
| R1 | PASS | correct raw kill-switch accepted |
| R2 | PASS | former parsed/reduced shape rejected / reproduces historical failure |
| R3 | PASS | missing site_id fails closed |
| R4 | PASS | wrong site_id fails closed |
| R5 | PASS | missing mode fails closed |
| R6 | PASS | ENABLED rejected |
| R7 | PASS | malformed JSON fails closed |
| R8 | PASS | correct DRY_RUN passes kill-switch gate without delivery |
| R9 | PASS | request path prohibited |
| R10 | PASS | activation/Telegram/Data Table mutation methods prohibited |

Source: D6D3R `WRAPPER-FIX-SELF-CHECK.json` (`pass: true`).
