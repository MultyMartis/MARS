<?php
/**
 * Shpigovsky theme bootstrap — foundation only.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'SHPIGOVSKY_THEME_VERSION', '0.1.0' );
define( 'SHPIGOVSKY_THEME_DIR', get_template_directory() );
define( 'SHPIGOVSKY_THEME_URI', get_template_directory_uri() );

require_once SHPIGOVSKY_THEME_DIR . '/inc/setup.php';
require_once SHPIGOVSKY_THEME_DIR . '/inc/assets.php';
