<?php
/**
 * FP-0002 V9-06E29B — O-centre admin parity DB seed (page #11 only).
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: baseline | seed | verify | all
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$mode         = isset( $argv[1] ) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29b-ocentre-admin-parity-implementation';
$v9_img       = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/img';
$page_id      = 11;

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E29B_PHASE = 'V9-06E29B';

function fp02e29b_json_write( $path, $data ) {
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
}

/**
 * @return array<int, array<string, mixed>>
 */
function fp02e29b_seed_targets() {
	global $v9_img, $page_id;

	return array(
		array(
			'key'             => 'hero_media',
			'object_id'       => $page_id,
			'acf_field'       => 'hero_media',
			'source_path'     => $v9_img . '/content/o-centre/o-centre-hero.webp',
			'target_filename' => 'o-centre-hero.webp',
			'title'           => 'О центре — hero',
			'alt_text'        => 'Шпиговский дом — реабилитационный центр',
		),
		array(
			'key'             => 'founder_photo',
			'object_id'       => $page_id,
			'acf_field'       => 'about_founder_photo',
			'source_path'     => $v9_img . '/content/founder-sergey-shpigovsky.png',
			'target_filename' => 'founder-sergey-shpigovsky.png',
			'title'           => 'Сергей Юрьевич Шпиговский',
			'alt_text'        => 'Сергей Юрьевич Шпиговский',
		),
		array(
			'key'             => 'clinic_landscape',
			'object_id'       => $page_id,
			'acf_field'       => 'about_clinic_landscape_image',
			'source_path'     => $v9_img . '/content/pre-reviews/shpigovsky-clinic-landscape.webp',
			'target_filename' => 'shpigovsky-clinic-landscape.webp',
			'title'           => 'Территория реабилитационного центра',
			'alt_text'        => 'Здание и территория реабилитационного центра',
		),
	);
}

function fp02e29b_summarize_image_field( $value ) {
	if ( empty( $value ) ) {
		return array( 'empty' => true );
	}
	if ( is_numeric( $value ) ) {
		$id = (int) $value;
		return array(
			'empty'         => false,
			'attachment_id' => $id,
			'url'           => (string) wp_get_attachment_url( $id ),
		);
	}
	if ( is_array( $value ) ) {
		return array(
			'empty'         => false,
			'attachment_id' => isset( $value['ID'] ) ? (int) $value['ID'] : null,
			'url'           => isset( $value['url'] ) ? (string) $value['url'] : '',
		);
	}
	return array( 'empty' => false, 'raw_type' => gettype( $value ) );
}

function fp02e29b_upload_attachment( array $target ) {
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';

	if ( ! is_readable( $target['source_path'] ) ) {
		return array( 'ok' => false, 'error' => 'source_missing', 'path' => $target['source_path'] );
	}

	$upload_dir = wp_upload_dir();
	$dest       = trailingslashit( $upload_dir['path'] ) . $target['target_filename'];

	if ( ! copy( $target['source_path'], $dest ) ) {
		return array( 'ok' => false, 'error' => 'copy_failed' );
	}

	$filetype = wp_check_filetype( basename( $dest ), null );
	$attach   = array(
		'post_mime_type' => $filetype['type'],
		'post_title'     => $target['title'],
		'post_content'   => '',
		'post_status'    => 'inherit',
	);

	$attachment_id = wp_insert_attachment( $attach, $dest, $target['object_id'] );
	if ( is_wp_error( $attachment_id ) || ! $attachment_id ) {
		return array( 'ok' => false, 'error' => 'insert_failed' );
	}

	$metadata = wp_generate_attachment_metadata( $attachment_id, $dest );
	wp_update_attachment_metadata( $attachment_id, $metadata );

	if ( '' !== $target['alt_text'] ) {
		update_post_meta( $attachment_id, '_wp_attachment_image_alt', $target['alt_text'] );
	}

	return array(
		'ok'            => true,
		'attachment_id' => (int) $attachment_id,
		'url'           => (string) wp_get_attachment_url( $attachment_id ),
	);
}

function fp02e29b_get_founder_static_copy() {
	if ( function_exists( 'shpigovsky_get_v9_about_founder_quote_copy' ) ) {
		return shpigovsky_get_v9_about_founder_quote_copy();
	}

	return array(
		'paragraphs' => array(),
		'name'       => '',
		'role'       => '',
		'cta_label'  => '',
	);
}

function fp02e29b_get_clinic_static_copy() {
	if ( function_exists( 'shpigovsky_get_v9_about_clinic_landscape_copy' ) ) {
		return shpigovsky_get_v9_about_clinic_landscape_copy();
	}

	return array( 'alt' => '' );
}

function fp02e29b_seed_text_fields( $page_id ) {
	$founder = fp02e29b_get_founder_static_copy();
	$clinic  = fp02e29b_get_clinic_static_copy();
	$rows    = array();

	$paragraph_rows = array();
	foreach ( $founder['paragraphs'] as $paragraph ) {
		$paragraph_rows[] = array( 'text' => $paragraph );
	}

	$text_updates = array(
		'about_founder_quote_paragraphs' => $paragraph_rows,
		'about_founder_name'             => $founder['name'],
		'about_founder_role'             => $founder['role'],
		'about_founder_cta_label'        => $founder['cta_label'],
		'about_clinic_landscape_alt'     => $clinic['alt'],
	);

	foreach ( $text_updates as $field => $value ) {
		$current = function_exists( 'get_field' ) ? get_field( $field, $page_id ) : null;
		$empty   = empty( $current );

		if ( 'about_founder_quote_paragraphs' === $field && is_array( $current ) && ! empty( $current ) ) {
			$empty = false;
		}

		if ( ! $empty && 'about_clinic_landscape_alt' !== $field ) {
			$rows[] = array(
				'field'  => $field,
				'result' => 'SKIP_ALREADY_SET',
			);
			continue;
		}

		if ( 'about_clinic_landscape_alt' === $field && is_string( $current ) && '' !== trim( $current ) ) {
			$rows[] = array(
				'field'  => $field,
				'result' => 'SKIP_ALREADY_SET',
			);
			continue;
		}

		$updated = function_exists( 'update_field' ) ? update_field( $field, $value, $page_id ) : false;
		$rows[]  = array(
			'field'  => $field,
			'result' => $updated ? 'PASS' : 'ACF_UPDATE_FAIL',
		);
	}

	return $rows;
}

function fp02e29b_seed_images() {
	$results = array();
	foreach ( fp02e29b_seed_targets() as $target ) {
		$current = function_exists( 'get_field' ) ? get_field( $target['acf_field'], $target['object_id'] ) : null;
		if ( ! fp02e29b_summarize_image_field( $current )['empty'] ) {
			$results[] = array(
				'key'    => $target['key'],
				'field'  => $target['acf_field'],
				'result' => 'SKIP_ALREADY_SET',
			);
			continue;
		}

		$upload = fp02e29b_upload_attachment( $target );
		if ( empty( $upload['ok'] ) ) {
			$results[] = array(
				'key'    => $target['key'],
				'field'  => $target['acf_field'],
				'result' => 'UPLOAD_FAIL',
				'error'  => $upload['error'] ?? 'unknown',
			);
			continue;
		}

		$updated = function_exists( 'update_field' )
			? update_field( $target['acf_field'], (int) $upload['attachment_id'], $target['object_id'] )
			: false;

		$results[] = array(
			'key'           => $target['key'],
			'field'         => $target['acf_field'],
			'attachment_id' => $upload['attachment_id'],
			'url'           => $upload['url'],
			'result'        => $updated ? 'PASS' : 'ACF_UPDATE_FAIL',
		);
	}

	return $results;
}

function fp02e29b_baseline( $page_id ) {
	global $wpdb;
	$post = get_post( $page_id );
	$meta = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id = %d ORDER BY meta_key",
			$page_id
		),
		ARRAY_A
	);

	$fields = array(
		'hero_media',
		'about_founder_quote_paragraphs',
		'about_founder_name',
		'about_founder_role',
		'about_founder_photo',
		'about_founder_cta_label',
		'about_clinic_landscape_image',
		'about_clinic_landscape_alt',
		'about_program_lead',
		'about_program_intro',
		'about_program_intro2',
	);

	$acf_state = array();
	foreach ( $fields as $field ) {
		$value = function_exists( 'get_field' ) ? get_field( $field, $page_id ) : null;
		$acf_state[ $field ] = array(
			'empty' => empty( $value ),
			'type'  => gettype( $value ),
		);
		if ( in_array( $field, array( 'hero_media', 'about_founder_photo', 'about_clinic_landscape_image' ), true ) ) {
			$acf_state[ $field ] = fp02e29b_summarize_image_field( $value );
		}
	}

	return array(
		'phase'          => FP02_E29B_PHASE,
		'generated_at'   => gmdate( 'c' ),
		'page_id'        => $page_id,
		'post'           => $post ? array(
			'ID'          => $post->ID,
			'post_title'  => $post->post_title,
			'post_name'   => $post->post_name,
			'post_status' => $post->post_status,
		) : null,
		'postmeta_count' => is_array( $meta ) ? count( $meta ) : 0,
		'acf_state'      => $acf_state,
	);
}

function fp02e29b_verify( $page_id ) {
	$rows = array();
	foreach ( fp02e29b_seed_targets() as $target ) {
		$current = function_exists( 'get_field' ) ? get_field( $target['acf_field'], $target['object_id'] ) : null;
		$summary = fp02e29b_summarize_image_field( $current );
		$rows[]  = array(
			'field'  => $target['acf_field'],
			'seeded' => ! $summary['empty'],
			'url'    => $summary['url'] ?? '',
			'result' => $summary['empty'] ? 'EMPTY' : 'PASS',
		);
	}

	$founder = function_exists( 'get_field' ) ? get_field( 'about_founder_quote_paragraphs', $page_id ) : null;
	$rows[]  = array(
		'field'  => 'about_founder_quote_paragraphs',
		'count'  => is_array( $founder ) ? count( $founder ) : 0,
		'result' => ( is_array( $founder ) && count( $founder ) >= 4 ) ? 'PASS' : 'PARTIAL',
	);

	$fail = array_filter(
		$rows,
		static function ( $row ) {
			return ! in_array( $row['result'], array( 'PASS', 'PARTIAL' ), true );
		}
	);

	return array(
		'phase'        => FP02_E29B_PHASE,
		'generated_at' => gmdate( 'c' ),
		'rows'         => $rows,
		'result'       => empty( $fail ) ? 'PASS' : 'FAIL',
	);
}

$out = array( 'mode' => $mode, 'page_id' => $page_id );

switch ( $mode ) {
	case 'baseline':
		$out['baseline'] = fp02e29b_baseline( $page_id );
		break;
	case 'seed':
		$out['image_seed'] = fp02e29b_seed_images();
		$out['text_seed']  = fp02e29b_seed_text_fields( $page_id );
		break;
	case 'verify':
		$out['verify'] = fp02e29b_verify( $page_id );
		break;
	case 'all':
		$out['baseline']   = fp02e29b_baseline( $page_id );
		$out['image_seed'] = fp02e29b_seed_images();
		$out['text_seed']  = fp02e29b_seed_text_fields( $page_id );
		$out['verify']     = fp02e29b_verify( $page_id );
		break;
	default:
		$out['error'] = 'unknown_mode';
}

fp02e29b_json_write( $evidence_dir . '/_seed-runner-output.json', $out );
echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . PHP_EOL;
