<?php
/**
 * V9-06E40 — sync FieldGroups → ACF JSON/DB, seed Home meta, attach media, validate.
 *
 * Usage: php _e40_sync_seed_validate.php
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

$root      = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime   = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$evidence  = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$val_dir   = $root . '/validation/v9-06e40-home-admin-editable-blocks';
$home_id   = (int) get_option( 'page_on_front' );
$result    = array(
	'wave'    => 'V9-06E40',
	'home_id' => $home_id,
	'steps'   => array(),
);

if ( ! is_dir( $evidence ) ) {
	mkdir( $evidence, 0777, true );
}

/**
 * Copy source → runtime and return SHA256 match.
 *
 * @param string $rel Relative under WORDPRESS/.
 * @return array{rel:string,match:bool,source:string,runtime:string}
 */
function e40_sync_file( $rel ) {
	global $root, $runtime;
	$src = $root . '/' . $rel;
	// Map source paths to runtime.
	$dst = $src;
	if ( 0 === strpos( $rel, 'theme/shpigovsky/' ) ) {
		$dst = $runtime . '/wp-content/themes/shpigovsky/' . substr( $rel, strlen( 'theme/shpigovsky/' ) );
	} elseif ( 0 === strpos( $rel, 'plugins/shpigovsky-core/' ) ) {
		$dst = $runtime . '/wp-content/plugins/shpigovsky-core/' . substr( $rel, strlen( 'plugins/shpigovsky-core/' ) );
	} elseif ( 0 === strpos( $rel, 'acf-json/' ) ) {
		$dst = $runtime . '/wp-content/acf-json/' . substr( $rel, strlen( 'acf-json/' ) );
	}
	$dir = dirname( $dst );
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
	copy( $src, $dst );
	$hs = hash_file( 'sha256', $src );
	$hd = hash_file( 'sha256', $dst );
	return array(
		'rel'     => $rel,
		'match'   => $hs === $hd,
		'source'  => $hs,
		'runtime' => $hd,
	);
}

/**
 * Find or create attachment from theme asset path.
 *
 * @param string $asset_rel Relative under theme assets/.
 * @param string $title Attachment title.
 * @return int Attachment ID or 0.
 */
function e40_ensure_attachment( $asset_rel, $title ) {
	$path = get_stylesheet_directory() . '/assets/' . ltrim( $asset_rel, '/' );
	if ( ! is_readable( $path ) ) {
		return 0;
	}

	$basename = basename( $path );
	$existing = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_status'    => 'inherit',
			'posts_per_page' => 5,
			'meta_query'     => array(
				array(
					'key'     => '_wp_attached_file',
					'value'   => $basename,
					'compare' => 'LIKE',
				),
			),
		)
	);
	foreach ( $existing as $p ) {
		$file = get_attached_file( $p->ID );
		if ( $file && basename( $file ) === $basename ) {
			return (int) $p->ID;
		}
	}

	// Also search by title.
	$by_title = get_page_by_title( $title, OBJECT, 'attachment' );
	if ( $by_title instanceof WP_Post ) {
		return (int) $by_title->ID;
	}

	$upload = wp_upload_bits( $basename, null, file_get_contents( $path ) );
	if ( ! empty( $upload['error'] ) ) {
		return 0;
	}

	$filetype = wp_check_filetype( $basename, null );
	$attach_id = wp_insert_attachment(
		array(
			'post_mime_type' => $filetype['type'] ?? 'application/octet-stream',
			'post_title'     => $title,
			'post_content'   => '',
			'post_status'    => 'inherit',
		),
		$upload['file']
	);

	if ( is_wp_error( $attach_id ) || ! $attach_id ) {
		return 0;
	}

	$meta = wp_generate_attachment_metadata( $attach_id, $upload['file'] );
	if ( is_array( $meta ) ) {
		wp_update_attachment_metadata( $attach_id, $meta );
	}

	return (int) $attach_id;
}

// --- 1. Sync PHP sources to runtime ---
$sync_files = array(
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'plugins/shpigovsky-core/src/Fields/RepeaterValidation.php',
	'theme/shpigovsky/inc/home-fallbacks.php',
	'theme/shpigovsky/inc/home-helpers.php',
	'theme/shpigovsky/template-parts/home/recovery-intro.php',
	'theme/shpigovsky/template-parts/home/treatment-prevention.php',
	'theme/shpigovsky/template-parts/home/why-us.php',
	'theme/shpigovsky/template-parts/home/staff-photo.php',
	'theme/shpigovsky/template-parts/home/clinic-landscape.php',
	'theme/shpigovsky/template-parts/home/recovery-life.php',
	'theme/shpigovsky/template-parts/home/genotyping.php',
	'theme/shpigovsky/template-parts/home/videos.php',
);

$sync_rows = array();
foreach ( $sync_files as $rel ) {
	$sync_rows[] = e40_sync_file( $rel );
}
$result['steps']['source_runtime_sync'] = $sync_rows;

// Reload plugin classes if possible — FieldGroups is already loaded; import from runtime file via reflection not needed:
// acf_import_field_group uses get_field_groups which reads from loaded class.
// Force re-require by reading groups from file after copying — class already in memory with OLD definition.
// Workaround: rebuild group array by including a bootstrap that calls the updated runtime file via eval is unsafe.
// Better: use ACF JSON written from a subprocess, OR manually rebuild via CLI re-exec.

echo "SYNCED_FILES=" . count( $sync_rows ) . "\n";
echo "NOTE: FieldGroups class may be stale in this process — re-exec import phase.\n";

file_put_contents(
	$val_dir . '/_e40_sync_phase1.json',
	wp_json_encode( $result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES )
);

echo "PHASE1_OK\n";
