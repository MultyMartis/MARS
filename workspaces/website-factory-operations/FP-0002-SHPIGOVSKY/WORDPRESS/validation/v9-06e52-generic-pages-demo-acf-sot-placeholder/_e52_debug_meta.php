<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$id = 1039;
$rows = $wpdb->get_results( $wpdb->prepare(
	"SELECT meta_key, LEFT(meta_value,120) AS v FROM {$wpdb->postmeta} WHERE post_id=%d AND (meta_key LIKE %s OR meta_key LIKE %s) ORDER BY meta_key",
	$id,
	'%generic%',
	'%page_layout%'
), ARRAY_A );
echo "META:\n";
foreach ( (array) $rows as $r ) {
	echo $r['meta_key'] . ' = ' . $r['v'] . "\n";
}
echo "\nget_field body: ";
var_export( get_field( 'generic_page_body', $id ) );
echo "\nget_field lead: ";
var_export( get_field( 'generic_page_lead', $id ) );
echo "\nacf_get_field body: ";
$f = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_generic_page_body' ) : null;
var_export( is_array( $f ) ? $f['name'] : $f );
echo "\n";
$ch = curl_init( get_permalink( $id ) );
curl_setopt_array( $ch, array( CURLOPT_RETURNTRANSFER => 1, CURLOPT_FOLLOWLOCATION => 1, CURLOPT_TIMEOUT => 30 ) );
$b = (string) curl_exec( $ch );
$c = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
curl_close( $ch );
echo "HTTP $c\n";
if ( preg_match( '/data-content-status="([^"]+)"/', $b, $m ) ) {
	echo "status={$m[1]}\n";
}
if ( preg_match( '/data-content-source="([^"]+)"/', $b, $m ) ) {
	echo "source={$m[1]}\n";
}
echo ( false !== strpos( $b, 'Раздел находится в подготовке' ) ? "has_demo_phrase\n" : "no_demo_phrase\n" );
