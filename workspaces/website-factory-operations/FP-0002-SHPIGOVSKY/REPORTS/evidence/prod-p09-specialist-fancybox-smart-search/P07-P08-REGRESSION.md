# PROD-P09 — P07/P08 Regression Smoke

HTTP + Playwright spot checks after exact-file deploy (6 theme files only).

| Surface | Result |
|---------|--------|
| Specialist structured template (`kostyuk`) | intact (`data-content-status="specialist-structured"`) |
| Certificate grid layout | intact; Fancybox opens |
| Comfort Fancybox | opens / closes |
| Existing Fancybox binds in shell | present |
| Home / uslugi / blog / o-centre routes | no PHP Fatal/Parse in HTML |
| Lifebuoy asset/script references | present on sampled pages |
| WPilot `write_enabled` | **false** (public ping) |
| Unrelated P07 Lorem/DEMO cleanup | not re-touched (no deploy of those files) |

No unrelated fixes performed in this wave.
