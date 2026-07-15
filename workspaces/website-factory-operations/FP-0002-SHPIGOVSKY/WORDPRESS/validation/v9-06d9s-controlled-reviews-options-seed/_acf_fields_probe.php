<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$fields = $wpdb->get_results("SELECT p.ID, p.post_name, p.post_title, p.post_excerpt, p.post_content FROM {$wpdb->posts} p WHERE p.post_type='acf-field' AND p.post_excerpt LIKE '%review%' ORDER BY p.ID");
$out = [];
foreach ($fields as $f) {
    $out[] = ['id' => $f->ID, 'name' => $f->post_name, 'label' => $f->post_title, 'parent' => $f->post_excerpt, 'content_preview' => substr($f->post_content, 0, 200)];
}
file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9s-controlled-reviews-options-seed/_acf_fields_probe.json', json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
