<?php
/**
 * Shpigovsky theme bootstrap — V9-06B skeleton.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'SHPIGOVSKY_THEME_VERSION', '0.2.0-skeleton' );
define( 'SHPIGOVSKY_THEME_DIR', get_template_directory() );
define( 'SHPIGOVSKY_THEME_URI', get_template_directory_uri() );
define( 'SHPIGOVSKY_THEME_SKELETON', true );

require_once SHPIGOVSKY_THEME_DIR . '/inc/setup.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/assets.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/template-tags.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/service-template-loader.php';
