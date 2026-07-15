<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$q = new WP_Query(["post_type"=>"service","posts_per_page"=>5,"post_status"=>"publish"]);
foreach ($q->posts as $p) {
  echo get_permalink($p) . " tpl=" . get_page_template_slug($p->ID) . " type=" . $p->post_type . "\n";
}
