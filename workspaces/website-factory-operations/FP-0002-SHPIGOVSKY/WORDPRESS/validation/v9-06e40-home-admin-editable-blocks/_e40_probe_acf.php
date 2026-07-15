<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$g = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_page_home' ) : null;
echo 'group_ID=' . ( $g['ID'] ?? 'none' ) . "\n";
echo 'group_title=' . ( $g['title'] ?? 'none' ) . "\n";
$f = function_exists( 'acf_get_fields' ) ? acf_get_fields( 'group_fp02_page_home' ) : array();
echo 'fields=' . count( (array) $f ) . "\n";
foreach ( (array) $f as $i => $x ) {
	echo $i . "\t" . ( $x['name'] ?? '' ) . "\t" . ( $x['type'] ?? '' ) . "\t" . ( $x['label'] ?? '' ) . "\n";
}

// Fix inventory if empty earlier.
$backup = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e40-home-admin-editable-blocks-before-20260714-010957/exports';
$fLines = array( "menu_order\tname\tlabel\ttype\tkey" );
foreach ( (array) $f as $i => $x ) {
	$fLines[] = $i . "\t" . ( $x['name'] ?? '' ) . "\t" . ( $x['label'] ?? '' ) . "\t" . ( $x['type'] ?? '' ) . "\t" . ( $x['key'] ?? '' );
}
file_put_contents( $backup . '/home-admin-inventory-before.txt', implode( "\n", $fLines ) );
echo "inventory_rewritten\n";
