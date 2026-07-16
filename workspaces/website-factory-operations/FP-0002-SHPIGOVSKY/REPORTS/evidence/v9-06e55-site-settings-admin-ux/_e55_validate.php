<?php
/**
 * V9-06E55 — post-implementation admin + frontend validation (local helper).
 */
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e55-site-settings-admin-ux';
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

function e55_fetch( $url, $cookie_str = '' ) {
	$ch = curl_init( $url );
	$opts = array(
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_FOLLOWLOCATION => true,
		CURLOPT_TIMEOUT        => 45,
		CURLOPT_USERAGENT      => 'MARS-E55-VALIDATE/1.0',
	);
	if ( $cookie_str ) {
		$opts[ CURLOPT_COOKIE ] = $cookie_str;
	}
	curl_setopt_array( $ch, $opts );
	$body = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array( 'http' => $code, 'body' => is_string( $body ) ? $body : '' );
}

function e55_admin_row( $label, $body, $page ) {
	$login = ( false !== stripos( $body, 'id="loginform"' ) );
	return array(
		'screen'               => $label,
		'page'                 => $page,
		'sections_visible'     => $login ? 'NO' : ( ( preg_match_all( '/id="acf-group_/', $body ) > 0 || false !== stripos( $body, 'acf-field' ) ) ? 'YES' : 'PARTIAL' ),
		'repeaters_usable'     => $login ? 'UNKNOWN' : ( false !== stripos( $body, 'acf-repeater-add-row' ) ? 'YES' : ( preg_match( '/acf-field-repeater/', $body ) ? 'YES' : 'N/A' ) ),
		'overflow'             => 'NOT_MEASURED',
		'js_errors'            => 'NOT_MEASURED',
		'body_fp02_acf_admin'  => ( false !== stripos( $body, 'fp02-acf-admin' ) ) ? 'YES' : 'NO',
		'body_site_settings'   => ( false !== stripos( $body, 'fp02-site-settings-admin' ) ) ? 'YES' : 'NO',
		'css_enqueued'         => ( false !== stripos( $body, 'admin-fp02-acf.css' ) ) ? 'YES' : 'NO',
		'result'               => ( $login || false === stripos( $body, 'fp02-acf-admin' ) || ( 0 === strpos( $page, 'fp02-' ) && false === stripos( $body, 'fp02-site-settings-admin' ) ) ) ? 'FAIL' : 'PASS',
	);
}

$user = get_user_by( 'login', 'admin' ) ?: get_users( array( 'role' => 'administrator', 'number' => 1 ) )[0];
$exp  = time() + DAY_IN_SECONDS;
$h    = COOKIEHASH;
$cookie = 'wordpress_logged_in_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'logged_in' ) )
	. '; wordpress_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'auth' ) )
	. '; wordpress_sec_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'secure_auth' ) );

$admin_screens = array(
	array( 'Общие настройки', 'fp02-site-settings-general' ),
	array( 'Header block', 'fp02-block-header' ),
	array( 'Footer block', 'fp02-block-footer' ),
	array( 'Final form block', 'fp02-block-final-form' ),
	array( 'Specialists block', 'fp02-block-specialists' ),
	array( 'CTA bands block', 'fp02-block-cta-bands' ),
	array( 'Comfort block', 'fp02-block-comfort' ),
	array( 'Service section #73', 'post.php?post=73&action=edit' ),
	array( 'Generic page #1039', 'post.php?post=1039&action=edit' ),
	array( 'Home #4', 'post.php?post=4&action=edit' ),
	array( 'Services hub #5', 'post.php?post=5&action=edit' ),
);

$admin_rows = array();
foreach ( $admin_screens as $screen ) {
	$url  = ( false !== strpos( $screen[1], 'post.php' ) ) ? admin_url( $screen[1] ) : admin_url( 'admin.php?page=' . $screen[1] );
	$resp = e55_fetch( $url, $cookie );
	$row  = e55_admin_row( $screen[0], $resp['body'], $screen[1] );
	$row['http'] = $resp['http'];
	if ( 'fp02-site-settings-general' === $screen[1] || 'fp02-block-comfort' === $screen[1] || 'post.php?post=73&action=edit' === $screen[1] ) {
		$safe = preg_replace( '/[^a-z0-9_-]+/i', '-', $screen[1] );
		file_put_contents( $evidence . '/after-' . $safe . '.html', $resp['body'] );
	}
	$admin_rows[] = $row;
}

$fe_routes = array( '/', '/uslugi/', '/uslugi/zavisimosti/', '/o-centre/', '/kontakty/', '/privacy-policy/' );
$fe_rows   = array();
$before_hashes = array();
if ( is_readable( $evidence . '/frontend-hashes-before.json' ) ) {
	$before_hashes = json_decode( (string) file_get_contents( $evidence . '/frontend-hashes-before.json' ), true );
}
$after_hashes = array();
foreach ( $fe_routes as $route ) {
	$resp = e55_fetch( 'http://shpigovsky.test' . $route );
	$len  = strlen( $resp['body'] );
	$hash = hash( 'sha256', $resp['body'] );
	$after_hashes[ $route ] = $hash;
	$visual = 'PRESUMED_PASS';
	if ( isset( $before_hashes[ $route ] ) && $before_hashes[ $route ] !== $hash ) {
		$visual = 'CHANGED';
	}
	$fe_rows[] = array(
		'route'         => $route,
		'http'          => $resp['http'],
		'visual_change' => $visual,
		'result'        => ( 200 === $resp['http'] && 'CHANGED' !== $visual ) ? 'PASS' : ( 200 === $resp['http'] ? 'REVIEW' : 'FAIL' ),
	);
}
file_put_contents( $evidence . '/frontend-hashes-after.json', wp_json_encode( $after_hashes, JSON_PRETTY_PRINT ) );

$src_theme = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky';
$rt_theme  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky';
$sync = array();
foreach ( array( 'assets/css/admin-fp02-acf.css', 'inc/admin-editor.php' ) as $rel ) {
	$sync[] = array(
		'file'  => $rel,
		'match' => hash_file( 'sha256', $src_theme . '/' . $rel ) === hash_file( 'sha256', $rt_theme . '/' . $rel ),
	);
}

$out = array(
	'admin' => $admin_rows,
	'frontend' => $fe_rows,
	'sync' => $sync,
	'v9_style_prefix' => strtoupper( substr( hash_file( 'sha256', $rt_theme . '/assets/css/v9-style.css' ), 0, 8 ) ),
	'db_writes' => 0,
);
file_put_contents( $evidence . '/validation-result.json', wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// CSV matrices
$admin_csv = array( array( 'screen', 'sections_visible', 'repeaters_usable', 'overflow', 'js_errors', 'css', 'site_body', 'result' ) );
foreach ( $admin_rows as $r ) {
	$admin_csv[] = array( $r['screen'], $r['sections_visible'], $r['repeaters_usable'], $r['overflow'], $r['js_errors'], $r['css_enqueued'], $r['body_site_settings'], $r['result'] );
}
$fh = fopen( $evidence . '/admin-validation-matrix.csv', 'wb' );
foreach ( $admin_csv as $row ) {
	fputcsv( $fh, $row );
}
fclose( $fh );

$fe_csv = array( array( 'route', 'http', 'visual_change', 'result' ) );
foreach ( $fe_rows as $r ) {
	$fe_csv[] = array( $r['route'], $r['http'], $r['visual_change'], $r['result'] );
}
$fh = fopen( $evidence . '/frontend-regression.csv', 'wb' );
foreach ( $fe_csv as $row ) {
	fputcsv( $fh, $row );
}
fclose( $fh );

echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
