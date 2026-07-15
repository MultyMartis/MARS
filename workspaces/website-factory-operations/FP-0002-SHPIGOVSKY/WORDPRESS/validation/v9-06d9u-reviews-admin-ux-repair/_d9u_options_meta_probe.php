<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results(
    "SELECT option_name, LENGTH(option_value) len FROM {$wpdb->prefix}options WHERE option_name LIKE '%review%' ORDER BY option_name",
    ARRAY_A
);
echo json_encode($rows, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
