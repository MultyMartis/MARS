<?php
define('ABSPATH', 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/' );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
header('Content-Type: text/plain; charset=utf-8');
$out = [];
// Program children of page 13
$prog = get_pages(['parent'=>13,'post_status'=>'publish','sort_column'=>'menu_order']);
foreach ($prog as $p) { $out[] = 'PROG\t'.$p->ID."\t".get_permalink($p)."\t".$p->post_title; }
// Service sections + samples
$services = get_posts(['post_type'=>'service','post_status'=>'publish','numberposts'=>-1,'orderby'=>'menu_order','order'=>'ASC']);
foreach ($services as $s) {
  $role = function_exists('get_field') ? get_field('service_editor_role', $s->ID) : '';
  $out[] = 'SVC\t'.$s->ID."\t".get_permalink($s)."\t".$s->post_title."\t".$role;
}
// Specialists
$specs = get_posts(['post_type'=>'specialist','post_status'=>'publish','numberposts'=>5]);
if (!$specs) {
  // maybe pages under specialists
  $sp = get_page_by_path('specyalisty');
  if ($sp) {
    $kids = get_pages(['parent'=>$sp->ID,'post_status'=>'publish']);
    foreach ($kids as $k) { $out[] = 'SPEC\t'.$k->ID."\t".get_permalink($k)."\t".$k->post_title; }
  }
} else {
  foreach ($specs as $s) { $out[] = 'SPEC\t'.$s->ID."\t".get_permalink($s)."\t".$s->post_title; }
}
// Legal pages
$legals = get_posts(['post_type'=>'page','post_status'=>'publish','numberposts'=>-1,'s'=>'']);
foreach (get_pages(['post_status'=>'publish']) as $p) {
  $tpl = get_page_template_slug($p->ID);
  if (stripos($p->post_name,'polit')!==false || stripos($p->post_title,'политик')!==false || stripos($tpl,'legal')!==false || stripos($p->post_name,'soglash')!==false || stripos($p->post_name,'obrabot')!==false) {
    $out[] = 'LEGAL\t'.$p->ID."\t".get_permalink($p)."\t".$p->post_title."\t".$tpl;
  }
}
// Search pagination test URL
$q = new WP_Query(['s'=>'лечение','post_type'=>['post','page','service'],'posts_per_page'=>12]);
$out[] = 'SEARCH_FOUND\t'.$q->found_posts."\tmax_num_pages=". $q->max_num_pages;
echo implode("\n", $out);
