<?php
/**
 * ACF field group: service general (Услуга) page admin parity — V9-06E47.
 *
 * Frontend stack order from alcohol-direct-v9.php drives admin field order.
 * Visible when service_editor_role === service.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service/Услуга admin parity fields.
 */
final class ServiceGeneralParity {

	/**
	 * Field-level role conditional (disabled — V9-06E47-FIX02).
	 *
	 * Group visibility for Услуга vs Раздел is owned by
	 * FieldGroups::filter_service_parity_groups_by_role. Nested services convert
	 * service_editor_role into a message field (empty name) via FIX03, which breaks
	 * ACF admin JS conditionals referencing that field and hides every field here.
	 *
	 * @return int ACF "no conditional" sentinel.
	 */
	private static function when_service() {
		return 0;
	}

	/**
	 * Message field with section title styling.
	 *
	 * @param string $key Field key.
	 * @param string $label Label.
	 * @param string $name Name.
	 * @param string $message HTML message.
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
			'conditional_logic' => self::when_service(),
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
	 * true_false toggle with service conditional.
	 *
	 * @param string              $key Field key.
	 * @param string              $label Label.
	 * @param string              $name Name.
	 * @param array<string,mixed> $args Overrides.
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
				'conditional_logic' => self::when_service(),
				'wrapper'           => array(
					'width' => '',
					'class' => '',
					'id'    => '',
				),
				'default_value'     => 1,
				'ui'                => 1,
			),
			$args
		);
	}

	/**
	 * Scalar field with service conditional.
	 *
	 * @param string              $key Field key.
	 * @param string              $label Label.
	 * @param string              $name Name.
	 * @param string              $type Type.
	 * @param array<string,mixed> $args Overrides.
	 * @return array<string, mixed>
	 */
	private static function field( $key, $label, $name, $type, array $args = array() ) {
		$base = array(
			'key'               => $key,
			'label'             => $label,
			'name'              => $name,
			'type'              => $type,
			'instructions'      => '',
			'required'          => 0,
			'conditional_logic' => self::when_service(),
			'wrapper'           => array(
				'width' => '',
				'class' => '',
				'id'    => '',
			),
			'default_value'     => '',
			'placeholder'       => '',
		);

		return array_merge( $base, $args );
	}

	/**
	 * Shared demo-content instruction for editable content fields.
	 *
	 * @return string
	 */
	private static function demo_instructions() {
		return __( 'Заполнено демо-контентом. При необходимости замените вручную. Если поле оставить пустым, блок может использовать аварийный резерв.', 'shpigovsky-core' );
	}

	/**
	 * Services CPT admin list URL for notices.
	 *
	 * @return string
	 */
	private static function services_admin_url() {
		return function_exists( 'admin_url' ) ? esc_url( admin_url( 'edit.php?post_type=service' ) ) : '';
	}

	/**
	 * Field group definition.
	 *
	 * @return array<string, mixed>
	 */
	public static function group() {
		$url              = self::services_admin_url();
		$demo             = self::demo_instructions();
		$specialists_url  = function_exists( 'admin_url' ) ? esc_url( admin_url( 'edit.php?post_type=page' ) ) : '';

		$program_notice = __( 'Карточки программы: автоматический блок из каталога программы лечения (общий справочник). Заголовок / «подробнее» / lead / intro редактируются ниже. Источник уникального текста — ACF этой страницы услуги.', 'shpigovsky-core' );

		$specialists_notice = sprintf(
			/* translators: %s: pages admin URL */
			__( 'Автоматический блок: карточки <strong class="fp02-acf-notice-danger">из дочерних страниц «Специалисты»</strong>. Заголовок/ссылка — в настройках переиспользуемого блока. На странице услуги — только показ/скрытие. <a href="%s">Страницы</a>.', 'shpigovsky-core' ),
			$specialists_url
		);

		$children_notice = sprintf(
			/* translators: %s: services CPT admin URL */
			__( 'Автоматический блок: плитки дочерних услуг строятся <strong class="fp02-acf-notice-danger">из <a href="%s">страниц услуг</a></strong> (дети текущего CPT). На странице услуги — показ/скрытие.', 'shpigovsky-core' ),
			$url
		);

		return array(
			'key'                   => 'group_fp02_service_general_parity',
			'title'                 => __( 'Услуга — блоки страницы', 'shpigovsky-core' ),
			'fields'                => array(
				// 1. Hero — pointer to existing fields.
				self::section_message(
					'field_fp02_service_general_hero_notice',
					__( '1. Hero', 'shpigovsky-core' ),
					'service_general_hero_notice',
					__( 'Контент hero редактируется в отдельной группе «Hero страницы услуги» (надзаголовок, H1 override, лид, изображение, текст/ссылка кнопки). Макет — в группе «Макет страницы услуги».', 'shpigovsky-core' )
				),

				// 2. Nav.
				self::section_message(
					'field_fp02_service_general_nav_notice',
					__( '2. Навигация по якорям', 'shpigovsky-core' ),
					'service_general_nav_notice',
					__( 'Автоматический блок: пункты якорей задаются шаблоном страницы услуги. Хлебные крошки — из иерархии услуг.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_nav_visible',
					__( 'Показывать навигацию по якорям', 'shpigovsky-core' ),
					'service_general_nav_visible'
				),

				// 3. Intro.
				self::section_message(
					'field_fp02_service_general_intro_notice',
					__( '3. Intro', 'shpigovsky-core' ),
					'service_general_intro_notice',
					__( 'Уникальный intro страницы услуги. Источник на сайте: значения ACF этой страницы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_intro_visible',
					__( 'Показывать intro', 'shpigovsky-core' ),
					'service_general_intro_visible'
				),
				self::field(
					'field_fp02_service_general_intro_heading',
					__( 'Заголовок intro', 'shpigovsky-core' ),
					'service_general_intro_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_intro_highlight',
					__( 'Выделенный текст intro', 'shpigovsky-core' ),
					'service_general_intro_highlight',
					'textarea',
					array(
						'rows'         => 4,
						'instructions' => $demo,
					)
				),

				// 4. Bordered info / nature bands.
				self::section_message(
					'field_fp02_service_general_bordered_info_notice',
					__( '4. Информационные полосы', 'shpigovsky-core' ),
					'service_general_bordered_info_notice',
					__( 'Уникальные текстовые полосы страницы услуги (заголовок + текст). Источник на сайте: ACF этой страницы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_bordered_info_visible',
					__( 'Показывать информационные полосы', 'shpigovsky-core' ),
					'service_general_bordered_info_visible'
				),
				array(
					'key'               => 'field_fp02_service_general_bordered_info_items',
					'label'             => __( 'Блоки информационных полос', 'shpigovsky-core' ),
					'name'              => 'service_general_bordered_info_items',
					'type'              => 'repeater',
					'instructions'      => $demo,
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить блок', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_bordered_info_item_heading',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'heading',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_service_general_bordered_info_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 4,
						),
					),
				),

				// 5. Mid CTA — visibility + shared cta_* meta (legacy Structured group hidden for Услуга).
				self::section_message(
					'field_fp02_service_general_mid_cta_notice',
					__( '5. Средний CTA', 'shpigovsky-core' ),
					'service_general_mid_cta_notice',
					__( 'Блок середины страницы: телефон сайта общий. Тексты ниже — поля этой страницы (meta cta_*). Если пусто — стандартные подсказки темы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_mid_cta_visible',
					__( 'Показывать средний CTA', 'shpigovsky-core' ),
					'service_general_mid_cta_visible'
				),
				self::field(
					'field_fp02_service_general_cta_title',
					__( 'Заголовок среднего CTA', 'shpigovsky-core' ),
					'cta_title',
					'text',
					array(
						'instructions' => __( 'Meta-ключ cta_title (совпадает с прежним Structured Sections). Пусто — текст по умолчанию.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_service_general_cta_text',
					__( 'Текст среднего CTA', 'shpigovsky-core' ),
					'cta_text',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Meta-ключ cta_text. Пусто — текст по умолчанию.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_service_general_cta_button_label',
					__( 'Текст кнопки среднего CTA', 'shpigovsky-core' ),
					'cta_button_label',
					'text',
					array(
						'instructions' => __( 'Meta-ключ cta_button_label. Пусто — кнопка по умолчанию / опции сайта.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_service_general_cta_button_target',
					__( 'Ссылка кнопки среднего CTA', 'shpigovsky-core' ),
					'cta_button_target',
					'url',
					array(
						'instructions' => __( 'Meta-ключ cta_button_target. Обычно не обязателен (телефон/модалка).', 'shpigovsky-core' ),
					)
				),

				// 6. Signs.
				self::section_message(
					'field_fp02_service_general_signs_notice',
					__( '6. Признаки', 'shpigovsky-core' ),
					'service_general_signs_notice',
					__( 'Уникальный блок признаков/симптомов этой страницы услуги. Источник на сайте: ACF этой страницы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_signs_visible',
					__( 'Показывать блок признаков', 'shpigovsky-core' ),
					'service_general_signs_visible'
				),
				self::field(
					'field_fp02_service_general_signs_heading',
					__( 'Заголовок признаков', 'shpigovsky-core' ),
					'service_general_signs_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_signs_intro',
					__( 'Intro признаков', 'shpigovsky-core' ),
					'service_general_signs_intro',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_signs_items',
					'label'             => __( 'Пункты признаков', 'shpigovsky-core' ),
					'name'              => 'service_general_signs_items',
					'type'              => 'repeater',
					'instructions'      => $demo,
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'table',
					'button_label'      => __( 'Добавить пункт', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 20,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_signs_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'text',
						),
					),
				),
				self::field(
					'field_fp02_service_general_signs_editorial',
					__( 'Редакционный текст после признаков', 'shpigovsky-core' ),
					'service_general_signs_editorial',
					'textarea',
					array(
						'rows'         => 4,
						'instructions' => $demo,
					)
				),

				// 7. Approach.
				self::section_message(
					'field_fp02_service_general_approach_notice',
					__( '7. Наш подход к лечению', 'shpigovsky-core' ),
					'service_general_approach_notice',
					__( 'Уникальный контент услуги: заголовки, тексты, изображение команды и карточки. Источник на сайте — ACF этой страницы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_approach_visible',
					__( 'Показывать блок «Наш подход»', 'shpigovsky-core' ),
					'service_general_approach_visible'
				),
				self::field(
					'field_fp02_service_general_approach_heading',
					__( 'Заголовок подхода', 'shpigovsky-core' ),
					'service_general_approach_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_approach_more_label',
					__( 'Текст ссылки «подробнее»', 'shpigovsky-core' ),
					'service_general_approach_more_label',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_approach_more_url',
					__( 'URL ссылки «подробнее»', 'shpigovsky-core' ),
					'service_general_approach_more_url',
					'url'
				),
				self::field(
					'field_fp02_service_general_approach_highlight',
					__( 'Выделенный абзац (красная линия)', 'shpigovsky-core' ),
					'service_general_approach_highlight',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_approach_intro',
					__( 'Intro подхода', 'shpigovsky-core' ),
					'service_general_approach_intro',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_team_image',
					__( 'Изображение команды', 'shpigovsky-core' ),
					'service_general_team_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока команды на этой странице услуги. Источник — ACF этой страницы услуги. Если поле оставить пустым, блок может использовать аварийный резерв темы.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_service_general_team_image_alt',
					__( 'Alt изображения команды', 'shpigovsky-core' ),
					'service_general_team_image_alt',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_approach_cards',
					'label'             => __( 'Карточки подхода', 'shpigovsky-core' ),
					'name'              => 'service_general_approach_cards',
					'type'              => 'repeater',
					'instructions'      => __( 'Редактируйте здесь карточки подхода, видимые на странице услуги (до 6 шт.). Источник фронта — этот repeater. Пустые ряды скрываются. Не оставляйте Lorem/DEMO — такие тексты на фронте заменяются техническим запасным описанием.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить карточку', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 6,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_approach_card_title',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'title',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_service_general_approach_card_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
					),
				),

				// 8. Clinic landscape.
				self::section_message(
					'field_fp02_service_general_clinic_landscape_notice',
					__( '8. Территория клиники', 'shpigovsky-core' ),
					'service_general_clinic_landscape_notice',
					__( 'Изображение блока «Территория клиники» для <strong class="fp02-acf-notice-danger">этой страницы услуги</strong>. Источник — ACF этой страницы (не Home). Если поле оставить пустым, блок может использовать аварийный резерв темы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_clinic_landscape_visible',
					__( 'Показывать территорию клиники', 'shpigovsky-core' ),
					'service_general_clinic_landscape_visible'
				),
				self::field(
					'field_fp02_service_general_clinic_landscape_image',
					__( 'Изображение территории клиники', 'shpigovsky-core' ),
					'service_general_clinic_landscape_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока «Территория клиники» на этой странице услуги. Источник — ACF этой страницы услуги. Если поле оставить пустым, блок может использовать аварийный резерв темы.', 'shpigovsky-core' ),
					)
				),

				// 9. Program.
				self::section_message(
					'field_fp02_service_general_program_notice',
					__( '9. Программа лечения', 'shpigovsky-core' ),
					'service_general_program_notice',
					$program_notice
				),
				self::toggle(
					'field_fp02_service_general_program_visible',
					__( 'Показывать программу лечения', 'shpigovsky-core' ),
					'service_general_program_visible'
				),
				self::field(
					'field_fp02_service_general_program_heading',
					__( 'Заголовок программы', 'shpigovsky-core' ),
					'service_general_program_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_program_more_label',
					__( 'Текст ссылки «подробнее»', 'shpigovsky-core' ),
					'service_general_program_more_label',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_program_lead',
					__( 'Лид программы', 'shpigovsky-core' ),
					'service_general_program_lead',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_program_intro_items',
					'label'             => __( 'Intro программы', 'shpigovsky-core' ),
					'name'              => 'service_general_program_intro_items',
					'type'              => 'repeater',
					'instructions'      => $demo,
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить intro', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 6,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_program_intro_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 4,
						),
					),
				),

				// 10. Stages.
				self::section_message(
					'field_fp02_service_general_stages_notice',
					__( '10. Этапы лечения', 'shpigovsky-core' ),
					'service_general_stages_notice',
					__( 'Этапы редактируются ниже. Источник: ACF этой страницы услуги.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_stages_visible',
					__( 'Показывать блок этапов', 'shpigovsky-core' ),
					'service_general_stages_visible'
				),
				self::field(
					'field_fp02_service_general_stages_heading',
					__( 'Заголовок этапов', 'shpigovsky-core' ),
					'service_general_stages_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				self::field(
					'field_fp02_service_general_stages_lead',
					__( 'Лид этапов', 'shpigovsky-core' ),
					'service_general_stages_lead',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_stages_items',
					'label'             => __( 'Этапы', 'shpigovsky-core' ),
					'name'              => 'service_general_stages_items',
					'type'              => 'repeater',
					'instructions'      => $demo,
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить этап', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_stages_item_title',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'title',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_service_general_stages_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
						array(
							'key'           => 'field_fp02_service_general_stages_item_enabled',
							'label'         => __( 'Показывать этап', 'shpigovsky-core' ),
							'name'          => 'enabled',
							'type'          => 'true_false',
							'default_value' => 1,
							'ui'            => 1,
						),
					),
				),
				self::field(
					'field_fp02_service_general_stages_support_heading',
					__( 'Заголовок поддержки', 'shpigovsky-core' ),
					'service_general_stages_support_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_stages_support_items',
					'label'             => __( 'Пункты поддержки', 'shpigovsky-core' ),
					'name'              => 'service_general_stages_support_items',
					'type'              => 'repeater',
					'instructions'      => $demo,
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'table',
					'button_label'      => __( 'Добавить пункт', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_stages_support_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'text',
						),
					),
				),

				// 11. Corridor.
				self::section_message(
					'field_fp02_service_general_corridor_notice',
					__( '11. Коридор / интерьер', 'shpigovsky-core' ),
					'service_general_corridor_notice',
					__( 'Изображение блока коридора/интерьера для <strong class="fp02-acf-notice-danger">этой страницы услуги</strong>. Источник — ACF этой страницы. Если поле оставить пустым, блок может использовать аварийный резерв темы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_corridor_visible',
					__( 'Показывать блок коридора', 'shpigovsky-core' ),
					'service_general_corridor_visible'
				),
				self::field(
					'field_fp02_service_general_corridor_image',
					__( 'Изображение коридора', 'shpigovsky-core' ),
					'service_general_corridor_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока коридора/интерьера на этой странице услуги. Источник — ACF этой страницы услуги. Если поле оставить пустым, блок может использовать аварийный резерв темы.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_service_general_corridor_image_alt',
					__( 'Alt изображения коридора', 'shpigovsky-core' ),
					'service_general_corridor_image_alt',
					'text',
					array(
						'instructions' => $demo,
					)
				),

				// 12. Specialists.
				self::section_message(
					'field_fp02_service_general_specialists_notice',
					__( '12. Специалисты', 'shpigovsky-core' ),
					'service_general_specialists_notice',
					$specialists_notice
				),
				self::toggle(
					'field_fp02_service_general_specialists_visible',
					__( 'Показывать специалистов', 'shpigovsky-core' ),
					'service_general_specialists_visible'
				),

				// 13. Founder quote.
				self::section_message(
					'field_fp02_service_general_founder_quote_notice',
					__( '13. Слово основателя', 'shpigovsky-core' ),
					'service_general_founder_quote_notice',
					__( 'Общий статический блок (контент в шаблоне/переиспользуемом блоке). На странице услуги — показ/скрытие. Не дублируем текст на каждой странице услуги.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_founder_quote_visible',
					__( 'Показывать слово основателя', 'shpigovsky-core' ),
					'service_general_founder_quote_visible'
				),

				// 14. Comfort.
				self::section_message(
					'field_fp02_service_general_comfort_notice',
					__( '14. Условия центра', 'shpigovsky-core' ),
					'service_general_comfort_notice',
					__( 'Общий блок: контент из переиспользуемого блока Comfort. На странице услуги — показ/скрытие.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_comfort_visible',
					__( 'Показывать условия центра', 'shpigovsky-core' ),
					'service_general_comfort_visible'
				),

				// 15. Reviews.
				self::section_message(
					'field_fp02_service_general_reviews_notice',
					__( '15. Отзывы', 'shpigovsky-core' ),
					'service_general_reviews_notice',
					__( 'Общий блок: отзывы из настроек сайта / CPT отзывов. На странице услуги — показ/скрытие.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_reviews_visible',
					__( 'Показывать отзывы', 'shpigovsky-core' ),
					'service_general_reviews_visible'
				),

				// 16. Child services tiles.
				self::section_message(
					'field_fp02_service_general_children_notice',
					__( '16. Дочерние услуги', 'shpigovsky-core' ),
					'service_general_children_notice',
					$children_notice
				),
				self::toggle(
					'field_fp02_service_general_children_visible',
					__( 'Показывать плитки дочерних услуг', 'shpigovsky-core' ),
					'service_general_children_visible'
				),

				// 17. FAQ.
				self::section_message(
					'field_fp02_service_general_faq_notice',
					__( '17. FAQ', 'shpigovsky-core' ),
					'service_general_faq_notice',
					__( 'Вопросы/ответы — repeater FAQ этой страницы услуги. Ниже — заголовок секции и показ.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_faq_visible',
					__( 'Показывать FAQ', 'shpigovsky-core' ),
					'service_general_faq_visible'
				),
				self::field(
					'field_fp02_service_general_faq_heading',
					__( 'Заголовок FAQ', 'shpigovsky-core' ),
					'service_general_faq_heading',
					'text',
					array(
						'instructions' => $demo,
					)
				),
				array(
					'key'               => 'field_fp02_service_general_faq_items',
					'label'             => __( 'Вопросы и ответы', 'shpigovsky-core' ),
					'name'              => 'service_general_faq_items',
					'type'              => 'repeater',
					'instructions'      => __( 'Заполнено демо-контентом. При необходимости замените вручную. В ответе абзацы разделяйте пустой строкой. Если поле оставить пустым, блок может использовать аварийный резерв.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_service(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить вопрос', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 20,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_service_general_faq_item_question',
							'label' => __( 'Вопрос', 'shpigovsky-core' ),
							'name'  => 'question',
							'type'  => 'text',
						),
						array(
							'key'          => 'field_fp02_service_general_faq_item_answer',
							'label'        => __( 'Ответ', 'shpigovsky-core' ),
							'name'         => 'answer',
							'type'         => 'textarea',
							'rows'         => 5,
							'instructions' => __( 'Абзацы разделяйте пустой строкой.', 'shpigovsky-core' ),
						),
					),
				),

				// 18. Final form.
				self::section_message(
					'field_fp02_service_general_final_form_notice',
					__( '18. Финальная форма', 'shpigovsky-core' ),
					'service_general_final_form_notice',
					__( 'Общий блок: тексты формы из настроек Final Form. На странице услуги — показ/скрытие.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_service_general_final_form_visible',
					__( 'Показывать финальную форму', 'shpigovsky-core' ),
					'service_general_final_form_visible'
				),
			),
			'location'              => array(
				array(
					array(
						'param'    => 'post_type',
						'operator' => '==',
						'value'    => 'service',
					),
				),
			),
			'menu_order'            => 2,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'hide_on_screen'        => '',
			'active'                => true,
			'description'           => 'FP-0002 V9-06E47/FIX02 service general (Услуга) admin parity; field order mirrors alcohol-direct-v9.php; visibility via role group filter (no field-level when_service; nested FIX03 message field breaks ACF JS conditionals); no normal template-fallback wording.',
			'show_in_rest'          => 0,
			'modified'              => 1784454900,
		);
	}
}
