<?php
/**
 * ACF Pro field group source definitions for FP-0002 V9-06C.
 *
 * Source authority:
 * - FP-0002-ACF-STRATEGY-v1.md
 * - FP-0002-FIELD-OWNERSHIP-MATRIX-v1.json
 * - FP-0002-V9-06C-ACF-FIELD-GROUP-REGISTRY-v1.json
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Registers local ACF groups after ACF Pro is available.
 */
final class FieldGroups implements ModuleInterface {

	/**
	 * Deterministic modified timestamp for canonical JSON source.
	 */
	public const MODIFIED = 1784452800;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'fields.field-groups';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() ) && shpigovsky_core_acf_pro_is_active();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'acf/init', array( __CLASS__, 'register_field_groups' ), 20 );
		add_action( 'acf/init', array( SocialPlatformsOptions::class, 'maybe_migrate' ), 40 );
		add_filter( 'acf/prepare_field/name=social_links', array( __CLASS__, 'hide_legacy_social_links_field' ) );
		// ACF 5.7.11+: acf/get_field_groups is deprecated alias of acf/load_field_groups.
		add_filter( 'acf/load_field_groups', array( __CLASS__, 'filter_service_parity_groups_by_role' ), 30 );
		add_filter( 'acf/get_field_groups', array( __CLASS__, 'filter_service_parity_groups_by_role' ), 30 );
	}

	/**
	 * Hide opposite parity + legacy service groups for clean editor UX (V9-06E47 / E47-FIX01).
	 *
	 * Field-level conditional alone still leaves an empty metabox title; remove groups
	 * from the edit screen list when role is known. Definitions and postmeta preserved.
	 *
	 * @param array<int, array<string, mixed>> $groups Field groups.
	 * @return array<int, array<string, mixed>>
	 */
	public static function filter_service_parity_groups_by_role( $groups ) {
		if ( ! is_array( $groups ) || empty( $groups ) ) {
			return $groups;
		}

		$post_id = 0;
		if ( function_exists( 'acf_get_form_data' ) ) {
			$form_post = acf_get_form_data( 'post_id' );
			if ( is_numeric( $form_post ) ) {
				$post_id = (int) $form_post;
			}
		}
		if ( $post_id <= 0 && isset( $_GET['post'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			$post_id = (int) $_GET['post']; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		}
		if ( $post_id <= 0 && function_exists( 'get_the_ID' ) ) {
			$post_id = (int) get_the_ID();
		}

		if ( $post_id <= 0 || 'service' !== get_post_type( $post_id ) ) {
			return $groups;
		}

		$role = '';
		if ( function_exists( 'get_field' ) ) {
			$role = (string) get_field( 'service_editor_role', $post_id );
		}
		if ( '' === $role ) {
			$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
		}

		if ( '' === $role ) {
			return $groups;
		}

		// V9-06E62C: always hide obsolete Structured Sections + Relationships on Service edit
		// screens (all roles). Data retained; frontend helpers still read postmeta.
		// Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.
		$always_hide = array(
			'group_fp02_service_structured_sections',
			'group_fp02_service_relationships',
		);

		// V9-06E47-FIX01: Услуга editor only needs Layout + Hero + Услуга blocks.
		// V9-06E51: Заглушка keeps the same admin content groups as Услуга (content not deleted).
		$hide_keys = $always_hide;
		if ( 'service' === $role || 'placeholder' === $role ) {
			$hide_keys = array_merge(
				$always_hide,
				array(
					'group_fp02_service_section_parity',
					'group_fp02_service_faq',
				)
			);
		} elseif ( 'section' === $role ) {
			// Раздел: mid-cta lives in section parity; Structured Sections no longer shown (E62C).
			$hide_keys = array_merge(
				$always_hide,
				array(
					'group_fp02_service_general_parity',
				)
			);
		}

		if ( empty( $hide_keys ) ) {
			return $groups;
		}

		$out = array();
		foreach ( $groups as $group ) {
			$key = isset( $group['key'] ) ? (string) $group['key'] : '';
			if ( in_array( $key, $hide_keys, true ) ) {
				continue;
			}
			$out[] = $group;
		}

		return $out;
	}

	/**
	 * Register local field groups through ACF Pro public API.
	 */
	public static function register_field_groups() {
		if ( ! function_exists( 'acf_add_local_field_group' ) ) {
			return;
		}

		foreach ( self::get_field_groups() as $group ) {
			acf_add_local_field_group( $group );
		}
	}

	/**
	 * Hide the legacy General social_links repeater after P13 structured settings exist.
	 * Data is retained.
	 *
	 * @param array<string, mixed>|false $field Field.
	 * @return array<string, mixed>|false
	 */
	public static function hide_legacy_social_links_field( $field ) {
		return false;
	}

	/**
	 * Return deterministic field group definitions.
	 *
	 * @return array<int, array<string, mixed>>
	 */
	public static function get_field_groups() {
		return array(
			self::service_layout(),
			self::service_hero(),
			ServiceSectionParity::group(),
			ServiceGeneralParity::group(),
			self::service_structured_sections(),
			self::service_faq(),
			self::service_relationships(),
			self::page_home(),
			self::page_services_hub(),
			self::page_ocentre_hub(),
			self::page_layout_mode(),
			self::page_generic_content(),
			self::page_treatment_program_child(),
			self::page_specialist_profile(),
			self::page_institutional_child(),
			self::page_contacts(),
			self::page_reviews(),
			self::page_legal(),
			self::blog_post_article_meta(),
			self::blog_archive_settings(),
			self::site_options_contacts(),
			self::site_options_modal_cta(),
			self::site_options_reviews(),
			SeoIntegrationsOptions::group(),
			SocialPlatformsOptions::group(),
			SeoEntityMeta::group(),
			self::block_final_form(),
			self::block_specialists(),
			self::block_cta_bands(),
			self::block_founder_quote(),
			self::block_header(),
			self::block_footer(),
			self::block_comfort_intro(),
			self::block_comfort_gallery(),
			self::block_comfort_requirements(),
		);
	}

	/**
	 * Service layout group (layout selector + hub/catalog flags). Hero fields live in service_hero().
	 *
	 * @return array<string, mixed>
	 */
	private static function service_layout() {
		$group = self::group(
			'group_fp02_service_layout_hero',
			__( 'Макет страницы услуги', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_service_editor_role',
					__( 'Макет страницы услуги', 'shpigovsky-core' ),
					'service_editor_role',
					'button_group',
					array(
						'instructions'  => __( 'Временный режим «Заглушка»: на фронте выводятся только шапка, навигация, H1 и подвал. Контент в полях не удаляется и может быть включён обратно сменой макета.', 'shpigovsky-core' ),
						'required'      => 0,
						'choices'       => array(
							'section'     => __( 'Раздел', 'shpigovsky-core' ),
							'service'     => __( 'Услуга', 'shpigovsky-core' ),
							'placeholder' => __( 'Заглушка', 'shpigovsky-core' ),
						),
						'default_value' => '',
						'return_format' => 'value',
						'allow_null'    => 1,
						'layout'        => 'horizontal',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-section-title fp02-service-layout-selector',
							'id'    => '',
						),
					)
				),
				// Technical fields kept in meta for resolver/sync; hidden from normal admin UI (FIX03 prepare_field).
				self::field(
					'field_fp02_service_layout_advanced_heading',
					__( 'Расширенные настройки шаблона', 'shpigovsky-core' ),
					'service_layout_advanced_heading',
					'message',
					array(
						'message' => __( 'Служебные параметры (скрыты в обычном UI). subdivision = Раздел; service_general = Услуга; placeholder = Заглушка; standard / extended — Legacy. alcohol_special — устаревший alias service_general.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title fp02-service-layout-advanced fp02-service-layout-technical-hidden',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_layout_override_enabled',
					__( 'Ручной технический шаблон', 'shpigovsky-core' ),
					'service_layout_override_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Служебное поле (скрыто в обычном UI). FIX03: синхронизация идёт по макету/глубине; override не используется редактором.', 'shpigovsky-core' ),
						'default_value' => 0,
						'ui'            => 1,
						'wrapper'       => array(
							'width' => '50',
							'class' => 'fp02-service-layout-advanced fp02-service-layout-technical-hidden',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_layout_variant',
					__( 'Технический шаблон', 'shpigovsky-core' ),
					'service_layout_variant',
					'select',
					array(
						'instructions'  => __( 'Служебное поле (скрыто в обычном UI). Синхронизируется автоматически: Раздел→subdivision, Услуга→service_general, Заглушка→placeholder.', 'shpigovsky-core' ),
						'required'      => 0,
						'choices'       => array(
							'subdivision'     => __( 'Раздел', 'shpigovsky-core' ),
							'service_general' => __( 'Услуга', 'shpigovsky-core' ),
							'placeholder'     => __( 'Заглушка', 'shpigovsky-core' ),
							'standard'        => __( 'Legacy: стандартная услуга', 'shpigovsky-core' ),
							'extended'        => __( 'Legacy: расширенная услуга', 'shpigovsky-core' ),
						),
						'default_value' => 'service_general',
						'return_format' => 'value',
						'wrapper'       => array(
							'width' => '50',
							'class' => 'fp02-service-layout-advanced fp02-service-layout-technical-hidden',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_layout_hub_heading',
					__( 'Карточка и показ на /uslugi/', 'shpigovsky-core' ),
					'service_layout_hub_heading',
					'message',
					array(
						'message' => __( 'Поля карточки/хаба (не hero и не макет шаблона). Мини-описание и флаги показа на /uslugi/ и главной.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_short_description',
					__( 'Мини-описание', 'shpigovsky-core' ),
					'service_short_description',
					'textarea',
					array(
						'instructions' => __( 'Краткий текст для карточки услуги на странице /uslugi/ и в блоке дочерних услуг. Для корневых разделов также выводится в блоке категории на /uslugi/.', 'shpigovsky-core' ),
						'rows'         => 4,
					)
				),
				self::field(
					'field_fp02_service_child_services_enabled',
					__( 'Показывать дочерние услуги', 'shpigovsky-core' ),
					'service_child_services_enabled',
					'true_false',
					array(
						'instructions'      => __( 'Автоматический блок плиток дочерних услуг перед FAQ. Если дочерних страниц нет — блок не выводится.', 'shpigovsky-core' ),
						'default_value'     => 1,
						'ui'                => 1,
						'conditional_logic' => array(
							array(
								array(
									'field'    => 'field_fp02_service_editor_role',
									'operator' => '==',
									'value'    => 'service',
								),
							),
						),
						'wrapper'           => array(
							'width' => '50',
							'class' => '',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_child_services_heading',
					__( 'Заголовок блока дочерних услуг', 'shpigovsky-core' ),
					'service_child_services_heading',
					'text',
					array(
						'instructions'      => __( 'Если пусто — используется «Направления внутри услуги».', 'shpigovsky-core' ),
						'default_value'     => '',
						'placeholder'       => __( 'Направления внутри услуги', 'shpigovsky-core' ),
						'conditional_logic' => array(
							array(
								array(
									'field'    => 'field_fp02_service_editor_role',
									'operator' => '==',
									'value'    => 'service',
								),
							),
						),
						'wrapper'           => array(
							'width' => '50',
							'class' => '',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_service_category_section_lead',
					__( 'Текст под мини-описанием на странице «Услуги»', 'shpigovsky-core' ),
					'service_category_section_lead',
					'textarea',
					array(
						'instructions'      => __( 'Выводится в блоке категории услуги на странице /uslugi/ под мини-описанием. Используется для корневых разделов (тип «Раздел» / технический шаблон subdivision).', 'shpigovsky-core' ),
						'rows'              => 4,
						'conditional_logic' => array(
							array(
								array(
									'field'    => 'field_fp02_service_editor_role',
									'operator' => '==',
									'value'    => 'section',
								),
							),
							array(
								array(
									'field'    => 'field_fp02_service_layout_variant',
									'operator' => '==',
									'value'    => 'subdivision',
								),
							),
						),
					)
				),
				self::field(
					'field_fp02_service_show_in_text_list',
					'Показывать в текстовом списке',
					'service_show_in_text_list',
					'true_false',
					array(
						'instructions'  => 'Показывать услугу в текстовом списке раздела на /uslugi/.',
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_service_show_in_slider',
					'Показывать в слайдере',
					'service_show_in_slider',
					'true_false',
					array(
						'instructions'  => 'Показывать услугу карточкой в галерее/слайдере раздела на /uslugi/. Не путать с «Показывать в слайдере на главной».',
						'default_value' => 0,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_service_show_on_home_gallery',
					'Показывать в слайдере на главной',
					'service_show_on_home_gallery',
					'true_false',
					array(
						'instructions'  => 'Отдельный флаг для слайдера услуг на главной (Home gallery). По умолчанию включено для услуг 1-го уровня (дети корневых разделов). Не связан с флагом слайдера /uslugi/.',
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_service_slider_image',
					'Изображение для слайдера',
					'service_slider_image',
					'image',
					array(
						'instructions'  => 'Опционально. Если изображение не выбрано, на сайте используется заглушка.',
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'required'      => 0,
					)
				),
			),
			self::location( 'post_type', '==', 'service' )
		);
		$group['menu_order']  = 0;
		$group['description'] = 'FP-0002 V9-06E46-FIX01: service layout (role/template) + hub/catalog flags. Hero separated to group_fp02_service_hero.';
		return $group;
	}

	/**
	 * Service hero group — shared for Раздел and Услуга. Meta keys unchanged.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_hero() {
		$group = self::group(
			'group_fp02_service_hero',
			__( 'Hero страницы услуги', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_service_hero_heading',
					__( 'Hero страницы услуги', 'shpigovsky-core' ),
					'service_hero_heading',
					'message',
					array(
						'message' => __( 'Общий блок hero для типов «Раздел» и «Услуга». Не дублируйте эти поля в других группах. Ключи meta сохранены (hero_eyebrow, hero_title_override, hero_lead, hero_media, hero_cta_label, hero_cta_target).', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field( 'field_fp02_hero_eyebrow_service', __( 'Надзаголовок', 'shpigovsky-core' ), 'hero_eyebrow', 'text' ),
				self::field( 'field_fp02_hero_title_override_service', __( 'Заголовок H1 override', 'shpigovsky-core' ), 'hero_title_override', 'text' ),
				self::field( 'field_fp02_hero_lead_service', __( 'Лид', 'shpigovsky-core' ), 'hero_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field(
					'field_fp02_hero_media_service',
					__( 'Изображение (Hero)', 'shpigovsky-core' ),
					'hero_media',
					'image',
					array(
						'instructions'  => __( 'Фоновое изображение hero. Если пусто — fallback по теме/макету.', 'shpigovsky-core' ),
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field(
					'field_fp02_hero_cta_label_service',
					__( 'Текст кнопки в hero-блоке', 'shpigovsky-core' ),
					'hero_cta_label',
					'text',
					array(
						'instructions' => __( 'Индивидуальный текст кнопки для hero. Если пусто — текст по умолчанию.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_hero_cta_target_service',
					__( 'Ссылка кнопки (CTA)', 'shpigovsky-core' ),
					'hero_cta_target',
					'url'
				),
			),
			self::location( 'post_type', '==', 'service' )
		);
		$group['menu_order']  = 1;
		$group['description'] = 'FP-0002 V9-06E46-FIX01: shared service hero fields (section + service). Meta keys preserved.';
		return $group;
	}

	/**
	 * Service structured sections group.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_structured_sections() {
		// Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.
		$group = self::group(
			'group_fp02_service_structured_sections',
			'Service — Structured Sections',
			array(
				self::field( 'field_fp02_intro_text_service', 'Intro text', 'intro_text', 'textarea', array( 'rows' => 5 ) ),
				self::field( 'field_fp02_intro_note_service', 'Intro note', 'intro_note', 'textarea', array( 'rows' => 3 ) ),
				self::repeater(
					'field_fp02_signs_items_service',
					'Признаки / симптомы',
					'signs_items',
					12,
					array(
						self::field(
							'field_fp02_signs_item_title_service',
							'Заголовок',
							'title',
							'text',
							array(
								'required'     => 0,
								'instructions' => 'Optional.',
							)
						),
						self::field(
							'field_fp02_signs_item_text_service',
							'Текст',
							'text',
							'textarea',
							array(
								'required'     => 0,
								'rows'         => 3,
								'instructions' => 'Optional.',
							)
						),
					),
					0,
					array(
						'required'     => 0,
						'instructions' => 'Optional. Empty section does not block save.',
					)
				),
				self::repeater(
					'field_fp02_programme_items_service',
					'Пункты программы',
					'programme_items',
					6,
					array(
						self::field(
							'field_fp02_programme_item_title_service',
							'Заголовок',
							'title',
							'text',
							array(
								'required'     => 0,
								'instructions' => 'Optional. Leave empty to omit row on save.',
							)
						),
						self::field(
							'field_fp02_programme_item_text_service',
							'Текст',
							'text',
							'textarea',
							array(
								'required'     => 0,
								'rows'         => 3,
								'instructions' => 'Optional. Theme uses static fallback when programme block is empty.',
							)
						),
					),
					0,
					array(
						'required'     => 0,
						'instructions' => 'Optional programme block. Empty or partial rows do not block save; frontend falls back to static V9 programme when unset.',
					)
				),
				self::repeater(
					'field_fp02_stages_service',
					'Этапы',
					'stages',
					8,
					array(
						self::field(
							'field_fp02_stage_title_service',
							'Заголовок',
							'title',
							'text',
							array(
								'required'     => 0,
								'instructions' => 'Optional.',
							)
						),
						self::field(
							'field_fp02_stage_text_service',
							'Текст',
							'text',
							'textarea',
							array(
								'required'     => 0,
								'rows'         => 3,
								'instructions' => 'Optional.',
							)
						),
					),
					0,
					array(
						'required'     => 0,
						'instructions' => 'Optional. Empty section does not block save.',
					)
				),
				self::field( 'field_fp02_cta_title_service', 'CTA title', 'cta_title', 'text' ),
				self::field( 'field_fp02_cta_text_service', 'CTA text', 'cta_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_cta_button_label_service', 'CTA button label', 'cta_button_label', 'text' ),
				self::field( 'field_fp02_cta_button_target_service', 'CTA button target', 'cta_button_target', 'url' ),
			),
			self::location( 'post_type', '==', 'service' )
		);
		$group['active']      = false;
		$group['description'] = 'Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.';
		return $group;
	}

	/**
	 * Service FAQ group.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_faq() {
		return self::group(
			'group_fp02_service_faq',
			'Service — FAQ',
			array(
				self::repeater(
					'field_fp02_faq_items_service',
					'FAQ',
					'faq_items',
					15,
					array(
						self::field( 'field_fp02_faq_question_service', 'Вопрос', 'question', 'text' ),
						self::field( 'field_fp02_faq_answer_service', 'Ответ', 'answer', 'textarea', array( 'rows' => 4 ) ),
					)
				),
			),
			self::location( 'post_type', '==', 'service' )
		);
	}

	/**
	 * Service relationships group.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_relationships() {
		// Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.
		$group = self::group(
			'group_fp02_service_relationships',
			'Service — Relationships / Related Services',
			array(
				self::field(
					'field_fp02_manual_related_services',
					'Связанные услуги вручную',
					'manual_related_services',
					'relationship',
					array(
						'instructions' => 'Optional override. Fallback behavior is derived sibling query.',
						'post_type'    => array( 'service' ),
						'max'          => 6,
						'return_format'=> 'object',
					)
				),
			),
			self::location( 'post_type', '==', 'service' )
		);
		$group['active']      = false;
		$group['description'] = 'Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.';
		return $group;
	}

	/**
	 * Home page group.
	 *
	 * V9-06E39: admin field order follows front-page.php Home partial sequence.
	 * V9-06E40: editable blocks expansion (benefits, treatment heading/lead, gallery
	 * settings, why-us, staff/landscape images, recovery-life, genotyping, videos).
	 * Labels/instructions use Russian source strings + shpigovsky-core i18n.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_home() {
		$gallery_mode_key  = 'field_fp02_home_gallery_display_mode';
		$gallery_count_key = 'field_fp02_home_gallery_random_count';
		$gallery_sel_key   = 'field_fp02_home_gallery_selected_services';

		return self::group(
			'group_fp02_page_home',
			__( 'Страница — Главная', 'shpigovsky-core' ),
			array(
				// 1. Hero (template-parts/home/hero.php)
				self::field(
					'field_fp02_hero_media_home',
					__( 'Изображение hero (устарело)', 'shpigovsky-core' ),
					'hero_media',
					'image',
					array(
						'instructions'  => __( 'Устарело: используйте «Слайды hero». Поле скрыто в админке; значение сохранено как legacy fallback.', 'shpigovsky-core' ),
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_hero_cta_label_home',
					__( 'Текст кнопки в hero-блоке', 'shpigovsky-core' ),
					'hero_cta_label',
					'text',
					array(
						'instructions' => __( 'Индивидуальный текст кнопки для hero-блока этой страницы. Если оставить пустым, используется текущий текст по умолчанию.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_home_hero_slides',
					__( 'Слайды hero', 'shpigovsky-core' ),
					'home_hero_slides',
					5,
					array(
						self::field( 'field_fp02_home_hero_title', __( 'Заголовок', 'shpigovsky-core' ), 'title', 'text' ),
						self::field( 'field_fp02_home_hero_text', __( 'Текст', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 3 ) ),
						self::field( 'field_fp02_home_hero_image', __( 'Изображение', 'shpigovsky-core' ), 'image', 'image', array( 'return_format' => 'array' ) ),
					),
					0,
					array(
						'instructions' => __( 'Слайды hero на главной. При двух и более слайдах включается слайдер. Ограниченный повторитель; максимум строк задан в исходнике и проверках.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_hero_autoplay_enabled',
					__( 'Hero — автопрокрутка', 'shpigovsky-core' ),
					'home_hero_autoplay_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Автопрокрутка слайдов hero (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_home_hero_autoplay_delay',
					__( 'Hero — задержка автопрокрутки (мс)', 'shpigovsky-core' ),
					'home_hero_autoplay_delay',
					'number',
					array(
						'instructions'  => __( 'Пауза между слайдами в миллисекундах. По умолчанию 5000.', 'shpigovsky-core' ),
						'default_value' => 5000,
						'min'           => 1000,
						'max'           => 60000,
						'step'          => 500,
					)
				),
				self::field(
					'field_fp02_home_hero_arrows_enabled',
					__( 'Hero — стрелки', 'shpigovsky-core' ),
					'home_hero_arrows_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показывать стрелки навигации (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_home_hero_dots_enabled',
					__( 'Hero — точки', 'shpigovsky-core' ),
					'home_hero_dots_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показывать точки пагинации (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 2. Recovery intro (template-parts/home/recovery-intro.php)
				self::field(
					'field_fp02_home_recovery_intro_heading',
					__( 'Введение о восстановлении — заголовок', 'shpigovsky-core' ),
					'home_recovery_intro_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Шпиговский дом — восстановление…» на главной.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_recovery_intro_lead_1',
					__( 'Введение о восстановлении — абзац 1', 'shpigovsky-core' ),
					'home_recovery_intro_lead_1',
					'textarea',
					array(
						'rows'         => 4,
						'instructions' => __( 'Первый абзац блока введения о восстановлении на главной.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_recovery_intro_lead_2',
					__( 'Введение о восстановлении — абзац 2', 'shpigovsky-core' ),
					'home_recovery_intro_lead_2',
					'textarea',
					array(
						'rows'         => 4,
						'instructions' => __( 'Второй абзац блока введения о восстановлении на главной.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_recovery_intro_benefits_enabled',
					__( 'Список преимуществ — показывать', 'shpigovsky-core' ),
					'home_recovery_intro_benefits_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Включить или скрыть список преимуществ в блоке введения о восстановлении.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_recovery_intro_benefits',
					__( 'Список преимуществ', 'shpigovsky-core' ),
					'home_recovery_intro_benefits',
					12,
					array(
						self::field( 'field_fp02_home_recovery_intro_benefit_text', __( 'Текст пункта', 'shpigovsky-core' ), 'text', 'text' ),
						self::field(
							'field_fp02_home_recovery_intro_benefit_enabled',
							__( 'Показывать пункт', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Пункты списка преимуществ (ul.home-recovery-intro__benefits).', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::repeater(
					'field_fp02_home_intro_bands',
					__( 'Карточки введения', 'shpigovsky-core' ),
					'home_intro_bands',
					6,
					self::title_text_subfields( 'home_intro_bands' ),
					0,
					array(
						'instructions' => __( 'Карточки в блоке введения о восстановлении. Ограниченный повторитель; максимум строк задан в исходнике и проверках.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				// 3. Founder quote — automated / options (template-parts/home/founder-quote.php)
				self::field(
					'field_fp02_home_founder_quote_source_notice',
					__( 'Цитата основателя на главной', 'shpigovsky-core' ),
					'home_founder_quote_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: цитата основателя берётся из «Настройки сайта → Цитата основателя». На главной отдельных полей контента нет — только показ/скрытие.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_founder_quote_visible',
					__( 'Показывать цитату основателя', 'shpigovsky-core' ),
					'home_founder_quote_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть блок цитаты основателя на главной. Контент блока не редактируется здесь.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 4. Treatment & prevention (template-parts/home/treatment-prevention.php)
				self::field(
					'field_fp02_home_treatment_prevention_heading',
					__( 'Лечение и профилактика — заголовок', 'shpigovsky-core' ),
					'home_treatment_prevention_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок секции «Лечение и профилактика» на главной.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_treatment_prevention_lead',
					__( 'Лечение и профилактика — описание', 'shpigovsky-core' ),
					'home_treatment_prevention_lead',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Лид/описание под заголовком секции «Лечение и профилактика».', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_treatment_source_notice',
					__( 'Лечение и профилактика — аккордеон', 'shpigovsky-core' ),
					'home_treatment_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: аккордеон услуг формируется из иерархии CPT service. Редактируйте услуги в каталоге «Услуги». Заголовок и описание секции редактируются полями выше.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_treatment_prevention_visible',
					__( 'Показывать блок «Лечение и профилактика»', 'shpigovsky-core' ),
					'home_treatment_prevention_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть весь блок на главной (включая аккордеон услуг).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 5. Gallery / service slider (template-parts/home/gallery.php)
				self::field(
					'field_fp02_home_gallery_source_notice',
					__( 'Галерея на главной', 'shpigovsky-core' ),
					'home_gallery_source_notice',
					'message',
					array(
						'message' => __( 'Слайдер галереи строится из услуг (CPT service) с флагом «Показывать в слайдере на главной». Ниже — режим отображения. Ручной блок Gallery / media bands не используется.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_gallery_visible',
					__( 'Показывать галерею на главной', 'shpigovsky-core' ),
					'home_gallery_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть слайдер галереи услуг на главной.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					$gallery_mode_key,
					__( 'Галерея — режим отображения', 'shpigovsky-core' ),
					'home_gallery_display_mode',
					'select',
					array(
						'instructions'  => __( 'Как выбирать услуги для слайдера на главной. Eligible = опубликованные услуги 1-го уровня с включённым флагом «Показывать в слайдере на главной».', 'shpigovsky-core' ),
						'choices'       => array(
							'all'      => __( 'Показать все подходящие услуги', 'shpigovsky-core' ),
							'random'   => __( 'Показать случайные N услуг', 'shpigovsky-core' ),
							'selected' => __( 'Показать только выбранные услуги', 'shpigovsky-core' ),
						),
						'default_value' => 'random',
						'allow_null'    => 0,
						'ui'            => 1,
						'return_format' => 'value',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					$gallery_count_key,
					__( 'Галерея — число случайных услуг', 'shpigovsky-core' ),
					'home_gallery_random_count',
					'number',
					array(
						'instructions'      => __( 'Сколько случайных eligible-услуг показывать (режим «случайные N»). По умолчанию 12.', 'shpigovsky-core' ),
						'default_value'     => 12,
						'min'               => 1,
						'max'               => 48,
						'step'              => 1,
						'conditional_logic' => array(
							array(
								array(
									'field'    => $gallery_mode_key,
									'operator' => '==',
									'value'    => 'random',
								),
							),
						),
					)
				),
				self::field(
					$gallery_sel_key,
					__( 'Галерея — выбранные услуги', 'shpigovsky-core' ),
					'home_gallery_selected_services',
					'relationship',
					array(
						'instructions'      => __( 'Услуги для режима «только выбранные». Порядок выбора сохраняется. Если список пуст — fallback на случайные N. Учитываются только опубликованные eligible-услуги.', 'shpigovsky-core' ),
						'post_type'         => array( 'service' ),
						'filters'           => array( 'search' ),
						'return_format'     => 'id',
						'max'               => 48,
						'conditional_logic' => array(
							array(
								array(
									'field'    => $gallery_mode_key,
									'operator' => '==',
									'value'    => 'selected',
								),
							),
						),
					)
				),
				// 6. Why-us (template-parts/home/why-us.php)
				self::field(
					'field_fp02_home_why_us_heading',
					__( 'Почему нас выбирают — заголовок', 'shpigovsky-core' ),
					'home_why_us_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Почему нас выбирают» на главной.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_why_us_lead',
					__( 'Почему нас выбирают — лид', 'shpigovsky-core' ),
					'home_why_us_lead',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Лид блока «Почему нас выбирают».', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_why_us_body_enabled',
					__( 'Почему нас выбирают — абзацы показывать', 'shpigovsky-core' ),
					'home_why_us_body_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть абзацы тела блока.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_why_us_body',
					__( 'Почему нас выбирают — абзацы', 'shpigovsky-core' ),
					'home_why_us_body',
					6,
					array(
						self::field( 'field_fp02_home_why_us_body_text', __( 'Текст', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 3 ) ),
						self::field(
							'field_fp02_home_why_us_body_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Абзацы .home-why-us__body.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_why_us_items_enabled',
					__( 'Почему нас выбирают — список ссылок показывать', 'shpigovsky-core' ),
					'home_why_us_items_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть список ссылок в блоке.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_why_us_items',
					__( 'Почему нас выбирают — ссылки', 'shpigovsky-core' ),
					'home_why_us_items',
					12,
					array(
						self::field( 'field_fp02_home_why_us_item_title', __( 'Название', 'shpigovsky-core' ), 'title', 'text' ),
						self::field( 'field_fp02_home_why_us_item_url', __( 'Ссылка', 'shpigovsky-core' ), 'url', 'url' ),
						self::field(
							'field_fp02_home_why_us_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Ссылки-пункты списка в блоке «Почему нас выбирают».', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				// 7. Staff photo (template-parts/home/staff-photo.php)
				self::field(
					'field_fp02_home_staff_photo_image',
					__( 'Фото команды', 'shpigovsky-core' ),
					'home_staff_photo_image',
					'image',
					array(
						'instructions'  => __( 'Изображение блока «Команда центра». Выберите из медиабиблиотеки.', 'shpigovsky-core' ),
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				// 8. Feature grid / advantages (template-parts/home/feature-grid.php)
				self::repeater(
					'field_fp02_home_advantages',
					__( 'Преимущества / доверие', 'shpigovsky-core' ),
					'home_advantages',
					8,
					self::title_text_subfields( 'home_advantages' ),
					0,
					array(
						'instructions' => __( 'Карточки преимуществ (feature grid) на главной. Ограниченный повторитель; максимум строк задан в исходнике и проверках.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				// 9. Clinic landscape (template-parts/home/clinic-landscape.php)
				self::field(
					'field_fp02_home_clinic_landscape_image',
					__( 'Территория клиники — изображение', 'shpigovsky-core' ),
					'home_clinic_landscape_image',
					'image',
					array(
						'instructions'  => __( 'Изображение блока «Территория клиники». Выберите из медиабиблиотеки.', 'shpigovsky-core' ),
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				// 10. Recovery life (template-parts/home/recovery-life.php)
				self::field(
					'field_fp02_home_recovery_life_heading',
					__( 'Как меняется жизнь — заголовок', 'shpigovsky-core' ),
					'home_recovery_life_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Как меняется жизнь человека в процессе восстановления».', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_recovery_life_highlight',
					__( 'Как меняется жизнь — акцент', 'shpigovsky-core' ),
					'home_recovery_life_highlight',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Выделенный абзац (.home-recovery-life__highlight).', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_recovery_life_intro_enabled',
					__( 'Как меняется жизнь — вводные абзацы показывать', 'shpigovsky-core' ),
					'home_recovery_life_intro_enabled',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_recovery_life_intro',
					__( 'Как меняется жизнь — вводные абзацы', 'shpigovsky-core' ),
					'home_recovery_life_intro',
					6,
					array(
						self::field( 'field_fp02_home_recovery_life_intro_text', __( 'Текст', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 3 ) ),
						self::field(
							'field_fp02_home_recovery_life_intro_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_recovery_life_stages_enabled',
					__( 'Как меняется жизнь — этапы показывать', 'shpigovsky-core' ),
					'home_recovery_life_stages_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть список этапов восстановления.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_recovery_life_stages',
					__( 'Как меняется жизнь — этапы', 'shpigovsky-core' ),
					'home_recovery_life_stages',
					8,
					array(
						self::field(
							'field_fp02_home_recovery_life_stage_label',
							__( 'Подпись месяца', 'shpigovsky-core' ),
							'stage_label',
							'text',
							array(
								'instructions' => __( 'Красная подпись над карточкой этапа (например «1 месяц»). Если пусто — подставляется порядковый номер.', 'shpigovsky-core' ),
							)
						),
						self::field( 'field_fp02_home_recovery_life_stage_title', __( 'Заголовок этапа', 'shpigovsky-core' ), 'title', 'text' ),
						self::field(
							'field_fp02_home_recovery_life_stage_items',
							__( 'Пункты этапа (по одному в строке)', 'shpigovsky-core' ),
							'items_text',
							'textarea',
							array(
								'rows'         => 6,
								'instructions' => __( 'Каждый пункт списка — отдельная строка.', 'shpigovsky-core' ),
							)
						),
						self::field(
							'field_fp02_home_recovery_life_stage_enabled',
							__( 'Показывать этап', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Этапы .home-recovery-life__stages.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				// 11. Reviews — automated (template-parts/home/reviews.php)
				self::field(
					'field_fp02_home_reviews_source_notice',
					__( 'Отзывы на главной', 'shpigovsky-core' ),
					'home_reviews_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: заголовок и список отзывов — «Настройки сайта / Отзывы». Home-мета home_reviews_heading — только fallback, в админке главной не показывается.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_reviews_visible',
					__( 'Показывать отзывы на главной', 'shpigovsky-core' ),
					'home_reviews_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть блок отзывов на главной. Контент редактируется в «Отзывы».', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 12. Rehab requirements — automated reusable
				self::field(
					'field_fp02_home_rehab_requirements_source_notice',
					__( 'Условия реабилитации на главной', 'shpigovsky-core' ),
					'home_rehab_requirements_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: контент берётся из «Повторяемые блоки — Условия реабилитации». На главной — только показ/скрытие.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_rehab_requirements_visible',
					__( 'Показывать блок условий реабилитации', 'shpigovsky-core' ),
					'home_rehab_requirements_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 13. Rehab program — automated direction cards + editable intro
				self::field(
					'field_fp02_home_rehab_program_source_notice',
					__( 'Программа / направления на главной', 'shpigovsky-core' ),
					'home_rehab_program_source_notice',
					'message',
					array(
						'message'  => self::home_rehab_program_source_notice_message(),
						'esc_html' => 0,
						'wrapper'  => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_rehabilitation_program_head',
					__( 'Программа — заголовок', 'shpigovsky-core' ),
					'home_rehabilitation_program_head',
					'text',
					array(
						'instructions' => __( 'Заголовок секции программы / направлений на главной (рядом со ссылкой «подробнее»).', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_rehabilitation_program_lead',
					__( 'Программа — описание', 'shpigovsky-core' ),
					'home_rehabilitation_program_lead',
					'textarea',
					array(
						'instructions' => __( 'Короткое описание (лид) под заголовком секции.', 'shpigovsky-core' ),
						'rows'         => 3,
						'new_lines'    => '',
					)
				),
				self::field(
					'field_fp02_home_rehabilitation_program_intro_1',
					__( 'Программа — вводный текст 1', 'shpigovsky-core' ),
					'home_rehabilitation_program_intro_1',
					'textarea',
					array(
						'instructions' => __( 'Первый вводный абзац перед карточками направлений.', 'shpigovsky-core' ),
						'rows'         => 4,
						'new_lines'    => '',
					)
				),
				self::field(
					'field_fp02_home_rehabilitation_program_intro_2',
					__( 'Программа — вводный текст 2', 'shpigovsky-core' ),
					'home_rehabilitation_program_intro_2',
					'textarea',
					array(
						'instructions' => __( 'Второй вводный абзац перед карточками направлений.', 'shpigovsky-core' ),
						'rows'         => 4,
						'new_lines'    => '',
					)
				),
				self::field(
					'field_fp02_home_rehab_program_visible',
					__( 'Показывать блок программы / направлений', 'shpigovsky-core' ),
					'home_rehab_program_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 14. genotyping editable
				self::field(
					'field_fp02_home_genotyping_heading',
					__( 'Генотипирование — заголовок', 'shpigovsky-core' ),
					'home_genotyping_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока генотипирования на главной (не путать со страницей программы генотипирования).', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_genotyping_link_text',
					__( 'Генотипирование — текст ссылки', 'shpigovsky-core' ),
					'home_genotyping_link_text',
					'text',
					array(
						'instructions' => __( 'Текст ссылки «подробнее» рядом с заголовком.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_genotyping_link_url',
					__( 'Генотипирование — URL ссылки', 'shpigovsky-core' ),
					'home_genotyping_link_url',
					'url',
					array(
						'instructions' => __( 'URL ссылки «подробнее». Если пусто — используется текущий URL услуги.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_genotyping_lead',
					__( 'Генотипирование — лид', 'shpigovsky-core' ),
					'home_genotyping_lead',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::field(
					'field_fp02_home_genotyping_body_enabled',
					__( 'Генотипирование — абзацы тела показывать', 'shpigovsky-core' ),
					'home_genotyping_body_enabled',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_genotyping_body',
					__( 'Генотипирование — абзацы тела', 'shpigovsky-core' ),
					'home_genotyping_body',
					6,
					array(
						self::field( 'field_fp02_home_genotyping_body_text', __( 'Текст', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 4 ) ),
						self::field(
							'field_fp02_home_genotyping_body_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_genotyping_subheading',
					__( 'Генотипирование — подзаголовок списка', 'shpigovsky-core' ),
					'home_genotyping_subheading',
					'text'
				),
				self::field(
					'field_fp02_home_genotyping_list_intro',
					__( 'Генотипирование — текст перед списком', 'shpigovsky-core' ),
					'home_genotyping_list_intro',
					'textarea',
					array(
						'rows' => 4,
					)
				),
				self::field(
					'field_fp02_home_genotyping_items_enabled',
					__( 'Генотипирование — список показывать', 'shpigovsky-core' ),
					'home_genotyping_items_enabled',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_genotyping_items',
					__( 'Генотипирование — пункты списка', 'shpigovsky-core' ),
					'home_genotyping_items',
					12,
					array(
						self::field( 'field_fp02_home_genotyping_item_text', __( 'Текст пункта', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 2 ) ),
						self::field(
							'field_fp02_home_genotyping_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_genotyping_cta_label',
					__( 'Генотипирование — текст кнопки', 'shpigovsky-core' ),
					'home_genotyping_cta_label',
					'text',
					array(
						'instructions' => __( 'Текст кнопки записи на консультацию в блоке генотипирования.', 'shpigovsky-core' ),
					)
				),
				// 15. Comfort — automated (template-parts/home/comfort.php)
				self::field(
					'field_fp02_home_comfort_source_notice',
					__( 'Комфорт на главной', 'shpigovsky-core' ),
					'home_comfort_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: заголовок и лид блока «Комфорт» берутся из «Повторяемые блоки — Комфорт / преимущества». Home-мета home_comfort_* — только fallback, в админке главной не показываются.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_comfort_visible',
					__( 'Показывать блок «Комфорт»', 'shpigovsky-core' ),
					'home_comfort_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть блок комфорта на главной.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 16. Videos (template-parts/home/videos.php)
				self::field(
					'field_fp02_home_videos_heading',
					__( 'Видео — заголовок', 'shpigovsky-core' ),
					'home_videos_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Видео о нашем центре».', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_videos_items_enabled',
					__( 'Видео — список показывать', 'shpigovsky-core' ),
					'home_videos_items_enabled',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::repeater(
					'field_fp02_home_videos_items',
					__( 'Видео — элементы', 'shpigovsky-core' ),
					'home_videos_items',
					8,
					array(
						self::field( 'field_fp02_home_videos_item_title', __( 'Заголовок / подпись', 'shpigovsky-core' ), 'title', 'text' ),
						self::field(
							'field_fp02_home_videos_item_file',
							__( 'Видеофайл (медиабиблиотека)', 'shpigovsky-core' ),
							'video_file',
							'file',
							array(
								'return_format' => 'array',
								'library'       => 'all',
								'mime_types'    => 'mp4,webm,ogg',
							)
						),
						self::field(
							'field_fp02_home_videos_item_poster',
							__( 'Постер', 'shpigovsky-core' ),
							'poster',
							'image',
							array(
								'return_format' => 'array',
								'preview_size'  => 'medium',
							)
						),
						self::field(
							'field_fp02_home_videos_item_enabled',
							__( 'Показывать', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Видео из медиабиблиотеки WordPress. Сохраняется разметка fancybox/ссылки текущего фронтенда.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				// 17. Specialists — automated (template-parts/home/specialists.php)
				self::field(
					'field_fp02_home_specialists_source_notice',
					__( 'Специалисты на главной', 'shpigovsky-core' ),
					'home_specialists_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: карточки специалистов берутся из CPT «Специалисты» (меню Специалисты). Заголовок секции редактируйте в «Повторяемые блоки — Специалисты». Поле home_specialists_heading на главной сохранено только как fallback и скрыто из админки.', 'shpigovsky-core' ),
						'wrapper' => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_specialists_visible',
					__( 'Показывать специалистов на главной', 'shpigovsky-core' ),
					'home_specialists_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть слайдер специалистов на главной.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 18. Articles teaser (template-parts/home/articles-teaser.php)
				self::field(
					'field_fp02_home_articles_heading',
					__( 'Статьи — заголовок', 'shpigovsky-core' ),
					'home_articles_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Статьи» на главной. Сами карточки — опубликованные записи блога.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_home_articles_source_notice',
					__( 'Статьи на главной', 'shpigovsky-core' ),
					'home_articles_source_notice',
					'message',
					array(
						'message' => __( 'Автоматический блок: слайдер статей на главной формируется из опубликованных записей (posts). Переключатель Blog teaser enabled снят — тема его не читает.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_articles_visible',
					__( 'Показывать статьи на главной', 'shpigovsky-core' ),
					'home_articles_visible',
					'true_false',
					array(
						'instructions'  => __( 'Показать или скрыть блок статей на главной.', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 19. FAQ (template-parts/home/faq.php)
				self::field(
					'field_fp02_home_faq_heading',
					__( 'Заголовок FAQ', 'shpigovsky-core' ),
					'home_faq_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок секции FAQ на главной (например «Нас часто спрашивают»).', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_home_faq_items',
					__( 'Вопросы и ответы (FAQ)', 'shpigovsky-core' ),
					'home_faq_items',
					15,
					self::faq_subfields( 'home' ),
					0,
					array(
						'instructions' => __( 'Вопросы и ответы на главной. Ограниченный повторитель; максимум строк задан в исходнике и проверках.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				// 20. Final form / CTA (template-parts/components/final-form.php)
				self::field(
					'field_fp02_home_cta_title',
					__( 'CTA / форма — заголовок (fallback)', 'shpigovsky-core' ),
					'home_cta_title',
					'text',
					array(
						'instructions' => __( 'Fallback-заголовок финальной формы на главной. Приоритет: «Повторяемые блоки — Финальная форма», затем это поле, затем статический текст темы.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_home_cta_text',
					__( 'CTA / форма — текст (fallback)', 'shpigovsky-core' ),
					'home_cta_text',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => __( 'Fallback-текст финальной формы на главной. Приоритет: «Повторяемые блоки — Финальная форма», затем это поле, затем статический текст темы.', 'shpigovsky-core' ),
					)
				),
			),
			self::location( 'page_type', '==', 'front_page' )
		);
	}

	/**
	 * Services hub page group (/uslugi/) — V9-06E43 admin parity.
	 * Admin field order follows page-templates/services-hub.php frontend stack.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_services_hub() {
		return self::group(
			'group_fp02_page_services_hub',
			__( 'Страница — Услуги (хаб)', 'shpigovsky-core' ),
			array(
				// 1. Hero — services-inner-hero-v2
				self::field(
					'field_fp02_hero_cta_label_hub',
					__( 'Текст кнопки в hero-блоке', 'shpigovsky-core' ),
					'hero_cta_label',
					'text',
					array(
						'instructions' => __( 'Индивидуальный текст кнопки для hero-блока страницы «Услуги». Если оставить пустым, используется текст по умолчанию. На слайде можно задать свой текст кнопки.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_services_hero_slides',
					__( 'Слайды hero', 'shpigovsky-core' ),
					'services_hero_slides',
					5,
					array(
						self::field( 'field_fp02_services_hero_slide_eyebrow', __( 'Надзаголовок', 'shpigovsky-core' ), 'eyebrow', 'text' ),
						self::field( 'field_fp02_services_hero_slide_title', __( 'Заголовок', 'shpigovsky-core' ), 'title', 'text' ),
						self::field( 'field_fp02_services_hero_slide_lead', __( 'Лид', 'shpigovsky-core' ), 'lead', 'textarea', array( 'rows' => 4 ) ),
						self::field( 'field_fp02_services_hero_slide_image', __( 'Изображение', 'shpigovsky-core' ), 'image', 'image', array( 'return_format' => 'array', 'preview_size' => 'medium' ) ),
						self::field( 'field_fp02_services_hero_slide_cta', __( 'Текст кнопки слайда', 'shpigovsky-core' ), 'cta_label', 'text', array( 'instructions' => __( 'Пусто — используется общая кнопка hero страницы.', 'shpigovsky-core' ) ) ),
						self::field(
							'field_fp02_services_hero_slide_enabled',
							__( 'Показывать слайд', 'shpigovsky-core' ),
							'item_enabled',
							'true_false',
							array(
								'default_value' => 1,
								'ui'            => 1,
							)
						),
					),
					0,
					array(
						'instructions' => __( 'Слайды hero на /uslugi/ (дизайн services-inner-hero-v2). При двух и более слайдах включается горизонтальный слайдер. Максимум 5 слайдов.', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить слайд', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hero_autoplay_enabled',
					__( 'Hero — автопрокрутка', 'shpigovsky-core' ),
					'services_hero_autoplay_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Автопрокрутка слайдов hero (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_services_hero_autoplay_delay',
					__( 'Hero — задержка автопрокрутки (мс)', 'shpigovsky-core' ),
					'services_hero_autoplay_delay',
					'number',
					array(
						'instructions'  => __( 'Пауза между слайдами в миллисекундах. По умолчанию 5000.', 'shpigovsky-core' ),
						'default_value' => 5000,
						'min'           => 1000,
						'max'           => 60000,
						'step'          => 500,
					)
				),
				self::field(
					'field_fp02_services_hero_arrows_enabled',
					__( 'Hero — стрелки', 'shpigovsky-core' ),
					'services_hero_arrows_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показывать стрелки навигации (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_services_hero_dots_enabled',
					__( 'Hero — точки', 'shpigovsky-core' ),
					'services_hero_dots_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Показывать точки пагинации (только если слайдов больше одного).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// Legacy hero fields — retained as fallback, hidden in admin.
				self::field(
					'field_fp02_hero_eyebrow_hub',
					__( 'Hero eyebrow (устарело)', 'shpigovsky-core' ),
					'hero_eyebrow',
					'text',
					array(
						'instructions' => __( 'Устарело: используйте «Слайды hero». Скрыто в админке; значение — legacy fallback.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_hero_title_override_hub',
					__( 'Hero H1 (устарело)', 'shpigovsky-core' ),
					'hero_title_override',
					'text',
					array(
						'instructions' => __( 'Устарело: используйте «Слайды hero». Скрыто в админке; значение — legacy fallback.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_hero_media_hub',
					__( 'Изображение hero (устарело)', 'shpigovsky-core' ),
					'hero_media',
					'image',
					array(
						'instructions'  => __( 'Устарело: используйте «Слайды hero». Скрыто в админке; значение — legacy fallback.', 'shpigovsky-core' ),
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_intro',
					__( 'Hero lead (устарело)', 'shpigovsky-core' ),
					'services_hub_intro',
					'textarea',
					array(
						'rows'         => 5,
						'instructions' => __( 'Устарело: используйте лид в «Слайдах hero». Скрыто в админке; значение — legacy fallback.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				// 2. Internal page nav
				self::field(
					'field_fp02_services_hub_nav_notice',
					__( 'Навигация по разделам', 'shpigovsky-core' ),
					'services_hub_nav_notice',
					'message',
					array(
						'message'   => self::services_hub_catalog_source_notice_message(
							__( 'Автоматический блок: пункты поднавигации строятся <strong class="fp02-acf-notice-danger">из родительских услуг CPT</strong>. На странице «Услуги» — только показ/скрытие.', 'shpigovsky-core' )
						),
						'new_lines' => 'wpautop',
						'esc_html'  => 0,
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_nav_visible',
					__( 'Показывать навигацию по разделам', 'shpigovsky-core' ),
					'services_hub_nav_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 3. Service category groups / catalog
				self::field(
					'field_fp02_services_hub_catalog_notice',
					__( 'Каталог услуг по разделам', 'shpigovsky-core' ),
					'services_hub_catalog_notice',
					'message',
					array(
						'message'   => self::services_hub_catalog_source_notice_message(
							__( 'Автоматический блок: карточки и галереи разделов строятся <strong class="fp02-acf-notice-danger">из страниц услуг</strong>. На странице «Услуги» — настройки показа, режим списка и подписи к слайдерам категорий.', 'shpigovsky-core' )
						),
						'new_lines' => 'wpautop',
						'esc_html'  => 0,
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_catalog_visible',
					__( 'Показывать каталог разделов', 'shpigovsky-core' ),
					'services_hub_catalog_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_services_hub_query_mode',
					__( 'Режим отображения каталога', 'shpigovsky-core' ),
					'services_hub_query_mode',
					'select',
					array(
						'choices'       => array(
							'grouped_by_parent' => __( 'Группами по родительским услугам', 'shpigovsky-core' ),
							'flat'              => __( 'Плоский список', 'shpigovsky-core' ),
						),
						'default_value' => 'grouped_by_parent',
						'instructions'  => __( 'Сгруппированный режим — канон V9 для /uslugi/.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_services_hub_show_placeholders',
					__( 'Показывать услуги-заглушки', 'shpigovsky-core' ),
					'services_hub_show_placeholders',
					'true_false',
					array(
						'instructions'  => __( 'Технический переключатель. В проде обычно выключен.', 'shpigovsky-core' ),
						'default_value' => 0,
						'ui'            => 1,
					)
				),
				self::field(
					'field_fp02_services_hub_category_gallery_dots_enabled',
					__( 'Галереи разделов — точки', 'shpigovsky-core' ),
					'services_hub_category_gallery_dots_enabled',
					'true_false',
					array(
						'instructions'  => __( 'Точки пагинации у слайдеров карточек внутри разделов (как после E33-FIX01).', 'shpigovsky-core' ),
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 4. Rehabilitation program
				self::field(
					'field_fp02_services_hub_program_heading',
					__( 'Программа — заголовок', 'shpigovsky-core' ),
					'services_hub_program_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока «Наша программа включает…». Пусто — static V9 fallback.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_program_lead',
					__( 'Программа — лид', 'shpigovsky-core' ),
					'services_hub_program_lead',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::field(
					'field_fp02_services_hub_program_intro',
					__( 'Программа — описание', 'shpigovsky-core' ),
					'services_hub_program_intro',
					'textarea',
					array(
						'rows' => 5,
					)
				),
				self::field(
					'field_fp02_services_hub_program_cta_title',
					__( 'Программа — CTA заголовок', 'shpigovsky-core' ),
					'services_hub_program_cta_title',
					'text'
				),
				self::field(
					'field_fp02_services_hub_program_cta_subtitle',
					__( 'Программа — CTA подзаголовок', 'shpigovsky-core' ),
					'services_hub_program_cta_subtitle',
					'text'
				),
				self::field(
					'field_fp02_services_hub_program_cta_button',
					__( 'Программа — CTA кнопка', 'shpigovsky-core' ),
					'services_hub_program_cta_button',
					'text'
				),
				self::field(
					'field_fp02_services_hub_program_notice',
					__( 'Программа — источник карточек', 'shpigovsky-core' ),
					'services_hub_program_notice',
					'message',
					array(
						'message'   => self::services_hub_program_source_notice_message(),
						'new_lines' => 'wpautop',
						'esc_html'  => 0,
					)
				),
				self::field(
					'field_fp02_services_hub_program_visible',
					__( 'Показывать блок программы', 'shpigovsky-core' ),
					'services_hub_program_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 5. Founder quote (automated/shared)
				self::field(
					'field_fp02_services_hub_founder_notice',
					__( 'Цитата основателя', 'shpigovsky-core' ),
					'services_hub_founder_notice',
					'message',
					array(
						'message'   => __( 'Автоматический / общий блок: контент цитаты общий с главной (шаблон founder-quote). На странице «Услуги» — только показ/скрытие.', 'shpigovsky-core' ),
						'new_lines' => 'wpautop',
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_founder_quote_visible',
					__( 'Показывать цитату основателя', 'shpigovsky-core' ),
					'services_hub_founder_quote_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 6. Comfort (reusable block)
				self::field(
					'field_fp02_services_hub_comfort_notice',
					__( 'Комфорт', 'shpigovsky-core' ),
					'services_hub_comfort_notice',
					'message',
					array(
						'message'   => __( 'Автоматический блок: заголовок, лид и галерея берутся из «Повторяемые блоки — Комфорт / преимущества». На странице «Услуги» — только показ/скрытие.', 'shpigovsky-core' ),
						'new_lines' => 'wpautop',
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_comfort_visible',
					__( 'Показывать блок «Комфорт»', 'shpigovsky-core' ),
					'services_hub_comfort_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 7. Secondary CTA band
				self::field(
					'field_fp02_services_hub_secondary_cta_title',
					__( 'Второй CTA — заголовок', 'shpigovsky-core' ),
					'services_hub_secondary_cta_title',
					'text',
					array(
						'instructions' => __( 'Полоса CTA после блока «Комфорт». Пусто — static V9 fallback.', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_secondary_cta_subtitle',
					__( 'Второй CTA — подзаголовок', 'shpigovsky-core' ),
					'services_hub_secondary_cta_subtitle',
					'text'
				),
				self::field(
					'field_fp02_services_hub_secondary_cta_button',
					__( 'Второй CTA — кнопка', 'shpigovsky-core' ),
					'services_hub_secondary_cta_button',
					'text'
				),
				self::field(
					'field_fp02_services_hub_secondary_cta_visible',
					__( 'Показывать второй CTA', 'shpigovsky-core' ),
					'services_hub_secondary_cta_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 8. FAQ
				self::field(
					'field_fp02_services_hub_faq_heading',
					__( 'FAQ — заголовок', 'shpigovsky-core' ),
					'services_hub_faq_heading',
					'text',
					array(
						'instructions' => __( 'Заголовок блока FAQ. Пусто — «Нас часто спрашивают».', 'shpigovsky-core' ),
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_services_hub_faq_items',
					__( 'FAQ — вопросы', 'shpigovsky-core' ),
					'services_hub_faq_items',
					15,
					self::faq_subfields( 'services_hub' ),
					0,
					array(
						'instructions' => __( 'Вопросы и ответы на странице «Услуги».', 'shpigovsky-core' ),
						'button_label' => __( 'Добавить', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_services_hub_faq_visible',
					__( 'Показывать FAQ', 'shpigovsky-core' ),
					'services_hub_faq_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
				// 9. Final form
				self::field(
					'field_fp02_services_hub_final_form_notice',
					__( 'Финальная форма', 'shpigovsky-core' ),
					'services_hub_final_form_notice',
					'message',
					array(
						'message'   => __( 'Автоматический / общий блок: тексты финальной формы берутся из «Повторяемые блоки — Финальная форма». На странице «Услуги» — только показ/скрытие.', 'shpigovsky-core' ),
						'new_lines' => 'wpautop',
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::field(
					'field_fp02_services_hub_final_form_visible',
					__( 'Показывать финальную форму', 'shpigovsky-core' ),
					'services_hub_final_form_visible',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
					)
				),
			),
			self::location( 'page_template', '==', 'page-templates/services-hub.php' )
		);
	}

	/**
	 * O-centre hub page group (page #11 only).
	 *
	 * @return array<string, mixed>
	 */
	private static function page_ocentre_hub() {
		return self::group(
			'group_fp02_page_ocentre_hub',
			'Page — O-Centre Hub',
			array(
				self::field( 'field_fp02_hero_eyebrow_institutional', 'Hero eyebrow', 'hero_eyebrow', 'text' ),
				self::field( 'field_fp02_hero_title_override_institutional', 'Hero H1 override', 'hero_title_override', 'text' ),
				self::field( 'field_fp02_hero_lead_institutional', 'Hero lead', 'hero_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field(
					'field_fp02_hero_media_institutional',
					'Hero image',
					'hero_media',
					'image',
					array(
						'instructions' => 'Hero background image. Empty falls back to theme asset o-centre-hero.webp.',
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field(
					'field_fp02_hero_cta_label_institutional',
					'Текст кнопки в hero-блоке',
					'hero_cta_label',
					'text',
					array(
						'instructions' => 'Индивидуальный текст кнопки для hero-блока этой страницы/услуги. Если оставить пустым, используется текущий текст по умолчанию.',
					)
				),
				self::field(
					'field_fp02_about_hub_admin_overview',
					'О центре — Обзор редактирования',
					'about_hub_admin_overview',
					'message',
					array(
						'message'   => 'Блоки ниже соответствуют публичной странице /o-centre/ сверху вниз: Hero → Кто мы → Слово основателя → Кого лечим → Подход → Территория → Программа → Инфраструктура. Общие блоки (специалисты, отзывы, форма) — см. раздел ниже.',
						'new_lines' => 'br',
					)
				),
				self::field(
					'field_fp02_about_narrative_heading',
					'О центре — Кто мы: заголовок',
					'about_narrative_heading',
					'text',
					array(
						'instructions' => 'Секция #who-we-are. Пустое значение — static V9 fallback.',
					)
				),
				self::field(
					'field_fp02_about_narrative_lead',
					'О центре — Кто мы: лид',
					'about_narrative_lead',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::repeater(
					'field_fp02_about_narrative_paragraphs',
					'О центре — Кто мы: абзацы',
					'about_narrative_paragraphs',
					6,
					array(
						self::field( 'field_fp02_about_narrative_paragraph_text', 'Абзац', 'text', 'textarea', array( 'rows' => 3 ) ),
					)
				),
				self::field(
					'field_fp02_about_who_treat_heading',
					'О центре — Кого лечим: заголовок',
					'about_who_treat_heading',
					'text'
				),
				self::field(
					'field_fp02_about_who_treat_intro',
					'О центре — Кого лечим: вводный текст',
					'about_who_treat_intro',
					'textarea',
					array(
						'rows' => 4,
					)
				),
				self::field(
					'field_fp02_about_who_treat_lead',
					'О центре — Кого лечим: лид',
					'about_who_treat_lead',
					'textarea',
					array(
						'rows' => 2,
					)
				),
				self::repeater(
					'field_fp02_about_who_treat_spectrum',
					'О центре — Кого лечим: спектр состояний',
					'about_who_treat_spectrum',
					3,
					self::title_text_subfields( 'about_who_treat_spectrum' )
				),
				self::field(
					'field_fp02_about_who_treat_callout',
					'О центре — Кого лечим: выноска',
					'about_who_treat_callout',
					'textarea',
					array(
						'rows' => 2,
					)
				),
				self::repeater(
					'field_fp02_about_who_treat_cards',
					'О центре — Кого лечим: карточки',
					'about_who_treat_cards',
					4,
					self::title_text_subfields( 'about_who_treat_cards' )
				),
				self::field(
					'field_fp02_about_approach_heading',
					'О центре — Подход: заголовок',
					'about_approach_heading',
					'text'
				),
				self::field(
					'field_fp02_about_approach_highlight',
					'О центре — Подход: акцент',
					'about_approach_highlight',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::field(
					'field_fp02_about_approach_intro',
					'О центре — Подход: вводный текст',
					'about_approach_intro',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::repeater(
					'field_fp02_about_founder_quote_paragraphs',
					'О центре — Слово основателя: абзацы',
					'about_founder_quote_paragraphs',
					6,
					array(
						self::field( 'field_fp02_about_founder_quote_paragraph_text', 'Абзац', 'text', 'textarea', array( 'rows' => 3 ) ),
					),
					0,
					array(
						'instructions' => 'Секция founder-quote на /o-centre/. Пустые значения — static V9 fallback.',
					)
				),
				self::field(
					'field_fp02_about_founder_name',
					'О центре — Слово основателя: имя',
					'about_founder_name',
					'text'
				),
				self::field(
					'field_fp02_about_founder_role',
					'О центре — Слово основателя: должность',
					'about_founder_role',
					'text'
				),
				self::field(
					'field_fp02_about_founder_photo',
					'О центре — Слово основателя: фото',
					'about_founder_photo',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'instructions'  => 'Пустое значение — theme asset founder-sergey-shpigovsky.png.',
					)
				),
				self::field(
					'field_fp02_about_founder_cta_label',
					'О центре — Слово основателя: текст кнопки',
					'about_founder_cta_label',
					'text'
				),
				self::field(
					'field_fp02_about_clinic_landscape_image',
					'О центре — Территория клиники: изображение',
					'about_clinic_landscape_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'instructions'  => 'Пустое значение — theme asset shpigovsky-clinic-landscape.webp.',
					)
				),
				self::field(
					'field_fp02_about_clinic_landscape_alt',
					'О центре — Территория клиники: alt-текст',
					'about_clinic_landscape_alt',
					'text'
				),
				self::field(
					'field_fp02_about_hub_admin_note_shared_blocks',
					'О центре — Общие блоки (редактирование)',
					'about_hub_admin_note_shared_blocks',
					'message',
					array(
						'message'   => 'Специалисты: Настройки сайта → fp02-block-specialists. Отзывы: меню «Отзывы» (fp02-reviews). Финальная форма: Настройки сайта → fp02-block-final-form.',
						'new_lines' => 'br',
					)
				),
				self::field(
					'field_fp02_about_hub_admin_note_cta_phone',
					'О центре — CTA и телефон',
					'about_hub_admin_note_cta_phone',
					'message',
					array(
						'message'   => 'CTA-ленты program-cta-band на странице используют шаблонный fallback. Телефон: Настройки сайта → контакты (phone_primary).',
						'new_lines' => 'br',
					)
				),
				self::field(
					'field_fp02_about_program_heading',
					'О центре — Программа: заголовок',
					'about_program_heading',
					'text'
				),
				self::field(
					'field_fp02_about_program_lead',
					'О центре — Программа: лид',
					'about_program_lead',
					'textarea',
					array(
						'rows' => 2,
					)
				),
				self::field(
					'field_fp02_about_program_intro',
					'О центре — Программа: вводный текст 1',
					'about_program_intro',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::field(
					'field_fp02_about_program_intro2',
					'О центре — Программа: вводный текст 2',
					'about_program_intro2',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::field(
					'field_fp02_about_program_items_auto_note',
					'О центре — Программа: направления (автоматически)',
					'about_program_items_auto_note',
					'message',
					array(
						'message'   => 'Карточки направлений читаются автоматически из дочерних страниц «Программа лечения» (родитель #13): заголовок страницы, постоянная ссылка и поле «Мини-описание». Редактируйте карточки там. Устаревший повторитель скрыт; исторические postmeta сохранены.',
						'new_lines' => 'br',
						'wrapper'   => array(
							'width' => '',
							'class' => 'fp02-acf-section-title',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_about_program_items',
					'О центре — Программа: направления (устарело)',
					'about_program_items',
					4,
					array(
						self::field( 'field_fp02_about_program_item_title', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_about_program_item_image', 'Изображение', 'image', 'image', array( 'return_format' => 'array' ) ),
					),
					0,
					array(
						'instructions' => 'LEGACY DORMANT (V9-07A01): не читается на фронтенде. Исторические postmeta сохранены для отката. Источник карточек — дочерние страницы программы лечения.',
						'wrapper'      => array(
							'width' => '',
							'class' => 'fp02-acf-legacy-retired',
							'id'    => '',
						),
					)
				),
				self::repeater(
					'field_fp02_infrastructure_g0_g5',
					'Наш Дом — Infrastructure G0-G5',
					'infrastructure_g0_g5',
					6,
					self::media_text_subfields( 'infrastructure_g' ),
					6,
					array(
						'instructions' => 'G0 intro + G1-G4 bullets for /o-centre/ hub. Images use static V9 theme assets when media empty.',
					)
				),
				self::field(
					'field_fp02_infrastructure_narrative_bullet_intro',
					'Дополнительный текст после вводного блока',
					'infrastructure_narrative_bullet_intro',
					'textarea',
					array(
						'rows'         => 5,
						'instructions' => 'Текст сразу после красной линии (G0 lead). Рендерится как .infrastructure-narrative__bullet со span. Пусто — блок скрыт.',
					)
				),
			),
			self::location_page_id( 11 )
		);
	}

	/**
	 * Shared page layout mode for Generic Content template pages (V9-06E51).
	 * Temporary stub render: header / nav / H1 / footer. Content fields preserved.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_layout_mode() {
		return self::group(
			'group_fp02_page_layout_mode',
			__( 'Макет страницы', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_page_layout_mode',
					__( 'Макет страницы', 'shpigovsky-core' ),
					'page_layout_mode',
					'button_group',
					array(
						'instructions'  => __( '«Полная страница» показывает обычные редактируемые блоки. «Заглушка» временно выводит только шапку, навигацию, H1 и подвал. Содержимое в полях сохраняется и возвращается при переключении обратно.', 'shpigovsky-core' ),
						'required'      => 0,
						'choices'       => array(
							'full'        => __( 'Полная страница', 'shpigovsky-core' ),
							'placeholder' => __( 'Заглушка', 'shpigovsky-core' ),
						),
						'default_value' => 'full',
						'return_format' => 'value',
						'allow_null'    => 0,
						'layout'        => 'horizontal',
						'wrapper'       => array(
							'width' => '',
							'class' => 'fp02-acf-section-title fp02-page-layout-selector',
							'id'    => '',
						),
					)
				),
			),
			self::location( 'page_template', '==', 'page-templates/generic.php' )
		);
	}

	/**
	 * Generic Content template — page body SoT (V9-06E52).
	 * Empty optional fields hide on frontend (no hardcoded demo injection).
	 *
	 * @return array<string, mixed>
	 */
	private static function page_generic_content() {
		$group = self::group(
			'group_fp02_page_generic_content',
			__( 'Содержимое страницы', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_generic_page_lead',
					__( 'Лид / вступление', 'shpigovsky-core' ),
					'generic_page_lead',
					'textarea',
					array(
						'instructions' => __( 'Необязательно. Если поле пустое — блок на фронте скрывается (без демо-текста).', 'shpigovsky-core' ),
						'rows'         => 3,
						'new_lines'    => 'br',
					)
				),
				self::field(
					'field_fp02_generic_page_body',
					__( 'Основной текст', 'shpigovsky-core' ),
					'generic_page_body',
					'wysiwyg',
					array(
						'instructions'  => __( 'Источник содержимого обычной страницы. Если пусто — текст на фронте не подставляется из шаблона. Аварийный запас: post_content только если ACF пуст.', 'shpigovsky-core' ),
						'tabs'          => 'all',
						'toolbar'       => 'full',
						'media_upload'  => 1,
						'delay'         => 0,
					)
				),
				array(
					'key'           => 'field_fp02_generic_page_reusable_notice',
					'label'         => __( 'Повторно используемые блоки', 'shpigovsky-core' ),
					'name'          => 'generic_page_reusable_notice',
					'type'          => 'message',
					'message'       => __( 'Включает уже существующие общие блоки сайта. Контент блоков не копируется на страницу — редактируется в их канонических настройках (Комфорт / требования; галерея «О доме»).', 'shpigovsky-core' ),
					'new_lines'     => 'wpautop',
					'esc_html'      => 0,
				),
				array(
					'key'           => 'field_fp02_generic_page_reusable_blocks',
					'label'         => __( 'Показать блоки на странице', 'shpigovsky-core' ),
					'name'          => 'generic_page_reusable_blocks',
					'type'          => 'checkbox',
					'instructions'  => __( 'Отметьте блоки, которые нужно показать под основным текстом. Порядок на странице фиксированный: сначала требования к реабилитации, затем «О доме».', 'shpigovsky-core' ),
					'choices'       => array(
						'rehab_requirements' => __( 'Что нужно для прохождения реабилитации и лечения', 'shpigovsky-core' ),
						'about_home'         => __( 'О доме / комфорт и территория', 'shpigovsky-core' ),
					),
					'default_value' => array(),
					'layout'        => 'vertical',
					'return_format' => 'value',
					'allow_custom'  => 0,
					'save_custom'   => 0,
				),
			),
			self::location( 'page_template', '==', 'page-templates/generic.php' )
		);

		$group['menu_order']     = 1;
		$group['hide_on_screen'] = array(
			'the_content',
			'excerpt',
			'discussion',
			'comments',
			'revisions',
			'author',
			'format',
			'categories',
			'tags',
			'send-trackbacks',
		);
		$group['description']    = 'V9-06E52 generic page ACF content source of truth (Generic Content template). PROD-P07: reusable shared blocks selector.';

		return $group;
	}

	/**
	 * Treatment Program child pages (direct children of «Программа лечения» #13).
	 * Owns Home direction-card mini-descriptions (`.home-rehabilitation-program__direction-text`).
	 *
	 * @return array<string, mixed>
	 */
	private static function page_treatment_program_child() {
		$group = self::group(
			'group_fp02_treatment_program_child',
			__( 'Программа лечения — карточка', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_treatment_program_short_description',
					__( 'Мини-описание', 'shpigovsky-core' ),
					'treatment_program_short_description',
					'textarea',
					array(
						'instructions' => __( 'Краткий текст для карточки направления в блоке программы лечения на Главной странице.', 'shpigovsky-core' ),
						'rows'         => 4,
						'new_lines'    => '',
					)
				),
			),
			self::location( 'page_parent', '==', '13' )
		);

		$group['menu_order']  = 0;
		$group['description'] = 'V9-06E62D Treatment Program child mini-description for Home direction cards. Location: page_parent == 13 (Программа лечения).';

		return $group;
	}

	/**
	 * Specialist profile CPT (PROD-P11). Field keys preserved from P08.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_specialist_profile() {
		$group = self::group(
			'group_fp02_specialist_profile',
			__( 'Специалист — профиль', 'shpigovsky-core' ),
			array(
				self::field(
					'field_fp02_specialist_portrait_notice',
					__( 'Портрет', 'shpigovsky-core' ),
					'specialist_portrait_notice',
					'message',
					array(
						'message'   => __( 'Портрет берётся из поля «Фото» (Featured Image). Отдельное поле-дубликат не создаём.', 'shpigovsky-core' ),
						'new_lines' => 'br',
					)
				),
				self::field(
					'field_fp02_specialist_role',
					__( 'Должность / профессия', 'shpigovsky-core' ),
					'specialist_role',
					'text',
					array(
						'instructions' => __( 'Кратко: кто специалист (например: «Психолог, EMDR терапевт»). Показывается в карточке слайдера и в шапке страницы.', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_specialist_experience',
					__( 'Опыт', 'shpigovsky-core' ),
					'specialist_experience',
					'text',
					array(
						'instructions' => __( 'Например: «Опыт — 2,5 года».', 'shpigovsky-core' ),
					)
				),
				self::field(
					'field_fp02_specialist_specialty',
					__( 'Специальность', 'shpigovsky-core' ),
					'specialist_specialty',
					'wysiwyg',
					array(
						'instructions' => __( 'Блок «Специальность». Пустое поле на сайте не показывается.', 'shpigovsky-core' ),
						'tabs'         => 'all',
						'toolbar'      => 'basic',
						'media_upload' => 0,
					)
				),
				self::field(
					'field_fp02_specialist_education',
					__( 'Образование', 'shpigovsky-core' ),
					'specialist_education',
					'wysiwyg',
					array(
						'instructions' => __( 'Блок «Образование». Пустое поле на сайте не показывается.', 'shpigovsky-core' ),
						'tabs'         => 'all',
						'toolbar'      => 'basic',
						'media_upload' => 0,
					)
				),
				self::field(
					'field_fp02_specialist_specialization',
					__( 'Специализация', 'shpigovsky-core' ),
					'specialist_specialization',
					'wysiwyg',
					array(
						'instructions' => __( 'Блок «Специализация». Пустое поле на сайте не показывается.', 'shpigovsky-core' ),
						'tabs'         => 'all',
						'toolbar'      => 'basic',
						'media_upload' => 0,
					)
				),
				self::field(
					'field_fp02_specialist_principles',
					__( 'Принципы / подход к работе', 'shpigovsky-core' ),
					'specialist_principles',
					'wysiwyg',
					array(
						'instructions' => __( 'Блок про подход к работе. Пустое поле на сайте не показывается.', 'shpigovsky-core' ),
						'tabs'         => 'all',
						'toolbar'      => 'basic',
						'media_upload' => 0,
					)
				),
				self::field(
					'field_fp02_specialist_additional',
					__( 'Дополнительная информация', 'shpigovsky-core' ),
					'specialist_additional',
					'wysiwyg',
					array(
						'instructions' => __( 'Всё, что не вошло в структурированные блоки выше (legacy-текст без потери содержимого).', 'shpigovsky-core' ),
						'tabs'         => 'all',
						'toolbar'      => 'full',
						'media_upload' => 0,
					)
				),
				self::field(
					'field_fp02_specialist_certificates',
					__( 'Сертификаты и дипломы', 'shpigovsky-core' ),
					'specialist_certificates',
					'gallery',
					array(
						'instructions' => __( 'Галерея сертификатов/дипломов. На сайте — сетка с увеличением по клику.', 'shpigovsky-core' ),
						'return_format'=> 'array',
						'preview_size' => 'medium',
						'library'      => 'all',
						'min'          => 0,
						'max'          => 40,
					)
				),
			),
			self::location( 'post_type', '==', 'specialist' )
		);

		$group['menu_order']     = 5;
		$group['hide_on_screen'] = array(
			'the_content',
			'excerpt',
			'discussion',
			'comments',
			'revisions',
			'author',
			'format',
			'categories',
			'tags',
			'send-trackbacks',
		);
		$group['description']    = 'PROD-P11 Specialist CPT structured profile (keys from P08). Portrait = Featured Image. Location: post_type=specialist.';

		return $group;
	}

	/**
	 * Institutional child pages group (pages #12-#16).
	 *
	 * @return array<string, mixed>
	 */
	private static function page_institutional_child() {
		return self::group(
			'group_fp02_page_institutional_child',
			'Page — Institutional Child',
			array(
				self::field(
					'field_fp02_institutional_child_pages_note',
					'Institutional child pages — note',
					'institutional_child_pages_note',
					'message',
					array(
						'message'   => 'Content sections и Stages — для дочерних institutional-страниц. На странице «О центре» (#11) не используются публичным шаблоном.',
						'new_lines' => 'br',
					)
				),
				self::field(
					'field_fp02_institutional_placeholder_notice',
					'Placeholder notice',
					'institutional_placeholder_notice',
					'textarea',
					array(
						'rows' => 3,
					)
				),
				self::repeater(
					'field_fp02_institutional_content_sections',
					'Content sections',
					'institutional_content_sections',
					8,
					self::media_text_subfields( 'institutional_section' )
				),
				self::repeater(
					'field_fp02_institutional_stages',
					'Stages',
					'institutional_stages',
					8,
					self::title_text_subfields( 'institutional_stages' )
				),
			),
			self::institutional_child_locations()
		);
	}

	/**
	 * Contacts page group.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_contacts() {
		return self::group(
			'group_fp02_page_contacts',
			'Page — Contacts',
			array(
				self::field( 'field_fp02_contacts_heading', 'Заголовок страницы', 'contacts_heading', 'text', array( 'instructions' => 'Пусто — используется заголовок страницы.' ) ),
				self::field( 'field_fp02_contacts_form_intro', 'Вводный текст формы', 'contacts_form_intro', 'textarea', array( 'rows' => 3 ) ),
				self::repeater( 'field_fp02_contacts_phones', 'Телефоны', 'contacts_phones', 4, array( self::field( 'field_fp02_contacts_phone_label', 'Подпись', 'label', 'text' ), self::field( 'field_fp02_contacts_phone_value', 'Телефон', 'phone', 'text' ) ) ),
				self::repeater( 'field_fp02_contacts_messengers', 'Мессенджеры', 'contacts_messengers', 6, array( self::field( 'field_fp02_contacts_messenger_label', 'Подпись', 'label', 'text' ), self::field( 'field_fp02_contacts_messenger_url', 'URL', 'url', 'url' ) ) ),
				self::repeater(
					'field_fp02_contacts_locations',
					'Адреса и карты',
					'contacts_locations',
					8,
					array(
						self::field( 'field_fp02_contacts_location_title', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_contacts_location_address', 'Адрес', 'address', 'text' ),
						self::field( 'field_fp02_contacts_location_address_label', 'Подпись к адресу', 'address_label', 'text' ),
						self::field( 'field_fp02_contacts_location_hours_label', 'Подпись режима работы', 'hours_label', 'text' ),
						self::field( 'field_fp02_contacts_location_hours_html', 'Режим работы', 'hours_html', 'textarea', array( 'rows' => 2, 'instructions' => 'Пусто — общий режим работы из настроек сайта.' ) ),
						self::field( 'field_fp02_contacts_location_email', 'Email', 'email', 'email' ),
						self::field( 'field_fp02_contacts_location_email_label', 'Подпись email', 'email_label', 'text' ),
						self::field(
							'field_fp02_contacts_location_map_embed_code',
							'Код Яндекс.Карты',
							'map_embed_code',
							'textarea',
							array(
								'rows'         => 4,
								'instructions' => 'Вставьте полный код конструктора Яндекс.Карт: <script ...></script>.',
							)
						),
						self::field( 'field_fp02_contacts_location_map_alt', 'Alt карты', 'map_alt', 'text' ),
						self::field( 'field_fp02_contacts_location_simplified', 'Упрощённая карточка', 'simplified', 'true_false' ),
					),
					0,
					array(
						'collapsed' => 'field_fp02_contacts_location_address',
					)
				),
			),
			self::location( 'page_template', '==', 'page-templates/contacts.php' )
		);
	}

	/**
	 * Reviews page group.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_reviews() {
		return self::group(
			'group_fp02_page_reviews',
			'Page — Reviews',
			array(
				self::field(
					'field_fp02_page_reviews_source_notice',
					'Источник отзывов',
					'page_reviews_source_notice',
					'message',
					array(
						'message'   => 'Отзывы редактируются в отдельном разделе админки: <a href="' . esc_url( admin_url( 'admin.php?page=fp02-reviews' ) ) . '">Отзывы</a>. Эта страница использует общий список отзывов и настройку «Отзывов на странице».',
						'new_lines' => 'br',
					)
				),
			),
			self::location( 'page_template', '==', 'page-templates/reviews.php' )
		);
	}

	/**
	 * Legal page group.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_legal() {
		return self::group(
			'group_fp02_page_legal',
			'Page — Legal',
			array(
				self::field( 'field_fp02_legal_status', 'Legal status', 'legal_status', 'select', array( 'choices' => array( 'demo' => 'Demo', 'review' => 'Review', 'production_ready' => 'Production ready' ), 'default_value' => 'demo' ) ),
				self::field( 'field_fp02_legal_demo_marker', 'Demo marker', 'legal_demo_marker', 'true_false', array( 'default_value' => 1 ) ),
				self::field( 'field_fp02_legal_effective_date', 'Effective date', 'legal_effective_date', 'date_picker', array( 'display_format' => 'Y-m-d', 'return_format' => 'Y-m-d' ) ),
				self::field( 'field_fp02_legal_version', 'Version', 'legal_version', 'text' ),
				self::field( 'field_fp02_legal_production_blocker', 'Production blocker flag', 'legal_production_blocker', 'true_false', array( 'default_value' => 1 ) ),
			),
			self::location( 'page_template', '==', 'page-templates/legal.php' )
		);
	}

	/**
	 * Blog post article meta group.
	 *
	 * @return array<string, mixed>
	 */
	private static function blog_post_article_meta() {
		return self::group(
			'group_fp02_blog_post_article_meta',
			'Blog Post — Article Meta',
			array(
				self::field( 'field_fp02_article_eyebrow', 'Eyebrow', 'article_eyebrow', 'text' ),
				self::field( 'field_fp02_article_lead', 'Lead / announcement', 'article_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field( 'field_fp02_article_source_label', 'Source label', 'article_source_label', 'text' ),
				self::field(
					'field_fp02_article_reading_time',
					__( 'Время на чтение', 'shpigovsky-core' ),
					'article_reading_time',
					'number',
					array(
						'min'          => 0,
						'instructions' => __( 'Необязательно. Число минут. Если заполнено — показывается вручную. Если пусто — сайт посчитает время автоматически (~190 слов/мин). Не пишите слово «минут».', 'shpigovsky-core' ),
						'placeholder'  => '',
					)
				),
				self::field( 'field_fp02_article_disclaimer', 'Article disclaimer', 'article_disclaimer', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_article_hide_author_public', 'Hide author publicly', 'article_hide_author_public', 'true_false', array( 'default_value' => 1 ) ),
				self::field( 'field_fp02_article_author_label', 'Author label override', 'article_author_label', 'text' ),
				self::field( 'field_fp02_article_show_date_public', 'Show date publicly', 'article_show_date_public', 'true_false', array( 'default_value' => 1 ) ),
				self::field( 'field_fp02_article_show_toc', 'Show table of contents', 'article_show_toc', 'true_false', array( 'default_value' => 1 ) ),
				self::field( 'field_fp02_article_toc_title', 'TOC title', 'article_toc_title', 'text', array( 'default_value' => 'Оглавление:' ) ),
				self::field( 'field_fp02_article_conclusion_heading', 'Conclusion heading', 'article_conclusion_heading', 'text', array( 'default_value' => 'Заключение' ) ),
				self::field( 'field_fp02_article_conclusion_quote', 'Conclusion quote', 'article_conclusion_quote', 'textarea', array( 'rows' => 5 ) ),
				self::repeater(
					'field_fp02_article_source_items',
					'Sources',
					'article_source_items',
					20,
					array(
						self::field( 'field_fp02_article_source_text', 'Source text', 'source_text', 'textarea', array( 'rows' => 2 ) ),
					)
				),
				self::repeater(
					'field_fp02_article_faq_items',
					'FAQ items',
					'article_faq_items',
					15,
					self::faq_subfields( 'article' )
				),
				self::field( 'field_fp02_related_posts', 'Related posts', 'related_posts', 'relationship', array( 'post_type' => array( 'post' ), 'max' => 3, 'return_format' => 'object' ) ),
				self::field( 'field_fp02_article_final_cta_title', 'Final CTA title', 'article_final_cta_title', 'text' ),
				self::field( 'field_fp02_article_final_cta_text', 'Final CTA text', 'article_final_cta_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_article_final_cta_button_label', 'Final CTA button label', 'article_final_cta_button_label', 'text' ),
				self::field( 'field_fp02_article_final_cta_button_url', 'Final CTA button URL', 'article_final_cta_button_url', 'url' ),
				self::field( 'field_fp02_article_source_file_name', 'WPilot source file name', 'article_source_file_name', 'text' ),
				self::field( 'field_fp02_article_source_import_date', 'WPilot source import date', 'article_source_import_date', 'text' ),
				self::field( 'field_fp02_article_editor_status', 'WPilot editor status', 'article_editor_status', 'text' ),
				self::field( 'field_fp02_article_content_qa_status', 'WPilot content QA status', 'article_content_qa_status', 'text' ),
			),
			self::location( 'post_type', '==', 'post' )
		);
	}

	/**
	 * Blog archive settings group (posts page).
	 *
	 * @return array<string, mixed>
	 */
	private static function blog_archive_settings() {
		return self::group(
			'group_fp02_blog_archive_settings',
			'Blog — Archive Settings',
			array(
				self::field( 'field_fp02_blog_archive_title', 'Заголовок архива', 'blog_archive_title', 'text' ),
				self::field( 'field_fp02_blog_archive_intro', 'Вводный текст', 'blog_archive_intro', 'textarea', array( 'rows' => 4 ) ),
				self::field(
					'field_fp02_blog_archive_posts_per_page',
					'Статей на странице',
					'blog_archive_posts_per_page',
					'number',
					array(
						'default_value' => 12,
						'min'           => 1,
						'max'           => 50,
						'step'          => 1,
					)
				),
				self::field(
					'field_fp02_blog_archive_show_cta',
					'Показывать CTA-блок',
					'blog_archive_show_cta',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
						'ui_on_text'    => 'Да',
						'ui_off_text'   => 'Нет',
						'instructions'  => 'Контент берётся из повторяемого блока «CTA-блоки».',
					)
				),
				self::field(
					'field_fp02_blog_archive_show_founder_word',
					'Показывать слово основателя',
					'blog_archive_show_founder_word',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
						'ui_on_text'    => 'Да',
						'ui_off_text'   => 'Нет',
						'instructions'  => 'Контент берётся из «Настройки сайта → Цитата основателя». Здесь только показ/скрытие.',
					)
				),
			),
			self::location( 'page_type', '==', 'posts_page' )
		);
	}

	/**
	 * Site contacts/options group.
	 *
	 * @return array<string, mixed>
	 */
	private static function site_options_contacts() {
		return self::group(
			'group_fp02_site_options_contacts',
			'Site Options — Contacts and Organisation',
			array(
				self::field(
					'field_fp02_show_breadcrumbs_pages',
					'Показывать хлебные крошки на страницах',
					'show_breadcrumbs_pages',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
						'ui_on_text'    => 'Да',
						'ui_off_text'   => 'Нет',
					)
				),
				self::field(
					'field_fp02_show_breadcrumbs_services',
					'Показывать хлебные крошки в услугах',
					'show_breadcrumbs_services',
					'true_false',
					array(
						'default_value' => 1,
						'ui'            => 1,
						'ui_on_text'    => 'Да',
						'ui_off_text'   => 'Нет',
					)
				),
				self::field( 'field_fp02_org_name', 'Organisation name', 'organisation_name', 'text' ),
				self::field( 'field_fp02_phone_primary', 'Primary phone', 'phone_primary', 'text' ),
				self::field( 'field_fp02_phone_secondary', 'Secondary phone', 'phone_secondary', 'text' ),
				self::field( 'field_fp02_site_email', 'Email', 'site_email', 'email' ),
				self::field( 'field_fp02_site_address', 'Address', 'site_address', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_opening_hours', 'Opening hours', 'opening_hours', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_map_link', 'Map link', 'map_link', 'url' ),
				self::repeater( 'field_fp02_social_links', 'Messengers / socials', 'social_links', 8, array( self::field( 'field_fp02_social_label', 'Label', 'label', 'text' ), self::field( 'field_fp02_social_url', 'URL', 'url', 'url' ) ) ),
				self::field( 'field_fp02_legal_org_identifiers', 'Legal organisation identifiers', 'legal_org_identifiers', 'textarea', array( 'rows' => 4 ) ),
			),
			self::location( 'options_page', '==', 'fp02-site-settings-general' )
		);
	}

	/**
	 * Site modal/global CTA group.
	 *
	 * @return array<string, mixed>
	 */
	private static function site_options_modal_cta() {
		return self::group(
			'group_fp02_site_options_modal_cta',
			'Site Options — Modal and Global CTA',
			array(
				self::field( 'field_fp02_default_callback_title', 'Default callback title', 'default_callback_title', 'text' ),
				self::field( 'field_fp02_default_callback_text', 'Default callback text', 'default_callback_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_default_button_label', 'Default button label', 'default_button_label', 'text' ),
				self::field( 'field_fp02_default_secondary_button_label', 'Default secondary button label', 'default_secondary_button_label', 'text' ),
				self::field( 'field_fp02_default_consent_text_reference', 'Consent text reference', 'default_consent_text_reference', 'text' ),
				self::field( 'field_fp02_global_cta_title', 'Global CTA title', 'global_cta_title', 'text' ),
				self::field( 'field_fp02_global_cta_text', 'Global CTA text', 'global_cta_text', 'textarea', array( 'rows' => 3 ) ),
			),
			self::location( 'options_page', '==', 'fp02-site-settings-general' )
		);
	}

	/**
	 * Site reviews/options group.
	 *
	 * @return array<string, mixed>
	 */
	private static function site_options_reviews() {
		return self::group(
			'group_fp02_site_options_reviews',
			'Site Options — Reviews',
			array(
				self::field( 'field_fp02_options_reviews_enabled', 'Включить блок отзывов', 'reviews_enabled', 'true_false', array( 'default_value' => 1, 'ui' => 1, 'ui_on_text' => 'Да', 'ui_off_text' => 'Нет' ) ),
				self::field( 'field_fp02_options_reviews_section_heading', 'Заголовок блока отзывов', 'reviews_section_heading', 'text' ),
				self::field(
					'field_fp02_options_reviews_per_page',
					'Отзывов на странице',
					'reviews_per_page',
					'number',
					array(
						'default_value' => 10,
						'min'           => 1,
						'max'           => 50,
						'step'          => 1,
					)
				),
				self::repeater(
					'field_fp02_options_reviews_items',
					'Отзывы',
					'reviews_items',
					50,
					array(
						self::field(
							'field_fp02_options_review_uid',
							'Постоянный ID отзыва',
							'review_uid',
							'text',
							array(
								'instructions' => 'Стабильный якорь (review-xxxxxxxx). Не меняется при перестановке строк. Заполняется автоматически.',
								'wrapper'      => array(
									'width' => '50',
									'class' => 'fp02-review-uid-field',
									'id'    => '',
								),
							)
						),
						self::field( 'field_fp02_options_review_author', 'Автор', 'review_author', 'text' ),
						self::field( 'field_fp02_options_review_text', 'Текст отзыва', 'review_text', 'textarea', array( 'rows' => 5 ) ),
						self::field(
							'field_fp02_options_review_service',
							'Повод обращения',
							'review_service',
							'post_object',
							array(
								'post_type'      => array( 'service' ),
								'return_format'  => 'id',
								'ui'             => 1,
								'allow_null'     => 1,
								'instructions'   => 'Автоматический список услуг (CPT service).',
							)
						),
						self::field( 'field_fp02_options_review_context', 'Контекст / повод вручную', 'review_context', 'text', array( 'instructions' => 'Fallback, если услуга не выбрана.' ) ),
						self::field( 'field_fp02_options_review_source', 'Источник', 'review_source', 'text' ),
						self::field( 'field_fp02_options_review_date', 'Дата', 'review_date', 'text' ),
						self::field( 'field_fp02_options_review_rating', 'Оценка (1–5)', 'review_rating', 'number', array( 'default_value' => 5, 'min' => 1, 'max' => 5, 'step' => 1 ) ),
						self::field( 'field_fp02_options_review_visible', 'Показывать', 'review_visible', 'true_false', array( 'default_value' => 1, 'ui' => 1, 'ui_on_text' => 'Да', 'ui_off_text' => 'Нет' ) ),
						self::field( 'field_fp02_options_review_featured', 'В слайдере на главной', 'review_featured', 'true_false', array( 'default_value' => 1, 'ui' => 1, 'ui_on_text' => 'Да', 'ui_off_text' => 'Нет' ) ),
					),
					0,
					array(
						'button_label' => 'Добавить отзыв',
						'instructions' => 'Site-wide reviews source. Если пусто — на фронтенде используется статический V9 fallback. Якоря используют постоянный review_uid (не индекс строки).',
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-reviews' )
		);
	}

	/**
	 * Reusable block — final form group (V9-06E18 Batch 1).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_final_form() {
		return self::group(
			'group_fp02_block_final_form',
			'Reusable Block — Final Form',
			array(
				self::field(
					'field_fp02_final_form_heading',
					'Заголовок',
					'final_form_heading',
					'text',
					array(
						'instructions' => 'Пусто — home_cta_title, затем статический fallback.',
					)
				),
				self::field(
					'field_fp02_final_form_lead',
					'Подзаголовок / лид',
					'final_form_lead',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => 'Пусто — home_cta_text, затем статический fallback.',
					)
				),
				self::field(
					'field_fp02_final_form_submit_label',
					'Текст кнопки отправки',
					'final_form_submit_label',
					'text',
					array(
						'instructions' => 'Пусто — default_button_label из Общих настроек.',
					)
				),
				self::field( 'field_fp02_final_form_name_label', 'Подпись поля «Имя»', 'final_form_name_label', 'text' ),
				self::field( 'field_fp02_final_form_phone_label', 'Подпись поля «Телефон»', 'final_form_phone_label', 'text' ),
				self::field( 'field_fp02_final_form_message_label', 'Подпись поля «Сообщение»', 'final_form_message_label', 'text' ),
				self::field( 'field_fp02_final_form_name_placeholder', 'Placeholder «Имя»', 'final_form_name_placeholder', 'text' ),
				self::field( 'field_fp02_final_form_phone_placeholder', 'Placeholder «Телефон»', 'final_form_phone_placeholder', 'text' ),
				self::field( 'field_fp02_final_form_message_placeholder', 'Placeholder «Сообщение»', 'final_form_message_placeholder', 'text' ),
			),
			self::location( 'options_page', '==', 'fp02-block-final-form' )
		);
	}

	/**
	 * Reusable block — specialists group (V9-06E18 Batch 1).
	 *
	 * V9-06E34: slider cards come from published child pages of `/specyalisty/`.
	 * Manual specialists_items repeater retired from admin render path.
	 *
	 * @return array<string, mixed>
	 */
	private static function block_specialists() {
		return self::group(
			'group_fp02_block_specialists',
			'Reusable Block — Specialists',
			array(
				self::field(
					'field_fp02_specialists_source_notice',
					'Источник слайдера',
					'specialists_source_notice',
					'message',
					array(
						'message' => 'PROD-P11: карточки слайдера автоматически берутся из CPT «Специалисты». Добавляйте/переупорядочивайте специалистов через меню Специалисты (menu_order). Ручной repeater specialists_items больше не используется в рендере.',
					)
				),
				self::field( 'field_fp02_specialists_section_heading', 'Заголовок секции', 'specialists_section_heading', 'text' ),
				self::field( 'field_fp02_specialists_all_link_label', 'Текст ссылки «все специалисты»', 'specialists_all_link_label', 'text' ),
				self::field(
					'field_fp02_specialists_all_link_url',
					'URL ссылки «все специалисты»',
					'specialists_all_link_url',
					'url',
					array(
						'instructions' => 'Пусто — /specyalisty/.',
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-specialists' )
		);
	}

	/**
	 * Reusable block — global CTA band defaults (V9-06E18 Batch 1).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_cta_bands() {
		return self::group(
			'group_fp02_block_cta_bands',
			'Reusable Block — CTA Bands',
			array(
				self::field(
					'field_fp02_cta_band_default_title',
					'CTA лид',
					'cta_band_default_title',
					'textarea',
					array(
						'rows'         => 2,
						'instructions' => 'Основной текст `.program-cta-band__lead` (как Comfort CTA лид). Используется когда у услуги нет cta_title. Пусто — global_cta_title из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_cta_band_default_subtitle',
					'Текст CTA',
					'cta_band_default_subtitle',
					'textarea',
					array(
						'rows'         => 2,
						'instructions' => 'Короткий текст `.program-cta-band__lead-txt` (как Comfort `cta_lead_text`). Пусто — global_cta_text из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_cta_band_phone_hint',
					'Подпись телефона',
					'cta_band_phone_hint',
					'text',
					array(
						'instructions' => 'Текст рядом с телефоном (как «Или позвоните нам» в Comfort CTA).',
					)
				),
				self::field(
					'field_fp02_cta_band_default_button_label',
					'Текст кнопки CTA',
					'cta_band_default_button_label',
					'text',
					array(
						'instructions' => 'Пусто — default_button_label из Общих настроек. URL кнопки задаётся на уровне страницы/услуги (`cta_button_target`), иначе открывается модалка консультации.',
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-cta-bands' )
		);
	}

	/**
	 * Reusable block — Founder’s Word / founder quote (V9-06E62B).
	 *
	 * Blog archive keeps only the visibility toggle; content lives here.
	 *
	 * @return array<string, mixed>
	 */
	private static function block_founder_quote() {
		return self::group(
			'group_fp02_block_founder_quote',
			'Reusable Block — Founder Quote',
			array(
				self::field(
					'field_fp02_founder_quote_source_notice',
					'Слово основателя',
					'founder_quote_source_notice',
					'message',
					array(
						'message' => 'Общий контент блока «Слово основателя» для Главной, Блога (при включённом переключателе), Услуг и других страниц, где подключён шаблон founder-quote. На странице Блога редактируется только показ/скрытие.',
					)
				),
				self::repeater(
					'field_fp02_founder_quote_paragraphs',
					'Абзацы цитаты',
					'founder_quote_paragraphs',
					10,
					array(
						self::field(
							'field_fp02_founder_quote_paragraph_text',
							'Абзац',
							'text',
							'textarea',
							array( 'rows' => 3 )
						),
					),
					0,
					array(
						'button_label' => 'Добавить абзац',
						'instructions' => 'Пусто — статический V9 fallback в шаблоне.',
					)
				),
				self::field(
					'field_fp02_founder_quote_photo',
					'Фото',
					'founder_quote_photo',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'instructions'  => 'Пусто — theme asset founder-sergey-shpigovsky.png.',
					)
				),
				self::field(
					'field_fp02_founder_quote_name',
					'Имя',
					'founder_quote_name',
					'text',
					array(
						'instructions' => 'Пусто — Сергей Юрьевич Шпиговский.',
					)
				),
				self::field(
					'field_fp02_founder_quote_role',
					'Роль / подпись',
					'founder_quote_role',
					'text',
					array(
						'instructions' => 'Пусто — Основатель центра. Аддиктолог, интервенционист.',
					)
				),
				self::field(
					'field_fp02_founder_quote_cta_label',
					'Текст кнопки',
					'founder_quote_cta_label',
					'text',
					array(
						'instructions' => 'Пусто — Записаться на консультацию.',
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-founder-quote' )
		);
	}

	/**
	 * Reusable block — header chrome (V9-06E21 Batch 2).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_header() {
		return self::group(
			'group_fp02_block_header',
			'Reusable Block — Header',
			array(
				self::field(
					'field_fp02_header_logo',
					'Логотип (медиа)',
					'header_logo',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'instructions'  => 'Опционально. Пусто — theme asset ниже или img/branding/logo.svg.',
					)
				),
				self::field(
					'field_fp02_header_logo_asset',
					'Theme asset path логотипа',
					'header_logo_asset',
					'text',
					array(
						'default_value' => 'img/branding/logo.svg',
						'instructions'  => 'Относительный путь в theme/assets.',
					)
				),
				self::field(
					'field_fp02_header_callback_label',
					'Текст кнопки «Заказать звонок» в шапке',
					'header_callback_label',
					'text',
					array(
						'instructions' => 'Пусто — default_button_label из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_header_general_settings_note',
					'Контакты и навигация',
					'header_general_settings_note',
					'message',
					array(
						'message' => 'Телефоны, адрес, часы работы и мессенджеры редактируются в «Общие настройки». Навигация — через меню WordPress (WP_NAV_MENU_AUTHORITY).',
						'new_lines' => 'wpautop',
						'esc_html' => 0,
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-header' )
		);
	}

	/**
	 * Reusable block — footer chrome (V9-06E21 Batch 2).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_footer() {
		return self::group(
			'group_fp02_block_footer',
			'Reusable Block — Footer',
			array(
				self::field(
					'field_fp02_footer_logo',
					'Логотип подвала (медиа)',
					'footer_logo',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
						'instructions'  => 'Опционально. Пусто — theme asset ниже.',
					)
				),
				self::field(
					'field_fp02_footer_logo_asset',
					'Theme asset path логотипа',
					'footer_logo_asset',
					'text',
					array(
						'default_value' => 'img/branding/logo.svg',
					)
				),
				self::field(
					'field_fp02_footer_copyright_suffix',
					'Текст copyright после года',
					'footer_copyright_suffix',
					'text',
					array(
						'default_value' => 'Все права защищены.',
					)
				),
				self::field(
					'field_fp02_footer_credit_text',
					'Текст разработчика',
					'footer_credit_text',
					'text',
					array(
						'default_value' => 'Разработка и продвижение: Overseo',
					)
				),
				self::field( 'field_fp02_footer_credit_url', 'Ссылка разработчика', 'footer_credit_url', 'url' ),
				self::field(
					'field_fp02_footer_callback_label',
					'Текст кнопки «Заказать звонок»',
					'footer_callback_label',
					'text',
					array(
						'instructions' => 'Пусто — default_callback_title из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_footer_appointment_label',
					'Текст кнопки «Записаться»',
					'footer_appointment_label',
					'text',
					array(
						'instructions' => 'Пусто — default_secondary_button_label из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_footer_nav_note',
					'Навигация и legal',
					'footer_nav_note',
					'message',
					array(
						'message' => 'Меню подвала и legal-ссылки остаются WordPress menu authority. Контент legal-страниц не редактируется здесь.',
						'new_lines' => 'wpautop',
						'esc_html' => 0,
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-footer' )
		);
	}

	/**
	 * Reusable block — comfort intro (V9-06E56 split; storage post_id fp02-block-comfort).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_comfort_intro() {
		return self::group(
			'group_fp02_block_comfort_intro',
			'Reusable Block — Comfort Intro',
			array(
				self::field( 'field_fp02_comfort_heading', 'Комфорт — заголовок', 'comfort_heading', 'text' ),
				self::field( 'field_fp02_comfort_lead', 'Комфорт — лид', 'comfort_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field( 'field_fp02_comfort_all_link_label', 'Комфорт — текст ссылки', 'comfort_all_link_label', 'text' ),
				self::field( 'field_fp02_comfort_all_link_url', 'Комфорт — URL ссылки', 'comfort_all_link_url', 'url' ),
			),
			self::location( 'options_page', '==', 'fp02-block-comfort-intro' )
		);
	}

	/**
	 * Reusable block — comfort gallery (V9-06E56 split; storage post_id fp02-block-comfort).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_comfort_gallery() {
		return self::group(
			'group_fp02_block_comfort_gallery',
			'Reusable Block — Comfort Gallery',
			array(
				self::repeater(
					'field_fp02_comfort_gallery_items',
					'Комфорт — галерея',
					'comfort_gallery_items',
					12,
					array(
						self::field( 'field_fp02_comfort_gallery_image', 'Изображение (медиа)', 'gallery_image', 'image', array( 'return_format' => 'array' ) ),
						self::field( 'field_fp02_comfort_gallery_asset', 'Theme asset path', 'gallery_image_asset', 'text' ),
						self::field( 'field_fp02_comfort_gallery_width', 'Ширина', 'gallery_image_width', 'number', array( 'min' => 0 ) ),
						self::field( 'field_fp02_comfort_gallery_height', 'Высота', 'gallery_image_height', 'number', array( 'min' => 0 ) ),
						self::field( 'field_fp02_comfort_gallery_is_decor', 'Декор (логотип)', 'gallery_is_decor', 'true_false' ),
						self::field( 'field_fp02_comfort_gallery_is_wide', 'Широкий элемент', 'gallery_is_wide', 'true_false' ),
						self::field( 'field_fp02_comfort_gallery_fancybox', 'Fancybox', 'gallery_fancybox_enabled', 'true_false', array( 'default_value' => 1 ) ),
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-comfort-gallery' )
		);
	}

	/**
	 * Reusable block — rehab requirements (V9-06E56 split; storage post_id fp02-block-comfort).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_comfort_requirements() {
		return self::group(
			'group_fp02_block_comfort_requirements',
			'Reusable Block — Comfort Requirements',
			array(
				self::field( 'field_fp02_rehab_requirements_heading', 'Требования — заголовок', 'rehab_requirements_heading', 'text' ),
				self::field( 'field_fp02_rehab_requirements_intro', 'Требования — вводный текст', 'rehab_requirements_intro', 'textarea', array( 'rows' => 3 ) ),
				self::repeater(
					'field_fp02_rehab_requirements_steps',
					'Требования — шаги',
					'rehab_requirements_steps',
					8,
					array(
						self::field( 'field_fp02_rehab_step_title', 'Заголовок', 'step_title', 'text' ),
						self::field( 'field_fp02_rehab_step_text', 'Текст', 'step_text', 'textarea', array( 'rows' => 3 ) ),
					)
				),
				self::field( 'field_fp02_rehab_requirements_cta_lead', 'Требования — CTA лид', 'rehab_requirements_cta_lead', 'textarea', array( 'rows' => 2 ) ),
				self::field(
					'field_fp02_rehab_requirements_cta_lead_text',
					'Текст CTA',
					'cta_lead_text',
					'textarea',
					array(
						'rows'         => 2,
						'instructions' => 'Короткий текст в блоке `.home-rehabilitation-requirements__cta-lead-txt` под основным CTA-лидом.',
					)
				),
				self::field( 'field_fp02_rehab_requirements_cta_phone', 'Требования — телефон CTA', 'rehab_requirements_cta_phone', 'text', array( 'instructions' => 'Пусто — phone_primary из Общих настроек или статический fallback.' ) ),
				self::field( 'field_fp02_rehab_requirements_cta_button_label', 'Требования — кнопка CTA', 'rehab_requirements_cta_button_label', 'text' ),
				self::field( 'field_fp02_rehab_requirements_support_heading', 'Требования — заголовок поддержки', 'rehab_requirements_support_heading', 'text' ),
				self::repeater(
					'field_fp02_rehab_requirements_support_items',
					'Требования — пункты поддержки',
					'rehab_requirements_support_items',
					8,
					array(
						self::field( 'field_fp02_rehab_support_item_text', 'Текст', 'item_text', 'textarea', array( 'rows' => 2 ) ),
					)
				),
				self::field( 'field_fp02_rehab_requirements_photo', 'Требования — фото (медиа)', 'rehab_requirements_photo', 'image', array( 'return_format' => 'array' ) ),
				self::field( 'field_fp02_rehab_requirements_photo_asset', 'Требования — theme asset path', 'rehab_requirements_photo_asset', 'text' ),
				self::field( 'field_fp02_rehab_requirements_photo_alt', 'Требования — alt фото', 'rehab_requirements_photo_alt', 'text' ),
				self::field( 'field_fp02_rehab_requirements_photo_width', 'Требования — ширина фото', 'rehab_requirements_photo_width', 'number', array( 'min' => 0 ) ),
				self::field( 'field_fp02_rehab_requirements_photo_height', 'Требования — высота фото', 'rehab_requirements_photo_height', 'number', array( 'min' => 0 ) ),
			),
			self::location( 'options_page', '==', 'fp02-block-comfort-requirements' )
		);
	}

	/**
	 * Group helper.
	 *
	 * @param string              $key Group key.
	 * @param string              $title Group title.
	 * @param array<int, mixed>   $fields Fields.
	 * @param array<int, mixed>   $location Location.
	 * @return array<string, mixed>
	 */
	private static function group( $key, $title, array $fields, $location ) {
		$location_rules = ( isset( $location[0]['param'] ) ) ? array( $location ) : $location;

		return array(
			'key'                   => $key,
			'title'                 => $title,
			'fields'                => $fields,
			'location'              => $location_rules,
			'menu_order'            => 0,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'hide_on_screen'        => '',
			'active'                => true,
			'description'           => 'FP-0002 V9-06C canonical source field group. Runtime registration occurs only after delivery authorization.',
			'show_in_rest'          => 0,
			'modified'              => self::MODIFIED,
		);
	}

	/**
	 * Field helper.
	 *
	 * @param string              $key Field key.
	 * @param string              $label Label.
	 * @param string              $name Name.
	 * @param string              $type ACF type.
	 * @param array<string,mixed> $args Overrides.
	 * @return array<string, mixed>
	 */
	private static function field( $key, $label, $name, $type, array $args = array() ) {
		return array_merge(
			array(
				'key'               => $key,
				'label'             => $label,
				'name'              => $name,
				'aria-label'        => '',
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
	 * Repeater helper with mandatory max rows.
	 *
	 * @param string            $key Field key.
	 * @param string            $label Label.
	 * @param string            $name Name.
	 * @param int               $max Max rows.
	 * @param array<int, mixed> $sub_fields Sub fields.
	 * @param int               $min Min rows.
	 * @param array<string,mixed> $args Repeater field overrides.
	 * @return array<string, mixed>
	 */
	private static function repeater( $key, $label, $name, $max, array $sub_fields, $min = 0, array $args = array() ) {
		return self::field(
			$key,
			$label,
			$name,
			'repeater',
			array_merge(
				array(
					'instructions' => 'Bounded repeater. Max rows are enforced in source and validation hooks.',
					'layout'       => 'row',
					'button_label' => 'Добавить',
					'min'          => $min,
					'max'          => $max,
					'sub_fields'   => $sub_fields,
				),
				$args
			)
		);
	}

	/**
	 * Location helper.
	 *
	 * @param string $param Param.
	 * @param string $operator Operator.
	 * @param string $value Value.
	 * @return array<int, array<string, string>>
	 */
	private static function location( $param, $operator, $value ) {
		return array(
			array(
				'param'    => $param,
				'operator' => $operator,
				'value'    => $value,
			),
		);
	}

	/**
	 * Location rule: specific page ID.
	 *
	 * @param int $page_id Page ID.
	 * @return array<int, array<string, string>>
	 */
	private static function location_page_id( $page_id ) {
		return array(
			array(
				'param'    => 'post_type',
				'operator' => '==',
				'value'    => 'page',
			),
			array(
				'param'    => 'page',
				'operator' => '==',
				'value'    => (string) $page_id,
			),
		);
	}

	/**
	 * Location rule: institutional child page by ID.
	 *
	 * @param int $page_id Page ID.
	 * @return array<int, array<string, string>>
	 */
	private static function location_institutional_child_page( $page_id ) {
		return array(
			array(
				'param'    => 'page_template',
				'operator' => '==',
				'value'    => 'page-templates/institutional.php',
			),
			array(
				'param'    => 'page',
				'operator' => '==',
				'value'    => (string) $page_id,
			),
		);
	}

	/**
	 * OR location rules for institutional placeholder pages #12-#16.
	 *
	 * @return array<int, array<int, array<string, string>>>
	 */
	private static function institutional_child_locations() {
		return array(
			self::location_institutional_child_page( 12 ),
			self::location_institutional_child_page( 13 ),
			self::location_institutional_child_page( 14 ),
			self::location_institutional_child_page( 15 ),
			self::location_institutional_child_page( 16 ),
		);
	}

	/**
	 * Reusable title/text subfields.
	 *
	 * @param string $prefix Field key prefix.
	 * @return array<int, mixed>
	 */
	private static function title_text_subfields( $prefix ) {
		return array(
			self::field( 'field_fp02_' . $prefix . '_title', __( 'Заголовок', 'shpigovsky-core' ), 'title', 'text' ),
			self::field( 'field_fp02_' . $prefix . '_text', __( 'Текст', 'shpigovsky-core' ), 'text', 'textarea', array( 'rows' => 3 ) ),
		);
	}

	/**
	 * Reusable media/text subfields.
	 *
	 * @param string $prefix Field key prefix.
	 * @return array<int, mixed>
	 */
	private static function media_text_subfields( $prefix ) {
		return array(
			self::field( 'field_fp02_' . $prefix . '_title', 'Заголовок', 'title', 'text' ),
			self::field( 'field_fp02_' . $prefix . '_text', 'Текст', 'text', 'textarea', array( 'rows' => 3 ) ),
			self::field( 'field_fp02_' . $prefix . '_media', 'Медиа', 'media', 'image', array( 'return_format' => 'array' ) ),
		);
	}

	/**
	 * Reusable FAQ subfields.
	 *
	 * @param string $prefix Field key prefix.
	 * @return array<int, mixed>
	 */
	private static function faq_subfields( $prefix ) {
		return array(
			self::field( 'field_fp02_' . $prefix . '_faq_question', __( 'Вопрос', 'shpigovsky-core' ), 'question', 'text' ),
			self::field( 'field_fp02_' . $prefix . '_faq_answer', __( 'Ответ', 'shpigovsky-core' ), 'answer', 'textarea', array( 'rows' => 4 ) ),
		);
	}

	/**
	 * Home rehab program auto-block notice (cards from program pages).
	 * Builds admin-edit URL for /o-centre/programma-lecheniya/ without hardcoding host.
	 *
	 * @return string Safe HTML for ACF message field (esc_html disabled).
	 */
	private static function home_rehab_program_source_notice_message() {
		$url  = '';
		$page = function_exists( 'get_page_by_path' ) ? get_page_by_path( 'o-centre/programma-lecheniya' ) : null;

		if ( $page instanceof \WP_Post ) {
			$url = admin_url( 'post.php?post=' . (int) $page->ID . '&action=edit' );
		}

		if ( '' === $url && function_exists( 'home_url' ) ) {
			$url = home_url( '/o-centre/programma-lecheniya/' );
		}

		$url = esc_url( $url );

		return sprintf(
			/* translators: %s: admin edit or frontend URL for treatment program pages */
			__( 'Автоматический блок: карточки направлений строятся <strong class="fp02-acf-notice-danger">из страниц <a href="%s">программы лечения</a></strong>. На главной редактируются заголовок, описания и показ/скрытие блока.', 'shpigovsky-core' ),
			$url
		);
	}

	/**
	 * Services hub program cards notice (same program pages source as Home).
	 *
	 * @return string Safe HTML for ACF message field (esc_html disabled).
	 */
	private static function services_hub_program_source_notice_message() {
		$url  = '';
		$page = function_exists( 'get_page_by_path' ) ? get_page_by_path( 'o-centre/programma-lecheniya' ) : null;

		if ( $page instanceof \WP_Post ) {
			$url = admin_url( 'post.php?post=' . (int) $page->ID . '&action=edit' );
		}

		if ( '' === $url && function_exists( 'home_url' ) ) {
			$url = home_url( '/o-centre/programma-lecheniya/' );
		}

		$url = esc_url( $url );

		return sprintf(
			/* translators: %s: admin edit or frontend URL for treatment program pages */
			__( 'Автоматический блок: карточки направлений строятся <strong class="fp02-acf-notice-danger">из страниц <a href="%s">программы лечения</a></strong>. На странице «Услуги» редактируются заголовок, описания и показ/скрытие блока.', 'shpigovsky-core' ),
			$url
		);
	}

	/**
	 * Services hub catalog/nav notice with link to service CPT list.
	 *
	 * @param string $message Already-translated HTML message; may include a %s placeholder for the CPT admin URL.
	 * @return string Safe HTML for ACF message field (esc_html disabled).
	 */
	private static function services_hub_catalog_source_notice_message( $message = '' ) {
		$url = function_exists( 'admin_url' ) ? admin_url( 'edit.php?post_type=service' ) : '';
		$url = esc_url( $url );

		if ( '' === $message ) {
			$message = __( 'Автоматический блок: карточки строятся <strong class="fp02-acf-notice-danger">из страниц услуг</strong>. На странице «Услуги» — настройки показа и подписи блока.', 'shpigovsky-core' );
		}

		if ( false !== strpos( $message, '%s' ) ) {
			return sprintf( $message, $url );
		}

		if ( '' !== $url ) {
			$message = str_replace(
				'из страниц услуг',
				sprintf(
					/* translators: %s: services CPT admin list URL */
					'из <a class="fp02-acf-notice-danger" href="%s">страниц услуг</a>',
					$url
				),
				$message
			);
			$message = str_replace(
				'из родительских услуг CPT',
				sprintf(
					/* translators: %s: services CPT admin list URL */
					'из <a class="fp02-acf-notice-danger" href="%s">родительских услуг CPT</a>',
					$url
				),
				$message
			);
		}

		return $message;
	}
}
