<?php
/**
 * ACF options page registration — FP-0002 V9-06E17 Site Settings IA skeleton.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Admin options pages boundary.
 */
final class OptionsPage implements ModuleInterface {

	/**
	 * Parent menu slug — stable since V9-06C.
	 */
	public const PARENT_SLUG = 'fp02-site-settings';

	/**
	 * General settings subpage slug.
	 */
	public const GENERAL_SLUG = 'fp02-site-settings-general';

	/**
	 * Reusable blocks parent subpage slug.
	 */
	public const BLOCKS_PARENT_SLUG = 'fp02-site-settings-blocks';

	/**
	 * Canonical ACF storage post_id for comfort / gallery / requirements.
	 * Frontend get_field(..., 'fp02-block-comfort') MUST keep using this.
	 */
	public const COMFORT_STORAGE_POST_ID = 'fp02-block-comfort';

	/**
	 * Legacy comfort menu slug — hidden; redirects to intro.
	 */
	public const COMFORT_LEGACY_SLUG = 'fp02-block-comfort';

	/**
	 * Split comfort admin menu slugs (location only; storage unchanged).
	 */
	public const COMFORT_INTRO_SLUG         = 'fp02-block-comfort-intro';
	public const COMFORT_GALLERY_SLUG       = 'fp02-block-comfort-gallery';
	public const COMFORT_REQUIREMENTS_SLUG  = 'fp02-block-comfort-requirements';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.options-page';
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
		add_action( 'acf/init', array( __CLASS__, 'register_options_pages' ) );
		add_action( 'acf/input/admin_head', array( __CLASS__, 'render_skeleton_admin_notice' ) );
		add_action( 'admin_menu', array( __CLASS__, 'hide_legacy_comfort_menu' ), 999 );
		add_action( 'admin_init', array( __CLASS__, 'redirect_legacy_comfort_page' ) );
	}

	/**
	 * Register ACF options pages and reusable-block skeleton subpages.
	 */
	public static function register_options_pages() {
		if ( ! function_exists( 'acf_add_options_page' ) ) {
			return;
		}

		acf_add_options_page(
			array(
				'page_title'      => __( 'Настройки сайта', 'shpigovsky-core' ),
				'menu_title'      => __( 'Настройки сайта', 'shpigovsky-core' ),
				'menu_slug'       => self::PARENT_SLUG,
				'capability'      => 'manage_options',
				'position'        => 59,
				'redirect'        => true,
				'icon_url'        => 'dashicons-admin-generic',
				'updated_message' => __( 'Настройки сайта обновлены.', 'shpigovsky-core' ),
			)
		);

		if ( ! function_exists( 'acf_add_options_sub_page' ) ) {
			return;
		}

		acf_add_options_sub_page(
			array(
				'page_title'  => __( 'Общие настройки', 'shpigovsky-core' ),
				'menu_title'  => __( 'Общие настройки', 'shpigovsky-core' ),
				'menu_slug'   => self::GENERAL_SLUG,
				'parent_slug' => self::PARENT_SLUG,
				'post_id'     => 'option',
				'capability'  => 'manage_options',
				'autoload'    => true,
			)
		);

		acf_add_options_sub_page(
			array(
				'page_title'  => __( 'Повторяемые блоки', 'shpigovsky-core' ),
				'menu_title'  => __( 'Повторяемые блоки', 'shpigovsky-core' ),
				'menu_slug'   => self::BLOCKS_PARENT_SLUG,
				'parent_slug' => self::PARENT_SLUG,
				'redirect'    => false,
				'capability'  => 'manage_options',
			)
		);

		foreach ( self::get_reusable_block_subpages() as $subpage ) {
			acf_add_options_sub_page( $subpage );
		}

		// Legacy slug kept registered for bookmarks / old links; menu item hidden.
		acf_add_options_sub_page(
			array(
				'page_title'  => __( 'Комфорт / преимущества (архив)', 'shpigovsky-core' ),
				'menu_title'  => __( 'Комфорт / преимущества', 'shpigovsky-core' ),
				'menu_slug'   => self::COMFORT_LEGACY_SLUG,
				'parent_slug' => self::PARENT_SLUG,
				'post_id'     => self::COMFORT_STORAGE_POST_ID,
				'capability'  => 'manage_options',
				'autoload'    => false,
			)
		);
	}

	/**
	 * Remove legacy comfort submenu after ACF registers it.
	 */
	public static function hide_legacy_comfort_menu() {
		remove_submenu_page( self::PARENT_SLUG, self::COMFORT_LEGACY_SLUG );
	}

	/**
	 * Redirect legacy comfort page to intro split page.
	 */
	public static function redirect_legacy_comfort_page() {
		if ( ! is_admin() ) {
			return;
		}

		// phpcs:ignore WordPress.Security.NonceVerification.Recommended -- read-only redirect gate.
		$page = isset( $_GET['page'] ) ? sanitize_key( wp_unslash( $_GET['page'] ) ) : '';

		if ( self::COMFORT_LEGACY_SLUG !== $page ) {
			return;
		}

		wp_safe_redirect( admin_url( 'admin.php?page=' . self::COMFORT_INTRO_SLUG ) );
		exit;
	}

	/**
	 * Skeleton reusable-block subpages from E16 inventory (no fields in E17).
	 *
	 * @return array<int, array<string, mixed>>
	 */
	public static function get_reusable_block_subpages() {
		$blocks = array(
			array(
				'menu_title' => __( 'Шапка', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-header',
			),
			array(
				'menu_title' => __( 'Подвал', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-footer',
			),
			array(
				'menu_title' => __( 'Финальная форма', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-final-form',
			),
			array(
				'menu_title' => __( 'Модальное окно', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-consultation-modal',
			),
			array(
				'menu_title' => __( 'Специалисты', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-specialists',
			),
			array(
				'menu_title' => __( 'CTA-блоки', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-cta-bands',
			),
			array(
				'menu_title' => __( 'Комфорт — вводный блок', 'shpigovsky-core' ),
				'menu_slug'  => self::COMFORT_INTRO_SLUG,
				'post_id'    => self::COMFORT_STORAGE_POST_ID,
			),
			array(
				'menu_title' => __( 'Комфорт — галерея', 'shpigovsky-core' ),
				'menu_slug'  => self::COMFORT_GALLERY_SLUG,
				'post_id'    => self::COMFORT_STORAGE_POST_ID,
			),
			array(
				'menu_title' => __( 'Комфорт — требования', 'shpigovsky-core' ),
				'menu_slug'  => self::COMFORT_REQUIREMENTS_SLUG,
				'post_id'    => self::COMFORT_STORAGE_POST_ID,
			),
			array(
				'menu_title' => __( 'Требования и преимущества', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-advantages',
			),
			array(
				'menu_title' => __( 'Цитата основателя', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-founder-quote',
			),
			array(
				'menu_title' => __( 'Фоновые секции', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-backgrounds',
			),
		);

		$subpages = array();

		foreach ( $blocks as $block ) {
			$is_fielded = in_array( $block['menu_slug'], self::get_fielded_block_slugs(), true );

			$subpage = array(
				'page_title'  => $block['menu_title'],
				'menu_title'  => $block['menu_title'],
				'menu_slug'   => $block['menu_slug'],
				'parent_slug' => $is_fielded ? self::PARENT_SLUG : self::BLOCKS_PARENT_SLUG,
				'capability'  => 'manage_options',
				'autoload'    => false,
			);

			if ( $is_fielded ) {
				$subpage['post_id'] = isset( $block['post_id'] ) ? $block['post_id'] : $block['menu_slug'];
			}

			$subpages[] = $subpage;
		}

		return $subpages;
	}

	/**
	 * Comfort split admin slugs (menu/location only).
	 *
	 * @return array<int, string>
	 */
	public static function get_comfort_split_slugs() {
		return array(
			self::COMFORT_INTRO_SLUG,
			self::COMFORT_GALLERY_SLUG,
			self::COMFORT_REQUIREMENTS_SLUG,
		);
	}

	/**
	 * Batch 1 reusable blocks with active ACF fields (E18).
	 *
	 * @return array<int, string>
	 */
	public static function get_batch1_fielded_block_slugs() {
		return array(
			'fp02-block-final-form',
			'fp02-block-specialists',
			'fp02-block-cta-bands',
			'fp02-block-founder-quote',
		);
	}

	/**
	 * Batch 2 reusable blocks with active ACF fields (V9-06E21 / E56 comfort split).
	 *
	 * Storage for comfort remains `fp02-block-comfort`; menu uses split slugs.
	 *
	 * @return array<int, string>
	 */
	public static function get_batch2_fielded_block_slugs() {
		return array_merge(
			array(
				'fp02-block-header',
				'fp02-block-footer',
			),
			self::get_comfort_split_slugs()
		);
	}

	/**
	 * All reusable blocks with active ACF fields (Batch 1 + Batch 2).
	 *
	 * @return array<int, string>
	 */
	public static function get_fielded_block_slugs() {
		return array_merge(
			self::get_batch1_fielded_block_slugs(),
			self::get_batch2_fielded_block_slugs()
		);
	}

	/**
	 * Resolve reusable-block menu title by slug for admin notices.
	 *
	 * @param string $slug Menu slug.
	 * @return string
	 */
	public static function get_block_menu_title_by_slug( $slug ) {
		foreach ( self::get_reusable_block_subpages() as $subpage ) {
			if ( ( $subpage['menu_slug'] ?? '' ) === $slug ) {
				return (string) ( $subpage['menu_title'] ?? '' );
			}
		}

		return '';
	}

	/**
	 * Return skeleton block slugs for validation and deferred field migration.
	 *
	 * @return array<int, string>
	 */
	public static function get_skeleton_block_slugs() {
		return array_map(
			static function ( $subpage ) {
				return $subpage['menu_slug'];
			},
			self::get_reusable_block_subpages()
		);
	}

	/**
	 * Show a minimal admin notice on skeleton reusable-block pages.
	 */
	public static function render_skeleton_admin_notice() {
		if ( ! is_admin() ) {
			return;
		}

		// phpcs:ignore WordPress.Security.NonceVerification.Recommended -- read-only admin screen detection.
		$page = isset( $_GET['page'] ) ? sanitize_key( wp_unslash( $_GET['page'] ) ) : '';

		if ( self::BLOCKS_PARENT_SLUG === $page ) {
			echo '<div class="notice notice-info"><p>';
			echo esc_html__( 'Контейнер повторяемых блоков. Редактируемые блоки — в подстраницах меню «Настройки сайта».', 'shpigovsky-core' );
			echo '</p><ul style="list-style:disc;margin-left:1.5em;">';
			foreach ( self::get_fielded_block_slugs() as $slug ) {
				$title = self::get_block_menu_title_by_slug( $slug );
				if ( $title ) {
					echo '<li><a href="' . esc_url( admin_url( 'admin.php?page=' . $slug ) ) . '">' . esc_html( $title ) . '</a></li>';
				}
			}
			echo '</ul></div>';
			return;
		}

		if ( in_array( $page, self::get_comfort_split_slugs(), true ) ) {
			echo '<div class="notice notice-info"><p>';
			echo esc_html__( 'Разделы «Комфорт» хранят данные в общем пространстве fp02-block-comfort (фронтенд без изменений). Старая страница «Комфорт / преимущества» скрыта и перенаправляет сюда.', 'shpigovsky-core' );
			echo '</p></div>';
			return;
		}

		if ( ! in_array( $page, self::get_skeleton_block_slugs(), true ) ) {
			return;
		}

		if ( in_array( $page, self::get_fielded_block_slugs(), true ) ) {
			return;
		}

		echo '<div class="notice notice-info"><p>';
		echo esc_html__( 'Скелет подстраницы повторяемого блока (V9-06E17). Поля и миграция данных будут добавлены в следующих волнах.', 'shpigovsky-core' );
		echo '</p></div>';
	}
}
