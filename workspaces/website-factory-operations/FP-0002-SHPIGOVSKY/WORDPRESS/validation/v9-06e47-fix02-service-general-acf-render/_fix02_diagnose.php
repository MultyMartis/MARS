<?php
/**
 * V9-06E47-FIX02 — pre-fix ACF render diagnostics for #74.
 *
 * @package Shpigovsky
 */

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once $wp_load;

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup_admin = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e47-fix02-service-general-acf-render-before-20260715-133411/admin';
if ( ! is_dir( $backup_admin ) ) {
	wp_mkdir_p( $backup_admin );
}

$post_id = 74;
$_GET['post'] = (string) $post_id;
if ( function_exists( 'acf_set_form_data' ) ) {
	acf_set_form_data( 'post_id', $post_id );
}

$role_meta = (string) get_post_meta( $post_id, 'service_editor_role', true );
$role_acf  = function_exists( 'get_field' ) ? (string) get_field( 'service_editor_role', $post_id ) : '';
$parent    = (int) get_post_field( 'post_parent', $post_id );
$depth     = class_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance' )
	? \Shpigovsky\Core\Admin\ServiceLayoutGovernance::get_service_depth( $post_id )
	: -1;
$nested    = class_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance' )
	? \Shpigovsky\Core\Admin\ServiceLayoutGovernance::is_nested_service( $post_id )
	: null;

// Simulate prepare_field for service_editor_role.
$role_field = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_service_editor_role' ) : null;
$prepared   = $role_field;
if ( is_array( $role_field ) && class_exists( '\\Shpigovsky\\Core\\Admin\\ServiceLayoutGovernance' ) ) {
	$prepared = \Shpigovsky\Core\Admin\ServiceLayoutGovernance::prepare_editor_role_field( $role_field );
}

$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $post_id ) ) : array();
$group_rows = array();
foreach ( $groups as $g ) {
	$key    = isset( $g['key'] ) ? (string) $g['key'] : '';
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $key ) : array();
	$with_cond = 0;
	$top_level = 0;
	if ( is_array( $fields ) ) {
		foreach ( $fields as $f ) {
			++$top_level;
			if ( ! empty( $f['conditional_logic'] ) ) {
				++$with_cond;
			}
		}
	}
	$group_rows[] = array(
		'key'                 => $key,
		'title'               => isset( $g['title'] ) ? $g['title'] : '',
		'active'              => ! empty( $g['active'] ),
		'menu_order'          => isset( $g['menu_order'] ) ? $g['menu_order'] : '',
		'top_level_fields'    => $top_level,
		'fields_with_cond'    => $with_cond,
		'local'               => isset( $g['local'] ) ? $g['local'] : '',
	);
}

$parity_fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( 'group_fp02_service_general_parity' ) : array();
$cond_refs_role = 0;
$dup_keys       = array();
$seen_keys      = array();
$walk           = function ( $fields ) use ( &$walk, &$cond_refs_role, &$dup_keys, &$seen_keys ) {
	if ( ! is_array( $fields ) ) {
		return;
	}
	foreach ( $fields as $f ) {
		$key = isset( $f['key'] ) ? (string) $f['key'] : '';
		if ( '' !== $key ) {
			if ( isset( $seen_keys[ $key ] ) ) {
				$dup_keys[] = $key;
			}
			$seen_keys[ $key ] = true;
		}
		if ( ! empty( $f['conditional_logic'] ) && is_array( $f['conditional_logic'] ) ) {
			foreach ( $f['conditional_logic'] as $group ) {
				foreach ( (array) $group as $rule ) {
					if ( isset( $rule['field'] ) && 'field_fp02_service_editor_role' === $rule['field'] ) {
						++$cond_refs_role;
					}
				}
			}
		}
		if ( ! empty( $f['sub_fields'] ) ) {
			$walk( $f['sub_fields'] );
		}
	}
};
$walk( $parity_fields );

// DB ACF group posts related to parity / layout.
$acf_posts = get_posts(
	array(
		'post_type'      => 'acf-field-group',
		'post_status'    => array( 'publish', 'acf-disabled', 'draft', 'trash' ),
		'posts_per_page' => 100,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);
$db_groups = array();
foreach ( $acf_posts as $p ) {
	$title = (string) $p->post_title;
	$ex    = (string) $p->post_excerpt;
	if (
		false !== stripos( $title, 'Услуга' )
		|| false !== stripos( $title, 'Service' )
		|| false !== stripos( $ex, 'service' )
		|| false !== stripos( $title, 'Hero' )
		|| false !== stripos( $title, 'Макет' )
	) {
		$db_groups[] = array(
			'id'     => (int) $p->ID,
			'title'  => $title,
			'key'    => $ex,
			'status' => $p->post_status,
		);
	}
}

// Supports / metabox relevance.
$supports = array(
	'editor'     => post_type_supports( 'service', 'editor' ),
	'excerpt'    => post_type_supports( 'service', 'excerpt' ),
	'revisions'  => post_type_supports( 'service', 'revisions' ),
	'thumbnail'  => post_type_supports( 'service', 'thumbnail' ),
);

$diagnostics = array(
	array(
		'area'                 => 'nested_role_field',
		'finding'              => sprintf(
			'#74 parent=%d depth=%d nested=%s; prepare_editor_role_field type=%s name=%s',
			$parent,
			$depth,
			$nested ? 'yes' : 'no',
			is_array( $prepared ) && isset( $prepared['type'] ) ? $prepared['type'] : 'n/a',
			is_array( $prepared ) && isset( $prepared['name'] ) ? $prepared['name'] : 'n/a'
		),
		'root_cause_candidate' => 'Nested FIX03 converts service_editor_role to message with empty name; ACF JS conditionals referencing that field never match, so all Услуга fields stay hidden.',
		'confirmed'            => ( $nested && is_array( $prepared ) && isset( $prepared['type'] ) && 'message' === $prepared['type'] && $cond_refs_role > 0 ) ? 'yes' : 'no',
		'fix'                  => 'Remove when_service() conditionals from group_fp02_service_general_parity; rely on load_field_groups role filter.',
		'notes'                => sprintf( 'role_meta=%s role_acf=%s cond_refs_role=%d', $role_meta, $role_acf, $cond_refs_role ),
	),
	array(
		'area'                 => 'field_definitions',
		'finding'              => sprintf( 'parity top-level fields=%d; duplicate keys=%d', is_array( $parity_fields ) ? count( $parity_fields ) : 0, count( $dup_keys ) ),
		'root_cause_candidate' => 'Invalid/empty field array or duplicate keys',
		'confirmed'            => ( is_array( $parity_fields ) && count( $parity_fields ) >= 60 && 0 === count( $dup_keys ) ) ? 'no' : 'partial',
		'fix'                  => 'N/A if confirmed no',
		'notes'                => 'dup_keys=' . implode( '|', $dup_keys ),
	),
	array(
		'area'                 => 'acf_filters',
		'finding'              => sprintf( 'visible groups on #74: %d', count( $group_rows ) ),
		'root_cause_candidate' => 'load_field_groups filter strips fields or group',
		'confirmed'            => 'no',
		'fix'                  => 'Keep FIX01 filter; do not strip parity group for service role',
		'notes'                => wp_json_encode( $group_rows, JSON_UNESCAPED_UNICODE ),
	),
	array(
		'area'                 => 'db_acf_groups',
		'finding'              => sprintf( 'related acf-field-group posts: %d', count( $db_groups ) ),
		'root_cause_candidate' => 'soft-disabled parity group in DB',
		'confirmed'            => 'no',
		'fix'                  => 'N/A',
		'notes'                => wp_json_encode( $db_groups, JSON_UNESCAPED_UNICODE ),
	),
	array(
		'area'                 => 'cpt_supports',
		'finding'              => wp_json_encode( $supports ),
		'root_cause_candidate' => 'excerpt/revisions supports show default metaboxes',
		'confirmed'            => ( ! empty( $supports['excerpt'] ) || ! empty( $supports['revisions'] ) ) ? 'yes' : 'partial',
		'fix'                  => 'remove_meta_box revisionsdiv + postexcerpt on service CPT',
		'notes'                => 'EditorRestrictions currently removes comments/custom only',
	),
);

$csv = "area,finding,root_cause_candidate,confirmed yes/no,fix,notes\n";
foreach ( $diagnostics as $row ) {
	$csv .= sprintf(
		"\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n",
		str_replace( '"', '""', $row['area'] ),
		str_replace( '"', '""', $row['finding'] ),
		str_replace( '"', '""', $row['root_cause_candidate'] ),
		str_replace( '"', '""', $row['confirmed'] ),
		str_replace( '"', '""', $row['fix'] ),
		str_replace( '"', '""', $row['notes'] )
	);
}
file_put_contents( $evidence_dir . '/v9-06e47-fix02-acf-render-diagnostics.csv', $csv );
file_put_contents(
	$backup_admin . '/admin-groups-74-before.json',
	wp_json_encode(
		array(
			'post_id'      => $post_id,
			'role_meta'    => $role_meta,
			'role_acf'     => $role_acf,
			'parent'       => $parent,
			'depth'        => $depth,
			'nested'       => $nested,
			'prepared_role'=> array(
				'type' => is_array( $prepared ) && isset( $prepared['type'] ) ? $prepared['type'] : null,
				'name' => is_array( $prepared ) && isset( $prepared['name'] ) ? $prepared['name'] : null,
			),
			'groups'       => $group_rows,
			'cond_refs'    => $cond_refs_role,
			'supports'     => $supports,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
	)
);

echo "DIAG_OK nested=" . ( $nested ? '1' : '0' ) . " prepared_type=" . ( is_array( $prepared ) && isset( $prepared['type'] ) ? $prepared['type'] : '?' ) . " cond_refs=$cond_refs_role groups=" . count( $group_rows ) . " fields=" . ( is_array( $parity_fields ) ? count( $parity_fields ) : 0 ) . PHP_EOL;
