# Producer Architecture (D2)

```text
normalized source / fixture
  → existing validator + envelope builder
  → producer request builder
  → sequential dispatch guard (concurrency=1)
  → transport: disabled | fixture | mock | http(BLOCKED)
  → response classifier + retry planner (no auto retry)
  → sanitized evidence writer
```

No daemon. No queue. No database. No scheduler.
