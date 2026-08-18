<?php
/**
 * Glossary CPT registration and pre-publication exposure controls.
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'ISEO_GLOSSARY_PUBLIC_EXPOSURE' ) ) {
	// Controlled public launch: eligible published glossary articles + archive.
	define( 'ISEO_GLOSSARY_PUBLIC_EXPOSURE', true );
}

/**
 * Whether glossary archive/singles are publicly exposable.
 *
 * @return bool
 */
function iseo_glossary_is_publicly_exposed() {
	return (bool) apply_filters( 'iseo_glossary_is_publicly_exposed', ISEO_GLOSSARY_PUBLIC_EXPOSURE );
}

/**
 * Register glossary custom post type.
 */
function iseo_register_glossary_type_init() {
	$labels = array(
		'name'               => 'Глоссарий',
		'singular_name'      => 'Термин',
		'menu_name'          => 'Глоссарий',
		'name_admin_bar'     => 'Термин',
		'add_new'            => 'Добавить термин',
		'add_new_item'       => 'Добавить термин',
		'edit_item'          => 'Редактировать термин',
		'new_item'           => 'Новый термин',
		'view_item'          => 'Просмотреть термин',
		'view_items'         => 'Просмотреть термины',
		'all_items'          => 'Все термины',
		'search_items'       => 'Искать термины',
		'not_found'          => 'Термины не найдены.',
		'not_found_in_trash' => 'В корзине терминов нет.',
		'archives'           => 'Глоссарий',
	);

	$args = array(
		'labels'              => $labels,
		'public'              => true,
		'publicly_queryable'  => true,
		'show_ui'             => true,
		'show_in_menu'        => true,
		'show_in_nav_menus'   => false,
		'show_in_admin_bar'   => true,
		'exclude_from_search' => true,
		'has_archive'         => 'glossary',
		'menu_position'       => 6,
		'menu_icon'           => 'dashicons-book-alt',
		'capability_type'     => 'post',
		'map_meta_cap'        => true,
		'hierarchical'        => false,
		'supports'            => array( 'title', 'editor', 'excerpt', 'revisions', 'custom-fields' ),
		'rewrite'             => array(
			'slug'       => 'glossary',
			'with_front' => false,
		),
		// Admin REST only when required by core/ACF; not for public WPilot onboarding.
		'show_in_rest'        => true,
		'can_export'          => true,
		'delete_with_user'    => false,
	);

	register_post_type( 'glossary', $args );
}
add_action( 'init', 'iseo_register_glossary_type_init' );

/**
 * Flush rewrite rules once after glossary CPT deploy.
 */
function iseo_glossary_maybe_flush_rewrite_rules() {
	$version = '1';
	if ( get_option( 'iseo_glossary_rewrite_version' ) === $version ) {
		return;
	}
	flush_rewrite_rules( false );
	update_option( 'iseo_glossary_rewrite_version', $version, false );
}
add_action( 'init', 'iseo_glossary_maybe_flush_rewrite_rules', 20 );

/**
 * Load all glossary terms on one alphabetical archive page.
 *
 * @param WP_Query $query Query.
 */
function iseo_glossary_archive_query( $query ) {
	if ( is_admin() || ! $query->is_main_query() ) {
		return;
	}
	if ( ! $query->is_post_type_archive( 'glossary' ) ) {
		return;
	}

	$query->set( 'posts_per_page', -1 );
	$query->set( 'orderby', 'title' );
	$query->set( 'order', 'ASC' );
	// Status list mirrors iseo_glossary_archive_post_statuses(); archive template
	// loads terms via iseo_glossary_get_archive_posts() because the main query
	// can report found_posts without hydrating $wp_query->posts for drafts.
	$query->set( 'post_status', iseo_glossary_archive_post_statuses() );
}
add_action( 'pre_get_posts', 'iseo_glossary_archive_query' );

/**
 * Block anonymous front-end exposure until publication gate opens.
 */
function iseo_glossary_block_public_exposure() {
	if ( is_admin() || iseo_glossary_is_publicly_exposed() ) {
		return;
	}
	if ( ! is_post_type_archive( 'glossary' ) && ! is_singular( 'glossary' ) ) {
		return;
	}
	if ( current_user_can( 'edit_posts' ) ) {
		return;
	}
	global $wp_query;
	$wp_query->set_404();
	status_header( 404 );
	nocache_headers();
}
add_action( 'template_redirect', 'iseo_glossary_block_public_exposure', 1 );

/**
 * Force noindex while glossary is not publicly launched.
 *
 * @param array $robots Robots directives.
 * @return array
 */
function iseo_glossary_robots( $robots ) {
	if ( ! is_post_type_archive( 'glossary' ) && ! is_singular( 'glossary' ) ) {
		return $robots;
	}
	if ( iseo_glossary_is_publicly_exposed() ) {
		if ( is_post_type_archive( 'glossary' ) ) {
			return $robots;
		}
		if ( is_singular( 'glossary' ) && 'publish' === get_post_status() ) {
			return $robots;
		}
	}
	$robots['noindex']  = true;
	$robots['nofollow'] = true;
	return $robots;
}
add_filter( 'wp_robots', 'iseo_glossary_robots', 20 );

/**
 * Keep glossary out of Yoast sitemap until public exposure is enabled.
 *
 * @param bool   $excluded  Whether excluded.
 * @param string $post_type Post type.
 * @return bool
 */
function iseo_glossary_exclude_from_yoast_sitemap( $excluded, $post_type ) {
	if ( 'glossary' === $post_type && ! iseo_glossary_is_publicly_exposed() ) {
		return true;
	}
	return $excluded;
}
add_filter( 'wpseo_sitemap_exclude_post_type', 'iseo_glossary_exclude_from_yoast_sitemap', 10, 2 );

/**
 * Whether the current request is the public glossary CPT archive (not a term single).
 *
 * @return bool
 */
function iseo_glossary_is_archive_request() {
	return is_post_type_archive( 'glossary' ) && ! is_singular();
}

/**
 * Remove leading archive-prefix semantics from the glossary archive title only.
 *
 * Yoast CPT archive titles currently render as "Архив Глоссарий - INTLSEO Studio".
 * Target is the same separator/sitename convention without the prefix.
 * Does not alter glossary singles, blog, or other archives.
 *
 * @param string $title Title.
 * @return string
 */
function iseo_glossary_strip_archive_title_prefix( $title ) {
	if ( ! iseo_glossary_is_archive_request() ) {
		return $title;
	}
	$title    = (string) $title;
	$stripped = preg_replace( '/^(Архив|Archives)\s+/u', '', $title, 1 );
	if ( ! is_string( $stripped ) || '' === trim( $stripped ) ) {
		return $title;
	}
	return $stripped;
}

add_filter( 'wpseo_title', 'iseo_glossary_strip_archive_title_prefix', 20 );
add_filter( 'wpseo_opengraph_title', 'iseo_glossary_strip_archive_title_prefix', 20 );
add_filter( 'wpseo_twitter_title', 'iseo_glossary_strip_archive_title_prefix', 20 );

/**
 * Keep Yoast CollectionPage/WebPage schema name aligned with the HTML title.
 *
 * @param array $data Schema WebPage data.
 * @return array
 */
function iseo_glossary_schema_webpage_title( $data ) {
	if ( ! iseo_glossary_is_archive_request() || ! is_array( $data ) ) {
		return $data;
	}
	if ( isset( $data['name'] ) ) {
		$data['name'] = iseo_glossary_strip_archive_title_prefix( (string) $data['name'] );
	}
	return $data;
}
add_filter( 'wpseo_schema_webpage', 'iseo_glossary_schema_webpage_title' );

/**
 * Fallback if Yoast is not the title presenter.
 *
 * @param array $parts Title parts.
 * @return array
 */
function iseo_glossary_document_title_parts( $parts ) {
	if ( ! iseo_glossary_is_archive_request() || ! is_array( $parts ) ) {
		return $parts;
	}
	if ( ! empty( $parts['title'] ) ) {
		$parts['title'] = iseo_glossary_strip_archive_title_prefix( (string) $parts['title'] );
	}
	return $parts;
}
add_filter( 'document_title_parts', 'iseo_glossary_document_title_parts', 20 );

/**
 * Body classes aligned with internal content pages.
 *
 * @param array $classes Classes.
 * @return array
 */
function iseo_glossary_body_classes( $classes ) {
	if ( is_post_type_archive( 'glossary' ) || is_singular( 'glossary' ) ) {
		$classes[] = 'overlay_on';
		$classes[] = 'content';
	}
	return $classes;
}
add_filter( 'body_class', 'iseo_glossary_body_classes' );
