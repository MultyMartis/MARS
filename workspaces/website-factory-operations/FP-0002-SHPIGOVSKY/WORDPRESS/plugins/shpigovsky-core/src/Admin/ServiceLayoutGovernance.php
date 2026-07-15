<?php
/**
 * Service layout governance — depth-based selector (V9-06E45-FIX03 / E51 / E51-FIX01 / E51-FIX02).
 *
 * First-level (depth 1): selector Раздел / Услуга / Заглушка.
 * Nested (depth 2+): selector Услуга / Заглушка (manual choice must persist).
 * Technical fields remain in meta; hidden from normal admin UI; synced from role.
 * FIX02: never rewrite prepared ACF input name — bare name breaks wp-admin POST.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service layout governance (depth UI / sync / warnings / child-services notice).
 */
final class ServiceLayoutGovernance implements ModuleInterface {

	/**
	 * Known alcohol content page ID (local FP-0002) — preserves V9 alcohol static copy.
	 * Not a layout name; gated by page identity only.
	 */
	public const ALCOHOL_SPECIAL_POST_ID = 74;

	/**
	 * Known alcohol content page slug.
	 */
	public const ALCOHOL_SPECIAL_SLUG = 'lechenie-alkogolnoy-zavisimosti';

	/**
	 * Active technical value for the general service stack.
	 */
	public const LAYOUT_SERVICE_GENERAL = 'service_general';

	/**
	 * Legacy technical value — alias of service_general.
	 */
	public const LAYOUT_ALCOHOL_SPECIAL_LEGACY = 'alcohol_special';

	/**
	 * Known root section post IDs.
	 *
	 * @var int[]
	 */
	public const ROOT_SECTION_IDS = array( 73, 77, 84 );

	/**
	 * In-flight editor role during acf/update_value (role not yet in meta).
	 *
	 * @var string|null
	 */
	private static $inflight_editor_role = null;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.service-layout-governance';
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
		add_action( 'acf/save_post', array( __CLASS__, 'sync_layout_from_role_on_save' ), 20 );
		// V9-06E51-FIX01: sync technical layout immediately when the visible role is written
		// (covers update_field / REST paths that do not always hit a full acf_save_post form).
		add_filter( 'acf/update_value/name=service_editor_role', array( __CLASS__, 'sync_layout_when_role_updated' ), 20, 3 );
		// Visible role must win if a stale/hidden technical layout value is posted afterwards.
		add_filter( 'acf/update_value/name=service_layout_variant', array( __CLASS__, 'guard_layout_value_against_role' ), 20, 3 );
		add_filter( 'acf/prepare_field/name=service_editor_role', array( __CLASS__, 'prepare_editor_role_field' ), 20 );
		add_filter( 'acf/prepare_field/name=service_layout_advanced_heading', array( __CLASS__, 'hide_technical_ui_field' ), 20 );
		add_filter( 'acf/prepare_field/name=service_layout_override_enabled', array( __CLASS__, 'hide_technical_ui_field' ), 20 );
		add_filter( 'acf/prepare_field/name=service_layout_variant', array( __CLASS__, 'prepare_technical_layout_field' ), 20 );
		add_action( 'acf/render_field/name=service_editor_role', array( __CLASS__, 'render_editor_role_help' ), 20 );
		add_action( 'acf/render_field/name=service_child_services_enabled', array( __CLASS__, 'render_child_services_notice' ), 20 );
		add_action( 'admin_notices', array( __CLASS__, 'render_role_warnings' ) );
		add_filter( 'manage_' . Service::POST_TYPE . '_posts_columns', array( __CLASS__, 'filter_service_columns' ), 20 );
		add_action( 'manage_' . Service::POST_TYPE . '_posts_custom_column', array( __CLASS__, 'render_service_column' ), 20, 2 );
	}

	/**
	 * Depth relative to service hierarchy root (parent chain length + 1 for the post itself).
	 * Depth 1 = top-level service (post_parent = 0). Depth 2+ = nested under another service.
	 *
	 * @param int $post_id Post ID.
	 * @return int Depth >= 1, or 0 if invalid.
	 */
	public static function get_service_depth( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 ) {
			return 0;
		}

		$depth   = 1;
		$parent  = (int) get_post_field( 'post_parent', $post_id );
		$guard   = 0;
		$seen    = array( $post_id => true );

		while ( $parent > 0 && $guard < 20 ) {
			if ( isset( $seen[ $parent ] ) ) {
				break;
			}
			$seen[ $parent ] = true;

			$parent_type = get_post_type( $parent );
			if ( Service::POST_TYPE !== $parent_type ) {
				break;
			}

			++$depth;
			$parent = (int) get_post_field( 'post_parent', $parent );
			++$guard;
		}

		return $depth;
	}

	/**
	 * Whether the service is first-level (direct top of service CPT hierarchy).
	 *
	 * @param int $post_id Post ID.
	 * @return bool
	 */
	public static function is_first_level_service( $post_id ) {
		return 1 === self::get_service_depth( $post_id );
	}

	/**
	 * Whether the service is nested (depth 2+).
	 *
	 * @param int $post_id Post ID.
	 * @return bool
	 */
	public static function is_nested_service( $post_id ) {
		return self::get_service_depth( $post_id ) >= 2;
	}

	/**
	 * Resolve current admin context post ID for ACF prepare/render.
	 *
	 * @return int
	 */
	private static function get_admin_service_post_id() {
		$post_id = 0;

		if ( isset( $_GET['post'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			$post_id = (int) $_GET['post']; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		}

		if ( $post_id <= 0 && function_exists( 'acf_get_form_data' ) ) {
			$form_post = acf_get_form_data( 'post_id' );
			if ( is_numeric( $form_post ) ) {
				$post_id = (int) $form_post;
			}
		}

		if ( $post_id <= 0 ) {
			$post_id = (int) get_the_ID();
		}

		return $post_id;
	}

	/**
	 * Map editor role → recommended technical layout.
	 *
	 * @param string $role Editor role.
	 * @return string Empty if unknown.
	 */
	public static function map_role_to_layout( $role ) {
		$map = array(
			'section'     => 'subdivision',
			'service'     => self::LAYOUT_SERVICE_GENERAL,
			'placeholder' => 'placeholder',
		);

		return isset( $map[ $role ] ) ? $map[ $role ] : '';
	}

	/**
	 * Normalize legacy technical layout aliases to current values.
	 *
	 * @param string $layout Technical layout.
	 * @return string
	 */
	public static function normalize_layout_value( $layout ) {
		$layout = is_string( $layout ) ? $layout : '';
		if ( self::LAYOUT_ALCOHOL_SPECIAL_LEGACY === $layout ) {
			return self::LAYOUT_SERVICE_GENERAL;
		}

		return $layout;
	}

	/**
	 * Infer editor role from existing technical layout / nesting / known roots.
	 *
	 * @param string $layout Technical layout.
	 * @param int    $children_count Children count.
	 * @param int    $post_id Post ID.
	 * @return string
	 */
	public static function infer_role_from_layout( $layout, $children_count = 0, $post_id = 0 ) {
		$layout   = is_string( $layout ) ? $layout : '';
		$post_id  = (int) $post_id;
		$children = (int) $children_count;

		// Nested: preserve explicit stub technical layout as placeholder role.
		if ( self::is_nested_service( $post_id ) ) {
			return ( 'placeholder' === $layout ) ? 'placeholder' : 'service';
		}

		if ( in_array( $post_id, self::ROOT_SECTION_IDS, true ) || 'subdivision' === $layout ) {
			return 'section';
		}

		if ( 'placeholder' === $layout ) {
			return 'placeholder';
		}

		// Legacy general service metas — treat as service.
		if ( in_array( $layout, array( 'standard', 'extended', 'service_general', 'alcohol_special', '' ), true ) ) {
			return 'service';
		}

		if ( $children > 0 && 0 === (int) get_post_field( 'post_parent', $post_id ) ) {
			return 'section';
		}

		return 'service';
	}

	/**
	 * Read visible editor role from in-flight update, request POST, or stored meta.
	 *
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function get_effective_editor_role( $post_id ) {
		$post_id = (int) $post_id;

		if ( is_string( self::$inflight_editor_role ) && '' !== self::$inflight_editor_role ) {
			return self::$inflight_editor_role;
		}

		$posted = self::get_posted_acf_value( 'field_fp02_service_editor_role' );
		if ( is_string( $posted ) && '' !== $posted ) {
			return $posted;
		}

		if ( function_exists( 'get_field' ) ) {
			$role = get_field( 'service_editor_role', $post_id );
			if ( is_string( $role ) && '' !== $role ) {
				return $role;
			}
		}

		$meta = get_post_meta( $post_id, 'service_editor_role', true );
		return is_string( $meta ) ? $meta : '';
	}

	/**
	 * Read a posted ACF field value by field key.
	 *
	 * @param string $field_key ACF field key.
	 * @return string|null
	 */
	public static function get_posted_acf_value( $field_key ) {
		if ( empty( $_POST['acf'] ) || ! is_array( $_POST['acf'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
			return null;
		}

		$acf = wp_unslash( $_POST['acf'] ); // phpcs:ignore WordPress.Security.NonceVerification.Missing,WordPress.Security.ValidatedSanitizedInput.InputNotSanitized
		if ( ! isset( $acf[ $field_key ] ) ) {
			return null;
		}

		$value = $acf[ $field_key ];
		if ( is_string( $value ) ) {
			return sanitize_text_field( $value );
		}

		return null;
	}

	/**
	 * Apply role → technical layout sync writes (shared by save_post / update_value).
	 *
	 * @param int    $post_id Post ID.
	 * @param string $role Editor role.
	 * @return void
	 */
	public static function apply_role_layout_sync( $post_id, $role ) {
		$post_id = (int) $post_id;
		$role    = is_string( $role ) ? $role : '';

		if ( $post_id <= 0 || ! function_exists( 'update_field' ) ) {
			return;
		}

		// Nested pages: Услуга or Заглушка only (manual selection must persist either way).
		if ( self::is_nested_service( $post_id ) ) {
			if ( 'placeholder' === $role ) {
				update_field( 'field_fp02_service_editor_role', 'placeholder', $post_id );
				update_field( 'field_fp02_service_layout_variant', 'placeholder', $post_id );
				update_field( 'field_fp02_service_layout_override_enabled', 0, $post_id );
				return;
			}

			// Explicit service, empty, or any other non-placeholder role → Услуга stack.
			// Empty role defaults to service for nested pages (depth model), but never
			// re-forces placeholder once the editor chose Услуга.
			update_field( 'field_fp02_service_editor_role', 'service', $post_id );
			update_field( 'field_fp02_service_layout_variant', self::LAYOUT_SERVICE_GENERAL, $post_id );
			update_field( 'field_fp02_service_layout_override_enabled', 0, $post_id );
			return;
		}

		if ( '' === $role ) {
			if ( in_array( $post_id, self::ROOT_SECTION_IDS, true ) ) {
				$role = 'section';
				update_field( 'field_fp02_service_editor_role', 'section', $post_id );
			} else {
				return;
			}
		}

		$current = function_exists( 'get_field' ) ? get_field( 'service_layout_variant', $post_id ) : '';
		$current = is_string( $current ) ? $current : '';

		if ( self::LAYOUT_ALCOHOL_SPECIAL_LEGACY === $current ) {
			update_field( 'field_fp02_service_layout_variant', self::LAYOUT_SERVICE_GENERAL, $post_id );
			$current = self::LAYOUT_SERVICE_GENERAL;
		}

		update_field( 'field_fp02_service_layout_override_enabled', 0, $post_id );

		$next = self::compute_synced_layout( $role, false, $current, $post_id );
		if ( '' === $next || $next === $current ) {
			return;
		}

		update_field( 'field_fp02_service_layout_variant', $next, $post_id );
	}

	/**
	 * When visible role is updated, sync technical layout in the same write path.
	 *
	 * @param mixed                $value   Role value.
	 * @param int|string           $post_id Post ID.
	 * @param array<string,mixed>  $field   ACF field.
	 * @return mixed
	 */
	public static function sync_layout_when_role_updated( $value, $post_id, $field ) {
		unset( $field );
		$post_id = (int) $post_id;
		if ( $post_id <= 0 || Service::POST_TYPE !== get_post_type( $post_id ) ) {
			return $value;
		}

		$role = is_string( $value ) ? $value : '';
		if ( '' === $role ) {
			return $value;
		}

		$layout = self::map_role_to_layout( $role );
		if ( '' === $layout || ! function_exists( 'update_field' ) ) {
			return $value;
		}

		// Expose in-flight role so nested layout update_value guard sees the new choice.
		self::$inflight_editor_role = $role;
		try {
			update_field( 'field_fp02_service_layout_variant', $layout, $post_id );
			update_field( 'field_fp02_service_layout_override_enabled', 0, $post_id );
		} finally {
			self::$inflight_editor_role = null;
		}

		return $value;
	}

	/**
	 * Prevent hidden/stale technical layout from overriding the visible role selection.
	 *
	 * @param mixed                $value   Layout value being saved.
	 * @param int|string           $post_id Post ID.
	 * @param array<string,mixed>  $field   ACF field.
	 * @return mixed
	 */
	public static function guard_layout_value_against_role( $value, $post_id, $field ) {
		unset( $field );
		$post_id = (int) $post_id;
		if ( $post_id <= 0 || Service::POST_TYPE !== get_post_type( $post_id ) ) {
			return $value;
		}

		$role = self::get_effective_editor_role( $post_id );
		if ( '' === $role ) {
			return $value;
		}

		$expected = self::map_role_to_layout( $role );
		if ( '' === $expected ) {
			return $value;
		}

		$value_norm = self::normalize_layout_value( is_string( $value ) ? $value : '' );
		if ( $value_norm !== $expected ) {
			return $expected;
		}

		return $value;
	}

	/**
	 * Whether post is the known alcohol special page (static V9 alcohol copy).
	 *
	 * @param int $post_id Post ID.
	 * @return bool
	 */
	public static function is_known_alcohol_page( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id === self::ALCOHOL_SPECIAL_POST_ID ) {
			return true;
		}

		$slug = (string) get_post_field( 'post_name', $post_id );
		return self::ALCOHOL_SPECIAL_SLUG === $slug;
	}

	/**
	 * Count child services.
	 *
	 * @param int $post_id Post ID.
	 * @return int
	 */
	public static function count_children( $post_id ) {
		$q = new \WP_Query(
			array(
				'post_type'      => Service::POST_TYPE,
				'post_parent'    => (int) $post_id,
				'post_status'    => array( 'publish', 'draft', 'pending', 'private' ),
				'posts_per_page' => 1,
				'fields'         => 'ids',
				'no_found_rows'  => false,
			)
		);

		return (int) $q->found_posts;
	}

	/**
	 * Count published child services.
	 *
	 * @param int $post_id Post ID.
	 * @return int
	 */
	public static function count_published_children( $post_id ) {
		$q = new \WP_Query(
			array(
				'post_type'      => Service::POST_TYPE,
				'post_parent'    => (int) $post_id,
				'post_status'    => 'publish',
				'posts_per_page' => 1,
				'fields'         => 'ids',
				'no_found_rows'  => false,
			)
		);

		return (int) $q->found_posts;
	}

	/**
	 * Compute recommended technical layout from role (override ignored in FIX03 UI).
	 *
	 * @param string $role Editor role.
	 * @param bool   $override_enabled Override flag (ignored when false path used).
	 * @param string $current_layout Current technical layout.
	 * @param int    $post_id Post ID.
	 * @return string
	 */
	public static function compute_synced_layout( $role, $override_enabled, $current_layout, $post_id ) {
		$current_layout = self::normalize_layout_value( is_string( $current_layout ) ? $current_layout : '' );
		$post_id        = (int) $post_id;
		$role           = is_string( $role ) ? $role : '';

		unset( $override_enabled );

		// Nested: Услуга or Заглушка (no Раздел).
		if ( self::is_nested_service( $post_id ) ) {
			if ( 'placeholder' === $role ) {
				return 'placeholder';
			}

			return self::LAYOUT_SERVICE_GENERAL;
		}

		$recommended = self::map_role_to_layout( $role );
		if ( '' === $recommended ) {
			return $current_layout;
		}

		return $recommended;
	}

	/**
	 * Hide technical override / advanced heading from normal admin UI.
	 *
	 * @param array<string,mixed>|false $field ACF field.
	 * @return array<string,mixed>|false
	 */
	public static function hide_technical_ui_field( $field ) {
		if ( ! is_admin() || ! is_array( $field ) ) {
			return $field;
		}

		return false;
	}

	/**
	 * Keep technical layout in the form (hidden) and aligned to the visible role.
	 *
	 * Returning false previously omitted the field from POST; a stale meta value then
	 * survived until sync. E51-FIX01 keeps the field, hides it, and pre-aligns value.
	 *
	 * @param array<string,mixed>|false $field ACF field.
	 * @return array<string,mixed>|false
	 */
	public static function prepare_technical_layout_field( $field ) {
		if ( ! is_admin() || ! is_array( $field ) ) {
			return $field;
		}

		$post_id = self::get_admin_service_post_id();
		if ( $post_id > 0 && Service::POST_TYPE === get_post_type( $post_id ) ) {
			$role = self::get_effective_editor_role( $post_id );
			$next = self::map_role_to_layout( $role );
			if ( '' !== $next ) {
				$field['value'] = $next;
			}
		}

		$wrapper         = isset( $field['wrapper'] ) && is_array( $field['wrapper'] ) ? $field['wrapper'] : array();
		$class           = isset( $wrapper['class'] ) ? (string) $wrapper['class'] : '';
		$wrapper['class'] = trim( $class . ' acf-hidden fp02-service-layout-technical-hidden' );
		$field['wrapper'] = $wrapper;
		$field['required'] = 0;

		return $field;
	}

	/**
	 * Prepare editor layout selector: first-level selector, nested Услуга/Заглушка.
	 *
	 * @param array<string,mixed>|false $field ACF field.
	 * @return array<string,mixed>|false
	 */
	public static function prepare_editor_role_field( $field ) {
		if ( ! is_admin() || ! is_array( $field ) ) {
			return $field;
		}

		$post_id = self::get_admin_service_post_id();
		if ( $post_id <= 0 || Service::POST_TYPE !== get_post_type( $post_id ) ) {
			$field['label'] = __( 'Макет страницы услуги', 'shpigovsky-core' );
			return $field;
		}

		$field['label'] = __( 'Макет страницы услуги', 'shpigovsky-core' );
		$field['type']  = 'button_group';
		// V9-06E51-FIX02: do NOT reset name/key here. acf_prepare_field() already
		// rewrites name to acf[field_…] BEFORE this filter; overwriting with the bare
		// meta name made radios post as $_POST['service_editor_role'] (outside ACF),
		// so wp-admin save never persisted Заглушка↔Услуга for nested services.

		// Nested (depth 2+): Услуга | Заглушка — no Раздел.
		if ( self::is_nested_service( $post_id ) ) {
			$field['choices']      = array(
				'service'     => __( 'Услуга', 'shpigovsky-core' ),
				'placeholder' => __( 'Заглушка', 'shpigovsky-core' ),
			);
			$field['instructions'] = __( 'Временный режим страницы. На фронте выводятся только шапка, навигация, H1 и подвал. Контент в полях не удаляется и может быть включён обратно сменой макета.', 'shpigovsky-core' );
			$field['wrapper']      = array(
				'width' => '',
				'class' => 'fp02-acf-section-title fp02-service-layout-selector fp02-service-layout-nested',
				'id'    => '',
			);
			$field['required']     = 0;
			$field['allow_null']   = 0;
			$field['layout']       = 'horizontal';
			$field['return_format'] = 'value';

			return $field;
		}

		// First-level: Раздел | Услуга | Заглушка.
		$field['choices'] = array(
			'section'     => __( 'Раздел', 'shpigovsky-core' ),
			'service'     => __( 'Услуга', 'shpigovsky-core' ),
			'placeholder' => __( 'Заглушка', 'shpigovsky-core' ),
		);
		$field['instructions'] = __( 'Выберите «Раздел», «Услуга» или временную «Заглушку». Контент в полях не удаляется при смене макета.', 'shpigovsky-core' );
		$field['wrapper']      = array(
			'width' => '',
			'class' => 'fp02-acf-section-title fp02-service-layout-selector',
			'id'    => '',
		);

		return $field;
	}

	/**
	 * After ACF save: depth-aware sync of role + technical layout.
	 *
	 * Prefers posted visible role so manual Услуга ↔ Заглушка switches persist.
	 *
	 * @param int|string $post_id Post ID.
	 */
	public static function sync_layout_from_role_on_save( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 || Service::POST_TYPE !== get_post_type( $post_id ) ) {
			return;
		}

		if ( ! function_exists( 'get_field' ) || ! function_exists( 'update_field' ) ) {
			return;
		}

		$role = self::get_effective_editor_role( $post_id );
		self::apply_role_layout_sync( $post_id, $role );
	}

	/**
	 * Help under layout selector (first-level only; nested uses message field).
	 *
	 * @param array<string,mixed> $field ACF field.
	 */
	public static function render_editor_role_help( $field ) {
		if ( ! is_admin() || empty( $field['name'] ) || 'service_editor_role' !== $field['name'] ) {
			return;
		}

		if ( isset( $field['type'] ) && 'message' === $field['type'] ) {
			return;
		}

		$post_id = self::get_admin_service_post_id();
		$nested  = $post_id > 0 && self::is_nested_service( $post_id );

		echo '<div class="fp02-service-layout-help notice notice-info inline fp02-service-layout-selector-help">';
		if ( $nested ) {
			echo '<p><strong class="fp02-acf-notice-danger">' . esc_html__( 'Вложенная услуга: выберите «Услуга» или временную «Заглушку».', 'shpigovsky-core' ) . '</strong></p>';
		} else {
			echo '<p><strong class="fp02-acf-notice-danger">' . esc_html__( 'Макет уже выбран по структуре страницы. Обычно его не нужно менять.', 'shpigovsky-core' ) . '</strong></p>';
			echo '<p>' . esc_html__( 'Если меняете макет — сначала проверьте, какую роль эта страница должна играть в структуре сайта.', 'shpigovsky-core' ) . '</p>';
		}
		echo '<ul class="fp02-service-layout-help__list">';
		if ( ! $nested ) {
			echo '<li><strong>' . esc_html__( 'Раздел', 'shpigovsky-core' ) . '</strong> — ' . esc_html__( 'первый уровень: страница группирует дочерние услуги (шаблон раздела).', 'shpigovsky-core' ) . '</li>';
		}
		echo '<li><strong>' . esc_html__( 'Услуга', 'shpigovsky-core' ) . '</strong> — ' . esc_html__( 'полный шаблон услуги с блоками контента.', 'shpigovsky-core' ) . '</li>';
		echo '<li><strong>' . esc_html__( 'Заглушка', 'shpigovsky-core' ) . '</strong> — ' . esc_html__( 'временный режим: только шапка, навигация, H1 и подвал. Контент в полях сохраняется.', 'shpigovsky-core' ) . '</li>';
		echo '</ul>';
		echo '</div>';
	}

	/**
	 * Admin notice under child-services toggle.
	 *
	 * @param array<string,mixed> $field ACF field.
	 */
	public static function render_child_services_notice( $field ) {
		if ( ! is_admin() || empty( $field['name'] ) || 'service_child_services_enabled' !== $field['name'] ) {
			return;
		}

		$post_id = self::get_admin_service_post_id();
		if ( $post_id <= 0 ) {
			return;
		}

		$published = self::count_published_children( $post_id );
		$list_url  = admin_url( 'edit.php?post_type=' . Service::POST_TYPE );

		echo '<div class="fp02-service-layout-help notice notice-info inline">';
		echo '<p><strong>' . esc_html__( 'Блок дочерних услуг', 'shpigovsky-core' ) . '</strong></p>';
		if ( $published > 0 ) {
			echo '<p>' . esc_html(
				sprintf(
					/* translators: %d: published children count */
					__( 'На фронтенде перед FAQ будет показана плитка из %d опубликованных дочерних услуг.', 'shpigovsky-core' ),
					$published
				)
			) . '</p>';
			echo '<p><strong class="fp02-acf-notice-danger">' . esc_html__( 'Источник:', 'shpigovsky-core' ) . '</strong> ';
			echo esc_html__( 'прямые дочерние страницы этого CPT «Услуга» (иерархия WordPress).', 'shpigovsky-core' ) . '</p>';
		} else {
			echo '<p>' . esc_html__( 'Сейчас дочерних опубликованных услуг нет — блок на сайте не отобразится, пока не появятся дочерние страницы.', 'shpigovsky-core' ) . '</p>';
			echo '<p><strong class="fp02-acf-notice-danger">' . esc_html__( 'Источник:', 'shpigovsky-core' ) . '</strong> ';
			echo esc_html__( 'автоматически из дочерних страниц услуги.', 'shpigovsky-core' ) . '</p>';
		}
		echo '<p><a href="' . esc_url( $list_url ) . '">' . esc_html__( 'Открыть список услуг', 'shpigovsky-core' ) . '</a></p>';
		echo '</div>';
	}

	/**
	 * Non-blocking role / nesting / conflict warnings.
	 */
	public static function render_role_warnings() {
		$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

		if ( ! $screen || Service::POST_TYPE !== $screen->post_type || 'post' !== $screen->base ) {
			return;
		}

		if ( ! current_user_can( 'edit_posts' ) || ! function_exists( 'get_field' ) ) {
			return;
		}

		$post_id = isset( $_GET['post'] ) ? (int) $_GET['post'] : 0; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		if ( $post_id <= 0 ) {
			return;
		}

		// Nested pages: still warn when placeholder is active (informational only).
		$role     = get_field( 'service_editor_role', $post_id );
		$role     = is_string( $role ) ? $role : '';
		$layout   = get_field( 'service_layout_variant', $post_id );
		$layout   = is_string( $layout ) ? $layout : '';
		$children = self::count_children( $post_id );

		$messages = array();

		if ( self::is_nested_service( $post_id ) ) {
			if ( 'placeholder' === $role || 'placeholder' === $layout ) {
				$messages[] = __( 'Включён временный режим «Заглушка»: на сайте только шапка, навигация, H1 и подвал. Контент в полях сохранён.', 'shpigovsky-core' );
			}
			if ( empty( $messages ) ) {
				return;
			}
			echo '<div class="notice notice-info fp02-service-layout-mismatch"><p><strong>' . esc_html__( 'Макет страницы услуги', 'shpigovsky-core' ) . '</strong></p>';
			foreach ( $messages as $msg ) {
				echo '<p>' . esc_html( $msg ) . '</p>';
			}
			echo '</div>';
			return;
		}

		if ( 'section' === $role && 0 === $children ) {
			$messages[] = __( 'Макет «Раздел», но дочерних услуг нет. Проверьте выбор или добавьте дочерние страницы. Значение не изменено автоматически.', 'shpigovsky-core' );
		}

		if ( 'service' === $role && $children > 0 ) {
			$messages[] = __( 'Макет «Услуга» с дочерними услугами — это нормально. Блок плиток дочерних услуг может отображаться перед FAQ.', 'shpigovsky-core' );
		}

		if ( 'placeholder' === $role ) {
			$messages[] = __( 'Включён временный режим «Заглушка»: на сайте только шапка, навигация, H1 и подвал. Контент в полях сохранён и может быть включён обратно сменой макета.', 'shpigovsky-core' );
		}

		if ( '' !== $role ) {
			$expected = self::map_role_to_layout( $role );
			if ( '' !== $expected && '' !== $layout && $expected !== $layout ) {
				$messages[] = sprintf(
					/* translators: 1: editor role, 2: technical layout */
					__( 'Выбранный макет (%1$s) ещё не совпадает с техническим значением (%2$s). Сохраните страницу, чтобы синхронизировать.', 'shpigovsky-core' ),
					$role,
					$layout
				);
			}
		}

		if ( empty( $messages ) ) {
			return;
		}

		echo '<div class="notice notice-warning fp02-service-layout-mismatch"><p><strong>' . esc_html__( 'Проверьте макет страницы услуги', 'shpigovsky-core' ) . '</strong></p>';
		foreach ( $messages as $msg ) {
			echo '<p>' . esc_html( $msg ) . '</p>';
		}
		echo '</div>';
	}

	/**
	 * Add editor role column.
	 *
	 * @param array<string,string> $columns Columns.
	 * @return array<string,string>
	 */
	public static function filter_service_columns( $columns ) {
		$columns['fp02_service_role'] = __( 'Макет', 'shpigovsky-core' );
		return $columns;
	}

	/**
	 * Render editor role column.
	 *
	 * @param string $column Column key.
	 * @param int    $post_id Post ID.
	 */
	public static function render_service_column( $column, $post_id ) {
		if ( 'fp02_service_role' !== $column ) {
			return;
		}

		$role   = function_exists( 'get_field' ) ? get_field( 'service_editor_role', $post_id ) : '';
		$labels = array(
			'section'     => __( 'Раздел', 'shpigovsky-core' ),
			'service'     => __( 'Услуга', 'shpigovsky-core' ),
			'placeholder' => __( 'Заглушка', 'shpigovsky-core' ),
		);

		if ( is_string( $role ) && isset( $labels[ $role ] ) ) {
			echo esc_html( $labels[ $role ] );
			return;
		}

		if ( self::is_nested_service( $post_id ) ) {
			echo esc_html__( 'Услуга', 'shpigovsky-core' );
			return;
		}

		echo '—';
	}
}
