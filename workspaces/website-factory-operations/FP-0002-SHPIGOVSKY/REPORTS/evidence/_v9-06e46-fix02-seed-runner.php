<?php
/**
 * V9-06E46-FIX02 — export ACF JSON + seed section repeaters for #73.
 * One-shot local runner. Do not leave enabled in production hooks.
 */

declare(strict_types=1);

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

if ( ! function_exists( 'get_field' ) || ! class_exists( '\\Shpigovsky\\Core\\Fields\\ServiceSectionParity' ) ) {
	fwrite( STDERR, "ACF or ServiceSectionParity missing\n" );
	exit( 1 );
}

$group = \Shpigovsky\Core\Fields\ServiceSectionParity::group();
$json_path_src = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_service_section_parity.json';
$json_path_rt  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_service_section_parity.json';

$export = $group;
// ACF JSON uses modified as int timestamp; ensure fields array is JSON-serializable.
$json = wp_json_encode( $export, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
if ( ! is_string( $json ) ) {
	fwrite( STDERR, "JSON encode failed\n" );
	exit( 1 );
}
$json .= "\n";
file_put_contents( $json_path_src, $json );
file_put_contents( $json_path_rt, $json );
echo "ACF_JSON_WRITTEN\n";

/**
 * Read legacy scalar meta.
 */
function fp02_fix02_meta( int $post_id, string $key ): string {
	$v = get_post_meta( $post_id, $key, true );
	return is_string( $v ) ? trim( $v ) : '';
}

$post_id = 73;
$writes  = 0;

// Nature text blocks from legacy / fallbacks.
$existing_blocks = get_field( 'section_nature_text_blocks', $post_id );
if ( empty( $existing_blocks ) ) {
	$neuro_h = fp02_fix02_meta( $post_id, 'section_nature_neurobiology_heading' ) ?: 'Нейробиология';
	$neuro_t = fp02_fix02_meta( $post_id, 'section_nature_neurobiology_text' );
	$geno_h  = fp02_fix02_meta( $post_id, 'section_nature_genotyping_heading' ) ?: 'Генотипирование';
	$geno_t  = fp02_fix02_meta( $post_id, 'section_nature_genotyping_text' );
	$geno_l  = fp02_fix02_meta( $post_id, 'section_nature_genotyping_link_label' ) ?: 'Подробнее о генотипировании';
	$geno_u  = fp02_fix02_meta( $post_id, 'section_nature_genotyping_link_url' ) ?: home_url( '/uslugi/zavisimosti/profilakticheskiy-analiz/' );
	$geno_a  = fp02_fix02_meta( $post_id, 'section_nature_genotyping_after_text' );

	$blocks = array(
		array(
			'heading'    => $neuro_h,
			'text'       => $neuro_t,
			'link_label' => '',
			'link_url'   => '',
			'after_text' => '',
		),
		array(
			'heading'    => $geno_h,
			'text'       => $geno_t,
			'link_label' => $geno_l,
			'link_url'   => $geno_u,
			'after_text' => $geno_a,
		),
	);
	update_field( 'section_nature_text_blocks', $blocks, $post_id );
	$writes++;
	echo "SEEDED section_nature_text_blocks\n";
} else {
	echo "SKIP section_nature_text_blocks already set\n";
}

// Program intros.
$existing_intros = get_field( 'section_program_intro_items', $post_id );
if ( empty( $existing_intros ) ) {
	$i1 = fp02_fix02_meta( $post_id, 'section_program_intro' );
	$i2 = fp02_fix02_meta( $post_id, 'section_program_intro2' );
	$intros = array();
	if ( '' !== $i1 ) {
		$intros[] = array( 'text' => $i1 );
	}
	if ( '' !== $i2 ) {
		$intros[] = array( 'text' => $i2 );
	}
	if ( empty( $intros ) ) {
		$intros = array(
			array( 'text' => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' ),
			array( 'text' => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' ),
		);
	}
	update_field( 'section_program_intro_items', $intros, $post_id );
	$writes++;
	echo "SEEDED section_program_intro_items count=" . count( $intros ) . "\n";
} else {
	echo "SKIP section_program_intro_items already set\n";
}

// Stages items from Structured Sections stages or fallback.
$existing_stages = get_field( 'section_stages_items', $post_id );
if ( empty( $existing_stages ) ) {
	$stages = get_field( 'stages', $post_id );
	$rows   = array();
	if ( is_array( $stages ) ) {
		foreach ( $stages as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
			$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $title && '' === $text ) {
				continue;
			}
			$rows[] = array(
				'title'   => $title,
				'text'    => $text,
				'enabled' => 1,
			);
		}
	}
	if ( empty( $rows ) && function_exists( 'shpigovsky_get_section_stages_items_fallback' ) ) {
		foreach ( shpigovsky_get_section_stages_items_fallback() as $row ) {
			$rows[] = array(
				'title'   => $row['title'],
				'text'    => $row['text'],
				'enabled' => 1,
			);
		}
	}
	update_field( 'section_stages_items', $rows, $post_id );
	$writes++;
	echo "SEEDED section_stages_items count=" . count( $rows ) . "\n";
} else {
	echo "SKIP section_stages_items already set\n";
}

// Ensure #77/#84 have toggles ON but do not overwrite content with #73.
foreach ( array( 77, 84 ) as $sid ) {
	$role = get_field( 'service_editor_role', $sid );
	echo "SECTION_$sid role=" . ( is_string( $role ) ? $role : 'n/a' ) . "\n";
	// Do not seed #73 content into other sections.
}

echo "DB_WRITES_FIELD_UPDATES=$writes\n";

// Admin label smoke via group definition.
$labels = array();
foreach ( $group['fields'] as $f ) {
	if ( isset( $f['name'] ) && in_array( $f['name'], array( 'section_dependencies_notice', 'section_mid_cta_notice', 'section_nature_text_blocks', 'section_program_intro_items', 'section_stages_items' ), true ) ) {
		$labels[ $f['name'] ] = $f['label'];
	}
}
echo "LABELS " . wp_json_encode( $labels, JSON_UNESCAPED_UNICODE ) . "\n";

// Quick frontend-facing helpers.
$text_blocks = shpigovsky_get_section_nature_text_blocks( $post_id );
$intros_h    = shpigovsky_get_section_program_intro_items( $post_id );
$stages_h    = shpigovsky_get_section_stages_items( $post_id );
echo 'NATURE_BLOCKS=' . count( $text_blocks ) . " INTROS=" . count( $intros_h ) . ' STAGES=' . count( $stages_h ) . "\n";

exit( 0 );
