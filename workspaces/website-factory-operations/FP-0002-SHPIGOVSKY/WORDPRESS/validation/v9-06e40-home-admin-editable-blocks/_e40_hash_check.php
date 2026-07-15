<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$body = wp_remote_retrieve_body(
	wp_remote_get(
		home_url( '/' ),
		array(
			'timeout'   => 30,
			'sslverify' => false,
		)
	)
);
preg_match_all( '/class="home-gallery__slide[^"]*"/', $body, $m );
echo 'GALLERY_SLIDE_EXACT=' . count( $m[0] ) . "\n";
echo 'MODE=' . shpigovsky_get_home_gallery_display_mode() . ' N=' . shpigovsky_get_home_gallery_random_count() . ' slides_fn=' . count( shpigovsky_get_home_gallery_service_slides() ) . "\n";

$src = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$map = array(
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php'         => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'plugins/shpigovsky-core/src/Fields/RepeaterValidation.php'  => 'wp-content/plugins/shpigovsky-core/src/Fields/RepeaterValidation.php',
	'theme/shpigovsky/inc/home-fallbacks.php'                    => 'wp-content/themes/shpigovsky/inc/home-fallbacks.php',
	'theme/shpigovsky/inc/home-helpers.php'                      => 'wp-content/themes/shpigovsky/inc/home-helpers.php',
	'theme/shpigovsky/template-parts/home/recovery-intro.php'    => 'wp-content/themes/shpigovsky/template-parts/home/recovery-intro.php',
	'theme/shpigovsky/template-parts/home/treatment-prevention.php' => 'wp-content/themes/shpigovsky/template-parts/home/treatment-prevention.php',
	'theme/shpigovsky/template-parts/home/why-us.php'            => 'wp-content/themes/shpigovsky/template-parts/home/why-us.php',
	'theme/shpigovsky/template-parts/home/staff-photo.php'       => 'wp-content/themes/shpigovsky/template-parts/home/staff-photo.php',
	'theme/shpigovsky/template-parts/home/clinic-landscape.php'  => 'wp-content/themes/shpigovsky/template-parts/home/clinic-landscape.php',
	'theme/shpigovsky/template-parts/home/recovery-life.php'     => 'wp-content/themes/shpigovsky/template-parts/home/recovery-life.php',
	'theme/shpigovsky/template-parts/home/genotyping.php'        => 'wp-content/themes/shpigovsky/template-parts/home/genotyping.php',
	'theme/shpigovsky/template-parts/home/videos.php'            => 'wp-content/themes/shpigovsky/template-parts/home/videos.php',
	'acf-json/group_fp02_page_home.json'                         => 'wp-content/acf-json/group_fp02_page_home.json',
);
foreach ( $map as $a => $b ) {
	$ha = hash_file( 'sha256', $src . '/' . $a );
	$hb = hash_file( 'sha256', $rt . '/' . $b );
	echo ( $ha === $hb ? 'MATCH' : 'DIFF' ) . "\t{$a}\n";
}
