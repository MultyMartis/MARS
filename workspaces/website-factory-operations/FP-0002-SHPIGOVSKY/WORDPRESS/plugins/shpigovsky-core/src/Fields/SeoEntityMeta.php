<?php
/**
 * Per-entity SEO Title + Meta Description — PROD-P13.
 *
 * Public singles: page, post, service, specialist.
 * Reviews have no public single URL — no fields.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ACF SEO meta for public content entities.
 */
final class SeoEntityMeta {

	public const GROUP_KEY = 'group_fp02_seo_entity_meta';

	/**
	 * Field group definition.
	 *
	 * @return array<string, mixed>
	 */
	public static function group() {
		return array(
			'key'                   => self::GROUP_KEY,
			'title'                 => __( 'SEO', 'shpigovsky-core' ),
			'fields'                => array(
				array(
					'key'           => 'field_fp02_seo_title',
					'label'         => __( 'SEO Title', 'shpigovsky-core' ),
					'name'          => 'fp02_seo_title',
					'type'          => 'text',
					'instructions'  => __( 'Optional. If empty, the public title uses the object title and site name.', 'shpigovsky-core' ),
					'maxlength'     => 70,
				),
				array(
					'key'           => 'field_fp02_seo_description',
					'label'         => __( 'Meta Description', 'shpigovsky-core' ),
					'name'          => 'fp02_seo_description',
					'type'          => 'textarea',
					'instructions'  => __( 'Optional. If empty, no meta description is output (marketing copy is not invented).', 'shpigovsky-core' ),
					'rows'          => 3,
					'maxlength'     => 180,
					'new_lines'     => '',
				),
			),
			'location'              => array(
				array( array( 'param' => 'post_type', 'operator' => '==', 'value' => 'page' ) ),
				array( array( 'param' => 'post_type', 'operator' => '==', 'value' => 'post' ) ),
				array( array( 'param' => 'post_type', 'operator' => '==', 'value' => 'service' ) ),
				array( array( 'param' => 'post_type', 'operator' => '==', 'value' => 'specialist' ) ),
			),
			'menu_order'            => 80,
			'position'              => 'side',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'active'                => true,
			'description'           => 'FP-0002 PROD-P13 entity SEO title + meta description.',
			'show_in_rest'          => 0,
			'modified'              => 1786838400,
		);
	}
}
