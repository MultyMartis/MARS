# SITE-002 — Deep Research Backlog (future Web-GPT phase)

**Do NOT run web research in this knowledge consolidation phase.**

| # | QUESTION | WHY IT MATTERS | CURRENT ASSUMPTION | WHAT DECISION IT MAY CHANGE |
|---|----------|----------------|--------------------|-----------------------------|
| 1 | Best architecture for small 1C/OpenCart import observability | Scale & maintainability | Custom wrapper + n8n OK for low volume | Whether to keep custom wrappers |
| 2 | Run-state/event modeling | Consistency | Terminal + event_id split | Schema for DB successor |
| 3 | PostgreSQL vs n8n Data Table | State authority | Data Table OK now; PG later | Migration timing |
| 4 | Idempotency patterns | Alert quality | Replay≠new run | Dedupe keys |
| 5 | Watchdog design | Silence detection | Server cron + freshness checks | Watchdog SLA |
| 6 | File-arrival race detection | Offers missing | Possible race contributor | Wrapper start policy |
| 7 | CommerceML observability | Partial exchange | Filename families contract | Monitoring metrics |
| 8 | Detecting partial 1C exchange | ATTENTION semantics | OFFERS_INPUT_MISSING | Classification taxonomy |
| 9 | Offers/prices/stock integrity monitoring | Business impact | ATTENTION alerts sufficient short-term | Extra integrity jobs |
| 10 | Telegram operational UX | Operator load | Russian concise factual | Formatter redesign |
| 11 | Alert fatigue / severity | Noise | Daily new events for recurring ATTENTION | Severity levels |
| 12 | Server-side scheduler architecture | Hosting limits | Beget cron + operator create | Move scheduler elsewhere |
| 13 | OpenCart/ocStore 1C failure patterns | Reuse | SITE-002 lessons apply | Playbook expansion |
| 14 | Migration away from custom wrappers | Complexity | Wrappers accepted now | Build vs buy |
| 15 | Multi-site Client Ops platform | Tenancy | Site config template | Shared service vs copies |
| 16 | n8n orchestration-only vs state in DB | Authority | n8n+Data Table current | State ownership |
