<?php
/**
 * Structured social / messenger settings — PROD-P13.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ACF repeater: platform type + URL + header/footer visibility.
 */
final class SocialPlatformsOptions {

	public const OPTION_MIGRATED = 'fp02_social_platforms_migrated';
	public const PAGE_SLUG       = 'fp02-site-settings-social';

	/**
	 * Field group.
	 *
	 * @return array<string, mixed>
	 */
	public static function group() {
		return array(
			'key'                   => 'group_fp02_site_options_social_platforms',
			'title'                 => __( 'Social networks and messengers', 'shpigovsky-core' ),
			'fields'                => array(
				array(
					'key'           => 'field_fp02_social_platforms_intro',
					'label'         => __( 'Platforms', 'shpigovsky-core' ),
					'name'          => 'social_platforms_intro',
					'type'          => 'message',
					'message'       => __( 'One row per platform. Type selects the icon and label. Empty URL hides that platform. Header and footer flags are independent. The Contacts page shows every configured platform with a URL.', 'shpigovsky-core' ),
					'new_lines'     => 'wpautop',
					'esc_html'      => 0,
				),
				array(
					'key'          => 'field_fp02_social_platforms',
					'label'        => __( 'Social networks and messengers', 'shpigovsky-core' ),
					'name'         => 'social_platforms',
					'type'         => 'repeater',
					'layout'       => 'row',
					'button_label' => __( 'Add platform', 'shpigovsky-core' ),
					'min'          => 0,
					'max'          => 8,
					'sub_fields'   => array(
						array(
							'key'           => 'field_fp02_social_platform_type',
							'label'         => __( 'Platform', 'shpigovsky-core' ),
							'name'          => 'type',
							'type'          => 'select',
							'choices'       => self::type_choices(),
							'allow_null'    => 0,
							'ui'            => 1,
							'return_format' => 'value',
							'wrapper'       => array( 'width' => '25', 'class' => '', 'id' => '' ),
						),
						array(
							'key'     => 'field_fp02_social_platform_url',
							'label'   => __( 'Link', 'shpigovsky-core' ),
							'name'    => 'url',
							'type'    => 'url',
							'wrapper' => array( 'width' => '45', 'class' => '', 'id' => '' ),
						),
						array(
							'key'           => 'field_fp02_social_platform_show_header',
							'label'         => __( 'Show in header', 'shpigovsky-core' ),
							'name'          => 'show_header',
							'type'          => 'true_false',
							'ui'            => 1,
							'default_value' => 1,
							'wrapper'       => array( 'width' => '15', 'class' => '', 'id' => '' ),
						),
						array(
							'key'           => 'field_fp02_social_platform_show_footer',
							'label'         => __( 'Show in footer', 'shpigovsky-core' ),
							'name'          => 'show_footer',
							'type'          => 'true_false',
							'ui'            => 1,
							'default_value' => 1,
							'wrapper'       => array( 'width' => '15', 'class' => '', 'id' => '' ),
						),
					),
				),
			),
			'location'              => array(
				array(
					array(
						'param'    => 'options_page',
						'operator' => '==',
						'value'    => self::PAGE_SLUG,
					),
				),
			),
			'menu_order'            => 0,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'instruction_placement' => 'label',
			'active'                => true,
			'description'           => 'FP-0002 PROD-P13 social/messenger settings.',
			'show_in_rest'          => 0,
			'modified'              => 1786838400,
		);
	}

	/**
	 * Platform choices that already have theme icons.
	 *
	 * @return array<string, string>
	 */
	public static function type_choices() {
		return array(
			'telegram' => 'Telegram',
			'whatsapp' => 'WhatsApp',
			'max'      => 'MAX',
			'youtube'  => 'YouTube',
		);
	}

	/**
	 * One-time migration from legacy social_links. Preserves current URLs.
	 */
	public static function maybe_migrate() {
		if ( get_option( self::OPTION_MIGRATED ) ) {
			return;
		}
		if ( ! function_exists( 'get_field' ) || ! function_exists( 'update_field' ) ) {
			return;
		}

		$existing = get_field( 'social_platforms', 'option' );
		if ( is_array( $existing ) && ! empty( $existing ) ) {
			update_option( self::OPTION_MIGRATED, '1', false );
			return;
		}

		$legacy = get_field( 'social_links', 'option' );
		if ( ! is_array( $legacy ) ) {
			$legacy = array();
		}

		$mapped = array();
		$seen   = array();
		foreach ( $legacy as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$url   = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
			$label = isset( $row['label'] ) ? trim( (string) $row['label'] ) : '';
			if ( '' === $url || '#' === $url ) {
				continue;
			}
			$type = self::infer_type( $label, $url );
			if ( '' === $type || isset( $seen[ $type ] ) ) {
				continue;
			}
			$seen[ $type ] = true;
			$mapped[]      = array(
				'type'        => $type,
				'url'         => $url,
				'show_header' => 1,
				'show_footer' => 1,
			);
		}

		if ( ! empty( $mapped ) ) {
			update_field( 'social_platforms', $mapped, 'option' );
		}

		update_option( self::OPTION_MIGRATED, '1', false );
	}

	/**
	 * Infer a known platform type from label + URL. Unknown → empty.
	 *
	 * @param string $label Label.
	 * @param string $url   URL.
	 * @return string
	 */
	public static function infer_type( $label, $url ) {
		$hay = mb_strtolower( trim( $label . ' ' . $url ) );

		if ( str_contains( $hay, 't.me' ) || str_contains( $hay, 'telegram' ) ) {
			return 'telegram';
		}
		if ( str_contains( $hay, 'wa.me' ) || str_contains( $hay, 'whatsapp' ) || str_contains( $hay, 'what\'s up' ) || str_contains( $hay, 'whats up' ) ) {
			return 'whatsapp';
		}
		if ( str_contains( $hay, 'youtu' ) ) {
			return 'youtube';
		}
		if ( str_contains( $hay, 'max.ru' ) || preg_match( '/(^|[^a-z])max([^a-z]|$)/', $hay ) ) {
			return 'max';
		}

		return '';
	}
}
