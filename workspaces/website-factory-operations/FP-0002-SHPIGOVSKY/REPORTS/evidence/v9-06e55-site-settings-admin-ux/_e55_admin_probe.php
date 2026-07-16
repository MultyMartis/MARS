<?php
/**
 * V9-06E55 — Site Settings admin DOM probe (local helper; not for git).
 */
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e55-site-settings-admin-ux';
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

function e55_admin_fetch( $page_slug, $cookie_str ) {
	$url = admin_url( 'admin.php?page=' . rawurlencode( $page_slug ) );
	$ch  = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_COOKIE         => $cookie_str,
			CURLOPT_USERAGENT      => 'MARS-E55-ADMIN-PROBE/1.0',
		)
	);
	$body = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	$final = (string) curl_getinfo( $ch, CURLINFO_EFFECTIVE_URL );
	curl_close( $ch );
	return array(
		'http'      => $code,
		'final_url' => $final,
		'body'      => is_string( $body ) ? $body : '',
	);
}

function e55_analyze_admin_html( $body, $page_slug ) {
	$login = ( false !== stripos( $body, 'id="loginform"' ) || false !== stripos( $body, 'name="log"' ) );
	$has_fp02_body = ( false !== stripos( $body, 'fp02-acf-admin' ) );
	$has_site_body = ( false !== stripos( $body, 'fp02-site-settings-admin' ) );
	$has_css       = ( false !== stripos( $body, 'admin-fp02-acf.css' ) || false !== stripos( $body, 'shpigovsky-fp02-acf-admin' ) );
	$section_titles = preg_match_all( '/fp02-acf-section-title/', $body );
	$postboxes      = preg_match_all( '/class="[^"]*acf-postbox/', $body );
	$repeaters      = preg_match_all( '/acf-field-repeater/', $body );
	$acf_rows       = preg_match_all( '/class="[^"]*acf-row/', $body );
	$group_titles   = array();
	if ( preg_match_all( '/<h2 class="hndle[^"]*"><span>([^<]+)<\/span>/', $body, $m ) ) {
		$group_titles = array_map( 'html_entity_decode', $m[1] );
	}
	$hook_guess = '';
	if ( preg_match( '/body class="([^"]+)"/', $body, $bm ) ) {
		$classes = explode( ' ', $bm[1] );
		foreach ( $classes as $cls ) {
			if ( false !== strpos( $cls, 'fp02-' ) || false !== strpos( $cls, 'settings_page_' ) || false !== strpos( $cls, 'toplevel_page_' ) ) {
				$hook_guess = $cls;
				break;
			}
		}
	}
	return array(
		'page'               => $page_slug,
		'login_redirect'     => $login,
		'body_fp02_acf_admin'=> $has_fp02_body,
		'body_site_settings' => $has_site_body,
		'css_enqueued'       => $has_css,
		'section_title_count'=> (int) $section_titles,
		'postbox_count'      => (int) $postboxes,
		'repeater_count'     => (int) $repeaters,
		'acf_row_count'      => (int) $acf_rows,
		'postbox_titles'     => $group_titles,
		'body_hook_class'    => $hook_guess,
	);
}

$user = get_user_by( 'login', 'admin' ) ?: get_user_by( 'login', 'mli_admin_fp0002' );
if ( ! $user ) {
	$admins = get_users( array( 'role' => 'administrator', 'number' => 1 ) );
	$user   = $admins ? $admins[0] : null;
}
if ( ! $user ) {
	fwrite( STDERR, "NO_ADMIN_USER\n" );
	exit( 2 );
}

$expiration  = time() + DAY_IN_SECONDS;
$cookie_hash = COOKIEHASH;
$cookie_str  = 'wordpress_logged_in_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'logged_in' ) )
	. '; wordpress_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'auth' ) )
	. '; wordpress_sec_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'secure_auth' ) );

$pages = array(
	'fp02-site-settings-general',
	'fp02-block-header',
	'fp02-block-footer',
	'fp02-block-final-form',
	'fp02-block-specialists',
	'fp02-block-cta-bands',
	'fp02-block-comfort',
);

$rows = array();
foreach ( $pages as $page ) {
	$resp = e55_admin_fetch( $page, $cookie_str );
	$row  = e55_analyze_admin_html( $resp['body'], $page );
	$row['http'] = $resp['http'];
	$rows[] = $row;
	if ( ! $row['login_redirect'] ) {
		$safe = preg_replace( '/[^a-z0-9_-]+/i', '-', $page );
		file_put_contents( $evidence . '/before-' . $safe . '.html', $resp['body'] );
	}
}

// Service comparison #73
$svc = e55_admin_fetch( 'post.php?post=73&action=edit', $cookie_str );
$svc_row = e55_analyze_admin_html( $svc['body'], 'service-73' );
$svc_row['http'] = $svc['http'];
$rows[] = $svc_row;

// Hook suffix simulation for enqueue logic.
$enqueue_checks = array();
foreach ( array_merge( $pages, array( 'fp02-site-settings-blocks' ) ) as $slug ) {
	$hook = 'settings_page_' . $slug;
	$enqueue_checks[] = array(
		'slug' => $slug,
		'hypothetical_hook' => $hook,
		'current_e53_match' => ( false !== strpos( $hook, 'fp02-site-settings' ) ),
		'proposed_fp02_block_match' => ( 0 === strpos( $slug, 'fp02-block-' ) || false !== strpos( $hook, 'fp02-site-settings' ) ),
	);
}

$out = array(
	'generated_at' => gmdate( 'c' ),
	'screens'      => $rows,
	'enqueue_checks' => $enqueue_checks,
	'function_exists' => array(
		'shpigovsky_admin_should_enqueue_fp02_acf_css' => function_exists( 'shpigovsky_admin_should_enqueue_fp02_acf_css' ),
	),
);

$json_path = $evidence . '/before-admin-probe.json';
file_put_contents( $json_path, wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
