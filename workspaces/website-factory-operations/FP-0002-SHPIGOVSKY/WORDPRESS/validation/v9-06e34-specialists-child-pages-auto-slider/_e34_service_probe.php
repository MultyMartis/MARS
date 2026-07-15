<?php
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
// Find alcohol leaf or service that renders specialists
$q = get_posts(["post_type"=>"service","name"=>"lechenie-alkogolizma","post_status"=>"publish","numberposts"=>3]);
if (!$q) {
  $q = get_posts(["post_type"=>"service","s"=>"алкогол","post_status"=>"publish","numberposts"=>5]);
}
foreach ($q as $p) {
  echo $p->ID." ".$p->post_name." ".get_permalink($p)."\n";
}
$urls = [];
foreach ($q as $p) { $urls[] = get_permalink($p); }
$urls[] = home_url("/uslugi/zavisimosti/lechenie-alkogolizma/");
foreach (array_unique($urls) as $u) {
  $r = wp_remote_get($u, ["timeout"=>20,"sslverify"=>false]);
  if (is_wp_error($r)) { echo "ERR $u\n"; continue; }
  $code = wp_remote_retrieve_response_code($r);
  $b = wp_remote_retrieve_body($r);
  $cards = preg_match_all('/class="specialists__card /', $b);
  $links = preg_match_all('/specialists__card-link/', $b);
  echo "HTTP=$code cards=$cards links=$links $u\n";
}
