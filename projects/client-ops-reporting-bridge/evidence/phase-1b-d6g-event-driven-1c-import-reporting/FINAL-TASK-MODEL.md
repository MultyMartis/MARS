# Final Task Model

| Task | Purpose | Schedule | Sends success/error? | Watchdog-only? |
|------|---------|----------|----------------------|----------------|
| Beget SITE-002 MARS 1C Import Wrapper | Start canonical import | 0 8 * * * Moscow | No (import only) | No |
| MARS_SITE_002_Import_Completion_Poller | Fetch pending terminals + dispatch | every 2 min 11:50–14:00 Barnaul | Yes (completion path) | No |
| MARS_SITE_002_Post_1C_Catalog_Monitor | Sitemap hygiene monitor | 12:30 Barnaul | No (hygiene) | No |
| MARS_SITE_002_Client_Ops_Producer | REPURPOSED → no-import watchdog entry | 13:00 Barnaul | Only NO_FRESH when applicable | Yes |
| MARS_SITE_002_No_Import_Watchdog | Explicit watchdog (alias/action) | 13:00 Barnaul | Only NO_FRESH | Yes |

Normal success/error delivery is completion-dispatch only — not the 13:00 producer backlog selector.
