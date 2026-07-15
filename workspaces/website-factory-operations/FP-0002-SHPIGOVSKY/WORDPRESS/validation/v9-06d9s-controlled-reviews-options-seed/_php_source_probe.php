<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$opt = shpigovsky_get_reviews_option_items();
$items = shpigovsky_get_reviews_items(['limit'=>10,'featured_only'=>true]);
$first = $items[0] ?? [];
$mode = empty($opt) ? 'FALLBACK' : ((!empty($first['is_demo'])) ? 'FALLBACK' : 'OPTIONS');
echo json_encode([
  'option_count'=>count($opt),
  'resolved_count'=>count($items),
  'source_mode'=>$mode,
  'first_author'=>$first['author'] ?? '',
  'is_demo'=>!empty($first['is_demo']),
], JSON_UNESCAPED_UNICODE);
