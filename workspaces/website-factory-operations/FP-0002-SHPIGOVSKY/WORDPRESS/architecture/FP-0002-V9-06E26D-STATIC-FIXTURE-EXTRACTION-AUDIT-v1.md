# FP-0002 V9-06E26D Static Fixture Extraction Audit v1

Static source: `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\src\partials\sections\blog-article-content.html`

- **canonical_route** → post permalink (post_name=nazvanie-stati)
- **title** → post_title (SEED)
- **slug** → post_name (SEED)
- **lead** → article_lead ACF (SEED)
- **card_excerpt** → post_excerpt (SEED)
- **date** → post_date (SEED)
- **reading_time** → article_reading_time (SEED)
- **author** → article_author_label + hide=0 (SEED)
- **featured_image** → theme fallback (NO_UPLOAD)
- **body** → post_content (SEED)
- **conclusion_quote** → article_conclusion_quote (SEED)
- **sources** → article_source_items (SEED)
- **faq** → hidden (SKIP)
- **related** → hidden (1 post) (SAFE_EMPTY)
- **final_cta** → archive CTA fallback (TEMPLATE_FALLBACK)