<?php
/**
 * Service general (Услуга / service_general) admin parity helpers — V9-06E47.
 *
 * Preferred model: ACF on the service page is the normal content source.
 * PHP emergency helpers exist only to avoid blank critical markup when unseeded.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether current singular service uses service_general stack.
 *
 * @param int|null $post_id Optional post ID.
 * @return bool
 */
function shpigovsky_is_service_general_context( $post_id = null ) {
	if ( null === $post_id ) {
		$post_id = function_exists( 'shpigovsky_get_current_service_id' ) ? shpigovsky_get_current_service_id() : get_the_ID();
	}

	$post_id = absint( $post_id );

	if ( $post_id <= 0 ) {
		return false;
	}

	$variant = function_exists( 'shpigovsky_get_service_layout_variant' )
		? shpigovsky_get_service_layout_variant( $post_id )
		: '';

	return function_exists( 'shpigovsky_is_service_general_variant' )
		? shpigovsky_is_service_general_variant( $variant )
		: in_array( (string) $variant, array( 'service-general', 'alcohol-special' ), true );
}

/**
 * Read service-general ACF field value (raw).
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @return mixed
 */
function shpigovsky_get_general_field_raw( $post_id, $field_name ) {
	$post_id = absint( $post_id );

	if ( $post_id <= 0 || '' === $field_name ) {
		return null;
	}

	if ( function_exists( 'get_field' ) ) {
		$value = get_field( $field_name, $post_id );
		if ( null !== $value && false !== $value && '' !== $value ) {
			return $value;
		}
	}

	$meta = get_post_meta( $post_id, $field_name, true );

	return ( '' === $meta || null === $meta ) ? null : $meta;
}

/**
 * Read service-general scalar string; empty → ''.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_general_field( $post_id, $field_name ) {
	$value = shpigovsky_get_general_field_raw( $post_id, $field_name );

	if ( is_array( $value ) || is_object( $value ) || null === $value || false === $value ) {
		return '';
	}

	return trim( (string) $value );
}

/**
 * Service-general block visibility (missing meta = enabled / default ON).
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Toggle field name.
 * @return bool
 */
function shpigovsky_general_block_enabled( $post_id, $field_name ) {
	$post_id = absint( $post_id );

	if ( $post_id <= 0 || '' === $field_name ) {
		return true;
	}

	if ( ! metadata_exists( 'post', $post_id, $field_name ) ) {
		return true;
	}

	$meta = get_post_meta( $post_id, $field_name, true );

	return (bool) (int) $meta;
}

/**
 * Resolve string with ACF override or emergency fallback.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @param string $fallback Emergency fallback text.
 * @return string
 */
function shpigovsky_general_text( $post_id, $field_name, $fallback ) {
	$value = shpigovsky_get_general_field( $post_id, $field_name );

	return '' !== $value ? $value : (string) $fallback;
}

/**
 * Resolve image URL/alt from ACF image field or theme asset (emergency).
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Image field.
 * @param string $asset_rel Theme-relative asset path.
 * @param string $fallback_alt Alt fallback.
 * @param int    $fallback_w Width.
 * @param int    $fallback_h Height.
 * @return array{url:string,alt:string,width:int,height:int,source:string}
 */
function shpigovsky_general_image_or_asset( $post_id, $field_name, $asset_rel, $fallback_alt, $fallback_w = 0, $fallback_h = 0 ) {
	$acf = shpigovsky_get_general_field_raw( $post_id, $field_name );

	if ( is_numeric( $acf ) ) {
		$attachment_id = (int) $acf;
		$url           = $attachment_id > 0 ? wp_get_attachment_image_url( $attachment_id, 'full' ) : '';
		if ( is_string( $url ) && '' !== $url ) {
			$meta = wp_get_attachment_metadata( $attachment_id );
			$alt  = (string) get_post_meta( $attachment_id, '_wp_attachment_image_alt', true );

			return array(
				'url'    => $url,
				'alt'    => '' !== trim( $alt ) ? $alt : $fallback_alt,
				'width'  => is_array( $meta ) && ! empty( $meta['width'] ) ? (int) $meta['width'] : $fallback_w,
				'height' => is_array( $meta ) && ! empty( $meta['height'] ) ? (int) $meta['height'] : $fallback_h,
				'source' => 'acf:' . $field_name,
			);
		}
	}

	if ( is_array( $acf ) ) {
		$url = function_exists( 'shpigovsky_acf_image_url' ) ? shpigovsky_acf_image_url( $acf ) : ( isset( $acf['url'] ) ? (string) $acf['url'] : '' );
		if ( '' !== $url ) {
			$alt = function_exists( 'shpigovsky_acf_image_alt' ) ? shpigovsky_acf_image_alt( $acf ) : ( isset( $acf['alt'] ) ? trim( (string) $acf['alt'] ) : '' );

			return array(
				'url'    => $url,
				'alt'    => '' !== $alt ? $alt : $fallback_alt,
				'width'  => isset( $acf['width'] ) ? (int) $acf['width'] : $fallback_w,
				'height' => isset( $acf['height'] ) ? (int) $acf['height'] : $fallback_h,
				'source' => 'acf:' . $field_name,
			);
		}
	}

	return array(
		'url'    => function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $asset_rel ) : '',
		'alt'    => $fallback_alt,
		'width'  => $fallback_w,
		'height' => $fallback_h,
		'source' => 'emergency_theme_asset',
	);
}

/**
 * Intro copy: ACF primary; alcohol emergency demo only as safety.
 *
 * @param int $post_id Service ID.
 * @return array{heading:string,highlight:string}
 */
function shpigovsky_get_general_intro_copy( $post_id ) {
	$demo = function_exists( 'shpigovsky_get_v9_alcohol_leaf_intro_copy' )
		? shpigovsky_get_v9_alcohol_leaf_intro_copy()
		: array(
			'heading'   => '',
			'highlight' => '',
		);

	$heading   = shpigovsky_get_general_field( $post_id, 'service_general_intro_heading' );
	$highlight = shpigovsky_get_general_field( $post_id, 'service_general_intro_highlight' );

	if ( '' === $heading && '' === $highlight ) {
		if ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) ) {
			return $demo;
		}

		return array(
			'heading'   => '',
			'highlight' => '',
		);
	}

	return array(
		'heading'   => '' !== $heading ? $heading : (string) ( $demo['heading'] ?? '' ),
		'highlight' => '' !== $highlight ? $highlight : (string) ( $demo['highlight'] ?? '' ),
	);
}

/**
 * Bordered-info subsections from ACF repeater; alcohol emergency if empty on alcohol page.
 *
 * @param int $post_id Service ID.
 * @return array<int, array{heading:string,text:string}>
 */
function shpigovsky_get_general_bordered_info_items( $post_id ) {
	$rows = shpigovsky_get_general_field_raw( $post_id, 'service_general_bordered_info_items' );
	$out  = array();

	if ( is_array( $rows ) && function_exists( 'shpigovsky_has_meaningful_repeater_rows' ) && shpigovsky_has_meaningful_repeater_rows( $rows, array( 'heading', 'text' ) ) ) {
		foreach ( $rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$heading = isset( $row['heading'] ) ? trim( (string) $row['heading'] ) : '';
			$text    = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $heading && '' === $text ) {
				continue;
			}
			$out[] = array(
				'heading' => $heading,
				'text'    => $text,
			);
		}

		return $out;
	}

	if ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) && function_exists( 'shpigovsky_get_v9_alcohol_bordered_info_subsections' ) ) {
		return shpigovsky_get_v9_alcohol_bordered_info_subsections();
	}

	return array();
}

/**
 * Signs copy from ACF; alcohol emergency if empty on alcohol page.
 *
 * @param int $post_id Service ID.
 * @return array{heading:string,intro:string,items:string[],editorial:string}|null
 */
function shpigovsky_get_general_signs_copy( $post_id ) {
	$heading   = shpigovsky_get_general_field( $post_id, 'service_general_signs_heading' );
	$intro     = shpigovsky_get_general_field( $post_id, 'service_general_signs_intro' );
	$editorial = shpigovsky_get_general_field( $post_id, 'service_general_signs_editorial' );
	if ( function_exists( 'shpigovsky_is_demo_or_lorem_placeholder_copy' ) && shpigovsky_is_demo_or_lorem_placeholder_copy( $editorial ) ) {
		$editorial = '';
	}
	$rows      = shpigovsky_get_general_field_raw( $post_id, 'service_general_signs_items' );
	$items     = array();

	if ( is_array( $rows ) ) {
		foreach ( $rows as $row ) {
			if ( is_array( $row ) ) {
				$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			} else {
				$text = is_scalar( $row ) ? trim( (string) $row ) : '';
			}
			if ( '' !== $text ) {
				$items[] = $text;
			}
		}
	}

	if ( '' !== $heading || '' !== $intro || ! empty( $items ) || '' !== $editorial ) {
		$demo = function_exists( 'shpigovsky_get_v9_alcohol_signs_copy' ) ? shpigovsky_get_v9_alcohol_signs_copy() : array();

		return array(
			'heading'   => '' !== $heading ? $heading : (string) ( $demo['heading'] ?? __( 'Признаки зависимости', 'shpigovsky' ) ),
			'intro'     => $intro,
			'items'     => ! empty( $items ) ? $items : ( isset( $demo['items'] ) && is_array( $demo['items'] ) ? $demo['items'] : array() ),
			'editorial' => $editorial,
		);
	}

	if ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) && function_exists( 'shpigovsky_get_v9_alcohol_signs_copy' ) ) {
		return shpigovsky_get_v9_alcohol_signs_copy();
	}

	return null;
}

/**
 * Approach copy from ACF; alcohol emergency if empty on alcohol page.
 *
 * @param int $post_id Service ID.
 * @return array{heading:string,highlight:string,intro:string,cards:array<int,array{title:string,text:string}>,more_label:string,more_url:string}|null
 */
function shpigovsky_get_general_approach_copy( $post_id ) {
	$demo = function_exists( 'shpigovsky_get_v9_alcohol_leaf_approach_copy' )
		? shpigovsky_get_v9_alcohol_leaf_approach_copy()
		: array(
			'heading'   => '',
			'highlight' => '',
			'intro'     => '',
			'cards'     => array(),
		);

	$heading   = shpigovsky_get_general_field( $post_id, 'service_general_approach_heading' );
	$highlight = shpigovsky_get_general_field( $post_id, 'service_general_approach_highlight' );
	$intro     = shpigovsky_get_general_field( $post_id, 'service_general_approach_intro' );
	$more_label = shpigovsky_get_general_field( $post_id, 'service_general_approach_more_label' );
	$more_url   = shpigovsky_get_general_field( $post_id, 'service_general_approach_more_url' );
	$rows       = shpigovsky_get_general_field_raw( $post_id, 'service_general_approach_cards' );
	$cards      = array();

	if ( is_array( $rows ) && function_exists( 'shpigovsky_has_meaningful_repeater_rows' ) && shpigovsky_has_meaningful_repeater_rows( $rows, array( 'title', 'text' ) ) ) {
		foreach ( $rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
			$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $title && '' === $text ) {
				continue;
			}
			$cards[] = array(
				'title' => $title,
				'text'  => function_exists( 'shpigovsky_sanitize_approach_card_text' )
					? shpigovsky_sanitize_approach_card_text( $title, $text )
					: $text,
			);
		}
	}

	$has_acf = '' !== $heading || '' !== $highlight || '' !== $intro || ! empty( $cards );

	if ( ! $has_acf ) {
		if ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) ) {
			$demo['more_label'] = __( 'подробнее', 'shpigovsky' );
			$demo['more_url']   = home_url( '/o-centre/programma-lecheniya/' );
			return $demo;
		}

		return null;
	}

	return array(
		'heading'    => '' !== $heading ? $heading : (string) ( $demo['heading'] ?? '' ),
		'highlight'  => '' !== $highlight ? $highlight : (string) ( $demo['highlight'] ?? '' ),
		'intro'      => '' !== $intro ? $intro : (string) ( $demo['intro'] ?? '' ),
		'cards'      => ! empty( $cards ) ? $cards : ( isset( $demo['cards'] ) && is_array( $demo['cards'] ) ? $demo['cards'] : array() ),
		'more_label' => '' !== $more_label ? $more_label : __( 'подробнее', 'shpigovsky' ),
		'more_url'   => '' !== $more_url ? $more_url : home_url( '/o-centre/programma-lecheniya/' ),
	);
}

/**
 * Program text chrome from ACF; alcohol emergency demos if empty on alcohol page.
 *
 * @param int $post_id Service ID.
 * @return array{heading:string,more_label:string,lead:string,intros:string[]}
 */
function shpigovsky_get_general_program_copy( $post_id ) {
	$demo = function_exists( 'shpigovsky_get_v9_alcohol_leaf_program_demo_copy' )
		? shpigovsky_get_v9_alcohol_leaf_program_demo_copy()
		: array(
			'lead'   => '',
			'intro'  => '',
			'intro2' => '',
		);

	$heading    = shpigovsky_get_general_field( $post_id, 'service_general_program_heading' );
	$more_label = shpigovsky_get_general_field( $post_id, 'service_general_program_more_label' );
	$lead       = shpigovsky_get_general_field( $post_id, 'service_general_program_lead' );
	if ( function_exists( 'shpigovsky_is_demo_or_lorem_placeholder_copy' ) && shpigovsky_is_demo_or_lorem_placeholder_copy( $lead ) ) {
		$lead = '';
	}
	$rows       = shpigovsky_get_general_field_raw( $post_id, 'service_general_program_intro_items' );
	$intros     = array();

	if ( is_array( $rows ) ) {
		foreach ( $rows as $row ) {
			$text = is_array( $row ) && isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' !== $text && function_exists( 'shpigovsky_is_demo_or_lorem_placeholder_copy' ) && shpigovsky_is_demo_or_lorem_placeholder_copy( $text ) ) {
				continue;
			}
			if ( '' !== $text ) {
				$intros[] = $text;
			}
		}
	}

	$use_emergency = '' === $heading && '' === $lead && empty( $intros )
		&& function_exists( 'shpigovsky_is_known_alcohol_service_page' )
		&& shpigovsky_is_known_alcohol_service_page( $post_id );

	if ( $use_emergency ) {
		$intros = array_values(
			array_filter(
				array(
					(string) ( $demo['intro'] ?? '' ),
					(string) ( $demo['intro2'] ?? '' ),
				)
			)
		);
		$lead = (string) ( $demo['lead'] ?? '' );
	}

	return array(
		'heading'    => '' !== $heading ? $heading : __( 'Наша программа включает 4 направления', 'shpigovsky' ),
		'more_label' => '' !== $more_label ? $more_label : __( 'подробнее', 'shpigovsky' ),
		'lead'       => $lead,
		'intros'     => $intros,
	);
}

/**
 * Stages copy from ACF; alcohol emergency if empty on alcohol page.
 *
 * @param int $post_id Service ID.
 * @return array{heading:string,lead:string,steps:array<int,array{title:string,text:string}>,support_heading:string,support_items:string[]}|null
 */
function shpigovsky_get_general_stages_copy( $post_id ) {
	$demo = function_exists( 'shpigovsky_get_v9_alcohol_leaf_stages_copy' )
		? shpigovsky_get_v9_alcohol_leaf_stages_copy()
		: null;

	$heading         = shpigovsky_get_general_field( $post_id, 'service_general_stages_heading' );
	$lead            = shpigovsky_get_general_field( $post_id, 'service_general_stages_lead' );
	$support_heading = shpigovsky_get_general_field( $post_id, 'service_general_stages_support_heading' );
	$step_rows       = shpigovsky_get_general_field_raw( $post_id, 'service_general_stages_items' );
	$support_rows    = shpigovsky_get_general_field_raw( $post_id, 'service_general_stages_support_items' );
	$steps           = array();
	$support_items   = array();

	if ( is_array( $step_rows ) ) {
		foreach ( $step_rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$enabled = ! isset( $row['enabled'] ) || (bool) $row['enabled'];
			if ( ! $enabled ) {
				continue;
			}
			$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
			$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $title && '' === $text ) {
				continue;
			}
			$steps[] = array(
				'title' => $title,
				'text'  => $text,
			);
		}
	}

	if ( is_array( $support_rows ) ) {
		foreach ( $support_rows as $row ) {
			$text = is_array( $row ) && isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' !== $text ) {
				$support_items[] = $text;
			}
		}
	}

	$has_acf = '' !== $heading || '' !== $lead || ! empty( $steps ) || '' !== $support_heading || ! empty( $support_items );

	if ( ! $has_acf ) {
		if ( $demo && function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) ) {
			return $demo;
		}

		return null;
	}

	return array(
		'heading'         => '' !== $heading ? $heading : (string) ( $demo['heading'] ?? '' ),
		'lead'            => '' !== $lead ? $lead : (string) ( $demo['lead'] ?? '' ),
		'steps'           => ! empty( $steps ) ? $steps : ( isset( $demo['steps'] ) && is_array( $demo['steps'] ) ? $demo['steps'] : array() ),
		'support_heading' => '' !== $support_heading ? $support_heading : (string) ( $demo['support_heading'] ?? '' ),
		'support_items'   => ! empty( $support_items ) ? $support_items : ( isset( $demo['support_items'] ) && is_array( $demo['support_items'] ) ? $demo['support_items'] : array() ),
	);
}

/**
 * FAQ items from ACF; alcohol emergency if empty on alcohol page.
 *
 * Answer textarea: paragraphs separated by blank lines.
 *
 * @param int $post_id Service ID.
 * @return array<int, array{question:string,answers:string[]}>
 */
function shpigovsky_get_general_faq_items( $post_id ) {
	$rows = shpigovsky_get_general_field_raw( $post_id, 'service_general_faq_items' );
	$out  = array();

	if ( is_array( $rows ) && function_exists( 'shpigovsky_has_meaningful_repeater_rows' ) && shpigovsky_has_meaningful_repeater_rows( $rows, array( 'question', 'answer' ) ) ) {
		foreach ( $rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$question = isset( $row['question'] ) ? trim( (string) $row['question'] ) : '';
			$answer   = isset( $row['answer'] ) ? trim( (string) $row['answer'] ) : '';
			if ( '' === $question && '' === $answer ) {
				continue;
			}
			if ( function_exists( 'shpigovsky_is_demo_or_lorem_placeholder_copy' ) && shpigovsky_is_demo_or_lorem_placeholder_copy( $answer ) ) {
				continue;
			}
			$answers = preg_split( "/\n\s*\n/", $answer ) ?: array();
			$answers = array_values(
				array_filter(
					array_map(
						static function ( $part ) {
							return trim( (string) $part );
						},
						$answers
					)
				)
			);
			if ( empty( $answers ) && '' !== $answer ) {
				$answers = array( $answer );
			}
			$out[] = array(
				'question' => $question,
				'answers'  => $answers,
			);
		}

		return $out;
	}

	if ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) && function_exists( 'shpigovsky_get_v9_alcohol_leaf_faq_items' ) ) {
		return shpigovsky_get_v9_alcohol_leaf_faq_items();
	}

	return array();
}
