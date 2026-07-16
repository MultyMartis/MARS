<?php
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e55-site-settings-admin-ux';
$routes = array( '/', '/uslugi/', '/uslugi/zavisimosti/', '/o-centre/', '/kontakty/', '/privacy-policy/' );
$hashes = array();
foreach ( $routes as $route ) {
	$ch = curl_init( 'http://shpigovsky.test' . $route );
	curl_setopt_array( $ch, array( CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 45 ) );
	$body = curl_exec( $ch );
	curl_close( $ch );
	$hashes[ $route ] = hash( 'sha256', is_string( $body ) ? $body : '' );
}
file_put_contents( $evidence . '/frontend-hashes-before.json', json_encode( $hashes, JSON_PRETTY_PRINT ) );
echo json_encode( $hashes, JSON_PRETTY_PRINT ) . "\n";
