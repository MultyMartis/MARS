<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$plugin = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core/shpigovsky-core.php';
if ( is_readable( $plugin ) ) {
	require_once $plugin;
}

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$validation = $root . '/validation/v9-06e24-hero-cta-button-text-per-entity';
$json_dir = $root . '/acf-json/';
$runtime = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';

$target_keys = array(
	'group_fp02_page_home',
	'group_fp02_page_services_hub',
	'group_fp02_service_layout_hero',
	'group_fp02_page_institutional',
);

$all = \Shpigovsky\Core\Fields\FieldGroups::get_field_groups();
$rows = array();

foreach ( $all as $group ) {
	if ( ! in_array( $group['key'], $target_keys, true ) ) {
		continue;
	}
	$has_cta = false;
	foreach ( $group['fields'] as $field ) {
		if ( ( $field['name'] ?? '' ) === 'hero_cta_label' ) {
			$has_cta = true;
			break;
		}
	}
	if ( function_exists( 'acf_import_field_group' ) ) {
		acf_import_field_group( $group );
	}
	$path = $json_dir . $group['key'] . '.json';
	file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	copy( $path, $runtime . '/wp-content/acf-json/' . $group['key'] . '.json' );
	$rows[] = array(
		'field_group'      => $group['key'],
		'hero_cta_present' => $has_cta,
		'sync'             => 'FieldGroups.php import',
		'result'           => $has_cta ? 'PASS' : 'FAIL',
	);
}

file_put_contents(
	$validation . '/acf-local-hero-field-group-sync-result.json',
	wp_json_encode( array( 'wave' => 'V9-06E24', 'result' => in_array( 'FAIL', array_column( $rows, 'result' ), true ) ? 'FAIL' : 'PASS', 'groups' => $rows ), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);

echo "Imported " . count( $rows ) . " groups\n";
foreach ( $rows as $r ) {
	echo $r['field_group'] . ': ' . $r['result'] . "\n";
}
