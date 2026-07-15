<?php
/**
 * FP-0002 V9-06E15 baseline probe — TEMPORARY HELPER, NOT FOR GIT.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out = array(
	'generated_at' => gmdate( 'c' ),
	'services'     => array(),
);

$services = get_posts(
	array(
		'post_type'      => 'service',
		'post_status'    => 'publish',
		'posts_per_page' => 50,
		'orderby'        => 'menu_order',
		'order'          => 'ASC',
	)
);

foreach ( $services as $s ) {
	$acf      = function_exists( 'get_field' ) ? get_field( 'service_short_description', $s->ID ) : '';
	$meta     = get_post_meta( $s->ID, 'service_short_description', true );
	$ref      = get_post_meta( $s->ID, '_service_short_description', true );
	$resolved = function_exists( 'shpigovsky_get_service_mini_description' ) ? shpigovsky_get_service_mini_description( $s->ID ) : '';
	$v9       = function_exists( 'shpigovsky_get_v9_services_hub_child_copy' ) ? shpigovsky_get_v9_services_hub_child_copy( $s->post_name ) : null;
	$v9text   = is_array( $v9 ) ? trim( (string) $v9['text'] ) : '';

	$source = 'UNKNOWN';
	if ( '' !== trim( (string) $acf ) ) {
		$source = 'ACF_FIELD';
	} elseif ( '' !== trim( (string) $meta ) ) {
		$source = 'RAW_META_ONLY';
	} elseif ( '' !== $v9text ) {
		$source = 'V9_FALLBACK';
	} else {
		$source = 'DEMO_FALLBACK';
	}

	$rendered_matches_acf = ( '' !== trim( (string) $acf ) && trim( (string) $acf ) === trim( (string) $resolved ) );
	$rendered_matches_v9  = ( '' !== $v9text && $v9text === trim( (string) $resolved ) && '' === trim( (string) $acf ) );

	$out['services'][] = array(
		'id'                   => $s->ID,
		'title'                => $s->post_title,
		'slug'                 => $s->post_name,
		'parent'               => (int) $s->post_parent,
		'acf_value'            => $acf,
		'meta_value'           => $meta,
		'acf_ref'              => $ref,
		'resolved'             => $resolved,
		'v9_text'              => $v9text,
		'source_attribution'   => $source,
		'rendered_matches_acf' => $rendered_matches_acf,
		'rendered_matches_v9'  => $rendered_matches_v9,
	);
}

$hub_mode = function_exists( 'shpigovsky_get_services_hub_field' ) ? shpigovsky_get_services_hub_field( 'services_hub_query_mode' ) : '';
if ( '' === $hub_mode ) {
	$hub_mode = 'grouped_by_parent';
}
$out['services_hub_query_mode'] = $hub_mode;

echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
