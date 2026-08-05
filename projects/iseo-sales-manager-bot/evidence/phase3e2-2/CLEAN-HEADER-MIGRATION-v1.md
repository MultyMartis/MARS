# CLEAN HEADER MIGRATION v1

Live CLEAN mapping columns: **65**.

Present: `first_reply_text`, `quality_comment`.  
Missing dedicated: `first_reply_version`, `first_reply_mode`, `first_reply_ready`, `first_reply_omitted_reason`, `meaningful_theme`, `human_reply_style_version`, linter fields.

**No live additive migration this phase** — Sheets full-path still rate-limited. Continue quality_comment carrier + stored first_reply_text. Plan append-only headers when Sheets window is healthy. No historical bulk regeneration.
