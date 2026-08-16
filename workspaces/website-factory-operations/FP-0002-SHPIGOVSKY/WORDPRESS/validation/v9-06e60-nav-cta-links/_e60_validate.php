<?php
/**
 * V9-06E60 validation + optional CTA option seed (idempotent).
 */
declare(strict_types=1);

$root = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
require $root . '/wp-load.php';

$report = array(
	'wave' => 'V9-06E60',
	'db_writes' => array(),
	'cta_options' => array(),
	'routes' => array(),
	'service_links' => array(),
	'cta_dom' => array(),
);

$ctx = 'fp02-block-cta-bands';
if ( function_exists( 'acf_get_options_page' ) || true ) {
	// Prefer option keys used by block context helpers.
}

$defaults = array(
	'cta_band_default_title' => '',
	'cta_band_default_subtitle' => '',
	'cta_band_phone_hint' => '',
	'cta_band_default_button_label' => '',
);

foreach ( array_keys( $defaults ) as $key ) {
	$before = function_exists( 'get_field' ) ? get_field( $key, 'option' ) : null;
	// Also try options page post id context used by FP02 blocks.
	$before_block = function_exists( 'get_field' ) ? get_field( $key, 'fp02-block-cta-bands' ) : null;
	$report['cta_options'][ $key ] = array(
		'option' => $before,
		'block'  => $before_block,
	);
}

// Seed only phone hint if empty (common hardcoded).
$hint_seed = 'Или позвоните нам';
$hint_now  = get_field( 'cta_band_phone_hint', 'fp02-block-cta-bands' );
if ( ( null === $hint_now || false === $hint_now || '' === trim( (string) $hint_now ) ) && function_exists( 'update_field' ) ) {
	update_field( 'cta_band_phone_hint', $hint_seed, 'fp02-block-cta-bands' );
	$after = get_field( 'cta_band_phone_hint', 'fp02-block-cta-bands' );
	$report['db_writes'][] = array(
		'field' => 'cta_band_phone_hint',
		'context' => 'fp02-block-cta-bands',
		'old' => $hint_now,
		'new' => $after,
		'action' => 'seed_empty',
	);
} else {
	$report['db_writes'][] = array(
		'field' => 'cta_band_phone_hint',
		'action' => 'skip_nonempty_or_missing',
		'value' => $hint_now,
	);
}

$routes = array(
	'/' => 'http://shpigovsky.test/',
	'/uslugi/' => 'http://shpigovsky.test/uslugi/',
	'/uslugi/zavisimosti/' => 'http://shpigovsky.test/uslugi/zavisimosti/',
	'/o-centre/' => 'http://shpigovsky.test/o-centre/',
	'/kontakty/' => 'http://shpigovsky.test/kontakty/',
	'/blog/' => 'http://shpigovsky.test/blog/',
);

foreach ( $routes as $path => $url ) {
	$res = wp_remote_get( $url, array( 'timeout' => 30, 'sslverify' => false ) );
	$code = is_wp_error( $res ) ? 0 : (int) wp_remote_retrieve_response_code( $res );
	$body = is_wp_error( $res ) ? '' : (string) wp_remote_retrieve_body( $res );
	$warn = ( false !== stripos( $body, 'Warning:' ) ) || ( false !== stripos( $body, 'Fatal error' ) ) || ( false !== stripos( $body, 'Notice:' ) && false !== stripos( $body, 'php' ) );
	$report['routes'][ $path ] = array(
		'http' => $code,
		'bytes' => strlen( $body ),
		'php_noise' => $warn,
		'has_program_cta' => ( false !== strpos( $body, 'program-cta-band__wrap01' ) ),
		'has_home_cta' => ( false !== strpos( $body, 'home-rehabilitation-requirements__cta-band' ) ),
		'has_service_name_a' => (bool) preg_match( '/<a[^>]*class="[^"]*services-category-section-v2__service-name/', $body ),
		'old_cta_title_class' => ( false !== strpos( $body, 'program-cta-band__title' ) ),
		'old_name_link_class' => ( false !== strpos( $body, 'service-name-link' ) ),
	);
}

// Service section children page deeper probe.
$z = wp_remote_get( 'http://shpigovsky.test/uslugi/zavisimosti/', array( 'timeout' => 30 ) );
$zb = is_wp_error( $z ) ? '' : (string) wp_remote_retrieve_body( $z );
preg_match_all( '/<a class="services-category-section-v2__service-name" href="([^"]+)">([^<]+)</u', $zb, $m );
$report['service_links']['zavisimosti'] = array();
for ( $i = 0; $i < count( $m[1] ); $i++ ) {
	$report['service_links']['zavisimosti'][] = array( 'href' => $m[1][ $i ], 'text' => $m[2][ $i ] );
}

$hub = wp_remote_get( 'http://shpigovsky.test/uslugi/', array( 'timeout' => 30 ) );
$hb = is_wp_error( $hub ) ? '' : (string) wp_remote_retrieve_body( $hub );
preg_match_all( '/<a class="services-category-section-v2__service-name" href="([^"]+)">([^<]+)</u', $hb, $m2 );
$report['service_links']['uslugi'] = array();
for ( $i = 0; $i < min( 8, count( $m2[1] ) ); $i++ ) {
	$report['service_links']['uslugi'][] = array( 'href' => $m2[1][ $i ], 'text' => $m2[2][ $i ] );
}

// Home CTA vs program CTA structure sample from blog.
$blog = wp_remote_get( 'http://shpigovsky.test/blog/', array( 'timeout' => 30 ) );
$bb = is_wp_error( $blog ) ? '' : (string) wp_remote_retrieve_body( $blog );
$report['cta_dom']['blog_has_wrap01'] = false !== strpos( $bb, 'program-cta-band__wrap01' );
$report['cta_dom']['blog_has_wrap02'] = false !== strpos( $bb, 'program-cta-band__wrap02' );
$report['cta_dom']['blog_has_lead'] = false !== strpos( $bb, 'program-cta-band__lead' );
$report['cta_dom']['blog_has_old_title'] = false !== strpos( $bb, 'program-cta-band__title' );

$home = wp_remote_get( 'http://shpigovsky.test/', array( 'timeout' => 30 ) );
$homb = is_wp_error( $home ) ? '' : (string) wp_remote_retrieve_body( $home );
$report['cta_dom']['home_has_canonical'] = false !== strpos( $homb, 'home-rehabilitation-requirements__cta-lead-txt' );

$out = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links/validation-report.json';
file_put_contents( $out, wp_json_encode( $report, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
echo "WROTE $out\n";
echo 'routes_ok=' . ( count( array_filter( $report['routes'], static function ( $r ) { return 200 === $r['http'] && ! $r['php_noise']; } ) ) ) . '/' . count( $report['routes'] ) . "\n";
echo 'service_links_uslugi=' . count( $report['service_links']['uslugi'] ) . ' zavisimosti=' . count( $report['service_links']['zavisimosti'] ) . "\n";
echo 'db_writes=' . count( array_filter( $report['db_writes'], static function ( $w ) { return ( $w['action'] ?? '' ) === 'seed_empty'; } ) ) . "\n";
