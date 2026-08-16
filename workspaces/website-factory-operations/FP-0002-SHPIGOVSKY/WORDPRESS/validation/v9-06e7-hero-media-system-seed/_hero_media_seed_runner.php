<?php
/**
 * FP-0002 V9-06E7 — Hero media upload + ACF seed (all hero contexts).
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: gate | baseline | dry-run | upload | seed | verify | all
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if ( ! function_exists( 'get_plugins' ) ) {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode         = isset( $argv[1] ) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e7-hero-media-system-seed';
$v9_img       = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/img';

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E7_PHASE = 'V9-06E7';

function fp02e7_json_write( $path, $data ) {
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
}

/**
 * Authorized hero media seed targets.
 *
 * @return array<int, array<string, mixed>>
 */
function fp02e7_seed_targets() {
	global $v9_img;

	return array(
		array(
			'key'              => 'home',
			'object_id'        => 4,
			'object_type'      => 'page',
			'acf_field'        => 'hero_media',
			'source_path'      => $v9_img . '/hero/hero-main.png',
			'target_filename'  => 'hero-main.png',
			'title'            => 'Шпиговский дом — hero',
			'alt_text'         => 'Шпиговский дом — центр профилактики и лечения зависимостей',
			'v9_ref'           => 'src/partials/sections/hero.html',
		),
		array(
			'key'              => 'services_hub',
			'object_id'        => 5,
			'object_type'      => 'page',
			'acf_field'        => 'hero_media',
			'source_path'      => $v9_img . '/content/services/services-hero.webp',
			'target_filename'  => 'services-hero.webp',
			'title'            => 'Услуги — hero',
			'alt_text'         => '',
			'v9_ref'           => 'src/pages/uslugi-v2.html',
		),
		array(
			'key'              => 'service_subdivision',
			'object_id'        => 73,
			'object_type'      => 'service',
			'acf_field'        => 'hero_media',
			'source_path'      => $v9_img . '/content/services/service-subdivision-hero.webp',
			'target_filename'  => 'service-subdivision-hero.webp',
			'title'            => 'Зависимости — hero',
			'alt_text'         => '',
			'v9_ref'           => 'src/pages/usluga-podrazdel-v1.html',
		),
		array(
			'key'              => 'service_leaf_alcohol',
			'object_id'        => 74,
			'object_type'      => 'service',
			'acf_field'        => 'hero_media',
			'source_path'      => $v9_img . '/content/services/service-leaf-alcohol-hero.webp',
			'target_filename'  => 'service-leaf-alcohol-hero.webp',
			'title'            => 'Алкогольная зависимость — hero',
			'alt_text'         => '',
			'v9_ref'           => 'src/pages/usluga-konechnaya-v1.html',
		),
	);
}

function fp02e7_summarize_image_field( $value ) {
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

function fp02e7_baseline() {
	$rows = array();
	foreach ( fp02e7_seed_targets() as $target ) {
		$current = function_exists( 'get_field' ) ? get_field( $target['acf_field'], $target['object_id'] ) : null;
		$rows[]  = array(
			'key'       => $target['key'],
			'object_id' => $target['object_id'],
			'field'     => $target['acf_field'],
			'current'   => fp02e7_summarize_image_field( $current ),
		);
	}
	return array(
		'phase'        => FP02_E7_PHASE,
		'generated_at' => gmdate( 'c' ),
		'rows'         => $rows,
	);
}

function fp02e7_upload_attachment( array $target ) {
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';

	if ( ! is_readable( $target['source_path'] ) ) {
		return array( 'ok' => false, 'error' => 'source_missing' );
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

function fp02e7_seed() {
	$results = array();
	foreach ( fp02e7_seed_targets() as $target ) {
		$current = function_exists( 'get_field' ) ? get_field( $target['acf_field'], $target['object_id'] ) : null;
		if ( ! fp02e7_summarize_image_field( $current )['empty'] ) {
			$results[] = array(
				'key'    => $target['key'],
				'result' => 'SKIP_ALREADY_SET',
			);
			continue;
		}

		$upload = fp02e7_upload_attachment( $target );
		if ( empty( $upload['ok'] ) ) {
			$results[] = array(
				'key'    => $target['key'],
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
			'object_id'     => $target['object_id'],
			'field'         => $target['acf_field'],
			'attachment_id' => $upload['attachment_id'],
			'url'           => $upload['url'],
			'result'        => $updated ? 'PASS' : 'ACF_UPDATE_FAIL',
		);
	}

	return array(
		'phase'        => FP02_E7_PHASE,
		'generated_at' => gmdate( 'c' ),
		'results'      => $results,
		'result'       => in_array( 'UPLOAD_FAIL', array_column( $results, 'result' ), true ) || in_array( 'ACF_UPDATE_FAIL', array_column( $results, 'result' ), true ) ? 'FAIL' : 'PASS',
	);
}

function fp02e7_verify() {
	$rows = array();
	foreach ( fp02e7_seed_targets() as $target ) {
		$current = function_exists( 'get_field' ) ? get_field( $target['acf_field'], $target['object_id'] ) : null;
		$summary = fp02e7_summarize_image_field( $current );
		$rows[]  = array(
			'key'       => $target['key'],
			'object_id' => $target['object_id'],
			'field'     => $target['acf_field'],
			'seeded'    => ! $summary['empty'],
			'url'       => $summary['url'] ?? '',
			'result'    => $summary['empty'] ? 'EMPTY' : 'PASS',
		);
	}
	$fail = array_filter( $rows, static fn( $r ) => 'PASS' !== $r['result'] );
	return array(
		'phase'        => FP02_E7_PHASE,
		'generated_at' => gmdate( 'c' ),
		'rows'         => $rows,
		'result'       => empty( $fail ) ? 'PASS' : 'PARTIAL',
	);
}

$out = array( 'mode' => $mode );

switch ( $mode ) {
	case 'baseline':
		$out['baseline'] = fp02e7_baseline();
		break;
	case 'seed':
		$out['seed'] = fp02e7_seed();
		break;
	case 'verify':
		$out['verify'] = fp02e7_verify();
		break;
	case 'all':
		$out['baseline'] = fp02e7_baseline();
		$out['seed']     = fp02e7_seed();
		$out['verify']   = fp02e7_verify();
		break;
	default:
		$out['error'] = 'unknown_mode';
}

fp02e7_json_write( $evidence_dir . '/hero-media-seed-result.json', $out );
echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . PHP_EOL;
