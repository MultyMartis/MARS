<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results("SELECT option_name, LENGTH(option_value) len FROM {$wpdb->options} WHERE option_name LIKE '%review%' ORDER BY option_name LIMIT 80");
foreach ($rows as $r) echo $r->option_name . "\t" . $r->len . "\n";
echo "----\n";
// try fp02-reviews
foreach (['option','fp02-reviews','fp02_reviews','reviews'] as $id) {
  $a = get_field('reviews_items', $id);
  echo "get_field($id)=" . (is_array($a)?count($a):var_export($a,true)) . "\n";
}
