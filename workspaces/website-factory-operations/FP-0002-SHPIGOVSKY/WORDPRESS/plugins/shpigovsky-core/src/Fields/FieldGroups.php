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
	public const MODIFIED = 1784200800;

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
	 * Return deterministic field group definitions.
	 *
	 * @return array<int, array<string, mixed>>
	 */
	public static function get_field_groups() {
		return array(
			self::service_layout_hero(),
			self::service_structured_sections(),
			self::service_faq(),
			self::service_relationships(),
			self::page_home(),
			self::page_services_hub(),
			self::page_ocentre_hub(),
			self::page_institutional_child(),
			self::page_contacts(),
			self::page_reviews(),
			self::page_legal(),
			self::blog_post_article_meta(),
			self::blog_archive_settings(),
			self::site_options_contacts(),
			self::site_options_modal_cta(),
			self::block_final_form(),
			self::block_specialists(),
			self::block_cta_bands(),
			self::block_header(),
			self::block_footer(),
			self::block_comfort_benefits(),
		);
	}

	/**
	 * Service layout and hero group.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_layout_hero() {
		return self::group(
			'group_fp02_service_layout_hero',
			'Service — Layout and Hero',
			array(
				self::field(
					'field_fp02_service_layout_variant',
					'Вариант макета',
					'service_layout_variant',
					'select',
					array(
						'instructions' => 'Allowed V9-06C values: subdivision, standard, extended, alcohol_special, placeholder.',
						'required'     => 1,
						'choices'      => array(
							'subdivision'     => 'Подраздел',
							'standard'        => 'Стандартная услуга',
							'extended'        => 'Расширенная услуга',
							'alcohol_special' => 'Алкогольная зависимость',
							'placeholder'     => 'Заглушка',
						),
						'default_value' => 'standard',
						'return_format' => 'value',
					)
				),
				self::field( 'field_fp02_hero_eyebrow_service', 'Надзаголовок', 'hero_eyebrow', 'text' ),
				self::field( 'field_fp02_hero_title_override_service', 'Заголовок H1 override', 'hero_title_override', 'text' ),
				self::field( 'field_fp02_hero_lead_service', 'Лид', 'hero_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field(
					'field_fp02_service_short_description',
					'Мини-описание',
					'service_short_description',
					'textarea',
					array(
						'instructions' => 'Краткий текст для карточки услуги на странице /uslugi/ (оба режима отображения).',
						'rows'         => 4,
					)
				),
				self::field( 'field_fp02_hero_media_service', 'Hero image', 'hero_media', 'image', array( 'instructions' => 'Hero background image for this service. Empty falls back to theme asset by layout variant.', 'return_format' => 'array', 'preview_size' => 'medium' ) ),
				self::field(
					'field_fp02_hero_cta_label_service',
					'Текст кнопки в hero-блоке',
					'hero_cta_label',
					'text',
					array(
						'instructions' => 'Индивидуальный текст кнопки для hero-блока этой страницы/услуги. Если оставить пустым, используется текущий текст по умолчанию.',
					)
				),
				self::field( 'field_fp02_hero_cta_target_service', 'CTA target', 'hero_cta_target', 'url' ),
			),
			self::location( 'post_type', '==', 'service' )
		);
	}

	/**
	 * Service structured sections group.
	 *
	 * @return array<string, mixed>
	 */
	private static function service_structured_sections() {
		return self::group(
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
						self::field( 'field_fp02_signs_item_title_service', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_signs_item_text_service', 'Текст', 'text', 'textarea', array( 'rows' => 3 ) ),
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
						self::field( 'field_fp02_stage_title_service', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_stage_text_service', 'Текст', 'text', 'textarea', array( 'rows' => 3 ) ),
					)
				),
				self::field( 'field_fp02_cta_title_service', 'CTA title', 'cta_title', 'text' ),
				self::field( 'field_fp02_cta_text_service', 'CTA text', 'cta_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_cta_button_label_service', 'CTA button label', 'cta_button_label', 'text' ),
				self::field( 'field_fp02_cta_button_target_service', 'CTA button target', 'cta_button_target', 'url' ),
			),
			self::location( 'post_type', '==', 'service' )
		);
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
		return self::group(
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
	}

	/**
	 * Home page group.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_home() {
		return self::group(
			'group_fp02_page_home',
			'Page — Home',
			array(
				self::field(
					'field_fp02_hero_media_home',
					'Hero image',
					'hero_media',
					'image',
					array(
						'instructions' => 'Primary hero image. Overrides slide image when set. Empty falls back to Hero slides image, then theme asset.',
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field(
					'field_fp02_hero_cta_label_home',
					'Текст кнопки в hero-блоке',
					'hero_cta_label',
					'text',
					array(
						'instructions' => 'Индивидуальный текст кнопки для hero-блока этой страницы/услуги. Если оставить пустым, используется текущий текст по умолчанию.',
					)
				),
				self::repeater(
					'field_fp02_home_hero_slides',
					'Hero slides',
					'home_hero_slides',
					5,
					array(
						self::field( 'field_fp02_home_hero_title', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_home_hero_text', 'Текст', 'text', 'textarea', array( 'rows' => 3 ) ),
						self::field( 'field_fp02_home_hero_image', 'Изображение', 'image', 'image', array( 'return_format' => 'array' ) ),
					)
				),
				self::repeater( 'field_fp02_home_service_nav_items', 'Настройки service navigation / accordion', 'home_service_nav_items', 6, self::title_text_subfields( 'home_service_nav' ) ),
				self::repeater( 'field_fp02_home_advantages', 'Advantages / trust', 'home_advantages', 8, self::title_text_subfields( 'home_advantages' ) ),
				self::repeater( 'field_fp02_home_intro_bands', 'Intro bands', 'home_intro_bands', 6, self::title_text_subfields( 'home_intro_bands' ) ),
				self::repeater( 'field_fp02_home_reviews_teaser', 'Reviews teaser', 'home_reviews_teaser', 6, self::title_text_subfields( 'home_reviews_teaser' ) ),
				self::field( 'field_fp02_home_blog_teaser_enabled', 'Blog teaser enabled', 'home_blog_teaser_enabled', 'true_false' ),
				self::repeater( 'field_fp02_home_gallery_media', 'Gallery / media bands', 'home_gallery_media', 12, self::media_text_subfields( 'home_gallery_item' ) ),
				self::repeater( 'field_fp02_home_faq_items', 'FAQ', 'home_faq_items', 15, self::faq_subfields( 'home' ) ),
				self::field( 'field_fp02_home_cta_title', 'CTA title', 'home_cta_title', 'text' ),
				self::field( 'field_fp02_home_cta_text', 'CTA text', 'home_cta_text', 'textarea', array( 'rows' => 3 ) ),
			),
			self::location( 'page_type', '==', 'front_page' )
		);
	}

	/**
	 * Services hub page group.
	 *
	 * @return array<string, mixed>
	 */
	private static function page_services_hub() {
		return self::group(
			'group_fp02_page_services_hub',
			'Page — Services Hub',
			array(
				self::field( 'field_fp02_hero_eyebrow_hub', 'Hero eyebrow', 'hero_eyebrow', 'text' ),
				self::field( 'field_fp02_hero_title_override_hub', 'Hero H1 override', 'hero_title_override', 'text' ),
				self::field(
					'field_fp02_hero_media_hub',
					'Hero image',
					'hero_media',
					'image',
					array(
						'instructions' => 'Hero background image for /uslugi/. Empty falls back to theme asset services-hero.webp.',
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field( 'field_fp02_services_hub_intro', 'Hero lead / intro', 'services_hub_intro', 'textarea', array( 'rows' => 5 ) ),
				self::field(
					'field_fp02_hero_cta_label_hub',
					'Текст кнопки в hero-блоке',
					'hero_cta_label',
					'text',
					array(
						'instructions' => 'Индивидуальный текст кнопки для hero-блока этой страницы/услуги. Если оставить пустым, используется текущий текст по умолчанию.',
					)
				),
				self::field( 'field_fp02_services_hub_query_mode', 'Query display mode', 'services_hub_query_mode', 'select', array( 'choices' => array( 'grouped_by_parent' => 'Grouped by parent', 'flat' => 'Flat' ), 'default_value' => 'grouped_by_parent' ) ),
				self::field( 'field_fp02_services_hub_show_placeholders', 'Show placeholder services', 'services_hub_show_placeholders', 'true_false' ),
				self::repeater( 'field_fp02_services_hub_faq_items', 'FAQ', 'services_hub_faq_items', 15, self::faq_subfields( 'services_hub' ) ),
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
				self::repeater(
					'field_fp02_about_program_items',
					'О центре — Программа: направления',
					'about_program_items',
					4,
					array(
						self::field( 'field_fp02_about_program_item_title', 'Заголовок', 'title', 'text' ),
						self::field( 'field_fp02_about_program_item_image', 'Изображение', 'image', 'image', array( 'return_format' => 'array' ) ),
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
			),
			self::location_page_id( 11 )
		);
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
				self::field( 'field_fp02_contacts_address', 'Address', 'contacts_address', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_contacts_map_url', 'Map URL', 'contacts_map_url', 'url' ),
				self::repeater( 'field_fp02_contacts_phones', 'Phones', 'contacts_phones', 4, array( self::field( 'field_fp02_contacts_phone_label', 'Label', 'label', 'text' ), self::field( 'field_fp02_contacts_phone_value', 'Phone', 'phone', 'text' ) ) ),
				self::repeater( 'field_fp02_contacts_messengers', 'Messengers', 'contacts_messengers', 6, array( self::field( 'field_fp02_contacts_messenger_label', 'Label', 'label', 'text' ), self::field( 'field_fp02_contacts_messenger_url', 'URL', 'url', 'url' ) ) ),
				self::repeater( 'field_fp02_contacts_blocks', 'Contact blocks', 'contacts_blocks', 8, self::title_text_subfields( 'contacts_block' ) ),
				self::field( 'field_fp02_contacts_form_intro', 'Form intro', 'contacts_form_intro', 'textarea', array( 'rows' => 3 ) ),
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
				self::repeater(
					'field_fp02_reviews_items',
					'Reviews',
					'reviews_items',
					50,
					array(
						self::field( 'field_fp02_review_author_label', 'Author label', 'author_label', 'text' ),
						self::field( 'field_fp02_review_text', 'Review text', 'text', 'textarea', array( 'rows' => 5 ) ),
						self::field( 'field_fp02_review_meta', 'Metadata', 'metadata', 'text' ),
						self::field( 'field_fp02_review_source', 'Source', 'source', 'text' ),
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
				self::field( 'field_fp02_article_reading_time', 'Reading time', 'article_reading_time', 'number', array( 'min' => 0 ) ),
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
				self::field( 'field_fp02_blog_archive_eyebrow', 'Eyebrow', 'blog_archive_eyebrow', 'text' ),
				self::field( 'field_fp02_blog_archive_title', 'Archive H1', 'blog_archive_title', 'text' ),
				self::field( 'field_fp02_blog_archive_lead', 'Lead', 'blog_archive_lead', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_blog_archive_intro', 'Intro', 'blog_archive_intro', 'textarea', array( 'rows' => 4 ) ),
				self::field( 'field_fp02_blog_archive_featured_label', 'Featured label', 'blog_archive_featured_label', 'text' ),
				self::field( 'field_fp02_blog_archive_all_label', 'All articles label', 'blog_archive_all_label', 'text' ),
				self::field( 'field_fp02_blog_archive_empty_title', 'Empty state title', 'blog_archive_empty_title', 'text' ),
				self::field( 'field_fp02_blog_archive_empty_text', 'Empty state text', 'blog_archive_empty_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_blog_archive_card_link_label', 'Card link label', 'blog_archive_card_link_label', 'text', array( 'default_value' => 'Читать' ) ),
				self::field(
					'field_fp02_blog_archive_card_fallback_image',
					'Card fallback image',
					'blog_archive_card_fallback_image',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field( 'field_fp02_blog_archive_final_cta_title', 'Final CTA title', 'blog_archive_final_cta_title', 'text' ),
				self::field( 'field_fp02_blog_archive_final_cta_text', 'Final CTA text', 'blog_archive_final_cta_text', 'textarea', array( 'rows' => 3 ) ),
				self::field( 'field_fp02_blog_archive_final_cta_phone', 'Final CTA phone', 'blog_archive_final_cta_phone', 'text' ),
				self::field( 'field_fp02_blog_archive_final_cta_phone_hint', 'Final CTA phone hint', 'blog_archive_final_cta_phone_hint', 'text' ),
				self::field( 'field_fp02_blog_archive_final_cta_button_label', 'Final CTA button label', 'blog_archive_final_cta_button_label', 'text' ),
				self::field( 'field_fp02_blog_archive_final_cta_button_url', 'Final CTA button URL', 'blog_archive_final_cta_button_url', 'url' ),
				self::field( 'field_fp02_blog_archive_expert_quote_text', 'Expert quote text', 'blog_archive_expert_quote_text', 'textarea', array( 'rows' => 5 ) ),
				self::field( 'field_fp02_blog_archive_expert_name', 'Expert name', 'blog_archive_expert_name', 'text' ),
				self::field( 'field_fp02_blog_archive_expert_role', 'Expert role', 'blog_archive_expert_role', 'text' ),
				self::field(
					'field_fp02_blog_archive_expert_photo',
					'Expert photo',
					'blog_archive_expert_photo',
					'image',
					array(
						'return_format' => 'array',
						'preview_size'  => 'medium',
					)
				),
				self::field( 'field_fp02_blog_archive_expert_cta_label', 'Expert CTA label', 'blog_archive_expert_cta_label', 'text' ),
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
	 * @return array<string, mixed>
	 */
	private static function block_specialists() {
		return self::group(
			'group_fp02_block_specialists',
			'Reusable Block — Specialists',
			array(
				self::field( 'field_fp02_specialists_section_heading', 'Заголовок секции', 'specialists_section_heading', 'text' ),
				self::field( 'field_fp02_specialists_all_link_label', 'Текст ссылки «все специалисты»', 'specialists_all_link_label', 'text' ),
				self::field( 'field_fp02_specialists_all_link_url', 'URL ссылки «все специалисты»', 'specialists_all_link_url', 'url' ),
				self::repeater(
					'field_fp02_specialists_items',
					'Специалисты',
					'specialists_items',
					12,
					array(
						self::field(
							'field_fp02_specialist_photo',
							'Фото (медиа)',
							'specialist_photo',
							'image',
							array(
								'return_format' => 'array',
								'preview_size'  => 'medium',
								'instructions'  => 'Опционально. Пусто — theme asset path ниже или V9 fallback.',
							)
						),
						self::field(
							'field_fp02_specialist_photo_asset',
							'Theme asset path',
							'specialist_photo_asset',
							'text',
							array(
								'instructions' => 'Относительный путь в theme/assets, напр. img/content/home-specialists/sergey-shpigovsky.webp',
							)
						),
						self::field( 'field_fp02_specialist_photo_width', 'Ширина (px)', 'specialist_photo_width', 'number', array( 'min' => 0 ) ),
						self::field( 'field_fp02_specialist_photo_height', 'Высота (px)', 'specialist_photo_height', 'number', array( 'min' => 0 ) ),
						self::field( 'field_fp02_specialist_name', 'Имя', 'specialist_name', 'text' ),
						self::field( 'field_fp02_specialist_role', 'Роль / специализация', 'specialist_role', 'textarea', array( 'rows' => 3 ) ),
						self::field( 'field_fp02_specialist_link', 'Ссылка (опционально)', 'specialist_link', 'url' ),
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
					'Заголовок CTA по умолчанию',
					'cta_band_default_title',
					'text',
					array(
						'instructions' => 'Используется когда у услуги нет cta_title. Пусто — global_cta_title из Общих настроек.',
					)
				),
				self::field(
					'field_fp02_cta_band_default_subtitle',
					'Текст CTA по умолчанию',
					'cta_band_default_subtitle',
					'textarea',
					array(
						'rows'         => 3,
						'instructions' => 'Пусто — global_cta_text из Общих настроек.',
					)
				),
				self::field( 'field_fp02_cta_band_phone_hint', 'Подпись телефона', 'cta_band_phone_hint', 'text' ),
				self::field(
					'field_fp02_cta_band_default_button_label',
					'Текст кнопки по умолчанию',
					'cta_band_default_button_label',
					'text',
					array(
						'instructions' => 'Пусто — default_button_label из Общих настроек.',
					)
				),
			),
			self::location( 'options_page', '==', 'fp02-block-cta-bands' )
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
	 * Reusable block — comfort / requirements / benefits (V9-06E21 Batch 2).
	 *
	 * @return array<string, mixed>
	 */
	private static function block_comfort_benefits() {
		return self::group(
			'group_fp02_block_comfort',
			'Reusable Block — Comfort / Benefits',
			array(
				self::field( 'field_fp02_comfort_heading', 'Комфорт — заголовок', 'comfort_heading', 'text' ),
				self::field( 'field_fp02_comfort_lead', 'Комфорт — лид', 'comfort_lead', 'textarea', array( 'rows' => 4 ) ),
				self::field( 'field_fp02_comfort_all_link_label', 'Комфорт — текст ссылки', 'comfort_all_link_label', 'text' ),
				self::field( 'field_fp02_comfort_all_link_url', 'Комфорт — URL ссылки', 'comfort_all_link_url', 'url' ),
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
			self::location( 'options_page', '==', 'fp02-block-comfort' )
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
			self::field( 'field_fp02_' . $prefix . '_title', 'Заголовок', 'title', 'text' ),
			self::field( 'field_fp02_' . $prefix . '_text', 'Текст', 'text', 'textarea', array( 'rows' => 3 ) ),
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
			self::field( 'field_fp02_' . $prefix . '_faq_question', 'Вопрос', 'question', 'text' ),
			self::field( 'field_fp02_' . $prefix . '_faq_answer', 'Ответ', 'answer', 'textarea', array( 'rows' => 4 ) ),
		);
	}
}
