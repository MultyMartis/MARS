<?php
/**
 * V9-06E38: Home ACF cleanup (strip imsc42, retire gallery/reviews fields) + validate.
 *
 * @package FP0002
 */

define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e38-home-admin-parity-uslugi-heading-links';
$report_ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$bak_exports = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e38-home-admin-parity-uslugi-links-before-20260713-190141/exports';
$runtime_acf = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json';
$source_acf  = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json';

$out = array(
	'home_id'           => (int) get_option( 'page_on_front' ),
	'imsc42_stripped'   => array(),
	'fields_trashed'    => array(),
	'json_export'       => array(),
	'classification'    => array(),
	'uslugi_links'      => array(),
	'validation'        => array(),
	'db_writes'         => 0,
);

$home_id = $out['home_id'] > 0 ? $out['home_id'] : 4;

/**
 * Strip leading imsc42 test marker variants.
 *
 * @param string $value Raw meta value.
 * @return string|null Cleaned value or null if unchanged.
 */
function e38_strip_imsc42( $value ) {
	if ( ! is_string( $value ) || '' === $value ) {
		return null;
	}
	$cleaned = preg_replace( '/^imsc42(?:\s*[\.\:\—\-–]?\s*|\s+)/u', '', $value, 1 );
	if ( null === $cleaned ) {
		return null;
	}
	// Exact marker-only value → empty string.
	if ( preg_match( '/^imsc42$/u', trim( $value ) ) ) {
		$cleaned = '';
	}
	if ( $cleaned === $value ) {
		return null;
	}
	return $cleaned;
}

// --- Export Home group JSON from FieldGroups PHP ---
$home_group = null;
if ( class_exists( '\\Shpigovsky\\Core\\Fields\\FieldGroups' ) ) {
	foreach ( \Shpigovsky\Core\Fields\FieldGroups::get_field_groups() as $group ) {
		if ( ( $group['key'] ?? '' ) === 'group_fp02_page_home' ) {
			$home_group = $group;
			break;
		}
	}
}

if ( is_array( $home_group ) ) {
	$json = wp_json_encode( $home_group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
	foreach ( array( $runtime_acf, $source_acf, $bak_exports ) as $dir ) {
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}
		$path = rtrim( $dir, '/\\' ) . '/group_fp02_page_home.json';
		file_put_contents( $path, $json . "\n" );
		$out['json_export'][] = $path;
	}
}

// --- Trash dead ACF field posts (gallery + reviews teaser + their children) ---
$retire_needles = array(
	'home_gallery_media',
	'home_gallery_item',
	'field_fp02_home_gallery',
	'home_reviews_teaser',
	'field_fp02_home_reviews_teaser',
);

$field_posts = get_posts(
	array(
		'post_type'      => 'acf-field',
		'post_status'    => 'any',
		'posts_per_page' => -1,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);

foreach ( $field_posts as $fp ) {
	$name = (string) $fp->post_excerpt;
	$key  = (string) $fp->post_name;
	$hit  = false;
	foreach ( $retire_needles as $needle ) {
		if ( false !== strpos( $name, $needle ) || false !== strpos( $key, $needle ) ) {
			$hit = true;
			break;
		}
	}
	if ( ! $hit ) {
		continue;
	}
	if ( 'trash' === $fp->post_status ) {
		$out['fields_trashed'][] = array(
			'ID'     => (int) $fp->ID,
			'name'   => $name,
			'key'    => $key,
			'action' => 'already_trash',
		);
		continue;
	}
	$ok = (bool) wp_trash_post( $fp->ID );
	if ( $ok ) {
		++$out['db_writes'];
	}
	$out['fields_trashed'][] = array(
		'ID'     => (int) $fp->ID,
		'name'   => $name,
		'key'    => $key,
		'action' => 'trash',
		'ok'     => $ok,
	);
}

if ( function_exists( 'wp_cache_flush' ) ) {
	wp_cache_flush();
}

// --- Strip imsc42 from Home postmeta ---
global $wpdb;
$rows = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT meta_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id = %d AND meta_value LIKE %s",
		$home_id,
		'imsc42%'
	),
	ARRAY_A
);

foreach ( (array) $rows as $row ) {
	$key   = (string) $row['meta_key'];
	$value = (string) $row['meta_value'];
	if ( 0 === strpos( $key, '_' ) ) {
		continue;
	}
	$cleaned = e38_strip_imsc42( $value );
	if ( null === $cleaned ) {
		continue;
	}
	$updated = $wpdb->update(
		$wpdb->postmeta,
		array( 'meta_value' => $cleaned ),
		array( 'meta_id' => (int) $row['meta_id'] ),
		array( '%s' ),
		array( '%d' )
	);
	if ( false !== $updated ) {
		++$out['db_writes'];
		$out['imsc42_stripped'][] = array(
			'meta_key' => $key,
			'before'   => mb_substr( $value, 0, 80 ),
			'after'    => mb_substr( $cleaned, 0, 80 ),
		);
	}
}

clean_post_cache( $home_id );

// --- Classification ---
$field_defs = array(
	array( 'hero_media', 'Hero image', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'keep', 'hero.php / hero-helpers' ),
	array( 'hero_cta_label', 'Текст кнопки в hero-блоке', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'hero CTA' ),
	array( 'home_hero_slides', 'Hero slides', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'hero.php' ),
	array( 'home_advantages', 'Advantages / trust', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'feature-grid.php' ),
	array( 'home_intro_bands', 'Intro bands', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'recovery-intro.php cards' ),
	array( 'home_gallery_media', 'Gallery / media bands (legacy)', 'group_fp02_page_home', 'DEAD_LEGACY', 'removed_from_admin', 'gallery.php uses service CPT' ),
	array( 'home_gallery_source_notice', 'Галерея на главной', 'group_fp02_page_home', 'AUTOMATED_NO_ADMIN_FIELD_NEEDED', 'message_notice_added', 'informational only' ),
	array( 'home_reviews_teaser', 'Reviews teaser', 'group_fp02_page_home', 'DEAD_LEGACY', 'removed_from_admin', 'reviews from options; theme already hid UI' ),
	array( 'home_blog_teaser_enabled', 'Blog teaser enabled', 'group_fp02_page_home', 'DEAD_LEGACY', 'kept_with_instruction', 'no theme read; articles from WP posts' ),
	array( 'home_faq_items', 'FAQ', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'faq.php' ),
	array( 'home_cta_title', 'CTA title', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'reusable-blocks-helpers' ),
	array( 'home_cta_text', 'CTA text', 'group_fp02_page_home', 'LIVE_FRONTEND_EDITABLE', 'strip_imsc42_keep', 'reusable-blocks-helpers' ),
	array( 'home_faq_heading', 'Заголовок FAQ', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'faq.php; not in FieldGroups.php' ),
	array( 'home_recovery_intro_heading', 'Recovery intro — заголовок', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'recovery-intro.php; not in FieldGroups.php' ),
	array( 'home_recovery_intro_lead_1', 'Recovery intro — абзац 1', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'recovery-intro.php' ),
	array( 'home_recovery_intro_lead_2', 'Recovery intro — абзац 2', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'recovery-intro.php' ),
	array( 'home_specialists_heading', 'Specialists — заголовок', 'stale_db_only', 'LIVE_BUT_SHOULD_BE_AUTOMATED', 'leave_meta', 'fallback after specialists options block' ),
	array( 'home_comfort_heading', 'Comfort — заголовок', 'stale_db_only', 'UNCLEAR_REVIEW', 'leave_meta', 'comfort helpers; may also use block options' ),
	array( 'home_comfort_lead', 'Comfort — лид', 'stale_db_only', 'UNCLEAR_REVIEW', 'leave_meta', 'comfort helpers' ),
	array( 'home_reviews_heading', 'Reviews — заголовок', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'reviews-helpers; not in FieldGroups.php' ),
	array( 'home_articles_heading', 'Articles — заголовок', 'stale_db_only', 'LIVE_FRONTEND_EDITABLE', 'leave_meta_unclear_admin', 'articles-teaser.php; cards from WP posts' ),
	array( 'home_service_nav_items', 'Service navigation / accordion', 'retired_e32', 'AUTOMATED_NO_ADMIN_FIELD_NEEDED', 'already_trashed', 'accordion from service CPT' ),
);

$home_html = '';
$home_resp = wp_remote_get( home_url( '/' ), array( 'timeout' => 30 ) );
if ( ! is_wp_error( $home_resp ) ) {
	$home_html = (string) wp_remote_retrieve_body( $home_resp );
	$out['validation']['home_http'] = (int) wp_remote_retrieve_response_code( $home_resp );
}
$out['validation']['home_imsc42_count'] = substr_count( $home_html, 'imsc42' );

$csv_rows   = array();
$csv_rows[] = 'field_name,label,group,current_value_preview,imsc42_detected,frontend_match,render_source,classification,action';

foreach ( $field_defs as $def ) {
	list( $name, $label, $group, $class, $action, $render ) = $def;
	$raw = get_post_meta( $home_id, $name, true );
	if ( is_array( $raw ) ) {
		$preview = wp_json_encode( $raw, JSON_UNESCAPED_UNICODE );
	} else {
		$preview = (string) $raw;
	}
	$preview_short = str_replace( array( "\r", "\n", ',' ), array( ' ', ' ', ';' ), mb_substr( $preview, 0, 100 ) );
	$imsc          = ( is_string( $raw ) && 0 === strpos( $raw, 'imsc42' ) ) || false !== strpos( $preview, 'imsc42' ) ? 'yes' : 'no';
	// Heuristic frontend match for scalar strings.
	$fe_match = 'n/a';
	if ( is_string( $raw ) && '' !== $raw && 'imsc42' !== trim( $raw ) ) {
		$probe    = e38_strip_imsc42( $raw );
		$probe    = null === $probe ? $raw : $probe;
		$fe_match = ( '' !== $probe && false !== mb_strpos( $home_html, wp_strip_all_tags( $probe ) ) ) ? 'yes' : 'no';
	}
	$csv_rows[] = implode(
		',',
		array(
			$name,
			'"' . str_replace( '"', '""', $label ) . '"',
			$group,
			'"' . str_replace( '"', '""', $preview_short ) . '"',
			$imsc,
			$fe_match,
			'"' . str_replace( '"', '""', $render ) . '"',
			$class,
			$action,
		)
	);
	$out['classification'][] = array(
		'field_name'     => $name,
		'label'          => $label,
		'group'          => $group,
		'classification' => $class,
		'action'         => $action,
		'imsc42'         => $imsc,
	);
}

$csv_path = $report_ev . '/v9-06e38-home-acf-field-classification.csv';
file_put_contents( $csv_path, implode( "\n", $csv_rows ) . "\n" );
$out['classification_csv'] = $csv_path;

// --- /uslugi/ link validation ---
$uslugi_resp = wp_remote_get( home_url( '/uslugi/' ), array( 'timeout' => 30 ) );
$uslugi_html = is_wp_error( $uslugi_resp ) ? '' : (string) wp_remote_retrieve_body( $uslugi_resp );
$out['validation']['uslugi_http'] = is_wp_error( $uslugi_resp ) ? 0 : (int) wp_remote_retrieve_response_code( $uslugi_resp );

if ( function_exists( 'shpigovsky_get_services_hub_groups' ) ) {
	foreach ( shpigovsky_get_services_hub_groups() as $g ) {
		$url = isset( $g['url'] ) ? (string) $g['url'] : '';
		$link_http = 0;
		if ( '' !== $url ) {
			$r = wp_remote_head( $url, array( 'timeout' => 15, 'redirection' => 3 ) );
			if ( is_wp_error( $r ) ) {
				$r = wp_remote_get( $url, array( 'timeout' => 15, 'redirection' => 3 ) );
			}
			$link_http = is_wp_error( $r ) ? 0 : (int) wp_remote_retrieve_response_code( $r );
		}
		$marker_linked  = '' !== $url && false !== strpos( $uslugi_html, 'services-category-section-v2__marker-link' ) && false !== strpos( $uslugi_html, esc_url( $url ) );
		$heading_linked = '' !== $url && false !== strpos( $uslugi_html, 'services-category-section-v2__heading-link' );
		$out['uslugi_links'][] = array(
			'title'          => $g['title'] ?? '',
			'slug'           => $g['slug'] ?? '',
			'url'            => $url,
			'http'           => $link_http,
			'marker_in_html' => $marker_linked,
			'heading_class'  => $heading_linked,
			'icon'           => $g['icon'] ?? '',
		);
	}
}

$out['validation']['marker_link_count']  = preg_match_all( '/services-category-section-v2__marker-link/', $uslugi_html );
$out['validation']['heading_link_count'] = preg_match_all( '/services-category-section-v2__heading-link/', $uslugi_html );
$out['validation']['gallery_field']      = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_home_gallery_media' ) : null;
$out['validation']['reviews_teaser_field'] = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_home_reviews_teaser' ) : null;
$out['validation']['gallery_notice']     = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_home_gallery_source_notice' ) : null;
$out['validation']['home_gallery_slides'] = function_exists( 'shpigovsky_get_home_gallery_service_slides' ) ? count( shpigovsky_get_home_gallery_service_slides() ) : 0;
$out['validation']['accordion_groups']   = function_exists( 'shpigovsky_get_home_service_accordion_groups' ) ? count( shpigovsky_get_home_service_accordion_groups() ) : 0;

// Regression routes
$routes = array( '/', '/uslugi/', '/blog/', '/specyalisty/', '/o-centre/', '/kontakty/' );
foreach ( $routes as $route ) {
	$r = wp_remote_get( home_url( $route ), array( 'timeout' => 30 ) );
	$out['validation']['routes'][ $route ] = is_wp_error( $r ) ? array( 'http' => 0, 'error' => $r->get_error_message() ) : array(
		'http'  => (int) wp_remote_retrieve_response_code( $r ),
		'fatal' => false !== stripos( (string) wp_remote_retrieve_body( $r ), 'Fatal error' ),
	);
}

file_put_contents( $out_dir . '/e38-result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo "E38_DONE db_writes={$out['db_writes']} imsc42_left={$out['validation']['home_imsc42_count']} marker_links={$out['validation']['marker_link_count']} heading_links={$out['validation']['heading_link_count']}\n";
