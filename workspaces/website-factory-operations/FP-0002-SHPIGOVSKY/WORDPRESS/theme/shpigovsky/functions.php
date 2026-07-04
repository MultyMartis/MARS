<?php
/**
 * Shpigovsky theme bootstrap — V9-06D7-A global shell.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'SHPIGOVSKY_THEME_VERSION', '0.3.0-d7a-shell' );
define( 'SHPIGOVSKY_THEME_DIR', get_template_directory() );
define( 'SHPIGOVSKY_THEME_URI', get_template_directory_uri() );
define( 'SHPIGOVSKY_THEME_SKELETON', false );

require_once SHPIGOVSKY_THEME_DIR . '/inc/setup.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/site-chrome.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/navigation.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/assets.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/template-tags.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/service-template-loader.php';
