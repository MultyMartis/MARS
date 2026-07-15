<?php
/**
 * FP-0002 V9-06E29B-FIX — ACF probe + resync for institutional group.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$mode = isset( $argv[1] ) ? $argv[1] : 'probe';
$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$evidence = $root . '/validation/v9-06e29b-fix-ocentre-admin-ui-field-visibility';
$group_key = 'group_fp02_page_institutional';
$page_id = 11;

$required_hub_fields = array(
	'hero_eyebrow',
	'hero_title_override',
	'hero_lead',
	'hero_media',
	'hero_cta_label',
	'about_narrative_heading',
	'about_narrative_lead',
	'about_narrative_paragraphs',
	'about_founder_quote_paragraphs',
	'about_founder_name',
	'about_founder_role',
	'about_founder_photo',
	'about_founder_cta_label',
	'about_clinic_landscape_image',
	'about_clinic_landscape_alt',
	'about_who_treat_heading',
	'about_approach_heading',
	'about_program_heading',
	'infrastructure_g0_g5',
);

$message_fields = array(
	'about_hub_admin_overview',
	'about_hub_admin_note_shared_blocks',
	'about_hub_admin_note_cta_phone',
);

function fp02_fix_flatten_fields( $fields, &$out = array() ) {
	if ( ! is_array( $fields ) ) {
		return $out;
	}
	foreach ( $fields as $field ) {
		if ( ! is_array( $field ) ) {
			continue;
		}
		$name = $field['name'] ?? '';
		$type = $field['type'] ?? '';
		if ( $name || 'message' === $type ) {
			$out[] = array(
				'key'   => $field['key'] ?? '',
				'name'  => $name,
				'label' => $field['label'] ?? '',
				'type'  => $type,
			);
		}
		if ( ! empty( $field['sub_fields'] ) && is_array( $field['sub_fields'] ) ) {
			fp02_fix_flatten_fields( $field['sub_fields'], $out );
		}
	}
	return $out;
}

function fp02_fix_message_names_from_json( $json_path ) {
	if ( ! is_readable( $json_path ) ) {
		return array();
	}
	$raw = json_decode( file_get_contents( $json_path ), true );
	$names = array();
	if ( ! empty( $raw['fields'] ) && is_array( $raw['fields'] ) ) {
		foreach ( fp02_fix_flatten_fields( $raw['fields'] ) as $field ) {
			if ( 'message' === ( $field['type'] ?? '' ) && ! empty( $field['name'] ) ) {
				$names[] = $field['name'];
			}
		}
	}
	return $names;
}

function fp02_fix_probe_group( $group_key, $page_id, $required, $messages ) {
	$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
	$flat = fp02_fix_flatten_fields( (array) $fields );
	$names = array_values( array_unique( array_filter( array_column( $flat, 'name' ) ) ) );
	$json_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/' . $group_key . '.json';
	foreach ( fp02_fix_message_names_from_json( $json_path ) as $message_name ) {
		if ( ! in_array( $message_name, $names, true ) ) {
			$names[] = $message_name;
		}
	}
	$missing = array();
	foreach ( array_merge( $required, $messages ) as $name ) {
		if ( ! in_array( $name, $names, true ) ) {
			$missing[] = $name;
		}
	}
	$hidden_on_hub = array();
	foreach ( array( 'institutional_content_sections', 'institutional_stages', 'institutional_placeholder_notice' ) as $name ) {
		$hidden_on_hub[] = array(
			'name'    => $name,
			'present' => in_array( $name, $names, true ),
		);
	}
	$groups_for_page = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $page_id ) ) : array();
	$page_group_keys = array();
	foreach ( (array) $groups_for_page as $g ) {
		$page_group_keys[] = $g['key'] ?? '';
	}
	return array(
		'group_exists'        => is_array( $group ),
		'group_key'           => $group_key,
		'group_title'         => is_array( $group ) ? ( $group['title'] ?? '' ) : '',
		'group_id'            => is_array( $group ) ? ( $group['ID'] ?? null ) : null,
		'field_count_top'     => is_array( $fields ) ? count( $fields ) : 0,
		'field_count_flat'    => count( $flat ),
		'visible_field_names' => $names,
		'missing_required'    => $missing,
		'child_only_fields'   => $hidden_on_hub,
		'page_11_group_keys'  => $page_group_keys,
		'institutional_on_page_11' => in_array( $group_key, $page_group_keys, true ),
		'result'              => empty( $missing ) ? 'PASS' : 'FAIL',
	);
}

if ( 'probe' === $mode ) {
	$out = fp02_fix_probe_group( $group_key, $page_id, $required_hub_fields, $message_fields );
	file_put_contents(
		$evidence . '/_acf_probe_output.json',
		wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n"
	);
	echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE ) . "\n";
	exit( 'PASS' === $out['result'] ? 0 : 1 );
}

if ( 'resync' === $mode ) {
	$json_dir     = $root . '/acf-json/';
	$runtime_json = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/';
	$export       = null;

	if ( class_exists( '\Shpigovsky\Core\Fields\FieldGroups' ) && method_exists( '\Shpigovsky\Core\Fields\FieldGroups', 'get_field_groups' ) ) {
		foreach ( \Shpigovsky\Core\Fields\FieldGroups::get_field_groups() as $group ) {
			if ( ( $group['key'] ?? '' ) === $group_key ) {
				$export = $group;
				break;
			}
		}
	}

	if ( ! is_array( $export ) ) {
		$export = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
		if ( is_array( $export ) ) {
			$export['fields'] = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
		}
	}

	if ( ! is_array( $export ) ) {
		fwrite( STDERR, "group missing\n" );
		exit( 1 );
	}

	unset( $export['ID'] );
	$path = $json_dir . $group_key . '.json';
	file_put_contents( $path, wp_json_encode( $export, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	if ( ! is_dir( $runtime_json ) ) {
		mkdir( $runtime_json, 0777, true );
	}
	copy( $path, $runtime_json . $group_key . '.json' );

	$deleted = array();
	$db_group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
	if ( is_array( $db_group ) && ! empty( $db_group['ID'] ) ) {
		$db_fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $db_group['key'] ) : array();
		if ( is_array( $db_fields ) ) {
			foreach ( $db_fields as $field ) {
				if ( ! empty( $field['ID'] ) ) {
					acf_delete_field( $field['ID'] );
					$deleted[] = 'field:' . ( $field['name'] ?? '' );
				}
				if ( ! empty( $field['sub_fields'] ) && is_array( $field['sub_fields'] ) ) {
					foreach ( $field['sub_fields'] as $sub ) {
						if ( ! empty( $sub['ID'] ) ) {
							acf_delete_field( $sub['ID'] );
							$deleted[] = 'subfield:' . ( $sub['name'] ?? '' );
						}
					}
				}
			}
		}
		acf_delete_field_group( $db_group['ID'] );
		$deleted[] = 'group:' . $group_key;
	}

	$import_ok = false;
	if ( function_exists( 'acf_import_field_group' ) ) {
		$import_ok = (bool) acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
	}

	$after = fp02_fix_probe_group( $group_key, $page_id, $required_hub_fields, $message_fields );
	$out   = array(
		'mode'          => 'resync',
		'source'        => 'FieldGroups::get_field_groups',
		'source_json'   => $path,
		'runtime_json'  => $runtime_json . $group_key . '.json',
		'deleted_db'    => $deleted,
		'import_ok'     => $import_ok,
		'field_count'   => $after['field_count_top'],
		'missing_after' => $after['missing_required'],
		'probe_after'   => $after,
		'result'        => $import_ok && 'PASS' === $after['result'] ? 'PASS' : 'FAIL',
	);
	file_put_contents(
		$evidence . '/_acf_resync_output.json',
		wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n"
	);
	echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE ) . "\n";
	exit( 'PASS' === $out['result'] ? 0 : 1 );
}

fwrite( STDERR, "unknown mode\n" );
exit( 1 );
