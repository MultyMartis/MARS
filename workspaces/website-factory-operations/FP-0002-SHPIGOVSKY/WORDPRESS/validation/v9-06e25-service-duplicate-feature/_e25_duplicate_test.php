<?php
/**
 * E25 duplicate test probe — loads WordPress and exercises ServiceDuplicate.
 * NOT FOR GIT.
 */
define( 'WP_USE_THEMES', false );
require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

use Shpigovsky\Core\Admin\ServiceDuplicate;
use Shpigovsky\Core\ContentTypes\Service;

$source_slug = $argv[1] ?? 'zavisimosti';
$source      = get_page_by_path( $source_slug, OBJECT, Service::POST_TYPE );

if ( ! $source ) {
	// Try by known ID for zavisimosti subdivision.
	$source = get_post( 73 );
}

if ( ! $source || Service::POST_TYPE !== $source->post_type ) {
	fwrite( STDERR, "Source service not found for slug: {$source_slug}\n" );
	exit( 1 );
}

$source_id = (int) $source->ID;
$before    = array(
	'ID'           => $source_id,
	'post_title'   => $source->post_title,
	'post_status'  => $source->post_status,
	'post_parent'  => (int) $source->post_parent,
	'menu_order'   => (int) $source->menu_order,
	'post_modified'=> $source->post_modified,
	'meta_count'   => count( get_post_meta( $source_id ) ),
);

wp_set_current_user( 1 );

$new_id = ServiceDuplicate::duplicate_service( $source_id, 1 );

if ( is_wp_error( $new_id ) ) {
	echo wp_json_encode(
		array(
			'result' => 'FAIL',
			'error'  => $new_id->get_error_message(),
		),
		JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
	);
	exit( 1 );
}

$new_post = get_post( (int) $new_id );
$source_after = get_post( $source_id );

function fp02_meta_subset( $post_id ) {
	$keys = array(
		'hero_cta_label',
		'hero_media',
		'hero_lead',
		'service_layout_variant',
		'service_short_description',
		'programme_items',
		'intro_text',
		'faq_items',
	);
	$out = array();
	foreach ( $keys as $key ) {
		$out[ $key ] = get_post_meta( $post_id, $key, true );
		$out[ '_' . $key ] = get_post_meta( $post_id, '_' . $key, true );
	}
	$out['_thumbnail_id'] = get_post_meta( $post_id, '_thumbnail_id', true );
	$out['_fp02_duplicated_from'] = get_post_meta( $post_id, '_fp02_duplicated_from', true );
	$out['_fp02_duplicated_at'] = get_post_meta( $post_id, '_fp02_duplicated_at', true );
	$out['_fp02_duplicate_wave'] = get_post_meta( $post_id, '_fp02_duplicate_wave', true );
	return $out;
}

$title_suffix_ok = (bool) preg_match( '/ — копия$/u', $new_post->post_title );

echo wp_json_encode(
	array(
		'result' => 'PASS',
		'source_service_id' => $source_id,
		'duplicate_service_id' => (int) $new_id,
		'source_before' => $before,
		'source_after_unchanged' => array(
			'post_title' => $source_after->post_title === $before['post_title'],
			'post_status' => $source_after->post_status === $before['post_status'],
			'post_parent' => (int) $source_after->post_parent === $before['post_parent'],
			'menu_order' => (int) $source_after->menu_order === $before['menu_order'],
			'post_modified' => $source_after->post_modified === $before['post_modified'],
		),
		'duplicate' => array(
			'post_title' => $new_post->post_title,
			'post_name' => $new_post->post_name,
			'post_status' => $new_post->post_status,
			'post_parent' => (int) $new_post->post_parent,
			'menu_order' => (int) $new_post->menu_order,
			'title_suffix_ok' => $title_suffix_ok,
			'status_draft' => 'draft' === $new_post->post_status,
			'parent_copied' => (int) $new_post->post_parent === $before['post_parent'],
			'menu_order_copied' => (int) $new_post->menu_order === $before['menu_order'],
		),
		'meta_comparison' => array(
			'source' => fp02_meta_subset( $source_id ),
			'duplicate' => fp02_meta_subset( (int) $new_id ),
		),
		'hero_cta_label_copied' => get_post_meta( $source_id, 'hero_cta_label', true ) === get_post_meta( (int) $new_id, 'hero_cta_label', true ),
		'hero_media_id_copied' => get_post_meta( $source_id, 'hero_media', true ) === get_post_meta( (int) $new_id, 'hero_media', true ),
		'programme_items_count_source' => (int) get_post_meta( $source_id, 'programme_items', true ),
		'programme_items_count_duplicate' => (int) get_post_meta( (int) $new_id, 'programme_items', true ),
		'duplicate_markers' => array(
			'_fp02_duplicated_from' => get_post_meta( (int) $new_id, '_fp02_duplicated_from', true ),
			'_fp02_duplicated_at' => get_post_meta( (int) $new_id, '_fp02_duplicated_at', true ),
			'_fp02_duplicate_wave' => get_post_meta( (int) $new_id, '_fp02_duplicate_wave', true ),
		),
		'edit_url' => admin_url( 'post.php?post=' . (int) $new_id . '&action=edit' ),
		'public_url' => get_permalink( (int) $new_id ),
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
