<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$counts = (array) wp_count_posts("page");
echo "PAGE_COUNTS=" . json_encode($counts) . "\n";
$pc = (array) wp_count_posts("post");
echo "POST_COUNTS=" . json_encode($pc) . "\n";
$sc = (array) wp_count_posts("service");
echo "SERVICE_COUNTS=" . json_encode($sc) . "\n";
$pages = get_posts(["post_type"=>"page","post_status"=>"any","numberposts"=>-1,"orderby"=>"ID","order"=>"ASC"]);
foreach ($pages as $p) {
  echo "PAGE id={$p->ID} status={$p->post_status} parent={$p->post_parent} slug={$p->post_name} title={$p->post_title}\n";
}
$posts = get_posts(["post_type"=>"post","post_status"=>"any","numberposts"=>-1]);
foreach ($posts as $p) {
  echo "POST id={$p->ID} status={$p->post_status} slug={$p->post_name} title={$p->post_title}\n";
}
