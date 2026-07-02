<?php
/**
 * Global footer shell — modal and scroll hooks included.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_template_part( 'template-parts/layout/footer' );
get_template_part( 'template-parts/layout/global-consultation-modal' );
get_template_part( 'template-parts/components/scroll-to-top' );
get_template_part( 'template-parts/global/document-close' );
