<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$group_key = 'group_fp02_block_header';
$group = acf_get_field_group( $group_key );
$group['fields'] = acf_get_fields( $group_key );
$path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/' . $group_key . '.json';
file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
echo "written\n";
acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
echo "imported\n";
