<?php
/**
 * FP-0002 V9-06E15 — Mini-description seed repair runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair';

const FP02_E15_DEMO_LOREM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.';

function fp02e15_json_write( $path, $data ) {
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
}

function fp02e15_set_field( $post_id, $field, $value ) {
	if ( function_exists( 'update_field' ) ) {
		update_field( $field, $value, $post_id );
	} else {
		update_post_meta( $post_id, $field, $value );
		update_post_meta( $post_id, '_' . $field, 'field_fp02_service_short_description' );
	}
}

function fp02e15_get_v9_child_text( $slug ) {
	if ( ! function_exists( 'shpigovsky_get_v9_services_hub_child_copy' ) ) {
		return null;
	}
	$v9 = shpigovsky_get_v9_services_hub_child_copy( $slug );
	return is_array( $v9 ) ? $v9 : null;
}

function fp02e15_classify_seed_source( $text, $slug ) {
	$text = trim( (string) $text );
	if ( '' === $text ) {
		return 'EMPTY_DEFERRED';
	}
	if ( false !== stripos( $text, 'DEMO —' ) || false !== stripos( $text, 'Lorem ipsum' ) ) {
		return 'DEMO';
	}
	return 'EXACT_V9';
}

function fp02e15_all_services() {
	return get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'posts_per_page' => 100,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
		)
	);
}

$results = array(
	'generated_at'   => gmdate( 'c' ),
	'seed_repair'    => array(),
	'db_write_count' => 0,
);

foreach ( fp02e15_all_services() as $service ) {
	if ( ! $service instanceof WP_Post ) {
		continue;
	}

	$before = function_exists( 'shpigovsky_get_service_field' )
		? shpigovsky_get_service_field( $service->ID, 'service_short_description' )
		: get_post_meta( $service->ID, 'service_short_description', true );
	$before = is_string( $before ) ? trim( $before ) : '';

	$status = 'PRESERVED';
	$after  = $before;

	$needs_reseed = ( '' === $before )
		|| ( 0 === strpos( $before, 'E15-ADMIN-MARKER-' ) );

	if ( $needs_reseed ) {
		$v9 = fp02e15_get_v9_child_text( $service->post_name );
		if ( is_array( $v9 ) && '' !== trim( (string) $v9['text'] ) ) {
			$after  = trim( (string) $v9['text'] );
			$status = fp02e15_classify_seed_source( $after, $service->post_name );
		} else {
			$after  = shpigovsky_get_service_demo_mini_description_fallback( $service->post_name );
			$status = 'DEMO';
		}
		fp02e15_set_field( $service->ID, 'service_short_description', $after );
		$results['db_write_count']++;
	} else {
		$status = fp02e15_classify_seed_source( $after, $service->post_name );
	}

	$acf_ref = get_post_meta( $service->ID, '_service_short_description', true );

	$results['seed_repair'][] = array(
		'id'     => (int) $service->ID,
		'title'  => $service->post_title,
		'slug'   => $service->post_name,
		'before' => $before,
		'after'  => $after,
		'source' => $status,
		'acf_reference_meta' => is_string( $acf_ref ) ? $acf_ref : '',
		'result' => '' !== trim( (string) $after ) ? 'PASS' : 'FAIL',
	);
}

fp02e15_json_write( $evidence_dir . '/_e15_repair_runner_output.json', $results );
echo wp_json_encode( $results, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
