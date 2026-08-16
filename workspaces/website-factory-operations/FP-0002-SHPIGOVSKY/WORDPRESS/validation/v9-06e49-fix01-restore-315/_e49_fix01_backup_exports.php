<?php
/**
 * V9-06E49-FIX01 — postmeta/post_content exports BEFORE restore for control posts.
 */
$backup = trim( (string) file_get_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e49-fix01-backup-path.txt'
) );
if ( '' === $backup || ! is_dir( $backup ) ) {
	fwrite( STDERR, "NO_BACKUP_PATH\n" );
	exit( 2 );
}

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$ids = array( 315, 78, 74, 314, 81, 85, 73, 77, 84 );
$pm_dir = $backup . '/postmeta';
$pc_dir = $backup . '/post_content';
if ( ! is_dir( $pm_dir ) ) {
	mkdir( $pm_dir, 0777, true );
}
if ( ! is_dir( $pc_dir ) ) {
	mkdir( $pc_dir, 0777, true );
}

$layout_rows = array();
$layout_rows[] = 'post_id,title,status,permalink,service_editor_role,service_layout_variant,override,parent';

foreach ( $ids as $id ) {
	$post = get_post( $id );
	if ( ! $post ) {
		fwrite( STDERR, "MISSING_POST $id\n" );
		continue;
	}

	$meta = get_post_meta( $id );
	ksort( $meta );
	$lines = array( "meta_key\tmeta_value_json" );
	foreach ( $meta as $key => $values ) {
		$lines[] = $key . "\t" . wp_json_encode( $values, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
	}
	file_put_contents( $pm_dir . '/post-' . $id . '-before.tsv', implode( "\n", $lines ) . "\n" );

	file_put_contents(
		$pc_dir . '/post-' . $id . '-before.html',
		(string) $post->post_content
	);

	$role   = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout = (string) get_post_meta( $id, 'service_layout_variant', true );
	$ovr    = (string) get_post_meta( $id, 'service_layout_override_enabled', true );
	$layout_rows[] = implode(
		',',
		array(
			$id,
			'"' . str_replace( '"', '""', $post->post_title ) . '"',
			$post->post_status,
			'"' . get_permalink( $id ) . '"',
			$role,
			$layout,
			$ovr,
			(string) $post->post_parent,
		)
	);

	// Content fingerprint (non-layout metas) for #315.
	if ( 315 === $id ) {
		$content_meta = array();
		foreach ( $meta as $key => $values ) {
			if ( in_array( $key, array( 'service_editor_role', 'service_layout_variant', 'service_layout_override_enabled', '_service_editor_role', '_service_layout_variant', '_service_layout_override_enabled', '_edit_lock', '_edit_last' ), true ) ) {
				continue;
			}
			if ( 0 === strpos( $key, '_' ) && in_array( ltrim( $key, '_' ), array( 'service_editor_role', 'service_layout_variant', 'service_layout_override_enabled' ), true ) ) {
				continue;
			}
			$content_meta[ $key ] = $values;
		}
		ksort( $content_meta );
		$json = wp_json_encode( $content_meta, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
		file_put_contents( $pm_dir . '/post-315-content-fingerprint-before.json', $json );
		file_put_contents(
			$pm_dir . '/post-315-content-fingerprint-before.sha256',
			hash( 'sha256', $json ) . "\n"
		);
	}
}

file_put_contents( $backup . '/exports/layout-summary-before.csv', implode( "\n", $layout_rows ) . "\n" );
echo "EXPORT_OK backup=$backup\n";
echo implode( "\n", array_slice( $layout_rows, 0, 12 ) ) . "\n";
