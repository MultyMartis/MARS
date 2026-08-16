<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression';

$alcohol = get_permalink( 74 );
$section = get_permalink( 73 );
echo "alcohol=$alcohol\nsection=$section\n";

$home = file_get_contents( 'http://shpigovsky.test/' );
echo 'full_link_count=' . substr_count( $home, 'data-review-slider-full-link' ) . "\n";
echo 'uid_attr_count=' . substr_count( $home, 'data-review-uid' ) . "\n";
preg_match_all( '/href="([^"]*#review-[^"]+)"/', $home, $m );
echo 'hash_links=' . count( $m[1] ) . "\n";
print_r( array_slice( $m[1], 0, 8 ) );

$otz = file_get_contents( 'http://shpigovsky.test/otzyvy/' );
preg_match_all( '/id="(review-[^"]+)"/', $otz, $ids );
echo 'page1_ids=' . implode( ',', $ids[1] ) . "\n";
$digit = 0;
foreach ( $ids[1] as $id ) {
	if ( preg_match( '/^review-\d+$/', $id ) ) {
		$digit++;
	}
}
echo "digit_only_on_page1=$digit\n";

// Alcohol service page check.
$svc = file_get_contents( $alcohol );
echo 'alcohol_http_bytes=' . strlen( $svc ) . "\n";
echo 'alcohol_has_cta=' . ( false !== strpos( $svc, 'program-cta-band' ) ? '1' : '0' ) . "\n";
echo 'alcohol_php_warn=' . ( preg_match( '/(Fatal error|Warning:.*\.php|Notice:.*on line)/i', $svc ) ? '1' : '0' ) . "\n";

// Specialist.
$specs = get_posts( array( 'post_type' => array( 'specialist', 'page' ), 's' => '', 'posts_per_page' => 5, 'post_parent' => 0 ) );
// Better: find child of specyalisty page.
$parent = get_page_by_path( 'specyalisty' );
$child = null;
if ( $parent ) {
	$children = get_pages( array( 'child_of' => $parent->ID, 'number' => 1 ) );
	if ( ! empty( $children ) ) {
		$child = $children[0];
	}
}
echo 'specialist_child=' . ( $child ? get_permalink( $child ) : 'NONE' ) . "\n";

file_put_contents(
	$ev . '/slider-destination-matrix.csv',
	"href\n" . implode( "\n", $m[1] ) . "\n"
);
file_put_contents(
	$ev . '/review-anchor-page1.txt',
	implode( "\n", $ids[1] )
);

// Lead regex recheck with u + s
$oc = file_get_contents( 'http://shpigovsky.test/o-centre/' );
$ok = preg_match( '/<p class="infrastructure-narrative__lead block-whith-red-line">(?!<span)[\s\S]*?<\/p>/u', $oc );
$has_span_inside = preg_match( '/<p class="infrastructure-narrative__lead block-whith-red-line"><span>/u', $oc );
echo "lead_ok=$ok has_span_inside=$has_span_inside\n";
