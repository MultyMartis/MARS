<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$n = $wpdb->get_var("SELECT option_value FROM {$wpdb->options} WHERE option_name='fp02-reviews_reviews_items'");
echo "reviews_count=$n\n";
$uids = $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->options} WHERE option_name LIKE 'fp02-reviews_reviews_items_%_review_uid' AND option_value<>''");
echo "review_uid_nonempty=$uids\n";
