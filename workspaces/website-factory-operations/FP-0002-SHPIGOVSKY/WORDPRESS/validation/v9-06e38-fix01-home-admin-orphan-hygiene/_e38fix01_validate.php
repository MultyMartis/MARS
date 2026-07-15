<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out = array();

// Direct local group fields
$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( 'group_fp02_page_home' ) : null;
$names = array();
if ( is_array( $fields ) ) {
	foreach ( $fields as $f ) {
		$names[] = array( 'name' => $f['name'] ?? '', 'label' => $f['label'] ?? '', 'type' => $f['type'] ?? '', 'key' => $f['key'] ?? '' );
	}
}
$out['acf_get_fields_count'] = is_array( $fields ) ? count( $fields ) : 0;
$out['field_names'] = array_map( function( $x ) { return $x['name']; }, $names );
$out['fields_detail'] = $names;

// Groups matching front page #4
$home_id = (int) get_option( 'page_on_front' );
$groups = acf_get_field_groups( array( 'post_id' => $home_id ) );
$out['groups_for_home'] = array();
foreach ( $groups as $g ) {
	$out['groups_for_home'][] = array(
		'key' => $g['key'] ?? '',
		'title' => $g['title'] ?? '',
		'ID' => $g['ID'] ?? null,
		'local' => $g['local'] ?? null,
		'active' => $g['active'] ?? null,
	);
}

// Publish DB home groups
$q = new WP_Query( array( 'post_type' => 'acf-field-group', 'post_status' => 'publish', 'name' => 'group_fp02_page_home', 'posts_per_page' => -1 ) );
$out['publish_db_home_groups'] = array_map( function( $p ) { return (int) $p->ID; }, $q->posts );

// Kept group 639 remaining publish fields
$keep_fields = get_posts( array( 'post_type' => 'acf-field', 'post_status' => 'publish', 'post_parent' => 639, 'posts_per_page' => -1, 'orderby' => 'menu_order', 'order' => 'ASC' ) );
$out['keep_639_publish_fields'] = array_map( function( $p ) { return $p->post_excerpt; }, $keep_fields );

// Simulate save: update_field home_faq_heading then restore
$before = get_field( 'home_faq_heading', $home_id );
$probe = update_field( 'home_faq_heading', $before, $home_id );
$after = get_field( 'home_faq_heading', $home_id );
$out['save_probe'] = array(
	'before' => is_string( $before ) ? mb_substr( $before, 0, 60 ) : $before,
	'update_ok' => (bool) $probe || ( $before === $after ),
	'after_match' => $before === $after,
);

// Frontend key snippets
$home_html = '';
$resp = wp_remote_get( home_url( '/' ), array( 'timeout' => 30 ) );
$code = wp_remote_retrieve_response_code( $resp );
$body = wp_remote_retrieve_body( $resp );
$out['home_http'] = $code;
$out['imsc42'] = substr_count( $body, 'imsc42' );
$out['has_faq_heading'] = false !== mb_strpos( $body, 'Нас часто спрашивают' );
$out['has_articles'] = false !== mb_strpos( $body, 'Статьи' ) || false !== mb_strpos( $body, 'articles' );
$out['has_recovery'] = false !== mb_strpos( $body, 'восстановление' );
$out['has_specialists'] = false !== mb_strpos( $body, 'Специалисты' );
$out['has_gallery_swiper'] = false !== strpos( $body, 'home-gallery' ) || false !== strpos( $body, 'data-home-gallery' );
$out['has_services_accordion'] = false !== strpos( $body, 'home-rehabilitation' ) || false !== strpos( $body, 'services-accordion' ) || false !== strpos( $body, 'rehabilitation-program' );

$routes = array( '/', '/uslugi/', '/blog/', '/specyalisty/', '/o-centre/', '/kontakty/' );
$out['routes'] = array();
foreach ( $routes as $r ) {
	$rr = wp_remote_get( home_url( $r ), array( 'timeout' => 30 ) );
	$out['routes'][ $r ] = wp_remote_retrieve_response_code( $rr );
}

// Operator CSS hash check
$css_src = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/assets/css/v9-style.css';
$css_rt  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/assets/css/v9-style.css';
$out['operator_css'] = array(
	'src' => is_readable( $css_src ) ? hash_file( 'sha256', $css_src ) : null,
	'rt' => is_readable( $css_rt ) ? hash_file( 'sha256', $css_rt ) : null,
);
$out['operator_css']['match'] = $out['operator_css']['src'] && $out['operator_css']['src'] === $out['operator_css']['rt'];

@file_put_contents( 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e38-fix01-home-admin-orphan-hygiene/e38fix01-validate.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
