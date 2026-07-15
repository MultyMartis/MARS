<?php
/**
 * Template part: services-hub/service-groups.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_services_hub_list_enabled( 'services_hub_catalog_visible' ) ) {
	return;
}

$groups = shpigovsky_get_services_hub_groups();

if ( empty( $groups ) ) {
	get_template_part( 'template-parts/services-hub/empty-state' );
	return;
}

foreach ( $groups as $group ) {
	set_query_var( 'services_hub_group', $group );
	get_template_part( 'template-parts/services-hub/service-group' );
}
