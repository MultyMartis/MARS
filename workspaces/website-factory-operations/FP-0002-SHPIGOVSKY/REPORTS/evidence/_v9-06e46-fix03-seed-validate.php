<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$db_writes = 0;
$log = array();

function fp02_fix03_log( &$log, $msg ) {
	$log[] = $msg;
	echo $msg . PHP_EOL;
}

// --- Seed #73 intro repeater from legacy if not meaningful ---
$post_id = 73;
$existing = get_field( 'section_program_intro_items', $post_id );
$has_meaningful = function_exists( 'shpigovsky_has_meaningful_repeater_rows' )
	? shpigovsky_has_meaningful_repeater_rows( $existing, array( 'text' ) )
	: false;

if ( ! $has_meaningful ) {
	$i1 = trim( (string) get_post_meta( $post_id, 'section_program_intro', true ) );
	$i2 = trim( (string) get_post_meta( $post_id, 'section_program_intro2', true ) );
	$rows = array();
	if ( '' !== $i1 ) {
		$rows[] = array( 'text' => $i1 );
	}
	if ( '' !== $i2 ) {
		$rows[] = array( 'text' => $i2 );
	}
	if ( ! empty( $rows ) ) {
		$ok = update_field( 'section_program_intro_items', $rows, $post_id );
		$db_writes++;
		fp02_fix03_log( $log, 'SEEDED_INTRO_ITEMS count=' . count( $rows ) . ' ok=' . ( $ok ? '1' : '0' ) );
	} else {
		fp02_fix03_log( $log, 'SKIP_SEED no legacy intros' );
	}
} else {
	fp02_fix03_log( $log, 'SKIP_SEED already meaningful rows=' . count( (array) $existing ) );
}

// Verify storage
$verify_rows = get_field( 'section_program_intro_items', $post_id );
$meta_count  = get_post_meta( $post_id, 'section_program_intro_items', true );
fp02_fix03_log( $log, 'VERIFY get_field_type=' . gettype( $verify_rows ) . ' count=' . ( is_array( $verify_rows ) ? count( $verify_rows ) : 0 ) . ' meta_count=' . var_export( $meta_count, true ) );

// --- Admin inventory after ---
$fields = acf_get_fields( 'group_fp02_service_section_parity' );
$names  = array();
$cta_left = array();
foreach ( (array) $fields as $f ) {
	$names[] = array(
		'name'  => $f['name'] ?? '',
		'label' => $f['label'] ?? '',
		'type'  => $f['type'] ?? '',
	);
	$label = (string) ( $f['label'] ?? '' );
	$name  = (string) ( $f['name'] ?? '' );
	if ( false !== strpos( $label, 'CTA «Раздел' ) || false !== strpos( $name, 'mid_cta' ) ) {
		$cta_left[] = $label . '/' . $name;
	}
}
file_put_contents( $evidence . '/v9-06e46-fix03-admin-73-after.json', wp_json_encode( array(
	'field_count' => count( $names ),
	'cta_left'    => $cta_left,
	'fields'      => $names,
), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
fp02_fix03_log( $log, 'ADMIN_FIELDS=' . count( $names ) . ' CTA_LEFT=' . count( $cta_left ) );

// --- Fallback behavior tests (temp post meta on #77, restore after) ---
$test_id = 77;
$backup_keys = array(
	'section_program_intro_items',
	'_section_program_intro_items',
	'section_program_footer_label',
	'_section_program_footer_label',
	'section_program_intro',
	'section_program_intro2',
);
$backup = array();
foreach ( $backup_keys as $k ) {
	$backup[ $k ] = array(
		'exists' => metadata_exists( 'post', $test_id, $k ),
		'value'  => get_post_meta( $test_id, $k, true ),
	);
}

$results = array();

// A) Empty: delete footer + intros, expect demo footer via section_text + demo intros
delete_post_meta( $test_id, 'section_program_footer_label' );
delete_post_meta( $test_id, '_section_program_footer_label' );
delete_post_meta( $test_id, 'section_program_intro_items' );
delete_post_meta( $test_id, '_section_program_intro_items' );
// clear any row metas
global $wpdb;
$wpdb->query( $wpdb->prepare( "DELETE FROM {$wpdb->postmeta} WHERE post_id=%d AND meta_key LIKE %s", $test_id, $wpdb->esc_like( 'section_program_intro_items_' ) . '%' ) );
delete_post_meta( $test_id, 'section_program_intro' );
delete_post_meta( $test_id, 'section_program_intro2' );
$db_writes += 2; // deletes counted loosely

$footer_empty = shpigovsky_section_text( $test_id, 'section_program_footer_label', 'подробнее о программе' );
$intros_empty = shpigovsky_get_section_program_intro_items( $test_id );
$results['empty'] = array(
	'footer' => $footer_empty,
	'footer_is_fallback' => ( 'подробнее о программе' === $footer_empty ),
	'intros_count' => count( $intros_empty ),
	'intro0_lorem' => ( 0 === strpos( (string) ( $intros_empty[0] ?? '' ), 'Lorem' ) ),
);

// B) Partial: one intro row filled, one empty; footer custom
update_field( 'section_program_intro_items', array(
	array( 'text' => 'USER_PARTIAL_INTRO_ONLY' ),
	array( 'text' => '' ),
), $test_id );
update_field( 'section_program_footer_label', 'USER_FOOTER_PARTIAL', $test_id );
$db_writes += 2;

$footer_partial = shpigovsky_section_text( $test_id, 'section_program_footer_label', 'подробнее о программе' );
$intros_partial = shpigovsky_get_section_program_intro_items( $test_id );
$joined = implode( '||', $intros_partial );
$results['partial'] = array(
	'footer' => $footer_partial,
	'footer_user_wins' => ( 'USER_FOOTER_PARTIAL' === $footer_partial ),
	'intros' => $intros_partial,
	'only_user_row' => ( array( 'USER_PARTIAL_INTRO_ONLY' ) === $intros_partial ),
	'no_lorem_mixed' => ( false === strpos( $joined, 'Lorem' ) ),
);

// C) Filled: two intros + footer
update_field( 'section_program_intro_items', array(
	array( 'text' => 'USER_INTRO_A' ),
	array( 'text' => 'USER_INTRO_B' ),
), $test_id );
update_field( 'section_program_footer_label', 'USER_FOOTER_FULL', $test_id );
$db_writes += 2;

$footer_full = shpigovsky_section_text( $test_id, 'section_program_footer_label', 'подробнее о программе' );
$intros_full = shpigovsky_get_section_program_intro_items( $test_id );
$results['filled'] = array(
	'footer' => $footer_full,
	'footer_user_wins' => ( 'USER_FOOTER_FULL' === $footer_full ),
	'intros' => $intros_full,
	'user_only' => ( array( 'USER_INTRO_A', 'USER_INTRO_B' ) === $intros_full ),
);

// Restore #77
foreach ( $backup as $k => $info ) {
	if ( $info['exists'] ) {
		update_post_meta( $test_id, $k, $info['value'] );
	} else {
		delete_post_meta( $test_id, $k );
	}
}
$wpdb->query( $wpdb->prepare( "DELETE FROM {$wpdb->postmeta} WHERE post_id=%d AND meta_key LIKE %s", $test_id, $wpdb->esc_like( 'section_program_intro_items_' ) . '%' ) );
// re-clear leftover from tests if backup had no rows
if ( ! $backup['section_program_intro_items']['exists'] ) {
	delete_post_meta( $test_id, 'section_program_intro_items' );
	delete_post_meta( $test_id, '_section_program_intro_items' );
}
$db_writes += 1;
fp02_fix03_log( $log, 'RESTORED_77' );

// Confirm #77 not contaminated with USER_
$check77 = get_post_meta( $test_id, 'section_program_footer_label', true );
$check77i = get_field( 'section_program_intro_items', $test_id );
fp02_fix03_log( $log, '77_footer=' . var_export( $check77, true ) . ' intros=' . var_export( $check77i, true ) );

// #73 FE helpers
$h73 = array(
	'footer' => shpigovsky_section_text( 73, 'section_program_footer_label', 'подробнее о программе' ),
	'intros' => shpigovsky_get_section_program_intro_items( 73 ),
	'mid_cta_enabled' => shpigovsky_section_block_enabled( 73, 'section_mid_cta_visible' ),
);

file_put_contents( $evidence . '/v9-06e46-fix03-fallback-helper-tests.json', wp_json_encode( array(
	'results' => $results,
	'h73'     => $h73,
	'db_writes_approx' => $db_writes,
	'log'     => $log,
), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

echo 'EMPTY_OK=' . ( ! empty( $results['empty']['footer_is_fallback'] ) && ! empty( $results['empty']['intro0_lorem'] ) ? '1' : '0' ) . PHP_EOL;
echo 'PARTIAL_OK=' . ( ! empty( $results['partial']['footer_user_wins'] ) && ! empty( $results['partial']['only_user_row'] ) && ! empty( $results['partial']['no_lorem_mixed'] ) ? '1' : '0' ) . PHP_EOL;
echo 'FILLED_OK=' . ( ! empty( $results['filled']['footer_user_wins'] ) && ! empty( $results['filled']['user_only'] ) ? '1' : '0' ) . PHP_EOL;
echo '73_FOOTER=' . $h73['footer'] . PHP_EOL;
echo '73_INTROS=' . count( $h73['intros'] ) . PHP_EOL;
echo '73_CTA_ON=' . ( $h73['mid_cta_enabled'] ? '1' : '0' ) . PHP_EOL;
echo 'DB_WRITES_APPROX=' . $db_writes . PHP_EOL;