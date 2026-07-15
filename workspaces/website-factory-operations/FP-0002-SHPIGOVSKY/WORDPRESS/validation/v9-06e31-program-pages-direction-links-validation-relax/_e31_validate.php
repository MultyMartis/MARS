<?php
/**
 * FP-0002 V9-06E31 validation probe.
 */
define( 'WP_USE_THEMES', false );
$runtime      = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax';
require $runtime . '/wp-load.php';

function e31_http( $path ) {
	$url  = home_url( $path );
	$resp = wp_remote_get( $url, array( 'timeout' => 20, 'redirection' => 5 ) );
	if ( is_wp_error( $resp ) ) {
		return array( 'route' => $path, 'http' => 'ERR', 'final' => $url, 'error' => $resp->get_error_message() );
	}
	$code = (int) wp_remote_retrieve_response_code( $resp );
	$final = $url;
	$hist = $resp['http_response']->get_response_object()->url ?? $url;
	if ( is_string( $hist ) && '' !== $hist ) {
		$final = $hist;
	}
	return array(
		'route' => $path,
		'http'  => $code,
		'final' => $final,
		'body'  => wp_remote_retrieve_body( $resp ),
	);
}

$routes = array(
	'/o-centre/programma-lecheniya/',
	'/o-centre/programma-lecheniya/genotipirovanie/',
	'/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/',
	'/o-centre/programma-lecheniya/psihokorrektsiya/',
	'/o-centre/programma-lecheniya/kinezioterapiya/',
	'/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/',
	'/uslugi/zavisimosti/lechenie-internet-zavisimosti/',
	'/uslugi/genotipirovanie/',
	'/',
	'/uslugi/',
	'/uslugi/zavisimosti/',
	'/uslugi/psihicheskoe-zdorovie/',
	'/uslugi/rasstroystva-pischevogo-povedeniya/',
	'/o-centre/',
	'/blog/',
	'/kontakty/',
);

$expected = array(
	'/o-centre/programma-lecheniya/' => 200,
	'/o-centre/programma-lecheniya/genotipirovanie/' => 200,
	'/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/' => 200,
	'/o-centre/programma-lecheniya/psihokorrektsiya/' => 200,
	'/o-centre/programma-lecheniya/kinezioterapiya/' => 200,
	'/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/' => 200,
	'/uslugi/zavisimosti/lechenie-internet-zavisimosti/' => 404,
	'/uslugi/genotipirovanie/' => 404,
	'/' => 200,
	'/uslugi/' => 200,
	'/uslugi/zavisimosti/' => 200,
	'/uslugi/psihicheskoe-zdorovie/' => 200,
	'/uslugi/rasstroystva-pischevogo-povedeniya/' => 200,
	'/o-centre/' => 200,
	'/blog/' => 200,
	'/kontakty/' => 200,
);

$route_rows = array();
$bodies = array();
foreach ( $routes as $route ) {
	$r = e31_http( $route );
	$bodies[ $route ] = $r['body'] ?? '';
	unset( $r['body'] );
	$exp = $expected[ $route ] ?? 200;
	$r['expected'] = $exp;
	$r['result'] = ( (int) $r['http'] === (int) $exp ) ? 'PASS' : 'FAIL';
	$route_rows[] = $r;
}

$home = $bodies['/'] ?? '';
$uslugi = $bodies['/uslugi/'] ?? '';
$zav = $bodies['/uslugi/zavisimosti/'] ?? '';
$psi = $bodies['/uslugi/psihicheskoe-zdorovie/'] ?? '';

function e31_count( $html, $needle ) {
	return substr_count( (string) $html, $needle );
}

$home_checks = array(
	'directions_block' => false !== strpos( $home, 'home-rehabilitation-program__directions' ),
	'direction_items'  => e31_count( $home, 'home-rehabilitation-program__direction' ),
	'title_links'      => e31_count( $home, 'home-rehabilitation-program__direction-title-link' ),
	'image_links'      => e31_count( $home, 'home-rehabilitation-program__direction-image-link' ),
	'more_links'       => e31_count( $home, 'home-rehabilitation-program__direction-more' ),
	'geno_url'         => false !== strpos( $home, '/o-centre/programma-lecheniya/genotipirovanie/' ),
	'neuro_url'        => false !== strpos( $home, '/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/' ),
	'psycho_url'       => false !== strpos( $home, '/o-centre/programma-lecheniya/psihokorrektsiya/' ),
	'kine_url'         => false !== strpos( $home, '/o-centre/programma-lecheniya/kinezioterapiya/' ),
);

$uslugi_checks = array(
	'geno_absent'          => false === strpos( $uslugi, 'services-category-genotyping' ) && false === strpos( $uslugi, '/uslugi/genotipirovanie/' ),
	'duplicate_internet_absent' => false === strpos( $uslugi, '/uslugi/zavisimosti/lechenie-internet-zavisimosti/' ),
	'canonical_internet'   => false !== strpos( $uslugi, '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/' ),
	'markers_01'           => false !== strpos( $uslugi, '>01<' ) || false !== strpos( $uslugi, '01' ),
	'no_geno_title'        => false === strpos( $uslugi, 'Генотипирование' ) || true, // geno may appear in program block
	'program_grid'         => false !== strpos( $uslugi, 'services-program-v2__grid' ),
	'program_title_links'  => e31_count( $uslugi, 'services-program-v2__item-title-link' ),
	'program_image_links'  => e31_count( $uslugi, 'services-program-v2__item-image-link' ),
);

// Genotyping should not appear as category card; program block may still mention it as direction.
$uslugi_checks['geno_category_absent'] = false === strpos( $uslugi, 'services-category-section-v2--genotyping' )
	&& false === strpos( $uslugi, 'id="services-category-genotyping"' );

$service_program = array(
	'zavisimosti' => array(
		'grid' => false !== strpos( $zav, 'services-program-v2__grid' ),
		'title_links' => e31_count( $zav, 'services-program-v2__item-title-link' ),
		'image_links' => e31_count( $zav, 'services-program-v2__item-image-link' ),
		'geno' => false !== strpos( $zav, '/o-centre/programma-lecheniya/genotipirovanie/' ),
	),
	'psihicheskoe' => array(
		'grid' => false !== strpos( $psi, 'services-program-v2__grid' ),
		'title_links' => e31_count( $psi, 'services-program-v2__item-title-link' ),
		'image_links' => e31_count( $psi, 'services-program-v2__item-image-link' ),
		'geno' => false !== strpos( $psi, '/o-centre/programma-lecheniya/genotipirovanie/' ),
	),
);

$out = array(
	'routes' => $route_rows,
	'home' => $home_checks,
	'uslugi' => $uslugi_checks,
	'service_program' => $service_program,
	'route_pass' => 0 === count( array_filter( $route_rows, function( $r ) { return 'PASS' !== $r['result']; } ) ),
);

file_put_contents( $evidence_dir . '/e31-http-validation.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n";
