<?php
/**
 * V9-06E47 — seed service_general parity fields + admin/frontend probes.
 *
 * Usage (from site root with MLI PHP):
 *   php validation/_e47_seed_and_probe.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	$wp_load = getenv( 'E47_WP_LOAD' );
	if ( ! is_string( $wp_load ) || '' === $wp_load ) {
		$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
	}
	require_once $wp_load;
}

if ( ! function_exists( 'update_field' ) ) {
	fwrite( STDERR, "ACF update_field missing\n" );
	exit( 1 );
}

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
if ( ! is_dir( $evidence_dir ) ) {
	wp_mkdir_p( $evidence_dir );
}

$seed_log = array();
$db_writes = 0;

/**
 * Seed scalar/image only when empty (do not overwrite meaningful values).
 *
 * @param int    $post_id Post ID.
 * @param string $field Field name.
 * @param mixed  $value Value.
 * @param string $note Note.
 * @return void
 */
function e47_seed_if_empty( $post_id, $field, $value, $note = '' ) {
	global $seed_log, $db_writes;

	$existing = get_field( $field, $post_id );
	$empty    = ( null === $existing || false === $existing || '' === $existing || array() === $existing );

	if ( is_numeric( $existing ) && (int) $existing === 0 ) {
		$empty = true;
	}

	if ( ! $empty ) {
		$seed_log[] = array(
			'post_id'  => $post_id,
			'field'    => $field,
			'action'   => 'preserved',
			'note'     => $note,
			'preview'  => is_scalar( $existing ) ? substr( (string) $existing, 0, 80 ) : 'non-scalar',
		);
		return;
	}

	$ok = update_field( $field, $value, $post_id );
	++$db_writes;
	$seed_log[] = array(
		'post_id'  => $post_id,
		'field'    => $field,
		'action'   => $ok ? 'seeded' : 'seed_failed',
		'note'     => $note,
		'preview'  => is_scalar( $value ) ? substr( (string) $value, 0, 80 ) : ( is_array( $value ) ? 'array:' . count( $value ) : gettype( $value ) ),
	);
}

$base_id = 74;
$rep_ids = array( 314, 78 );

// Confirm base page.
$base = get_post( $base_id );
if ( ! $base || 'service' !== $base->post_type ) {
	fwrite( STDERR, "Base post #74 missing or wrong type\n" );
	exit( 2 );
}

$intro     = shpigovsky_get_v9_alcohol_leaf_intro_copy();
$bordered  = shpigovsky_get_v9_alcohol_bordered_info_subsections();
$signs     = shpigovsky_get_v9_alcohol_signs_copy();
$approach  = shpigovsky_get_v9_alcohol_leaf_approach_copy();
$program   = shpigovsky_get_v9_alcohol_leaf_program_demo_copy();
$stages    = shpigovsky_get_v9_alcohol_leaf_stages_copy();
$faq_items = shpigovsky_get_v9_alcohol_leaf_faq_items();

$bordered_rows = array();
foreach ( $bordered as $row ) {
	$bordered_rows[] = array(
		'heading' => $row['heading'],
		'text'    => $row['text'],
	);
}

$signs_rows = array();
foreach ( $signs['items'] as $text ) {
	$signs_rows[] = array( 'text' => $text );
}

$approach_cards = array();
foreach ( $approach['cards'] as $card ) {
	$approach_cards[] = array(
		'title' => $card['title'],
		'text'  => $card['text'],
	);
}

$program_intros = array(
	array( 'text' => $program['intro'] ),
	array( 'text' => $program['intro2'] ),
);

$stages_rows = array();
foreach ( $stages['steps'] as $step ) {
	$stages_rows[] = array(
		'title'   => $step['title'],
		'text'    => $step['text'],
		'enabled' => 1,
	);
}

$support_rows = array();
foreach ( $stages['support_items'] as $text ) {
	$support_rows[] = array( 'text' => $text );
}

$faq_rows = array();
foreach ( $faq_items as $item ) {
	$faq_rows[] = array(
		'question' => $item['question'],
		'answer'   => implode( "\n\n", $item['answers'] ),
	);
}

// Image IDs (existing ML attachments from E46).
$team_image_id      = 1238;
$landscape_image_id = 1239;
$corridor_image_id  = 1709;

// --- Seed #74 full demo/current FE content ---
e47_seed_if_empty( $base_id, 'service_general_intro_heading', $intro['heading'], 'alcohol intro' );
e47_seed_if_empty( $base_id, 'service_general_intro_highlight', $intro['highlight'], 'alcohol intro' );
e47_seed_if_empty( $base_id, 'service_general_bordered_info_items', $bordered_rows, 'alcohol bordered' );
e47_seed_if_empty( $base_id, 'service_general_signs_heading', $signs['heading'], 'alcohol signs' );
e47_seed_if_empty( $base_id, 'service_general_signs_intro', $signs['intro'], 'alcohol signs' );
e47_seed_if_empty( $base_id, 'service_general_signs_items', $signs_rows, 'alcohol signs' );
e47_seed_if_empty( $base_id, 'service_general_signs_editorial', $signs['editorial'], 'alcohol signs' );
e47_seed_if_empty( $base_id, 'service_general_approach_heading', $approach['heading'], 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_approach_highlight', $approach['highlight'], 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_approach_intro', $approach['intro'], 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_approach_more_label', 'подробнее', 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_approach_more_url', home_url( '/o-centre/programma-lecheniya/' ), 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_approach_cards', $approach_cards, 'alcohol approach' );
e47_seed_if_empty( $base_id, 'service_general_team_image', $team_image_id, 'team image #1238' );
e47_seed_if_empty( $base_id, 'service_general_clinic_landscape_image', $landscape_image_id, 'landscape #1239' );
e47_seed_if_empty( $base_id, 'service_general_corridor_image', $corridor_image_id, 'corridor #1709' );
e47_seed_if_empty( $base_id, 'service_general_program_heading', 'Наша программа включает 4 направления', 'alcohol program' );
e47_seed_if_empty( $base_id, 'service_general_program_more_label', 'подробнее', 'alcohol program' );
e47_seed_if_empty( $base_id, 'service_general_program_lead', $program['lead'], 'alcohol program' );
e47_seed_if_empty( $base_id, 'service_general_program_intro_items', $program_intros, 'alcohol program' );
e47_seed_if_empty( $base_id, 'service_general_stages_heading', $stages['heading'], 'alcohol stages' );
e47_seed_if_empty( $base_id, 'service_general_stages_lead', $stages['lead'], 'alcohol stages' );
e47_seed_if_empty( $base_id, 'service_general_stages_items', $stages_rows, 'alcohol stages' );
e47_seed_if_empty( $base_id, 'service_general_stages_support_heading', $stages['support_heading'], 'alcohol stages' );
e47_seed_if_empty( $base_id, 'service_general_stages_support_items', $support_rows, 'alcohol stages' );
e47_seed_if_empty( $base_id, 'service_general_faq_heading', 'Нас часто спрашивают', 'alcohol faq' );
e47_seed_if_empty( $base_id, 'service_general_faq_items', $faq_rows, 'alcohol faq' );

// Explicit toggles ON for alcohol specialists (historic visibility).
e47_seed_if_empty( $base_id, 'service_general_specialists_visible', 1, 'alcohol specialists toggle' );

// Representative pages: seed shared images only + specialists OFF to preserve layout; do not copy alcohol copy.
foreach ( $rep_ids as $rid ) {
	e47_seed_if_empty( $rid, 'service_general_clinic_landscape_image', $landscape_image_id, 'rep landscape shared demo asset' );
	e47_seed_if_empty( $rid, 'service_general_corridor_image', $corridor_image_id, 'rep corridor shared demo asset' );
	// Preserve no-specialists historic leaf for non-alcohol unless already set.
	if ( ! metadata_exists( 'post', $rid, 'service_general_specialists_visible' ) ) {
		update_field( 'service_general_specialists_visible', 0, $rid );
		++$db_writes;
		$seed_log[] = array(
			'post_id' => $rid,
			'field'   => 'service_general_specialists_visible',
			'action'  => 'seeded',
			'note'    => 'preserve no-specialists layout',
			'preview' => '0',
		);
	}
}

// Export seeded CSV.
$csv_path = $evidence_dir . '/v9-06e47-service-general-seeded-fields.csv';
$fp       = fopen( $csv_path, 'wb' );
fputcsv( $fp, array( 'post_id', 'field', 'action', 'note', 'preview' ) );
foreach ( $seed_log as $row ) {
	fputcsv( $fp, array( $row['post_id'], $row['field'], $row['action'], $row['note'], $row['preview'] ) );
}
fclose( $fp );

// Admin probe for #74.
$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $base_id ) ) : array();
$group_titles = array();
foreach ( $groups as $g ) {
	$group_titles[] = isset( $g['title'] ) ? $g['title'] : ( $g['key'] ?? '' );
}

$admin = array(
	'post_id'            => $base_id,
	'title'              => $base->post_title,
	'editor_role'        => get_field( 'service_editor_role', $base_id ),
	'layout_variant'     => get_field( 'service_layout_variant', $base_id ),
	'acf_group_titles'   => $group_titles,
	'has_general_group'  => in_array( 'Услуга — блоки страницы', $group_titles, true ),
	'has_section_group'  => false,
	'classic_editor'     => post_type_supports( 'service', 'editor' ),
	'sample_fields'      => array(
		'intro_heading'   => (string) get_field( 'service_general_intro_heading', $base_id ),
		'team_image'      => get_field( 'service_general_team_image', $base_id ),
		'landscape_image' => get_field( 'service_general_clinic_landscape_image', $base_id ),
		'corridor_image'  => get_field( 'service_general_corridor_image', $base_id ),
		'signs_count'     => is_array( get_field( 'service_general_signs_items', $base_id ) ) ? count( get_field( 'service_general_signs_items', $base_id ) ) : 0,
		'faq_count'       => is_array( get_field( 'service_general_faq_items', $base_id ) ) ? count( get_field( 'service_general_faq_items', $base_id ) ) : 0,
		'stages_count'    => is_array( get_field( 'service_general_stages_items', $base_id ) ) ? count( get_field( 'service_general_stages_items', $base_id ) ) : 0,
	),
);

foreach ( $group_titles as $t ) {
	if ( false !== stripos( $t, 'Раздел' ) ) {
		$admin['has_section_group'] = true;
	}
}

file_put_contents( $evidence_dir . '/v9-06e47-admin-probe-74.json', wp_json_encode( $admin, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Resolve sources for images on #74.
$resolve = array(
	'team'      => shpigovsky_general_image_or_asset( $base_id, 'service_general_team_image', 'img/content/pre-reviews/shpigovsky-staff-group.webp', 'team', 1139, 443 ),
	'landscape' => shpigovsky_general_image_or_asset( $base_id, 'service_general_clinic_landscape_image', 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', 'landscape', 1139, 584 ),
	'corridor'  => shpigovsky_general_image_or_asset( $base_id, 'service_general_corridor_image', 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp', 'corridor', 2187, 1231 ),
	'intro'     => shpigovsky_get_general_intro_copy( $base_id ),
);
file_put_contents( $evidence_dir . '/v9-06e47-resolve-74.json', wp_json_encode( $resolve, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

echo wp_json_encode(
	array(
		'ok'         => true,
		'db_writes'  => $db_writes,
		'seed_rows'  => count( $seed_log ),
		'admin'      => $admin,
		'resolve'    => array(
			'team_source'      => $resolve['team']['source'],
			'landscape_source' => $resolve['landscape']['source'],
			'corridor_source'  => $resolve['corridor']['source'],
		),
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
) . PHP_EOL;
