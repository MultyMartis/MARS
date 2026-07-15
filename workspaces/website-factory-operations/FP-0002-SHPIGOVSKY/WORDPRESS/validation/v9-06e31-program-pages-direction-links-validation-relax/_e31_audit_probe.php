<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

function row_post($p) {
  return array(
    'ID' => (int)$p->ID,
    'title' => $p->post_title,
    'slug' => $p->post_name,
    'status' => $p->post_status,
    'parent' => (int)$p->post_parent,
    'type' => $p->post_type,
    'url' => get_permalink($p),
    'template' => $p->post_type==='page' ? get_page_template_slug($p->ID) : '',
    'slider' => get_post_meta($p->ID, 'service_show_in_slider', true),
    'text_list' => get_post_meta($p->ID, 'service_show_in_text_list', true),
  );
}

$slugs = array('internet-zavisimost','lechenie-internet-zavisimosti','genotipirovanie','kompyuternaya-zavisimost','lechenie-opiumnoy-zavisimosti');
$services = array();
foreach ($slugs as $slug) {
  $posts = get_posts(array('name'=>$slug,'post_type'=>'service','post_status'=>array('publish','draft','private','trash','pending'),'posts_per_page'=>10,'suppress_filters'=>true));
  $services[$slug] = array_map('row_post', $posts);
}

$prog = get_page_by_path('o-centre/programma-lecheniya');
$children = array();
if ($prog) {
  $kids = get_posts(array('post_type'=>'page','post_parent'=>(int)$prog->ID,'post_status'=>array('publish','draft','private','trash'),'posts_per_page'=>50,'orderby'=>'menu_order','order'=>'ASC'));
  $children = array_map('row_post', $kids);
}

$fields = array();
foreach (array('field_fp02_signs_items_service','field_fp02_programme_items_service','field_fp02_stages_service') as $key) {
  $f = function_exists('acf_get_field') ? acf_get_field($key) : null;
  if (!is_array($f)) { $fields[$key]=null; continue; }
  $fields[$key] = array(
    'label'=>$f['label']??'',
    'name'=>$f['name']??'',
    'required'=>(int)($f['required']??0),
    'min'=>$f['min']??null,
    'max'=>$f['max']??null,
    'instructions'=>$f['instructions']??'',
    'sub_required'=>array_map(function($s){return array('name'=>$s['name']??'','required'=>(int)($s['required']??0));}, $f['sub_fields']??array()),
  );
}

$validation = array();
if (function_exists('acf_validate_value')) {
  foreach (array('field_fp02_signs_items_service','field_fp02_programme_items_service','field_fp02_stages_service') as $key) {
    $f = acf_get_field($key);
    $empty = acf_validate_value(array(), $f, 'acf['.$key.']');
    $validation[$key] = (true===$empty) ? 'PASS_EMPTY' : $empty;
  }
}

echo wp_json_encode(array(
  'program_parent' => $prog ? row_post($prog) : null,
  'program_children' => $children,
  'services' => $services,
  'acf_fields' => $fields,
  'validation_empty' => $validation,
), JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);