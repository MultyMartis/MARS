# Founder's Word ownership — E62B

## Before
- Context slug: `fp02-block-founder-quote` (menu existed)
- ACF field group: **missing** (not in `get_fielded_block_slugs()`, no PHP group, no JSON)
- Frontend: `shpigovsky_get_founder_quote_block_context_data()` → empty options → **static V9 fallbacks**
- Blog page: toggle `blog_archive_show_founder_word` only (no duplicate content fields) — already E61 shape

## After
- ACF group `group_fp02_block_founder_quote` registered in plugin + JSON delivered to runtime
- Options page `fp02-block-founder-quote` now fielded
- Seeded if empty: paragraphs (4), name, role, CTA label, photo `#754`
- Blog retains visibility toggle only; content owned by reusable block
- Visible frontend text/image/name preserved (same copy as prior static fallbacks)