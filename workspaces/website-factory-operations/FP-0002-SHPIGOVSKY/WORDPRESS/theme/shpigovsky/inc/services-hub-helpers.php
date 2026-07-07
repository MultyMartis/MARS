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
 * Read a boolean Services Hub ACF field safely.
 *
 * @param string $field_name Field name.
 * @return bool
 */
function shpigovsky_get_services_hub_bool( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return false;
	}

	$page_id = shpigovsky_get_services_hub_page_id();

	if ( $page_id <= 0 ) {
		return false;
	}

	return (bool) get_field( $field_name, $page_id );
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
 * Static V9 gallery fallback images for a services hub group slug.
 *
 * @param string $slug Parent service slug.
 * @return array<int, array{url:string,width:int,height:int,alt:string,caption:string}>
 */
function shpigovsky_get_services_hub_group_gallery( $slug ) {
	$map = array(
		'zavisimosti' => array(
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-addictions-01.webp' ),
				'width'   => 994,
				'height'  => 751,
				'alt'     => '',
				'caption' => 'Лечение интернет зависимости',
			),
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-addictions-02.webp' ),
				'width'   => 744,
				'height'  => 566,
				'alt'     => '',
				'caption' => 'Компьютерная зависимость',
			),
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-addictions-03.webp' ),
				'width'   => 748,
				'height'  => 716,
				'alt'     => '',
				'caption' => 'Лечение опиумной зависимости',
			),
		),
		'psihicheskoe-zdorovie' => array(
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-mental-health-01.webp' ),
				'width'   => 690,
				'height'  => 512,
				'alt'     => '',
				'caption' => 'Хроническая усталось',
			),
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-mental-health-02.webp' ),
				'width'   => 902,
				'height'  => 763,
				'alt'     => '',
				'caption' => 'Стресс',
			),
			array(
				'url'     => shpigovsky_asset_uri( 'img/content/services/services-mental-health-03.webp' ),
				'width'   => 905,
				'height'  => 602,
				'alt'     => '',
				'caption' => 'Нарциссизм',
			),
		),
	);

	return isset( $map[ $slug ] ) ? $map[ $slug ] : array();
}

/**
 * Marker icon label for a services hub group slug.
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
 * DEMO mini-description fallback when ACF and V9 static are empty.
 *
 * @param string $slug Service post slug.
 * @return string
 */
function shpigovsky_get_service_demo_mini_description_fallback( $slug ) {
	$demos = array(
		'zavisimosti'                        => 'DEMO — направление лечения зависимостей. Карточка раздела для плоского режима отображения /uslugi/.',
		'psihicheskoe-zdorovie'              => 'DEMO — направление психического здоровья. Карточка раздела для плоского режима отображения /uslugi/.',
		'rasstroystva-pischevogo-povedeniya' => 'DEMO — направление расстройств пищевого поведения. Карточка раздела для плоского режима отображения /uslugi/.',
		'genotipirovanie'                    => 'DEMO — направление генотипирования. Карточка раздела для плоского режима отображения /uslugi/.',
	);

	if ( isset( $demos[ $slug ] ) ) {
		return $demos[ $slug ];
	}

	return 'DEMO — краткое описание услуги для карточки на /uslugi/. Контент ожидает согласования оператором.';
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

	if ( '' !== $admin ) {
		return 'ACF_FIELD';
	}

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return 'EMPTY';
	}

	$v9 = shpigovsky_get_v9_services_hub_child_copy( $post->post_name );

	if ( null !== $v9 && '' !== trim( (string) $v9['text'] ) ) {
		return 'V9_FALLBACK';
	}

	$demo = shpigovsky_get_service_demo_mini_description_fallback( $post->post_name );

	return '' !== $demo ? 'DEMO_FALLBACK' : 'EMPTY';
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

	if ( '' !== $admin ) {
		return $admin;
	}

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return '';
	}

	$v9 = shpigovsky_get_v9_services_hub_child_copy( $post->post_name );

	if ( null !== $v9 && '' !== trim( (string) $v9['text'] ) ) {
		return trim( (string) $v9['text'] );
	}

	return shpigovsky_get_service_demo_mini_description_fallback( $post->post_name );
}

/**
 * Build child service card data from a service post.
 *
 * @param WP_Post $child Child service post.
 * @return array{title:string,url:string,text:string}|null
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
		'title' => $title,
		'url'   => is_string( $url ) ? $url : '',
		'text'  => $text,
		'slug'  => $slug,
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

	$groups = array();

	foreach ( $parents as $parent ) {
		if ( ! $parent instanceof WP_Post ) {
			continue;
		}

		$children = get_posts(
			array(
				'post_type'      => 'service',
				'post_status'    => 'publish',
				'post_parent'    => $parent->ID,
				'posts_per_page' => 30,
				'orderby'        => 'menu_order',
				'order'          => 'ASC',
				'no_found_rows'  => true,
			)
		);

		$cards = array();

		foreach ( $children as $child ) {
			$card = shpigovsky_build_services_hub_child_card( $child );

			if ( null !== $card ) {
				$cards[] = $card;
			}
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

		if ( null !== $v9 ) {
			$lead_primary   = $v9['intro'];
			$lead_secondary = $v9['lead'];
			$group_title    = $v9['title'];
		} else {
			$lead_primary   = shpigovsky_get_service_field( $parent->ID, 'hero_lead' );
			$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_text' );
			$group_title    = get_the_title( $parent );

			if ( '' === $lead_secondary ) {
				$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_note' );
			}
		}

		$gallery = shpigovsky_get_services_hub_group_gallery( $slug );
		$captions = shpigovsky_get_v9_services_hub_gallery_captions( $slug );

		if ( ! empty( $captions ) ) {
			foreach ( $gallery as $index => $image ) {
				if ( isset( $captions[ $index ] ) ) {
					$gallery[ $index ]['caption'] = $captions[ $index ];
				}
			}
		}

		$groups[] = array(
			'parent_id'      => $parent->ID,
			'title'          => $group_title,
			'slug'           => $slug,
			'lead_primary'   => $lead_primary,
			'lead_secondary' => $lead_secondary,
			'intro'          => $lead_primary,
			'lead'           => $lead_secondary,
			'modifier_class' => shpigovsky_get_services_hub_group_modifier( $slug ),
			'block_id'       => shpigovsky_get_services_hub_group_block_id( $slug ),
			'section_id'     => shpigovsky_get_services_hub_group_block_id( $slug ) . '-heading',
			'icon'           => shpigovsky_get_services_hub_group_icon( $slug ),
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
