<?php
/**
 * Primary navigation walkers — second-level desktop dropdown + offcanvas accordion (PROD-P13).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Desktop walker.
 */
class Shpigovsky_Desktop_Nav_Walker extends Walker_Nav_Menu {

	/**
	 * {@inheritdoc}
	 */
	public function start_lvl( &$output, $depth = 0, $args = null ) {
		$indent = str_repeat( "\t", $depth );
		$output .= "\n{$indent}<ul class=\"site-header__sub-list\">\n";
	}

	/**
	 * {@inheritdoc}
	 */
	public function start_el( &$output, $item, $depth = 0, $args = null, $id = 0 ) {
		$classes      = empty( $item->classes ) ? array() : (array) $item->classes;
		$has_children = in_array( 'menu-item-has-children', $classes, true );
		$li_class     = ( 0 === $depth ) ? 'site-header__nav-item' : 'site-header__sub-item';
		if ( $has_children && 0 === $depth ) {
			$li_class .= ' site-header__nav-item--has-children';
		}

		$output .= '<li class="' . esc_attr( $li_class ) . '">';
		$link_class = ( 0 === $depth ) ? 'site-header__nav-link' : 'site-header__sub-link';
		$title      = apply_filters( 'the_title', $item->title, $item->ID );
		$url        = ! empty( $item->url ) ? $item->url : '';

		$output .= '<a class="' . esc_attr( $link_class ) . '" href="' . esc_url( $url ) . '"' . ( $has_children && 0 === $depth ? ' aria-haspopup="true"' : '' ) . '>' . esc_html( $title ) . '</a>';
	}
}

/**
 * Offcanvas walker with a separate expand control.
 */
class Shpigovsky_Offcanvas_Nav_Walker extends Walker_Nav_Menu {

	/**
	 * Last parent item ID for submenu aria-controls.
	 *
	 * @var int
	 */
	private $current_parent_id = 0;

	/**
	 * {@inheritdoc}
	 */
	public function start_lvl( &$output, $depth = 0, $args = null ) {
		$indent = str_repeat( "\t", $depth );
		$sub_id = 'offcanvas-sub-' . (int) $this->current_parent_id;
		$output .= "\n{$indent}<ul class=\"offcanvas__sub-list\" id=\"" . esc_attr( $sub_id ) . "\" hidden>\n";
	}

	/**
	 * {@inheritdoc}
	 */
	public function start_el( &$output, $item, $depth = 0, $args = null, $id = 0 ) {
		$classes      = empty( $item->classes ) ? array() : (array) $item->classes;
		$has_children = in_array( 'menu-item-has-children', $classes, true ) && 0 === $depth;
		$li_class     = ( 0 === $depth ) ? 'offcanvas__nav-item' : 'offcanvas__sub-item';
		if ( $has_children ) {
			$li_class .= ' offcanvas__nav-item--has-children';
			$this->current_parent_id = (int) $item->ID;
		}

		$output .= '<li class="' . esc_attr( $li_class ) . '">';
		$link_class = ( 0 === $depth ) ? 'offcanvas__nav-link' : 'offcanvas__sub-link';
		$title      = apply_filters( 'the_title', $item->title, $item->ID );
		$url        = ! empty( $item->url ) ? $item->url : '';

		if ( $has_children ) {
			$sub_id = 'offcanvas-sub-' . (int) $item->ID;
			$output .= '<div class="offcanvas__nav-row">';
			$output .= '<a class="' . esc_attr( $link_class ) . '" href="' . esc_url( $url ) . '">' . esc_html( $title ) . '</a>';
			$output .= '<button type="button" class="offcanvas__sub-toggle" data-offcanvas-sub-toggle aria-expanded="false" aria-controls="' . esc_attr( $sub_id ) . '" aria-label="' . esc_attr__( 'Open submenu', 'shpigovsky' ) . '"><span aria-hidden="true">▾</span></button>';
			$output .= '</div>';
		} else {
			$output .= '<a class="' . esc_attr( $link_class ) . '" href="' . esc_url( $url ) . '">' . esc_html( $title ) . '</a>';
		}
	}
}
