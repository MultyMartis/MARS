<?php
/**
 * V9-06E38-FIX01: Home admin orphan hygiene + duplicate ACF group cleanup.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e38-fix01-home-admin-orphan-hygiene';
$report_ev = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$bak = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e38-fix01-home-admin-orphan-hygiene-before-20260713-193615';
$runtime_acf = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json';
$source_acf  = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json';
$runtime_plugin = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php';
$source_plugin  = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php';

$out = array(
	'phase' => 'v9-06e38-fix01',
	'home_id' => (int) get_option( 'page_on_front' ),
	'db_writes' => 0,
	'groups_before' => array(),
	'groups_trashed' => array(),
	'fields_trashed' => array(),
	'json_export' => array(),
	'sync' => array(),
	'admin_fields_after' => array(),
	'validation' => array(),
	'classification' => array(),
);

$home_id = $out['home_id'] > 0 ? $out['home_id'] : 4;

// Sync source FieldGroups.php → runtime (runtime may still be pre-edit).
if ( is_readable( $source_plugin ) ) {
	$src_hash = hash_file( 'sha256', $source_plugin );
	$copied = copy( $source_plugin, $runtime_plugin );
	$out['sync']['FieldGroups.php'] = array(
		'copied' => (bool) $copied,
		'source_hash' => $src_hash,
		'runtime_hash' => is_readable( $runtime_plugin ) ? hash_file( 'sha256', $runtime_plugin ) : null,
		'match' => is_readable( $runtime_plugin ) && hash_file( 'sha256', $runtime_plugin ) === $src_hash,
	);
}

// Export Home group JSON from PHP FieldGroups (after sync; re-require class already loaded — use reflection of registered definition).
$home_group = null;
if ( class_exists( '\\Shpigovsky\\Core\\Fields\\FieldGroups' ) ) {
	// Class already loaded from runtime at bootstrap — force re-read by evaluating source file definitions is hard.
	// Prefer parsing via get_field_groups if runtime file was updated BEFORE wp-load.
	// If mismatch, re-bootstrap note.
	foreach ( \Shpigovsky\Core\Fields\FieldGroups::get_field_groups() as $group ) {
		if ( ( $group['key'] ?? '' ) === 'group_fp02_page_home' ) {
			$home_group = $group;
			break;
		}
	}
}

$out['sync']['home_group_has_faq_heading'] = false;
$out['sync']['home_group_has_blog_teaser'] = false;
if ( is_array( $home_group ) ) {
	foreach ( $home_group['fields'] as $f ) {
		if ( ( $f['name'] ?? '' ) === 'home_faq_heading' ) {
			$out['sync']['home_group_has_faq_heading'] = true;
		}
		if ( ( $f['name'] ?? '' ) === 'home_blog_teaser_enabled' ) {
			$out['sync']['home_group_has_blog_teaser'] = true;
		}
	}
	$json = wp_json_encode( $home_group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
	foreach ( array( $runtime_acf, $source_acf, $bak . '/exports' ) as $dir ) {
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}
		$path = rtrim( $dir, '/\\' ) . '/group_fp02_page_home.json';
		file_put_contents( $path, $json . "\n" );
		$out['json_export'][] = $path;
	}
}

// Inventory Home DB groups before trash.
$group_q = new WP_Query( array(
	'post_type' => 'acf-field-group',
	'post_status' => 'any',
	'posts_per_page' => -1,
	'name' => 'group_fp02_page_home',
	'orderby' => 'ID',
	'order' => 'ASC',
) );
foreach ( $group_q->posts as $g ) {
	$out['groups_before'][] = array(
		'ID' => (int) $g->ID,
		'title' => $g->post_title,
		'status' => $g->post_status,
		'name' => $g->post_name,
	);
}

// Canonical keep: newest publish group (639 expected). Trash older publish duplicates.
$publish_ids = array();
foreach ( $group_q->posts as $g ) {
	if ( 'publish' === $g->post_status ) {
		$publish_ids[] = (int) $g->ID;
	}
}
sort( $publish_ids );
$keep_id = $publish_ids ? max( $publish_ids ) : 0;
$out['canonical_db_group_keep'] = $keep_id;

/**
 * Recursively trash acf-field children.
 */
function e38fix01_trash_field_tree( $parent_id, &$out ) {
	$children = get_posts( array(
		'post_type' => 'acf-field',
		'post_status' => 'any',
		'posts_per_page' => -1,
		'post_parent' => (int) $parent_id,
		'orderby' => 'ID',
		'order' => 'ASC',
	) );
	foreach ( $children as $child ) {
		e38fix01_trash_field_tree( $child->ID, $out );
		if ( 'trash' === $child->post_status ) {
			$out['fields_trashed'][] = array( 'ID' => (int) $child->ID, 'name' => $child->post_excerpt, 'action' => 'already_trash' );
			continue;
		}
		$ok = (bool) wp_trash_post( $child->ID );
		if ( $ok ) {
			$out['db_writes']++;
		}
		$out['fields_trashed'][] = array(
			'ID' => (int) $child->ID,
			'name' => $child->post_excerpt,
			'title' => $child->post_title,
			'parent' => (int) $parent_id,
			'action' => $ok ? 'trash' : 'fail',
		);
	}
}

foreach ( $publish_ids as $gid ) {
	if ( $gid === $keep_id ) {
		continue;
	}
	e38fix01_trash_field_tree( $gid, $out );
	$g = get_post( $gid );
	if ( $g && 'trash' !== $g->post_status ) {
		$ok = (bool) wp_trash_post( $gid );
		if ( $ok ) {
			$out['db_writes']++;
		}
		$out['groups_trashed'][] = array( 'ID' => $gid, 'action' => $ok ? 'trash' : 'fail' );
	} else {
		$out['groups_trashed'][] = array( 'ID' => $gid, 'action' => 'already_trash' );
	}
}

// On kept group: retire dead fields (blog teaser, and any still-published fallback-only headings we intentionally hide from PHP).
$retire_names = array(
	'home_blog_teaser_enabled',
	'home_specialists_heading',
	'home_comfort_heading',
	'home_comfort_lead',
	'home_reviews_heading',
);
if ( $keep_id ) {
	$keep_fields = get_posts( array(
		'post_type' => 'acf-field',
		'post_status' => 'any',
		'posts_per_page' => -1,
		'post_parent' => $keep_id,
	) );
	foreach ( $keep_fields as $fp ) {
		if ( in_array( $fp->post_excerpt, $retire_names, true ) && 'trash' !== $fp->post_status ) {
			e38fix01_trash_field_tree( $fp->ID, $out );
			$ok = (bool) wp_trash_post( $fp->ID );
			if ( $ok ) {
				$out['db_writes']++;
			}
			$out['fields_trashed'][] = array(
				'ID' => (int) $fp->ID,
				'name' => $fp->post_excerpt,
				'title' => $fp->post_title,
				'parent' => $keep_id,
				'action' => $ok ? 'trash_on_keep' : 'fail',
			);
		}
	}
}

// Also trash any leftover publish fields with retire names under ANY home group (including already-trashed parents — safety).
$orphan_field_q = new WP_Query( array(
	'post_type' => 'acf-field',
	'post_status' => 'publish',
	'posts_per_page' => -1,
	'meta_query' => array(),
) );
foreach ( $orphan_field_q->posts as $fp ) {
	if ( ! in_array( $fp->post_excerpt, $retire_names, true ) ) {
		continue;
	}
	$parent = get_post( $fp->post_parent );
	$parent_is_home = $parent && ( 'group_fp02_page_home' === $parent->post_name || false !== strpos( (string) $parent->post_name, 'group_fp02_page_home' ) );
	// Also match by parent title.
	if ( ! $parent_is_home && $parent ) {
		$parent_is_home = ( false !== stripos( $parent->post_title, 'Home' ) );
	}
	if ( ! $parent_is_home ) {
		continue;
	}
	e38fix01_trash_field_tree( $fp->ID, $out );
	$ok = (bool) wp_trash_post( $fp->ID );
	if ( $ok ) {
		$out['db_writes']++;
	}
	$out['fields_trashed'][] = array(
		'ID' => (int) $fp->ID,
		'name' => $fp->post_excerpt,
		'action' => $ok ? 'trash_residual' : 'fail',
	);
}

// Admin field inventory AFTER via local group definition + acf_get_field_groups.
if ( function_exists( 'acf_get_field_groups' ) ) {
	$groups = acf_get_field_groups( array( 'page_type' => 'front_page' ) );
	foreach ( $groups as $g ) {
		$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $g['key'] ) : array();
		$names = array();
		if ( is_array( $fields ) ) {
			foreach ( $fields as $f ) {
				$names[] = $f['name'] ?? '';
			}
		}
		$out['admin_fields_after'][] = array(
			'key' => $g['key'] ?? '',
			'title' => $g['title'] ?? '',
			'ID' => $g['ID'] ?? 0,
			'local' => $g['local'] ?? '',
			'fields' => $names,
		);
	}
}

// Groups after
$group_after = new WP_Query( array(
	'post_type' => 'acf-field-group',
	'post_status' => array( 'publish', 'trash' ),
	'posts_per_page' => -1,
	'name' => 'group_fp02_page_home',
	'orderby' => 'ID',
	'order' => 'ASC',
) );
$out['groups_after'] = array();
foreach ( $group_after->posts as $g ) {
	$out['groups_after'][] = array( 'ID' => (int) $g->ID, 'status' => $g->post_status );
}

// Validation: meta preserved
$check_metas = array(
	'home_faq_heading',
	'home_recovery_intro_heading',
	'home_recovery_intro_lead_1',
	'home_recovery_intro_lead_2',
	'home_articles_heading',
	'home_specialists_heading',
	'home_comfort_heading',
	'home_comfort_lead',
	'home_reviews_heading',
	'home_blog_teaser_enabled',
);
$out['meta_preserved'] = array();
foreach ( $check_metas as $k ) {
	$v = get_post_meta( $home_id, $k, true );
	$out['meta_preserved'][ $k ] = array(
		'empty' => ( '' === $v || null === $v ),
		'preview' => is_string( $v ) ? mb_substr( $v, 0, 80 ) : $v,
	);
}

// Local field presence checks
$want_visible = array( 'home_faq_heading', 'home_recovery_intro_heading', 'home_recovery_intro_lead_1', 'home_recovery_intro_lead_2', 'home_articles_heading', 'home_gallery_source_notice', 'home_faq_items' );
$want_absent = array( 'home_blog_teaser_enabled', 'home_gallery_media', 'home_reviews_teaser', 'home_specialists_heading', 'home_comfort_heading', 'home_comfort_lead', 'home_reviews_heading' );
$flat_names = array();
foreach ( $out['admin_fields_after'] as $g ) {
	foreach ( $g['fields'] as $n ) {
		$flat_names[] = $n;
	}
}
$out['validation']['visible_fields'] = array();
foreach ( $want_visible as $n ) {
	$out['validation']['visible_fields'][ $n ] = in_array( $n, $flat_names, true ) ? 'PASS' : 'FAIL';
}
$out['validation']['absent_fields'] = array();
foreach ( $want_absent as $n ) {
	$out['validation']['absent_fields'][ $n ] = in_array( $n, $flat_names, true ) ? 'FAIL_STILL_VISIBLE' : 'PASS';
}
$publish_after = array_values( array_filter( $out['groups_after'], function( $g ) { return 'publish' === $g['status']; } ) );
$out['validation']['publish_home_groups_count'] = count( $publish_after );
$out['validation']['duplicate_groups_cleaned'] = count( $publish_after ) <= 1 ? 'PASS' : 'FAIL';

// Save probe (no content change): touch updated date? skip — just check acf validation map.
$out['validation']['home_group_php_blog_teaser_absent'] = empty( $out['sync']['home_group_has_blog_teaser'] ) ? 'PASS' : 'FAIL';
$out['validation']['home_group_php_faq_heading_present'] = ! empty( $out['sync']['home_group_has_faq_heading'] ) ? 'PASS' : 'FAIL';

@file_put_contents( $out_dir . '/e38fix01-result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
@file_put_contents( $bak . '/exports/e38fix01-result.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo wp_json_encode( array(
	'db_writes' => $out['db_writes'],
	'keep' => $keep_id,
	'trashed_groups' => $out['groups_trashed'],
	'publish_after' => $publish_after,
	'faq_heading' => $out['validation']['home_group_php_faq_heading_present'] ?? null,
	'blog_teaser' => $out['validation']['home_group_php_blog_teaser_absent'] ?? null,
	'visible' => $out['validation']['visible_fields'],
	'absent' => $out['validation']['absent_fields'],
	'sync_match' => $out['sync']['FieldGroups.php']['match'] ?? null,
	'admin_groups' => count( $out['admin_fields_after'] ),
), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
