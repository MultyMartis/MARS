<?php
/**
 * Home page ACF read helpers — V9-06D7-B source integration.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Front page post ID for ACF context.
 *
 * @return int
 */
function shpigovsky_get_front_page_id() {
	$page_id = (int) get_option( 'page_on_front' );

	if ( $page_id > 0 ) {
		return $page_id;
	}

	if ( is_singular( 'page' ) ) {
		return (int) get_queried_object_id();
	}

	return 0;
}

/**
 * Read a scalar home ACF field safely.
 *
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_home_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return '';
	}

	$value = get_field( $field_name, $page_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Read a boolean home ACF field safely.
 *
 * @param string $field_name Field name.
 * @param bool   $default    Default when meta/field is unset.
 * @return bool
 */
function shpigovsky_get_home_bool( $field_name, $default = false ) {
	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return (bool) $default;
	}

	if ( ! metadata_exists( 'post', $page_id, $field_name ) ) {
		return (bool) $default;
	}

	if ( function_exists( 'get_field' ) ) {
		return (bool) get_field( $field_name, $page_id );
	}

	return (bool) get_post_meta( $page_id, $field_name, true );
}

/**
 * Whether a Home repeater/list toggle is enabled (default true).
 *
 * @param string $field_name Enabled field name.
 * @return bool
 */
function shpigovsky_home_list_enabled( $field_name ) {
	return shpigovsky_get_home_bool( $field_name, true );
}

/**
 * Filter repeater rows by item_enabled (missing key = enabled).
 *
 * @param array<int, array<string, mixed>> $rows Rows.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_home_filter_enabled_rows( $rows ) {
	$out = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		if ( array_key_exists( 'item_enabled', $row ) && ! (bool) $row['item_enabled'] ) {
			continue;
		}

		$out[] = $row;
	}

	return $out;
}

/**
 * Resolve Home ACF image or theme asset fallback.
 *
 * @param string $field_name ACF image field.
 * @param string $asset_rel  Theme asset relative path under assets/.
 * @param string $fallback_alt Alt text.
 * @param int    $width Fallback width.
 * @param int    $height Fallback height.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_home_image_or_asset( $field_name, $asset_rel, $fallback_alt = '', $width = 0, $height = 0 ) {
	$page_id = shpigovsky_get_front_page_id();
	$image   = ( $page_id > 0 && function_exists( 'get_field' ) ) ? get_field( $field_name, $page_id ) : null;
	$url     = shpigovsky_acf_image_url( $image );
	$alt     = shpigovsky_acf_image_alt( $image );

	if ( '' !== $url ) {
		$w = is_array( $image ) && ! empty( $image['width'] ) ? (int) $image['width'] : $width;
		$h = is_array( $image ) && ! empty( $image['height'] ) ? (int) $image['height'] : $height;

		return array(
			'url'    => $url,
			'alt'    => '' !== $alt ? $alt : $fallback_alt,
			'width'  => $w,
			'height' => $h,
		);
	}

	return array(
		'url'    => shpigovsky_asset_uri( $asset_rel ),
		'alt'    => $fallback_alt,
		'width'  => $width,
		'height' => $height,
	);
}

/**
 * Split textarea lines into list items.
 *
 * @param string $text Multiline text.
 * @return string[]
 */
function shpigovsky_home_lines_to_items( $text ) {
	$parts = preg_split( "/\r\n|\n|\r/", (string) $text );

	if ( ! is_array( $parts ) ) {
		return array();
	}

	$out = array();

	foreach ( $parts as $part ) {
		$part = trim( (string) $part );
		if ( '' !== $part ) {
			$out[] = $part;
		}
	}

	return $out;
}

/**
 * Resolve Home videos from ACF Media Library or theme fallbacks.
 *
 * @return array<int, array{title:string,video_url:string,poster_url:string,width:int,height:int}>
 */
function shpigovsky_get_home_videos_items() {
	if ( ! shpigovsky_home_list_enabled( 'home_videos_items_enabled' ) ) {
		return array();
	}

	$rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback( 'home_videos_items', array() )
	);

	$out = array();

	foreach ( $rows as $row ) {
		$title  = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$file   = isset( $row['video_file'] ) ? $row['video_file'] : null;
		$poster = isset( $row['poster'] ) ? $row['poster'] : null;
		$vurl   = '';

		if ( is_array( $file ) && ! empty( $file['url'] ) ) {
			$vurl = (string) $file['url'];
		} elseif ( is_numeric( $file ) ) {
			$vurl = (string) wp_get_attachment_url( (int) $file );
		}

		$purl = shpigovsky_acf_image_url( $poster );
		$w    = is_array( $poster ) && ! empty( $poster['width'] ) ? (int) $poster['width'] : 1280;
		$h    = is_array( $poster ) && ! empty( $poster['height'] ) ? (int) $poster['height'] : 720;

		if ( '' === $vurl ) {
			continue;
		}

		$out[] = array(
			'title'      => $title,
			'video_url'  => $vurl,
			'poster_url' => $purl,
			'width'      => $w,
			'height'     => $h,
		);
	}

	if ( ! empty( $out ) ) {
		return $out;
	}

	$fallback = shpigovsky_home_videos_fallback_rows();
	$mapped   = array();

	foreach ( $fallback as $row ) {
		if ( empty( $row['item_enabled'] ) ) {
			continue;
		}
		$mapped[] = array(
			'title'      => (string) $row['title'],
			'video_url'  => (string) $row['video_url'],
			'poster_url' => (string) $row['poster_url'],
			'width'      => (int) $row['width'],
			'height'     => (int) $row['height'],
		);
	}

	return $mapped;
}

/**
 * Read a bounded home repeater safely.
 *
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_home_repeater( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return array();
	}

	$rows = get_field( $field_name, $page_id );

	if ( ! is_array( $rows ) ) {
		return array();
	}

	$normalized = array();

	foreach ( $rows as $row ) {
		if ( is_array( $row ) ) {
			$normalized[] = $row;
		}
	}

	return $normalized;
}

/**
 * Static V9 home hero image fallback when ACF image is not seeded.
 *
 * D9-C: theme asset only — no DB/media upload required.
 *
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_home_hero_image_fallback() {
	return shpigovsky_get_hero_theme_fallback( 'home' );
}

/**
 * Resolve ACF image array to URL.
 *
 * @param mixed $image Image field value.
 * @param string $size Image size slug.
 * @return string
 */
function shpigovsky_acf_image_url( $image, $size = 'full' ) {
	if ( ! is_array( $image ) ) {
		return '';
	}

	if ( ! empty( $image['sizes'][ $size ] ) ) {
		return (string) $image['sizes'][ $size ];
	}

	if ( ! empty( $image['url'] ) ) {
		return (string) $image['url'];
	}

	return '';
}

/**
 * Resolve ACF image alt text.
 *
 * @param mixed $image Image field value.
 * @return string
 */
function shpigovsky_acf_image_alt( $image ) {
	if ( ! is_array( $image ) ) {
		return '';
	}

	if ( ! empty( $image['alt'] ) ) {
		return trim( (string) $image['alt'] );
	}

	return '';
}

/**
 * Ordered published child services for a parent.
 *
 * @param int $parent_id Parent service ID.
 * @param int $limit     Max posts.
 * @return WP_Post[]
 */
function shpigovsky_get_published_service_children( $parent_id, $limit = 40 ) {
	$parent_id = (int) $parent_id;

	if ( ! post_type_exists( 'service' ) || $parent_id < 0 ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $parent_id,
			'posts_per_page' => (int) $limit,
			'orderby'        => array(
				'menu_order' => 'ASC',
				'title'      => 'ASC',
			),
			'no_found_rows'  => true,
		)
	);

	return is_array( $children ) ? $children : array();
}

/**
 * Build one accordion link item from a service post.
 *
 * @param WP_Post $service Service post.
 * @return array{title:string,url:string,children:array<int, array{title:string,url:string}>}|null
 */
function shpigovsky_build_home_accordion_item( $service ) {
	if ( ! $service instanceof WP_Post ) {
		return null;
	}

	$title = get_the_title( $service );
	$url   = get_permalink( $service );
	$title = is_string( $title ) ? trim( $title ) : '';
	$url   = is_string( $url ) ? trim( $url ) : '';

	if ( '' === $title || '' === $url ) {
		return null;
	}

	$nested   = array();
	$children = shpigovsky_get_published_service_children( (int) $service->ID, 30 );

	foreach ( $children as $child ) {
		if ( ! $child instanceof WP_Post ) {
			continue;
		}

		$child_title = get_the_title( $child );
		$child_url   = get_permalink( $child );
		$child_title = is_string( $child_title ) ? trim( $child_title ) : '';
		$child_url   = is_string( $child_url ) ? trim( $child_url ) : '';

		if ( '' === $child_title || '' === $child_url ) {
			continue;
		}

		$nested[] = array(
			'title' => $child_title,
			'url'   => $child_url,
		);
	}

	return array(
		'title'    => $title,
		'url'      => $url,
		'children' => $nested,
	);
}

/**
 * Build service accordion groups from the service CPT hierarchy.
 *
 * Model: root published services = accordion groups; depth-1 children = primary
 * links; depth-2 grandchildren nest under their parent when present.
 *
 * @return array<int, array{title:string,items:array<int, array{title:string,url:string,children:array}>}>
 */
function shpigovsky_get_home_service_accordion_groups() {
	if ( ! post_type_exists( 'service' ) ) {
		return array();
	}

	$parents = shpigovsky_get_published_service_children( 0, 12 );

	if ( empty( $parents ) ) {
		return array();
	}

	$groups = array();

	foreach ( $parents as $parent ) {
		if ( ! $parent instanceof WP_Post ) {
			continue;
		}

		$items    = array();
		$children = shpigovsky_get_published_service_children( (int) $parent->ID, 40 );

		foreach ( $children as $child ) {
			$item = shpigovsky_build_home_accordion_item( $child );
			if ( null !== $item ) {
				$items[] = $item;
			}
		}

		if ( empty( $items ) ) {
			continue;
		}

		$groups[] = array(
			'title' => get_the_title( $parent ),
			'items' => $items,
		);
	}

	return $groups;
}

/**
 * Whether a published service is eligible for the Home gallery slider by depth.
 *
 * Conservative rule (V9-06E32): depth === 1 only
 * (e.g. «Депрессия», «Поведенческие зависимости»).
 * Root hubs (depth 0) and deep leaf/subservices (depth >= 2) are excluded
 * unless an operator later expands the rule.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_is_home_gallery_depth_eligible( $post_id ) {
	$post_id = (int) $post_id;
	$post    = get_post( $post_id );

	if ( ! $post instanceof WP_Post || 'service' !== $post->post_type || 'publish' !== $post->post_status ) {
		return false;
	}

	$parent_id = (int) $post->post_parent;

	if ( $parent_id <= 0 ) {
		return false;
	}

	$parent = get_post( $parent_id );

	if ( ! $parent instanceof WP_Post || 'service' !== $parent->post_type ) {
		return false;
	}

	// Depth 1: parent is a root hub.
	return 0 === (int) $parent->post_parent;
}

/**
 * Whether a service should appear in the Home gallery slider.
 * Separate from /uslugi/ service_show_in_slider (E30).
 * Default true for depth-eligible services when meta is unset.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_show_on_home_gallery( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 || ! shpigovsky_service_is_home_gallery_depth_eligible( $post_id ) ) {
		return false;
	}

	if ( metadata_exists( 'post', $post_id, 'service_show_on_home_gallery' ) ) {
		return (bool) (int) get_post_meta( $post_id, 'service_show_on_home_gallery', true );
	}

	return true;
}

/**
 * Build one Home gallery slide from a service post.
 *
 * @param WP_Post $child Service post.
 * @return array{title:string,url:string,image_url:string,width:int,height:int,alt:string,image_source:string,id:int}|null
 */
function shpigovsky_home_gallery_slide_from_service( $child ) {
	if ( ! $child instanceof WP_Post ) {
		return null;
	}

	$image = shpigovsky_get_service_image_or_placeholder( (int) $child->ID );
	$title = get_the_title( $child );
	$url   = get_permalink( $child );
	$title = is_string( $title ) ? trim( $title ) : '';
	$url   = is_string( $url ) ? trim( $url ) : '';

	if ( '' === $title || '' === $url || empty( $image['url'] ) ) {
		return null;
	}

	return array(
		'id'           => (int) $child->ID,
		'title'        => $title,
		'url'          => $url,
		'image_url'    => (string) $image['url'],
		'width'        => (int) $image['width'],
		'height'       => (int) $image['height'],
		'alt'          => (string) $image['alt'],
		'image_source' => (string) $image['source'],
	);
}

/**
 * Collect all eligible Home gallery service slides (depth-1 + flag).
 *
 * @return array<int, array{title:string,url:string,image_url:string,width:int,height:int,alt:string,image_source:string,id:int}>
 */
function shpigovsky_get_home_gallery_eligible_slides() {
	if ( ! post_type_exists( 'service' ) ) {
		return array();
	}

	$roots  = shpigovsky_get_published_service_children( 0, 12 );
	$slides = array();

	foreach ( $roots as $root ) {
		if ( ! $root instanceof WP_Post ) {
			continue;
		}

		$children = shpigovsky_get_published_service_children( (int) $root->ID, 40 );

		foreach ( $children as $child ) {
			if ( ! $child instanceof WP_Post ) {
				continue;
			}

			if ( ! shpigovsky_service_show_on_home_gallery( (int) $child->ID ) ) {
				continue;
			}

			$slide = shpigovsky_home_gallery_slide_from_service( $child );

			if ( null !== $slide ) {
				$slides[] = $slide;
			}
		}
	}

	return $slides;
}

/**
 * Home gallery display mode from ACF (default random).
 *
 * @return string all|random|selected
 */
function shpigovsky_get_home_gallery_display_mode() {
	$mode = strtolower( trim( shpigovsky_get_home_field( 'home_gallery_display_mode' ) ) );

	if ( in_array( $mode, array( 'all', 'random', 'selected' ), true ) ) {
		return $mode;
	}

	return 'random';
}

/**
 * Random count for Home gallery (default 12).
 *
 * @return int
 */
function shpigovsky_get_home_gallery_random_count() {
	$raw = shpigovsky_get_home_field( 'home_gallery_random_count' );
	$n   = '' !== $raw ? (int) $raw : 12;

	return max( 1, min( 48, $n > 0 ? $n : 12 ) );
}

/**
 * Build Home gallery slides from eligible service CPT posts.
 *
 * V9-06E40: respects home_gallery_display_mode / random_count / selected_services.
 * Eligibility (E32/E33) still requires published depth-1 + service_show_on_home_gallery.
 *
 * @return array<int, array{title:string,url:string,image_url:string,width:int,height:int,alt:string,image_source:string,id:int}>
 */
function shpigovsky_get_home_gallery_service_slides() {
	$eligible = shpigovsky_get_home_gallery_eligible_slides();

	if ( empty( $eligible ) ) {
		return array();
	}

	$mode = shpigovsky_get_home_gallery_display_mode();

	if ( 'all' === $mode ) {
		return $eligible;
	}

	if ( 'selected' === $mode ) {
		$page_id = shpigovsky_get_front_page_id();
		$selected = ( $page_id > 0 && function_exists( 'get_field' ) )
			? get_field( 'home_gallery_selected_services', $page_id )
			: array();

		$ids = array();

		if ( is_array( $selected ) ) {
			foreach ( $selected as $item ) {
				if ( is_numeric( $item ) ) {
					$ids[] = (int) $item;
				} elseif ( $item instanceof WP_Post ) {
					$ids[] = (int) $item->ID;
				} elseif ( is_array( $item ) && ! empty( $item['ID'] ) ) {
					$ids[] = (int) $item['ID'];
				}
			}
		}

		$by_id = array();
		foreach ( $eligible as $slide ) {
			$by_id[ (int) $slide['id'] ] = $slide;
		}

		$ordered = array();
		foreach ( $ids as $id ) {
			if ( isset( $by_id[ $id ] ) ) {
				$ordered[] = $by_id[ $id ];
			}
		}

		if ( ! empty( $ordered ) ) {
			return $ordered;
		}

		// Empty selected list → fallback to random N.
		$mode = 'random';
	}

	// random (default) — shuffle per request (local prototype acceptable).
	$count = shpigovsky_get_home_gallery_random_count();
	$pool  = $eligible;

	if ( count( $pool ) <= $count ) {
		return $pool;
	}

	shuffle( $pool );

	return array_slice( $pool, 0, $count );
}

/**
 * Home articles teaser cards from published blog posts.
 *
 * V9-06E35: replaces hardcoded HTML mock in articles-teaser.php.
 *
 * @param int $limit Max cards (default 6).
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_home_articles_cards( $limit = 6 ) {
	$limit = max( 1, (int) $limit );
	$cards = array();

	$query = new WP_Query(
		array(
			'post_type'           => 'post',
			'post_status'         => 'publish',
			'posts_per_page'      => $limit,
			'ignore_sticky_posts' => true,
			'orderby'             => 'date',
			'order'               => 'DESC',
			'no_found_rows'       => true,
		)
	);

	if ( ! $query->have_posts() ) {
		return $cards;
	}

	while ( $query->have_posts() ) {
		$query->the_post();
		$post_id = (int) get_the_ID();

		if ( ! function_exists( 'shpigovsky_build_blog_archive_card_args' ) ) {
			continue;
		}

		$card = shpigovsky_build_blog_archive_card_args( $post_id );

		if ( empty( $card ) || empty( $card['url'] ) || empty( $card['title'] ) ) {
			continue;
		}

		$cards[] = $card;
	}

	wp_reset_postdata();

	return $cards;
}
