<?php
/**
 * V9-06E40 — pre-write Home exports into backup folder.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$backup = $argv[1] ?? 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e40-home-admin-editable-blocks-before-20260714-010957';
$exports = $backup . '/exports';
$snapshots = $backup . '/snapshots';
$media = $backup . '/media-map';

foreach ( array( $exports, $snapshots, $media ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

$home_id = (int) get_option( 'page_on_front' );
$site    = site_url( '/' );
$home_u  = home_url( '/' );

echo "HOME_ID={$home_id}\nSITE={$site}\nHOME_URL={$home_u}\n";

$meta  = get_post_meta( $home_id );
$lines = array( "meta_key\tmeta_value_preview" );
foreach ( $meta as $k => $vals ) {
	$v       = is_array( $vals ) ? $vals[0] : $vals;
	$preview = is_string( $v ) ? mb_substr( str_replace( array( "\r", "\n", "\t" ), ' ', $v ), 0, 200 ) : wp_json_encode( $v );
	$lines[] = $k . "\t" . $preview;
}
file_put_contents( $exports . '/home-meta-before.tsv', implode( "\n", $lines ) );

$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'page_id' => $home_id ) ) : array();
$gLines = array( "ID\tkey\ttitle\tactive" );
foreach ( $groups as $g ) {
	$gLines[] = ( $g['ID'] ?? '' ) . "\t" . ( $g['key'] ?? '' ) . "\t" . ( $g['title'] ?? '' ) . "\t" . ( $g['active'] ?? '' );
}
file_put_contents( $exports . '/home-acf-groups-before.tsv', implode( "\n", $gLines ) );

$fields = ( function_exists( 'acf_get_fields' ) && ! empty( $groups ) ) ? acf_get_fields( $groups[0]['key'] ) : array();
$fLines = array( "menu_order\tname\tlabel\ttype\tkey" );
$i      = 0;
foreach ( (array) $fields as $f ) {
	$fLines[] = ( $i++ ) . "\t" . ( $f['name'] ?? '' ) . "\t" . ( $f['label'] ?? '' ) . "\t" . ( $f['type'] ?? '' ) . "\t" . ( $f['key'] ?? '' );
}
file_put_contents( $exports . '/home-admin-inventory-before.txt', implode( "\n", $fLines ) );

$assets = array(
	'staff'          => 'img/content/pre-reviews/shpigovsky-staff-group.webp',
	'landscape'      => 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp',
	'video1'         => 'video/sergey-shpigovsky-interview.mp4',
	'video1_poster'  => 'img/content/videos/sergey-shpigovsky-interview-poster.webp',
	'video2'         => 'video/shpigovsky-center.mp4',
	'video2_poster'  => 'img/content/videos/shpigovsky-center-poster.webp',
);
$map = array();
foreach ( $assets as $k => $rel ) {
	$path = get_stylesheet_directory() . '/assets/' . $rel;
	$uri  = function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $rel ) : '';
	$map[ $k ] = array(
		'theme_rel' => $rel,
		'exists'    => file_exists( $path ),
		'uri'       => $uri,
		'size'      => file_exists( $path ) ? filesize( $path ) : 0,
	);
}

$q    = new WP_Query(
	array(
		'post_type'      => 'attachment',
		'post_status'    => 'inherit',
		'posts_per_page' => 80,
		's'              => 'shpigovsky',
	)
);
$atts = array();
foreach ( $q->posts as $p ) {
	$atts[] = array(
		'id'    => $p->ID,
		'title' => $p->post_title,
		'file'  => get_attached_file( $p->ID ),
		'url'   => wp_get_attachment_url( $p->ID ),
		'mime'  => get_post_mime_type( $p->ID ),
	);
}

file_put_contents(
	$media . '/media-mapping-before.json',
	wp_json_encode(
		array(
			'assets'           => $map,
			'attachments'      => $atts,
			'attachment_755'   => array(
				'exists' => (bool) get_post( 755 ),
				'url'    => wp_get_attachment_url( 755 ),
				'file'   => get_attached_file( 755 ),
			),
			'attachment_754'   => array(
				'url'  => wp_get_attachment_url( 754 ),
				'file' => get_attached_file( 754 ),
			),
			'home_url'         => $home_u,
			'site_url'         => $site,
			'field_count'      => count( (array) $fields ),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

// Frontend snapshot via WP HTTP or file_get_contents.
$response = wp_remote_get(
	$home_u,
	array(
		'timeout'     => 30,
		'redirection' => 5,
		'sslverify'   => false,
	)
);
$code = wp_remote_retrieve_response_code( $response );
$body = wp_remote_retrieve_body( $response );
if ( is_wp_error( $response ) ) {
	echo 'HOME_SNAP_ERR=' . $response->get_error_message() . "\n";
} else {
	file_put_contents( $snapshots . '/home-before.html', $body );
	echo "HOME_HTTP={$code} bytes=" . strlen( $body ) . "\n";
}

echo 'acf_fields=' . count( (array) $fields ) . "\n";
echo "EXPORT_OK\n";
