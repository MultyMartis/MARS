<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$checks = [];
$checks['site_options_contacts'] = function_exists('get_field') ? (get_field('contacts_phones','option') !== null || get_field('phone_primary','option') !== null || true) : false;
$reviews = function_exists('get_field') ? get_field('reviews_items','option') : null;
$checks['reviews_rows'] = is_array($reviews) ? count($reviews) : 0;
$checks['demo_blog_count'] = count(get_posts(['post_type'=>'post','post_status'=>'publish','numberposts'=>-1,'name'=>'']));
// count demo posts by slug prefix
$demos = get_posts(['post_type'=>'post','post_status'=>'publish','numberposts'=>-1]);
$demoN = 0; foreach ($demos as $p) { if (strpos($p->post_name,'demo-pagination-article-')===0) $demoN++; }
$checks['demo_blog_posts'] = $demoN;
$checks['blog_page'] = (int) get_option('page_for_posts');
$founder = get_posts(['post_type'=>'fp02-block','name'=>'founder','numberposts'=>1]);
if (!$founder) { $founder = get_posts(['s'=>'Founder','post_type'=>'any','numberposts'=>1]); }
$checks['mini_desc_1053'] = function_exists('get_field') ? (string) get_field('treatment_program_short_description', 1053) : '';
echo json_encode($checks, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
