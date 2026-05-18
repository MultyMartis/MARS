<?php
/**
 * Main WPilot plugin bootstrap class.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Plugin {
	/**
	 * Singleton instance.
	 *
	 * @var WPilot_Plugin|null
	 */
	private static $instance = null;

	/**
	 * REST controller instance.
	 *
	 * @var WPilot_REST_Controller
	 */
	private $rest_controller;

	/**
	 * Admin page instance.
	 *
	 * @var WPilot_Admin_Page
	 */
	private $admin_page;

	/**
	 * Get plugin singleton.
	 *
	 * @return WPilot_Plugin
	 */
	public static function instance() {
		if ( null === self::$instance ) {
			self::$instance = new self();
		}

		return self::$instance;
	}

	private function __construct() {
		$this->rest_controller = new WPilot_REST_Controller();
		$this->admin_page      = new WPilot_Admin_Page();
	}

	/**
	 * Attach WordPress hooks.
	 *
	 * @return void
	 */
	public function init() {
		add_action( 'admin_menu', array( $this->admin_page, 'register_menu' ) );
		add_action( 'rest_api_init', array( $this->rest_controller, 'register_routes' ) );
	}
}
