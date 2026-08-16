<?php
/**
 * Generate auth cookies for local admin screenshot session (temporary evidence helper).
 */
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$user_id = 1; // mli_admin_fp0002
wp_set_current_user( $user_id );
wp_set_auth_cookie( $user_id, true );

$cookies = array();
foreach ( array( LOGGED_IN_COOKIE, AUTH_COOKIE, SECURE_AUTH_COOKIE, USER_COOKIE, PASS_COOKIE ) as $name ) {
	if ( ! empty( $_COOKIE[ $name ] ) ) {
		$cookies[ $name ] = $_COOKIE[ $name ];
	}
}

// Also capture from headers that would be sent.
$ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression';

// Build cookie jar manually using wp_generate_auth_cookie
$logged = wp_generate_auth_cookie( $user_id, time() + DAY_IN_SECONDS, 'logged_in' );
$auth   = wp_generate_auth_cookie( $user_id, time() + DAY_IN_SECONDS, 'auth' );

$jar = array(
	LOGGED_IN_COOKIE => $logged,
	AUTH_COOKIE      => $auth,
);

file_put_contents( $ev . '/_admin-cookies.json', wp_json_encode( $jar, JSON_PRETTY_PRINT ) );

// Fetch admin pages with cookies via WP HTTP API impersonation isn't enough for full HTML.
// Use curl-like stream with Cookie header.
$cookie_header = LOGGED_IN_COOKIE . '=' . rawurlencode( $logged ) . '; ' . AUTH_COOKIE . '=' . rawurlencode( $auth );

$pages = array(
	'service-74'      => admin_url( 'post.php?post=74&action=edit' ),
	'service-73'      => admin_url( 'post.php?post=73&action=edit' ),
	'ocentre-11'      => admin_url( 'post.php?post=11&action=edit' ),
	'reviews'         => admin_url( 'admin.php?page=fp02-reviews' ),
	'site-settings'   => admin_url( 'admin.php?page=fp02-site-settings-general' ),
	'contacts-20'     => admin_url( 'post.php?post=20&action=edit' ),
	'blog-19'         => admin_url( 'post.php?post=19&action=edit' ),
	'founder'         => admin_url( 'admin.php?page=fp02-block-founder-quote' ),
);

$admin_matrix = array();
foreach ( $pages as $key => $url ) {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_HTTPHEADER     => array( 'Cookie: ' . $cookie_header ),
			CURLOPT_USERAGENT      => 'FP0002-E62C-AdminProbe/1.0',
		)
	);
	$body = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	$body = is_string( $body ) ? $body : '';
	$checks = array(
		'url'  => $url,
		'code' => $code,
		'is_login' => false !== strpos( $body, 'wp-login.php' ) || false !== strpos( $body, 'loginform' ),
		'has_structured_title' => false !== strpos( $body, 'Service — Structured Sections' ),
		'has_relationships_title' => false !== strpos( $body, 'Service — Relationships' ),
		'has_review_uid_label' => false !== strpos( $body, 'Постоянный ID отзыва' ),
		'has_bullet_intro_label' => false !== strpos( $body, 'Дополнительный текст после вводного блока' ),
		'has_breadcrumb_fields' => false !== strpos( $body, 'show_breadcrumbs' ) || false !== strpos( $body, 'Хлебн' ),
		'bytes' => strlen( $body ),
	);
	$admin_matrix[ $key ] = $checks;
	file_put_contents( $ev . '/admin-html-' . $key . '.html', $body );
}

file_put_contents( $ev . '/admin-validation-matrix.json', wp_json_encode( $admin_matrix, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $admin_matrix, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
