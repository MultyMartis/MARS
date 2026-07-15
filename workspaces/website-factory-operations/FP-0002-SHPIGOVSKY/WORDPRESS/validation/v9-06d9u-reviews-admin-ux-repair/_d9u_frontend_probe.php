<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$opt = shpigovsky_get_reviews_option_items();
$items = shpigovsky_get_reviews_items(['limit'=>10]);
$mode = shpigovsky_get_reviews_source_mode();
echo json_encode([
  'option_count'=>count($opt),
  'resolved_count'=>count($items),
  'source_mode'=>$mode,
  'first_author'=>$items[0]['author'] ?? '',
], JSON_UNESCAPED_UNICODE);
