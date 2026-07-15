<?php
/**
 * V9-06E34 validation — pages, slider automation, regression HTTP.
 */
require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider';
$backup  = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e34-specialists-pages-slider-before-20260713-020509';

/**
 * @param string $url URL.
 * @return array{http:int,bytes:int,body:string,error:string}
 */
function fp02_e34_http( $url ) {
	$res = wp_remote_get(
		$url,
		array(
			'timeout'     => 30,
			'redirection' => 5,
			'sslverify'   => false,
		)
	);
	if ( is_wp_error( $res ) ) {
		return array( 'http' => 0, 'bytes' => 0, 'body' => '', 'error' => $res->get_error_message() );
	}
	$body = (string) wp_remote_retrieve_body( $res );
	return array(
		'http'  => (int) wp_remote_retrieve_response_code( $res ),
		'bytes' => strlen( $body ),
		'body'  => $body,
		'error' => '',
	);
}

$parent = get_page_by_path( 'specyalisty' );
$cards  = function_exists( 'shpigovsky_get_specialists_cards' ) ? shpigovsky_get_specialists_cards() : array();
$children = array();
if ( $parent instanceof WP_Post ) {
	$children = get_posts(
		array(
			'post_type'      => 'page',
			'post_parent'    => (int) $parent->ID,
			'post_status'    => 'publish',
			'numberposts'    => 50,
			'orderby'        => array( 'menu_order' => 'ASC', 'title' => 'ASC' ),
		)
	);
}

$child_rows = array();
foreach ( $children as $c ) {
	$child_rows[] = array(
		'ID'         => (int) $c->ID,
		'title'      => $c->post_title,
		'slug'       => $c->post_name,
		'url'        => get_permalink( $c->ID ),
		'template'   => (string) get_page_template_slug( $c->ID ),
		'menu_order' => (int) $c->menu_order,
		'thumb'      => (int) get_post_thumbnail_id( $c->ID ),
		'excerpt'    => $c->post_excerpt,
	);
}

$routes = array(
	'/',
	'/specyalisty/',
	'/specyalisty/shipovsky/',
	'/specyalisty/kazakov/',
	'/specyalisty/kostyuk/',
	'/specyalisty/shapiguzova/',
	'/uslugi/',
	'/o-centre/',
	'/o-centre/programma-lecheniya/',
	'/blog/',
	'/kontakty/',
);

$route_results = array();
foreach ( $routes as $path ) {
	$url  = home_url( $path );
	$probe = fp02_e34_http( $url );
	$fatal = ( false !== stripos( $probe['body'], 'Fatal error' ) || false !== stripos( $probe['body'], 'Uncaught Error' ) );
	$route_results[] = array(
		'route'  => $path,
		'url'    => $url,
		'http'   => $probe['http'],
		'bytes'  => $probe['bytes'],
		'fatal'  => $fatal,
		'result' => ( 200 === $probe['http'] && ! $fatal ) ? 'PASS' : 'FAIL',
	);
}

$home = fp02_e34_http( home_url( '/' ) );
$spec = fp02_e34_http( home_url( '/specyalisty/' ) );
@file_put_contents( $backup . '/home-route-snapshot-after.html', $home['body'] );
@file_put_contents( $backup . '/specialists-route-snapshot-after.html', $spec['body'] );

/**
 * Parse specialists slider from HTML.
 *
 * @param string $html HTML.
 * @return array<string,mixed>
 */
function fp02_e34_parse_slider( $html ) {
	$out = array(
		'slider_present' => false !== strpos( $html, 'data-specialists-slider' ),
		'cards'          => 0,
		'links'          => array(),
		'names'          => array(),
		'all_link'       => '',
		'duplicates'     => array(),
	);
	if ( preg_match_all( '/class="specialists__card[^"]*"/', $html, $m ) ) {
		$out['cards'] = count( $m[0] );
	}
	if ( preg_match_all( '/class="specialists__card-link"[^>]*href="([^"]+)"/', $html, $m ) ) {
		$out['links'] = $m[1];
	}
	if ( preg_match_all( '/class="specialists__name"[^>]*>([^<]+)</', $html, $m ) ) {
		$out['names'] = array_map( 'trim', $m[1] );
		$counts = array_count_values( $out['names'] );
		foreach ( $counts as $n => $c ) {
			if ( $c > 1 ) {
				$out['duplicates'][] = $n;
			}
		}
	}
	if ( preg_match( '/class="specialists__all-link"[^>]*href="([^"]+)"/', $html, $m ) ) {
		$out['all_link'] = $m[1];
	}
	return $out;
}

$home_slider = fp02_e34_parse_slider( $home['body'] );
$link_checks = array();
foreach ( $home_slider['links'] as $link ) {
	$p = fp02_e34_http( $link );
	$link_checks[] = array( 'url' => $link, 'http' => $p['http'], 'result' => 200 === $p['http'] ? 'PASS' : 'FAIL' );
}

// Confirm cards match child query (not ACF/static count of 5 with duplicate).
$expected_count = count( $children );
$card_count_ok  = count( $cards ) === $expected_count && $home_slider['cards'] === $expected_count;
$links_to_children = true;
$child_urls = array_map( 'untrailingslashit', wp_list_pluck( $child_rows, 'url' ) );
foreach ( $home_slider['links'] as $link ) {
	if ( ! in_array( untrailingslashit( $link ), $child_urls, true ) ) {
		$links_to_children = false;
		break;
	}
}

$out = array(
	'parent' => $parent instanceof WP_Post ? array(
		'ID'       => (int) $parent->ID,
		'title'    => $parent->post_title,
		'url'      => get_permalink( $parent->ID ),
		'template' => (string) get_page_template_slug( $parent->ID ),
	) : null,
	'children'              => $child_rows,
	'child_count'           => count( $child_rows ),
	'cards_from_query'      => $cards,
	'cards_query_count'     => count( $cards ),
	'home_slider'           => $home_slider,
	'home_link_checks'      => $link_checks,
	'card_count_matches'    => $card_count_ok,
	'links_are_children'    => $links_to_children,
	'no_name_duplicates'    => empty( $home_slider['duplicates'] ),
	'all_link_is_spec'      => ( false !== strpos( $home_slider['all_link'], '/specyalisty' ) ),
	'routes'                => $route_results,
	'templates_generic'     => array_reduce(
		$child_rows,
		static function ( $ok, $row ) {
			return $ok && ( 'page-templates/generic.php' === $row['template'] );
		},
		true
	),
);

file_put_contents( $evidence . '/e34-validation.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

$fail_routes = array_filter( $route_results, static function ( $r ) { return 'FAIL' === $r['result']; } );
$fail_links  = array_filter( $link_checks, static function ( $r ) { return 'FAIL' === $r['result']; } );

echo 'VALIDATE children=' . count( $child_rows ) . ' cards=' . count( $cards ) . ' home_cards=' . $home_slider['cards']
	. ' count_ok=' . ( $card_count_ok ? 'Y' : 'N' )
	. ' links_children=' . ( $links_to_children ? 'Y' : 'N' )
	. ' dupes=' . count( $home_slider['duplicates'] )
	. ' route_fails=' . count( $fail_routes )
	. ' link_fails=' . count( $fail_links )
	. PHP_EOL;
