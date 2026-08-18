<?php
/**
 * SEO integrations settings getters + analytics/verification output — PROD-P10.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read ACF option with null-safe default (never-saved fields stay at code defaults).
 *
 * @param string $name Field name.
 * @param mixed  $default Default.
 * @return mixed
 */
function shpigovsky_seo_get_option( $name, $default = null ) {
	if ( ! function_exists( 'get_field' ) ) {
		return $default;
	}

	$value = get_field( $name, 'option' );

	if ( null === $value || false === $value || '' === $value ) {
		// true_false saved as 0/false must not fall through when explicitly saved.
		if ( false === $value && function_exists( 'acf_get_field' ) ) {
			// Distinguish unset vs saved false: ACF stores options_{name} when saved.
			$stored = get_option( 'options_' . $name, null );
			if ( null !== $stored ) {
				return $value;
			}
		}

		if ( null === $value || '' === $value ) {
			return $default;
		}
	}

	return $value;
}

/**
 * Boolean option with default.
 *
 * @param string $name Field name.
 * @param bool   $default Default.
 * @return bool
 */
function shpigovsky_seo_get_bool( $name, $default = true ) {
	if ( ! function_exists( 'get_field' ) ) {
		return (bool) $default;
	}

	$stored = get_option( 'options_' . $name, null );

	if ( null === $stored ) {
		return (bool) $default;
	}

	return (bool) $stored;
}

/**
 * Integer option clamped to bounds.
 *
 * @param string $name Field name.
 * @param int    $default Default.
 * @param int    $min Min.
 * @param int    $max Max.
 * @return int
 */
function shpigovsky_seo_get_int( $name, $default, $min, $max ) {
	$stored = get_option( 'options_' . $name, null );

	if ( null === $stored || '' === $stored ) {
		$value = (int) $default;
	} else {
		$value = (int) $stored;
	}

	return max( (int) $min, min( (int) $max, $value ) );
}

/**
 * Relationship ID list from option.
 *
 * @param string $name Field name.
 * @return array<int, int>
 */
function shpigovsky_seo_get_id_list( $name ) {
	$raw = shpigovsky_seo_get_option( $name, array() );

	if ( ! is_array( $raw ) ) {
		return array();
	}

	$ids = array();

	foreach ( $raw as $item ) {
		if ( is_numeric( $item ) ) {
			$ids[] = (int) $item;
		} elseif ( is_object( $item ) && isset( $item->ID ) ) {
			$ids[] = (int) $item->ID;
		} elseif ( is_array( $item ) && isset( $item['ID'] ) ) {
			$ids[] = (int) $item['ID'];
		}
	}

	return array_values( array_unique( array_filter( $ids ) ) );
}

/**
 * Sanitize counter / verification / measurement IDs for safe attribute output.
 *
 * @param string $value Raw.
 * @param string $pattern Regex character class without delimiters.
 * @return string
 */
function shpigovsky_seo_sanitize_public_id( $value, $pattern = 'A-Za-z0-9_-' ) {
	$value = trim( (string) $value );
	$value = preg_replace( '/[^' . $pattern . ']/', '', $value );
	return is_string( $value ) ? $value : '';
}

/**
 * Whether sitemap generation is enabled (independent of blog_public indexing).
 *
 * @return bool
 */
function shpigovsky_sitemap_is_enabled() {
	return shpigovsky_seo_get_bool( 'sitemap_enabled', true );
}

/**
 * Smart Search settings package (public-safe).
 *
 * @return array{
 *   min_chars:int,
 *   per_group:int,
 *   enabled:array<string,bool>,
 *   order:array<int,string>,
 *   match_excerpt:bool,
 *   match_body:bool,
 *   exclude_ids:array<int,int>
 * }
 */
function shpigovsky_smart_search_settings() {
	$enabled = array(
		'services'    => shpigovsky_seo_get_bool( 'smart_search_enable_services', true ),
		'articles'    => shpigovsky_seo_get_bool( 'smart_search_enable_articles', true ),
		'specialists' => shpigovsky_seo_get_bool( 'smart_search_enable_specialists', true ),
		'pages'       => shpigovsky_seo_get_bool( 'smart_search_enable_pages', true ),
	);

	$order_map = array(
		'services'    => shpigovsky_seo_get_int( 'smart_search_order_services', 1, 1, 20 ),
		'articles'    => shpigovsky_seo_get_int( 'smart_search_order_articles', 2, 1, 20 ),
		'specialists' => shpigovsky_seo_get_int( 'smart_search_order_specialists', 3, 1, 20 ),
		'pages'       => shpigovsky_seo_get_int( 'smart_search_order_pages', 4, 1, 20 ),
	);

	$keys = array_keys( $order_map );
	usort(
		$keys,
		static function ( $a, $b ) use ( $order_map ) {
			if ( $order_map[ $a ] === $order_map[ $b ] ) {
				return strcmp( $a, $b );
			}
			return $order_map[ $a ] <=> $order_map[ $b ];
		}
	);

	return array(
		'min_chars'     => shpigovsky_seo_get_int( 'smart_search_min_chars', 3, 2, 10 ),
		'per_group'     => shpigovsky_seo_get_int( 'smart_search_per_group', 5, 1, 20 ),
		'enabled'       => $enabled,
		'order'         => $keys,
		'match_excerpt' => shpigovsky_seo_get_bool( 'smart_search_match_excerpt', true ),
		'match_body'    => shpigovsky_seo_get_bool( 'smart_search_match_body', true ),
		'exclude_ids'   => shpigovsky_seo_get_id_list( 'smart_search_exclude_objects' ),
	);
}

/**
 * Build admin HTML list of live sitemap endpoints.
 *
 * @return string
 */
function shpigovsky_sitemap_admin_urls_html() {
	if ( ! shpigovsky_sitemap_is_enabled() ) {
		return '<p>Карта сайта выключена. Включите переключатель выше, чтобы получить рабочие адреса.</p>';
	}

	$index = home_url( '/wp-sitemap.xml' );
	$lines = array(
		sprintf(
			'<li><strong>Основная карта сайта:</strong> <a href="%1$s" target="_blank" rel="noopener noreferrer">%1$s</a></li>',
			esc_url( $index )
		),
	);

	$children = shpigovsky_sitemap_child_endpoint_labels();

	foreach ( $children as $label => $url ) {
		$lines[] = sprintf(
			'<li><strong>%1$s:</strong> <a href="%2$s" target="_blank" rel="noopener noreferrer">%2$s</a></li>',
			esc_html( $label ),
			esc_url( $url )
		);
	}

	$indexing = (int) get_option( 'blog_public' );
	$note     = $indexing
		? '<p>Индексация сайта сейчас <strong>разрешена</strong>.</p>'
		: '<p><strong>Важно:</strong> сейчас сайт закрыт от индексации. Карта сайта генерируется, но открытие индексации выполняется только явным действием администратора (Оля или оператор), не автоматически.</p>';

	return '<p>Рабочие адреса (на основе текущего адреса сайта):</p><ul>' . implode( '', $lines ) . '</ul>' . $note;
}

/**
 * Labeled child sitemap endpoints that exist for current settings.
 *
 * @return array<string, string> Label => URL.
 */
function shpigovsky_sitemap_child_endpoint_labels() {
	$out = array();

	if ( shpigovsky_seo_get_bool( 'sitemap_include_pages', true ) ) {
		$out['Страницы'] = home_url( '/wp-sitemap-posts-page-1.xml' );
	}

	if ( shpigovsky_seo_get_bool( 'sitemap_include_services', true ) && post_type_exists( 'service' ) ) {
		$out['Услуги'] = home_url( '/wp-sitemap-posts-service-1.xml' );
	}

	if ( shpigovsky_seo_get_bool( 'sitemap_include_articles', true ) ) {
		$out['Статьи'] = home_url( '/wp-sitemap-posts-post-1.xml' );
	}

	if ( shpigovsky_seo_get_bool( 'sitemap_include_specialists', true ) ) {
		// Core custom-provider index currently emits wp-sitemap-specialists-1.xml
		// (also reachable as specialists-specialist-1 depending on WP version).
		$out['Специалисты'] = home_url( '/wp-sitemap-specialists-1.xml' );
	}

	return $out;
}

/**
 * Populate dynamic ACF message fields on SEO settings screen.
 *
 * @param array<string, mixed> $field Field.
 * @return array<string, mixed>
 */
function shpigovsky_seo_acf_load_sitemap_urls_help( $field ) {
	$field['message'] = shpigovsky_sitemap_admin_urls_html();
	return $field;
}
add_filter( 'acf/load_field/key=field_fp02_sitemap_urls_help', 'shpigovsky_seo_acf_load_sitemap_urls_help' );

/**
 * Yandex Webmaster help message with official sitemap submission guidance.
 *
 * @param array<string, mixed> $field Field.
 * @return array<string, mixed>
 */
function shpigovsky_seo_acf_load_yandex_help( $field ) {
	$index = esc_url( home_url( '/wp-sitemap.xml' ) );
	$field['message'] = '<p>По текущей официальной справке Яндекс Вебмастера для обычных страниц, разделов и услуг используется <strong>стандартный XML Sitemap</strong> (протокол sitemaps.org), а не отдельный универсальный «фид страниц/услуг».</p>'
		. '<p>Отдельные YML-фиды Яндекса относятся к узким вертикалям дополненного представления (недвижимость, вакансии, врачи и т.п.) и <strong>не заменяют</strong> карту сайта для обычной структуры клиники.</p>'
		. '<p>Отправьте в Яндекс Вебмастер → «Файлы Sitemap» адрес:</p>'
		. '<p><a href="' . $index . '" target="_blank" rel="noopener noreferrer">' . $index . '</a></p>'
		. '<p>Справка: <a href="https://yandex.ru/support/webmaster/controlling-robot/sitemap.html" target="_blank" rel="noopener noreferrer">Использование файла Sitemap</a>.</p>';
	return $field;
}
add_filter( 'acf/load_field/key=field_fp02_yandex_webmaster_sitemap_help', 'shpigovsky_seo_acf_load_yandex_help' );

/**
 * Output verification meta + GTM/GA head snippets + custom head code.
 *
 * @return void
 */
function shpigovsky_seo_output_head_integrations() {
	$yandex_v = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'yandex_webmaster_verification', '' ), 'A-Za-z0-9_-' );
	if ( '' !== $yandex_v ) {
		echo '<meta name="yandex-verification" content="' . esc_attr( $yandex_v ) . '" />' . "\n";
	}

	$google_v = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'google_site_verification', '' ), 'A-Za-z0-9_-' );
	if ( '' !== $google_v ) {
		echo '<meta name="google-site-verification" content="' . esc_attr( $google_v ) . '" />' . "\n";
	}

	$gtm = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'google_tag_manager_id', '' ), 'A-Za-z0-9_-' );
	$gtm_ok = ( '' !== $gtm && 0 === strpos( $gtm, 'GTM-' ) );

	if ( $gtm_ok ) {
		// phpcs:ignore WordPress.WP.EnqueuedResources.NonEnqueuedScript -- intentional operator-owned GTM bootstrap.
		echo "<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
			. "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
			. "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src="
			. "'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
			. "})(window,document,'script','dataLayer','" . esc_js( $gtm ) . "');</script>\n<!-- End Google Tag Manager -->\n";
	}

	$ga = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'google_analytics_measurement_id', '' ), 'A-Za-z0-9_-' );
	// Prefer GTM when both set — avoid double counting.
	if ( ! $gtm_ok && '' !== $ga && 0 === strpos( $ga, 'G-' ) ) {
		// phpcs:ignore WordPress.WP.EnqueuedResources.NonEnqueuedScript -- intentional GA4 bootstrap from admin ID.
		echo '<script async src="https://www.googletagmanager.com/gtag/js?id=' . rawurlencode( $ga ) . '"></script>' . "\n";
		echo "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config','" . esc_js( $ga ) . "');</script>\n";
	}

	$head = (string) get_option( 'options_custom_head_code', '' );
	if ( is_string( $head ) && '' !== trim( $head ) ) {
		// phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- trusted Administrator option.
		echo $head . "\n";
	}
}
add_action( 'wp_head', 'shpigovsky_seo_output_head_integrations', 2 );

/**
 * Body-open custom code + GTM noscript.
 *
 * @return void
 */
function shpigovsky_seo_output_body_open() {
	$gtm = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'google_tag_manager_id', '' ), 'A-Za-z0-9_-' );
	if ( '' !== $gtm && 0 === strpos( $gtm, 'GTM-' ) ) {
		echo '<!-- Google Tag Manager (noscript) -->'
			. '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' . esc_attr( $gtm ) . '" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
			. '<!-- End Google Tag Manager (noscript) -->' . "\n";
	}

	$body = (string) get_option( 'options_custom_body_open_code', '' );
	if ( is_string( $body ) && '' !== trim( $body ) ) {
		// phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- trusted Administrator option.
		echo $body . "\n";
	}
}
add_action( 'wp_body_open', 'shpigovsky_seo_output_body_open', 1 );

/**
 * Footer integrations: Metrica + custom footer code.
 *
 * @return void
 */
function shpigovsky_seo_output_footer_integrations() {
	$metrica = shpigovsky_seo_sanitize_public_id( (string) shpigovsky_seo_get_option( 'yandex_metrica_counter_id', '' ), '0-9' );
	if ( '' !== $metrica ) {
		// phpcs:ignore WordPress.WP.EnqueuedResources.NonEnqueuedScript -- standard Yandex.Metrica bootstrap from counter ID.
		echo "<!-- Yandex.Metrika counter -->\n<script type=\"text/javascript\">\n"
			. "(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};\n"
			. "m[i].l=1*new Date();"
			. "for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}\n"
			. "k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})\n"
			. "(window, document, 'script', 'https://mc.yandex.ru/metrika/tag.js', 'ym');\n"
			. "ym(" . esc_js( $metrica ) . ", 'init', {clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor:true});\n"
			. "</script>\n<noscript><div><img src=\"https://mc.yandex.ru/watch/" . esc_attr( $metrica ) . "\" style=\"position:absolute; left:-9999px;\" alt=\"\" /></div></noscript>\n"
			. "<!-- /Yandex.Metrika counter -->\n";
	}

	$footer = (string) get_option( 'options_custom_footer_code', '' );
	if ( is_string( $footer ) && '' !== trim( $footer ) ) {
		// phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- trusted Administrator option.
		echo $footer . "\n";
	}
}
add_action( 'wp_footer', 'shpigovsky_seo_output_footer_integrations', 20 );

/**
 * Append Sitemap directive to robots.txt without changing Disallow / indexing policy.
 *
 * @param string $output Robots.txt.
 * @param bool   $public blog_public.
 * @return string
 */
function shpigovsky_seo_robots_txt( $output, $public ) {
	unset( $public );

	if ( ! shpigovsky_sitemap_is_enabled() ) {
		return $output;
	}

	$sitemap = home_url( '/wp-sitemap.xml' );
	if ( false === strpos( $output, 'Sitemap:' ) ) {
		$output = rtrim( $output ) . "\n\nSitemap: " . esc_url_raw( $sitemap ) . "\n";
	}

	return $output;
}
add_filter( 'robots_txt', 'shpigovsky_seo_robots_txt', 99, 2 );
