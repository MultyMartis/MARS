<?php
/**
 * ACF field group: service section (Раздел) page admin parity — V9-06E46.
 *
 * Frontend stack order for subdivision pages drives admin field order.
 * Visible when service_editor_role === section.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Section/Раздел admin parity fields.
 */
final class ServiceSectionParity {

	/**
	 * Conditional: show when editor role is section (Раздел).
	 *
	 * @return array<int, array<int, array<string, string>>>
	 */
	private static function when_section() {
		return array(
			array(
				array(
					'field'    => 'field_fp02_service_editor_role',
					'operator' => '==',
					'value'    => 'section',
				),
			),
		);
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
			'conditional_logic' => self::when_section(),
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
	 * true_false toggle with section conditional.
	 *
	 * @param string $key Field key.
	 * @param string $label Label.
	 * @param string $name Name.
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
				'conditional_logic' => self::when_section(),
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
	 * Scalar field with section conditional.
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
			'conditional_logic' => self::when_section(),
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
		$url = self::services_admin_url();

		$children_notice = sprintf(
			/* translators: %s: services CPT admin URL */
			__( 'Автоматический блок: список дочерних услуг строится <strong class="fp02-acf-notice-danger">из <a href="%s">страниц услуг</a></strong> (дети текущего раздела или ручной relationship). Ниже — заголовок/лид/футер и показ блока.', 'shpigovsky-core' ),
			$url
		);

		$program_notice = sprintf(
			/* translators: %s: services CPT admin URL */
			__( 'Карточки направлений: ACF «Пункты программы» на этой странице; изображения/ссылки направлений — из каталога программы лечения (общий справочник). Текст lead/intro редактируется ниже. Заполнено демо-контентом — при необходимости замените вручную.', 'shpigovsky-core' ),
			$url
		);

		$specialists_url = function_exists( 'admin_url' ) ? esc_url( admin_url( 'edit.php?post_type=page' ) ) : '';
		$specialists_notice = sprintf(
			/* translators: %s: pages admin URL */
			__( 'Автоматический блок: карточки <strong class="fp02-acf-notice-danger">из дочерних страниц «Специалисты»</strong>. Заголовок/ссылка — в настройках переиспользуемого блока. На странице раздела — только показ/скрытие.', 'shpigovsky-core' ),
			$specialists_url
		);

		return array(
			'key'                   => 'group_fp02_service_section_parity',
			'title'                 => __( 'Service — Раздел (блоки по порядку сайта)', 'shpigovsky-core' ),
			'fields'                => array(
				// 1. Hero — pointer to existing fields.
				self::section_message(
					'field_fp02_section_hero_notice',
					__( '1. Hero', 'shpigovsky-core' ),
					'section_hero_notice',
					__( 'Контент hero редактируется в отдельной группе «Hero страницы услуги» (надзаголовок, H1 override, лид, изображение, текст/ссылка кнопки). Макет — в «Service — Layout».', 'shpigovsky-core' )
				),

				// 2. Subnav.
				self::section_message(
					'field_fp02_section_nav_notice',
					__( '2. Навигация по якорям', 'shpigovsky-core' ),
					'section_nav_notice',
					__( 'Автоматический блок: пункты якорей задаются шаблоном раздела. Хлебные крошки — из иерархии услуг.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_nav_visible',
					__( 'Показывать навигацию по якорям', 'shpigovsky-core' ),
					'section_nav_visible'
				),

				// 3. Dependencies / children.
				self::section_message(
					'field_fp02_section_dependencies_notice',
					__( '3. Дочерние услуги', 'shpigovsky-core' ),
					'section_dependencies_notice',
					$children_notice
				),
				self::toggle(
					'field_fp02_section_dependencies_visible',
					__( 'Показывать блок дочерних услуг', 'shpigovsky-core' ),
					'section_dependencies_visible'
				),
				self::field(
					'field_fp02_section_dependencies_heading',
					__( 'Заголовок блока дочерних услуг', 'shpigovsky-core' ),
					'section_dependencies_heading',
					'text',
					array(
						'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную. Если поле очистить, необязательный текст на сайте может скрыться. Аварийный резерв — только технический запас, не обычный источник контента.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_section_dependencies_lead',
					__( 'Лид блока дочерних услуг', 'shpigovsky-core' ),
					'section_dependencies_lead',
					'textarea',
					array(
						'rows'         => 4,
						'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную. Если поле очистить, лид может скрыться (или подтянуться intro_text / hero_lead этой страницы, если они заполнены). Аварийный резерв — только технический запас.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_section_dependencies_footer',
					__( 'Текст после списка дочерних услуг', 'shpigovsky-core' ),
					'section_dependencies_footer',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную. Если поле очистить, необязательный текст на сайте может скрыться. Аварийный резерв — только технический запас, не обычный источник контента.', 'shpigovsky-core' ),
					)
				),

				// 4. Nature.
				self::section_message(
					'field_fp02_section_nature_notice',
					__( '4. Природа зависимости', 'shpigovsky-core' ),
					'section_nature_notice',
					__( 'Уникальный контент страницы раздела. Заполнено демо-контентом — при необходимости замените вручную. Источник на сайте: значения ACF этой страницы.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_nature_visible',
					__( 'Показывать блок «Природа зависимости»', 'shpigovsky-core' ),
					'section_nature_visible'
				),
				self::field( 'field_fp02_section_nature_heading', __( 'Заголовок', 'shpigovsky-core' ), 'section_nature_heading', 'text' ),
				self::field( 'field_fp02_section_nature_lead', __( 'Лид', 'shpigovsky-core' ), 'section_nature_lead', 'textarea', array( 'rows' => 3 ) ),
				array(
					'key'               => 'field_fp02_section_nature_text_blocks',
					'label'             => __( 'Текстовые блоки (подзаголовок + текст)', 'shpigovsky-core' ),
					'name'              => 'section_nature_text_blocks',
					'type'              => 'repeater',
					'instructions'      => __( 'Строки вроде «Нейробиология» / «Генотипирование». Необязательные ссылка и текст после ссылки — для блоков со ссылкой. Заполнено демо-контентом. При необходимости замените вручную.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить текстовый блок', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_nature_text_block_heading',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'heading',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_section_nature_text_block_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 4,
						),
						array(
							'key'   => 'field_fp02_section_nature_text_block_link_label',
							'label' => __( 'Текст ссылки (опционально)', 'shpigovsky-core' ),
							'name'  => 'link_label',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_section_nature_text_block_link_url',
							'label' => __( 'URL ссылки (опционально)', 'shpigovsky-core' ),
							'name'  => 'link_url',
							'type'  => 'url',
						),
						array(
							'key'   => 'field_fp02_section_nature_text_block_after_text',
							'label' => __( 'Текст после ссылки (опционально)', 'shpigovsky-core' ),
							'name'  => 'after_text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
					),
				),
				array(
					'key'               => 'field_fp02_section_nature_cards',
					'label'             => __( 'Карточки проявлений', 'shpigovsky-core' ),
					'name'              => 'section_nature_cards',
					'type'              => 'repeater',
					'instructions'      => __( 'До 4 карточек. Заполнено демо-контентом. При необходимости замените вручную. Если очистить, карточки на сайте могут скрыться. Аварийный резерв — только технический запас.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить карточку', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 4,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_nature_card_title',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'title',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_section_nature_card_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
					),
				),

				// Mid CTA: no admin block in this group (E46-FIX03).
				// Frontend mid-cta uses Structured Sections cta_* + site phone;
				// visibility remains default-ON via legacy meta section_mid_cta_visible if present.

				// 5. Program.
				self::section_message(
					'field_fp02_section_program_notice',
					__( '5. Программа лечения', 'shpigovsky-core' ),
					'section_program_notice',
					$program_notice
				),
				self::toggle(
					'field_fp02_section_program_visible',
					__( 'Показывать программу лечения', 'shpigovsky-core' ),
					'section_program_visible'
				),
				self::field( 'field_fp02_section_program_heading', __( 'Заголовок программы', 'shpigovsky-core' ), 'section_program_heading', 'text' ),
				self::field( 'field_fp02_section_program_more_label', __( 'Текст ссылки «подробнее»', 'shpigovsky-core' ), 'section_program_more_label', 'text' ),
				self::field( 'field_fp02_section_program_lead', __( 'Лид программы', 'shpigovsky-core' ), 'section_program_lead', 'textarea', array( 'rows' => 3 ) ),
				array(
					'key'               => 'field_fp02_section_program_intro_items',
					'label'             => __( 'Intro программы', 'shpigovsky-core' ),
					'name'              => 'section_program_intro_items',
					'type'              => 'repeater',
					'instructions'      => __( 'Абзацы intro. Заполнено демо-контентом. При необходимости замените вручную. Пустые строки игнорируются. Если все абзацы очистить, intro на сайте может скрыться. Аварийный резерв — только технический запас.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить intro', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 6,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_program_intro_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 4,
						),
					),
				),
				// V9-06E46-FIX04: section_program_footer_label removed from admin UI (legacy meta kept; FE uses stored value or «подробнее о программе»).

				// 6. Stages.
				self::section_message(
					'field_fp02_section_stages_notice',
					__( '6. Этапы / что нужно для лечения', 'shpigovsky-core' ),
					'section_stages_notice',
					__( 'Этапы редактируются ниже (паттерн как у блока «Что нужно…»). Источник: ACF этой страницы. Заполнено демо-контентом — при необходимости замените вручную.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_stages_visible',
					__( 'Показывать блок этапов', 'shpigovsky-core' ),
					'section_stages_visible'
				),
				self::field( 'field_fp02_section_stages_heading', __( 'Заголовок этапов', 'shpigovsky-core' ), 'section_stages_heading', 'text' ),
				self::field( 'field_fp02_section_stages_lead', __( 'Лид этапов', 'shpigovsky-core' ), 'section_stages_lead', 'textarea', array( 'rows' => 3 ) ),
				array(
					'key'               => 'field_fp02_section_stages_items',
					'label'             => __( 'Этапы', 'shpigovsky-core' ),
					'name'              => 'section_stages_items',
					'type'              => 'repeater',
					'instructions'      => __( 'Заголовок и текст каждого этапа. Заполнено демо-контентом. При необходимости замените вручную. Пустой repeater: этапы могут скрыться (или показаться legacy Structured Sections stages, если они есть). Аварийный резерв темы — только технический запас.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить этап', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_stages_item_title',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'title',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_section_stages_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
						array(
							'key'           => 'field_fp02_section_stages_item_enabled',
							'label'         => __( 'Показывать этап', 'shpigovsky-core' ),
							'name'          => 'enabled',
							'type'          => 'true_false',
							'default_value' => 1,
							'ui'            => 1,
						),
					),
				),
				self::field( 'field_fp02_section_stages_support_heading', __( 'Заголовок поддержки', 'shpigovsky-core' ), 'section_stages_support_heading', 'text' ),
				array(
					'key'               => 'field_fp02_section_stages_support_items',
					'label'             => __( 'Пункты поддержки', 'shpigovsky-core' ),
					'name'              => 'section_stages_support_items',
					'type'              => 'repeater',
					'instructions'      => __( 'Заполнено демо-контентом. При необходимости замените вручную. Если оставить пустым — аварийный резерв.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'table',
					'button_label'      => __( 'Добавить пункт', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 8,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_stages_support_item_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'text',
						),
					),
				),

				// 7. Approach / team-stats.
				self::section_message(
					'field_fp02_section_approach_notice',
					__( '7. Наш подход к лечению', 'shpigovsky-core' ),
					'section_approach_notice',
					__( 'Уникальный контент раздела: заголовки, тексты, изображения и карточки. Источник на сайте — ACF этой страницы. Заполнено демо-контентом; при необходимости замените вручную.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_approach_visible',
					__( 'Показывать блок «Наш подход»', 'shpigovsky-core' ),
					'section_approach_visible'
				),
				self::field( 'field_fp02_section_approach_heading', __( 'Заголовок подхода', 'shpigovsky-core' ), 'section_approach_heading', 'text', array( 'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную.', 'shpigovsky-core' ) ) ),
				self::field( 'field_fp02_section_approach_more_label', __( 'Текст ссылки «подробнее»', 'shpigovsky-core' ), 'section_approach_more_label', 'text', array( 'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную.', 'shpigovsky-core' ) ) ),
				self::field( 'field_fp02_section_approach_more_url', __( 'URL ссылки «подробнее»', 'shpigovsky-core' ), 'section_approach_more_url', 'url' ),
				self::field( 'field_fp02_section_approach_highlight', __( 'Выделенный абзац (красная линия)', 'shpigovsky-core' ), 'section_approach_highlight', 'textarea', array( 'rows' => 3, 'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную.', 'shpigovsky-core' ) ) ),
				self::field( 'field_fp02_section_approach_intro', __( 'Intro подхода', 'shpigovsky-core' ), 'section_approach_intro', 'textarea', array( 'rows' => 3, 'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную.', 'shpigovsky-core' ) ) ),
				self::field(
					'field_fp02_section_corridor_image',
					__( 'Изображение коридора', 'shpigovsky-core' ),
					'section_corridor_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока коридора/интерьера на этой странице раздела. Если поле очистить, блок может использовать аварийный резерв темы (технический запас).', 'shpigovsky-core' ),
					)
				),
				self::field( 'field_fp02_section_corridor_image_alt', __( 'Alt изображения коридора', 'shpigovsky-core' ), 'section_corridor_image_alt', 'text' ),
				self::field(
					'field_fp02_section_team_image',
					__( 'Изображение команды', 'shpigovsky-core' ),
					'section_team_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока команды на этой странице раздела. Если поле очистить, блок может использовать аварийный резерв темы (технический запас).', 'shpigovsky-core' ),
					)
				),
				self::field( 'field_fp02_section_team_image_alt', __( 'Alt изображения команды', 'shpigovsky-core' ), 'section_team_image_alt', 'text' ),
				array(
					'key'               => 'field_fp02_section_approach_cards',
					'label'             => __( 'Карточки подхода', 'shpigovsky-core' ),
					'name'              => 'section_approach_cards',
					'type'              => 'repeater',
					'instructions'      => __( 'Редактируйте здесь карточки, которые видны на сайте в блоке подхода (до 6 шт.). Источник фронта — этот repeater. Если ряды пустые, карточки скрываются. Аварийный резерв темы — только технический запас и не должен подменять реальный контент.', 'shpigovsky-core' ),
					'required'          => 0,
					'conditional_logic' => self::when_section(),
					'layout'            => 'row',
					'button_label'      => __( 'Добавить карточку', 'shpigovsky-core' ),
					'min'               => 0,
					'max'               => 6,
					'sub_fields'        => array(
						array(
							'key'   => 'field_fp02_section_approach_card_title',
							'label' => __( 'Заголовок', 'shpigovsky-core' ),
							'name'  => 'title',
							'type'  => 'text',
						),
						array(
							'key'   => 'field_fp02_section_approach_card_text',
							'label' => __( 'Текст', 'shpigovsky-core' ),
							'name'  => 'text',
							'type'  => 'textarea',
							'rows'  => 3,
						),
					),
				),

				// 8. Clinic landscape (section-specific image — V9-06E46-FIX04).
				self::section_message(
					'field_fp02_section_clinic_landscape_notice',
					__( '8. Территория клиники', 'shpigovsky-core' ),
					'section_clinic_landscape_notice',
					__( 'Изображение блока «Территория клиники» для <strong class="fp02-acf-notice-danger">этой страницы раздела</strong>. Источник — ACF этой страницы (не Home). Если поле очистить, блок может использовать аварийный резерв темы (технический запас).', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_clinic_landscape_visible',
					__( 'Показывать территорию клиники', 'shpigovsky-core' ),
					'section_clinic_landscape_visible'
				),
				self::field(
					'field_fp02_section_clinic_landscape_image',
					__( 'Изображение территории клиники', 'shpigovsky-core' ),
					'section_clinic_landscape_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'library'       => 'all',
						'instructions'  => __( 'Выберите изображение для блока «Территория клиники» на этой странице раздела. Если поле очистить, блок может использовать аварийный резерв темы (технический запас).', 'shpigovsky-core' ),
					)
				),

				// 9. Specialists.
				self::section_message(
					'field_fp02_section_specialists_notice',
					__( '9. Специалисты', 'shpigovsky-core' ),
					'section_specialists_notice',
					$specialists_notice
				),
				self::toggle(
					'field_fp02_section_specialists_visible',
					__( 'Показывать специалистов', 'shpigovsky-core' ),
					'section_specialists_visible'
				),

				// 10. Founder quote.
				self::section_message(
					'field_fp02_section_founder_quote_notice',
					__( '10. Слово основателя', 'shpigovsky-core' ),
					'section_founder_quote_notice',
					__( 'Общий статический блок (контент в шаблоне). На странице раздела — показ/скрытие. Не дублируем текст на каждой странице раздела.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_founder_quote_visible',
					__( 'Показывать слово основателя', 'shpigovsky-core' ),
					'section_founder_quote_visible'
				),

				// 11. Comfort.
				self::section_message(
					'field_fp02_section_comfort_notice',
					__( '11. Условия центра', 'shpigovsky-core' ),
					'section_comfort_notice',
					__( 'Автоматический/общий блок: контент из переиспользуемого блока Comfort. На странице раздела — показ/скрытие.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_comfort_visible',
					__( 'Показывать условия центра', 'shpigovsky-core' ),
					'section_comfort_visible'
				),

				// 12. Reviews.
				self::section_message(
					'field_fp02_section_reviews_notice',
					__( '12. Отзывы', 'shpigovsky-core' ),
					'section_reviews_notice',
					__( 'Автоматический блок: отзывы из настроек сайта / CPT отзывов. На странице раздела — показ/скрытие (не зависит от тумблера Home).', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_reviews_visible',
					__( 'Показывать отзывы', 'shpigovsky-core' ),
					'section_reviews_visible'
				),

				// 13. FAQ.
				self::section_message(
					'field_fp02_section_faq_notice',
					__( '13. FAQ', 'shpigovsky-core' ),
					'section_faq_notice',
					__( 'Вопросы/ответы — repeater FAQ этой страницы услуги. Ниже — заголовок секции и показ.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_faq_visible',
					__( 'Показывать FAQ', 'shpigovsky-core' ),
					'section_faq_visible'
				),
				self::field(
					'field_fp02_section_faq_heading',
					__( 'Заголовок FAQ', 'shpigovsky-core' ),
					'section_faq_heading',
					'text',
					array(
						'instructions' => __( 'Заполнено демо-контентом. При необходимости замените вручную. Если поле очистить, заголовок FAQ на сайте может скрыться или остаться пустым. Аварийный резерв — только технический запас.', 'shpigovsky-core' ),
					)
				),

				// 14. Final form.
				self::section_message(
					'field_fp02_section_final_form_notice',
					__( '14. Финальная форма', 'shpigovsky-core' ),
					'section_final_form_notice',
					__( 'Общий блок: тексты формы из настроек Final Form. На странице раздела — показ/скрытие.', 'shpigovsky-core' )
				),
				self::toggle(
					'field_fp02_section_final_form_visible',
					__( 'Показывать финальную форму', 'shpigovsky-core' ),
					'section_final_form_visible'
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
			'description'           => 'FP-0002 V9-06E50 section demo ACF SoT; empty fields hide optional text; emergency reserve technical only.',
			'show_in_rest'          => 0,
			'modified'              => 1784452800,
		);
	}
}
