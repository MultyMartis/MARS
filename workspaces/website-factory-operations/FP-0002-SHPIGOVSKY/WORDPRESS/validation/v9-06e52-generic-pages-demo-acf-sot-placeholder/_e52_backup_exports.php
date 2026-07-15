<?php
/**
 * V9-06E52 — backup meta + frontend snapshots (after DB/theme copy).
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$backup = getenv( 'E52_BACKUP_ROOT' );
if ( ! is_string( $backup ) || '' === $backup || ! is_dir( $backup ) ) {
	fwrite( STDERR, "STOP — E52_BACKUP_ROOT missing\n" );
	exit( 2 );
}

$ids = array( 12, 13, 14, 15, 16, 1030, 1031, 1032, 1033, 1039, 1053, 1054, 1055, 1056, 1097 );
$controls = array(
	'home'         => home_url( '/' ),
	'uslugi'       => home_url( '/uslugi/' ),
	'zavisimosti'  => home_url( '/uslugi/zavisimosti/' ),
	'psihicheskoe' => home_url( '/uslugi/psihicheskoe-zdorovie/' ),
	'rpp'          => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ),
	'svc74'        => get_permalink( 74 ),
	'svc314'       => get_permalink( 314 ),
	'svc315'       => get_permalink( 315 ),
	'svc78'        => get_permalink( 78 ),
	'svc81'        => get_permalink( 81 ),
	'svc85'        => get_permalink( 85 ),
	'blog'         => home_url( '/blog/' ),
	'specyalisty'  => home_url( '/specyalisty/' ),
	'o-centre'     => home_url( '/o-centre/' ),
	'kontakty'     => home_url( '/kontakty/' ),
);

/**
 * @param string $url URL.
 * @return array{0:int,1:string}
 */
function e52_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 40,
			CURLOPT_SSL_VERIFYPEER => false,
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array( $code, $body );
}

global $wpdb;

foreach ( $ids as $id ) {
	$post = get_post( $id );
	file_put_contents( $backup . "/meta/post_content-{$id}-before.txt", (string) ( $post ? $post->post_content : '' ) );
	$rows = $wpdb->get_results(
		$wpdb->prepare( "SELECT meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id=%d ORDER BY meta_key", $id ),
		ARRAY_A
	);
	$fp = fopen( $backup . "/meta/postmeta-{$id}-before.tsv", 'wb' );
	fputcsv( $fp, array( 'meta_key', 'meta_value' ), "\t" );
	foreach ( (array) $rows as $r ) {
		fputcsv( $fp, array( $r['meta_key'], $r['meta_value'] ), "\t" );
	}
	fclose( $fp );

	$url = (string) get_permalink( $id );
	list( $code, $body ) = e52_http( $url );
	file_put_contents( $backup . "/frontend/generic-{$id}-{$code}.html", $body );
}

foreach ( $controls as $slug => $url ) {
	if ( ! $url ) {
		continue;
	}
	list( $code, $body ) = e52_http( (string) $url );
	file_put_contents( $backup . "/frontend/control-{$slug}-{$code}.html", $body );
}

echo "EXPORT_OK\n";
