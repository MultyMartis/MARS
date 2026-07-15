<?php
/**
 * V9-06E41 — repair duplicate Home ACF groups: keep newest publish with new fields.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';

global $wpdb;
$rows = $wpdb->get_results(
	"SELECT ID, post_status, post_title FROM {$wpdb->posts}
	 WHERE post_type = 'acf-field-group'
	   AND (post_name LIKE 'group_fp02_page_home%' OR post_title LIKE '%Главная%')
	 ORDER BY ID ASC"
);
echo "GROUPS=" . count( $rows ) . "\n";
foreach ( $rows as $r ) {
	$children = (int) $wpdb->get_var(
		$wpdb->prepare(
			"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_parent = %d AND post_type = 'acf-field'",
			(int) $r->ID
		)
	);
	$key = get_post_meta( (int) $r->ID, 'key', true );
	echo "ID={$r->ID} status={$r->post_status} children={$children} key={$key}\n";
}

// Prefer publish group with most children and new toggle field.
$keep_id = 0;
$best    = -1;
foreach ( $rows as $r ) {
	if ( 'publish' !== $r->post_status ) {
		continue;
	}
	$id       = (int) $r->ID;
	$children = (int) $wpdb->get_var(
		$wpdb->prepare(
			"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_parent = %d AND post_type = 'acf-field'",
			$id
		)
	);
	$has_toggle = (int) $wpdb->get_var(
		$wpdb->prepare(
			"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_parent = %d AND post_type = 'acf-field' AND post_excerpt = %s",
			$id,
			'home_founder_quote_visible'
		)
	);
	$score = $children + ( $has_toggle ? 1000 : 0 );
	if ( $score > $best ) {
		$best    = $score;
		$keep_id = $id;
	}
}
echo "KEEP_ID={$keep_id}\n";

foreach ( $rows as $r ) {
	$id = (int) $r->ID;
	if ( $id === $keep_id ) {
		continue;
	}
	if ( 'trash' === $r->post_status ) {
		continue;
	}
	wp_trash_post( $id );
	echo "TRASHED={$id}\n";
}

wp_update_post(
	array(
		'ID'          => $keep_id,
		'post_status' => 'publish',
		'post_name'   => 'group_fp02_page_home',
	)
);
update_post_meta( $keep_id, 'key', 'group_fp02_page_home' );
update_post_meta( $keep_id, 'active', 1 );

if ( function_exists( 'acf_get_store' ) ) {
	foreach ( array( 'fields', 'field-groups' ) as $store_name ) {
		$store = acf_get_store( $store_name );
		if ( $store ) {
			$store->reset();
		}
	}
}

$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'ACF_FIELD_COUNT=' . count( (array) $fields ) . "\n";
$names  = array();
foreach ( (array) $fields as $f ) {
	$names[] = (string) ( $f['name'] ?? '' );
}
foreach ( array( 'home_hero_autoplay_enabled', 'home_founder_quote_visible', 'home_gallery_visible', 'home_rehab_program_visible', 'home_articles_visible' ) as $n ) {
	echo 'HAS_' . $n . '=' . ( in_array( $n, $names, true ) ? '1' : '0' ) . "\n";
}

// Check stage_label subfield exists under stages repeater.
$stage_label_posts = $wpdb->get_var(
	$wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='acf-field' AND post_excerpt=%s AND post_parent IN (
			SELECT ID FROM {$wpdb->posts} WHERE post_parent=%d AND post_excerpt='home_recovery_life_stages'
		)",
		'stage_label',
		$keep_id
	)
);
echo "STAGE_LABEL_FIELD={$stage_label_posts}\n";

// Rewrite JSON from local PHP group.
$all   = \Shpigovsky\Core\Fields\FieldGroups::get_field_groups();
$group = null;
foreach ( $all as $g ) {
	if ( ( $g['key'] ?? '' ) === 'group_fp02_page_home' ) {
		$group = $g;
		break;
	}
}
if ( $group ) {
	unset( $group['ID'] );
	$json = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
	file_put_contents( $root . '/acf-json/group_fp02_page_home.json', $json );
	copy( $root . '/acf-json/group_fp02_page_home.json', 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_page_home.json' );
	$php_count = isset( $group['fields'] ) ? count( $group['fields'] ) : 0;
	echo "PHP_TOP_FIELDS={$php_count}\nJSON_WRITTEN=1\n";
}

$children = (int) $wpdb->get_var(
	$wpdb->prepare(
		"SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_parent = %d AND post_type = 'acf-field'",
		$keep_id
	)
);
echo "KEEP_CHILDREN={$children}\nDONE\n";
