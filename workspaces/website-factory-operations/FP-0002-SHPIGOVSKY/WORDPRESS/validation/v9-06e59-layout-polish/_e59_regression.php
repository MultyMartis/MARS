<?php
/**
 * V9-06E59 regression route smoke.
 */
if ( php_sapi_name() !== 'cli' ) {
	exit( 1 );
}
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$routes = array(
	'/',
	'/uslugi/',
	'/uslugi/zavisimosti/',
	'/uslugi/zavisimosti/lechenie-alkogolnoj-zavisimosti/',
	'/uslugi/zavisimosti/lechenie-narkoticheskoj-zavisimosti/',
	'/uslugi/psihicheskie-rasstrojstva/',
	'/o-centre/',
	'/kontakty/',
	'/blog/',
);
$out = array();
foreach ( $routes as $route ) {
	$r = wp_remote_get( home_url( $route ), array( 'timeout' => 30, 'sslverify' => false ) );
	$body = is_wp_error( $r ) ? '' : (string) wp_remote_retrieve_body( $r );
	$out[] = array(
		'route' => $route,
		'http' => is_wp_error( $r ) ? 0 : (int) wp_remote_retrieve_response_code( $r ),
		'has_horizontal_overflow_hint' => false !== strpos( $body, 'overflow-x: scroll' ),
		'php_warning' => (bool) preg_match( '/(Notice|Warning|Fatal error):/i', $body ),
	);
}
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e59-layout-polish-maps-footer-comfort-admin/regression-matrix.json';
file_put_contents( $evidence, wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE );
