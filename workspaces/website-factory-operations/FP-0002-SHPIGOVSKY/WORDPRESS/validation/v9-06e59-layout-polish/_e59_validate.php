<?php
/**
 * V9-06E59 frontend validation harness.
 *
 * @package Shpigovsky
 */

if ( php_sapi_name() !== 'cli' ) {
	exit( 1 );
}

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e59-layout-polish-maps-footer-comfort-admin';
if ( ! is_dir( $evidence_dir ) ) {
	wp_mkdir_p( $evidence_dir );
}

$routes = array(
	'/',
	'/kontakty/',
	'/uslugi/',
	'/o-centre/',
);

$results = array(
	'routes' => array(),
	'home_spacing' => array(),
	'contacts_maps' => array(),
	'footer_links' => array(),
	'comfort_cta' => array(),
);

foreach ( $routes as $route ) {
	$url      = home_url( $route );
	$response = wp_remote_get( $url, array( 'timeout' => 30, 'sslverify' => false ) );
	$code     = is_wp_error( $response ) ? 0 : (int) wp_remote_retrieve_response_code( $response );
	$body     = is_wp_error( $response ) ? '' : (string) wp_remote_retrieve_body( $response );
	$results['routes'][ $route ] = array(
		'url' => $url,
		'http' => $code,
		'bytes' => strlen( $body ),
	);
}

$home = wp_remote_get( home_url( '/' ), array( 'timeout' => 30, 'sslverify' => false ) );
$home_body = is_wp_error( $home ) ? '' : (string) wp_remote_retrieve_body( $home );

$spacing_checks = array(
	'home-staff-photo no-top-padding no-top-padding--30' => false !== strpos( $home_body, 'home-staff-photo no-top-padding no-top-padding--30' ),
	'home-feature-grid no-top-padding no-top-padding--30' => false !== strpos( $home_body, 'home-feature-grid no-top-padding no-top-padding--30' ),
	'clinic-landscape no-top-padding' => false !== strpos( $home_body, 'clinic-landscape no-top-padding' ),
	'home-why-us no-top-padding--30' => false !== strpos( $home_body, 'home-why-us no-top-padding--30' ),
	'no @@class literal' => false === strpos( $home_body, '@@class' ),
);
$results['home_spacing'] = $spacing_checks;

$contacts = wp_remote_get( home_url( '/kontakty/' ), array( 'timeout' => 30, 'sslverify' => false ) );
$contacts_body = is_wp_error( $contacts ) ? '' : (string) wp_remote_retrieve_body( $contacts );

$map_hosts = array();
if ( preg_match_all( '#https://api-maps\.yandex\.ru/services/constructor/1\.0/js/\?[^"\']+#i', $contacts_body, $matches ) ) {
	$map_hosts = array_values( array_unique( $matches[0] ) );
}

$results['contacts_maps'] = array(
	'location_articles' => substr_count( $contacts_body, 'class="contacts-location"' ),
	'constructor_scripts' => substr_count( $contacts_body, 'api-maps.yandex.ru/services/constructor/1.0/js/' ),
	'static_map_images' => substr_count( $contacts_body, 'contacts-location__map-image' ),
	'constructor_wrapper' => substr_count( $contacts_body, 'contacts-location__map--constructor' ),
	'addresses' => array(
		'mo' => false !== strpos( $contacts_body, 'Московская область, район ж.д. станции Катуар, д. Сухарево' ),
		'moscow' => false !== strpos( $contacts_body, 'Москва, ул. Ленина, 3' ),
	),
	'urls' => $map_hosts,
);

$footer_checks = array();
foreach ( $routes as $route ) {
	$response = wp_remote_get( home_url( $route ), array( 'timeout' => 30, 'sslverify' => false ) );
	$body     = is_wp_error( $response ) ? '' : (string) wp_remote_retrieve_body( $response );
	$footer_checks[ $route ] = array(
		'uslugi_heading_link' => (bool) preg_match( '#site-footer__nav-heading-link[^>]+href="[^"]*/uslugi/"#', $body ),
		'ocentre_heading_link' => (bool) preg_match( '#site-footer__nav-heading-link[^>]+href="[^"]*/o-centre/"#', $body ),
	);
}
$results['footer_links'] = $footer_checks;

$cta_text = function_exists( 'shpigovsky_get_rehab_requirements_scalar' )
	? shpigovsky_get_rehab_requirements_scalar( 'cta_lead_text', '' )
	: '';
$results['comfort_cta'] = array(
	'acf_value' => $cta_text,
	'frontend_contains' => false !== strpos( $home_body, 'home-rehabilitation-requirements__cta-lead-txt' ) && false !== strpos( $home_body, 'Вы сможете все посмотреть и задать вопросы лично' ),
);

file_put_contents( $evidence_dir . '/validation-report.json', wp_json_encode( $results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
echo wp_json_encode( $results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . PHP_EOL;
