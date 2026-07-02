<?php
/**
 * Service CPT module — registration deferred to V9-06C.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\ContentTypes;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service custom post type boundary.
 */
final class Service implements ModuleInterface {

	/**
	 * Post type slug.
	 */
	public const POST_TYPE = 'service';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'content-types.service';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'init', array( __CLASS__, 'register_post_type' ) );
	}

	/**
	 * Register the service post type.
	 *
	 * V9-06B: method exists for contract completeness; not hooked while skeleton mode is active.
	 */
	public static function register_post_type() {
		register_post_type(
			self::POST_TYPE,
			array(
				'labels'       => array(
					'name'          => __( 'Услуги', 'shpigovsky-core' ),
					'singular_name' => __( 'Услуга', 'shpigovsky-core' ),
				),
				'public'       => true,
				'show_in_rest' => true,
				'has_archive'  => false,
				'rewrite'      => false,
				'supports'     => array( 'title', 'editor', 'thumbnail', 'revisions' ),
				'menu_icon'    => 'dashicons-heart',
			)
		);
	}
}
