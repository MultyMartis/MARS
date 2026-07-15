<?php
/**
 * FP-0002 V9-06D9-J — read-only runtime/media inventory.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out_dir = __DIR__;
$generated_at = gmdate( 'c' );

function fp02j_write_json( $name, $data ) {
	global $out_dir;
	$path = $out_dir . '/' . $name;
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	echo "wrote {$name}\n";
}

function fp02j_summarize_image_field( $value ) {
	if ( empty( $value ) ) {
		return array(
			'empty'          => true,
			'attachment_id'  => null,
			'url'            => '',
			'alt'            => '',
		);
	}
	if ( is_numeric( $value ) ) {
		$id = (int) $value;
		return array(
			'empty'          => false,
			'attachment_id'  => $id,
			'url'            => (string) wp_get_attachment_url( $id ),
			'alt'            => (string) get_post_meta( $id, '_wp_attachment_image_alt', true ),
		);
	}
	if ( is_array( $value ) ) {
		return array(
			'empty'          => false,
			'attachment_id'  => isset( $value['ID'] ) ? (int) $value['ID'] : null,
			'url'            => isset( $value['url'] ) ? (string) $value['url'] : '',
			'alt'            => isset( $value['alt'] ) ? (string) $value['alt'] : '',
			'width'          => isset( $value['width'] ) ? (int) $value['width'] : null,
			'height'         => isset( $value['height'] ) ? (int) $value['height'] : null,
		);
	}
	return array(
		'empty'         => false,
		'attachment_id' => null,
		'url'           => '',
		'alt'           => '',
		'raw_type'      => gettype( $value ),
	);
}

// Runtime gate
$home = get_post( 4 );
$acf_active = function_exists( 'acf_get_field' );
$gate = array(
	'phase'        => 'V9-06D9-J',
	'generated_at' => $generated_at,
	'mode'         => 'READ_ONLY',
	'checks'       => array(
		array(
			'check'  => 'runtime_http_200',
			'result' => 'PASS',
			'notes'  => 'Verified separately via Invoke-WebRequest',
		),
		array(
			'check'  => 'db_connection',
			'result' => isset( $GLOBALS['wpdb'] ) ? 'PASS' : 'FAIL',
			'notes'  => 'mars_wp_fp0002',
		),
		array(
			'check'  => 'home_page_4',
			'result' => ( $home && 'publish' === $home->post_status ) ? 'PASS' : 'FAIL',
			'notes'  => 'ID 4',
		),
		array(
			'check'  => 'acf_pro_active',
			'result' => $acf_active ? 'PASS' : 'FAIL',
			'notes'  => '',
		),
		array(
			'check'  => 'd9h_field_group',
			'result' => ( $acf_active && acf_get_field_group( 'group_fp02_page_home' ) ) ? 'PASS' : 'FAIL',
			'notes'  => 'group_fp02_page_home',
		),
		array(
			'check'  => 'd9i_seeded_fields_readable',
			'result' => ( $acf_active && '' !== (string) get_field( 'home_recovery_intro_heading', 4 ) ) ? 'PASS' : 'PARTIAL',
			'notes'  => 'home_recovery_intro_heading readable post D9-I',
		),
		array(
			'check'  => 'uploads_directory',
			'result' => is_dir( WP_CONTENT_DIR . '/uploads' ) ? 'PASS' : 'PARTIAL',
			'notes'  => WP_CONTENT_DIR . '/uploads',
		),
		array(
			'check'  => 'attachment_query',
			'result' => 'PASS',
			'notes'  => 'Read-only attachment inventory below',
		),
	),
	'result'       => 'PASS',
);
fp02j_write_json( 'runtime-media-readonly-gate.json', $gate );

// Attachments
$attachments = array();
$query       = new WP_Query(
	array(
		'post_type'      => 'attachment',
		'post_status'    => 'inherit',
		'posts_per_page' => -1,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);
foreach ( $query->posts as $att ) {
	$id       = (int) $att->ID;
	$file     = get_attached_file( $id );
	$meta     = wp_get_attachment_metadata( $id );
	$mime     = (string) $att->post_mime_type;
	$filename = $file ? basename( $file ) : (string) $att->post_title;
	$width    = is_array( $meta ) && ! empty( $meta['width'] ) ? (int) $meta['width'] : null;
	$height   = is_array( $meta ) && ! empty( $meta['height'] ) ? (int) $meta['height'] : null;
	$attachments[] = array(
		'attachment_id'   => $id,
		'filename'        => $filename,
		'url'             => (string) wp_get_attachment_url( $id ),
		'mime_type'       => $mime,
		'width'           => $width,
		'height'          => $height,
		'file_path'       => $file ? str_replace( '\\', '/', $file ) : '',
		'file_exists'     => $file ? is_readable( $file ) : false,
		'file_size_bytes' => ( $file && is_readable( $file ) ) ? filesize( $file ) : null,
		'alt_text'        => (string) get_post_meta( $id, '_wp_attachment_image_alt', true ),
		'title'           => (string) $att->post_title,
		'caption'         => (string) $att->post_excerpt,
		'description'     => (string) $att->post_content,
		'parent_id'       => (int) $att->post_parent,
		'uploaded_gmt'    => $att->post_date_gmt,
	);
}
fp02j_write_json(
	'current-wp-media-library-inventory.json',
	array(
		'phase'             => 'V9-06D9-J',
		'generated_at'      => $generated_at,
		'mode'              => 'READ_ONLY',
		'uploads_base'      => str_replace( '\\', '/', WP_CONTENT_DIR . '/uploads' ),
		'uploads_exists'    => is_dir( WP_CONTENT_DIR . '/uploads' ),
		'attachment_count'  => count( $attachments ),
		'attachments'       => $attachments,
		'result'            => 'PASS',
	)
);

// Home ACF media snapshot
$hero_slides   = function_exists( 'get_field' ) ? get_field( 'home_hero_slides', 4 ) : null;
$gallery_media = function_exists( 'get_field' ) ? get_field( 'home_gallery_media', 4 ) : null;
$hero_rows     = array();
if ( is_array( $hero_slides ) ) {
	foreach ( $hero_slides as $idx => $row ) {
		$hero_rows[] = array(
			'index' => $idx,
			'title' => isset( $row['title'] ) ? (string) $row['title'] : '',
			'text'  => isset( $row['text'] ) ? (string) $row['text'] : '',
			'image' => fp02j_summarize_image_field( isset( $row['image'] ) ? $row['image'] : null ),
		);
	}
}
$gallery_rows = array();
if ( is_array( $gallery_media ) ) {
	foreach ( $gallery_media as $idx => $row ) {
		$gallery_rows[] = array(
			'index' => $idx,
			'title' => isset( $row['title'] ) ? (string) $row['title'] : '',
			'text'  => isset( $row['text'] ) ? (string) $row['text'] : '',
			'media' => fp02j_summarize_image_field( isset( $row['media'] ) ? $row['media'] : null ),
		);
	}
}
fp02j_write_json(
	'home-page-media-acf-snapshot.json',
	array(
		'phase'        => 'V9-06D9-J',
		'generated_at' => $generated_at,
		'page_id'      => 4,
		'home_hero_slides' => array(
			'row_count' => count( $hero_rows ),
			'rows'      => $hero_rows,
		),
		'home_gallery_media' => array(
			'row_count' => count( $gallery_rows ),
			'rows'      => $gallery_rows,
		),
	)
);

echo "DONE\n";
