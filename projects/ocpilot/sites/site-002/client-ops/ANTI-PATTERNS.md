# SITE-002 — Anti-Patterns (DO NOT)

DO NOT:

1. Rely on operator workstation for normal production reporting.
2. Use a visible interactive Scheduled Task for background production.
3. Run duplicate local and server producers.
4. Treat offers absence as full success.
5. Assume literal `offer.xml` as the offers contract.
6. Use broad stale backlog selection (naive oldest-first).
7. Use secret-name aliases inconsistently.
8. Use stale `_current` as watchdog truth without validation.
9. Couple terminal recording to outbound dispatch.
10. Allow manual import to bypass the canonical runner.
11. Run concurrent imports (`MAX_SAFE_IMPORT_CONCURRENCY` must stay 1).
12. Create uncontrolled retries.
13. Delete historical workstation tasks before proving server replacement.
14. Use Google Sheets as assumed BZPM operational memory.
15. Treat n8n Data Table as automatically the forever architecture (document successor; do not force migration here).
16. Broad reset/clean dirty MARS MAIN / foreign WIP.
17. Store secrets in Git/reports.
18. Repeat watchdog cron tokens from screenshots/chats.
19. Claim offers root cause closed without STOP CONDITIONS.
20. Redesign live importer/reporting in a docs-only wave.
