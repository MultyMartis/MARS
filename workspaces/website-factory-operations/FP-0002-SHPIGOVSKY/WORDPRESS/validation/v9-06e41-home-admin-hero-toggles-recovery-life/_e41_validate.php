<?php
/**
 * V9-06E41 validation: frontend markers, toggle off/on, regression HTTP.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$base = 'http://shpigovsky.test';
$page_id = (int) get_option( 'page_on_front' );
if ( $page_id <= 0 ) {
	$page_id = 4;
}

function e41_fetch( $url ) {
	$res = wp_remote_get(
		$url,
		array(
			'timeout'     => 30,
			'redirection' => 3,
		)
	);
	$code = is_wp_error( $res ) ? 0 : (int) wp_remote_retrieve_response_code( $res );
	$body = is_wp_error( $res ) ? '' : (string) wp_remote_retrieve_body( $res );
	return array( $code, $body );
}

list( $code, $html ) = e41_fetch( $base . '/' );
echo "HOME_HTTP={$code} LEN=" . strlen( $html ) . "\n";

$checks = array(
	'hero_slider'           => ( false !== strpos( $html, 'data-hero-slider' ) ),
	'hero_slide_2_title'    => ( false !== strpos( $html, 'Шпиговский дом 2' ) ),
	'hero_slide_1_title'    => ( false !== strpos( $html, 'Шпиговский дом 1' ) ),
	'hero_nav'              => ( false !== strpos( $html, 'data-hero-prev' ) ),
	'hero_dots'             => ( false !== strpos( $html, 'data-hero-pagination' ) ),
	'stage_label_1'         => ( false !== strpos( $html, '1 месяц' ) ),
	'stage_label_2'         => ( false !== strpos( $html, '2 месяц' ) ),
	'stage_label_3'         => ( false !== strpos( $html, '3 месяц' ) ),
	'stage_inner'           => ( false !== strpos( $html, 'home-recovery-life__stage-inner' ) ),
	'stage_label_class'     => ( false !== strpos( $html, 'home-recovery-life__stage-label' ) ),
	'founder_quote'         => ( false !== strpos( $html, 'founder-quote--variant-b' ) ),
);
foreach ( $checks as $k => $ok ) {
	echo ( $ok ? 'PASS' : 'FAIL' ) . "\t{$k}\n";
}

// Toggle founder quote off/on.
update_field( 'home_founder_quote_visible', 0, $page_id );
list( $c2, $h2 ) = e41_fetch( $base . '/?e41=off' );
$off_ok = ( false === strpos( $h2, 'founder-quote--variant-b' ) );
echo ( $off_ok ? 'PASS' : 'FAIL' ) . "\tfounder_toggle_off http={$c2}\n";

update_field( 'home_founder_quote_visible', 1, $page_id );
list( $c3, $h3 ) = e41_fetch( $base . '/?e41=on' );
$on_ok = ( false !== strpos( $h3, 'founder-quote--variant-b' ) );
echo ( $on_ok ? 'PASS' : 'FAIL' ) . "\tfounder_toggle_on http={$c3}\n";

// Ensure all toggles enabled.
$toggles = array(
	'home_hero_autoplay_enabled',
	'home_hero_arrows_enabled',
	'home_hero_dots_enabled',
	'home_founder_quote_visible',
	'home_treatment_prevention_visible',
	'home_gallery_visible',
	'home_reviews_visible',
	'home_rehab_requirements_visible',
	'home_rehab_program_visible',
	'home_comfort_visible',
	'home_specialists_visible',
	'home_articles_visible',
);
foreach ( $toggles as $t ) {
	update_field( $t, 1, $page_id );
}
echo "TOGGLES_RESTORED=1\n";

$routes = array( '/', '/uslugi/', '/blog/', '/specyalisty/', '/o-centre/', '/kontakty/' );
foreach ( $routes as $route ) {
	list( $rc, $rb ) = e41_fetch( $base . $route );
	$fatal = ( false !== stripos( $rb, 'Fatal error' ) || false !== stripos( $rb, 'Uncaught Error' ) );
	echo ( ( 200 === $rc && ! $fatal ) ? 'PASS' : 'FAIL' ) . "\tREGRESSION\t{$route}\thttp={$rc}\tfatal=" . ( $fatal ? '1' : '0' ) . "\n";
}

// Admin field presence probe.
$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'ADMIN_FIELD_COUNT=' . count( (array) $fields ) . "\n";
echo 'DONE\n';
