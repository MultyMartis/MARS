# RAW ACCESS PASS VS DENIED v1

Same operator identity: ADMIN_A (`access_code` 24701D, role admin active when registry readable).

| | RAW_ACCESS_PASS_LEAD | RAW_ACCESS_DENIED_LEAD |
|---|---|---|
| Exec | 33304 | 33500 (also 33501, 33502 same minute) |
| MSK | 2026-08-17 08:41:14 | 2026-08-17 14:26:27 |
| callback_data | `sm:i:<token>` | `sm:i:<token>` |
| action | raw_source | raw_source |
| CONFIG read | OK (`config_map` 236 keys, environment=production) | fail `invalid_grant` |
| ACCESS read | OK | fail `invalid_grant` |
| authorized | true | false |
| auth_role | admin | public (unresolved) |
| deny_reason | null | registry_unavailable |
| Handle Callback | raw_inspected / viewed | **not reached** |
| Telegram | raw text returned | Answer Callback Deny hardcoded permission text |

Tokens and lead_ids not committed. PASS vs DENIED are different cards/tokens; the authorization divergence is registry read success vs failure, not staff-set difference.
