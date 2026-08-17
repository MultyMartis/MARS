# RAW ACCESS ADMIN_A LIVE PROOF v1

| Case | Result |
|---|---|
| Historical PASS 33304 | ADMIN_A + payload path returned «Исходная заявка» (pre-OAuth-break) |
| Historical DENIED 33500–33502 | ADMIN_A + registry_unavailable shown as permission deny (pre-patch) |
| Post-patch live ADMIN_A retest | **NOT RUN** — Sheets OAuth still `invalid_grant` at post-probe; a live callback would still fail registry read (now with truthful unavailable text) |
| Unauthorized synthetic | isolated harness only — no Telegram |
| Moderator test messages | **0** |
| Customer test messages | **0** |

Do not ask moderators to press raw buttons for this phase.
