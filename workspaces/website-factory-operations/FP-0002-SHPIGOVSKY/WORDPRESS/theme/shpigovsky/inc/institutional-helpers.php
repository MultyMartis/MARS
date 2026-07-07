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
