# Production invariants — Phase 3G.2.2

**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

| Invariant | Value |
|-----------|-------|
| Operational.dev | active, **45** nodes, sole Gmail intake |
| Admin.dev | active, **85** nodes, same workflow patched in place |
| Sales-Manager-v2 | **inactive** |
| AI | **OFF** |
| Reminders | **OFF** |
| Workflows created | **0** |
| Reply profiles | 1 ADMIN_A Андрей enabled · 2 MOD_B_REVOKED Оля disabled/revoked · 3 MOD_A Михаил enabled · 4 MOD_C_REVOKED Никита disabled/revoked |
| Authoritative profile rows | 4 |
| Duplicate profile rows | 0 |
| Divergent profile read paths | 0 (unified resolver contract across all 8 read paths) |
| Unsafe name fallbacks (display/username/nickname → client copy) | 0 |
| Access-role changes | 0 |
| Production leads modified | 0 |
| Historical drafts modified | 0 |
| LEADS / LEAD_EVENTS writes by this phase | 0 |

Stats posture unchanged by this phase — epoch and counts remain as last recorded by operator evidence unless an independent real lead arrives.
