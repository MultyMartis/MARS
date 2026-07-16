<?php
/**
 * V9-06E55 — authenticated admin screenshots via headless Chrome + saved HTML.
 */
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e55-site-settings-admin-ux';
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$user = get_user_by( 'login', 'admin' ) ?: get_users( array( 'role' => 'administrator', 'number' => 1 ) )[0];
$exp  = time() + DAY_IN_SECONDS;
$h    = COOKIEHASH;
$cookie = 'wordpress_logged_in_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'logged_in' ) )
	. '; wordpress_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'auth' ) )
	. '; wordpress_sec_' . $h . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $exp, 'secure_auth' ) );

$chrome_candidates = array(
	'C:/Program Files/Google/Chrome/Application/chrome.exe',
	'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
	'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
);
$chrome = '';
foreach ( $chrome_candidates as $candidate ) {
	if ( is_readable( $candidate ) ) {
		$chrome = $candidate;
		break;
	}
}
if ( ! $chrome ) {
	fwrite( STDERR, "NO_BROWSER\n" );
	exit( 2 );
}

function e55_fetch_html( $target, $cookie ) {
	$url = ( false !== strpos( $target, 'post.php' ) ) ? admin_url( $target ) : admin_url( 'admin.php?page=' . $target );
	$ch  = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_COOKIE         => $cookie,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
		)
	);
	$body = curl_exec( $ch );
	curl_close( $ch );
	return is_string( $body ) ? $body : '';
}

function e55_shot( $chrome, $html, $out, $w, $h ) {
	$tmp = sys_get_temp_dir() . '/e55-admin-shot-' . wp_generate_password( 8, false ) . '.html';
	file_put_contents( $tmp, $html );
	$cmd = '"' . $chrome . '" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 '
		. '--window-size=' . (int) $w . ',' . (int) $h . ' '
		. '--screenshot="' . str_replace( '/', '\\', $out ) . '" '
		. '"' . str_replace( '/', '\\', $tmp ) . '"';
	exec( $cmd, $ignored, $code );
	@unlink( $tmp );
	return 0 === $code && is_readable( $out );
}

$targets = array(
	'fp02-site-settings-general' => e55_fetch_html( 'fp02-site-settings-general', $cookie ),
	'fp02-block-comfort'           => e55_fetch_html( 'fp02-block-comfort', $cookie ),
	'post.php?post=73&action=edit' => e55_fetch_html( 'post.php?post=73&action=edit', $cookie ),
	'post.php?post=1039&action=edit' => e55_fetch_html( 'post.php?post=1039&action=edit', $cookie ),
	'post.php?post=4&action=edit'  => e55_fetch_html( 'post.php?post=4&action=edit', $cookie ),
);

$before_html = is_readable( $evidence . '/before-fp02-site-settings-general.html' )
	? (string) file_get_contents( $evidence . '/before-fp02-site-settings-general.html' )
	: $targets['fp02-site-settings-general'];

$plan = array(
	array( 'before-site-settings-full.png', $before_html, 1440, 2600 ),
	array( 'after-site-settings-full.png', $targets['fp02-site-settings-general'], 1440, 2600 ),
	array( 'after-site-settings-top.png', $targets['fp02-site-settings-general'], 1440, 900 ),
	array( 'after-site-settings-repeater.png', $targets['fp02-block-comfort'], 1440, 1400 ),
	array( 'after-site-settings-lower.png', $targets['fp02-site-settings-general'], 1440, 1200 ),
	array( 'after-service-73-comparison.png', $targets['post.php?post=73&action=edit'], 1440, 2200 ),
	array( 'after-generic-1039-regression.png', $targets['post.php?post=1039&action=edit'], 1440, 1600 ),
	array( 'after-home-4-regression.png', $targets['post.php?post=4&action=edit'], 1440, 2200 ),
);

$manifest = array();
foreach ( $plan as $item ) {
	list( $file, $html, $w, $h ) = $item;
	$out = $evidence . '/' . $file;
	$ok  = e55_shot( $chrome, $html, $out, $w, $h );
	$manifest[] = array( 'file' => $file, 'ok' => $ok, 'bytes' => $ok ? filesize( $out ) : 0 );
}
file_put_contents( $evidence . '/screenshots-manifest.json', wp_json_encode( $manifest, JSON_PRETTY_PRINT ) );
echo wp_json_encode( $manifest, JSON_PRETTY_PRINT ) . "\n";
