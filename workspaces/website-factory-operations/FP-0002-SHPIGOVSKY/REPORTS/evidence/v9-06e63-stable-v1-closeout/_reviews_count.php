<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$n = $wpdb->get_var("SELECT option_value FROM {$wpdb->options} WHERE option_name='options_reviews_items'");
echo "acf_repeater_count=$n\n";
$uids = $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->options} WHERE option_name LIKE 'options_reviews_items_%_review_uid'");
echo "uid_meta_rows=$uids\n";
$a = get_field('reviews_items', 'option');
echo 'get_field_count=' . (is_array($a) ? count($a) : 'null') . "\n";
