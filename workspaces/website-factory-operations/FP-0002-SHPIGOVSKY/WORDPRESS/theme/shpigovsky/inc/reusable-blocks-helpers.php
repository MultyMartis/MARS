<?php
/**
 * Reusable blocks helpers — V9-06E18 Batch 1.
 *
 * Read-only option resolution with layered fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ACF options context for final form block admin.
 */
function shpigovsky_get_final_form_block_context() {
	return 'fp02-block-final-form';
}

/**
 * ACF options context for specialists block admin.
 */
function shpigovsky_get_specialists_block_context() {
	return 'fp02-block-specialists';
}

/**
 * ACF options context for global CTA band defaults admin.
 */
function shpigovsky_get_cta_bands_block_context() {
	return 'fp02-block-cta-bands';
}

/**
 * ACF options context for founder quote block admin.
 */
function shpigovsky_get_founder_quote_block_context() {
	return 'fp02-block-founder-quote';
}

/**
 * Read a scalar block option field.
 *
 * @param string $field_name Field name.
 * @param string $context    ACF options context slug.
 * @return string
 */
function shpigovsky_get_block_option_scalar( $field_name, $context ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $field_name, $context );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Resolve final form heading with block → home → static fallback chain.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_heading( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_heading', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Остались вопросы?', 'shpigovsky' );
	}

	return shpigovsky_home_text_or_fallback( 'home_cta_title', $static_fallback );
}

/**
 * Resolve final form lead text.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_lead( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_lead', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь', 'shpigovsky' );
	}

	return shpigovsky_home_text_or_fallback( 'home_cta_text', $static_fallback );
}

/**
 * Resolve final form submit button label.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_submit_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_submit_label', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Записаться на консультацию', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_button_label', $static_fallback );
}

/**
 * Resolve a final form field label with block option then static i18n fallback.
 *
 * @param string $field_name      Block option field name.
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_final_form_field_label( $field_name, $static_fallback ) {
	$block = shpigovsky_get_block_option_scalar( $field_name, shpigovsky_get_final_form_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve specialists section heading.
 *
 * @param string $static_fallback Static fallback heading.
 * @return string
 */
function shpigovsky_get_specialists_section_heading( $static_fallback = 'Специалисты центра' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_section_heading', shpigovsky_get_specialists_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	return shpigovsky_home_text_or_fallback( 'home_specialists_heading', $static_fallback );
}

/**
 * Resolve specialists all-link label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_specialists_all_link_label( $static_fallback = 'все специалисты' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_all_link_label', shpigovsky_get_specialists_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve specialists all-link URL.
 *
 * V9-06E34: default points to `/specyalisty/` parent page.
 *
 * @param string $static_fallback Static fallback URL.
 * @return string
 */
function shpigovsky_get_specialists_all_link_url( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_all_link_url', shpigovsky_get_specialists_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$parent_id = shpigovsky_get_specialists_parent_page_id();
		$static_fallback = $parent_id > 0 ? get_permalink( $parent_id ) : home_url( '/specyalisty/' );
	}

	return $static_fallback;
}

/**
 * Resolve Specialists parent page ID (`/specyalisty/`).
 *
 * @return int
 */
function shpigovsky_get_specialists_parent_page_id() {
	static $cached = null;

	if ( null !== $cached ) {
		return $cached;
	}

	$page = get_page_by_path( 'specyalisty' );
	$cached = ( $page instanceof WP_Post ) ? (int) $page->ID : 0;

	return $cached;
}

/**
 * Specialist no-photo placeholder (theme-local SVG; distinct from service/blog placeholders).
 *
 * @return array{url:string,width:int,height:int,alt:string,source:string}
 */
function shpigovsky_get_specialist_placeholder_image() {
	return array(
		'url'    => shpigovsky_asset_uri( 'images/specialist-no-photo.svg' ),
		'width'  => 640,
		'height' => 640,
		'alt'    => '',
		'source' => 'specialist-placeholder',
	);
}

/**
 * Normalize a specialist child page into render-ready card data.
 *
 * @param WP_Post $page Specialist child page.
 * @return array{image:string,width:int,height:int,name:string,role:string,link:string}|null
 */
function shpigovsky_normalize_specialist_page_card( $page ) {
	if ( ! ( $page instanceof WP_Post ) ) {
		return null;
	}

	$name = trim( (string) $page->post_title );
	if ( '' === $name ) {
		return null;
	}

	$role = trim( (string) $page->post_excerpt );
	if ( '' === $role ) {
		$role = trim( (string) get_post_meta( $page->ID, '_shpigovsky_specialist_role', true ) );
	}
	if ( '' === $role ) {
		$content = trim( wp_strip_all_tags( (string) $page->post_content ) );
		if ( '' !== $content ) {
			$role = wp_html_excerpt( $content, 160, '…' );
		}
	}

	$width  = 615;
	$height = 605;
	$image  = '';

	$thumb_id = (int) get_post_thumbnail_id( $page->ID );
	if ( $thumb_id > 0 ) {
		$src = wp_get_attachment_image_src( $thumb_id, 'full' );
		if ( is_array( $src ) && ! empty( $src[0] ) ) {
			$image  = (string) $src[0];
			$width  = ! empty( $src[1] ) ? (int) $src[1] : $width;
			$height = ! empty( $src[2] ) ? (int) $src[2] : $height;
		}
	}

	if ( '' === $image ) {
		$asset = trim( (string) get_post_meta( $page->ID, '_shpigovsky_specialist_photo_asset', true ) );
		if ( '' !== $asset ) {
			$image = preg_match( '#^https?://#i', $asset ) ? $asset : shpigovsky_asset_uri( $asset );
			$meta_w = (int) get_post_meta( $page->ID, '_shpigovsky_specialist_photo_width', true );
			$meta_h = (int) get_post_meta( $page->ID, '_shpigovsky_specialist_photo_height', true );
			if ( $meta_w > 0 ) {
				$width = $meta_w;
			}
			if ( $meta_h > 0 ) {
				$height = $meta_h;
			}
		}
	}

	if ( '' === $image ) {
		$placeholder = shpigovsky_get_specialist_placeholder_image();
		$image       = $placeholder['url'];
		$width       = $placeholder['width'];
		$height      = $placeholder['height'];
	}

	return array(
		'image'  => $image,
		'width'  => $width,
		'height' => $height,
		'name'   => $name,
		'role'   => $role,
		'link'   => get_permalink( $page ),
	);
}

/**
 * Resolve specialists cards for all reusable specialists renderers.
 *
 * V9-06E34: automatic from published child pages of `/specyalisty/`.
 * Manual ACF repeater / static fixture are no longer the active source.
 *
 * @return array<int, array{image:string,width:int,height:int,name:string,role:string,link:string}>
 */
function shpigovsky_get_specialists_cards() {
	$parent_id = shpigovsky_get_specialists_parent_page_id();
	if ( $parent_id <= 0 ) {
		return array();
	}

	$pages = get_posts(
		array(
			'post_type'      => 'page',
			'post_parent'    => $parent_id,
			'post_status'    => 'publish',
			'numberposts'    => 50,
			'orderby'        => array(
				'menu_order' => 'ASC',
				'title'      => 'ASC',
			),
		)
	);

	$cards = array();
	foreach ( $pages as $page ) {
		$card = shpigovsky_normalize_specialist_page_card( $page );
		if ( null !== $card ) {
			$cards[] = $card;
		}
	}

	return $cards;
}

/**
 * Resolve global program CTA band default title.
 *
 * @param string $static_fallback Static fallback title.
 * @return string
 */
function shpigovsky_get_cta_band_default_title( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_title', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	$global = shpigovsky_get_site_option( 'global_cta_title' );

	if ( '' !== $global ) {
		return $global;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Запишитесь на встречу', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band default subtitle.
 *
 * @param string $static_fallback Static fallback subtitle.
 * @return string
 */
function shpigovsky_get_cta_band_default_subtitle( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_subtitle', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	$global = shpigovsky_get_site_option( 'global_cta_text' );

	if ( '' !== $global ) {
		return $global;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band phone hint.
 *
 * @param string $static_fallback Static fallback hint.
 * @return string
 */
function shpigovsky_get_cta_band_phone_hint( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_phone_hint', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Или позвоните нам', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band default button label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_cta_band_default_button_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_button_label', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Записаться', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_button_label', $static_fallback );
}

/**
 * Founder quote reusable block payload.
 *
 * @return array<string, mixed>
 */
function shpigovsky_get_founder_quote_block_context_data() {
	$context = shpigovsky_get_founder_quote_block_context();
	$rows    = function_exists( 'get_field' ) ? get_field( 'founder_quote_paragraphs', $context ) : array();
	$texts   = array();

	if ( is_array( $rows ) ) {
		foreach ( $rows as $row ) {
			$text = is_array( $row ) && isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' !== $text ) {
				$texts[] = $text;
			}
		}
	}

	if ( empty( $texts ) ) {
		$texts = array(
			'Мы создавали «Шпиговский Дом» как место, где человек может получить профессиональную помощь, не&nbsp;теряя связь с&nbsp;собственной жизнью.',
			'Многие боятся обратиться за&nbsp;лечением, потому что опасаются потерять семью, работу и&nbsp;привычный уклад жизни.',
			'Мы считаем, что современная реабилитация должна помогать человеку восстанавливать себя, сохраняя то, что для него действительно важно.',
			'«Наша цель&nbsp;— создать безопасное пространство для изменений. Наша задача&nbsp;— не&nbsp;изолировать человека от&nbsp;жизни, а&nbsp;помочь ему вернуть контроль над ней.»',
		);
	}

	$photo = function_exists( 'get_field' ) ? get_field( 'founder_quote_photo', $context ) : null;
	$url   = shpigovsky_acf_image_url( $photo );
	$alt   = shpigovsky_acf_image_alt( $photo );

	return array(
		'paragraphs' => $texts,
		'name'       => shpigovsky_get_block_option_scalar( 'founder_quote_name', $context ) ?: 'Сергей Юрьевич Шпиговский',
		'role'       => shpigovsky_get_block_option_scalar( 'founder_quote_role', $context ) ?: 'Основатель центра. Аддиктолог, интервенционист',
		'photo_url'  => '' !== $url ? $url : shpigovsky_asset_uri( 'img/content/founder-sergey-shpigovsky.png' ),
		'photo_alt'  => '' !== $alt ? $alt : 'Сергей Юрьевич Шпиговский',
		'photo_width' => is_array( $photo ) && ! empty( $photo['width'] ) ? (int) $photo['width'] : 1281,
		'photo_height' => is_array( $photo ) && ! empty( $photo['height'] ) ? (int) $photo['height'] : 1278,
		'cta_label'  => shpigovsky_get_block_option_scalar( 'founder_quote_cta_label', $context ) ?: 'Записаться на консультацию',
	);
}

/**
 * ACF options context for header block admin.
 */
function shpigovsky_get_header_block_context() {
	return 'fp02-block-header';
}

/**
 * ACF options context for footer block admin.
 */
function shpigovsky_get_footer_block_context() {
	return 'fp02-block-footer';
}

/**
 * ACF options context for comfort / benefits block admin.
 */
function shpigovsky_get_comfort_block_context() {
	return 'fp02-block-comfort';
}

/**
 * Resolve header logo URL with block → theme asset fallback.
 *
 * @return string
 */
function shpigovsky_get_header_logo_url() {
	$context = shpigovsky_get_header_block_context();

	if ( function_exists( 'get_field' ) ) {
		$media = get_field( 'header_logo', $context );
		$url   = shpigovsky_acf_image_url( $media );

		if ( '' !== $url ) {
			return $url;
		}
	}

	$asset = shpigovsky_get_block_option_scalar( 'header_logo_asset', $context );

	if ( '' === $asset ) {
		$asset = 'img/branding/logo.svg';
	}

	return shpigovsky_asset_uri( $asset );
}

/**
 * Resolve header callback button label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_header_callback_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'header_callback_label', shpigovsky_get_header_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Заказать звонок', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_button_label', $static_fallback );
}

/**
 * Resolve footer logo URL with block → theme asset fallback.
 *
 * @return string
 */
function shpigovsky_get_footer_logo_url() {
	$context = shpigovsky_get_footer_block_context();

	if ( function_exists( 'get_field' ) ) {
		$media = get_field( 'footer_logo', $context );
		$url   = shpigovsky_acf_image_url( $media );

		if ( '' !== $url ) {
			return $url;
		}
	}

	$asset = shpigovsky_get_block_option_scalar( 'footer_logo_asset', $context );

	if ( '' === $asset ) {
		$asset = 'img/branding/logo.svg';
	}

	return shpigovsky_asset_uri( $asset );
}

/**
 * Resolve footer copyright suffix text.
 *
 * @param string $static_fallback Static fallback suffix.
 * @return string
 */
function shpigovsky_get_footer_copyright_suffix( $static_fallback = 'Все права защищены.' ) {
	$block = shpigovsky_get_block_option_scalar( 'footer_copyright_suffix', shpigovsky_get_footer_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve footer developer credit text.
 *
 * @param string $static_fallback Static fallback credit.
 * @return string
 */
function shpigovsky_get_footer_credit_text( $static_fallback = 'Разработка и продвижение: Overseo' ) {
	$block = shpigovsky_get_block_option_scalar( 'footer_credit_text', shpigovsky_get_footer_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve footer developer credit URL.
 *
 * @return string
 */
function shpigovsky_get_footer_credit_url() {
	return shpigovsky_get_block_option_scalar( 'footer_credit_url', shpigovsky_get_footer_block_context() );
}

/**
 * Resolve footer callback button label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_footer_callback_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'footer_callback_label', shpigovsky_get_footer_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Заказать звонок', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_callback_title', $static_fallback );
}

/**
 * Resolve footer appointment button label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_footer_appointment_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'footer_appointment_label', shpigovsky_get_footer_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Записаться', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_secondary_button_label', $static_fallback );
}

/**
 * Resolve comfort section heading.
 *
 * @param string $static_fallback Static fallback heading.
 * @return string
 */
function shpigovsky_get_comfort_heading( $static_fallback = 'Комфорт, приватность, забота' ) {
	$block = shpigovsky_get_block_option_scalar( 'comfort_heading', shpigovsky_get_comfort_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	return shpigovsky_home_text_or_fallback( 'home_comfort_heading', $static_fallback );
}

/**
 * Resolve comfort section lead.
 *
 * @param string $static_fallback Static fallback lead.
 * @return string
 */
function shpigovsky_get_comfort_lead( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'comfort_lead', shpigovsky_get_comfort_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = 'Разговор&nbsp;— это уже первый шаг. Мы расскажем, что можем предложить именно вам или вашему близкому&nbsp;— без давления и&nbsp;без шаблонных ответов.';
	}

	return shpigovsky_home_text_or_fallback( 'home_comfort_lead', $static_fallback );
}

/**
 * Resolve comfort all-link label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_comfort_all_link_label( $static_fallback = 'подробнее о&nbsp;доме' ) {
	$block = shpigovsky_get_block_option_scalar( 'comfort_all_link_label', shpigovsky_get_comfort_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve comfort all-link URL.
 *
 * @param string $static_fallback Static fallback URL.
 * @return string
 */
function shpigovsky_get_comfort_all_link_url( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'comfort_all_link_url', shpigovsky_get_comfort_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = home_url( '/o-centre/galereya-o-dome/' );
	}

	return $static_fallback;
}

/**
 * Default comfort gallery rows from V9 static assets.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_comfort_gallery_static_rows() {
	return array(
		array(
			'gallery_image_asset'    => 'img/branding/logo.svg',
			'gallery_is_decor'         => true,
			'gallery_is_wide'          => false,
			'gallery_fancybox_enabled' => false,
			'gallery_image_width'      => 0,
			'gallery_image_height'     => 0,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-01.webp',
			'gallery_is_decor'         => false,
			'gallery_is_wide'          => true,
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 1957,
			'gallery_image_height'     => 1113,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-02.webp',
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 1881,
			'gallery_image_height'     => 1246,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-03.webp',
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 1623,
			'gallery_image_height'     => 1155,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-04.webp',
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 1610,
			'gallery_image_height'     => 1146,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-05.webp',
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 1276,
			'gallery_image_height'     => 1136,
		),
		array(
			'gallery_image_asset'    => 'img/content/home-comfort/comfort-room-06.webp',
			'gallery_is_wide'          => true,
			'gallery_fancybox_enabled' => true,
			'gallery_image_width'      => 2201,
			'gallery_image_height'     => 1227,
		),
	);
}

/**
 * Normalize one comfort gallery row for rendering.
 *
 * @param array<string, mixed> $row          ACF row.
 * @param array<string, mixed> $fallback_row Static fallback row.
 * @return array<string, mixed>|null
 */
function shpigovsky_normalize_comfort_gallery_row( $row, $fallback_row ) {
	if ( ! is_array( $row ) ) {
		return null;
	}

	$media     = isset( $row['gallery_image'] ) ? $row['gallery_image'] : null;
	$media_url = shpigovsky_acf_image_url( $media );
	$asset     = isset( $row['gallery_image_asset'] ) ? trim( (string) $row['gallery_image_asset'] ) : '';
	$url       = $media_url;

	if ( '' === $url && '' !== $asset ) {
		$url = shpigovsky_asset_uri( $asset );
	} elseif ( '' === $url && is_array( $fallback_row ) && ! empty( $fallback_row['gallery_image_asset'] ) ) {
		$url = shpigovsky_asset_uri( (string) $fallback_row['gallery_image_asset'] );
	}

	if ( '' === $url ) {
		return null;
	}

	$width  = isset( $row['gallery_image_width'] ) ? (int) $row['gallery_image_width'] : 0;
	$height = isset( $row['gallery_image_height'] ) ? (int) $row['gallery_image_height'] : 0;

	if ( $width <= 0 && is_array( $fallback_row ) ) {
		$width = isset( $fallback_row['gallery_image_width'] ) ? (int) $fallback_row['gallery_image_width'] : 0;
	}

	if ( $height <= 0 && is_array( $fallback_row ) ) {
		$height = isset( $fallback_row['gallery_image_height'] ) ? (int) $fallback_row['gallery_image_height'] : 0;
	}

	$is_decor = ! empty( $row['gallery_is_decor'] );
	if ( ! $is_decor && is_array( $fallback_row ) ) {
		$is_decor = ! empty( $fallback_row['gallery_is_decor'] );
	}

	$is_wide = ! empty( $row['gallery_is_wide'] );
	if ( ! $is_wide && is_array( $fallback_row ) ) {
		$is_wide = ! empty( $fallback_row['gallery_is_wide'] );
	}

	$fancybox = array_key_exists( 'gallery_fancybox_enabled', $row ) ? ! empty( $row['gallery_fancybox_enabled'] ) : null;
	if ( null === $fancybox && is_array( $fallback_row ) ) {
		$fancybox = ! empty( $fallback_row['gallery_fancybox_enabled'] );
	}
	if ( null === $fancybox ) {
		$fancybox = ! $is_decor;
	}

	return array(
		'url'      => $url,
		'width'    => $width,
		'height'   => $height,
		'is_decor' => $is_decor,
		'is_wide'  => $is_wide,
		'fancybox' => $fancybox,
	);
}

/**
 * Resolve all comfort gallery rows (including decor) before separation.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_comfort_gallery_all_items() {
	$fallback = shpigovsky_get_comfort_gallery_static_rows();
	$rows     = array();

	if ( function_exists( 'get_field' ) ) {
		$candidate = get_field( 'comfort_gallery_items', shpigovsky_get_comfort_block_context() );

		if ( is_array( $candidate ) && ! empty( $candidate ) ) {
			$rows = $candidate;
		}
	}

	if ( empty( $rows ) ) {
		$rows = $fallback;
	}

	$items = array();

	foreach ( $rows as $index => $row ) {
		$fallback_row = isset( $fallback[ $index ] ) ? $fallback[ $index ] : ( ! empty( $fallback ) ? $fallback[0] : array() );
		$item         = shpigovsky_normalize_comfort_gallery_row( $row, $fallback_row );

		if ( null !== $item ) {
			$items[] = $item;
		}
	}

	if ( ! empty( $items ) ) {
		return $items;
	}

	$mapped = array();

	foreach ( $fallback as $fallback_row ) {
		$item = shpigovsky_normalize_comfort_gallery_row( $fallback_row, $fallback_row );

		if ( null !== $item ) {
			$mapped[] = $item;
		}
	}

	return $mapped;
}

/**
 * Decor-only comfort gallery asset (logo), if present.
 *
 * Separated from real gallery items so it does not participate in layout/JS indexing.
 *
 * @return array<string, mixed>|null
 */
function shpigovsky_get_comfort_gallery_decor_item() {
	foreach ( shpigovsky_get_comfort_gallery_all_items() as $item ) {
		if ( ! empty( $item['is_decor'] ) ) {
			return $item;
		}
	}

	return null;
}

/**
 * Resolve real comfort gallery items for rendering (decor excluded).
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_comfort_gallery_items() {
	$items = array();

	foreach ( shpigovsky_get_comfort_gallery_all_items() as $item ) {
		if ( ! empty( $item['is_decor'] ) ) {
			continue;
		}

		$items[] = $item;
	}

	return $items;
}

/**
 * Default rehabilitation requirements steps from V9 static.
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_rehab_requirements_static_steps() {
	return array(
		array(
			'title' => 'Связаться с нами',
			'text'  => 'Расскажите нам о своей ситуации — в удобном для вас формате и в удобное время. Первый разговор ни к чему не обязывает, но часто становится началом перемен.',
		),
		array(
			'title' => 'Определить цели и программу',
			'text'  => 'Вместе со специалистами центра мы разберёмся, что именно происходит, и составим программу, которая отвечает вашей ситуации.',
		),
		array(
			'title' => 'Выбрать категорию номера, период стационарного проживания',
			'text'  => 'Комфорт среды — часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и согласуем удобные сроки.',
		),
		array(
			'title' => 'Начать реабилитацию и лечение',
			'text'  => 'С первого дня рядом с вами будет команда специалистов. Здесь начинается то, ради чего вы пришли. Мы с вами — шаг за шагом, в вашем темпе.',
		),
	);
}

/**
 * Resolve rehabilitation requirements block scalar with block → static fallback.
 *
 * @param string $field_name      Block field name.
 * @param string $static_fallback Static fallback.
 * @return string
 */
function shpigovsky_get_rehab_requirements_scalar( $field_name, $static_fallback ) {
	$block = shpigovsky_get_block_option_scalar( $field_name, shpigovsky_get_comfort_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve rehabilitation requirements steps.
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_rehab_requirements_steps() {
	$fallback = shpigovsky_get_rehab_requirements_static_steps();
	$rows     = array();

	if ( function_exists( 'get_field' ) ) {
		$candidate = get_field( 'rehab_requirements_steps', shpigovsky_get_comfort_block_context() );

		if ( is_array( $candidate ) && ! empty( $candidate ) ) {
			$rows = $candidate;
		}
	}

	if ( empty( $rows ) ) {
		return $fallback;
	}

	$steps = array();

	foreach ( $rows as $index => $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$title = isset( $row['step_title'] ) ? trim( (string) $row['step_title'] ) : '';
		$text  = isset( $row['step_text'] ) ? trim( (string) $row['step_text'] ) : '';

		if ( '' === $title && isset( $fallback[ $index ]['title'] ) ) {
			$title = (string) $fallback[ $index ]['title'];
		}

		if ( '' === $text && isset( $fallback[ $index ]['text'] ) ) {
			$text = (string) $fallback[ $index ]['text'];
		}

		if ( '' === $title && '' === $text ) {
			continue;
		}

		$steps[] = array(
			'title' => $title,
			'text'  => $text,
		);
	}

	return ! empty( $steps ) ? $steps : $fallback;
}

/**
 * Resolve rehabilitation requirements support items.
 *
 * @return string[]
 */
function shpigovsky_get_rehab_requirements_support_items() {
	$fallback = array(
		'Интервенция на лечение — мотивация вас или ваших близких;',
		'Круглосуточная поддержка психологов — в любое время будет оказана помощь;',
		'Занятия в мини-группах — эффективная работа с каждым;',
		'По договоренности, возможность удалённой работы в условиях стационара.',
	);

	$rows = array();

	if ( function_exists( 'get_field' ) ) {
		$candidate = get_field( 'rehab_requirements_support_items', shpigovsky_get_comfort_block_context() );

		if ( is_array( $candidate ) && ! empty( $candidate ) ) {
			$rows = $candidate;
		}
	}

	if ( empty( $rows ) ) {
		return $fallback;
	}

	$items = array();

	foreach ( $rows as $index => $row ) {
		$text = '';

		if ( is_array( $row ) ) {
			$text = isset( $row['item_text'] ) ? trim( (string) $row['item_text'] ) : '';
		}

		if ( '' === $text && isset( $fallback[ $index ] ) ) {
			$text = (string) $fallback[ $index ];
		}

		if ( '' !== $text ) {
			$items[] = $text;
		}
	}

	return ! empty( $items ) ? $items : $fallback;
}

/**
 * Resolve rehabilitation requirements photo descriptor.
 *
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_rehab_requirements_photo() {
	$context  = shpigovsky_get_comfort_block_context();
	$fallback = array(
		'url'    => shpigovsky_asset_uri( 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp' ),
		'alt'    => 'Интерьер клиники — коридор с картинами',
		'width'  => 2187,
		'height' => 1231,
	);

	if ( function_exists( 'get_field' ) ) {
		$media = get_field( 'rehab_requirements_photo', $context );
		$url   = shpigovsky_acf_image_url( $media );

		if ( '' !== $url ) {
			$alt_field = shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_alt', $context );
			$alt       = '' !== $alt_field ? $alt_field : shpigovsky_acf_image_alt( $media );
			if ( '' === $alt ) {
				$alt = $fallback['alt'];
			}

			$width_field  = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_width', $context );
			$height_field = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_height', $context );

			return array(
				'url'    => $url,
				'alt'    => $alt,
				'width'  => $width_field > 0 ? $width_field : ( is_array( $media ) && ! empty( $media['width'] ) ? (int) $media['width'] : $fallback['width'] ),
				'height' => $height_field > 0 ? $height_field : ( is_array( $media ) && ! empty( $media['height'] ) ? (int) $media['height'] : $fallback['height'] ),
			);
		}
	}

	$asset = shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_asset', $context );

	if ( '' !== $asset ) {
		$width_field  = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_width', $context );
		$height_field = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_height', $context );

		return array(
			'url'    => shpigovsky_asset_uri( $asset ),
			'alt'    => shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_photo_alt', $fallback['alt'] ),
			'width'  => $width_field > 0 ? $width_field : $fallback['width'],
			'height' => $height_field > 0 ? $height_field : $fallback['height'],
		);
	}

	$width_field  = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_width', $context );
	$height_field = (int) shpigovsky_get_block_option_scalar( 'rehab_requirements_photo_height', $context );

	return array(
		'url'    => $fallback['url'],
		'alt'    => shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_photo_alt', $fallback['alt'] ),
		'width'  => $width_field > 0 ? $width_field : $fallback['width'],
		'height' => $height_field > 0 ? $height_field : $fallback['height'],
	);
}

/**
 * Resolve rehabilitation requirements CTA phone display and href.
 *
 * @return array{display:string,href:string}
 */
function shpigovsky_get_rehab_requirements_cta_phone() {
	$display = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_cta_phone', '' );

	if ( '' === $display ) {
		$display = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
	}

	if ( '' === $display ) {
		$display = '8 (925) 183-64-64';
	}

	$href = shpigovsky_phone_href( $display );

	if ( '' === $href ) {
		$href = 'tel:+79251836464';
	}

	return array(
		'display' => $display,
		'href'    => $href,
	);
}
