<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$group = acf_get_field_group('group_fp02_site_options_reviews');
global $wpdb;
$db = $wpdb->get_var("SELECT post_content FROM {$wpdb->prefix}posts WHERE post_name='group_fp02_site_options_reviews' AND post_type='acf-field-group'");
echo json_encode([
  'acf_get_location' => $group['location'] ?? null,
  'db_has_fp02_reviews' => is_string($db) && strpos($db, 'fp02-reviews') !== false,
  'db_has_site_settings' => is_string($db) && strpos($db, 'fp02-site-settings') !== false,
  'acf_get_options_page_reviews' => function_exists('acf_get_options_page') ? acf_get_options_page('fp02-reviews') : null,
], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
