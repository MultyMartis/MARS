<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$routes = array( '/', '/uslugi/', '/blog/', '/specyalisty/', '/o-centre/', '/kontakty/' );
$out    = array();

foreach ( $routes as $path ) {
	$url  = home_url( $path );
	$resp = wp_remote_get(
		$url,
		array(
			'timeout'   => 30,
			'sslverify' => false,
		)
	);
	$code = is_wp_error( $resp ) ? 0 : (int) wp_remote_retrieve_response_code( $resp );
	$body = is_wp_error( $resp ) ? $resp->get_error_message() : wp_remote_retrieve_body( $resp );
	$fatal = ( false !== stripos( (string) $body, 'fatal error' ) || false !== stripos( (string) $body, 'parse error' ) );
	$out[] = array(
		'route'  => $path,
		'http'   => $code,
		'fatal'  => $fatal,
		'bytes'  => is_string( $body ) ? strlen( $body ) : 0,
		'result' => ( 200 === $code && ! $fatal ) ? 'PASS' : 'FAIL',
	);
	echo "{$path}\t{$code}\t" . ( $fatal ? 'FATAL' : 'ok' ) . "\n";
}

$home = wp_remote_get( home_url( '/' ), array( 'timeout' => 30, 'sslverify' => false ) );
$body = is_wp_error( $home ) ? '' : wp_remote_retrieve_body( $home );

$markers = array(
	'home-recovery-intro__benefits',
	'home-treatment-prevention__heading',
	'home-gallery__slider',
	'home-why-us',
	'home-staff-photo',
	'clinic-landscape',
	'home-recovery-life__stages',
	'home-genotyping',
	'home-videos',
	'/uploads/2026/07/shpigovsky-staff-group',
	'/uploads/2026/07/sergey-shpigovsky-interview.mp4',
	'/uploads/2026/07/shpigovsky-center.mp4',
	'imsc42',
);

echo "--- HOME MARKERS ---\n";
foreach ( $markers as $m ) {
	$found = false !== strpos( $body, $m );
	echo ( $found ? 'YES' : 'NO ' ) . "\t{$m}\n";
}

// Count gallery slides in HTML
preg_match_all( '/home-gallery__slide/', $body, $m1 );
echo 'GALLERY_SLIDES=' . count( $m1[0] ) . "\n";

file_put_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e40-home-admin-editable-blocks/_e40_regression.json',
	wp_json_encode(
		array(
			'routes'  => $out,
			'gallery' => count( $m1[0] ),
			'markers' => array_combine(
				$markers,
				array_map(
					static function ( $m ) use ( $body ) {
						return false !== strpos( $body, $m );
					},
					$markers
				)
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

// Operator CSS hash check vs E40 backup
$css_rt = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/assets/css/v9-style.css';
$css_bk = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e40-home-admin-editable-blocks-before-20260714-010957/theme/assets/css/v9-style.css';
if ( is_readable( $css_rt ) && is_readable( $css_bk ) ) {
	echo 'OPERATOR_CSS_MATCH=' . ( hash_file( 'sha256', $css_rt ) === hash_file( 'sha256', $css_bk ) ? 'YES' : 'NO' ) . "\n";
} else {
	// try alternate path
	$alts = glob( 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/**/*style*.css' );
	echo 'CSS_RT_EXISTS=' . ( is_readable( $css_rt ) ? '1' : '0' ) . ' BK=' . ( is_readable( $css_bk ) ? '1' : '0' ) . "\n";
}

echo "REGRESSION_DONE\n";
