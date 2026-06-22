<?php
/**
 * FWS Synthetic theme bootstrap.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'FWS_SYNTHETIC_VERSION', '1.0.0' );
define( 'FWS_SYNTHETIC_DIR', get_template_directory() );
define( 'FWS_SYNTHETIC_URI', get_template_directory_uri() );

require_once FWS_SYNTHETIC_DIR . '/inc/setup.php';
require_once FWS_SYNTHETIC_DIR . '/inc/assets.php';
require_once FWS_SYNTHETIC_DIR . '/inc/template-tags.php';
require_once FWS_SYNTHETIC_DIR . '/inc/options.php';
