<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$items = shpigovsky_get_reviews_items(["featured_only"=>false,"limit"=>0]);
$ppp = shpigovsky_get_reviews_per_page();
$rows = [];
foreach ($items as $i => $item) {
  $page = (int)floor($i / $ppp) + 1;
  $id = (int)($item["review_id"] ?? ($i+1));
  $rows[] = [
    "review_id" => (string)$id,
    "author" => (string)($item["author"] ?? ""),
    "archive_page" => (string)$page,
    "archive_url" => shpigovsky_get_review_archive_url($id),
    "featured" => !empty($item["featured"]) ? "1" : "0",
  ];
}
$fh = fopen("X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links/review-anchor-destination-matrix.csv", "wb");
fputcsv($fh, array_keys($rows[0]));
foreach ($rows as $r) fputcsv($fh, array_values($r));
fclose($fh);

$blog_ppp = (int)get_field("blog_archive_posts_per_page", (int)get_option("page_for_posts"));
$q = new WP_Query(["post_type"=>"post","post_status"=>"publish","posts_per_page"=>-1,"fields"=>"ids"]);
$total_posts = count($q->posts);
$blog_pages = (int)ceil($total_posts / max(1,$blog_ppp));
file_put_contents("X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links/pagination-summary.json", json_encode([
  "blog_posts_per_page" => $blog_ppp,
  "blog_total_posts" => $total_posts,
  "blog_pages" => $blog_pages,
  "reviews_per_page" => $ppp,
  "reviews_total" => count($items),
  "reviews_pages" => (int)ceil(count($items)/max(1,$ppp)),
], JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE));
echo "OK matrix\n";
