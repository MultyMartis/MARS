<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$test_id = 77;

// Wipe all program intro repeater metas for #77 (were absent before FIX03 except maybe none)
$deleted = $wpdb->query( $wpdb->prepare(
  "DELETE FROM {$wpdb->postmeta} WHERE post_id=%d AND (meta_key LIKE %s OR meta_key LIKE %s OR meta_key IN ('section_program_footer_label','_section_program_footer_label'))",
  $test_id,
  $wpdb->esc_like('section_program_intro_items') . '%',
  $wpdb->esc_like('_section_program_intro_items') . '%'
) );
echo "DELETED_ROWS=$deleted\n";

// Also ensure no USER_ leftovers
$rows = $wpdb->get_results( $wpdb->prepare(
  "SELECT meta_key, LEFT(meta_value,80) v FROM {$wpdb->postmeta} WHERE post_id=%d AND (meta_key LIKE %s OR meta_value LIKE %s)",
  $test_id, '%program_intro%', '%USER_%'
), ARRAY_A );
echo "LEFT=".wp_json_encode($rows, JSON_UNESCAPED_UNICODE)."\n";

// Confirm helper still returns demo for empty #77
$intros = shpigovsky_get_section_program_intro_items(77);
$footer = shpigovsky_section_text(77, 'section_program_footer_label', 'подробнее о программе');
echo "77_intros_count=".count($intros)." intro0=".substr($intros[0]??'',0,40)."\n";
echo "77_footer=$footer\n";

// Confirm #73 still good
$i73 = shpigovsky_get_section_program_intro_items(73);
echo "73_intros=".count($i73)." meta=".get_post_meta(73,'section_program_intro_items',true)."\n";
$meta73 = $wpdb->get_results("SELECT meta_key, LEFT(meta_value,40) v FROM {$wpdb->postmeta} WHERE post_id=73 AND meta_key LIKE 'section_program_intro_items%' ORDER BY meta_key", ARRAY_A);
echo "73_meta=".wp_json_encode($meta73, JSON_UNESCAPED_UNICODE)."\n";