<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results("SELECT ID, post_name, post_title, post_status FROM {$wpdb->prefix}posts WHERE post_type='acf-field-group' AND (post_name LIKE '%reviews%' OR post_title LIKE '%Reviews%')", ARRAY_A);
echo json_encode($rows, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
