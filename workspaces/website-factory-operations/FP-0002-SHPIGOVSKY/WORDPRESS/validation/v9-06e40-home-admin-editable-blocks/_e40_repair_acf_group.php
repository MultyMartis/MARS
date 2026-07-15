<?php
/**
 * V9-06E40 — repair Home ACF group: keep one publish group_fp02_page_home with 55 fields.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';

$all = \Shpigovsky\Core\Fields\FieldGroups::get_field_groups();
$group = null;
foreach ( $all as $g ) {
	if ( ( $g['key'] ?? '' ) === 'group_fp02_page_home' ) {
		$group = $g;
		break;
	}
}
if ( ! $group ) {
	fwrite( STDERR, "no group\n" );
	exit( 1 );
}

// Find all DB posts for this key.
global $wpdb;
$rows = $wpdb->get_results(
	"SELECT p.ID, p.post_title, p.post_status, p.post_name
	 FROM {$wpdb->posts} p
	 INNER JOIN {$wpdb->postmeta} m ON m.post_id = p.ID AND m.meta_key = 'key' AND m.meta_value = 'group_fp02_page_home'
	 WHERE p.post_type = 'acf-field-group'
	 ORDER BY p.ID ASC"
);

echo "DB_GROUPS=" . count( $rows ) . "\n";
foreach ( $rows as $r ) {
	echo "  ID={$r->ID} status={$r->post_status} title={$r->post_title}\n";
}

// Prefer keep ID 639 if present, else lowest publish ID, else imported 1153.
$keep_id = 0;
foreach ( $rows as $r ) {
	if ( (int) $r->ID === 639 && 'publish' === $r->post_status ) {
		$keep_id = 639;
		break;
	}
}
if ( ! $keep_id ) {
	foreach ( $rows as $r ) {
		if ( 'publish' === $r->post_status ) {
			$keep_id = (int) $r->ID;
			break;
		}
	}
}
if ( ! $keep_id && ! empty( $rows ) ) {
	$keep_id = (int) $rows[0]->ID;
}

echo "KEEP_ID={$keep_id}\n";

// Trash others.
foreach ( $rows as $r ) {
	$id = (int) $r->ID;
	if ( $id === $keep_id ) {
		continue;
	}
	wp_trash_post( $id );
	echo "TRASHED={$id}\n";
}

// Force import onto keep ID: set group ID then import.
$group['ID'] = $keep_id;
$imported    = acf_import_field_group( $group );
echo 'REIMPORT=' . wp_json_encode( is_array( $imported ) ? array( 'ID' => $imported['ID'] ?? null, 'key' => $imported['key'] ?? null ) : $imported ) . "\n";

// Ensure publish.
wp_update_post(
	array(
		'ID'          => $keep_id,
		'post_status' => 'publish',
	)
);

// Clear ACF caches.
if ( function_exists( 'acf_get_store' ) ) {
	$store = acf_get_store( 'fields' );
	if ( $store ) {
		$store->reset();
	}
	$store2 = acf_get_store( 'field-groups' );
	if ( $store2 ) {
		$store2->reset();
	}
}

$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'FIELD_COUNT=' . count( (array) $fields ) . "\n";
foreach ( (array) $fields as $i => $f ) {
	echo $i . "\t" . ( $f['name'] ?? '' ) . "\t" . ( $f['type'] ?? '' ) . "\t" . ( $f['label'] ?? '' ) . "\n";
}

// Also check by post parent field count.
$child_fields = get_posts(
	array(
		'post_type'      => 'acf-field',
		'post_parent'    => $keep_id,
		'posts_per_page' => -1,
		'post_status'    => array( 'publish', 'acf-disabled' ),
	)
);
echo 'CHILD_FIELD_POSTS=' . count( $child_fields ) . "\n";

// Rewrite JSON from PHP group (without ID).
unset( $group['ID'] );
$json = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
file_put_contents( $root . '/acf-json/group_fp02_page_home.json', $json );
copy( $root . '/acf-json/group_fp02_page_home.json', 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_page_home.json' );

$final_groups = $wpdb->get_results(
	"SELECT p.ID, p.post_status FROM {$wpdb->posts} p
	 INNER JOIN {$wpdb->postmeta} m ON m.post_id = p.ID AND m.meta_key = 'key' AND m.meta_value = 'group_fp02_page_home'
	 WHERE p.post_type = 'acf-field-group' AND p.post_status = 'publish'"
);
echo 'PUBLISH_COUNT=' . count( $final_groups ) . "\n";
echo "REPAIR_OK\n";
