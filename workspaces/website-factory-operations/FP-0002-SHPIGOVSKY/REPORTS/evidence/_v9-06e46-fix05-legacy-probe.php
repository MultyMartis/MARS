<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$keys = array(
	'section_nature_neurobiology_heading',
	'section_nature_neurobiology_text',
	'section_nature_genotyping_heading',
	'section_nature_genotyping_text',
	'section_nature_genotyping_link_label',
	'section_nature_genotyping_link_url',
	'section_nature_genotyping_after_text',
	'section_stages_items',
	'_section_stages_items',
);
$out = array();
foreach ( array( 73, 77, 84 ) as $pid ) {
	$out[ $pid ] = array();
	foreach ( $keys as $k ) {
		$out[ $pid ][ $k ] = get_post_meta( $pid, $k, true );
	}
	if ( function_exists( 'shpigovsky_get_service_repeater' ) ) {
		$out[ $pid ]['structured_stages'] = shpigovsky_get_service_repeater( $pid, 'stages' );
	}
	if ( function_exists( 'shpigovsky_get_section_nature_text_blocks' ) ) {
		$out[ $pid ]['resolved_nature_blocks'] = shpigovsky_get_section_nature_text_blocks( $pid );
	}
	if ( function_exists( 'shpigovsky_get_section_stages_items' ) ) {
		$out[ $pid ]['resolved_stages'] = shpigovsky_get_section_stages_items( $pid );
	}
}
file_put_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/_v9-06e46-fix05-legacy-probe.json',
	wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT )
);
echo "ok\n";
