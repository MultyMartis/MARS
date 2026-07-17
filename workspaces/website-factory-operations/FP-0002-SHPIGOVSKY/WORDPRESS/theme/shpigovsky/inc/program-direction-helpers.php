<?php
/**
 * Program direction map — shared Home / services / about program blocks.
 *
 * V9-06E62D: Home direction card text (`.home-rehabilitation-program__direction-text`)
 * is owned by each Treatment Program child page ACF field
 * `treatment_program_short_description` («Мини-описание»).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical program direction page paths under /o-centre/programma-lecheniya/.
 *
 * Body copy for Home cards lives on the child page ACF field — not in this map.
 *
 * @return array<int, array{slug:string,title:string,marker:string,image:string,width:int,height:int,alt:string}>
 */
function shpigovsky_get_program_direction_definitions() {
	return array(
		array(
			'slug'   => 'genotipirovanie',
			'title'  => 'Генотипирование',
			'marker' => '01',
			'image'  => 'img/content/rehabilitation-program/program-genotyping.webp',
			'width'  => 1216,
			'height' => 1632,
			'alt'    => 'Генотипирование',
		),
		array(
			'slug'   => 'neyropsihologicheskaya-korrektsiya',
			'title'  => 'Нейропсихологическая коррекция',
			'marker' => '02',
			'image'  => 'img/content/rehabilitation-program/program-neuropsychology.webp',
			'width'  => 1632,
			'height' => 1216,
			'alt'    => 'Нейропсихологическая коррекция',
		),
		array(
			'slug'   => 'psihokorrektsiya',
			'title'  => 'Психокоррекция',
			'marker' => '03',
			'image'  => 'img/content/rehabilitation-program/program-psychocorrection.webp',
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Психокоррекция',
		),
		array(
			'slug'   => 'kinezioterapiya',
			'title'  => 'Кинезиотерапия',
			'marker' => '04',
			'image'  => 'img/content/rehabilitation-program/program-kinesiotherapy.webp',
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Кинезиотерапия',
		),
	);
}

/**
 * Resolve program direction child page under programma-lecheniya.
 *
 * @param string $slug Child page slug.
 * @return WP_Post|null
 */
function shpigovsky_get_program_direction_page( $slug ) {
	$slug = sanitize_title( (string) $slug );
	$path = 'o-centre/programma-lecheniya/' . $slug;
	$page = get_page_by_path( $path );

	return ( $page instanceof WP_Post ) ? $page : null;
}

/**
 * Resolve permalink for a program direction page under programma-lecheniya.
 *
 * @param string $slug Child page slug.
 * @return string Absolute URL (falls back to expected path when page missing).
 */
function shpigovsky_get_program_direction_url( $slug ) {
	$page = shpigovsky_get_program_direction_page( $slug );

	if ( $page instanceof WP_Post ) {
		$url = get_permalink( $page );
		if ( is_string( $url ) && '' !== $url ) {
			return $url;
		}
	}

	$slug = sanitize_title( (string) $slug );
	$path = 'o-centre/programma-lecheniya/' . $slug;

	return home_url( '/' . $path . '/' );
}

/**
 * Mini-description for a Treatment Program child page (Home direction card text).
 *
 * @param int $page_id Child page ID.
 * @return string Raw HTML-safe fragment (may contain &nbsp;); empty when unset.
 */
function shpigovsky_get_treatment_program_short_description( $page_id ) {
	$page_id = (int) $page_id;
	if ( $page_id <= 0 ) {
		return '';
	}

	$value = '';
	if ( function_exists( 'get_field' ) ) {
		$raw = get_field( 'treatment_program_short_description', $page_id );
		if ( is_string( $raw ) ) {
			$value = $raw;
		}
	}

	if ( '' === $value ) {
		$meta = get_post_meta( $page_id, 'treatment_program_short_description', true );
		if ( is_string( $meta ) ) {
			$value = $meta;
		}
	}

	return is_string( $value ) ? trim( $value ) : '';
}

/**
 * Program direction items with resolved URLs and asset URIs.
 *
 * @param string $variant home|service|about — controls whether body text is included.
 * @return array<int, array{slug:string,title:string,marker:string,title_display:string,url:string,image:string,width:int,height:int,alt:string,text:string,page_id:int}>
 */
function shpigovsky_get_program_direction_items( $variant = 'service' ) {
	$items = array();

	foreach ( shpigovsky_get_program_direction_definitions() as $def ) {
		$page          = shpigovsky_get_program_direction_page( $def['slug'] );
		$page_id       = ( $page instanceof WP_Post ) ? (int) $page->ID : 0;
		$title_display = $def['marker'] . ' — ' . $def['title'];
		$item          = array(
			'slug'          => $def['slug'],
			'title'         => $def['title'],
			'marker'        => $def['marker'],
			'title_display' => $title_display,
			'url'           => shpigovsky_get_program_direction_url( $def['slug'] ),
			'image'         => shpigovsky_asset_uri( $def['image'] ),
			'width'         => (int) $def['width'],
			'height'        => (int) $def['height'],
			'alt'           => $def['alt'],
			'text'          => '',
			'page_id'       => $page_id,
		);

		if ( 'home' === $variant && $page_id > 0 ) {
			$item['text'] = shpigovsky_get_treatment_program_short_description( $page_id );
		}

		$items[] = $item;
	}

	return $items;
}
