<?php
/**
 * Frontend render-time typography hooks (FP-0002 PROD-P16).
 *
 * Narrow surface only: public human-facing text. Admin stored values untouched.
 * ONE TYPOGRAPHY OWNER — delegates all transforms to RussianTypography.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Typography;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Bounded frontend filters for Russian typography.
 */
final class TypographyFilters implements ModuleInterface {

	/**
	 * Recursion / double-apply guard.
	 *
	 * @var bool
	 */
	private static $busy = false;

	/**
	 * ACF field names excluded from typography (technical / URL / SEO raw).
	 *
	 * @var array<int, string>
	 */
	private const ACF_EXCLUDE_NAMES = array(
		'post_name',
		'slug',
		'permalink',
		'canonical',
		'redirect',
		'map_url',
		'map_embed',
		'map_embed_code',
		'yandex_map',
		'video_url',
		'video_file',
		'iframe',
		'embed',
		'schema',
		'json_ld',
		'gtm',
		'metrika',
		'analytics',
		'verification',
		'robots',
		'sitemap',
		'email',
		'phone',
		'tel',
		'whatsapp',
		'telegram',
		'max_url',
		'social_url',
		'url',
		'href',
		'link_url',
		'button_url',
		'cta_url',
		'cta_button_url',
		'all_link_url',
		'image',
		'gallery',
		'file',
		'attachment',
		'css',
		'js',
		'class',
		'id',
	);

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'typography.russian';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		// Late on the_content so TOC heading IDs (priority 5) stay stable.
		add_filter( 'the_content', array( __CLASS__, 'filter_html_content' ), 20 );
		add_filter( 'the_excerpt', array( __CLASS__, 'filter_html_content' ), 20 );
		add_filter( 'the_title', array( __CLASS__, 'filter_plain_title' ), 20, 2 );

		// ACF formatted values on frontend (and REST display after match uses raw DB for scoring).
		add_filter( 'acf/format_value', array( __CLASS__, 'filter_acf_value' ), 20, 3 );

		// Document title parts (browser title) — Unicode only, no HTML entities.
		add_filter( 'document_title_parts', array( __CLASS__, 'filter_document_title_parts' ), 20 );
	}

	/**
	 * Whether typography filters should run.
	 *
	 * @return bool
	 */
	public static function should_apply() {
		if ( self::$busy ) {
			return false;
		}

		if ( is_admin() && ! wp_doing_ajax() ) {
			return false;
		}

		// Cron / CLI: leave stored/raw.
		if ( ( defined( 'WP_CLI' ) && WP_CLI ) || ( function_exists( 'wp_doing_cron' ) && wp_doing_cron() ) ) {
			return false;
		}

		/**
		 * Allow operators/tests to disable render-time typography.
		 *
		 * @param bool $apply Whether to apply.
		 */
		return (bool) apply_filters( 'fp02_typography_should_apply', true );
	}

	/**
	 * @param string $content HTML.
	 * @return string
	 */
	public static function filter_html_content( $content ) {
		if ( ! self::should_apply() || ! is_string( $content ) || '' === $content ) {
			return $content;
		}

		return self::run(
			static function () use ( $content ) {
				return RussianTypography::process_html( $content );
			}
		);
	}

	/**
	 * @param string $title   Title.
	 * @param int    $post_id Post ID (optional).
	 * @return string
	 */
	public static function filter_plain_title( $title, $post_id = 0 ) {
		unset( $post_id );

		if ( ! self::should_apply() || ! is_string( $title ) || '' === $title ) {
			return $title;
		}

		// Nav menus / feed sometimes pass HTML — detect.
		if ( false !== strpos( $title, '<' ) ) {
			return self::run(
				static function () use ( $title ) {
					return RussianTypography::process_html( $title );
				}
			);
		}

		return self::run(
			static function () use ( $title ) {
				return RussianTypography::process_plain( $title );
			}
		);
	}

	/**
	 * @param mixed $value   Field value.
	 * @param mixed $post_id Post ID / option.
	 * @param array $field   ACF field array.
	 * @return mixed
	 */
	public static function filter_acf_value( $value, $post_id, $field ) {
		unset( $post_id );

		if ( ! self::should_apply() ) {
			return $value;
		}

		if ( ! is_array( $field ) ) {
			return $value;
		}

		$type = isset( $field['type'] ) ? (string) $field['type'] : '';
		$name = isset( $field['name'] ) ? (string) $field['name'] : '';

		if ( self::acf_name_excluded( $name ) ) {
			return $value;
		}

		if ( ! in_array( $type, array( 'text', 'textarea', 'wysiwyg' ), true ) ) {
			return $value;
		}

		if ( ! is_string( $value ) || '' === $value ) {
			return $value;
		}

		$kind = ( 'wysiwyg' === $type ) ? 'html' : 'plain';
		if ( 'textarea' === $type && false !== strpos( $value, '<' ) ) {
			$kind = 'html';
		}

		return self::run(
			static function () use ( $value, $kind ) {
				return RussianTypography::process( $value, $kind );
			}
		);
	}

	/**
	 * @param array<string, string> $parts Title parts.
	 * @return array<string, string>
	 */
	public static function filter_document_title_parts( $parts ) {
		if ( ! self::should_apply() || ! is_array( $parts ) ) {
			return $parts;
		}

		foreach ( $parts as $key => $part ) {
			if ( ! is_string( $part ) || '' === $part ) {
				continue;
			}
			if ( in_array( $key, array( 'title', 'tagline', 'site', 'page' ), true ) ) {
				$parts[ $key ] = self::run(
					static function () use ( $part ) {
						return RussianTypography::process_plain( $part );
					}
				);
			}
		}

		return $parts;
	}

	/**
	 * @param string $name Field name.
	 * @return bool
	 */
	private static function acf_name_excluded( $name ) {
		$name = strtolower( (string) $name );
		if ( '' === $name ) {
			return true;
		}

		foreach ( self::ACF_EXCLUDE_NAMES as $needle ) {
			if ( $name === $needle || false !== strpos( $name, $needle ) ) {
				// Avoid over-matching: require suffix/prefix boundaries for short needles.
				if ( strlen( $needle ) <= 3 ) {
					if ( preg_match( '/(^|_)' . preg_quote( $needle, '/' ) . '(_|$)/', $name ) ) {
						return true;
					}
					continue;
				}
				return true;
			}
		}

		// SEO meta: typograph carefully as plain Unicode (allowed) unless key looks like raw robots.
		if ( preg_match( '/(seo_.*url|canonical|robots|og_image)/', $name ) ) {
			return true;
		}

		return false;
	}

	/**
	 * @param callable $cb Callback returning string.
	 * @return string
	 */
	private static function run( $cb ) {
		self::$busy = true;
		try {
			$result = $cb();
		} finally {
			self::$busy = false;
		}
		return is_string( $result ) ? $result : '';
	}
}
