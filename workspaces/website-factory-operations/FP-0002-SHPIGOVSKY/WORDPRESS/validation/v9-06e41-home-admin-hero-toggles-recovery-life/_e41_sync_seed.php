<?php
/**
 * V9-06E41 — sync Home ACF group from PHP, seed toggles + stage labels, export JSON.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$php  = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';

$all   = \Shpigovsky\Core\Fields\FieldGroups::get_field_groups();
$group = null;
foreach ( $all as $g ) {
	if ( ( $g['key'] ?? '' ) === 'group_fp02_page_home' ) {
		$group = $g;
		break;
	}
}
if ( ! $group ) {
	fwrite( STDERR, "NO_GROUP\n" );
	exit( 1 );
}

global $wpdb;
$rows = $wpdb->get_results(
	"SELECT p.ID, p.post_status
	 FROM {$wpdb->posts} p
	 INNER JOIN {$wpdb->postmeta} m ON m.post_id = p.ID AND m.meta_key = 'key' AND m.meta_value = 'group_fp02_page_home'
	 WHERE p.post_type = 'acf-field-group'
	 ORDER BY FIELD(p.post_status,'publish','acf-disabled','trash'), p.ID ASC"
);
$keep_id = 0;
foreach ( $rows as $r ) {
	if ( 'publish' === $r->post_status ) {
		$keep_id = (int) $r->ID;
		break;
	}
}
if ( ! $keep_id && ! empty( $rows ) ) {
	$keep_id = (int) $rows[0]->ID;
}
echo "KEEP_ID={$keep_id}\n";

foreach ( $rows as $r ) {
	$id = (int) $r->ID;
	if ( $id === $keep_id ) {
		continue;
	}
	if ( 'trash' !== $r->post_status ) {
		wp_trash_post( $id );
		echo "TRASHED={$id}\n";
	}
}

$group['ID'] = $keep_id;
$imported    = acf_import_field_group( $group );
echo 'REIMPORT=' . wp_json_encode(
	is_array( $imported )
		? array(
			'ID'  => $imported['ID'] ?? null,
			'key' => $imported['key'] ?? null,
		)
		: $imported
) . "\n";

wp_update_post(
	array(
		'ID'          => $keep_id,
		'post_status' => 'publish',
	)
);

if ( function_exists( 'acf_get_store' ) ) {
	foreach ( array( 'fields', 'field-groups' ) as $store_name ) {
		$store = acf_get_store( $store_name );
		if ( $store ) {
			$store->reset();
		}
	}
}

$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'FIELD_COUNT=' . count( (array) $fields ) . "\n";

$page_id = (int) get_option( 'page_on_front' );
if ( $page_id <= 0 ) {
	$page_id = 4;
}
echo "HOME_ID={$page_id}\n";

$toggles = array(
	'home_hero_autoplay_enabled'        => 1,
	'home_hero_autoplay_delay'          => 5000,
	'home_hero_arrows_enabled'          => 1,
	'home_hero_dots_enabled'            => 1,
	'home_founder_quote_visible'        => 1,
	'home_treatment_prevention_visible' => 1,
	'home_gallery_visible'              => 1,
	'home_reviews_visible'              => 1,
	'home_rehab_requirements_visible'   => 1,
	'home_rehab_program_visible'        => 1,
	'home_comfort_visible'              => 1,
	'home_specialists_visible'          => 1,
	'home_articles_visible'             => 1,
);

foreach ( $toggles as $key => $val ) {
	if ( ! metadata_exists( 'post', $page_id, $key ) ) {
		update_field( $key, $val, $page_id );
		echo "SEEDED_TOGGLE={$key}={$val}\n";
	} else {
		echo "KEEP_TOGGLE={$key}=" . get_post_meta( $page_id, $key, true ) . "\n";
	}
}

$labels = array( '1 месяц', '2 месяц', '3 месяц' );
$stage_count = (int) get_post_meta( $page_id, 'home_recovery_life_stages', true );
if ( $stage_count < 1 ) {
	$stage_count = 3;
}
for ( $i = 0; $i < $stage_count && $i < 3; $i++ ) {
	$meta_key = "home_recovery_life_stages_{$i}_stage_label";
	$current  = get_post_meta( $page_id, $meta_key, true );
	if ( '' === (string) $current ) {
		update_post_meta( $page_id, $meta_key, $labels[ $i ] );
		update_post_meta( $page_id, '_' . $meta_key, 'field_fp02_home_recovery_life_stage_label' );
		echo "SEEDED_STAGE_LABEL={$i}={$labels[$i]}\n";
	} else {
		echo "KEEP_STAGE_LABEL={$i}={$current}\n";
	}
}

// Also refresh via update_field if ACF knows the repeater.
if ( function_exists( 'get_field' ) && function_exists( 'update_field' ) ) {
	$rows = get_field( 'home_recovery_life_stages', $page_id );
	if ( is_array( $rows ) && ! empty( $rows ) ) {
		$changed = false;
		foreach ( $rows as $idx => $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$label = isset( $row['stage_label'] ) ? trim( (string) $row['stage_label'] ) : '';
			if ( '' === $label && isset( $labels[ $idx ] ) ) {
				$rows[ $idx ]['stage_label'] = $labels[ $idx ];
				$changed                     = true;
			}
		}
		if ( $changed ) {
			update_field( 'home_recovery_life_stages', $rows, $page_id );
			echo "UPDATED_STAGES_VIA_ACF=1\n";
		}
	}
}

unset( $group['ID'] );
$json = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
file_put_contents( $root . '/acf-json/group_fp02_page_home.json', $json );
copy( $root . '/acf-json/group_fp02_page_home.json', 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_page_home.json' );
echo "JSON_WRITTEN=1\n";

$names = array();
foreach ( (array) $fields as $f ) {
	$names[] = $f['name'] ?? '';
}
$need = array(
	'home_hero_autoplay_enabled',
	'home_founder_quote_visible',
	'home_gallery_visible',
	'home_reviews_visible',
	'home_rehab_program_visible',
	'home_articles_visible',
);
foreach ( $need as $n ) {
	echo 'HAS_' . $n . '=' . ( in_array( $n, $names, true ) ? '1' : '0' ) . "\n";
}

echo "DONE\n";
