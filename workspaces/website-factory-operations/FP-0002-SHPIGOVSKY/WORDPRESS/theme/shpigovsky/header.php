<?php
/**
 * Global header shell — orchestrates layout partials only.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_template_part( 'template-parts/global/document-open' );
get_template_part( 'template-parts/layout/head' );
get_template_part( 'template-parts/layout/body-start' );
get_template_part( 'template-parts/layout/header' );
get_template_part( 'template-parts/layout/floating-header' );
