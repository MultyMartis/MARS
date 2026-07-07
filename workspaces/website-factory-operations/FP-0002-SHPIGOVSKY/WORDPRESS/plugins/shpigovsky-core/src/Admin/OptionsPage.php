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
				'redirect'    => true,
				'capability'  => 'manage_options',
			)
		);

		foreach ( self::get_reusable_block_subpages() as $subpage ) {
			acf_add_options_sub_page( $subpage );
		}
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
				'menu_title' => __( 'Отзывы', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-reviews',
			),
			array(
				'menu_title' => __( 'CTA-блоки', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-cta-bands',
			),
			array(
				'menu_title' => __( 'Комфорт', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-comfort',
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
			array(
				'menu_title' => __( 'Герои / fallback-изображения', 'shpigovsky-core' ),
				'menu_slug'  => 'fp02-block-hero-fallbacks',
			),
		);

		$subpages = array();

		foreach ( $blocks as $block ) {
			$subpages[] = array(
				'page_title'  => $block['menu_title'],
				'menu_title'  => $block['menu_title'],
				'menu_slug'   => $block['menu_slug'],
				'parent_slug' => self::BLOCKS_PARENT_SLUG,
				'capability'  => 'manage_options',
				'autoload'    => false,
			);
		}

		return $subpages;
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

		if ( ! in_array( $page, self::get_skeleton_block_slugs(), true ) ) {
			return;
		}

		echo '<div class="notice notice-info"><p>';
		echo esc_html__( 'Скелет подстраницы повторяемого блока (V9-06E17). Поля и миграция данных будут добавлены в следующих волнах.', 'shpigovsky-core' );
		if ( 'fp02-block-reviews' === $page ) {
			echo ' ';
			echo esc_html__( 'Активное редактирование отзывов остаётся в меню «Отзывы» до явной миграции.', 'shpigovsky-core' );
		}
		echo '</p></div>';
	}
}
