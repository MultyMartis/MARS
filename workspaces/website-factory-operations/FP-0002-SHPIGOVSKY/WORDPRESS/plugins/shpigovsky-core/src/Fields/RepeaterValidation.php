<?php
/**
 * Repeater validation — server-side bounded repeater enforcement.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Repeater max-item validation boundary.
 */
final class RepeaterValidation implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'fields.repeater-validation';
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
		add_action( 'acf/validate_save_post', array( __CLASS__, 'validate_repeaters' ) );
		add_filter( 'acf/validate_value/name=service_layout_variant', array( __CLASS__, 'validate_service_layout' ), 10, 4 );
		add_filter( 'acf/validate_value/name=manual_related_services', array( __CLASS__, 'validate_related_services' ), 10, 4 );
		add_filter( 'acf/validate_value/type=url', array( __CLASS__, 'validate_url_field' ), 10, 4 );
		add_filter( 'acf/validate_value/type=email', array( __CLASS__, 'validate_email_field' ), 10, 4 );
		add_filter( 'acf/validate_value/name=programme_items', array( __CLASS__, 'validate_optional_programme_items' ), 10, 4 );
		add_filter( 'acf/validate_value/name=signs_items', array( __CLASS__, 'validate_optional_structured_repeater' ), 10, 4 );
		add_filter( 'acf/validate_value/name=stages', array( __CLASS__, 'validate_optional_structured_repeater' ), 10, 4 );
		add_action( 'save_post_' . Service::POST_TYPE, array( __CLASS__, 'validate_service_depth_on_save' ), 10, 3 );
	}

	/**
	 * Validate repeater field bounds on save.
	 */
	public static function validate_repeaters() {
		if ( empty( $_POST['acf'] ) || ! is_array( $_POST['acf'] ) || ! function_exists( 'acf_add_validation_error' ) ) {
			return;
		}

		foreach ( self::get_repeater_limits() as $field_key => $max_rows ) {
			if ( isset( $_POST['acf'][ $field_key ] ) && ! self::is_within_max_rows( $_POST['acf'][ $field_key ], $max_rows ) ) {
				acf_add_validation_error(
					'acf[' . $field_key . ']',
					sprintf(
						/* translators: %d: maximum repeater rows. */
						__( 'Максимальное количество строк: %d.', 'shpigovsky-core' ),
						$max_rows
					)
				);
			}
		}
	}

	/**
	 * Repeater max rows by field key.
	 *
	 * @return array<string, int>
	 */
	public static function get_repeater_limits() {
		return array(
			'field_fp02_signs_items_service'       => 12,
			'field_fp02_programme_items_service'   => 6,
			'field_fp02_stages_service'            => 8,
			'field_fp02_faq_items_service'         => 15,
			'field_fp02_section_nature_cards'      => 4,
			'field_fp02_section_approach_cards'    => 6,
			'field_fp02_section_stages_support_items' => 8,
			'field_fp02_home_hero_slides'          => 5,
			'field_fp02_home_advantages'           => 8,
			'field_fp02_home_intro_bands'          => 6,
			'field_fp02_home_recovery_intro_benefits' => 12,
			'field_fp02_home_why_us_body'          => 6,
			'field_fp02_home_why_us_items'         => 12,
			'field_fp02_home_recovery_life_intro'  => 6,
			'field_fp02_home_recovery_life_stages' => 8,
			'field_fp02_home_genotyping_body'      => 6,
			'field_fp02_home_genotyping_items'     => 12,
			'field_fp02_home_videos_items'         => 8,
			'field_fp02_home_faq_items'            => 15,
			'field_fp02_services_hero_slides'      => 5,
			'field_fp02_services_hub_faq_items'    => 15,
			'field_fp02_institutional_content_sections' => 8,
			'field_fp02_institutional_stages'      => 8,
			'field_fp02_infrastructure_g0_g5'      => 6,
			'field_fp02_contacts_phones'           => 4,
			'field_fp02_contacts_messengers'       => 6,
			'field_fp02_contacts_locations'        => 8,
			'field_fp02_reviews_items'             => 50,
			'field_fp02_social_links'              => 8,
		);
	}

	/**
	 * Allowed service layout values.
	 *
	 * @return array<int, string>
	 */
	public static function get_allowed_service_layouts() {
		return array( 'subdivision', 'standard', 'extended', 'service_general', 'alcohol_special', 'placeholder' );
	}

	/**
	 * Validate row count without requiring ACF runtime.
	 *
	 * @param mixed $value Field value.
	 * @param int   $max_rows Max rows.
	 * @return bool
	 */
	public static function is_within_max_rows( $value, $max_rows ) {
		if ( null === $value || '' === $value || false === $value ) {
			return true;
		}

		if ( ! is_array( $value ) ) {
			return true;
		}

		return count( $value ) <= $max_rows;
	}

	/**
	 * Validate service layout enum.
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Value.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_service_layout( $valid, $value, $field, $input ) {
		if ( true !== $valid ) {
			return $valid;
		}

		return in_array( $value, self::get_allowed_service_layouts(), true )
			? true
			: __( 'Недопустимый вариант макета услуги.', 'shpigovsky-core' );
	}

	/**
	 * Validate related services field.
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Related IDs/objects.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_related_services( $valid, $value, $field, $input ) {
		if ( true !== $valid || empty( $value ) ) {
			return $valid;
		}

		$current_id = isset( $_POST['post_ID'] ) ? (int) $_POST['post_ID'] : 0;

		foreach ( (array) $value as $related ) {
			$related_id = is_object( $related ) && isset( $related->ID ) ? (int) $related->ID : (int) $related;

			if ( $current_id && $related_id === $current_id ) {
				return __( 'Услуга не может быть связана сама с собой.', 'shpigovsky-core' );
			}

			if ( $related_id && Service::POST_TYPE !== get_post_type( $related_id ) ) {
				return __( 'Связанные материалы должны быть услугами.', 'shpigovsky-core' );
			}
		}

		return true;
	}

	/**
	 * Validate service max depth on save.
	 *
	 * @param int      $post_id Post ID.
	 * @param \WP_Post $post Post object.
	 * @param bool     $update Whether update.
	 */
	public static function validate_service_depth_on_save( $post_id, $post, $update ) {
		if ( wp_is_post_revision( $post_id ) || wp_is_post_autosave( $post_id ) ) {
			return;
		}

		if ( ! self::is_service_depth_allowed( $post ) && function_exists( 'wp_die' ) ) {
			wp_die( esc_html__( 'Service depth above 2 is not allowed by FP-0002 V9-06C.', 'shpigovsky-core' ) );
		}
	}

	/**
	 * Pure max-depth helper.
	 *
	 * @param object $post Service-like post object.
	 * @return bool
	 */
	public static function is_service_depth_allowed( $post ) {
		$depth     = 1;
		$parent_id = isset( $post->post_parent ) ? (int) $post->post_parent : 0;

		while ( $parent_id > 0 && $depth <= 3 ) {
			$parent = get_post( $parent_id );

			if ( ! $parent ) {
				break;
			}

			$depth++;
			$parent_id = (int) $parent->post_parent;
		}

		return $depth <= 3;
	}

	/**
	 * Allow optional programme repeater rows with title-only or fully empty subfields.
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Repeater rows.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_optional_programme_items( $valid, $value, $field, $input ) {
		return true;
	}

	/**
	 * Allow empty optional structured repeaters (signs / stages).
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Repeater rows.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_optional_structured_repeater( $valid, $value, $field, $input ) {
		return true;
	}

	/**
	 * Validate URL fields.
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Value.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_url_field( $valid, $value, $field, $input ) {
		if ( true !== $valid || '' === $value || null === $value ) {
			return $valid;
		}

		return filter_var( $value, FILTER_VALIDATE_URL ) ? true : __( 'Введите корректный URL.', 'shpigovsky-core' );
	}

	/**
	 * Validate email fields.
	 *
	 * @param true|string         $valid Current validity.
	 * @param mixed               $value Value.
	 * @param array<string,mixed> $field Field definition.
	 * @param string              $input Input name.
	 * @return true|string
	 */
	public static function validate_email_field( $valid, $value, $field, $input ) {
		if ( true !== $valid || '' === $value || null === $value ) {
			return $valid;
		}

		return filter_var( $value, FILTER_VALIDATE_EMAIL ) ? true : __( 'Введите корректный email.', 'shpigovsky-core' );
	}

	/**
	 * Pure phone boundary sanitizer.
	 *
	 * @param string $phone Phone-like value.
	 * @return string
	 */
	public static function sanitize_phone_boundary( $phone ) {
		return preg_replace( '/[^0-9+()\-\s]/', '', (string) $phone );
	}

	/**
	 * Detect secret-like option field names or values.
	 *
	 * @param string $name Field name.
	 * @param mixed  $value Field value.
	 * @return bool
	 */
	public static function is_secret_like_option( $name, $value ) {
		$haystack = strtolower( $name . ' ' . ( is_scalar( $value ) ? (string) $value : '' ) );
		$patterns = array( 'password', 'passwd', 'secret', 'token', 'api_key', 'apikey', 'license', 'smtp' );

		foreach ( $patterns as $pattern ) {
			if ( false !== strpos( $haystack, $pattern ) ) {
				return true;
			}
		}

		return false;
	}

	/**
	 * Validate legal blocker state for production delivery gates.
	 *
	 * @param string $status Legal status.
	 * @param bool   $production_blocker Production blocker flag.
	 * @return bool
	 */
	public static function legal_state_allows_production( $status, $production_blocker ) {
		return 'production_ready' === $status && ! $production_blocker;
	}
}
