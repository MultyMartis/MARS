<?php
/**
 * Template part: service/subnav.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$trail   = shpigovsky_get_service_breadcrumb_trail( $post_id );
$items   = shpigovsky_get_service_subnav_items( $variant );

if ( empty( $items ) ) {
	return;
}

set_query_var( 'shpigovsky_breadcrumb_trail', $trail );
set_query_var( 'shpigovsky_subnav_items', $items );

get_template_part( 'template-parts/components/internal-page-nav' );
