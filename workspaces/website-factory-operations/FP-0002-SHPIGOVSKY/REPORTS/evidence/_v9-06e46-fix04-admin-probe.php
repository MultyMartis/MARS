<?php
/**
 * V9-06E46-FIX04 admin inventory probe (WP-CLI eval-file).
 *
 * @package FP0002
 */

$pid    = 73;
$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => $pid ) ) : array();
$parity = null;

foreach ( $groups as $g ) {
	if ( isset( $g['key'] ) && 'group_fp02_service_section_parity' === $g['key'] ) {
		$parity = $g;
		break;
	}
}

$fields = ( $parity && function_exists( 'acf_get_fields' ) ) ? acf_get_fields( $parity ) : array();
$names  = array();
$notice = '';

foreach ( (array) $fields as $f ) {
	$names[] = isset( $f['name'] ) ? (string) $f['name'] : '';
	if ( isset( $f['name'] ) && 'section_clinic_landscape_notice' === $f['name'] ) {
		$notice = isset( $f['message'] ) ? (string) $f['message'] : '';
	}
}

$notice_plain = wp_strip_all_tags( $notice );

$out = array(
	'parity_field_count'         => count( $names ),
	'has_footer_label'           => in_array( 'section_program_footer_label', $names, true ),
	'has_landscape_image'        => in_array( 'section_clinic_landscape_image', $names, true ),
	'has_landscape_visible'      => in_array( 'section_clinic_landscape_visible', $names, true ),
	'notice_mentions_home'       => ( false !== stripos( $notice, 'home_clinic_landscape' ) || false !== stripos( $notice_plain, 'с главной' ) ),
	'notice_section_specific'    => ( false !== stripos( $notice_plain, 'этой страницы раздела' ) ),
	'notice_text'                => $notice_plain,
	'section_image_73'           => (int) get_post_meta( 73, 'section_clinic_landscape_image', true ),
	'section_image_77'           => (int) get_post_meta( 77, 'section_clinic_landscape_image', true ),
	'section_image_84'           => (int) get_post_meta( 84, 'section_clinic_landscape_image', true ),
	'footer_meta_73'             => get_post_meta( 73, 'section_program_footer_label', true ),
	'post_content_73'            => strlen( (string) get_post( 73 )->post_content ),
	'post_content_77'            => strlen( (string) get_post( 77 )->post_content ),
	'post_content_84'            => strlen( (string) get_post( 84 )->post_content ),
	'supports_editor_global'     => post_type_supports( 'service', 'editor' ),
	'has_hide_helpers'           => function_exists( 'shpigovsky_admin_is_service_edit_screen' ),
	'home_landscape_untouched'   => (int) get_post_meta( 4, 'home_clinic_landscape_image', true ),
	'hooks'                      => array(
		'admin_init'              => (bool) has_action( 'admin_init', 'shpigovsky_maybe_remove_page_editor_support' ),
		'add_meta_boxes'          => (bool) has_action( 'add_meta_boxes', 'shpigovsky_hide_native_editor_metabox' ),
		'admin_head-post.php'     => (bool) has_action( 'admin_head-post.php', 'shpigovsky_hide_native_editor_admin_css' ),
		'admin_head-post-new.php' => (bool) has_action( 'admin_head-post-new.php', 'shpigovsky_hide_native_editor_admin_css' ),
	),
);

$path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/_v9-06e46-fix04-admin.json';
file_put_contents( $path, wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
