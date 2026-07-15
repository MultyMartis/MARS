<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$fields = array(
	'section_team_image',
	'section_corridor_image',
	'section_clinic_landscape_image',
	'section_nature_text_blocks',
	'section_stages_items',
	'section_dependencies_heading',
	'section_approach_heading',
	'section_faq_heading',
);
$out = array();
foreach ( array( 73, 77, 84 ) as $pid ) {
	$out[ $pid ] = array( 'title' => get_the_title( $pid ) );
	foreach ( $fields as $f ) {
		$v = get_field( $f, $pid );
		if ( is_array( $v ) ) {
			if ( isset( $v['ID'] ) ) {
				$out[ $pid ][ $f ] = 'image:' . (int) $v['ID'];
			} else {
				$out[ $pid ][ $f ] = 'rows:' . count( $v );
			}
		} else {
			$out[ $pid ][ $f ] = $v;
		}
	}
}
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
