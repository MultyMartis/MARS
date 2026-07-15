<?php
/**
 * V9-06E47-FIX01 — admin group visibility / order / overlap audit (read-only).
 */
$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once $wp_load;

if ( ! function_exists( 'acf_get_field_groups' ) ) {
	fwrite( STDERR, "ACF missing\n" );
	exit( 1 );
}

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup_admin = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e47-fix01-service-general-admin-ux-cleanup-before-20260715-125222/admin';

$posts = array( 74, 314, 78, 73 );

function fix01_group_fields( $group_key ) {
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
	if ( ! is_array( $fields ) ) {
		return array();
	}
	$out = array();
	foreach ( $fields as $f ) {
		$out[] = array(
			'name'  => isset( $f['name'] ) ? (string) $f['name'] : '',
			'label' => isset( $f['label'] ) ? (string) $f['label'] : '',
			'type'  => isset( $f['type'] ) ? (string) $f['type'] : '',
			'key'   => isset( $f['key'] ) ? (string) $f['key'] : '',
		);
	}
	return $out;
}

$all_inventory = array();

foreach ( $posts as $post_id ) {
	$post = get_post( $post_id );
	$role = (string) get_post_meta( $post_id, 'service_editor_role', true );
	if ( function_exists( 'get_field' ) ) {
		$acf_role = (string) get_field( 'service_editor_role', $post_id );
		if ( '' !== $acf_role ) {
			$role = $acf_role;
		}
	}

	// Simulate ACF form context for filters.
	if ( function_exists( 'acf_set_form_data' ) ) {
		acf_set_form_data( 'post_id', $post_id );
	}
	$_GET['post'] = (string) $post_id;

	$groups = acf_get_field_groups( array( 'post_id' => $post_id ) );
	$rows   = array();
	$order  = 0;
	foreach ( $groups as $g ) {
		++$order;
		$key   = isset( $g['key'] ) ? (string) $g['key'] : '';
		$title = isset( $g['title'] ) ? (string) $g['title'] : '';
		$local = isset( $g['local'] ) ? (string) $g['local'] : ( isset( $g['ID'] ) && $g['ID'] ? 'DB' : 'unknown' );
		$fields = fix01_group_fields( $key );
		$rows[] = array(
			'visible_order' => $order,
			'group_title'   => $title,
			'group_key'     => $key,
			'source'        => $local,
			'menu_order'    => isset( $g['menu_order'] ) ? (int) $g['menu_order'] : 0,
			'field_count'   => count( $fields ),
			'fields'        => $fields,
		);
	}

	$all_inventory[ $post_id ] = array(
		'post_id'   => $post_id,
		'title'     => $post ? $post->post_title : '',
		'role'      => $role,
		'groups'    => $rows,
	);

	file_put_contents(
		$backup_admin . '/admin-groups-' . $post_id . '-before.json',
		wp_json_encode( $all_inventory[ $post_id ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
	);
}

file_put_contents(
	$backup_admin . '/admin-groups-inventory-before.json',
	wp_json_encode( $all_inventory, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE )
);

// Known legacy / parity keys.
$parity_service = 'group_fp02_service_general_parity';
$parity_section = 'group_fp02_service_section_parity';
$layout         = 'group_fp02_service_layout_hero';
$hero           = 'group_fp02_service_hero';
$legacy_keys    = array(
	'group_fp02_service_structured_sections',
	'group_fp02_service_faq',
	'group_fp02_service_relationships',
);

// Build CSV for #74.
$csv = "visible_order,group_title,group_key,source,field_count,editor_facing,currently_needed_for_frontend,overlaps_with_service_general_parity,target_action,notes\n";
$inv74 = $all_inventory[74]['groups'];
foreach ( $inv74 as $row ) {
	$key = $row['group_key'];
	$editor = 'yes';
	$needed = 'investigate';
	$overlap = 'no';
	$action = 'investigate';
	$notes = '';

	if ( $key === $layout ) {
		$editor = 'yes'; $needed = 'yes'; $action = 'keep'; $notes = 'Desired position 1; rename title to Макет if needed';
	} elseif ( $key === $hero ) {
		$editor = 'yes'; $needed = 'yes'; $action = 'keep'; $notes = 'Desired position 2';
	} elseif ( $key === $parity_service ) {
		$editor = 'yes'; $needed = 'yes'; $action = 'keep'; $notes = 'Desired position 3 — primary service blocks';
	} elseif ( $key === $parity_section ) {
		$editor = 'no'; $needed = 'no'; $action = 'hide_from_normal_ui'; $notes = 'Opposite role — already filtered for service role';
	} elseif ( in_array( $key, $legacy_keys, true ) ) {
		$editor = 'no';
		$needed = ( $key === 'group_fp02_service_structured_sections' ) ? 'partial_cta_meta' : ( $key === 'group_fp02_service_relationships' ? 'partial_children_override' : 'legacy_emergency' );
		$overlap = 'yes';
		$action = 'hide_from_normal_ui';
		$notes = 'Parity replaces editor UX; keep definitions/meta';
	} else {
		$action = 'investigate';
		$notes = 'Unexpected group on #74';
	}

	$csv .= sprintf(
		"%d,\"%s\",%s,%s,%d,%s,%s,%s,%s,\"%s\"\n",
		$row['visible_order'],
		str_replace( '"', '""', $row['group_title'] ),
		$key,
		$row['source'],
		$row['field_count'],
		$editor,
		$needed,
		$overlap,
		$action,
		str_replace( '"', '""', $notes )
	);
}
file_put_contents( $evidence . '/v9-06e47-fix01-visible-admin-group-audit.csv', $csv );

// Admin order audit.
$order_csv = "current_order,current_group_or_box,desired_order,desired_group_or_box,action,notes\n";
$desired = array(
	1 => 'Макет страницы услуги (group_fp02_service_layout_hero)',
	2 => 'Hero страницы услуги (group_fp02_service_hero)',
	3 => 'Услуга — блоки страницы (group_fp02_service_general_parity)',
);
foreach ( $inv74 as $row ) {
	$des_ord = '';
	$des_name = '';
	$act = 'hide_or_reorder';
	if ( $row['group_key'] === $layout ) { $des_ord = 1; $des_name = $desired[1]; $act = 'keep_as_1'; }
	elseif ( $row['group_key'] === $hero ) { $des_ord = 2; $des_name = $desired[2]; $act = 'keep_as_2'; }
	elseif ( $row['group_key'] === $parity_service ) { $des_ord = 3; $des_name = $desired[3]; $act = 'keep_as_3'; }
	elseif ( $row['group_key'] === $parity_section ) { $act = 'ensure_hidden'; }
	else { $act = 'hide_from_normal_ui'; }
	$order_csv .= sprintf(
		"%d,\"%s\",%s,\"%s\",%s,\"%s\"\n",
		$row['visible_order'],
		str_replace( '"', '""', $row['group_title'] . '|' . $row['group_key'] ),
		$des_ord === '' ? '' : $des_ord,
		str_replace( '"', '""', $des_name ),
		$act,
		'before FIX01'
	);
}
file_put_contents( $evidence . '/v9-06e47-fix01-admin-order-audit.csv', $order_csv );

// Field overlap audit — structured vs parity key names.
$structured_fields = fix01_group_fields( 'group_fp02_service_structured_sections' );
$faq_fields        = fix01_group_fields( 'group_fp02_service_faq' );
$parity_fields     = fix01_group_fields( $parity_service );
$rel_fields        = fix01_group_fields( 'group_fp02_service_relationships' );

$parity_names = array();
foreach ( $parity_fields as $f ) {
	if ( $f['name'] !== '' ) {
		$parity_names[ $f['name'] ] = $f;
	}
}

$overlap_map = array(
	'intro_text' => array( 'parity' => 'service_general_intro_heading/highlight (different names)', 'fe' => 'parity primary', 'action' => 'hide_legacy' ),
	'intro_note' => array( 'parity' => 'service_general_intro_*', 'fe' => 'parity', 'action' => 'hide_legacy' ),
	'signs_items' => array( 'parity' => 'service_general_signs_items', 'fe' => 'parity for alcohol stack', 'action' => 'hide_legacy' ),
	'programme_items' => array( 'parity' => 'service_general_approach_cards / program', 'fe' => 'legacy partial on non-alcohol', 'action' => 'hide_legacy_keep_meta' ),
	'stages' => array( 'parity' => 'service_general_stages_items', 'fe' => 'parity', 'action' => 'hide_legacy' ),
	'cta_title' => array( 'parity' => 'none (visibility-only mid-cta)', 'fe' => 'yes via Structured meta', 'action' => 'keep_meta_hide_ui_or_mirror' ),
	'cta_text' => array( 'parity' => 'none', 'fe' => 'yes', 'action' => 'keep_meta_hide_ui_or_mirror' ),
	'cta_button_label' => array( 'parity' => 'none', 'fe' => 'yes', 'action' => 'keep_meta_hide_ui_or_mirror' ),
	'cta_button_target' => array( 'parity' => 'none', 'fe' => 'yes', 'action' => 'keep_meta_hide_ui_or_mirror' ),
	'faq_items' => array( 'parity' => 'service_general_faq_items', 'fe' => 'parity for general stack', 'action' => 'hide_legacy' ),
	'manual_related_services' => array( 'parity' => 'children toggle only', 'fe' => 'children override', 'action' => 'hide_legacy_keep_meta' ),
);

$ov_csv = "field_name,field_label,current_group,also_in_group,used_by_frontend,parity_field_exists,target_group,target_action,meta_key_preserved,notes\n";
$sets = array(
	array( 'group' => 'group_fp02_service_structured_sections', 'fields' => $structured_fields ),
	array( 'group' => 'group_fp02_service_faq', 'fields' => $faq_fields ),
	array( 'group' => 'group_fp02_service_relationships', 'fields' => $rel_fields ),
);
foreach ( $sets as $set ) {
	foreach ( $set['fields'] as $f ) {
		if ( $f['name'] === '' || $f['type'] === 'message' ) {
			continue;
		}
		$m = isset( $overlap_map[ $f['name'] ] ) ? $overlap_map[ $f['name'] ] : null;
		$parity_exists = 'no';
		foreach ( $parity_names as $pn => $_ ) {
			if ( false !== strpos( $pn, 'service_general_' ) && (
				false !== strpos( $pn, str_replace( array( 'items', '_' ), '', $f['name'] ) ) ||
				( $f['name'] === 'faq_items' && false !== strpos( $pn, 'faq' ) ) ||
				( $f['name'] === 'signs_items' && false !== strpos( $pn, 'signs' ) ) ||
				( $f['name'] === 'stages' && false !== strpos( $pn, 'stages' ) )
			) ) {
				$parity_exists = 'yes';
			}
		}
		if ( in_array( $f['name'], array( 'cta_title', 'cta_text', 'cta_button_label', 'cta_button_target', 'manual_related_services' ), true ) ) {
			$parity_exists = 'no';
		}
		if ( in_array( $f['name'], array( 'signs_items', 'stages', 'faq_items' ), true ) ) {
			$parity_exists = 'yes';
		}
		$ov_csv .= sprintf(
			"%s,\"%s\",%s,%s,%s,%s,%s,%s,yes,\"%s\"\n",
			$f['name'],
			str_replace( '"', '""', $f['label'] ),
			$set['group'],
			$parity_service,
			$m ? 'yes' : 'partial',
			$parity_exists,
			$parity_exists === 'yes' ? $parity_service : 'meta_only_hidden_legacy',
			$m ? $m['action'] : 'hide_from_normal_ui',
			$m ? str_replace( '"', '""', $m['parity'] . '; ' . $m['fe'] ) : 'legacy field'
		);
	}
}
file_put_contents( $evidence . '/v9-06e47-fix01-field-overlap-audit.csv', $ov_csv );

echo "POST 74 groups:\n";
foreach ( $inv74 as $row ) {
	echo $row['visible_order'] . '. [' . $row['menu_order'] . '] ' . $row['group_title'] . ' (' . $row['group_key'] . ") fields=" . $row['field_count'] . " src=" . $row['source'] . "\n";
}
echo "\nPOST 73 group keys: ";
echo implode( ', ', array_map( function( $r ) { return $r['group_key']; }, $all_inventory[73]['groups'] ) ) . "\n";
echo "DONE\n";
