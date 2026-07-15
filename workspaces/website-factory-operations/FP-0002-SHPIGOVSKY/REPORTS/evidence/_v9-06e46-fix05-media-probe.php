<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results(
	"SELECT p.ID, p.post_title, pm.meta_value AS file
	 FROM {$wpdb->posts} p
	 INNER JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key = '_wp_attached_file'
	 WHERE p.post_type = 'attachment'
	   AND (
	     pm.meta_value LIKE '%corridor%'
	     OR pm.meta_value LIKE '%interior%'
	     OR pm.meta_value LIKE '%rehab%'
	     OR pm.meta_value LIKE '%картин%'
	     OR p.post_title LIKE '%коридор%'
	     OR p.post_title LIKE '%интерьер%'
	     OR p.post_title LIKE '%коридор%'
	   )
	 ORDER BY p.ID DESC
	 LIMIT 50",
	ARRAY_A
);

$html = file_get_contents(
	'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351/frontend/zavisimosti-before.html'
);
preg_match_all( '/<(?:img)[^>]+class="[^"]*(?:corridor-image|staff-image|clinic-landscape)[^"]*"[^>]+src="([^"]+)"/i', $html, $m1 );
preg_match_all( '/src="([^"]*(?:corridor|staff-group|clinic-landscape)[^"]*)"/i', $html, $m2 );

$out = array(
	'media' => $rows,
	'class_srcs' => $m1[1] ?? array(),
	'name_srcs'  => array_values( array_unique( $m2[1] ?? array() ) ),
);
file_put_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/_v9-06e46-fix05-media-probe.json',
	wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT )
);
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
