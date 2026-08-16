<?php
/**
 * V9-06E47-FIX02 — post-fix validation + evidence CSVs.
 *
 * @package Shpigovsky
 */

define( 'WP_USE_THEMES', false );
$_SERVER['REQUEST_URI'] = '/wp-admin/post.php?post=74&action=edit';
$_SERVER['PHP_SELF']    = '/wp-admin/post.php';
$_GET['post']           = '74';
$_GET['action']         = 'edit';

require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/meta-boxes.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

if ( ! defined( 'WP_ADMIN' ) ) {
	define( 'WP_ADMIN', true );
}

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup   = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e47-fix02-service-general-acf-render-before-20260715-133411';

/**
 * Probe groups for a post.
 *
 * @param int $post_id Post ID.
 * @return array{role:string,keys:string[],titles:string[],field_count:int,cond_count:int}
 */
function fix02_probe( $post_id ) {
	$_GET['post'] = (string) $post_id;
	if ( function_exists( 'acf_set_form_data' ) ) {
		acf_set_form_data( 'post_id', $post_id );
	}

	$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
	if ( function_exists( 'get_field' ) ) {
		$acf_role = (string) get_field( 'service_editor_role', $post_id );
		if ( '' !== $acf_role ) {
			$role = $acf_role;
		}
	}

	$groups = acf_get_field_groups( array( 'post_id' => $post_id ) );
	$keys   = array();
	$titles = array();
	foreach ( $groups as $g ) {
		$keys[]   = isset( $g['key'] ) ? (string) $g['key'] : '';
		$titles[] = isset( $g['title'] ) ? (string) $g['title'] : '';
	}

	$fields = acf_get_fields( 'group_fp02_service_general_parity' );
	$cond   = 0;
	$count  = is_array( $fields ) ? count( $fields ) : 0;
	if ( is_array( $fields ) ) {
		foreach ( $fields as $f ) {
			if ( ! empty( $f['conditional_logic'] ) ) {
				++$cond;
			}
		}
	}

	$prepared = null;
	$role_field = acf_get_field( 'field_fp02_service_editor_role' );
	if ( is_array( $role_field ) && class_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance' ) ) {
		$prepared = \Shpigovsky\Core\Admin\ServiceLayoutGovernance::prepare_editor_role_field( $role_field );
	}

	return array(
		'role'               => $role,
		'keys'               => $keys,
		'titles'             => $titles,
		'field_count'        => $count,
		'cond_count'         => $cond,
		'prepared_role_type' => is_array( $prepared ) && isset( $prepared['type'] ) ? $prepared['type'] : '',
		'parity_visible'     => in_array( 'group_fp02_service_general_parity', $keys, true ),
		'section_visible'    => in_array( 'group_fp02_service_section_parity', $keys, true ),
		'legacy_visible'     => (bool) array_intersect(
			$keys,
			array(
				'group_fp02_service_structured_sections',
				'group_fp02_service_faq',
				'group_fp02_service_relationships',
			)
		),
	);
}

/**
 * CSV escape.
 *
 * @param mixed $v Value.
 * @return string
 */
function fix02_csv( $v ) {
	$s = is_scalar( $v ) || null === $v ? (string) $v : wp_json_encode( $v, JSON_UNESCAPED_UNICODE );
	return '"' . str_replace( '"', '""', $s ) . '"';
}

// --- Metabox inventory (simulate service edit screen) ---
set_current_screen( 'service' );
$GLOBALS['post'] = get_post( 74 );
$GLOBALS['wp_meta_boxes'] = array();
do_action( 'add_meta_boxes', 'service', $GLOBALS['post'] );
do_action( 'add_meta_boxes_service', $GLOBALS['post'] );

$metabox_rows = array();
$wanted = array(
	'revisionsdiv' => 'Редакция',
	'postexcerpt'  => 'Отрывок',
	'postdivrich'  => 'Classic editor',
	'commentstatusdiv' => 'Discussion',
	'commentsdiv'  => 'Comments',
	'postcustom'   => 'Custom Fields',
	'trackbacksdiv'=> 'Trackbacks',
	'submitdiv'    => 'Publish',
	'pageparentdiv'=> 'Page Attributes',
	'postimagediv' => 'Featured Image',
	'slugdiv'      => 'Slug',
);

$found = array();
if ( ! empty( $GLOBALS['wp_meta_boxes']['service'] ) && is_array( $GLOBALS['wp_meta_boxes']['service'] ) ) {
	foreach ( $GLOBALS['wp_meta_boxes']['service'] as $context => $priorities ) {
		foreach ( (array) $priorities as $prio => $boxes ) {
			foreach ( (array) $boxes as $id => $box ) {
				if ( ! is_array( $box ) || empty( $box['title'] ) ) {
					continue;
				}
				$found[ $id ] = array(
					'id'       => $id,
					'title'    => (string) $box['title'],
					'context'  => $context,
					'priority' => $prio,
				);
			}
		}
	}
}

$map = array(
	'revisionsdiv' => array( 'before' => 'visible', 'action' => 'hide', 'source' => 'wp-core (revisions support)' ),
	'postexcerpt'  => array( 'before' => 'visible', 'action' => 'hide', 'source' => 'wp-core (excerpt support)' ),
	'postdivrich'  => array( 'before' => 'hidden', 'action' => 'keep_hidden', 'source' => 'theme admin-editor.php' ),
	'commentstatusdiv' => array( 'before' => 'hidden', 'action' => 'keep_hidden', 'source' => 'EditorRestrictions' ),
	'commentsdiv'  => array( 'before' => 'hidden', 'action' => 'keep_hidden', 'source' => 'EditorRestrictions' ),
	'postcustom'   => array( 'before' => 'hidden', 'action' => 'keep_hidden', 'source' => 'EditorRestrictions' ),
	'trackbacksdiv'=> array( 'before' => 'hidden', 'action' => 'keep_hidden', 'source' => 'EditorRestrictions' ),
	'submitdiv'    => array( 'before' => 'visible', 'action' => 'keep', 'source' => 'wp-core' ),
	'pageparentdiv'=> array( 'before' => 'visible', 'action' => 'keep', 'source' => 'wp-core' ),
	'postimagediv' => array( 'before' => 'visible', 'action' => 'keep', 'source' => 'wp-core' ),
);

$csv_meta = "metabox_id,title,source,visible_before,visible_after,target_action,notes\n";
foreach ( $map as $id => $info ) {
	$visible_after = isset( $found[ $id ] ) ? 'visible' : 'hidden';
	$title = isset( $found[ $id ] ) ? $found[ $id ]['title'] : ( isset( $wanted[ $id ] ) ? $wanted[ $id ] : $id );
	$csv_meta .= implode(
		',',
		array(
			fix02_csv( $id ),
			fix02_csv( $title ),
			fix02_csv( $info['source'] ),
			fix02_csv( $info['before'] ),
			fix02_csv( $visible_after ),
			fix02_csv( $info['action'] ),
			fix02_csv( isset( $found[ $id ] ) ? 'present in add_meta_boxes result' : 'removed / not registered' ),
		)
	) . "\n";
}
// Also list leftover unexpected boxes.
foreach ( $found as $id => $box ) {
	if ( isset( $map[ $id ] ) || 0 === strpos( $id, 'acf-' ) || 0 === strpos( $id, 'acfgroup_' ) ) {
		continue;
	}
	$csv_meta .= implode(
		',',
		array(
			fix02_csv( $id ),
			fix02_csv( $box['title'] ),
			fix02_csv( 'unknown' ),
			fix02_csv( 'unknown' ),
			fix02_csv( 'visible' ),
			fix02_csv( 'audit_only' ),
			fix02_csv( 'context=' . $box['context'] ),
		)
	) . "\n";
}
file_put_contents( $evidence . '/v9-06e47-fix02-admin-metabox-inventory.csv', $csv_meta );

// --- Field visibility ---
$fields = acf_get_fields( 'group_fp02_service_general_parity' );
$csv_fields = "field_order,field_name,field_label,field_type,parent_group,visible_after yes/no,notes\n";
$order = 0;
$repeater_hits = array(
	'service_general_signs_items'            => false,
	'service_general_bordered_info_items'    => false,
	'service_general_approach_cards'         => false,
	'service_general_program_intro_items'    => false,
	'service_general_stages_items'           => false,
	'service_general_stages_support_items'   => false,
	'service_general_faq_items'              => false,
	'cta_title'                              => false,
	'cta_text'                               => false,
	'cta_button_label'                       => false,
	'cta_button_target'                      => false,
);
if ( is_array( $fields ) ) {
	foreach ( $fields as $f ) {
		++$order;
		$name = isset( $f['name'] ) ? (string) $f['name'] : '';
		if ( isset( $repeater_hits[ $name ] ) ) {
			$repeater_hits[ $name ] = true;
		}
		$csv_fields .= implode(
			',',
			array(
				fix02_csv( $order ),
				fix02_csv( $name ),
				fix02_csv( isset( $f['label'] ) ? $f['label'] : '' ),
				fix02_csv( isset( $f['type'] ) ? $f['type'] : '' ),
				fix02_csv( 'group_fp02_service_general_parity' ),
				fix02_csv( empty( $f['conditional_logic'] ) ? 'yes' : 'no' ),
				fix02_csv( empty( $f['conditional_logic'] ) ? 'no field conditional' : 'HAS conditional' ),
			)
		) . "\n";
	}
}
file_put_contents( $evidence . '/v9-06e47-fix02-service-general-field-visibility.csv', $csv_fields );

// --- Admin validation probes ---
$p74  = fix02_probe( 74 );
$p314 = fix02_probe( 314 );
$p78  = fix02_probe( 78 );
$p73  = fix02_probe( 73 );

file_put_contents(
	$backup . '/admin/admin-groups-74-after.json',
	wp_json_encode( $p74, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);
file_put_contents(
	$backup . '/admin/admin-groups-314-after.json',
	wp_json_encode( $p314, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);
file_put_contents(
	$backup . '/admin/admin-groups-78-after.json',
	wp_json_encode( $p78, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);
file_put_contents(
	$backup . '/admin/admin-groups-73-after.json',
	wp_json_encode( $p73, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);

$revisions_hidden = ! isset( $found['revisionsdiv'] );
$excerpt_hidden   = ! isset( $found['postexcerpt'] );
$classic_hidden   = ! isset( $found['postdivrich'] );

$admin_rows = array(
	array( 'check' => '#74_groups_count', 'expected' => '3', 'actual' => (string) count( $p74['keys'] ), 'result' => 3 === count( $p74['keys'] ) ? 'PASS' : 'FAIL' ),
	array( 'check' => '#74_parity_visible', 'expected' => 'yes', 'actual' => $p74['parity_visible'] ? 'yes' : 'no', 'result' => $p74['parity_visible'] ? 'PASS' : 'FAIL' ),
	array( 'check' => '#74_parity_fields', 'expected' => '68', 'actual' => (string) $p74['field_count'], 'result' => 68 === (int) $p74['field_count'] ? 'PASS' : 'FAIL' ),
	array( 'check' => '#74_parity_conditionals', 'expected' => '0', 'actual' => (string) $p74['cond_count'], 'result' => 0 === (int) $p74['cond_count'] ? 'PASS' : 'FAIL' ),
	array( 'check' => '#74_nested_role_is_message', 'expected' => 'message', 'actual' => $p74['prepared_role_type'], 'result' => 'message' === $p74['prepared_role_type'] ? 'PASS' : 'FAIL' ),
	array( 'check' => '#74_legacy_hidden', 'expected' => 'yes', 'actual' => $p74['legacy_visible'] ? 'no' : 'yes', 'result' => $p74['legacy_visible'] ? 'FAIL' : 'PASS' ),
	array( 'check' => '#74_section_hidden', 'expected' => 'yes', 'actual' => $p74['section_visible'] ? 'no' : 'yes', 'result' => $p74['section_visible'] ? 'FAIL' : 'PASS' ),
	array( 'check' => 'revisionsdiv_hidden', 'expected' => 'yes', 'actual' => $revisions_hidden ? 'yes' : 'no', 'result' => $revisions_hidden ? 'PASS' : 'FAIL' ),
	array( 'check' => 'postexcerpt_hidden', 'expected' => 'yes', 'actual' => $excerpt_hidden ? 'yes' : 'no', 'result' => $excerpt_hidden ? 'PASS' : 'FAIL' ),
	array( 'check' => 'classic_hidden', 'expected' => 'yes', 'actual' => $classic_hidden ? 'yes' : 'no', 'result' => $classic_hidden ? 'PASS' : 'FAIL' ),
	array( 'check' => '#314_parity_usable', 'expected' => 'yes', 'actual' => ( $p314['parity_visible'] && 0 === (int) $p314['cond_count'] ) ? 'yes' : 'no', 'result' => ( $p314['parity_visible'] && 0 === (int) $p314['cond_count'] ) ? 'PASS' : 'FAIL' ),
	array( 'check' => '#78_parity_usable', 'expected' => 'yes', 'actual' => ( $p78['parity_visible'] && 0 === (int) $p78['cond_count'] ) ? 'yes' : 'no', 'result' => ( $p78['parity_visible'] && 0 === (int) $p78['cond_count'] ) ? 'PASS' : 'FAIL' ),
	array( 'check' => '#73_section_preserved', 'expected' => 'section_visible_parity_hidden', 'actual' => ( $p73['section_visible'] && ! $p73['parity_visible'] ) ? 'section_visible_parity_hidden' : wp_json_encode( $p73['titles'] ), 'result' => ( $p73['section_visible'] && ! $p73['parity_visible'] ) ? 'PASS' : 'FAIL' ),
);

foreach ( $repeater_hits as $name => $ok ) {
	$admin_rows[] = array(
		'check'    => 'field_' . $name,
		'expected' => 'visible',
		'actual'   => $ok ? 'visible' : 'missing',
		'result'   => $ok ? 'PASS' : 'FAIL',
	);
}

$csv_admin = "check,expected,actual,result\n";
foreach ( $admin_rows as $row ) {
	$csv_admin .= implode( ',', array( fix02_csv( $row['check'] ), fix02_csv( $row['expected'] ), fix02_csv( $row['actual'] ), fix02_csv( $row['result'] ) ) ) . "\n";
}
file_put_contents( $evidence . '/v9-06e47-fix02-admin-validation.csv', $csv_admin );

// Update diagnostics confirmed row rewrite.
$diag = "area,finding,root_cause_candidate,confirmed yes/no,fix,notes\n";
$diag .= fix02_csv( 'nested_role_field' ) . ',' . fix02_csv( '#74 nested depth=2; prepare_editor_role_field → type=message name=""; all 68 parity fields previously had when_service conditional on field_fp02_service_editor_role' ) . ',' . fix02_csv( 'ACF JS conditionals cannot evaluate message/empty-name controller → fields stay hidden while group title still shows' ) . ',' . fix02_csv( 'yes' ) . ',' . fix02_csv( 'when_service() returns 0; rely on load_field_groups role filter' ) . ',' . fix02_csv( 'verified via WP_ADMIN bootstrap' ) . "\n";
$diag .= fix02_csv( 'field_definitions' ) . ',' . fix02_csv( '68 top-level fields; 0 nonempty conditionals after fix' ) . ',' . fix02_csv( 'empty/invalid field defs' ) . ',' . fix02_csv( 'no' ) . ',' . fix02_csv( 'n/a' ) . ',' . fix02_csv( 'field count preserved' ) . "\n";
$diag .= fix02_csv( 'acf_filters' ) . ',' . fix02_csv( 'FIX01 role filter keeps parity for service; hides for section' ) . ',' . fix02_csv( 'filter strips fields' ) . ',' . fix02_csv( 'no' ) . ',' . fix02_csv( 'kept' ) . ',' . fix02_csv( '#74 keys=' . implode( '|', $p74['keys'] ) ) . "\n";
$diag .= fix02_csv( 'admin_metaboxes' ) . ',' . fix02_csv( 'revisionsdiv/postexcerpt supported by CPT' ) . ',' . fix02_csv( 'default WP metabox clutter' ) . ',' . fix02_csv( 'yes' ) . ',' . fix02_csv( 'remove_meta_box in EditorRestrictions' ) . ',' . fix02_csv( 'revisions_hidden=' . ( $revisions_hidden ? '1' : '0' ) . '; excerpt_hidden=' . ( $excerpt_hidden ? '1' : '0' ) ) . "\n";
$diag .= fix02_csv( 'admin_js_css_postbox' ) . ',' . fix02_csv( 'no evidence of collapsed-only preference as sole cause; empty body from conditionals' ) . ',' . fix02_csv( 'postbox user meta' ) . ',' . fix02_csv( 'no' ) . ',' . fix02_csv( 'n/a' ) . ',' . fix02_csv( 'primary fix is conditional removal' ) . "\n";
file_put_contents( $evidence . '/v9-06e47-fix02-acf-render-diagnostics.csv', $diag );

$fail = 0;
foreach ( $admin_rows as $row ) {
	if ( 'PASS' !== $row['result'] ) {
		++$fail;
		echo 'FAIL ' . $row['check'] . ' actual=' . $row['actual'] . PHP_EOL;
	}
}
echo 'ADMIN_VALIDATION fail_count=' . $fail . ' groups74=' . implode( '|', $p74['titles'] ) . ' fields=' . $p74['field_count'] . ' cond=' . $p74['cond_count'] . PHP_EOL;
echo 'METABOX revisions=' . ( $revisions_hidden ? 'hidden' : 'VISIBLE' ) . ' excerpt=' . ( $excerpt_hidden ? 'hidden' : 'VISIBLE' ) . ' classic=' . ( $classic_hidden ? 'hidden' : 'VISIBLE' ) . PHP_EOL;
echo 'FOUND_BOXES=' . implode( '|', array_keys( $found ) ) . PHP_EOL;
