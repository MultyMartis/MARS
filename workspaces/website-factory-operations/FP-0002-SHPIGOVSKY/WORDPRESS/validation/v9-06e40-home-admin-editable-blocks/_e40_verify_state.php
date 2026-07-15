<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

// List all acf-field-group posts mentioning page_home or Главная
$posts = get_posts(
	array(
		'post_type'      => 'acf-field-group',
		'post_status'    => array( 'publish', 'acf-disabled', 'trash', 'draft' ),
		'posts_per_page' => 50,
	)
);

echo "ALL_ACF_GROUPS=" . count( $posts ) . "\n";
foreach ( $posts as $p ) {
	$content = $p->post_content;
	$key     = '';
	if ( is_serialized( $content ) ) {
		$data = @unserialize( $content );
		$key  = is_array( $data ) ? ( $data['key'] ?? '' ) : '';
	}
	$meta_key = get_post_meta( $p->ID, 'key', true );
	$has_home = ( false !== strpos( $p->post_title, 'Главная' ) || false !== strpos( $p->post_title, 'Home' ) || 'group_fp02_page_home' === $key || 'group_fp02_page_home' === $meta_key );
	if ( ! $has_home && false === strpos( (string) $content, 'group_fp02_page_home' ) ) {
		continue;
	}
	$children = get_posts(
		array(
			'post_type'      => 'acf-field',
			'post_parent'    => $p->ID,
			'posts_per_page' => -1,
			'post_status'    => 'any',
		)
	);
	echo "ID={$p->ID} status={$p->post_status} title={$p->post_title} key={$key}|{$meta_key} children=" . count( $children ) . "\n";
}

// Local fields from PHP registration
$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'LOCAL_OR_DB_FIELDS=' . count( (array) $fields ) . "\n";

$fg = acf_get_field_group( 'group_fp02_page_home' );
echo 'GROUP_LOCAL=' . ( ! empty( $fg['local'] ) ? $fg['local'] : 'n/a' ) . ' ID=' . ( $fg['ID'] ?? 0 ) . "\n";

// Seeded meta spot-check
$home = (int) get_option( 'page_on_front' );
$keys = array(
	'home_recovery_intro_benefits',
	'home_gallery_display_mode',
	'home_gallery_random_count',
	'home_why_us_heading',
	'home_staff_photo_image',
	'home_clinic_landscape_image',
	'home_videos_items',
	'home_genotyping_heading',
	'home_treatment_prevention_heading',
	'home_recovery_life_stages',
);
foreach ( $keys as $k ) {
	$v = get_field( $k, $home );
	$preview = is_array( $v ) ? ( 'array:' . count( $v ) ) : ( is_scalar( $v ) ? mb_substr( (string) $v, 0, 60 ) : gettype( $v ) );
	echo "META {$k} => {$preview}\n";
}

// Video URL check
$videos = shpigovsky_get_home_videos_items();
foreach ( $videos as $i => $v ) {
	echo "VIDEO{$i} url=" . ( $v['video_url'] ?? '' ) . " poster=" . ( $v['poster_url'] ?? '' ) . "\n";
}

// Staff/land URLs
$staff = shpigovsky_home_image_or_asset( 'home_staff_photo_image', 'img/content/pre-reviews/shpigovsky-staff-group.webp', '', 1139, 443 );
$land  = shpigovsky_home_image_or_asset( 'home_clinic_landscape_image', 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', '', 1139, 584 );
echo 'STAFF_URL=' . $staff['url'] . "\n";
echo 'LAND_URL=' . $land['url'] . "\n";
echo ( false !== strpos( $staff['url'], '/uploads/' ) ? 'STAFF_FROM_ML=1' : 'STAFF_FROM_THEME=1' ) . "\n";
echo ( false !== strpos( $land['url'], '/uploads/' ) ? 'LAND_FROM_ML=1' : 'LAND_FROM_THEME=1' ) . "\n";
