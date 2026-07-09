<?php
/**
 * Institutional page ACF read helpers — V9-06E7 hero integration.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read a scalar institutional ACF field safely.
 *
 * @param int    $page_id    Page ID.
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_institutional_field( $page_id, $field_name ) {
	if ( ! function_exists( 'get_field' ) || $page_id <= 0 ) {
		return '';
	}

	$value = get_field( $field_name, $page_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Build institutional hero copy with static V9 fallbacks.
 *
 * @param int $page_id Page ID.
 * @return array{title_id:string,eyebrow:string,title:string,lead:string,cta_label:string,cta_source:string,image:array{url:string,alt:string,width:int,height:int}}
 */
function shpigovsky_get_institutional_hero_context( $page_id ) {
	$slug       = get_post_field( 'post_name', $page_id );
	$slug       = is_string( $slug ) ? $slug : '';
	$title_id   = '' !== $slug ? $slug . '-hero-title' : 'institutional-hero-title';
	$eyebrow    = shpigovsky_get_institutional_field( $page_id, 'hero_eyebrow' );
	$title      = shpigovsky_get_institutional_field( $page_id, 'hero_title_override' );
	$lead       = shpigovsky_get_institutional_field( $page_id, 'hero_lead' );
	$cta_source = '' !== $slug ? $slug . '-hero' : 'institutional-hero';

	if ( '' === $eyebrow ) {
		$eyebrow = __( 'О центре', 'shpigovsky' );
	}

	if ( '' === $title ) {
		$title = get_the_title( $page_id );
	}

	$cta_label = shpigovsky_get_local_hero_cta_label( $page_id );

	return array(
		'title_id'   => $title_id,
		'eyebrow'    => $eyebrow,
		'title'      => is_string( $title ) ? trim( $title ) : '',
		'lead'       => $lead,
		'cta_label'  => $cta_label,
		'cta_source' => $cta_source,
		'image'      => shpigovsky_get_institutional_hero_image( $page_id ),
	);
}

/**
 * Whether the current request is the /o-centre/ hub page.
 *
 * @param int $page_id Optional page ID.
 * @return bool
 */
function shpigovsky_is_about_hub_page( $page_id = 0 ) {
	if ( $page_id <= 0 ) {
		$page_id = (int) get_queried_object_id();
	}

	$slug = get_post_field( 'post_name', $page_id );

	return 'o-centre' === $slug;
}

/**
 * Breadcrumb trail for about hub page.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_about_hub_breadcrumb_trail() {
	return array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'О центре', 'shpigovsky' ),
			'url'   => '',
		),
	);
}

/**
 * Read repeater rows from ACF with static fallback rows.
 *
 * @param int    $page_id      Page ID.
 * @param string $field_name   Field name.
 * @param array  $static_rows  Fallback rows.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_institutional_repeater_or_static( $page_id, $field_name, array $static_rows ) {
	if ( function_exists( 'get_field' ) && $page_id > 0 ) {
		$rows = get_field( $field_name, $page_id );

		if ( is_array( $rows ) && ! empty( $rows ) ) {
			return $rows;
		}
	}

	return $static_rows;
}

/**
 * About hub narrative context (ACF with V9 fallback).
 *
 * @param int $page_id Page ID.
 * @return array{heading:string,lead:string,paragraphs:array<int,string>}
 */
function shpigovsky_get_about_narrative_context( $page_id ) {
	$static = shpigovsky_get_v9_about_narrative_copy();
	$heading = shpigovsky_get_institutional_field( $page_id, 'about_narrative_heading' );
	$lead    = shpigovsky_get_institutional_field( $page_id, 'about_narrative_lead' );

	if ( '' === $heading ) {
		$heading = $static['heading'];
	}

	if ( '' === $lead ) {
		$lead = $static['lead'];
	}

	$paragraphs = array();
	$rows       = shpigovsky_get_institutional_repeater_or_static( $page_id, 'about_narrative_paragraphs', array() );

	if ( ! empty( $rows ) ) {
		foreach ( $rows as $row ) {
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';

			if ( '' !== $text ) {
				$paragraphs[] = $text;
			}
		}
	}

	if ( empty( $paragraphs ) ) {
		$paragraphs = $static['paragraphs'];
	}

	return array(
		'heading'    => $heading,
		'lead'       => $lead,
		'paragraphs' => $paragraphs,
	);
}

/**
 * About hub who-we-treat context.
 *
 * @param int $page_id Page ID.
 * @return array<string,mixed>
 */
function shpigovsky_get_about_who_we_treat_context( $page_id ) {
	$static = shpigovsky_get_v9_about_who_we_treat_copy();

	$heading = shpigovsky_get_institutional_field( $page_id, 'about_who_treat_heading' );
	$intro   = shpigovsky_get_institutional_field( $page_id, 'about_who_treat_intro' );
	$lead    = shpigovsky_get_institutional_field( $page_id, 'about_who_treat_lead' );
	$callout = shpigovsky_get_institutional_field( $page_id, 'about_who_treat_callout' );

	$spectrum = shpigovsky_get_institutional_repeater_or_static( $page_id, 'about_who_treat_spectrum', $static['spectrum'] );
	$cards    = shpigovsky_get_institutional_repeater_or_static( $page_id, 'about_who_treat_cards', $static['cards'] );

	return array(
		'heading'  => '' !== $heading ? $heading : $static['heading'],
		'intro'    => '' !== $intro ? $intro : $static['intro'],
		'lead'     => '' !== $lead ? $lead : $static['lead'],
		'spectrum' => $spectrum,
		'callout'  => '' !== $callout ? $callout : $static['callout'],
		'cards'    => $cards,
	);
}

/**
 * About hub approach band context.
 *
 * @param int $page_id Page ID.
 * @return array{heading:string,highlight:string,intro:string,link_url:string,link_label:string}
 */
function shpigovsky_get_about_approach_context( $page_id ) {
	$static = shpigovsky_get_v9_about_approach_copy();

	$heading   = shpigovsky_get_institutional_field( $page_id, 'about_approach_heading' );
	$highlight = shpigovsky_get_institutional_field( $page_id, 'about_approach_highlight' );
	$intro     = shpigovsky_get_institutional_field( $page_id, 'about_approach_intro' );

	return array(
		'heading'    => '' !== $heading ? $heading : $static['heading'],
		'highlight'  => '' !== $highlight ? $highlight : $static['highlight'],
		'intro'      => '' !== $intro ? $intro : $static['intro'],
		'link_url'   => home_url( '/o-centre/programma-lecheniya/' ),
		'link_label' => __( 'подробнее', 'shpigovsky' ),
	);
}

/**
 * About hub program section context.
 *
 * @param int $page_id Page ID.
 * @return array<string,mixed>
 */
function shpigovsky_get_about_program_context( $page_id ) {
	$static = shpigovsky_get_v9_about_program_copy();

	$heading = shpigovsky_get_institutional_field( $page_id, 'about_program_heading' );
	$lead    = shpigovsky_get_institutional_field( $page_id, 'about_program_lead' );
	$intro   = shpigovsky_get_institutional_field( $page_id, 'about_program_intro' );
	$intro2  = shpigovsky_get_institutional_field( $page_id, 'about_program_intro2' );

	$items = shpigovsky_get_institutional_repeater_or_static( $page_id, 'about_program_items', array() );

	if ( empty( $items ) ) {
		$items = $static['items'];
	} else {
		$normalized = array();

		foreach ( $items as $index => $row ) {
			$fallback = isset( $static['items'][ $index ] ) ? $static['items'][ $index ] : array();
			$image    = isset( $row['image'] ) && is_array( $row['image'] ) ? $row['image'] : array();
			$asset    = isset( $fallback['image'] ) ? (string) $fallback['image'] : '';

			$normalized[] = array(
				'title'  => isset( $row['title'] ) && '' !== trim( (string) $row['title'] ) ? trim( (string) $row['title'] ) : ( isset( $fallback['title'] ) ? $fallback['title'] : '' ),
				'image'  => ! empty( $image['url'] ) ? (string) $image['url'] : shpigovsky_asset_uri( $asset ),
				'width'  => ! empty( $image['width'] ) ? (int) $image['width'] : ( isset( $fallback['width'] ) ? (int) $fallback['width'] : 0 ),
				'height' => ! empty( $image['height'] ) ? (int) $image['height'] : ( isset( $fallback['height'] ) ? (int) $fallback['height'] : 0 ),
				'alt'    => ! empty( $image['alt'] ) ? (string) $image['alt'] : ( isset( $fallback['alt'] ) ? (string) $fallback['alt'] : '' ),
			);
		}

		$items = $normalized;
	}

	if ( ! empty( $items ) && isset( $items[0]['image'] ) && false === strpos( (string) $items[0]['image'], '://' ) ) {
		foreach ( $items as $index => $item ) {
			$items[ $index ]['image'] = shpigovsky_asset_uri( (string) $item['image'] );
		}
	}

	return array(
		'heading'  => '' !== $heading ? $heading : $static['heading'],
		'lead'     => '' !== $lead ? $lead : $static['lead'],
		'intro'    => '' !== $intro ? $intro : $static['intro'],
		'intro2'   => '' !== $intro2 ? $intro2 : $static['intro2'],
		'items'    => $items,
		'link_url' => home_url( '/o-centre/programma-lecheniya/' ),
	);
}

/**
 * Guest CTA band context for about hub.
 *
 * @param string $source CTA source slug.
 * @return array<string,string>
 */
function shpigovsky_get_about_guest_cta_band( $source = 'o-centre-cta-1' ) {
	$static = shpigovsky_get_v9_about_guest_cta_copy();
	$phone  = shpigovsky_get_site_option( 'phone_primary' );
	$phone  = '' !== $phone ? $phone : '8 (925) 183-64-64';

	return array(
		'title'          => shpigovsky_get_cta_band_default_title( $static['title'] ),
		'subtitle'       => shpigovsky_get_cta_band_default_subtitle( $static['subtitle'] ),
		'phone'          => $phone,
		'phone_hint'     => '',
		'button_label'   => shpigovsky_get_cta_band_default_button_label( $static['button_label'] ),
		'source'         => $source,
		'section_id'     => $source,
		'heading_id'     => $source . '-heading',
		'heading_text'   => shpigovsky_get_cta_band_default_title( $static['title'] ),
		'wrap_section'   => true,
		'wrap_container' => false,
		'button_first'   => false,
		'margin_flush'   => false,
	);
}

/**
 * Infrastructure narrative context for about hub.
 *
 * @param int $page_id Page ID.
 * @return array<string,mixed>
 */
function shpigovsky_get_about_infrastructure_context( $page_id ) {
	$static_copy = shpigovsky_get_v9_about_infrastructure_copy();
	$galleries   = shpigovsky_get_v9_about_infrastructure_gallery_sets();
	$acf_rows    = shpigovsky_get_institutional_repeater_or_static( $page_id, 'infrastructure_g0_g5', array() );

	$groups = array();

	foreach ( array( 'g0', 'g1', 'g2', 'g3', 'g4' ) as $index => $group_key ) {
		$row          = isset( $acf_rows[ $index ] ) && is_array( $acf_rows[ $index ] ) ? $acf_rows[ $index ] : array();
		$static_group = isset( $static_copy[ $group_key ] ) ? $static_copy[ $group_key ] : array();
		$heading      = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$lead         = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
		$bullet       = isset( $static_group['bullet'] ) ? (string) $static_group['bullet'] : '';

		if ( 'g0' === $group_key ) {
			$groups[ $group_key ] = array(
				'heading' => '' !== $heading ? $heading : ( isset( $static_group['heading'] ) ? $static_group['heading'] : '' ),
				'lead'    => '' !== $lead ? $lead : ( isset( $static_group['lead'] ) ? $static_group['lead'] : '' ),
			);
		} else {
			if ( '' !== $lead ) {
				$bullet = $lead;
			}

			$groups[ $group_key ] = array(
				'bullet'   => $bullet,
				'gallery'  => isset( $galleries[ $group_key ] ) ? $galleries[ $group_key ] : array(),
			);
		}
	}

	return array(
		'groups'        => $groups,
		'comfort_gallery' => isset( $galleries['g5'] ) ? $galleries['g5'] : array(),
		'fancybox_group'  => 'o-centre-infrastructure',
	);
}

/**
 * Add page-o-centre body class on about hub and children.
 *
 * @param array<int,string> $classes Body classes.
 * @return array<int,string>
 */
function shpigovsky_institutional_body_class( $classes ) {
	if ( ! is_page() ) {
		return $classes;
	}

	$page_id = (int) get_queried_object_id();
	$parent  = (int) wp_get_post_parent_id( $page_id );
	$slug    = get_post_field( 'post_name', $page_id );

	if ( 'o-centre' === $slug || 11 === $parent ) {
		$classes[] = 'page-o-centre';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_institutional_body_class' );
