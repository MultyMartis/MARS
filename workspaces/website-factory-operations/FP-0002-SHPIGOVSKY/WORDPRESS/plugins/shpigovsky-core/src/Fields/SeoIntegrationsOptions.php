<?php
/**
 * ACF field group: SEO и интеграции — PROD-P10.
 *
 * Admin surface under «Настройки сайта → SEO и интеграции».
 * Field names intentionally avoid forbidden SiteSettings patterns
 * (token / api_key / secret / password).
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * SEO / Smart Search / analytics options fields.
 */
final class SeoIntegrationsOptions {

	/**
	 * Field group definition.
	 *
	 * @return array<string, mixed>
	 */
	public static function group() {
		return array(
			'key'                   => 'group_fp02_site_options_seo_integrations',
			'title'                 => 'SEO и интеграции',
			'fields'                => self::fields(),
			'location'              => array(
				array(
					array(
						'param'    => 'options_page',
						'operator' => '==',
						'value'    => 'fp02-site-settings-seo-integrations',
					),
				),
			),
			'menu_order'            => 0,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'hide_on_screen'        => '',
			'active'                => true,
			'description'           => 'FP-0002 PROD-P10 SEO / Smart Search / analytics settings.',
			'show_in_rest'          => 0,
			'modified'              => 1786752000,
		);
	}

	/**
	 * Fields list.
	 *
	 * @return array<int, array<string, mixed>>
	 */
	private static function fields() {
		return array(
			self::tab( 'field_fp02_seo_tab_sitemap', 'Sitemap' ),
			self::section_message(
				'field_fp02_sitemap_intro',
				'Sitemap',
				'sitemap_intro',
				'Карта сайта для Google и Яндекс. Генерация не включает сайт в поиск автоматически — индексация на временном домене может оставаться закрытой.'
			),
			self::toggle(
				'field_fp02_sitemap_enabled',
				'Включить карту сайта',
				'sitemap_enabled',
				array(
					'default_value' => 1,
					'instructions'  => 'Да — публиковать XML-карту по адресу WordPress. Нет — отключить генерацию.',
				)
			),
			self::toggle( 'field_fp02_sitemap_include_pages', 'Включать страницы', 'sitemap_include_pages', array( 'default_value' => 1 ) ),
			self::toggle( 'field_fp02_sitemap_include_services', 'Включать услуги', 'sitemap_include_services', array( 'default_value' => 1 ) ),
			self::toggle( 'field_fp02_sitemap_include_articles', 'Включать статьи', 'sitemap_include_articles', array( 'default_value' => 1 ) ),
			self::toggle(
				'field_fp02_sitemap_include_specialists',
				'Включать специалистов',
				'sitemap_include_specialists',
				array(
					'default_value' => 1,
					'instructions'  => 'Дочерние страницы раздела «Специалисты».',
				)
			),
			self::relationship(
				'field_fp02_sitemap_exclude_objects',
				'Исключить из карты сайта',
				'sitemap_exclude_objects',
				'Точные объекты, которые не должны попадать в XML-карту.'
			),
			self::section_message(
				'field_fp02_sitemap_urls_help',
				'Адреса карты сайта',
				'sitemap_urls_help',
				'Адреса появятся после сохранения настроек и при включённой карте сайта.'
			),
			self::section_message(
				'field_fp02_yandex_webmaster_sitemap_help',
				'Яндекс Вебмастер',
				'yandex_webmaster_sitemap_help',
				'Для обычных страниц, разделов и услуг Яндекс принимает стандартный XML Sitemap. Отдельный универсальный «фид страниц/услуг» для этого сценария официально не применяется. Отправьте основную карту сайта в разделе «Файлы Sitemap» Яндекс Вебмастера.'
			),

			self::tab( 'field_fp02_seo_tab_smart_search', 'Умный поиск' ),
			self::section_message(
				'field_fp02_smart_search_intro',
				'Умный поиск',
				'smart_search_intro',
				'Настройки подсказок в шапке (компьютер и телефон). Полная страница поиска по кнопке «Найти» сохраняется.'
			),
			self::toggle( 'field_fp02_smart_search_enable_services', 'Искать в услугах', 'smart_search_enable_services', array( 'default_value' => 1 ) ),
			self::toggle( 'field_fp02_smart_search_enable_articles', 'Искать в статьях', 'smart_search_enable_articles', array( 'default_value' => 1 ) ),
			self::toggle( 'field_fp02_smart_search_enable_specialists', 'Искать в специалистах', 'smart_search_enable_specialists', array( 'default_value' => 1 ) ),
			self::toggle( 'field_fp02_smart_search_enable_pages', 'Искать в страницах', 'smart_search_enable_pages', array( 'default_value' => 1 ) ),
			self::field(
				'field_fp02_smart_search_min_chars',
				'Минимум символов для подсказок',
				'smart_search_min_chars',
				'number',
				array(
					'default_value' => 3,
					'min'           => 2,
					'max'           => 10,
					'step'          => 1,
					'instructions'  => 'Подсказки появляются после ввода указанного числа символов. По умолчанию 3.',
				)
			),
			self::field(
				'field_fp02_smart_search_per_group',
				'Результатов в каждой группе',
				'smart_search_per_group',
				'number',
				array(
					'default_value' => 5,
					'min'           => 1,
					'max'           => 20,
					'step'          => 1,
					'instructions'  => 'Сколько ссылок показывать в каждой группе. По умолчанию 5.',
				)
			),
			self::field(
				'field_fp02_smart_search_order_services',
				'Порядок: Услуги',
				'smart_search_order_services',
				'number',
				array(
					'default_value' => 1,
					'min'           => 1,
					'max'           => 20,
					'step'          => 1,
					'wrapper'       => array( 'width' => '25', 'class' => '', 'id' => '' ),
				)
			),
			self::field(
				'field_fp02_smart_search_order_articles',
				'Порядок: Статьи',
				'smart_search_order_articles',
				'number',
				array(
					'default_value' => 2,
					'min'           => 1,
					'max'           => 20,
					'step'          => 1,
					'wrapper'       => array( 'width' => '25', 'class' => '', 'id' => '' ),
				)
			),
			self::field(
				'field_fp02_smart_search_order_specialists',
				'Порядок: Специалисты',
				'smart_search_order_specialists',
				'number',
				array(
					'default_value' => 3,
					'min'           => 1,
					'max'           => 20,
					'step'          => 1,
					'wrapper'       => array( 'width' => '25', 'class' => '', 'id' => '' ),
				)
			),
			self::field(
				'field_fp02_smart_search_order_pages',
				'Порядок: Страницы',
				'smart_search_order_pages',
				'number',
				array(
					'default_value' => 4,
					'min'           => 1,
					'max'           => 20,
					'step'          => 1,
					'wrapper'       => array( 'width' => '25', 'class' => '', 'id' => '' ),
				)
			),
			self::section_message(
				'field_fp02_smart_search_match_intro',
				'Где искать',
				'smart_search_match_intro',
				'Заголовок всегда учитывается. Дополнительно можно включить краткое описание и текст страницы.'
			),
			self::toggle(
				'field_fp02_smart_search_match_excerpt',
				'Искать в кратком описании',
				'smart_search_match_excerpt',
				array( 'default_value' => 1 )
			),
			self::toggle(
				'field_fp02_smart_search_match_body',
				'Искать в тексте страницы',
				'smart_search_match_body',
				array( 'default_value' => 1 )
			),
			self::relationship(
				'field_fp02_smart_search_exclude_objects',
				'Исключить из умного поиска',
				'smart_search_exclude_objects',
				'Эти материалы не появятся в подсказках. Удобно для служебных или временных страниц.'
			),

			self::tab( 'field_fp02_seo_tab_analytics', 'Аналитика и верификация' ),
			self::section_message(
				'field_fp02_analytics_intro',
				'Аналитика и верификация',
				'analytics_intro',
				'Пустые поля ничего не выводят на сайт. Не вставляйте пароли и секретные ключи — только публичные счётчики и коды подтверждения.'
			),
			self::field(
				'field_fp02_yandex_metrica_counter_id',
				'Яндекс.Метрика — номер счётчика',
				'yandex_metrica_counter_id',
				'text',
				array(
					'instructions' => 'Только цифры номера счётчика. Сайт сам добавит стандартный код Метрики.',
					'placeholder'  => '12345678',
				)
			),
			self::field(
				'field_fp02_yandex_webmaster_verification',
				'Яндекс Вебмастер — код подтверждения',
				'yandex_webmaster_verification',
				'text',
				array(
					'instructions' => 'Только содержимое meta-кода подтверждения (без тега). Пусто — тег не выводится.',
				)
			),
			self::field(
				'field_fp02_google_site_verification',
				'Google Search Console — код подтверждения',
				'google_site_verification',
				'text',
				array(
					'instructions' => 'Только содержимое meta-кода подтверждения (без тега). Пусто — тег не выводится.',
				)
			),
			self::field(
				'field_fp02_google_analytics_measurement_id',
				'Google Analytics — Measurement ID',
				'google_analytics_measurement_id',
				'text',
				array(
					'instructions' => 'Формат G-XXXXXXXX. Не заполняйте, если используете только Google Tag Manager.',
					'placeholder'  => 'G-XXXXXXXX',
				)
			),
			self::field(
				'field_fp02_google_tag_manager_id',
				'Google Tag Manager — Container ID',
				'google_tag_manager_id',
				'text',
				array(
					'instructions' => 'Формат GTM-XXXXXXX. Не включайте одновременно GA Measurement ID и GTM с тем же счётчиком, чтобы не считать дважды.',
					'placeholder'  => 'GTM-XXXXXXX',
				)
			),
			self::section_message(
				'field_fp02_advanced_code_warning',
				'Расширенные настройки',
				'advanced_code_warning',
				'<strong>Внимание:</strong> неверный код может сломать сайт. Используйте только при необходимости. Доступно администраторам.'
			),
			self::field(
				'field_fp02_custom_head_code',
				'Код в &lt;head&gt;',
				'custom_head_code',
				'textarea',
				array(
					'rows'         => 6,
					'instructions' => 'Произвольный HTML/скрипт перед закрытием head. Пусто — ничего не выводится.',
				)
			),
			self::field(
				'field_fp02_custom_body_open_code',
				'Код после открытия &lt;body&gt;',
				'custom_body_open_code',
				'textarea',
				array(
					'rows'         => 4,
					'instructions' => 'Например, noscript Google Tag Manager.',
				)
			),
			self::field(
				'field_fp02_custom_footer_code',
				'Код перед закрытием &lt;body&gt;',
				'custom_footer_code',
				'textarea',
				array(
					'rows'         => 6,
					'instructions' => 'Дополнительные скрипты в подвале.',
				)
			),
		);
	}

	/**
	 * Tab field.
	 *
	 * @param string $key Key.
	 * @param string $label Label.
	 * @return array<string, mixed>
	 */
	private static function tab( $key, $label ) {
		return array(
			'key'               => $key,
			'label'             => $label,
			'name'              => '',
			'type'              => 'tab',
			'instructions'      => '',
			'required'          => 0,
			'conditional_logic' => 0,
			'wrapper'           => array(
				'width' => '',
				'class' => '',
				'id'    => '',
			),
			'placement'         => 'top',
			'endpoint'          => 0,
		);
	}

	/**
	 * Section message.
	 *
	 * @param string $key Key.
	 * @param string $label Label.
	 * @param string $name Name.
	 * @param string $message Message HTML.
	 * @return array<string, mixed>
	 */
	private static function section_message( $key, $label, $name, $message ) {
		return array(
			'key'               => $key,
			'label'             => $label,
			'name'              => $name,
			'type'              => 'message',
			'instructions'      => '',
			'required'          => 0,
			'conditional_logic' => 0,
			'wrapper'           => array(
				'width' => '',
				'class' => 'fp02-acf-section-title',
				'id'    => '',
			),
			'message'           => $message,
			'new_lines'         => 'wpautop',
			'esc_html'          => 0,
		);
	}

	/**
	 * true_false toggle.
	 *
	 * @param string               $key Key.
	 * @param string               $label Label.
	 * @param string               $name Name.
	 * @param array<string, mixed> $args Args.
	 * @return array<string, mixed>
	 */
	private static function toggle( $key, $label, $name, array $args = array() ) {
		return array_merge(
			array(
				'key'               => $key,
				'label'             => $label,
				'name'              => $name,
				'type'              => 'true_false',
				'instructions'      => '',
				'required'          => 0,
				'conditional_logic' => 0,
				'wrapper'           => array(
					'width' => '',
					'class' => '',
					'id'    => '',
				),
				'default_value'     => 1,
				'ui'                => 1,
				'ui_on_text'        => 'Да',
				'ui_off_text'       => 'Нет',
			),
			$args
		);
	}

	/**
	 * Scalar field.
	 *
	 * @param string               $key Key.
	 * @param string               $label Label.
	 * @param string               $name Name.
	 * @param string               $type Type.
	 * @param array<string, mixed> $args Args.
	 * @return array<string, mixed>
	 */
	private static function field( $key, $label, $name, $type, array $args = array() ) {
		return array_merge(
			array(
				'key'               => $key,
				'label'             => $label,
				'name'              => $name,
				'type'              => $type,
				'instructions'      => '',
				'required'          => 0,
				'conditional_logic' => 0,
				'wrapper'           => array(
					'width' => '',
					'class' => '',
					'id'    => '',
				),
				'default_value'     => '',
				'placeholder'       => '',
			),
			$args
		);
	}

	/**
	 * Relationship field for pages / posts / services.
	 *
	 * @param string $key Key.
	 * @param string $label Label.
	 * @param string $name Name.
	 * @param string $instructions Instructions.
	 * @return array<string, mixed>
	 */
	private static function relationship( $key, $label, $name, $instructions ) {
		return array(
			'key'               => $key,
			'label'             => $label,
			'name'              => $name,
			'type'              => 'relationship',
			'instructions'      => $instructions,
			'required'          => 0,
			'conditional_logic' => 0,
			'wrapper'           => array(
				'width' => '',
				'class' => '',
				'id'    => '',
			),
			'post_type'         => array( 'page', 'post', 'service' ),
			'taxonomy'          => '',
			'filters'           => array( 'search', 'post_type' ),
			'elements'          => '',
			'min'               => 0,
			'max'               => 50,
			'return_format'     => 'id',
		);
	}
}
