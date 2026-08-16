# DOCX INTEGRATION — PROD-P16

`DocxImporter` writes `post_content` via `wp_insert_post` and does **not** embed a second typography engine.

Imported articles render through:

1. `the_content` → TOC heading IDs (priority 5)  
2. `the_content` → `TypographyFilters::filter_html_content` (priority 20)

Therefore:

`DOCX-IMPORTED ARTICLES FOLLOW THE SAME TYPOGRAPHY PIPELINE`
