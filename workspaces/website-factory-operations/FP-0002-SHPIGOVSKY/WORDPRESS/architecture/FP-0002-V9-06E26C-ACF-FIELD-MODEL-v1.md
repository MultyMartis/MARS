# FP-0002 V9-06E26C ACF Field Model v1

**Group:** `group_fp02_blog_post_article_meta`  
**Location:** `post_type == post`

## Preserved fields

- `article_source_label`, `article_reading_time`, `article_disclaimer`
- `article_hide_author_public`, `article_show_date_public`, `related_posts`

## Added fields

| Field | Type | Role |
|---|---|---|
| `article_eyebrow` | text | optional hero eyebrow |
| `article_lead` | textarea | lead override (fallback excerpt) |
| `article_author_label` | text | author override |
| `article_show_toc` | true_false | TOC toggle (default on) |
| `article_toc_title` | text | TOC heading |
| `article_conclusion_heading` | text | conclusion H2 |
| `article_conclusion_quote` | textarea | founder quote block |
| `article_source_items` | repeater | bibliography |
| `article_faq_items` | repeater | optional FAQ |
| `article_final_cta_*` | text/textarea/url | per-article CTA override |
| WPilot metadata | text | passive only |

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/acf-field-model-result.json`
