<?php
/**
 * Glossary ACF field group (PHP registration; no acf-json in theme).
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register ACF fields for glossary terms.
 */
function iseo_glossary_register_acf_fields() {
	if ( ! function_exists( 'acf_add_local_field_group' ) ) {
		return;
	}

	acf_add_local_field_group(
		array(
			'key'                   => 'group_iseo_glossary_term',
			'title'                 => 'Глоссарий — метаданные термина',
			'fields'                => array(
				array(
					'key'           => 'field_iseo_glossary_synonyms',
					'label'         => 'Синонимы',
					'name'          => 'glossary_synonyms',
					'type'          => 'textarea',
					'instructions'  => 'Синонимы и близкие формулировки. Не дублируйте полный текст определения из редактора.',
					'required'      => 0,
					'rows'          => 3,
					'new_lines'     => '',
				),
				array(
					'key'           => 'field_iseo_glossary_keywords',
					'label'         => 'Ключевые слова',
					'name'          => 'glossary_keywords',
					'type'          => 'textarea',
					'instructions'  => 'Редакционные ключевые слова из рабочей таблицы (не публичное определение).',
					'required'      => 0,
					'rows'          => 3,
					'new_lines'     => '',
				),
				array(
					'key'           => 'field_iseo_glossary_lsi',
					'label'         => 'LSI-фразы',
					'name'          => 'glossary_lsi_phrases',
					'type'          => 'textarea',
					'instructions'  => 'LSI-фразы из рабочей таблицы (редакционные).',
					'required'      => 0,
					'rows'          => 3,
					'new_lines'     => '',
				),
				array(
					'key'           => 'field_iseo_glossary_related_terms',
					'label'         => 'Связанные понятия',
					'name'          => 'glossary_related_terms',
					'type'          => 'textarea',
					'instructions'  => 'Канонические названия связанных терминов через «; ». На сайте ссылки только на опубликованные eligible записи.',
					'required'      => 0,
					'rows'          => 3,
					'new_lines'     => '',
				),
				array(
					'key'           => 'field_iseo_glossary_source_notes',
					'label'         => 'Внутренние заметки',
					'name'          => 'glossary_source_notes',
					'type'          => 'textarea',
					'instructions'  => 'Только для редакции. Не выводится на сайте.',
					'required'      => 0,
					'rows'          => 2,
					'new_lines'     => '',
				),
			),
			'location'              => array(
				array(
					array(
						'param'    => 'post_type',
						'operator' => '==',
						'value'    => 'glossary',
					),
				),
			),
			'menu_order'            => 0,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'active'                => true,
			'show_in_rest'          => 0,
		)
	);
}
add_action( 'acf/init', 'iseo_glossary_register_acf_fields' );

/**
 * Expose related-terms meta to authenticated REST for bounded launch tooling.
 */
function iseo_glossary_register_related_meta() {
	register_post_meta(
		'glossary',
		'glossary_related_terms',
		array(
			'type'              => 'string',
			'single'            => true,
			'show_in_rest'      => true,
			'auth_callback'     => static function () {
				return current_user_can( 'edit_posts' );
			},
			'sanitize_callback' => 'sanitize_textarea_field',
		)
	);
}
add_action( 'init', 'iseo_glossary_register_related_meta' );
