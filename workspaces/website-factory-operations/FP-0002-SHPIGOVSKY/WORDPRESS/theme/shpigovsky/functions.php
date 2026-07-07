<?php
/**
 * Shpigovsky theme bootstrap — V9-06D7-A global shell.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'SHPIGOVSKY_THEME_VERSION', '0.7.0-e8-v9-content-layout-authority' );
define( 'SHPIGOVSKY_THEME_DIR', get_template_directory() );
define( 'SHPIGOVSKY_THEME_URI', get_template_directory_uri() );
define( 'SHPIGOVSKY_THEME_SKELETON', false );

require_once SHPIGOVSKY_THEME_DIR . '/inc/setup.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/site-chrome.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/navigation.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/assets.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/template-tags.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/home-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/hero-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/home-fallbacks.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/home-vendors.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/alcohol-direct-v9-vendors.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/service-subdivision-vendors.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/v9-static-content.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/services-hub-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/service-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/service-template-loader.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/contacts-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/reviews-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/reusable-blocks-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/institutional-helpers.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/admin-options.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/admin-editor.php';
