<?php
/**
 * V9-06E62C frontend/admin regression probe.
 */
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression';
$base = 'http://shpigovsky.test';

function e62c_fetch( $url ) {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 30,
			CURLOPT_USERAGENT      => 'FP0002-E62C-Probe/1.0',
			CURLOPT_HEADER         => true,
		)
	);
	$raw  = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	$err  = curl_error( $ch );
	curl_close( $ch );
	if ( false === $raw ) {
		return array( 'code' => 0, 'body' => '', 'error' => $err );
	}
	$parts = explode( "\r\n\r\n", $raw, 2 );
	$body  = isset( $parts[1] ) ? $parts[1] : $raw;
	// Handle redirects with multiple headers.
	if ( 0 === strpos( $body, 'HTTP/' ) ) {
		$parts2 = explode( "\r\n\r\n", $body, 2 );
		$body   = isset( $parts2[1] ) ? $parts2[1] : $body;
	}
	$warn = ( false !== stripos( $body, 'Fatal error' ) )
		|| ( false !== stripos( $body, 'Warning:' ) && false !== stripos( $body, '.php' ) )
		|| ( false !== stripos( $body, 'Notice:' ) && false !== stripos( $body, '.php' ) )
		|| ( false !== stripos( $body, 'Deprecated:' ) && false !== stripos( $body, 'on line' ) );
	return array(
		'code'     => $code,
		'body'     => $body,
		'bytes'    => strlen( $body ),
		'php_warn' => $warn,
		'error'    => '',
	);
}

$routes = array(
	array( '/', 200 ),
	array( '/uslugi/', 200 ),
	array( '/uslugi/zavisimosti/', 200 ),
	array( '/uslugi/zavisimosti/lechenie-alkogolnoj-zavisimosti/', 200 ),
	array( '/o-centre/', 200 ),
	array( '/o-centre/galereya-o-dome/', 200 ),
	array( '/specyalisty/', 200 ),
	array( '/kontakty/', 200 ),
	array( '/blog/', 200 ),
	array( '/blog/page/2/', 200 ),
	array( '/otzyvy/', 200 ),
	array( '/otzyvy/page/2/', 200 ),
	array( '/otzyvy/page/3/', 200 ),
	array( '/otzyvy/page/99/', 404 ),
	array( '/this-route-should-404-e62c/', 404 ),
);

// Specialist child — discover one.
$spec = get_posts(
	array(
		'post_type'      => 'specialist',
		'post_status'    => 'publish',
		'posts_per_page' => 1,
		'fields'         => 'ids',
	)
);
if ( ! empty( $spec ) ) {
	$permalink = get_permalink( $spec[0] );
	if ( $permalink ) {
		$path = str_replace( home_url(), '', $permalink );
		$routes[] = array( $path, 200 );
	}
}

// Blog single.
$blog = get_posts(
	array(
		'post_type'      => 'post',
		'post_status'    => 'publish',
		'posts_per_page' => 1,
		'fields'         => 'ids',
	)
);
if ( ! empty( $blog ) ) {
	$permalink = get_permalink( $blog[0] );
	if ( $permalink ) {
		$path = str_replace( home_url(), '', $permalink );
		$routes[] = array( $path, 200 );
	}
}

$route_rows = array();
foreach ( $routes as $r ) {
	$url  = $base . $r[0];
	$res  = e62c_fetch( $url );
	$pass = ( (int) $res['code'] === (int) $r[1] ) && empty( $res['php_warn'] );
	$route_rows[] = array(
		'route'    => $r[0],
		'expected' => $r[1],
		'actual'   => $res['code'],
		'bytes'    => $res['bytes'],
		'php_warn' => $res['php_warn'] ? 1 : 0,
		'pass'     => $pass ? 'PASS' : 'FAIL',
	);
}

// O-centre deep DOM checks.
$oc = e62c_fetch( $base . '/o-centre/' );
$body = $oc['body'];
$oc_checks = array(
	'http_200'                 => 200 === (int) $oc['code'],
	'no_o_centre_cta_1'        => false === strpos( $body, 'id="o-centre-cta-1"' ),
	'no_who_we_treat_gallery'  => false === strpos( $body, 'services-category-section-v2__gallery' ) || false === strpos( $body, 'id="who-we-treat"' ) || ! preg_match( '/id="who-we-treat"[\s\S]{0,8000}?services-category-section-v2__gallery/', $body ),
	'has_who_we_treat'         => false !== strpos( $body, 'id="who-we-treat"' ),
	'has_program_cta_band'     => false !== strpos( $body, 'program-cta-band' ),
	'lead_without_inner_span'  => (bool) preg_match( '/<p class="infrastructure-narrative__lead block-whith-red-line">[^<]/<\/p>/u', $body ),
	'has_bullet_intro'         => (bool) preg_match( '/infrastructure-narrative__lead block-whith-red-line">[^<]+<\/p>\s*<p class="infrastructure-narrative__bullet"><span>/u', $body ),
	'bullet_has_seed_snip'     => false !== strpos( $body, 'бассейн и сауна' ),
	'nested_section_cta'       => (bool) preg_match( '/id="who-we-treat"[\s\S]{0,12000}?<section[^>]*program-cta-band-section/u', $body ),
	'cta_as_div_inside'        => (bool) preg_match( '/id="who-we-treat"[\s\S]{0,12000}?<div class="program-cta-band"/u', $body ),
	'has_staff_home'           => false !== strpos( $body, 'staff' ) || false !== strpos( $body, 'Команда' ),
	'has_feature_home'         => false !== strpos( $body, 'home-feature' ) || false !== strpos( $body, 'Преимущества' ),
	'has_landscape_home'       => false !== strpos( $body, 'landscape' ) || false !== strpos( $body, 'Территория' ),
	'duplicate_who_we_treat'   => substr_count( $body, 'id="who-we-treat"' ) <= 1,
	'duplicate_our_home'       => substr_count( $body, 'id="our-home"' ) <= 1,
);

// Extract who-we-treat CTA snippet.
$cta_dom = '';
if ( preg_match( '/id="who-we-treat"([\s\S]{0,15000})<\/section>/u', $body, $m ) ) {
	$cta_dom = '<section id="who-we-treat"' . $m[1] . '</section>';
}
file_put_contents( $ev . '/ocentre-who-we-treat-dom-after.html', $cta_dom );

// Infrastructure lead snippet.
$lead_dom = '';
if ( preg_match( '/<div class="infrastructure-narrative__group infrastructure-narrative__group--intro"[\s\S]*?<\/div>/u', $body, $m ) ) {
	$lead_dom = $m[0];
}
file_put_contents( $ev . '/ocentre-infrastructure-intro-dom-after.html', $lead_dom );

// Reviews anchors.
$otz = e62c_fetch( $base . '/otzyvy/' );
preg_match_all( '/id="(review-[a-z0-9]+)"/', $otz['body'], $ids1 );
$otz2 = e62c_fetch( $base . '/otzyvy/page/2/' );
preg_match_all( '/id="(review-[a-z0-9]+)"/', $otz2['body'], $ids2 );
$otz3 = e62c_fetch( $base . '/otzyvy/page/3/' );
preg_match_all( '/id="(review-[a-z0-9]+)"/', $otz3['body'], $ids3 );
$all_ids = array_merge( $ids1[1] ?? array(), $ids2[1] ?? array(), $ids3[1] ?? array() );
$review_anchor = array(
	'page1'          => $ids1[1] ?? array(),
	'page2'          => $ids2[1] ?? array(),
	'page3'          => $ids3[1] ?? array(),
	'total'          => count( $all_ids ),
	'unique'         => count( array_unique( $all_ids ) ),
	'no_legacy_idx'  => 0 === count( array_filter( $all_ids, static function ( $id ) {
		return preg_match( '/^review-\d+$/', $id );
	} ) ),
);

// Home slider links.
$home = e62c_fetch( $base . '/' );
preg_match_all( '/data-review-slider-full-link[^>]*href="([^"]+)"/', $home['body'], $slinks );
$slider_links = $slinks[1] ?? array();
$slider_ok = true;
foreach ( $slider_links as $href ) {
	if ( ! preg_match( '/#review-[a-z0-9]+/', $href ) ) {
		$slider_ok = false;
	}
	if ( preg_match( '/#review-\d+$/', $href ) ) {
		$slider_ok = false;
	}
}

// Service field groups visibility (admin filter simulation).
$service_id = 74;
$role = (string) get_field( 'service_editor_role', $service_id );
$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $service_id ) ) : array();
$group_keys = array_map( static function ( $g ) { return $g['key'] ?? ''; }, $groups );
$service_admin = array(
	'service_id' => $service_id,
	'role'       => $role,
	'has_structured' => in_array( 'group_fp02_service_structured_sections', $group_keys, true ),
	'has_relationships' => in_array( 'group_fp02_service_relationships', $group_keys, true ),
	'visible_keys' => array_values( array_filter( $group_keys ) ),
);

// Section role sample.
$section_id = 73;
$role_s = (string) get_field( 'service_editor_role', $section_id );
$groups_s = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $section_id ) ) : array();
$keys_s = array_map( static function ( $g ) { return $g['key'] ?? ''; }, $groups_s );
$section_admin = array(
	'service_id' => $section_id,
	'role'       => $role_s,
	'has_structured' => in_array( 'group_fp02_service_structured_sections', $keys_s, true ),
	'has_relationships' => in_array( 'group_fp02_service_relationships', $keys_s, true ),
);

// Demo inventory.
$demo_posts = get_posts(
	array(
		'post_type'      => 'post',
		'post_status'    => 'any',
		'posts_per_page' => 50,
		'name__in'       => array_map( static function ( $n ) {
			return sprintf( 'demo-pagination-article-%02d', $n );
		}, range( 1, 10 ) ),
	)
);
$demo_blog = array();
foreach ( $demo_posts as $p ) {
	$demo_blog[] = array( 'ID' => $p->ID, 'slug' => $p->post_name, 'title' => $p->post_title );
}

$review_matrix = json_decode( file_get_contents( $ev . '/review-uid-migration-matrix.json' ), true );
$demo_reviews = array_values( array_filter( $review_matrix ?: array(), static function ( $r ) {
	return ! empty( $r['is_demo'] ) || false !== stripos( (string) ( $r['author'] ?? '' ), 'demo' );
} ) );

$out = array(
	'routes'           => $route_rows,
	'ocentre'          => $oc_checks,
	'review_anchors'   => $review_anchor,
	'slider_links'     => array(
		'count' => count( $slider_links ),
		'links' => $slider_links,
		'pass'  => $slider_ok && count( $slider_links ) > 0,
	),
	'service_admin_74' => $service_admin,
	'service_admin_73' => $section_admin,
	'demo_blog'        => $demo_blog,
	'demo_reviews_count' => count( $demo_reviews ),
);

file_put_contents( $ev . '/regression-probe.json', wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

$csv = "route,expected,actual,php_warn,pass\n";
foreach ( $route_rows as $row ) {
	$csv .= "{$row['route']},{$row['expected']},{$row['actual']},{$row['php_warn']},{$row['pass']}\n";
}
file_put_contents( $ev . '/route-http-matrix.csv', $csv );

file_put_contents( $ev . '/demo-content-inventory.json', wp_json_encode( array(
	'blog_posts' => $demo_blog,
	'reviews'    => $demo_reviews,
	'note'       => 'Local demo content; require operator decision before production cleanup. Do not delete in E62C.',
	'cleanup_procedure' => array(
		'1. Operator confirm production cleanup charter',
		'2. Backup DB',
		'3. Trash/delete blog IDs 1745-1754 (or current demo list)',
		'4. Remove reviews_items rows marked e62b-demo / is_demo from fp02-reviews options',
		'5. Re-verify pagination page counts',
	),
), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

echo 'ROUTES ' . count( array_filter( $route_rows, static function ( $r ) { return 'PASS' === $r['pass']; } ) ) . '/' . count( $route_rows ) . PHP_EOL;
echo 'OCENTRE ' . wp_json_encode( $oc_checks ) . PHP_EOL;
echo 'ANCHORS total=' . $review_anchor['total'] . ' unique=' . $review_anchor['unique'] . ' no_legacy=' . ( $review_anchor['no_legacy_idx'] ? '1' : '0' ) . PHP_EOL;
echo 'SLIDER ' . ( $slider_ok ? 'PASS' : 'FAIL' ) . ' count=' . count( $slider_links ) . PHP_EOL;
echo 'ADMIN74 structured=' . ( $service_admin['has_structured'] ? 'YES' : 'NO' ) . ' rel=' . ( $service_admin['has_relationships'] ? 'YES' : 'NO' ) . PHP_EOL;
echo 'ADMIN73 structured=' . ( $section_admin['has_structured'] ? 'YES' : 'NO' ) . ' rel=' . ( $section_admin['has_relationships'] ? 'YES' : 'NO' ) . PHP_EOL;
