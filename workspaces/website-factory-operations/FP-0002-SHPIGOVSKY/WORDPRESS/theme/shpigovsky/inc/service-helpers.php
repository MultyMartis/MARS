<?php
/**
 * Service single template ACF read helpers and CPT queries — V9-06D7-D.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Current service post ID in the loop.
 *
 * @return int
 */
function shpigovsky_get_current_service_id() {
	return (int) get_the_ID();
}

/**
 * Read a bounded service repeater safely.
 *
 * @param int    $post_id    Service post ID.
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_service_repeater( $post_id, $field_name ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return array();
	}

	$rows = get_field( $field_name, $post_id );

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
 * Read service hero image attachment array.
 *
 * @param int $post_id Service post ID.
 * @return array<string, mixed>|null
 */
function shpigovsky_get_service_hero_image( $post_id ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return null;
	}

	$image = get_field( 'hero_media', $post_id );

	return is_array( $image ) ? $image : null;
}

/**
 * Neutral service placeholder image asset (theme-local SVG).
 *
 * @return array{url:string,width:int,height:int,alt:string,source:string}
 */
function shpigovsky_get_service_placeholder_image() {
	return array(
		'url'    => shpigovsky_asset_uri( 'images/service-placeholder.svg' ),
		'width'  => 800,
		'height' => 600,
		'alt'    => __( 'Фото скоро будет', 'shpigovsky' ),
		'source' => 'placeholder',
	);
}

/**
 * Resolve service card/page image with neutral placeholder fallback.
 *
 * Priority: service_slider_image → featured image → hero_media → placeholder.
 * Does not overwrite or mutate existing media.
 *
 * @param int $post_id Service post ID.
 * @return array{url:string,width:int,height:int,alt:string,source:string}
 */
function shpigovsky_get_service_image_or_placeholder( $post_id ) {
	$post_id = (int) $post_id;
	$title   = $post_id > 0 ? get_the_title( $post_id ) : '';
	$title   = is_string( $title ) ? trim( $title ) : '';
	$alt     = '' !== $title ? $title : __( 'Фото скоро будет', 'shpigovsky' );

	if ( $post_id > 0 && function_exists( 'get_field' ) ) {
		$acf_image = get_field( 'service_slider_image', $post_id );
		if ( is_array( $acf_image ) && ! empty( $acf_image['url'] ) ) {
			return array(
				'url'    => (string) $acf_image['url'],
				'width'  => isset( $acf_image['width'] ) ? (int) $acf_image['width'] : 0,
				'height' => isset( $acf_image['height'] ) ? (int) $acf_image['height'] : 0,
				'alt'    => ! empty( $acf_image['alt'] ) ? (string) $acf_image['alt'] : $alt,
				'source' => 'slider_image',
			);
		}
	}

	if ( $post_id > 0 && has_post_thumbnail( $post_id ) ) {
		$thumb_id = (int) get_post_thumbnail_id( $post_id );
		$src      = wp_get_attachment_image_src( $thumb_id, 'large' );
		if ( is_array( $src ) && ! empty( $src[0] ) ) {
			$thumb_alt = get_post_meta( $thumb_id, '_wp_attachment_image_alt', true );
			return array(
				'url'    => (string) $src[0],
				'width'  => isset( $src[1] ) ? (int) $src[1] : 0,
				'height' => isset( $src[2] ) ? (int) $src[2] : 0,
				'alt'    => is_string( $thumb_alt ) && '' !== trim( $thumb_alt ) ? trim( $thumb_alt ) : $alt,
				'source' => 'featured',
			);
		}
	}

	if ( $post_id > 0 && function_exists( 'get_field' ) ) {
		$hero = get_field( 'hero_media', $post_id );
		if ( is_array( $hero ) && ! empty( $hero['url'] ) ) {
			return array(
				'url'    => (string) $hero['url'],
				'width'  => isset( $hero['width'] ) ? (int) $hero['width'] : 0,
				'height' => isset( $hero['height'] ) ? (int) $hero['height'] : 0,
				'alt'    => ! empty( $hero['alt'] ) ? (string) $hero['alt'] : $alt,
				'source' => 'hero_media',
			);
		}
	}

	// Theme slug asset fallbacks for /uslugi/ gallery (non-placeholder) when present.
	if ( $post_id > 0 && function_exists( 'shpigovsky_get_services_hub_slider_asset_fallback_map' ) ) {
		$post = get_post( $post_id );
		if ( $post instanceof WP_Post ) {
			$fallbacks = shpigovsky_get_services_hub_slider_asset_fallback_map();
			if ( isset( $fallbacks[ $post->post_name ] ) ) {
				$fb = $fallbacks[ $post->post_name ];
				return array(
					'url'    => shpigovsky_asset_uri( $fb['asset'] ),
					'width'  => (int) $fb['width'],
					'height' => (int) $fb['height'],
					'alt'    => $alt,
					'source' => 'theme_slug_fallback',
				);
			}
		}
	}

	$placeholder         = shpigovsky_get_service_placeholder_image();
	$placeholder['alt']  = $alt;
	return $placeholder;
}

/**
 * Theme asset fallback for service hero images when ACF hero_media is empty.
 *
 * @param string $variant Layout variant slug.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_service_default_hero_image( $variant ) {
	$post_id     = shpigovsky_get_current_service_id();
	$context_key = shpigovsky_get_service_hero_context_key( $post_id, $variant );

	return shpigovsky_get_hero_theme_fallback( $context_key );
}

/**
 * Resolve service H1 title with optional ACF override.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_get_service_hero_title( $post_id ) {
	$override = shpigovsky_get_service_field( $post_id, 'hero_title_override' );

	if ( '' !== $override ) {
		return $override;
	}

	$title = get_the_title( $post_id );

	return is_string( $title ) ? trim( $title ) : '';
}

/**
 * Whether a service post has published child services.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_has_children( $post_id ) {
	if ( ! post_type_exists( 'service' ) || $post_id <= 0 ) {
		return false;
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $post_id,
			'posts_per_page' => 1,
			'fields'         => 'ids',
			'no_found_rows'  => true,
		)
	);

	return ! empty( $children );
}

/**
 * Get published child services for a parent service.
 *
 * @param int $post_id Parent service post ID.
 * @return WP_Post[]
 */
function shpigovsky_get_service_children( $post_id ) {
	if ( ! post_type_exists( 'service' ) || $post_id <= 0 ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $post_id,
			'posts_per_page' => 30,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	return is_array( $children ) ? $children : array();
}

/**
 * Map ACF layout value to theme stack variant slug.
 *
 * V9-06E45-FIX02: `service_general` is the active general service stack.
 * `alcohol_special` remains a legacy ACF alias mapping to the same stack.
 *
 * @param string $acf_value Raw ACF select value.
 * @return string
 */
function shpigovsky_map_acf_layout_to_variant( $acf_value ) {
	$map = array(
		'subdivision'     => 'subdivision',
		'standard'        => 'leaf',
		'extended'        => 'leaf',
		'service_general' => 'service-general',
		'alcohol_special' => 'service-general', // legacy alias
		'placeholder'     => 'placeholder',
	);

	return isset( $map[ $acf_value ] ) ? $map[ $acf_value ] : '';
}

/**
 * Whether frontend variant is the general service stack (incl. legacy slug).
 *
 * @param string $variant Theme stack variant slug.
 * @return bool
 */
function shpigovsky_is_service_general_variant( $variant ) {
	return in_array( (string) $variant, array( 'service-general', 'alcohol-special' ), true );
}

/**
 * Known alcohol page — preserves V9 alcohol-only static copy (not all service pages).
 *
 * @param int|null $post_id Optional post ID.
 * @return bool
 */
function shpigovsky_is_known_alcohol_service_page( $post_id = null ) {
	if ( null === $post_id ) {
		$post_id = shpigovsky_get_current_service_id();
	}

	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		return false;
	}

	if ( 74 === $post_id ) {
		return true;
	}

	$slug = (string) get_post_field( 'post_name', $post_id );
	return 'lechenie-alkogolnoy-zavisimosti' === $slug;
}

/**
 * Whether current/known post should render V9 alcohol static copy blocks.
 *
 * @param int|null $post_id Optional post ID.
 * @return bool
 */
function shpigovsky_service_uses_alcohol_v9_static_copy( $post_id = null ) {
	return shpigovsky_is_known_alcohol_service_page( $post_id );
}

/**
 * Infer layout variant from hierarchy / known roots when ACF+role empty.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_infer_service_layout_variant( $post_id ) {
	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return 'service-general';
	}

	// Known subdivision roots only — children with nesting stay service stack.
	// Alcohol page #74 is a service page (same stack); static copy gated separately.
	$root_section_ids = array( 73, 77, 84 );
	if ( in_array( (int) $post_id, $root_section_ids, true ) ) {
		return 'subdivision';
	}

	if ( 0 === (int) $post->post_parent && shpigovsky_service_has_children( $post_id ) ) {
		return 'subdivision';
	}

	return 'service-general';
}

/**
 * Service CPT hierarchy depth (1 = top-level, 2+ = nested).
 *
 * @param int $post_id Service post ID.
 * @return int
 */
function shpigovsky_get_service_depth( $post_id ) {
	if ( class_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance' )
		&& method_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance', 'get_service_depth' ) ) {
		return (int) \Shpigovsky\Core\Admin\ServiceLayoutGovernance::get_service_depth( $post_id );
	}

	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		return 0;
	}

	$depth  = 1;
	$parent = (int) get_post_field( 'post_parent', $post_id );
	$guard  = 0;
	$seen   = array( $post_id => true );

	while ( $parent > 0 && $guard < 20 ) {
		if ( isset( $seen[ $parent ] ) ) {
			break;
		}
		$seen[ $parent ] = true;
		if ( 'service' !== get_post_type( $parent ) ) {
			break;
		}
		++$depth;
		$parent = (int) get_post_field( 'post_parent', $parent );
		++$guard;
	}

	return $depth;
}

/**
 * Resolve canonical service layout variant for routing (V9-06E51 / E51-FIX01).
 *
 * Effective stack — visible editor role wins over stale technical layout:
 * - role placeholder → placeholder (nested allowed; content preserved)
 * - role section → subdivision
 * - role service → service-general
 * - nested (depth 2+) without role → service-general (unless layout placeholder leftover with empty role)
 * - empty role: derive from technical layout / hierarchy
 *
 * @param int|null $post_id Optional post ID; defaults to current post.
 * @return string
 */
function shpigovsky_resolve_service_layout_variant( $post_id = null ) {
	if ( null === $post_id ) {
		$post_id = shpigovsky_get_current_service_id();
	}

	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return 'service-general';
	}

	$role      = shpigovsky_get_service_field( $post_id, 'service_editor_role' );
	$override  = (bool) shpigovsky_get_service_field( $post_id, 'service_layout_override_enabled' );
	$acf_value = shpigovsky_get_service_field( $post_id, 'service_layout_variant' );

	// V9-06E51-FIX01: explicit editor role always wins. Stale layout=placeholder
	// must not keep the stub stack after a manual switch to Услуга / Раздел.
	if ( 'placeholder' === $role ) {
		return 'placeholder';
	}
	if ( 'section' === $role ) {
		return 'subdivision';
	}
	if ( 'service' === $role ) {
		return 'service-general';
	}

	// Depth 2+: nested services without an explicit role use the general stack.
	if ( shpigovsky_get_service_depth( $post_id ) >= 2 ) {
		return 'service-general';
	}

	// Legacy override path retained for stale meta; FIX03 admin UI no longer exposes it.
	if ( $override ) {
		$variant = shpigovsky_map_acf_layout_to_variant( $acf_value );
		if ( '' !== $variant ) {
			return $variant;
		}
	}

	// Empty role: derive safely from technical layout / hierarchy.
	$variant = shpigovsky_map_acf_layout_to_variant( $acf_value );
	if ( 'subdivision' === $variant ) {
		return 'subdivision';
	}
	if ( 'placeholder' === $variant ) {
		return 'placeholder';
	}
	if ( shpigovsky_is_service_general_variant( $variant ) ) {
		return 'service-general';
	}

	return shpigovsky_infer_service_layout_variant( $post_id );
}

/**
 * Whether child-services tile block should render.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_child_services_block_enabled( $post_id ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		return false;
	}

	$enabled = shpigovsky_get_service_field( $post_id, 'service_child_services_enabled' );
	if ( '' === $enabled || null === $enabled ) {
		return true;
	}

	return (bool) $enabled;
}

/**
 * Heading for child-services tile block.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_get_service_child_services_heading( $post_id ) {
	$heading = shpigovsky_get_service_field( $post_id, 'service_child_services_heading' );
	$heading = is_string( $heading ) ? trim( $heading ) : '';

	if ( '' !== $heading ) {
		return $heading;
	}

	return __( 'Направления внутри услуги', 'shpigovsky' );
}

/**
 * Card image URL for a child service card (optional).
 *
 * @param int $post_id Child service ID.
 * @return string
 */
function shpigovsky_get_service_child_card_image_url( $post_id ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		return '';
	}

	$image = shpigovsky_get_service_field( $post_id, 'service_slider_image' );
	if ( is_array( $image ) && ! empty( $image['url'] ) ) {
		return (string) $image['url'];
	}

	$hero = shpigovsky_get_service_field( $post_id, 'hero_media' );
	if ( is_array( $hero ) && ! empty( $hero['url'] ) ) {
		return (string) $hero['url'];
	}

	$thumb = get_the_post_thumbnail_url( $post_id, 'medium' );
	return is_string( $thumb ) ? $thumb : '';
}

/**
 * Main element class for the current service layout variant.
 *
 * @param string $variant Layout variant slug.
 * @return string
 */
function shpigovsky_get_service_main_class( $variant ) {
	if ( 'subdivision' === $variant ) {
		return 'page-service-subdivision-v1__main site-main site-main--service site-main--service-subdivision';
	}

	if ( 'placeholder' === $variant ) {
		return 'page-service-placeholder-v1__main site-main site-main--service site-main--service-placeholder';
	}

	return 'page-service-leaf-v1__main site-main site-main--service site-main--service-leaf';
}

/**
 * Build breadcrumb trail items for a service post.
 *
 * @param int $post_id Service post ID.
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_service_breadcrumb_trail( $post_id ) {
	$trail = array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'Услуги', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/' ),
		),
	);

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return $trail;
	}

	$ancestors = array_reverse( get_post_ancestors( $post ) );

	foreach ( $ancestors as $ancestor_id ) {
		$ancestor = get_post( $ancestor_id );

		if ( ! $ancestor instanceof WP_Post || 'service' !== $ancestor->post_type ) {
			continue;
		}

		$url = get_permalink( $ancestor );

		$trail[] = array(
			'label' => get_the_title( $ancestor ),
			'url'   => is_string( $url ) ? $url : '',
		);
	}

	$trail[] = array(
		'label' => get_the_title( $post ),
		'url'   => '',
	);

	return $trail;
}

/**
 * Build in-page subnav anchor items for a service layout variant.
 *
 * @param string $variant Layout variant slug.
 * @return array<int, array{id:string,label:string}>
 */
function shpigovsky_get_service_subnav_items( $variant ) {
	if ( 'subdivision' === $variant ) {
		// V9-06E50: labels from section ACF when present (avoid hardcoded «Зависимости» on all sections).
		$post_id = function_exists( 'shpigovsky_get_current_service_id' )
			? (int) shpigovsky_get_current_service_id()
			: (int) get_the_ID();
		$deps_label    = function_exists( 'shpigovsky_get_section_field' )
			? shpigovsky_get_section_field( $post_id, 'section_dependencies_heading' )
			: '';
		$nature_label  = function_exists( 'shpigovsky_get_section_field' )
			? shpigovsky_get_section_field( $post_id, 'section_nature_heading' )
			: '';
		$approach_label = function_exists( 'shpigovsky_get_section_field' )
			? shpigovsky_get_section_field( $post_id, 'section_approach_heading' )
			: '';

		if ( '' === $deps_label ) {
			$deps_label = __( 'Услуги раздела', 'shpigovsky' );
		}
		if ( '' === $nature_label ) {
			$nature_label = __( 'Природа', 'shpigovsky' );
		}
		if ( '' === $approach_label ) {
			$approach_label = __( 'Наш подход к лечению', 'shpigovsky' );
		}

		return array(
			array(
				'id'    => 'service-subdivision-dependencies',
				'label' => $deps_label,
			),
			array(
				'id'    => 'service-subdivision-nature',
				'label' => $nature_label,
			),
			array(
				'id'    => 'service-subdivision-program',
				'label' => __( 'Программа лечения', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-start',
				'label' => __( 'С чего начать', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-approach',
				'label' => $approach_label,
			),
			array(
				'id'    => 'service-subdivision-specialists',
				'label' => __( 'Специалисты', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-comfort',
				'label' => __( 'Условия центра', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-faq',
				'label' => __( 'Вопросы и ответы', 'shpigovsky' ),
			),
		);
	}

	$items = array(
		array(
			'id'    => 'service-leaf-intro',
			'label' => __( 'О программе', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-program',
			'label' => __( 'Программа лечения', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-start',
			'label' => __( 'С чего начать', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-faq',
			'label' => __( 'Вопросы и ответы', 'shpigovsky' ),
		),
	);

	if ( shpigovsky_is_service_general_variant( $variant ) ) {
		return array(
			array(
				'id'    => 'service-leaf-approach',
				'label' => __( 'Наш подход к лечению', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-leaf-program',
				'label' => __( 'Программа лечения', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-leaf-start',
				'label' => __( 'С чего начать', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-leaf-specialists',
				'label' => __( 'Специалисты', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-leaf-comfort',
				'label' => __( 'Условия центра', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-leaf-reviews',
				'label' => __( 'Отзывы о программе', 'shpigovsky' ),
			),
		);
	}

	return $items;
}

/**
 * Default programme direction labels when ACF repeater is empty.
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_service_programme_fallback_items() {
	return array(
		array(
			'title' => '01 — Генотипирование',
			'text'  => '',
		),
		array(
			'title' => '02 — Нейропсихологическая коррекция',
			'text'  => '',
		),
		array(
			'title' => '03 — Психокоррекция',
			'text'  => '',
		),
		array(
			'title' => '04 — Кинезиотерапия',
			'text'  => '',
		),
	);
}

/**
 * Static V9 programme items for service subdivision layout parity.
 *
 * @return array<int, array{title:string,image:string,width:int,height:int,alt:string}>
 */
function shpigovsky_get_service_subdivision_programme_fallback_items() {
	$items = array();

	foreach ( shpigovsky_get_program_direction_items( 'service' ) as $direction ) {
		$items[] = array(
			'title'  => $direction['title_display'],
			'image'  => $direction['image'],
			'width'  => $direction['width'],
			'height' => $direction['height'],
			'alt'    => $direction['alt'],
			'url'    => $direction['url'],
		);
	}

	return $items;
}

/**
 * Static V9 dependencies section heading for subdivision pages.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_heading() {
	return __( 'Зависимости, которые мы лечим', 'shpigovsky' );
}

/**
 * Static V9 dependencies section lead fallback.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_lead_fallback() {
	return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

/**
 * Static V9 dependencies section footer text fallback.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_footer_fallback() {
	return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

/**
 * Add V9 body class for service single routes.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_service_body_class( $classes ) {
	if ( ! is_singular( 'service' ) ) {
		return $classes;
	}

	$variant = shpigovsky_get_service_layout_variant();

	if ( 'subdivision' === $variant ) {
		$classes[] = 'page-service-subdivision-v1';
	} elseif ( 'leaf' === $variant || shpigovsky_is_service_general_variant( $variant ) ) {
		$classes[] = 'page-service-leaf-v1';
		if ( shpigovsky_is_service_general_variant( $variant ) ) {
			$classes[] = 'page-service-general-v1';
			$classes[] = 'page-service-alcohol-special-legacy'; // CSS/legacy marker until styles fully renamed
		}
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_service_body_class' );

/**
 * Resolve CTA band copy for service mid-page CTAs.
 *
 * @param int $post_id Service post ID.
 * @return array{title:string,subtitle:string,phone:string,phone_hint:string,button_label:string,source:string}
 */
function shpigovsky_get_service_cta_band( $post_id ) {
	$title        = shpigovsky_get_service_field( $post_id, 'cta_title' );
	$subtitle     = shpigovsky_get_service_field( $post_id, 'cta_text' );
	$button_label = shpigovsky_get_service_field( $post_id, 'cta_button_label' );
	$phone        = shpigovsky_get_site_option( 'phone_primary' );
	$phone        = '' !== $phone ? shpigovsky_format_phone_display( $phone ) : '';
	$default_cta  = shpigovsky_get_site_option( 'default_button_label' );
	$default_cta  = '' !== $default_cta ? $default_cta : __( 'Записаться', 'shpigovsky' );

	if ( '' === $title ) {
		$title = shpigovsky_get_cta_band_default_title();
	}

	if ( '' === $subtitle ) {
		$subtitle = shpigovsky_get_cta_band_default_subtitle();
	}

	if ( '' === $button_label ) {
		$button_label = shpigovsky_get_cta_band_default_button_label( $default_cta );
	}

	$button_url = shpigovsky_get_service_field( $post_id, 'cta_button_target' );
	$button_url = is_string( $button_url ) ? trim( $button_url ) : '';

	return array(
		'title'        => $title,
		'subtitle'     => $subtitle,
		'phone'        => $phone,
		'phone_hint'   => shpigovsky_get_cta_band_phone_hint( __( 'Или позвоните нам', 'shpigovsky' ) ),
		'button_label' => $button_label,
		'button_url'   => $button_url,
		'source'       => 'service-cta-' . $post_id,
	);
}
