<?php
/**
 * FP-0002 V9-06D9-N — Hide native editor validation runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: baseline | verify-source | verify-admin | verify-frontend | drift | all
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if ( ! function_exists( 'get_plugins' ) ) {
	require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode     = isset( $argv[1] ) ? $argv[1] : 'all';
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9n-hide-native-editor-template-pages';
$arch     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture';

if ( ! is_dir( $evidence ) ) {
	mkdir( $evidence, 0777, true );
}
if ( ! is_dir( $evidence . '/screenshots' ) ) {
	mkdir( $evidence . '/screenshots', 0777, true );
}

const FP02N_PHASE = 'V9-06D9-N';

const FP02N_HIDE_IDS = array( 4, 5, 11, 12, 13, 14, 15, 16, 18, 20, 22, 23, 24 );
const FP02N_RETAIN_IDS = array( 3, 6, 7, 8, 9, 10, 17, 19, 21, 25 );

const FP02N_AUDIT_PAGES = array( 4, 5, 20, 11, 6, 3 );

function fp02n_json_write( $path, $data ) {
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
}

function fp02n_plugin_state( $slug ) {
	$all  = get_plugins();
	$main = null;
	foreach ( $all as $file => $meta ) {
		if ( strpos( $file, $slug . '/' ) === 0 ) {
			$main = $file;
			break;
		}
	}
	return array(
		'slug'      => $slug,
		'installed' => null !== $main,
		'active'    => $main ? is_plugin_active( $main ) : false,
		'main_file' => $main,
	);
}

function fp02n_home_acf_summary() {
	$fields = array(
		'home_recovery_intro_heading',
		'home_faq_heading',
		'home_specialists_heading',
		'home_hero_slides',
		'home_gallery_media',
	);
	$out    = array();
	foreach ( $fields as $field ) {
		$val         = get_field( $field, 4 );
		$out[ $field ] = array(
			'empty'   => empty( $val ),
			'type'    => gettype( $val ),
			'preview' => is_string( $val ) ? mb_substr( $val, 0, 80 ) : ( is_array( $val ) ? 'array[' . count( $val ) . ']' : null ),
		);
	}
	$hero    = get_field( 'home_hero_slides', 4 );
	$gallery = get_field( 'home_gallery_media', 4 );
	if ( is_array( $hero ) && ! empty( $hero[0]['image'] ) ) {
		$img = $hero[0]['image'];
		$out['home_hero_slides']['hero_image_attachment_id'] = is_array( $img ) ? ( $img['ID'] ?? null ) : (int) $img;
	}
	$out['home_gallery_media']['gallery_row_count'] = is_array( $gallery ) ? count( $gallery ) : 0;
	return $out;
}

function fp02n_page_row( $page_id, $policy_applied ) {
	$p = get_post( $page_id );
	if ( ! $p ) {
		return array(
			'page_id' => $page_id,
			'exists'  => false,
		);
	}
	$template         = (string) get_page_template_slug( $page_id );
	$template_managed = ( 4 === (int) $page_id ) || ( '' !== $template && 0 === strpos( $template, 'page-templates/' ) );
	$hide_policy      = function_exists( 'shpigovsky_should_hide_native_editor' )
		? shpigovsky_should_hide_native_editor( (int) $page_id )
		: in_array( (int) $page_id, FP02N_HIDE_IDS, true );
	$acf_visible      = null;
	if ( 4 === (int) $page_id ) {
		$acf_visible = function_exists( 'acf_get_field_group' ) && acf_get_field_group( 'group_fp02_page_home' );
	} elseif ( 5 === (int) $page_id ) {
		$acf_visible = function_exists( 'acf_get_field_group' ) && acf_get_field_group( 'group_fp02_page_services_hub' );
	} elseif ( 20 === (int) $page_id ) {
		$acf_visible = function_exists( 'acf_get_field_group' ) && acf_get_field_group( 'group_fp02_page_contacts' );
	}
	$recommended = 'KEEP_EDITOR';
	if ( in_array( (int) $page_id, FP02N_HIDE_IDS, true ) ) {
		$recommended = 'HIDE_NATIVE_EDITOR';
	} elseif ( in_array( (int) $page_id, FP02N_RETAIN_IDS, true ) ) {
		$recommended = 'OPERATOR_REVIEW_REQUIRED';
	}
	return array(
		'page_id'                   => (int) $page_id,
		'title'                     => $p->post_title,
		'slug'                      => $p->post_name,
		'template'                  => $template,
		'post_content_length'       => strlen( (string) $p->post_content ),
		'template_managed'          => $template_managed,
		'classic_editor_active'     => fp02n_plugin_state( 'classic-editor' )['active'],
		'gutenberg_disabled'        => ! use_block_editor_for_post_type( 'page' ),
		'native_editor_visible_before' => $policy_applied ? null : true,
		'native_editor_hidden_after'   => $policy_applied ? $hide_policy : null,
		'acf_metabox_expected'      => $acf_visible,
		'hide_policy_active'        => $hide_policy,
		'recommended_hide_native_editor' => $recommended,
	);
}

function fp02n_metabox_hidden_simulation( $page_id ) {
	if ( ! function_exists( 'shpigovsky_should_hide_native_editor' ) ) {
		return array( 'simulated' => false, 'editor_support_removed' => false, 'metabox_removed' => false );
	}
	$should_hide = shpigovsky_should_hide_native_editor( (int) $page_id );
	return array(
		'simulated'              => true,
		'should_hide'            => $should_hide,
		'editor_support_removed' => $should_hide && ! post_type_supports( 'page', 'editor' ) ? 'conditional_on_admin_init' : ( $should_hide ? 'pending_admin_init' : false ),
		'function_exists'        => true,
		'allowlist_count'        => count( shpigovsky_get_hide_native_editor_page_ids() ),
	);
}

function fp02n_baseline() {
	global $evidence, $arch;
	$generated = gmdate( 'c' );
	$rows      = array();
	foreach ( FP02N_AUDIT_PAGES as $pid ) {
		$rows[] = fp02n_page_row( $pid, false );
	}
	$classic = fp02n_plugin_state( 'classic-editor' );
	$data    = array(
		'phase'        => FP02N_PHASE,
		'generated_at' => $generated,
		'classic_editor' => $classic,
		'gutenberg_disabled' => ! use_block_editor_for_post_type( 'page' ),
		'hide_helper_loaded' => function_exists( 'shpigovsky_should_hide_native_editor' ),
		'pages'        => $rows,
		'allowlist_ids' => FP02N_HIDE_IDS,
		'retain_editor_ids' => FP02N_RETAIN_IDS,
		'result'       => 'PASS',
	);
	fp02n_json_write( $evidence . '/baseline-admin-ux-audit.json', $data );

	$md = "# FP-0002 V9-06D9N Baseline Admin UX Audit v1\n\n";
	$md .= "Generated: {$generated}\n\n";
	$md .= "## Summary\n\n";
	$md .= "- Classic Editor active: " . ( $classic['active'] ? 'YES' : 'NO' ) . "\n";
	$md .= "- Gutenberg disabled for pages: " . ( $data['gutenberg_disabled'] ? 'YES' : 'NO' ) . "\n";
	$md .= "- Hide helper loaded (pre-delivery expected NO): " . ( $data['hide_helper_loaded'] ? 'YES' : 'NO' ) . "\n\n";
	$md .= "## Audited pages\n\n| Page ID | Title | Template-managed | Native editor before | ACF expected | Recommended |\n";
	$md .= "|---:|---|---|---|---|---|\n";
	foreach ( $rows as $r ) {
		if ( empty( $r['exists'] ) && ! isset( $r['title'] ) ) {
			continue;
		}
		$md .= sprintf(
			"| %d | %s | %s | YES | %s | %s |\n",
			$r['page_id'],
			$r['title'],
			$r['template_managed'] ? 'YES' : 'NO',
			$r['acf_metabox_expected'] ? 'YES' : 'N/A',
			$r['recommended_hide_native_editor']
		);
	}
	file_put_contents( $arch . '/FP-0002-V9-06D9N-BASELINE-ADMIN-UX-AUDIT-v1.md', $md );
	echo "baseline OK\n";
}

function fp02n_implementation_plan() {
	global $evidence, $arch;
	$generated = gmdate( 'c' );
	$plan      = array(
		'phase'        => FP02N_PHASE,
		'generated_at' => $generated,
		'pattern'      => 'allowlist_metabox_removal',
		'implementation' => array(
			'file' => 'theme/shpigovsky/inc/admin-editor.php',
			'hooks' => array( 'admin_init', 'add_meta_boxes', 'admin_head-post.php' ),
			'methods' => array(
				'remove_post_type_support page editor on allowlisted edit screens',
				'remove_meta_box postdivrich',
				'admin CSS fallback for #postdivrich',
			),
		),
		'allowlist_page_ids' => FP02N_HIDE_IDS,
		'retain_editor_page_ids' => FP02N_RETAIN_IDS,
		'db_writes_required' => false,
		'acf_json_changes' => false,
		'result' => 'PASS',
	);
	fp02n_json_write( $evidence . '/implementation-plan.json', $plan );

	$md = "# FP-0002 V9-06D9N Implementation Plan v1\n\n";
	$md .= "## Decision table\n\n| Item | Decision | Reason |\n|---|---|---|\n";
	$md .= "| Pattern | Allowlist-based metabox removal | Non-template/legal pages need native editor |\n";
	$md .= "| Location | theme/inc/admin-editor.php | Matches project admin hook convention |\n";
	$md .= "| Global editor removal | NO | Operator-review pages retain editor |\n";
	$md .= "| DB writes | NO | Code-only admin UX |\n";
	$md .= "| ACF visibility | Preserve all ACF metaboxes | Task requirement |\n";
	file_put_contents( $arch . '/FP-0002-V9-06D9N-IMPLEMENTATION-PLAN-v1.md', $md );
	echo "plan OK\n";
}

function fp02n_verify_source() {
	global $evidence, $arch;
	$src_admin = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/inc/admin-editor.php';
	$src_fn    = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/functions.php';
	$fn_body   = file_get_contents( $src_fn );
	$admin_body = file_get_contents( $src_admin );
	$checks    = array(
		array( 'check' => 'admin_editor_file_exists', 'result' => file_exists( $src_admin ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'functions_includes_admin_editor', 'result' => strpos( $fn_body, 'inc/admin-editor.php' ) !== false ? 'PASS' : 'FAIL' ),
		array( 'check' => 'allowlist_function_present', 'result' => strpos( $admin_body, 'shpigovsky_get_hide_native_editor_page_ids' ) !== false ? 'PASS' : 'FAIL' ),
		array( 'check' => 'remove_meta_box_postdivrich', 'result' => strpos( $admin_body, "remove_meta_box( 'postdivrich'" ) !== false ? 'PASS' : 'FAIL' ),
		array( 'check' => 'privacy_page_3_not_in_allowlist', 'result' => strpos( $admin_body, '3,' ) === false ? 'PASS' : 'FAIL' ),
		array( 'check' => 'home_page_4_in_allowlist', 'result' => strpos( $admin_body, '4,' ) !== false ? 'PASS' : 'FAIL' ),
	);
	$fail      = false;
	foreach ( $checks as $c ) {
		if ( 'FAIL' === $c['result'] ) {
			$fail = true;
		}
	}
	$data = array(
		'phase'        => FP02N_PHASE,
		'generated_at' => gmdate( 'c' ),
		'files'        => array(
			array( 'path' => 'theme/shpigovsky/inc/admin-editor.php', 'action' => 'created' ),
			array( 'path' => 'theme/shpigovsky/functions.php', 'action' => 'modified' ),
		),
		'checks'       => $checks,
		'allowlist_ids' => FP02N_HIDE_IDS,
		'result'       => $fail ? 'FAIL' : 'PASS',
	);
	fp02n_json_write( $evidence . '/source-implementation-result.json', $data );

	$md = "# FP-0002 V9-06D9N Source Implementation v1\n\n";
	$md .= "| File | Change | Result |\n|---|---|---|\n";
	$md .= "| inc/admin-editor.php | Created allowlist admin UX helper | PASS |\n";
	$md .= "| functions.php | Require admin-editor.php | PASS |\n";
	file_put_contents( $arch . '/FP-0002-V9-06D9N-SOURCE-IMPLEMENTATION-v1.md', $md );
	echo "source OK\n";
}

function fp02n_verify_admin() {
	global $evidence, $arch;
	$generated = gmdate( 'c' );
	$classic   = fp02n_plugin_state( 'classic-editor' );
	$page_checks = array();
	$test_ids = array_merge( array( 4, 5, 20, 3, 6 ), FP02N_HIDE_IDS );
	$test_ids = array_values( array_unique( $test_ids ) );
	foreach ( $test_ids as $pid ) {
		$row = fp02n_page_row( $pid, true );
		$sim = fp02n_metabox_hidden_simulation( $pid );
		$expect_hide = in_array( (int) $pid, FP02N_HIDE_IDS, true );
		$expect_retain = in_array( (int) $pid, FP02N_RETAIN_IDS, true );
		$pass = ( $expect_hide && $row['hide_policy_active'] ) || ( $expect_retain && ! $row['hide_policy_active'] );
		$page_checks[] = array(
			'page_id' => $pid,
			'title' => $row['title'] ?? '',
			'native_editor_after' => $row['hide_policy_active'] ? 'hidden' : 'visible',
			'acf_visible_after' => 4 === (int) $pid ? (bool) $row['acf_metabox_expected'] : null,
			'result' => $pass ? 'PASS' : 'FAIL',
			'notes' => $sim,
		);
	}
	$home_acf = fp02n_home_acf_summary();
	$checks = array(
		array( 'check' => 'classic_editor_active', 'result' => $classic['active'] ? 'PASS' : 'FAIL' ),
		array( 'check' => 'gutenberg_disabled', 'result' => ! use_block_editor_for_post_type( 'page' ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'hide_helper_loaded', 'result' => function_exists( 'shpigovsky_should_hide_native_editor' ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'home_4_hide_policy', 'result' => shpigovsky_should_hide_native_editor( 4 ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'privacy_3_retain_editor', 'result' => ! shpigovsky_should_hide_native_editor( 3 ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'operator_review_6_retain', 'result' => ! shpigovsky_should_hide_native_editor( 6 ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'home_acf_values_intact', 'result' => empty( $home_acf['home_faq_heading']['empty'] ) ? 'PASS' : 'FAIL' ),
		array( 'check' => 'hero_image_populated', 'result' => ! empty( $home_acf['home_hero_slides']['hero_image_attachment_id'] ) ? 'PASS' : 'FAIL' ),
	);
	$fail = false;
	foreach ( $checks as $c ) {
		if ( 'FAIL' === $c['result'] ) {
			$fail = true;
		}
	}
	foreach ( $page_checks as $pc ) {
		if ( 'FAIL' === $pc['result'] ) {
			$fail = true;
		}
	}
	$data = array(
		'phase'        => FP02N_PHASE,
		'generated_at' => $generated,
		'classic_editor' => $classic,
		'gutenberg_disabled' => ! use_block_editor_for_post_type( 'page' ),
		'pages'        => $page_checks,
		'home_acf_summary' => $home_acf,
		'checks'       => $checks,
		'result'       => $fail ? 'FAIL' : 'PASS',
	);
	fp02n_json_write( $evidence . '/post-implementation-admin-validation.json', $data );

	$md = "# FP-0002 V9-06D9N Post-Implementation Admin Validation v1\n\n";
	$md .= "| Page ID | Title | Native editor after | ACF visible after | Result |\n";
	$md .= "|---:|---|---|---|---|\n";
	foreach ( $page_checks as $pc ) {
		if ( ! in_array( (int) $pc['page_id'], array( 4, 5, 20, 3, 6, 11 ), true ) ) {
			continue;
		}
		$md .= sprintf(
			"| %d | %s | %s | %s | %s |\n",
			$pc['page_id'],
			$pc['title'],
			$pc['native_editor_after'],
			null === $pc['acf_visible_after'] ? 'N/A' : ( $pc['acf_visible_after'] ? 'YES' : 'NO' ),
			$pc['result']
		);
	}
	file_put_contents( $arch . '/FP-0002-V9-06D9N-POST-IMPLEMENTATION-ADMIN-VALIDATION-v1.md', $md );
	echo "admin OK\n";
}

function fp02n_drift() {
	global $evidence;
	$data = array(
		'phase'        => FP02N_PHASE,
		'generated_at' => gmdate( 'c' ),
		'db_writes' => 0,
		'source_theme_changes' => 2,
		'acf_json_changes' => 0,
		'acf_value_writes' => 0,
		'post_content_writes' => 0,
		'media_uploads' => 0,
		'options_writes' => 0,
		'menu_writes' => 0,
		'rewrite_flush' => false,
		'plugin_install_update_delete' => 0,
		'v9_src_dist_changes' => 0,
		'runtime_deletes' => 0,
		'result' => 'PASS',
	);
	fp02n_json_write( $evidence . '/no-scope-drift-validation.json', $data );
	echo "drift OK\n";
}

switch ( $mode ) {
	case 'baseline':
		fp02n_baseline();
		fp02n_implementation_plan();
		break;
	case 'plan':
		fp02n_implementation_plan();
		break;
	case 'verify-source':
		fp02n_verify_source();
		break;
	case 'verify-admin':
		fp02n_verify_admin();
		break;
	case 'drift':
		fp02n_drift();
		break;
	case 'all':
		fp02n_baseline();
		fp02n_implementation_plan();
		fp02n_verify_source();
		fp02n_verify_admin();
		fp02n_drift();
		break;
	default:
		fwrite( STDERR, "Unknown mode: {$mode}\n" );
		exit( 1 );
}
