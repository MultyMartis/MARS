<?php
/**
 * V9-06E52 — empty-field hide probe + FE recheck after ACF-only path.
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$src = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/template-parts/generic/content-page.php';
$dst = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/template-parts/generic/content-page.php';
copy( $src, $dst );

/**
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e52e_http( string $url ): array {
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
	return array( 'code' => $code, 'body' => $body );
}

$id  = 14;
$bak = get_field( 'generic_page_body', $id );
$url = (string) get_permalink( $id );

update_field( 'generic_page_body', '', $id );
// Also clear raw meta for sure.
update_post_meta( $id, 'generic_page_body', '' );

$empty = e52e_http( $url );
$phrase = 'Раздел находится в подготовке';
$demo   = false !== strpos( $empty['body'], $phrase );
$src_m  = preg_match( '/data-content-source="([^"]+)"/', $empty['body'], $m ) ? $m[1] : '-';

update_field( 'generic_page_body', $bak, $id );
update_post_meta( $id, 'generic_page_body', is_string( $bak ) ? $bak : '' );
update_post_meta( $id, '_generic_page_body', 'field_fp02_generic_page_body' );

$rest = e52e_http( $url );
$demo2 = false !== strpos( $rest['body'], $phrase );
$src2  = preg_match( '/data-content-source="([^"]+)"/', $rest['body'], $m2 ) ? $m2[1] : '-';

$rows = array(
	array( 'empty_body', $id, 'no_demo_inject', sprintf( 'http=%d;demo=%s;source=%s', $empty['code'], $demo ? 'YES' : 'NO', $src_m ), ( ! $demo && 'empty' === $src_m && 200 === $empty['code'] ) ? 'PASS' : 'FAIL', 'temp clear ACF body' ),
	array( 'restore_body', $id, 'content_returns', sprintf( 'http=%d;demo=%s;source=%s', $rest['code'], $demo2 ? 'YES' : 'NO', $src2 ), ( $demo2 && 'acf' === $src2 && 200 === $rest['code'] ) ? 'PASS' : 'FAIL', 'restored seed' ),
);

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$fp       = fopen( $evidence . '/v9-06e52-empty-field-hide-validation.csv', 'wb' );
fprintf( $fp, "\xEF\xBB\xBF" );
fputcsv( $fp, array( 'step', 'post_id', 'expected', 'actual', 'result', 'notes' ) );
foreach ( $rows as $r ) {
	fputcsv( $fp, $r );
}
fclose( $fp );

// Spot-check FE source=acf on a few pages.
$ids = array( 12, 1031, 1039, 1053 );
$ok  = 0;
foreach ( $ids as $pid ) {
	$r = e52e_http( (string) get_permalink( $pid ) );
	$s = preg_match( '/data-content-source="([^"]+)"/', $r['body'], $mm ) ? $mm[1] : '-';
	if ( 200 === $r['code'] && 'acf' === $s ) {
		++$ok;
	}
	echo "fe_check id=$pid source=$s http={$r['code']}\n";
}

echo 'EMPTY_HIDE ' . ( ! $demo && $demo2 ? 'PASS' : 'FAIL' ) . " fe_acf_source=$ok/" . count( $ids ) . PHP_EOL;
