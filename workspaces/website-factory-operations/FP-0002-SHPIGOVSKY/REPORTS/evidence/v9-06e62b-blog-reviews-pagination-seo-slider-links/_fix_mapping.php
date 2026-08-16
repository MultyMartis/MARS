<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$ev = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links";
$fh = fopen("$ev/demo-blog-image-mapping.csv", "wb");
fputcsv($fh, ["title","post_id","attachment_id","attachment_url","action"]);
for ($i=1;$i<=10;$i++) {
  $title = sprintf("Демо-статья для проверки пагинации — %02d", $i);
  $p = get_page_by_title($title, OBJECT, "post");
  $id = $p instanceof WP_Post ? (int)$p->ID : 0;
  $aid = $id ? (int)get_post_thumbnail_id($id) : 0;
  fputcsv($fh, [$title, (string)$id, (string)$aid, $aid?wp_get_attachment_url($aid):"", $aid?"assigned_present":"missing"]);
}
fclose($fh);
echo "rewrote mapping\n";

// founder ownership before/after note
file_put_contents("$ev/founder-ownership-before-after.md", <<<MD
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
MD);
echo "founder note ok\n";
