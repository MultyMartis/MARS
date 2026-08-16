<?php
/**
 * Services Hub page ACF read helpers and Service CPT queries — V9-06D7-C.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Services Hub page post ID for ACF context.
 *
 * @return int
 */
function shpigovsky_get_services_hub_page_id() {
	if ( is_page_template( 'page-templates/services-hub.php' ) ) {
		return (int) get_queried_object_id();
	}

	$pages = get_posts(
		array(
			'post_type'      => 'page',
			'post_status'    => 'publish',
			'meta_key'       => '_wp_page_template',
			'meta_value'     => 'page-templates/services-hub.php',
			'posts_per_page' => 1,
			'no_found_rows'  => true,
			'fields'         => 'ids',
		)
	);

	if ( ! empty( $pages[0] ) ) {
		return (int) $pages[0];
	}

	return 0;
}

/**
 * Whether the current request is the Services hub page.
 *
 * @return bool
 */
function shpigovsky_is_services_hub_page() {
	return is_page_template( 'page-templates/services-hub.php' );
}

/**
 * Read a boolean Services Hub ACF field safely.
 *
 * @param string $field_name Field name.
 * @param bool   $default    Default when meta missing/empty.
 * @return bool
 */
function shpigovsky_get_services_hub_bool( $field_name, $default = false ) {
	$page_id = shpigovsky_get_services_hub_page_id();

	if ( $page_id <= 0 ) {
		return (bool) $default;
	}

	if ( function_exists( 'get_field' ) ) {
		$value = get_field( $field_name, $page_id );
		if ( null === $value || false === $value || '' === $value ) {
			$raw = get_post_meta( $page_id, $field_name, true );
			if ( '' === $raw || null === $raw ) {
				return (bool) $default;
			}
			return (bool) $raw;
		}
		return (bool) $value;
	}

	$raw = get_post_meta( $page_id, $field_name, true );
	if ( '' === $raw || null === $raw ) {
		return (bool) $default;
	}

	return (bool) $raw;
}

/**
 * Whether a Services hub toggle is enabled (default true).
 *
 * @param string $field_name Enabled field name.
 * @return bool
 */
function shpigovsky_services_hub_list_enabled( $field_name ) {
	return shpigovsky_get_services_hub_bool( $field_name, true );
}

/**
 * Read a scalar Services Hub ACF field safely.
 *
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_services_hub_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$page_id = shpigovsky_get_services_hub_page_id();

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
 * Read a bounded Services Hub repeater safely.
 *
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_repeater( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$page_id = shpigovsky_get_services_hub_page_id();

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
 * Read a scalar service ACF field safely.
 *
 * @param int    $post_id    Service post ID.
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_service_field( $post_id, $field_name ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return '';
	}

	$value = '';

	if ( function_exists( 'get_field' ) ) {
		$value = get_field( $field_name, $post_id );
	}

	if ( ( '' === $value || null === $value ) && '' !== $field_name ) {
		$value = get_post_meta( $post_id, $field_name, true );
	}

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Resolve V9 modifier classes for a parent service slug.
 *
 * @param string $slug Parent service slug.
 * @return string
 */
function shpigovsky_get_services_hub_group_modifier( $slug ) {
	$map = array(
		'zavisimosti'                        => 'services-category-section-v2--addictions',
		'psihicheskoe-zdorovie'              => 'services-category-section-v2--mental-health',
		'rasstroystva-pischevogo-povedeniya' => 'services-category-section-v2--eating-disorders',
		'genotipirovanie'                    => 'services-category-section-v2--genotyping',
	);

	if ( isset( $map[ $slug ] ) ) {
		return $map[ $slug ];
	}

	return '';
}

/**
 * V9 block id for a services hub group slug.
 *
 * @param string $slug Parent service slug.
 * @return string
 */
function shpigovsky_get_services_hub_group_block_id( $slug ) {
	$map = array(
		'zavisimosti'                        => 'services-category-addictions',
		'psihicheskoe-zdorovie'              => 'services-category-mental-health',
		'rasstroystva-pischevogo-povedeniya' => 'services-category-eating-disorders',
		'genotipirovanie'                    => 'services-category-genotyping',
	);

	if ( isset( $map[ $slug ] ) ) {
		return $map[ $slug ];
	}

	return 'services-category-' . sanitize_html_class( $slug );
}

/**
 * Theme-asset fallback map for services hub slider cards by service slug.
 *
 * @return array<string, array{asset:string,width:int,height:int}>
 */
function shpigovsky_get_services_hub_slider_asset_fallback_map() {
	return array(
		'internet-zavisimost'           => array(
			'asset'  => 'img/content/services/services-addictions-01.webp',
			'width'  => 994,
			'height' => 751,
		),
		'kompyuternaya-zavisimost'      => array(
			'asset'  => 'img/content/services/services-addictions-02.webp',
			'width'  => 744,
			'height' => 566,
		),
		'lechenie-opiumnoy-zavisimosti' => array(
			'asset'  => 'img/content/services/services-addictions-03.webp',
			'width'  => 748,
			'height' => 716,
		),
		'hronicheskaya-ustalost'        => array(
			'asset'  => 'img/content/services/services-mental-health-01.webp',
			'width'  => 690,
			'height' => 512,
		),
		'stress'                        => array(
			'asset'  => 'img/content/services/services-mental-health-02.webp',
			'width'  => 902,
			'height' => 763,
		),
		'nartsissizm'                   => array(
			'asset'  => 'img/content/services/services-mental-health-03.webp',
			'width'  => 905,
			'height' => 602,
		),
	);
}

/**
 * Whether a service should appear in the /uslugi/ text list.
 * Default true when meta is unset (legacy services).
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_show_in_text_list( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return false;
	}

	if ( metadata_exists( 'post', $post_id, 'service_show_in_text_list' ) ) {
		return (bool) (int) get_post_meta( $post_id, 'service_show_in_text_list', true );
	}

	return true;
}

/**
 * Whether a service should appear in the /uslugi/ slider/gallery.
 * Default false when meta is unset.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_show_in_slider( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return false;
	}

	if ( metadata_exists( 'post', $post_id, 'service_show_in_slider' ) ) {
		return (bool) (int) get_post_meta( $post_id, 'service_show_in_slider', true );
	}

	return false;
}

/**
 * Resolve slider/gallery image data for a service post.
 *
 * @param WP_Post $service Service post.
 * @return array{url:string,width:int,height:int,alt:string,caption:string,permalink:string}|null
 */
function shpigovsky_build_services_hub_slider_card( $service ) {
	if ( ! $service instanceof WP_Post ) {
		return null;
	}

	$title = get_the_title( $service );
	$url   = get_permalink( $service );
	$url   = is_string( $url ) ? $url : '';
	$title = is_string( $title ) ? trim( $title ) : '';

	if ( '' === $title || '' === $url ) {
		return null;
	}

	$image = function_exists( 'shpigovsky_get_service_image_or_placeholder' )
		? shpigovsky_get_service_image_or_placeholder( (int) $service->ID )
		: array();

	if ( empty( $image['url'] ) ) {
		return null;
	}

	return array(
		'url'       => (string) $image['url'],
		'width'     => isset( $image['width'] ) ? (int) $image['width'] : 0,
		'height'    => isset( $image['height'] ) ? (int) $image['height'] : 0,
		'alt'       => isset( $image['alt'] ) ? (string) $image['alt'] : $title,
		'caption'   => $title,
		'permalink' => $url,
	);
}

/**
 * Format automatic category marker from 1-based render index.
 *
 * @param int $index_one_based Render order index starting at 1.
 * @return string
 */
function shpigovsky_format_services_hub_group_marker( $index_one_based ) {
	$index_one_based = max( 1, (int) $index_one_based );
	return sprintf( '%02d', $index_one_based );
}

/**
 * Marker icon label for a services hub group slug (legacy fallback only).
 *
 * @param string $slug Parent service slug.
 * @return string
 */
function shpigovsky_get_services_hub_group_icon( $slug ) {
	$map = array(
		'zavisimosti'                        => '01',
		'psihicheskoe-zdorovie'              => '02',
		'rasstroystva-pischevogo-povedeniya' => '03',
		'genotipirovanie'                    => '04',
	);

	return isset( $map[ $slug ] ) ? $map[ $slug ] : '01';
}

/**
 * Direct child service links for inline wrap menu under a parent service card.
 *
 * @param int $parent_id Parent service post ID.
 * @return array<int, array{title:string,url:string}>
 */
function shpigovsky_get_services_hub_child_links( $parent_id ) {
	$parent_id = (int) $parent_id;

	if ( $parent_id <= 0 || ! post_type_exists( 'service' ) ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $parent_id,
			'posts_per_page' => 40,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	$links = array();

	foreach ( $children as $child ) {
		if ( ! $child instanceof WP_Post ) {
			continue;
		}

		$title = get_the_title( $child );
		$url   = get_permalink( $child );

		if ( '' === $title || ! is_string( $url ) || '' === $url ) {
			continue;
		}

		$links[] = array(
			'title' => $title,
			'url'   => $url,
		);
	}

	return $links;
}

/**
 * In-page subnav anchors for the services hub route.
 *
 * @return array<int, array{id:string,label:string}>
 */
function shpigovsky_get_services_hub_subnav_items() {
	$items = array();

	foreach ( shpigovsky_get_services_hub_groups() as $group ) {
		if ( ! is_array( $group ) ) {
			continue;
		}

		$section_id = isset( $group['section_id'] ) ? trim( (string) $group['section_id'] ) : '';
		$slug       = isset( $group['slug'] ) ? trim( (string) $group['slug'] ) : '';
		$title      = isset( $group['title'] ) ? trim( (string) $group['title'] ) : '';
		$v9         = '' !== $slug ? shpigovsky_get_v9_services_hub_group_copy( $slug ) : null;
		$label      = null !== $v9 && '' !== $v9['subnav_label'] ? $v9['subnav_label'] : $title;

		if ( '' === $section_id || '' === $label ) {
			continue;
		}

		$items[] = array(
			'id'    => $section_id,
			'label' => $label,
		);
	}

	$items[] = array(
		'id'    => 'services-program',
		'label' => __( 'Программа', 'shpigovsky' ),
	);
	$items[] = array(
		'id'    => 'services-comfort',
		'label' => __( 'Условия центра', 'shpigovsky' ),
	);
	$items[] = array(
		'id'    => 'services-faq',
		'label' => __( 'Вопрос/Ответ', 'shpigovsky' ),
	);

	return $items;
}

/**
 * Add V9 body class for services hub route.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_services_hub_body_class( $classes ) {
	if ( is_page_template( 'page-templates/services-hub.php' ) ) {
		$classes[] = 'page-uslugi-v2';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_services_hub_body_class' );

/**
 * Whether copy is technical DEMO/Lorem placeholder (non-empty payload only).
 *
 * Empty string is absence, not a placeholder.
 *
 * @param string $text Candidate copy.
 * @return bool
 */
function shpigovsky_is_demo_or_lorem_placeholder_copy( $text ) {
	$text = trim( (string) $text );

	if ( '' === $text ) {
		return false;
	}

	$lower = function_exists( 'mb_strtolower' ) ? mb_strtolower( $text ) : strtolower( $text );

	if ( false !== strpos( $lower, 'lorem ipsum' ) ) {
		return true;
	}

	if (
		0 === strpos( $text, 'DEMO' )
		|| 0 === strpos( $lower, 'demo —' )
		|| 0 === strpos( $lower, 'demo -' )
		|| 0 === strpos( $lower, 'demo:' )
	) {
		return true;
	}

	if ( false !== strpos( $lower, 'временный технический текст' ) ) {
		return true;
	}

	return false;
}

/**
 * DEMO mini-description fallback when ACF and V9 static are empty.
 *
 * PROD-P07-FU01: do not emit user-facing DEMO markers. Empty = omit card text.
 *
 * @param string $slug Service post slug.
 * @return string
 */
function shpigovsky_get_service_demo_mini_description_fallback( $slug ) {
	unset( $slug );

	return '';
}

/**
 * Resolve service mini-description source attribution for validation tooling.
 *
 * @param int $post_id Service post ID.
 * @return string One of: ACF_FIELD, V9_FALLBACK, DEMO_FALLBACK, EMPTY.
 */
function shpigovsky_resolve_service_mini_description_source( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return 'EMPTY';
	}

	$admin = shpigovsky_get_service_field( $post_id, 'service_short_description' );

	if ( '' !== $admin && ! shpigovsky_is_demo_or_lorem_placeholder_copy( $admin ) ) {
		return 'ACF_FIELD';
	}

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return 'EMPTY';
	}

	$v9 = shpigovsky_get_v9_services_hub_child_copy( $post->post_name );

	if ( null !== $v9 ) {
		$v9_text = trim( (string) $v9['text'] );
		if ( '' !== $v9_text && ! shpigovsky_is_demo_or_lorem_placeholder_copy( $v9_text ) ) {
			return 'V9_FALLBACK';
		}

		return 'EMPTY';
	}

	$demo = shpigovsky_get_service_demo_mini_description_fallback( $post->post_name );

	return '' !== $demo ? 'DEMO_FALLBACK' : 'EMPTY';
}

/**
 * Resolve category-section intro for a root service on /uslugi/.
 *
 * Priority: service_short_description (Мини-описание) → V9 static intro → empty.
 * V9-06E43-FIX01: category intro no longer hardcodes V9 as primary source.
 *
 * @param WP_Post     $parent Parent/root service post.
 * @param array|null  $v9     Optional V9 group copy for $parent slug.
 * @return string
 */
function shpigovsky_resolve_services_hub_category_intro( $parent, $v9 = null ) {
	if ( ! $parent instanceof WP_Post ) {
		return '';
	}

	$admin = shpigovsky_get_service_field( $parent->ID, 'service_short_description' );

	if ( '' !== $admin && ! shpigovsky_is_demo_or_lorem_placeholder_copy( $admin ) ) {
		return $admin;
	}

	if ( null === $v9 ) {
		$v9 = shpigovsky_get_v9_services_hub_group_copy( $parent->post_name );
	}

	if ( null !== $v9 && isset( $v9['intro'] ) && '' !== trim( (string) $v9['intro'] ) ) {
		return trim( (string) $v9['intro'] );
	}

	$hero_lead = shpigovsky_get_service_field( $parent->ID, 'hero_lead' );

	return '' !== $hero_lead ? $hero_lead : '';
}

/**
 * Resolve category-section lead for a root service on /uslugi/.
 *
 * Priority: service_category_section_lead → V9 static lead → intro_text/intro_note.
 * V9-06E43-FIX01: editable admin field with V9/legacy fallback only when empty.
 *
 * @param WP_Post    $parent Parent/root service post.
 * @param array|null $v9     Optional V9 group copy for $parent slug.
 * @return string
 */
function shpigovsky_resolve_services_hub_category_lead( $parent, $v9 = null ) {
	if ( ! $parent instanceof WP_Post ) {
		return '';
	}

	$admin = shpigovsky_get_service_field( $parent->ID, 'service_category_section_lead' );

	if ( '' !== $admin ) {
		return $admin;
	}

	if ( null === $v9 ) {
		$v9 = shpigovsky_get_v9_services_hub_group_copy( $parent->post_name );
	}

	if ( null !== $v9 && isset( $v9['lead'] ) && '' !== trim( (string) $v9['lead'] ) ) {
		return trim( (string) $v9['lead'] );
	}

	$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_text' );

	if ( '' === $lead_secondary ) {
		$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_note' );
	}

	return $lead_secondary;
}

/**
 * Resolve service mini-description for services hub cards.
 *
 * Priority: ACF field → V9 static authority → DEMO fallback.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_get_service_mini_description( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return '';
	}

	$admin = shpigovsky_get_service_field( $post_id, 'service_short_description' );

	if ( '' !== $admin && ! shpigovsky_is_demo_or_lorem_placeholder_copy( $admin ) ) {
		return $admin;
	}

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return '';
	}

	$v9 = shpigovsky_get_v9_services_hub_child_copy( $post->post_name );

	if ( null !== $v9 ) {
		$v9_text = trim( (string) $v9['text'] );
		if ( '' !== $v9_text && ! shpigovsky_is_demo_or_lorem_placeholder_copy( $v9_text ) ) {
			return $v9_text;
		}

		return '';
	}

	return shpigovsky_get_service_demo_mini_description_fallback( $post->post_name );
}

/**
 * Build child service card data from a service post.
 *
 * @param WP_Post $child Child service post.
 * @return array{title:string,url:string,text:string,slug:string,children:array<int,array{title:string,url:string}>}|null
 */
function shpigovsky_build_services_hub_child_card( $child ) {
	if ( ! $child instanceof WP_Post ) {
		return null;
	}

	$slug  = $child->post_name;
	$v9    = shpigovsky_get_v9_services_hub_child_copy( $slug );
	$title = null !== $v9 && '' !== $v9['title'] ? $v9['title'] : get_the_title( $child );
	$url   = get_permalink( $child );

	if ( '' === $title ) {
		return null;
	}

	$text = shpigovsky_get_service_mini_description( $child->ID );

	return array(
		'title'    => $title,
		'url'      => is_string( $url ) ? $url : '',
		'text'     => $text,
		'slug'     => $slug,
		'children' => shpigovsky_get_services_hub_child_links( $child->ID ),
	);
}

/**
 * Build grouped Services Hub sections from hierarchical Service CPT.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_groups() {
	if ( ! post_type_exists( 'service' ) ) {
		return array();
	}

	$query_mode = shpigovsky_get_services_hub_field( 'services_hub_query_mode' );

	if ( '' === $query_mode ) {
		$query_mode = 'grouped_by_parent';
	}

	if ( 'flat' === $query_mode ) {
		return shpigovsky_get_services_hub_flat_group();
	}

	$parents = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => 0,
			'posts_per_page' => 12,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	if ( empty( $parents ) ) {
		return array();
	}

	$groups       = array();
	$marker_index = 0;

	foreach ( $parents as $parent ) {
		if ( ! $parent instanceof WP_Post ) {
			continue;
		}

		$children = get_posts(
			array(
				'post_type'      => 'service',
				'post_status'    => 'publish',
				'post_parent'    => $parent->ID,
				'posts_per_page' => 40,
				'orderby'        => 'menu_order',
				'order'          => 'ASC',
				'no_found_rows'  => true,
			)
		);

		$cards   = array();
		$gallery = array();

		foreach ( $children as $child ) {
			if ( ! $child instanceof WP_Post ) {
				continue;
			}

			if ( shpigovsky_service_show_in_text_list( $child->ID ) ) {
				$card = shpigovsky_build_services_hub_child_card( $child );

				if ( null !== $card ) {
					$cards[] = $card;
				}
			}

			if ( shpigovsky_service_show_in_slider( $child->ID ) ) {
				$slide = shpigovsky_build_services_hub_slider_card( $child );

				if ( null !== $slide ) {
					$gallery[] = $slide;
				}
			}
		}

		if ( empty( $cards ) ) {
			if ( shpigovsky_service_show_in_text_list( $parent->ID ) ) {
				$parent_card = shpigovsky_build_services_hub_child_card( $parent );

				if ( null !== $parent_card ) {
					$cards[] = $parent_card;
				}
			}
		}

		if ( empty( $gallery ) && shpigovsky_service_show_in_slider( $parent->ID ) ) {
			$parent_slide = shpigovsky_build_services_hub_slider_card( $parent );

			if ( null !== $parent_slide ) {
				$gallery[] = $parent_slide;
			}
		}

		if ( empty( $cards ) && empty( $gallery ) ) {
			continue;
		}

		if ( empty( $cards ) ) {
			$parent_card = shpigovsky_build_services_hub_child_card( $parent );

			if ( null !== $parent_card ) {
				$cards[] = $parent_card;
			}
		}

		if ( empty( $cards ) ) {
			continue;
		}

		$slug = $parent->post_name;
		$v9   = shpigovsky_get_v9_services_hub_group_copy( $slug );

		// V9-06E43-FIX01: category intro from mini-description; lead from dedicated field.
		$lead_primary   = shpigovsky_resolve_services_hub_category_intro( $parent, $v9 );
		$lead_secondary = shpigovsky_resolve_services_hub_category_lead( $parent, $v9 );
		$group_title    = null !== $v9 && '' !== trim( (string) $v9['title'] )
			? trim( (string) $v9['title'] )
			: get_the_title( $parent );

		++$marker_index;

		$parent_url = get_permalink( $parent );
		if ( ! is_string( $parent_url ) ) {
			$parent_url = '';
		}

		$groups[] = array(
			'parent_id'      => $parent->ID,
			'title'          => $group_title,
			'slug'           => $slug,
			'url'            => $parent_url,
			'lead_primary'   => $lead_primary,
			'lead_secondary' => $lead_secondary,
			'intro'          => $lead_primary,
			'lead'           => $lead_secondary,
			'modifier_class' => shpigovsky_get_services_hub_group_modifier( $slug ),
			'block_id'       => shpigovsky_get_services_hub_group_block_id( $slug ),
			'section_id'     => shpigovsky_get_services_hub_group_block_id( $slug ) . '-heading',
			'icon'           => shpigovsky_format_services_hub_group_marker( $marker_index ),
			'cta_source'     => 'services-' . sanitize_html_class( $slug ),
			'children'       => $cards,
			'gallery'        => $gallery,
			'cta_label'      => null !== $v9 ? $v9['cta_label'] : 'Записаться на консультацию',
		);
	}

	return $groups;
}

/**
 * Build a single flat group when query mode is flat.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_flat_group() {
	$services = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'posts_per_page' => 50,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	if ( empty( $services ) ) {
		return array();
	}

	$cards = array();

	foreach ( $services as $service ) {
		$card = shpigovsky_build_services_hub_child_card( $service );

		if ( null !== $card ) {
			$cards[] = $card;
		}
	}

	if ( empty( $cards ) ) {
		return array();
	}

	return array(
		array(
			'parent_id'      => 0,
			'title'          => __( 'Услуги центра', 'shpigovsky' ),
			'slug'           => 'all-services',
			'lead_primary'   => shpigovsky_get_services_hub_field( 'services_hub_intro' ),
			'lead_secondary' => '',
			'modifier_class' => 'services-category-hub--no-gallery',
			'section_id'     => 'services-category-all-heading',
			'cta_source'     => 'services-flat',
			'children'       => $cards,
			'gallery'        => array(),
		),
	);
}

/**
 * Whether Services Hub has renderable service groups.
 *
 * @return bool
 */
function shpigovsky_services_hub_has_groups() {
	return ! empty( shpigovsky_get_services_hub_groups() );
}
