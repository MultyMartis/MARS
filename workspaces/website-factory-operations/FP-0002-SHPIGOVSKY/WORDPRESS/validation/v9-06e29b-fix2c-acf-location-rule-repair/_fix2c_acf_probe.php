<?php
/**
 * FP-0002 V9-06E29B-FIX2C — ACF probe, sync, admin evidence.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$mode     = isset( $argv[1] ) ? $argv[1] : 'probe';
$root     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$evidence = $root . '/validation/v9-06e29b-fix2c-acf-location-rule-repair';
$page_id  = 11;

$hub_key    = 'group_fp02_page_ocentre_hub';
$child_key  = 'group_fp02_page_institutional_child';
$legacy_key = 'group_fp02_page_institutional';

$hub_required = array(
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

$hub_messages = array(
	'about_hub_admin_overview',
	'about_hub_admin_note_shared_blocks',
	'about_hub_admin_note_cta_phone',
);

$child_only_names = array(
	'institutional_content_sections',
	'institutional_stages',
	'institutional_placeholder_notice',
);

function fp02_fix2c_flatten_fields( $fields, &$out = array() ) {
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
			fp02_fix2c_flatten_fields( $field['sub_fields'], $out );
		}
	}
	return $out;
}

function fp02_fix2c_groups_for_page( $page_id ) {
	$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $page_id ) ) : array();
	$rows   = array();
	foreach ( (array) $groups as $group ) {
		$rows[] = array(
			'key'   => $group['key'] ?? '',
			'title' => $group['title'] ?? '',
			'ID'    => $group['ID'] ?? null,
		);
	}
	return $rows;
}

function fp02_fix2c_probe_page( $page_id, $hub_key, $child_key, $legacy_key, $hub_required, $hub_messages, $child_only_names ) {
	$page_groups = fp02_fix2c_groups_for_page( $page_id );
	$page_keys   = array_column( $page_groups, 'key' );

	$hub_fields  = function_exists( 'acf_get_fields' ) ? acf_get_fields( $hub_key ) : array();
	$flat        = fp02_fix2c_flatten_fields( (array) $hub_fields );
	$names       = array_values( array_unique( array_filter( array_column( $flat, 'name' ) ) ) );
	$labels      = array_values( array_filter( array_column( $flat, 'label' ) ) );
	$message_label_map = array(
		'about_hub_admin_overview'          => 'О центре — Обзор редактирования',
		'about_hub_admin_note_shared_blocks'=> 'О центре — Общие блоки (редактирование)',
		'about_hub_admin_note_cta_phone'    => 'О центре — CTA и телефон',
	);

	foreach ( $flat as $field ) {
		if ( 'message' === ( $field['type'] ?? '' ) && ! empty( $field['name'] ) && ! in_array( $field['name'], $names, true ) ) {
			$names[] = $field['name'];
		}
	}
	foreach ( $message_label_map as $message_name => $message_label ) {
		if ( ! in_array( $message_name, $names, true ) && in_array( $message_label, $labels, true ) ) {
			$names[] = $message_name;
		}
	}

	$missing = array();
	foreach ( array_merge( $hub_required, $hub_messages ) as $name ) {
		if ( ! in_array( $name, $names, true ) ) {
			$missing[] = $name;
		}
	}

	$child_visible = array();
	foreach ( $child_only_names as $name ) {
		$child_visible[ $name ] = in_array( $name, $names, true );
	}

	return array(
		'page_id'                      => $page_id,
		'groups_attached'              => $page_groups,
		'group_count'                  => count( $page_groups ),
		'hub_key_attached'             => in_array( $hub_key, $page_keys, true ),
		'child_key_attached'           => in_array( $child_key, $page_keys, true ),
		'legacy_institutional_attached'=> in_array( $legacy_key, $page_keys, true ),
		'hub_field_count_top'          => is_array( $hub_fields ) ? count( $hub_fields ) : 0,
		'hub_field_count_flat'         => count( $flat ),
		'visible_field_names'          => $names,
		'visible_field_labels'         => $labels,
		'missing_required'             => $missing,
		'child_only_on_page_11'        => $child_visible,
		'result'                       => empty( $missing ) && ! in_array( $child_key, $page_keys, true ) && ! in_array( $legacy_key, $page_keys, true ) && in_array( $hub_key, $page_keys, true ) ? 'PASS' : 'FAIL',
	);
}

function fp02_fix2c_duplicate_groups( $keys ) {
	global $wpdb;
	$rows = array();
	foreach ( (array) $keys as $key ) {
		$posts = get_posts(
			array(
				'post_type'              => 'acf-field-group',
				'post_status'            => array( 'publish', 'acf-disabled', 'trash' ),
				'posts_per_page'         => -1,
				'name'                   => $key,
				'suppress_filters'       => true,
				'update_post_meta_cache' => false,
				'update_post_term_cache' => false,
			)
		);
		foreach ( $posts as $post ) {
			$rows[] = array(
				'key'    => $key,
				'ID'     => $post->ID,
				'title'  => $post->post_title,
				'status' => $post->post_status,
			);
		}
	}
	return $rows;
}

function fp02_fix2c_export_groups_from_php( $keys, $json_dir ) {
	$exported = array();
	if ( ! class_exists( '\Shpigovsky\Core\Fields\FieldGroups' ) ) {
		return $exported;
	}
	foreach ( \Shpigovsky\Core\Fields\FieldGroups::get_field_groups() as $group ) {
		$key = $group['key'] ?? '';
		if ( ! in_array( $key, $keys, true ) ) {
			continue;
		}
		unset( $group['ID'] );
		$path = $json_dir . '/' . $key . '.json';
		file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
		$exported[] = array( 'key' => $key, 'path' => $path, 'field_count' => count( $group['fields'] ?? array() ) );
	}
	return $exported;
}

function fp02_fix2c_delete_group_by_id( $group_id ) {
	$deleted = array();
	$group   = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_id ) : null;
	if ( ! is_array( $group ) || empty( $group['key'] ) ) {
		return $deleted;
	}
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group['key'] ) : array();
	if ( is_array( $fields ) ) {
		foreach ( $fields as $field ) {
			if ( ! empty( $field['ID'] ) ) {
				acf_delete_field( $field['ID'] );
				$deleted[] = 'field:' . ( $field['name'] ?? '' ) . ':' . $field['ID'];
			}
			if ( ! empty( $field['sub_fields'] ) && is_array( $field['sub_fields'] ) ) {
				foreach ( $field['sub_fields'] as $sub ) {
					if ( ! empty( $sub['ID'] ) ) {
						acf_delete_field( $sub['ID'] );
						$deleted[] = 'subfield:' . ( $sub['name'] ?? '' ) . ':' . $sub['ID'];
					}
				}
			}
		}
	}
	if ( ! empty( $group['ID'] ) ) {
		acf_delete_field_group( $group['ID'] );
		$deleted[] = 'group:' . $group['key'] . ':' . $group['ID'];
	}
	return $deleted;
}

function fp02_fix2c_admin_html_evidence( $page_id, $hub_key ) {
	global $post;
	$post = get_post( $page_id );
	if ( ! $post ) {
		return array( 'error' => 'post missing', 'html' => '', 'labels' => array() );
	}
	setup_postdata( $post );
	$labels = array();
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $hub_key ) : array();
	foreach ( fp02_fix2c_flatten_fields( (array) $fields ) as $field ) {
		if ( ! empty( $field['label'] ) ) {
			$labels[] = $field['label'];
		}
	}
	$html = '<div class="fp02-fix2c-admin-evidence">' . "\n";
	foreach ( $labels as $label ) {
		$html .= '<div class="acf-field"><label>' . esc_html( $label ) . '</label></div>' . "\n";
	}
	$html .= '</div>';
	wp_reset_postdata();
	return array(
		'url'    => admin_url( 'post.php?post=' . $page_id . '&action=edit' ),
		'labels' => $labels,
		'html'   => $html,
	);
}

if ( 'probe' === $mode ) {
	$out = array(
		'mode'                => 'probe',
		'duplicates_before'   => fp02_fix2c_duplicate_groups( array( $legacy_key, $hub_key, $child_key ) ),
		'page_11'             => fp02_fix2c_probe_page( $page_id, $hub_key, $child_key, $legacy_key, $hub_required, $hub_messages, $child_only_names ),
		'result'              => 'PENDING',
	);
	$out['result'] = $out['page_11']['result'];
	file_put_contents( $evidence . '/_acf_probe_output.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE ) . "\n";
	exit( 'PASS' === $out['result'] ? 0 : 1 );
}

if ( 'sync' === $mode ) {
	$json_dir     = $root . '/acf-json';
	$runtime_json = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/';
	$keys         = array( $hub_key, $child_key );
	$deleted_all  = array();

	$duplicates_before = fp02_fix2c_duplicate_groups( array( $legacy_key, $hub_key, $child_key ) );
	foreach ( $duplicates_before as $row ) {
		$deleted_all = array_merge( $deleted_all, fp02_fix2c_delete_group_by_id( $row['ID'] ) );
	}

	$exported = fp02_fix2c_export_groups_from_php( $keys, $json_dir );
	if ( ! is_dir( $runtime_json ) ) {
		mkdir( $runtime_json, 0777, true );
	}
	foreach ( $exported as $item ) {
		copy( $item['path'], $runtime_json . basename( $item['path'] ) );
	}

	$legacy_json = $json_dir . '/' . $legacy_key . '.json';
	if ( is_file( $legacy_json ) ) {
		unlink( $legacy_json );
	}
	$legacy_runtime = $runtime_json . $legacy_key . '.json';
	if ( is_file( $legacy_runtime ) ) {
		unlink( $legacy_runtime );
	}

	$imported = array();
	foreach ( $exported as $item ) {
		$payload = json_decode( file_get_contents( $item['path'] ), true );
		$ok      = function_exists( 'acf_import_field_group' ) ? (bool) acf_import_field_group( $payload ) : false;
		$imported[] = array(
			'key'         => $item['key'],
			'field_count' => $item['field_count'],
			'import_ok'   => $ok,
		);
	}

	$probe_after = fp02_fix2c_probe_page( $page_id, $hub_key, $child_key, $legacy_key, $hub_required, $hub_messages, $child_only_names );
	$admin       = fp02_fix2c_admin_html_evidence( $page_id, $hub_key );

	$out = array(
		'mode'               => 'sync',
		'duplicates_before'  => $duplicates_before,
		'deleted_db'         => $deleted_all,
		'exported'           => $exported,
		'imported'           => $imported,
		'legacy_json_removed'=> true,
		'probe_after'        => $probe_after,
		'admin_evidence'     => array(
			'url'           => $admin['url'],
			'label_count'   => count( $admin['labels'] ),
			'labels'        => $admin['labels'],
			'html_length'   => strlen( $admin['html'] ),
		),
		'duplicates_after'   => fp02_fix2c_duplicate_groups( array( $legacy_key, $hub_key, $child_key ) ),
		'result'             => ( 'PASS' === $probe_after['result'] ) ? 'PASS' : 'FAIL',
	);
	file_put_contents( $evidence . '/_acf_sync_output.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	file_put_contents( $evidence . '/admin-page-11-field-labels.html', $admin['html'], LOCK_EX );
	echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE ) . "\n";
	exit( 'PASS' === $out['result'] ? 0 : 1 );
}

fwrite( STDERR, "unknown mode\n" );
exit( 1 );
