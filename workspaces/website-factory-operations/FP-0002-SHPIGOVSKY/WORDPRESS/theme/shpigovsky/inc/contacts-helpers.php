<?php
/**
 * Contacts page ACF read helpers — V9-06D7-E source integration.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Contacts page post ID for ACF context.
 *
 * @return int
 */
function shpigovsky_get_contacts_page_id() {
	if ( is_page() ) {
		return (int) get_queried_object_id();
	}

	return 0;
}

/**
 * Read a scalar contacts page ACF field safely.
 *
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_contacts_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$page_id = shpigovsky_get_contacts_page_id();

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
 * Read a bounded contacts page repeater safely.
 *
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_contacts_repeater( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$page_id = shpigovsky_get_contacts_page_id();

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
 * Primary display phone for contacts hero row.
 *
 * @return array{display:string,href:string}
 */
function shpigovsky_get_contacts_primary_phone() {
	$phones = shpigovsky_get_contacts_repeater( 'contacts_phones' );

	foreach ( $phones as $row ) {
		$phone = isset( $row['phone'] ) ? trim( (string) $row['phone'] ) : '';

		if ( '' !== $phone ) {
			return array(
				'display' => $phone,
				'href'    => shpigovsky_phone_href( $phone ),
			);
		}
	}

	$option_phone = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );

	if ( '' !== $option_phone ) {
		return array(
			'display' => $option_phone,
			'href'    => shpigovsky_phone_href( $option_phone ),
		);
	}

	return array(
		'display' => '',
		'href'    => '',
	);
}

/**
 * Contacts page H1 with page title fallback.
 *
 * @return string
 */
function shpigovsky_get_contacts_heading() {
	$heading = shpigovsky_get_contacts_field( 'contacts_heading' );

	if ( '' !== $heading ) {
		return $heading;
	}

	$title = trim( (string) get_the_title() );

	return '' !== $title ? $title : __( 'Контакты', 'shpigovsky' );
}

/**
 * All display phones for the contacts hero row.
 *
 * @return array<int, array{label:string,display:string,href:string}>
 */
function shpigovsky_get_contacts_phone_rows() {
	$rows   = shpigovsky_get_contacts_repeater( 'contacts_phones' );
	$phones = array();

	foreach ( $rows as $row ) {
		$phone = isset( $row['phone'] ) ? trim( (string) $row['phone'] ) : '';
		$label = isset( $row['label'] ) ? trim( (string) $row['label'] ) : '';

		if ( '' === $phone ) {
			continue;
		}

		$phones[] = array(
			'label'   => $label,
			'display' => $phone,
			'href'    => shpigovsky_phone_href( $phone ),
		);
	}

	if ( ! empty( $phones ) ) {
		return $phones;
	}

	$option_phone = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );

	if ( '' === $option_phone ) {
		return array();
	}

	return array(
		array(
			'label'   => '',
			'display' => $option_phone,
			'href'    => shpigovsky_phone_href( $option_phone ),
		),
	);
}

/**
 * Messenger/social rows for contacts page.
 *
 * @return array<int, array{label:string,url:string,icon:string}>
 */
function shpigovsky_get_contacts_messenger_rows() {
	$normalized = array();
	$seen       = array();

	foreach ( shpigovsky_get_social_platform_rows( 'contacts' ) as $row ) {
		$url = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
		if ( '' === $url || isset( $seen[ $url ] ) ) {
			continue;
		}
		$seen[ $url ]   = true;
		$normalized[] = $row;
	}

	if ( ! empty( $normalized ) ) {
		return $normalized;
	}

	$page_rows = shpigovsky_get_contacts_repeater( 'contacts_messengers' );
	foreach ( $page_rows as $row ) {
		$url   = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
		$label = isset( $row['label'] ) ? trim( (string) $row['label'] ) : '';
		if ( '' === $url || '#' === $url ) {
			continue;
		}
		$type = shpigovsky_infer_social_platform_type( $label, $url );
		$mapped = shpigovsky_normalize_social_platform_row(
			array(
				'type'        => $type,
				'url'         => $url,
				'show_header' => 1,
				'show_footer' => 1,
			)
		);
		if ( null !== $mapped ) {
			$normalized[] = $mapped;
		}
	}

	return $normalized;
}

/**
 * Shared email for location cards.
 *
 * @return string
 */
function shpigovsky_get_contacts_email() {
	$site_email = sanitize_email( shpigovsky_get_site_option( 'site_email' ) );

	return is_email( $site_email ) ? $site_email : '';
}

/**
 * Shared opening hours lines for location cards.
 *
 * @return string[]
 */
function shpigovsky_get_contacts_hours_lines() {
	$hours = shpigovsky_get_site_option( 'opening_hours' );
	$lines = shpigovsky_split_option_lines( $hours );

	if ( ! empty( $lines ) ) {
		return $lines;
	}

	return array(
		'Пн-пт с 09-00 до 19-00',
		'Сб-вс с 09-00 до 20-00',
	);
}

/**
 * Static V9 location fallback when ACF locations repeater is empty.
 *
 * @return array<int, array<string, string>>
 */
function shpigovsky_get_contacts_static_locations() {
	$email       = shpigovsky_get_contacts_email();
	$hours_lines = shpigovsky_get_contacts_hours_lines();
	$hours_html  = implode( '<br>', array_map( 'esc_html', $hours_lines ) );

	$primary_address = shpigovsky_get_site_option( 'site_address' );

	$location_one_address = '' !== trim( $primary_address )
		? trim( $primary_address )
		: 'Московская область, район ж.д. станции Катуар, д. Сухарево';

	$location_two_address = 'Москва, ул. Ленина, 3';

	$map_images = shpigovsky_get_v9_contacts_map_images();

	return array(
		array(
			'title'         => 'Центр профилактики и лечения зависимости',
			'address'       => $location_one_address,
			'address_label' => 'Адрес центра Шпиговский дом',
			'hours_html'    => $hours_html,
			'hours_label'   => 'Режим работы',
			'email'         => $email,
			'email_label'   => 'почта',
			'map_image'     => $map_images['mo'],
			'map_embed'     => '',
			'map_alt'       => 'Карта расположения центра в Московской области',
		),
		array(
			'title'         => 'Лечение зависимостей Москва',
			'address'       => $location_two_address,
			'address_label' => 'Адрес консультирования в Москве',
			'hours_html'    => $hours_html,
			'hours_label'   => 'Режим работы',
			'email'         => $email,
			'email_label'   => 'почта',
			'map_image'     => $map_images['moscow'],
			'map_embed'     => '',
			'map_alt'       => 'Карта расположения консультационного офиса в Москве',
		),
	);
}

/**
 * Normalize contacts location repeater rows for the location card partial.
 *
 * @param array<int, array<string, mixed>> $rows Repeater rows.
 * @return array<int, array<string, string>>
 */
function shpigovsky_normalize_contacts_location_rows( array $rows ) {
	$email_default       = shpigovsky_get_contacts_email();
	$hours_lines_default = shpigovsky_get_contacts_hours_lines();
	$hours_html_default  = implode( '<br>', array_map( 'esc_html', $hours_lines_default ) );
	$locations           = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$title         = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$address       = isset( $row['address'] ) ? trim( (string) $row['address'] ) : '';
		$address_label = isset( $row['address_label'] ) ? trim( (string) $row['address_label'] ) : '';
		$hours_label   = isset( $row['hours_label'] ) ? trim( (string) $row['hours_label'] ) : '';
		$hours_html    = isset( $row['hours_html'] ) ? trim( (string) $row['hours_html'] ) : '';
		$email         = isset( $row['email'] ) ? sanitize_email( (string) $row['email'] ) : '';
		$email_label   = isset( $row['email_label'] ) ? trim( (string) $row['email_label'] ) : '';
		$map_embed_code = isset( $row['map_embed_code'] ) ? (string) $row['map_embed_code'] : '';
		$map_alt       = isset( $row['map_alt'] ) ? trim( (string) $row['map_alt'] ) : '';
		$map_scroll    = ! empty( $row['map_scroll'] );
		$simplified    = ! empty( $row['simplified'] );

		if ( '' === $title && '' === $address ) {
			continue;
		}

		if ( '' === $hours_html ) {
			$hours_html = $hours_html_default;
		}

		if ( '' === $hours_label ) {
			$hours_label = 'Режим работы';
		}

		if ( '' === $email || ! is_email( $email ) ) {
			$email = $email_default;
		}

		if ( '' === $email_label ) {
			$email_label = 'почта';
		}

		if ( '' === $map_alt && '' !== $address ) {
			$map_alt = sprintf(
				/* translators: %s: location address */
				__( 'Карта: %s', 'shpigovsky' ),
				wp_strip_all_tags( $address )
			);
		}

		$locations[] = array(
			'title'          => $title,
			'address'        => $address,
			'address_label'  => $address_label,
			'hours_html'     => $hours_html,
			'hours_label'    => $hours_label,
			'email'          => $email,
			'email_label'    => $email_label,
			'map_image'      => '',
			'map_embed'      => '',
			'map_embed_code' => $map_embed_code,
			'map_alt'        => $map_alt,
			'map_scroll'     => $map_scroll,
			'simplified'     => $simplified,
		);
	}

	return $locations;
}

/**
 * Resolve contacts location cards from ACF locations repeater or static fallback.
 *
 * @return array<int, array<string, string>>
 */
function shpigovsky_get_contacts_locations() {
	$location_rows = shpigovsky_get_contacts_repeater( 'contacts_locations' );

	if ( ! empty( $location_rows ) ) {
		return shpigovsky_normalize_contacts_location_rows( $location_rows );
	}

	return shpigovsky_get_contacts_static_locations();
}

/**
 * Map embed URL from site option when allowlisted.
 *
 * Legacy page field contacts_map_url was removed in V9-06E59-FIX01 (superseded by
 * per-location map_embed_code). Historical postmeta may remain dormant.
 *
 * @return string
 */
function shpigovsky_get_contacts_map_embed_url() {
	$candidates = array(
		shpigovsky_get_site_option( 'map_link' ),
	);

	foreach ( $candidates as $candidate ) {
		$candidate = trim( (string) $candidate );

		if ( '' !== $candidate && shpigovsky_is_allowed_map_embed_url( $candidate ) ) {
			return $candidate;
		}
	}

	return '';
}

/**
 * Whether a map URL is safe to embed in an iframe.
 *
 * @param string $url Candidate URL.
 * @return bool
 */
function shpigovsky_is_allowed_map_embed_url( $url ) {
	$url = trim( (string) $url );

	if ( '' === $url ) {
		return false;
	}

	$host = wp_parse_url( $url, PHP_URL_HOST );

	if ( ! is_string( $host ) || '' === $host ) {
		return false;
	}

	$host = strtolower( $host );

	$allowed_hosts = array(
		'yandex.ru',
		'yandex.com',
		'maps.yandex.ru',
		'google.com',
		'www.google.com',
		'maps.google.com',
	);

	foreach ( $allowed_hosts as $allowed ) {
		if ( $host === $allowed || str_ends_with( $host, '.' . $allowed ) ) {
			return true;
		}
	}

	return false;
}

/**
 * Contacts page intro copy.
 *
 * @return string
 */
function shpigovsky_get_contacts_intro() {
	$intro = shpigovsky_get_contacts_field( 'contacts_form_intro' );

	if ( '' !== $intro ) {
		return $intro;
	}

	return 'Ведем прием и консультируем в Москве и Московской области. Для нас не существует границ в привычном понимании этого слова — к нам приезжают из разных городов и стран, доверяя свое здоровье и благополучие заботливой помощи наших специалистов.';
}

/**
 * Rehabilitation steps for contacts page (static V9 structure).
 *
 * @return array<int, array{number:string,title:string,text:string}>
 */
function shpigovsky_get_contacts_rehabilitation_steps() {
	return array(
		array(
			'number' => '01',
			'title'  => 'Свяжитесь с нами удобным способом',
			'text'   => 'Расскажите нам о своей ситуации — в удобном для вас формате и в удобное время. Первый разговор ни к чему не обязывает, но часто становится началом перемен.',
		),
		array(
			'number' => '02',
			'title'  => 'Поможем определить цели и программу',
			'text'   => 'Вместе со специалистами центра мы разберёмся, что именно происходит, и составим программу, которая отвечает вашей ситуации.',
		),
		array(
			'number' => '03',
			'title'  => 'Выберите категорию номера, период стационарного проживания',
			'text'   => 'Комфорт среды — часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и согласуем удобные сроки.',
		),
		array(
			'number' => '04',
			'title'  => 'Начните реабилитацию и лечение',
			'text'   => 'С первого дня рядом с вами будет команда специалистов. Здесь начинается то, ради чего вы пришли. Мы с вами — шаг за шагом, в вашем темпе.',
		),
	);
}

/**
 * Support bullet list for contacts rehabilitation section.
 *
 * @return string[]
 */
function shpigovsky_get_contacts_support_items() {
	return array(
		'Интервенция на лечение — мотивация вас или ваших близких;',
		'Круглосуточная поддержка психологов — в любое время будет оказана помощь;',
		'Занятия в мини-группах — эффективная работа с каждым;',
		'По договоренности, возможность удалённой работы в условиях стационара.',
	);
}

/**
 * CTA band payload for contacts rehabilitation section.
 *
 * @return array<string, mixed>
 */
function shpigovsky_get_contacts_cta_band() {
	$phone = shpigovsky_get_contacts_primary_phone();

	return array(
		'title'        => 'Запишитесь на гостевой визит',
		'subtitle'     => 'Вы сможете все посмотреть и задать вопросы лично',
		'phone'        => $phone['display'],
		'phone_hint'   => 'Или позвоните нам',
		'button_label' => shpigovsky_get_site_option( 'default_button_label' ) ?: 'Записаться',
		'source'       => 'contacts-rehabilitation-steps-cta',
		'wrap_section' => false,
		'button_first' => true,
		'margin_flush' => true,
	);
}

/**
 * Add V9 page body class on contacts template.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_contacts_body_class( $classes ) {
	if ( is_page_template( 'page-templates/contacts.php' ) ) {
		$classes[] = 'page-kontakty';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_contacts_body_class' );
