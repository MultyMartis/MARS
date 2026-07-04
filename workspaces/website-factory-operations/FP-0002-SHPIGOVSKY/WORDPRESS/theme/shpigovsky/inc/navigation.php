<?php
/**
 * Navigation helpers — V9 class compatibility and first-wave fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * First-wave primary nav fallback when no WP menu is assigned.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_primary_nav_fallback_items() {
	return array(
		array(
			'label' => __( 'Лечение и профилактика', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/' ),
		),
		array(
			'label' => __( 'Зависимости', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/zavisimosti/' ),
		),
		array(
			'label' => __( 'О центре', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/' ),
		),
		array(
			'label' => __( 'Отзывы', 'shpigovsky' ),
			'url'   => home_url( '/otzyvy/' ),
		),
		array(
			'label' => __( 'Статьи', 'shpigovsky' ),
			'url'   => home_url( '/blog/' ),
		),
		array(
			'label' => __( 'Контакты', 'shpigovsky' ),
			'url'   => home_url( '/kontakty/' ),
		),
	);
}

/**
 * Footer services column fallback.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_footer_services_fallback_items() {
	return array(
		array(
			'label' => __( 'Зависимости', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/zavisimosti/' ),
		),
		array(
			'label' => __( 'Психическое здоровье', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/psihicheskoe-zdorovie/' ),
		),
		array(
			'label' => __( 'Расстройства пищевого поведения', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ),
		),
	);
}

/**
 * Footer about column fallback.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_footer_o_centre_fallback_items() {
	return array(
		array(
			'label' => __( 'О нас', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/o-nas/' ),
		),
		array(
			'label' => __( 'Программа лечения', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/programma-lecheniya/' ),
		),
		array(
			'label' => __( 'Галерея о доме', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/galereya-o-dome/' ),
		),
		array(
			'label' => __( 'Специалистам', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/specialistam/' ),
		),
		array(
			'label' => __( 'Родственникам', 'shpigovsky' ),
			'url'   => home_url( '/o-centre/rodstvennikam/' ),
		),
	);
}

/**
 * Legal footer column fallback.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_legal_nav_fallback_items() {
	return array(
		array(
			'label' => __( 'Политика конфиденциальности', 'shpigovsky' ),
			'url'   => home_url( '/privacy-policy/' ),
		),
		array(
			'label' => __( 'Пользовательское соглашение', 'shpigovsky' ),
			'url'   => home_url( '/user-agreement/' ),
		),
		array(
			'label' => __( 'Согласие на обработку персональных данных', 'shpigovsky' ),
			'url'   => home_url( '/consent-personal-data/' ),
		),
		array(
			'label' => __( 'Политика Cookie-файлов', 'shpigovsky' ),
			'url'   => home_url( '/cookie-files-policy/' ),
		),
	);
}

/**
 * Render a static nav list with V9 classes.
 *
 * @param array<int, array{label:string,url:string}> $items Nav items.
 * @param string                                    $list_class UL class list.
 * @param string                                    $item_class LI class.
 * @param string                                    $link_class Anchor class.
 */
function shpigovsky_render_static_nav_list( $items, $list_class, $item_class, $link_class ) {
	if ( empty( $items ) ) {
		return;
	}

	echo '<ul class="' . esc_attr( $list_class ) . '">';

	foreach ( $items as $item ) {
		if ( empty( $item['url'] ) || empty( $item['label'] ) ) {
			continue;
		}

		printf(
			'<li class="%1$s"><a class="%2$s" href="%3$s">%4$s</a></li>',
			esc_attr( $item_class ),
			esc_attr( $link_class ),
			esc_url( $item['url'] ),
			esc_html( $item['label'] )
		);
	}

	echo '</ul>';
}

/**
 * Primary menu fallback callback.
 *
 * @param array<string, mixed> $args wp_nav_menu args.
 */
function shpigovsky_primary_nav_fallback( $args ) {
	$list_class = isset( $args['menu_class'] ) ? (string) $args['menu_class'] : 'site-header__nav-list';

	echo '<ul class="' . esc_attr( $list_class ) . '">';

	foreach ( shpigovsky_primary_nav_fallback_items() as $item ) {
		if ( empty( $item['url'] ) || empty( $item['label'] ) ) {
			continue;
		}

		printf(
			'<li class="site-header__nav-item"><a class="site-header__nav-link" href="%1$s">%2$s</a></li>',
			esc_url( $item['url'] ),
			esc_html( $item['label'] )
		);
	}

	printf(
		'<li class="site-header__nav-item site-header__nav-item--search"><button type="button" class="site-header__search" aria-label="%1$s"><i class="fas fa-search" aria-hidden="true"></i></button></li>',
		esc_attr__( 'Открыть поиск', 'shpigovsky' )
	);

	echo '</ul>';
}

/**
 * Offcanvas menu fallback callback.
 *
 * @param array<string, mixed> $args wp_nav_menu args.
 */
function shpigovsky_offcanvas_nav_fallback( $args ) {
	shpigovsky_render_static_nav_list(
		shpigovsky_primary_nav_fallback_items(),
		isset( $args['menu_class'] ) ? (string) $args['menu_class'] : 'offcanvas__nav-list',
		'offcanvas__nav-item',
		'offcanvas__nav-link'
	);
}

/**
 * Footer menu fallback factory.
 *
 * @param array<int, array{label:string,url:string}> $items Items.
 * @return callable
 */
function shpigovsky_footer_nav_fallback_factory( $items ) {
	return static function ( $args ) use ( $items ) {
		shpigovsky_render_static_nav_list(
			$items,
			isset( $args['menu_class'] ) ? (string) $args['menu_class'] : 'site-footer__nav-list',
			'site-footer__nav-item',
			'site-footer__nav-link'
		);
	};
}

/**
 * Append V9 nav item class to menu LI elements.
 *
 * @param string[]             $classes CSS classes.
 * @param WP_Post              $item    Menu item.
 * @param stdClass             $args    Menu args.
 * @param int                  $depth   Depth.
 * @return string[]
 */
function shpigovsky_nav_menu_css_class( $classes, $item, $args, $depth ) {
	if ( ! empty( $args->shpigovsky_item_class ) ) {
		$classes[] = $args->shpigovsky_item_class;
	}

	return $classes;
}
add_filter( 'nav_menu_css_class', 'shpigovsky_nav_menu_css_class', 10, 4 );

/**
 * Append V9 nav link class to menu anchors.
 *
 * @param array<string, string> $atts  Link attributes.
 * @param WP_Post               $item  Menu item.
 * @param stdClass              $args  Menu args.
 * @param int                   $depth Depth.
 * @return array<string, string>
 */
function shpigovsky_nav_menu_link_attributes( $atts, $item, $args, $depth ) {
	if ( ! empty( $args->shpigovsky_link_class ) ) {
		$existing          = isset( $atts['class'] ) ? $atts['class'] . ' ' : '';
		$atts['class']     = trim( $existing . $args->shpigovsky_link_class );
	}

	return $atts;
}
add_filter( 'nav_menu_link_attributes', 'shpigovsky_nav_menu_link_attributes', 10, 4 );
