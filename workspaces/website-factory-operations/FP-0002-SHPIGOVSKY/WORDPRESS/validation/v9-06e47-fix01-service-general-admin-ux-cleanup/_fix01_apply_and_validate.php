<?php
/**
 * V9-06E47-FIX01 — soft-disable legacy DB ACF group duplicates + post-apply validation.
 *
 * @package Shpigovsky
 */

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once $wp_load;

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup_admin = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e47-fix01-service-general-admin-ux-cleanup-before-20260715-125222/admin';

$db_writes = 0;
$disabled  = array();

// Soft-disable DB duplicates of legacy service groups (definitions/meta preserved).
$legacy_excerpts = array(
	'service-structured-sections',
	'service-faq',
	'service-relationships-related-services',
);

$q = new WP_Query(
	array(
		'post_type'      => 'acf-field-group',
		'post_status'    => array( 'publish', 'acf-disabled' ),
		'posts_per_page' => 100,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);

foreach ( $q->posts as $post ) {
	$excerpt = (string) $post->post_excerpt;
	if ( ! in_array( $excerpt, $legacy_excerpts, true ) ) {
		continue;
	}
	if ( 'acf-disabled' === $post->post_status ) {
		$disabled[] = array(
			'id'     => (int) $post->ID,
			'title'  => $post->post_title,
			'action' => 'already_disabled',
		);
		continue;
	}
	$upd = wp_update_post(
		array(
			'ID'          => (int) $post->ID,
			'post_status' => 'acf-disabled',
		),
		true
	);
	++$db_writes;
	$disabled[] = array(
		'id'     => (int) $post->ID,
		'title'  => $post->post_title,
		'action' => is_wp_error( $upd ) ? 'disable_failed:' . $upd->get_error_message() : 'disabled',
	);
}

file_put_contents(
	$evidence . '/v9-06e47-fix01-db-legacy-group-disable.json',
	wp_json_encode(
		array(
			'db_writes' => $db_writes,
			'items'     => $disabled,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

/**
 * Probe visible groups for a post after FIX01.
 *
 * @param int $post_id Post ID.
 * @return array<string, mixed>
 */
function fix01_probe_groups( $post_id ) {
	if ( function_exists( 'acf_set_form_data' ) ) {
		acf_set_form_data( 'post_id', $post_id );
	}
	$_GET['post'] = (string) $post_id;

	$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
	if ( function_exists( 'get_field' ) ) {
		$acf_role = (string) get_field( 'service_editor_role', $post_id );
		if ( '' !== $acf_role ) {
			$role = $acf_role;
		}
	}

	$groups = acf_get_field_groups( array( 'post_id' => $post_id ) );
	$rows   = array();
	$order  = 0;
	foreach ( $groups as $g ) {
		++$order;
		$key = isset( $g['key'] ) ? (string) $g['key'] : '';
		$rows[] = array(
			'visible_order' => $order,
			'title'         => isset( $g['title'] ) ? (string) $g['title'] : '',
			'key'           => $key,
			'menu_order'    => isset( $g['menu_order'] ) ? (int) $g['menu_order'] : 0,
			'source'        => isset( $g['local'] ) ? (string) $g['local'] : ( ! empty( $g['ID'] ) ? 'DB' : 'unknown' ),
			'field_count'   => is_array( acf_get_fields( $key ) ) ? count( acf_get_fields( $key ) ) : 0,
		);
	}

	return array(
		'post_id' => $post_id,
		'title'   => get_the_title( $post_id ),
		'role'    => $role,
		'groups'  => $rows,
		'keys'    => array_map(
			static function ( $r ) {
				return $r['key'];
			},
			$rows
		),
	);
}

$probes = array();
foreach ( array( 74, 314, 78, 73 ) as $pid ) {
	$probes[ $pid ] = fix01_probe_groups( $pid );
	file_put_contents(
		$backup_admin . '/admin-groups-' . $pid . '-after.json',
		wp_json_encode( $probes[ $pid ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
	);
}

file_put_contents(
	$evidence . '/v9-06e47-fix01-admin-groups-after.json',
	wp_json_encode( $probes, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);

// Admin validation CSV.
$expected74 = array(
	'group_fp02_service_layout_hero',
	'group_fp02_service_hero',
	'group_fp02_service_general_parity',
);
$forbidden = array(
	'group_fp02_service_structured_sections',
	'group_fp02_service_faq',
	'group_fp02_service_relationships',
	'group_fp02_service_section_parity',
);

$keys74 = $probes[74]['keys'];
$admin_csv = "check,expected,actual,result\n";
$checks = array(
	array( '#74 edit groups resolve', 'yes', ! empty( $keys74 ) ? 'yes' : 'no' ),
	array( 'Layout visible', 'yes', in_array( 'group_fp02_service_layout_hero', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Hero visible', 'yes', in_array( 'group_fp02_service_hero', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Service general visible', 'yes', in_array( 'group_fp02_service_general_parity', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Section group hidden', 'yes', ! in_array( 'group_fp02_service_section_parity', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Structured hidden', 'yes', ! in_array( 'group_fp02_service_structured_sections', $keys74, true ) ? 'yes' : 'no' ),
	array( 'FAQ legacy hidden', 'yes', ! in_array( 'group_fp02_service_faq', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Relationships hidden', 'yes', ! in_array( 'group_fp02_service_relationships', $keys74, true ) ? 'yes' : 'no' ),
	array( 'Only 3 editor groups', '3', (string) count( $keys74 ) ),
);

$order_ok = true;
if ( count( $keys74 ) >= 3 ) {
	// Sort by menu_order then appearance for expected canonical trio.
	$by_key = array();
	foreach ( $probes[74]['groups'] as $g ) {
		$by_key[ $g['key'] ] = $g;
	}
	$order_actual = array();
	foreach ( $expected74 as $ek ) {
		$order_actual[] = isset( $by_key[ $ek ] ) ? $by_key[ $ek ]['title'] : 'MISSING';
	}
	$checks[] = array( 'Order layout/hero/parity present', 'yes', ( false === array_search( 'MISSING', $order_actual, true ) ) ? 'yes' : 'no' );
}

foreach ( $checks as $c ) {
	$pass = ( $c[1] === $c[2] ) ? 'PASS' : 'FAIL';
	$admin_csv .= sprintf( "\"%s\",%s,%s,%s\n", $c[0], $c[1], $c[2], $pass );
}

// Classic editor helper presence.
$classic_hidden = function_exists( 'shpigovsky_core_hide_classic_editor' ) || class_exists( '\\Shpigovsky\\Core\\Admin\\EditorRestrictions' );
$admin_csv .= sprintf( "Classic editor helpers present,yes,%s,%s\n", $classic_hidden ? 'yes' : 'unknown', $classic_hidden ? 'PASS' : 'PARTIAL' );

file_put_contents( $evidence . '/v9-06e47-fix01-admin-validation.csv', $admin_csv );

// Representative checks.
$rep_csv = "page,expected,actual,result,notes\n";
foreach ( array( 314, 78 ) as $pid ) {
	$keys = $probes[ $pid ]['keys'];
	$clean = ! array_intersect( $keys, $forbidden ) && in_array( 'group_fp02_service_general_parity', $keys, true );
	$rep_csv .= sprintf(
		"%d,service model clean,%s,%s,\"role=%s groups=%s\"\n",
		$pid,
		$clean ? 'clean' : 'dirty',
		$clean ? 'PASS' : 'FAIL',
		$probes[ $pid ]['role'],
		implode( '|', $keys )
	);
}
$keys73 = $probes[73]['keys'];
$section_ok = in_array( 'group_fp02_service_section_parity', $keys73, true )
	&& ! in_array( 'group_fp02_service_general_parity', $keys73, true )
	&& in_array( 'group_fp02_service_layout_hero', $keys73, true )
	&& in_array( 'group_fp02_service_hero', $keys73, true );
$rep_csv .= sprintf(
	"73,section model preserved,%s,%s,\"role=%s groups=%s\"\n",
	$section_ok ? 'preserved' : 'regressed',
	$section_ok ? 'PASS' : 'FAIL',
	$probes[73]['role'],
	implode( '|', $keys73 )
);
file_put_contents( $evidence . '/v9-06e47-fix01-representative-admin-validation.csv', $rep_csv );

echo "DB_WRITES=$db_writes\n";
echo "POST74:\n";
foreach ( $probes[74]['groups'] as $g ) {
	echo $g['visible_order'] . '. [' . $g['menu_order'] . '] ' . $g['title'] . ' (' . $g['key'] . ")\n";
}
echo "POST73 keys: " . implode( ', ', $keys73 ) . "\n";
echo "DONE\n";
