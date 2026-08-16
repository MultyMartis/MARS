<?php
/**
 * Service section (Раздел / subdivision) admin parity helpers — V9-06E46.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether current singular service uses subdivision/section stack.
 *
 * @param int|null $post_id Optional post ID.
 * @return bool
 */
function shpigovsky_is_service_section_context( $post_id = null ) {
	if ( null === $post_id ) {
		$post_id = function_exists( 'shpigovsky_get_current_service_id' ) ? shpigovsky_get_current_service_id() : get_the_ID();
	}

	$post_id = absint( $post_id );

	if ( $post_id <= 0 || ! is_singular( 'service' ) ) {
		return false;
	}

	$variant = function_exists( 'shpigovsky_get_service_layout_variant' )
		? shpigovsky_get_service_layout_variant( $post_id )
		: '';

	return 'subdivision' === $variant;
}

/**
 * Read section ACF field value (raw).
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @return mixed
 */
function shpigovsky_get_section_field_raw( $post_id, $field_name ) {
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
 * Read section scalar string; empty → ''.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_section_field( $post_id, $field_name ) {
	$value = shpigovsky_get_section_field_raw( $post_id, $field_name );

	if ( is_array( $value ) || is_object( $value ) || null === $value || false === $value ) {
		return '';
	}

	return trim( (string) $value );
}

/**
 * Section block visibility (missing meta = enabled / default ON).
 *
 * Important: ACF true_false returns boolean false when OFF — do not treat that as unset.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Toggle field name.
 * @return bool
 */
function shpigovsky_section_block_enabled( $post_id, $field_name ) {
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
 * Resolve string from ACF; optional emergency reserve when empty.
 *
 * V9-06E50: normal content source is ACF admin fields (seeded demo / editor copy).
 * Pass '' as $fallback for normal empty-safe rendering (hide optional text).
 * Non-empty $fallback is emergency/legacy only — not a normal demo content model.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Field name.
 * @param string $fallback Emergency reserve text (prefer '').
 * @return string
 */
function shpigovsky_section_text( $post_id, $field_name, $fallback = '' ) {
	$value = shpigovsky_get_section_field( $post_id, $field_name );

	return '' !== $value ? $value : (string) $fallback;
}

/**
 * Resolve first non-empty section image among preferred field names, else theme asset.
 *
 * @param int               $post_id Service ID.
 * @param array<int,string> $field_names Preferred field names (first wins).
 * @param string            $asset_rel Theme-relative asset path.
 * @param string            $fallback_alt Alt fallback.
 * @param int               $fallback_w Width.
 * @param int               $fallback_h Height.
 * @return array{url:string,alt:string,width:int,height:int,source:string}
 */
function shpigovsky_section_image_or_asset_prefer( $post_id, array $field_names, $asset_rel, $fallback_alt, $fallback_w = 0, $fallback_h = 0 ) {
	foreach ( $field_names as $field_name ) {
		$acf = shpigovsky_get_section_field_raw( $post_id, $field_name );
		if ( null === $acf || false === $acf || '' === $acf || array() === $acf ) {
			continue;
		}
		if ( is_numeric( $acf ) && (int) $acf <= 0 ) {
			continue;
		}

		$resolved = shpigovsky_section_image_or_asset( $post_id, $field_name, $asset_rel, $fallback_alt, $fallback_w, $fallback_h );
		$theme_url = function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $asset_rel ) : '';
		if ( ! empty( $resolved['url'] ) && ( '' === $theme_url || $resolved['url'] !== $theme_url ) ) {
			$resolved['source'] = 'acf:' . $field_name;
			return $resolved;
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
 * Resolve image URL/alt from ACF image field or theme asset.
 *
 * @param int    $post_id Service ID.
 * @param string $field_name Image field.
 * @param string $asset_rel Theme-relative asset path.
 * @param string $fallback_alt Alt fallback.
 * @param int    $fallback_w Width.
 * @param int    $fallback_h Height.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_section_image_or_asset( $post_id, $field_name, $asset_rel, $fallback_alt, $fallback_w = 0, $fallback_h = 0 ) {
	$acf = shpigovsky_get_section_field_raw( $post_id, $field_name );

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
			);
		}
	}

	return array(
		'url'    => function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $asset_rel ) : '',
		'alt'    => $fallback_alt,
		'width'  => $fallback_w,
		'height' => $fallback_h,
	);
}

/**
 * EMERGENCY ONLY — nature cards reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_section_nature_fallback_cards() {
	return array(
		array(
			'title' => __( 'Физиологическое проявление', 'shpigovsky' ),
			'text'  => __( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit,', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Поведенческое проявление', 'shpigovsky' ),
			'text'  => __( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit,', 'shpigovsky' ),
		),
	);
}

/**
 * EMERGENCY ONLY — nature text-blocks reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 *
 * @return array<int, array{heading:string,text:string,link_label:string,link_url:string,after_text:string}>
 */
function shpigovsky_get_section_nature_text_blocks_fallback() {
	return array(
		array(
			'heading'    => __( 'Нейробиология', 'shpigovsky' ),
			'text'       => __( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tem', 'shpigovsky' ),
			'link_label' => '',
			'link_url'   => '',
			'after_text' => '',
		),
		array(
			'heading'    => __( 'Генотипирование', 'shpigovsky' ),
			'text'       => __( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.', 'shpigovsky' ),
			'link_label' => __( 'Подробнее о генотипировании', 'shpigovsky' ),
			'link_url'   => home_url( '/uslugi/zavisimosti/profilakticheskiy-analiz/' ),
			'after_text' => __( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.', 'shpigovsky' ),
		),
	);
}

/**
 * Resolve nature text blocks: repeater → legacy pair fields → empty (no demo inject).
 *
 * V9-06E50: hardcoded demo fallback is not a normal content source.
 *
 * @param int $post_id Service ID.
 * @return array<int, array{heading:string,text:string,link_label:string,link_url:string,after_text:string}>
 */
function shpigovsky_get_section_nature_text_blocks( $post_id ) {
	$rows = shpigovsky_section_normalize_nature_text_blocks(
		shpigovsky_get_section_field_raw( $post_id, 'section_nature_text_blocks' )
	);

	if ( ! empty( $rows ) ) {
		return $rows;
	}

	$legacy = array();
	$neuro_heading = shpigovsky_get_section_field( $post_id, 'section_nature_neurobiology_heading' );
	$neuro_text    = shpigovsky_get_section_field( $post_id, 'section_nature_neurobiology_text' );
	if ( '' !== $neuro_heading || '' !== $neuro_text ) {
		$legacy[] = array(
			'heading'    => $neuro_heading,
			'text'       => $neuro_text,
			'link_label' => '',
			'link_url'   => '',
			'after_text' => '',
		);
	}

	$geno_heading = shpigovsky_get_section_field( $post_id, 'section_nature_genotyping_heading' );
	$geno_text    = shpigovsky_get_section_field( $post_id, 'section_nature_genotyping_text' );
	$geno_label   = shpigovsky_get_section_field( $post_id, 'section_nature_genotyping_link_label' );
	$geno_url     = shpigovsky_get_section_field( $post_id, 'section_nature_genotyping_link_url' );
	$geno_after   = shpigovsky_get_section_field( $post_id, 'section_nature_genotyping_after_text' );
	if ( '' !== $geno_heading || '' !== $geno_text || '' !== $geno_label || '' !== $geno_after ) {
		$legacy[] = array(
			'heading'    => $geno_heading,
			'text'       => $geno_text,
			'link_label' => $geno_label,
			'link_url'   => $geno_url,
			'after_text' => $geno_after,
		);
	}

	return $legacy;
}

/**
 * Normalize nature text-block repeater rows.
 *
 * @param mixed $rows Raw repeater.
 * @return array<int, array{heading:string,text:string,link_label:string,link_url:string,after_text:string}>
 */
function shpigovsky_section_normalize_nature_text_blocks( $rows ) {
	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$out = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$heading    = isset( $row['heading'] ) ? trim( (string) $row['heading'] ) : '';
		$text       = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
		$link_label = isset( $row['link_label'] ) ? trim( (string) $row['link_label'] ) : '';
		$link_url   = isset( $row['link_url'] ) ? trim( (string) $row['link_url'] ) : '';
		$after_text = isset( $row['after_text'] ) ? trim( (string) $row['after_text'] ) : '';

		if ( '' === $heading && '' === $text && '' === $link_label && '' === $after_text ) {
			continue;
		}

		$out[] = array(
			'heading'    => $heading,
			'text'       => $text,
			'link_label' => $link_label,
			'link_url'   => $link_url,
			'after_text' => $after_text,
		);
	}

	return $out;
}

/**
 * Whether a repeater value has at least one meaningful row.
 *
 * Empty rows do not count. Partial rows count when any of $keys is non-empty
 * (or any non-empty scalar cell when $keys is empty).
 *
 * @param mixed             $rows Repeater rows.
 * @param array<int,string> $keys Preferred cell keys to inspect (e.g. array( 'text' )).
 * @return bool
 */
function shpigovsky_has_meaningful_repeater_rows( $rows, $keys = array() ) {
	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return false;
	}

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			if ( is_string( $row ) && '' !== trim( $row ) ) {
				return true;
			}
			continue;
		}

		if ( ! empty( $keys ) ) {
			foreach ( $keys as $key ) {
				if ( isset( $row[ $key ] ) && '' !== trim( (string) $row[ $key ] ) ) {
					return true;
				}
			}
			continue;
		}

		foreach ( $row as $cell ) {
			if ( is_scalar( $cell ) && '' !== trim( (string) $cell ) ) {
				return true;
			}
		}
	}

	return false;
}

/**
 * Whether program intro repeater is under editor control (field key present).
 *
 * Once the repeater has been registered on the post, empty/cleared rows must
 * NOT fall back to legacy intro scalars (that looked like demo fighting edits).
 *
 * @param int $post_id Service ID.
 * @return bool
 */
function shpigovsky_section_program_intro_repeater_is_managed( $post_id ) {
	$post_id = absint( $post_id );

	return $post_id > 0 && metadata_exists( 'post', $post_id, '_section_program_intro_items' );
}

/**
 * Normalize raw program intro repeater value to rows array or null (unusable).
 *
 * @param mixed $raw Raw ACF/meta value.
 * @return array<int,mixed>|null
 */
function shpigovsky_section_program_intro_rows_normalize( $raw ) {
	if ( is_array( $raw ) ) {
		return $raw;
	}

	// Explicit empty count after clear (ACF may expose meta "0").
	if ( is_numeric( $raw ) && (int) $raw === 0 ) {
		return array();
	}

	return null;
}

/**
 * Program intro paragraphs: meaningful repeater → legacy scalars → empty (no demo inject).
 *
 * V9-06E50: user/ACF content wins; empty managed fields do not inject hardcoded demo.
 *
 * @param int $post_id Service ID.
 * @return array<int, string>
 */
function shpigovsky_get_section_program_intro_items( $post_id ) {
	$post_id = absint( $post_id );
	$raw     = shpigovsky_get_section_field_raw( $post_id, 'section_program_intro_items' );
	$rows    = shpigovsky_section_program_intro_rows_normalize( $raw );
	$out     = array();

	if ( is_array( $rows ) ) {
		foreach ( $rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' !== $text ) {
				$out[] = $text;
			}
		}

		if ( ! empty( $out ) ) {
			return $out;
		}

		// Managed + empty: do not invent demo copy.
		if ( shpigovsky_section_program_intro_repeater_is_managed( $post_id ) ) {
			return array();
		}
	} elseif ( shpigovsky_section_program_intro_repeater_is_managed( $post_id ) ) {
		$legacy = array();
		$intro  = shpigovsky_get_section_field( $post_id, 'section_program_intro' );
		$intro2 = shpigovsky_get_section_field( $post_id, 'section_program_intro2' );
		if ( '' !== $intro ) {
			$legacy[] = $intro;
		}
		if ( '' !== $intro2 ) {
			$legacy[] = $intro2;
		}

		return $legacy;
	}

	$intro  = shpigovsky_get_section_field( $post_id, 'section_program_intro' );
	$intro2 = shpigovsky_get_section_field( $post_id, 'section_program_intro2' );

	if ( '' !== $intro ) {
		$out[] = $intro;
	}
	if ( '' !== $intro2 ) {
		$out[] = $intro2;
	}

	return $out;
}

/**
 * EMERGENCY ONLY — program intro reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 *
 * @return array<int, string>
 */
function shpigovsky_get_section_program_intro_demo_fallback() {
	return array(
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
	);
}

/**
 * Subdivision stages items: section repeater → Structured Sections stages → empty.
 *
 * V9-06E50: theme hardcoded stage demos are emergency-only, not normal SoT.
 *
 * @param int $post_id Service ID.
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_section_stages_items( $post_id ) {
	$rows = shpigovsky_section_normalize_stages_items(
		shpigovsky_get_section_field_raw( $post_id, 'section_stages_items' )
	);

	if ( ! empty( $rows ) ) {
		return $rows;
	}

	if ( function_exists( 'shpigovsky_get_service_repeater' ) ) {
		$legacy = shpigovsky_get_service_repeater( $post_id, 'stages' );
		$rows   = shpigovsky_section_normalize_title_text_rows( $legacy );
		if ( ! empty( $rows ) ) {
			return $rows;
		}
	}

	return array();
}

/**
 * EMERGENCY ONLY — stage steps reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_section_stages_items_fallback() {
	return array(
		array(
			'title' => __( 'Связаться с нами', 'shpigovsky' ),
			'text'  => __( 'Расскажите нам о своей ситуации — в удобном для вас формате и в удобное время. Первый разговор ни к чему не обязывает, но часто становится началом перемен.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Определить цели и программу', 'shpigovsky' ),
			'text'  => __( 'Вместе со специалистами центра мы разберёмся, что именно происходит, и составим программу, которая отвечает вашей ситуации.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Выбрать категорию номера, период стационарного проживания', 'shpigovsky' ),
			'text'  => __( 'Комфорт среды — часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и согласуем удобные сроки.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Начать реабилитацию и лечение', 'shpigovsky' ),
			'text'  => __( 'С первого дня рядом с вами будет команда специалистов. Здесь начинается то, ради чего вы пришли.', 'shpigovsky' ),
		),
	);
}

/**
 * Normalize stages item rows (title/text + optional enabled).
 *
 * @param mixed $rows Raw repeater.
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_section_normalize_stages_items( $rows ) {
	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$out = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		if ( array_key_exists( 'enabled', $row ) && ! (bool) $row['enabled'] ) {
			continue;
		}

		$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';

		if ( '' === $title && '' === $text ) {
			continue;
		}

		$out[] = array(
			'title' => $title,
			'text'  => $text,
		);
	}

	return $out;
}

/**
 * EMERGENCY ONLY — approach cards reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 * Production-safe Russian copy (no Lorem / DEMO filler).
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_section_approach_fallback_cards() {
	return array(
		array(
			'title' => __( 'диагностические инструменты', 'shpigovsky' ),
			'text'  => __( 'Комплексная оценка состояния: клинические и лабораторные методы, которые помогают понять природу зависимости и выбрать безопасный старт.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'психиатрия', 'shpigovsky' ),
			'text'  => __( 'Врачебное сопровождение психического состояния, работа с сопутствующими расстройствами и подбор терапии по показаниям.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'функциональная терапия', 'shpigovsky' ),
			'text'  => __( 'Восстановление навыков саморегуляции, режима и повседневного функционирования как часть устойчивой ремиссии.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'комплементарная терапия', 'shpigovsky' ),
			'text'  => __( 'Дополнительные методы поддержки — движение, восстановление тела и эмоционального баланса в безопасной среде центра.', 'shpigovsky' ),
		),
	);
}

/**
 * Whether approach-card text looks like technical demo filler.
 *
 * @param string $text Card text.
 * @return bool
 */
function shpigovsky_is_technical_demo_card_text( $text ) {
	$text = trim( (string) $text );
	if ( '' === $text ) {
		return true;
	}
	$lower = function_exists( 'mb_strtolower' ) ? mb_strtolower( $text ) : strtolower( $text );
	if ( 0 === strpos( $lower, 'lorem ipsum' ) || false !== strpos( $lower, 'lorem ipsum' ) ) {
		return true;
	}
	if ( 0 === strpos( $text, 'DEMO' ) || 0 === strpos( $text, 'DEMO:' ) || 0 === strpos( $lower, 'demo —' ) || 0 === strpos( $lower, 'demo:' ) ) {
		return true;
	}
	return false;
}

/**
 * Replace technical demo card text with production-safe copy matched by title.
 *
 * @param string $title Card title.
 * @param string $text Current text.
 * @return string
 */
function shpigovsky_sanitize_approach_card_text( $title, $text ) {
	$title = trim( (string) $title );
	$text  = trim( (string) $text );

	if ( ! shpigovsky_is_technical_demo_card_text( $text ) ) {
		return $text;
	}

	foreach ( shpigovsky_get_section_approach_fallback_cards() as $row ) {
		if ( isset( $row['title'], $row['text'] ) && $title === (string) $row['title'] ) {
			return (string) $row['text'];
		}
	}

	return __( 'Краткое описание направления подхода. Замените текст в поле «Карточки подхода» в админке этой страницы.', 'shpigovsky' );
}

/**
 * Load approach cards for a section page with orphaned-meta recovery.
 *
 * Canonical Admin SoT: ACF repeater `section_approach_cards`.
 * Recovers broken count / 1-based orphan rows / accidental serialized blobs.
 *
 * @param int $post_id Service ID.
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_section_approach_cards( $post_id ) {
	$post_id = absint( $post_id );
	$raw     = shpigovsky_get_section_field_raw( $post_id, 'section_approach_cards' );
	$cards   = array();

	if ( is_array( $raw ) && ! empty( $raw ) ) {
		// Serialized / already-decoded array of rows, or ACF repeater rows.
		$is_list = array_keys( $raw ) === range( 0, count( $raw ) - 1 );
		if ( $is_list ) {
			$cards = shpigovsky_section_normalize_title_text_rows( $raw );
		}
	}

	if ( empty( $cards ) ) {
		// Recover orphaned ACF row meta when count meta is empty/broken.
		$found = array();
		for ( $i = 0; $i <= 6; $i++ ) {
			$title = get_post_meta( $post_id, 'section_approach_cards_' . $i . '_title', true );
			$text  = get_post_meta( $post_id, 'section_approach_cards_' . $i . '_text', true );
			$title = is_string( $title ) ? trim( $title ) : '';
			$text  = is_string( $text ) ? trim( $text ) : '';
			if ( '' === $title && '' === $text ) {
				continue;
			}
			$found[] = array(
				'title' => $title,
				'text'  => $text,
			);
		}
		$cards = $found;
	}

	if ( empty( $cards ) ) {
		return array();
	}

	$out = array();
	foreach ( $cards as $card ) {
		$title = isset( $card['title'] ) ? trim( (string) $card['title'] ) : '';
		$text  = isset( $card['text'] ) ? trim( (string) $card['text'] ) : '';
		if ( '' === $title && '' === $text ) {
			continue;
		}
		$out[] = array(
			'title' => $title,
			'text'  => shpigovsky_sanitize_approach_card_text( $title, $text ),
		);
	}

	return $out;
}

/**
 * EMERGENCY ONLY — stages support list reserve for unseeded/legacy pages.
 * Not used on the normal frontend path after V9-06E50 (ACF SoT).
 *
 * @return array<int, string>
 */
function shpigovsky_get_section_stages_support_fallback() {
	return array(
		__( 'Интервенция на лечение — мотивация вас или ваших близких;', 'shpigovsky' ),
		__( 'Круглосуточная поддержка психологов — в любое время будет оказана помощь;', 'shpigovsky' ),
		__( 'Занятия в мини-группах — эффективная работа с каждым;', 'shpigovsky' ),
		__( 'По договоренности, возможность удалённой работы в условиях стационара.', 'shpigovsky' ),
	);
}

/**
 * Normalize repeater rows with title/text.
 *
 * @param mixed $rows Raw repeater.
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_section_normalize_title_text_rows( $rows ) {
	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$out = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';

		if ( '' === $title && '' === $text ) {
			continue;
		}

		$out[] = array(
			'title' => $title,
			'text'  => $text,
		);
	}

	return $out;
}
