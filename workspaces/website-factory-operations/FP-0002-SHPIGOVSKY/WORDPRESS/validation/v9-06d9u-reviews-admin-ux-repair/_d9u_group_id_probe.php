<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$group = acf_get_field_group('group_fp02_site_options_reviews');
global $wpdb;
$all = $wpdb->get_results("SELECT ID, post_name, post_modified FROM {$wpdb->prefix}posts WHERE post_type='acf-field-group' AND post_name='group_fp02_site_options_reviews' ORDER BY ID", ARRAY_A);
echo json_encode(['active_id'=>$group['ID']??null,'active_location'=>$group['location']??null,'all_posts'=>$all], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
