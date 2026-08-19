# Indexing mutation path inventory — P18G

| # | Path | Mechanism | P18G status |
|---|------|-----------|-------------|
| 1 | `IndexingControl::handle_admin_post` | POST + nonce + confirm + close ack | Human-only close |
| 2 | `IndexingControl::request_state()` | Guarded API | Close requires `explicit_human_authorization` or charter const |
| 3 | `IndexingControl::set_site_indexability()` | Legacy wrapper | Close blocked (open-only auth by default) |
| 4 | `pre_update_option_blog_public` filter | Blocks direct `blog_public=0` | Active |
| 5 | `_fu01_runtime_closeout.py::close_indexing` | wp_eval | Would fail guard now |
| 6 | `_p18b_02_deploy_qa.py` | QA open/close cycle | Historical QA only |
| 7 | WP Admin → Settings → Reading | Core UI | Close blocked via filter |
| 8 | WP-CLI `option update blog_public 0` | CLI | Blocked via filter |
| 9 | `IndexingWatchdog::run_check` | Cron | Read-only + alert |
| 10 | Theme `seo-integrations.php` | Sitemap note only | No mutation |
| 11 | WPilot | read-only verification | No indexing mutation documented |

**Dangerous removed/neutralized:** FU01 «re-close because baseline says CLOSED» — **blocked**.
