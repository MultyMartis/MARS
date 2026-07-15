<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$target = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_page_institutional.json';

if ( ! function_exists( 'acf_get_local_field_groups' ) ) {
	fwrite( STDERR, "acf_get_local_field_groups missing\n" );
	exit( 1 );
}

foreach ( acf_get_local_field_groups() as $group ) {
	if ( ( $group['key'] ?? '' ) === 'group_fp02_page_institutional' ) {
		$fields = acf_get_fields( $group );
		$group['fields'] = is_array( $fields ) ? $fields : array();
		file_put_contents(
			$target,
			wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . "\n"
		);
		echo "exported\n";
		exit( 0 );
	}
}

fwrite( STDERR, "group not found\n" );
exit( 1 );
