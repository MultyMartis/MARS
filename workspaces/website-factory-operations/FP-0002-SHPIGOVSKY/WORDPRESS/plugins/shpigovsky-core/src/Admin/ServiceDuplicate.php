<?php
/**
 * Service duplicate admin action — safe draft copy for service entities.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;
use WP_Error;
use WP_Post;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Bounded admin duplication for hierarchical service posts.
 */
final class ServiceDuplicate implements ModuleInterface {

	/**
	 * Nonce action prefix.
	 */
	public const NONCE_ACTION = 'fp02_duplicate_service';

	/**
	 * admin-post.php action slug.
	 */
	public const ADMIN_ACTION = 'fp02_duplicate_service';

	/**
	 * Duplicate wave marker.
	 */
	public const DUPLICATE_WAVE = 'V9-06E25';

	/**
	 * Title suffix for duplicated services.
	 */
	public const TITLE_SUFFIX = ' — копия';

	/**
	 * Query arg used for one-time admin notice after redirect.
	 */
	public const NOTICE_QUERY_ARG = 'fp02_service_duplicated';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.service-duplicate';
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
		add_filter( 'post_row_actions', array( __CLASS__, 'add_row_action' ), 10, 2 );
		add_action( 'admin_post_' . self::ADMIN_ACTION, array( __CLASS__, 'handle_admin_post' ) );
		add_action( 'admin_notices', array( __CLASS__, 'render_duplicate_notice' ) );
	}

	/**
	 * Add duplicate row action for service posts.
	 *
	 * @param array<string,string> $actions Row actions.
	 * @param WP_Post                $post    Current post.
	 * @return array<string,string>
	 */
	public static function add_row_action( $actions, $post ) {
		if ( ! $post instanceof WP_Post || Service::POST_TYPE !== $post->post_type ) {
			return $actions;
		}

		if ( wp_is_post_autosave( $post ) || wp_is_post_revision( $post ) ) {
			return $actions;
		}

		if ( ! current_user_can( 'edit_post', $post->ID ) || ! current_user_can( 'create_posts' ) ) {
			return $actions;
		}

		$url = wp_nonce_url(
			admin_url(
				'admin-post.php?action=' . self::ADMIN_ACTION . '&post_id=' . (int) $post->ID
			),
			self::NONCE_ACTION . '_' . (int) $post->ID
		);

		$actions['fp02_duplicate'] = sprintf(
			'<a href="%s" aria-label="%s">%s</a>',
			esc_url( $url ),
			esc_attr(
				sprintf(
					/* translators: %s: service title */
					__( 'Дублировать услугу «%s»', 'shpigovsky-core' ),
					$post->post_title
				)
			),
			esc_html__( 'Дублировать', 'shpigovsky-core' )
		);

		return $actions;
	}

	/**
	 * Handle admin-post duplicate request.
	 */
	public static function handle_admin_post() {
		if ( ! is_user_logged_in() ) {
			wp_die( esc_html__( 'Требуется авторизация.', 'shpigovsky-core' ), 403 );
		}

		$source_id = isset( $_GET['post_id'] ) ? (int) $_GET['post_id'] : 0;

		if ( ! $source_id ) {
			wp_die( esc_html__( 'Не указан исходный пост.', 'shpigovsky-core' ), 400 );
		}

		check_admin_referer( self::NONCE_ACTION . '_' . $source_id );

		$source = get_post( $source_id );

		if ( ! $source instanceof WP_Post || Service::POST_TYPE !== $source->post_type ) {
			wp_die( esc_html__( 'Дублирование доступно только для услуг.', 'shpigovsky-core' ), 400 );
		}

		if ( wp_is_post_autosave( $source ) || wp_is_post_revision( $source ) ) {
			wp_die( esc_html__( 'Нельзя дублировать автосохранение или ревизию.', 'shpigovsky-core' ), 400 );
		}

		if ( ! current_user_can( 'edit_post', $source_id ) || ! current_user_can( 'create_posts' ) ) {
			wp_die( esc_html__( 'Недостаточно прав для дублирования услуги.', 'shpigovsky-core' ), 403 );
		}

		$result = self::duplicate_service( $source_id, get_current_user_id() );

		if ( is_wp_error( $result ) ) {
			wp_die( esc_html( $result->get_error_message() ), 500 );
		}

		$redirect = add_query_arg(
			array(
				self::NOTICE_QUERY_ARG => 1,
				'post'                 => (int) $result,
				'action'               => 'edit',
			),
			admin_url( 'post.php' )
		);

		wp_safe_redirect( $redirect );
		exit;
	}

	/**
	 * Render success notice on duplicate edit screen.
	 */
	public static function render_duplicate_notice() {
		if ( ! is_admin() || ! current_user_can( 'edit_posts' ) ) {
			return;
		}

		// phpcs:ignore WordPress.Security.NonceVerification.Recommended -- read-only notice flag.
		if ( empty( $_GET[ self::NOTICE_QUERY_ARG ] ) ) {
			return;
		}

		$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

		if ( ! $screen || Service::POST_TYPE !== $screen->post_type || 'post' !== $screen->base ) {
			return;
		}

		printf(
			'<div class="notice notice-success is-dismissible"><p><strong>FP-0002</strong> — %s</p></div>',
			esc_html__( 'Черновик-копия услуги создан. Проверьте поля и опубликуйте вручную при необходимости.', 'shpigovsky-core' )
		);
	}

	/**
	 * Create a draft duplicate of a service post.
	 *
	 * @param int      $source_id Source post ID.
	 * @param int|null $author_id Optional author override; defaults to current user.
	 * @return int|WP_Error New post ID or error.
	 */
	public static function duplicate_service( $source_id, $author_id = null ) {
		$source = get_post( (int) $source_id );

		if ( ! $source instanceof WP_Post || Service::POST_TYPE !== $source->post_type ) {
			return new WP_Error( 'fp02_invalid_source', __( 'Исходная услуга не найдена.', 'shpigovsky-core' ) );
		}

		if ( wp_is_post_autosave( $source ) || wp_is_post_revision( $source ) ) {
			return new WP_Error( 'fp02_invalid_source_type', __( 'Нельзя дублировать автосохранение или ревизию.', 'shpigovsky-core' ) );
		}

		$author_id = null === $author_id ? get_current_user_id() : (int) $author_id;

		if ( $author_id <= 0 ) {
			$author_id = (int) $source->post_author;
		}

		$new_title = self::build_duplicate_title( $source->post_title );
		$new_slug  = self::build_unique_slug( $source );

		$new_post_id = wp_insert_post(
			array(
				'post_type'    => Service::POST_TYPE,
				'post_status'  => 'draft',
				'post_title'   => $new_title,
				'post_name'    => $new_slug,
				'post_parent'  => (int) $source->post_parent,
				'menu_order'   => (int) $source->menu_order,
				'post_author'  => $author_id,
				'post_content' => $source->post_content,
				'post_excerpt' => $source->post_excerpt,
			),
			true
		);

		if ( is_wp_error( $new_post_id ) ) {
			return $new_post_id;
		}

		self::copy_postmeta( (int) $source->ID, (int) $new_post_id );
		self::copy_taxonomies( (int) $source->ID, (int) $new_post_id );

		update_post_meta( (int) $new_post_id, '_fp02_duplicated_from', (int) $source->ID );
		update_post_meta( (int) $new_post_id, '_fp02_duplicated_at', gmdate( 'c' ) );
		update_post_meta( (int) $new_post_id, '_fp02_duplicate_wave', self::DUPLICATE_WAVE );

		/**
		 * Fires after a service duplicate draft is created.
		 *
		 * @param int $new_post_id Duplicate post ID.
		 * @param int $source_id   Source post ID.
		 */
		do_action( 'fp02_service_duplicated', (int) $new_post_id, (int) $source->ID );

		return (int) $new_post_id;
	}

	/**
	 * Build duplicate title with suffix.
	 *
	 * @param string $title Source title.
	 * @return string
	 */
	public static function build_duplicate_title( $title ) {
		$title = trim( (string) $title );

		if ( '' === $title ) {
			return trim( self::TITLE_SUFFIX );
		}

		return $title . self::TITLE_SUFFIX;
	}

	/**
	 * Build a unique slug for the duplicate.
	 *
	 * @param WP_Post $source Source post.
	 * @return string
	 */
	public static function build_unique_slug( WP_Post $source ) {
		$base = sanitize_title( $source->post_name . '-kopiya' );

		if ( '' === $base ) {
			$base = sanitize_title( $source->post_title . '-kopiya' );
		}

		return wp_unique_post_slug(
			$base,
			0,
			'draft',
			Service::POST_TYPE,
			(int) $source->post_parent
		);
	}

	/**
	 * Postmeta keys that must never be copied to duplicates.
	 *
	 * @return array<int,string>
	 */
	public static function get_meta_skip_keys() {
		return array(
			'_edit_lock',
			'_edit_last',
			'_wp_old_slug',
			'_wp_trash_meta_status',
			'_wp_trash_meta_time',
			'_fp02_duplicated_from',
			'_fp02_duplicated_at',
			'_fp02_duplicate_wave',
		);
	}

	/**
	 * Copy postmeta from source to duplicate, preserving ACF reference keys.
	 *
	 * @param int $source_id Source post ID.
	 * @param int $new_id    Duplicate post ID.
	 */
	public static function copy_postmeta( $source_id, $new_id ) {
		$skip = self::get_meta_skip_keys();
		$meta = get_post_meta( (int) $source_id );

		if ( ! is_array( $meta ) ) {
			return;
		}

		foreach ( $meta as $meta_key => $values ) {
			if ( in_array( $meta_key, $skip, true ) ) {
				continue;
			}

			if ( ! is_array( $values ) ) {
				continue;
			}

			foreach ( $values as $value ) {
				add_post_meta( (int) $new_id, $meta_key, $value );
			}
		}
	}

	/**
	 * Copy taxonomy term relationships.
	 *
	 * @param int $source_id Source post ID.
	 * @param int $new_id    Duplicate post ID.
	 */
	public static function copy_taxonomies( $source_id, $new_id ) {
		$taxonomies = get_object_taxonomies( Service::POST_TYPE );

		if ( empty( $taxonomies ) ) {
			return;
		}

		foreach ( $taxonomies as $taxonomy ) {
			$term_ids = wp_get_object_terms( (int) $source_id, $taxonomy, array( 'fields' => 'ids' ) );

			if ( is_wp_error( $term_ids ) || empty( $term_ids ) ) {
				continue;
			}

			wp_set_object_terms( (int) $new_id, array_map( 'intval', $term_ids ), $taxonomy, false );
		}
	}
}
