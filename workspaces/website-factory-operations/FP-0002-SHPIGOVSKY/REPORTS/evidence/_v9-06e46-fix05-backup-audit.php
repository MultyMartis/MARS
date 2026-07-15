<?php
/**
 * V9-06E46-FIX05 — pre-write backup exports + audits (read-mostly; no ACF mutations).
 *
 * @package FP0002
 */

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$backup = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351';
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';

foreach ( array( $backup . '/meta', $backup . '/exports', $backup . '/admin', $backup . '/frontend', $backup . '/snapshots' ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		wp_mkdir_p( $dir );
	}
}

$section_ids = array( 73, 77, 84 );
$home_id     = 4;

// --- postmeta export ---
global $wpdb;
$ids_sql = implode( ',', array_map( 'intval', $section_ids ) );
$rows    = $wpdb->get_results(
	"SELECT post_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id IN ({$ids_sql}) ORDER BY post_id, meta_key",
	ARRAY_A
);
$meta_tsv = "post_id\tmeta_key\tmeta_value\n";
foreach ( (array) $rows as $r ) {
	$meta_tsv .= $r['post_id'] . "\t" . $r['meta_key'] . "\t" . str_replace( array( "\r", "\n", "\t" ), array( '\\r', '\\n', '\\t' ), (string) $r['meta_value'] ) . "\n";
}
file_put_contents( $backup . '/meta/postmeta-73-77-84-section-before.tsv', $meta_tsv );

foreach ( $section_ids as $pid ) {
	$post = get_post( $pid );
	file_put_contents(
		$backup . '/exports/post_content-' . $pid . '-before.txt',
		$post ? (string) $post->post_content : ''
	);
}

// Home image sources used by section blocks.
$home_imgs = array(
	'home_clinic_landscape_image' => (int) get_post_meta( $home_id, 'home_clinic_landscape_image', true ),
	'home_staff_photo_image'      => (int) get_post_meta( $home_id, 'home_staff_photo_image', true ),
);
$home_tsv = "field\tattachment_id\turl\n";
foreach ( $home_imgs as $fname => $aid ) {
	$url = $aid > 0 ? (string) wp_get_attachment_url( $aid ) : '';
	$home_tsv .= $fname . "\t" . $aid . "\t" . $url . "\n";
}
file_put_contents( $backup . '/exports/home-image-sources-before.tsv', $home_tsv );

// Find media by filename fragments for team/corridor/landscape.
$search_terms = array(
	'shpigovsky-staff-group',
	'shpigovsky-interior-corridor',
	'shpigovsky-clinic-landscape',
);
$media_hits = array();
foreach ( $search_terms as $term ) {
	$found = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT p.ID, p.post_title, pm.meta_value AS file
			 FROM {$wpdb->posts} p
			 INNER JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key = '_wp_attached_file'
			 WHERE p.post_type = 'attachment' AND pm.meta_value LIKE %s
			 ORDER BY p.ID DESC LIMIT 10",
			'%' . $wpdb->esc_like( $term ) . '%'
		),
		ARRAY_A
	);
	$media_hits[ $term ] = $found;
}
file_put_contents( $backup . '/exports/media-search-before.json', wp_json_encode( $media_hits, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Section ACF snapshot (raw meta for parity fields).
$parity_fields = array(
	'section_dependencies_heading',
	'section_dependencies_lead',
	'section_dependencies_footer',
	'section_nature_heading',
	'section_nature_lead',
	'section_nature_text_blocks',
	'section_nature_cards',
	'section_program_heading',
	'section_program_more_label',
	'section_program_lead',
	'section_program_intro_items',
	'section_program_footer_label',
	'section_stages_heading',
	'section_stages_lead',
	'section_stages_items',
	'section_stages_support_heading',
	'section_stages_support_items',
	'section_approach_heading',
	'section_approach_more_label',
	'section_approach_more_url',
	'section_approach_highlight',
	'section_approach_intro',
	'section_approach_corridor_image',
	'section_approach_corridor_alt',
	'section_approach_staff_image',
	'section_approach_staff_alt',
	'section_approach_cards',
	'section_clinic_landscape_image',
	'section_team_image',
	'section_corridor_image',
	'section_faq_heading',
);

$parity_export = array();
foreach ( $section_ids as $pid ) {
	$parity_export[ $pid ] = array(
		'title'  => get_the_title( $pid ),
		'fields' => array(),
	);
	foreach ( $parity_fields as $fname ) {
		$raw = function_exists( 'get_field' ) ? get_field( $fname, $pid ) : get_post_meta( $pid, $fname, true );
		$parity_export[ $pid ]['fields'][ $fname ] = $raw;
	}
}
file_put_contents( $backup . '/exports/section-parity-values-before.json', wp_json_encode( $parity_export, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Admin inventory before.
$groups = function_exists( 'acf_get_field_groups' ) ? acf_get_field_groups( array( 'post_id' => 73 ) ) : array();
$parity = null;
foreach ( $groups as $g ) {
	if ( isset( $g['key'] ) && 'group_fp02_service_section_parity' === $g['key'] ) {
		$parity = $g;
		break;
	}
}
$admin_fields = ( $parity && function_exists( 'acf_get_fields' ) ) ? acf_get_fields( $parity ) : array();
$admin_inv    = array(
	'group_key'   => $parity['key'] ?? '',
	'field_count' => is_array( $admin_fields ) ? count( $admin_fields ) : 0,
	'names'       => array(),
	'instructions_with_fallback' => array(),
);
foreach ( (array) $admin_fields as $f ) {
	$name = isset( $f['name'] ) ? (string) $f['name'] : '';
	$admin_inv['names'][] = $name;
	$instr = isset( $f['instructions'] ) ? (string) $f['instructions'] : '';
	$msg   = isset( $f['message'] ) ? (string) $f['message'] : '';
	$blob  = $instr . ' ' . $msg;
	if ( preg_match( '/fallback|шаблон|главн|theme asset|если пусто/iu', $blob ) ) {
		$admin_inv['instructions_with_fallback'][] = array(
			'name'  => $name,
			'label' => $f['label'] ?? '',
			'text'  => wp_strip_all_tags( $blob ),
		);
	}
}
file_put_contents( $backup . '/admin/admin-73-fields-before.json', wp_json_encode( $admin_inv, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

if ( class_exists( 'Shpigovsky\\Core\\Fields\\ServiceSectionParity' ) ) {
	$group_def = \Shpigovsky\Core\Fields\ServiceSectionParity::group();
	file_put_contents( $backup . '/acf-group_fp02_service_section_parity-source-before.json', wp_json_encode( $group_def, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
}

// Frontend snapshots (HTTP).
$routes = array(
	'/'                                              => 'home',
	'/uslugi/'                                       => 'uslugi',
	'/uslugi/zavisimosti/'                           => 'zavisimosti',
	'/uslugi/psihicheskoe-zdorovie/'                 => 'psihicheskoe-zdorovie',
	'/uslugi/rasstroystva-pischevogo-povedeniya/'    => 'rasstroystva',
);
$snap_summary = array();
foreach ( $routes as $path => $slug ) {
	$url  = home_url( $path );
	$resp = wp_remote_get(
		$url,
		array(
			'timeout'     => 30,
			'redirection' => 3,
			'sslverify'   => false,
		)
	);
	$code = is_wp_error( $resp ) ? 0 : (int) wp_remote_retrieve_response_code( $resp );
	$body = is_wp_error( $resp ) ? ( 'ERROR: ' . $resp->get_error_message() ) : (string) wp_remote_retrieve_body( $resp );
	file_put_contents( $backup . '/frontend/' . $slug . '-before.html', $body );
	$snap_summary[] = array(
		'route'  => $path,
		'url'    => $url,
		'http'   => $code,
		'bytes'  => strlen( $body ),
		'has_team_img' => ( false !== strpos( $body, 'service-subdivision-team-stats-v1__staff-image' ) ),
		'has_corridor' => ( false !== strpos( $body, 'service-subdivision-team-stats-v1__corridor-image' ) ),
		'has_landscape' => ( false !== strpos( $body, 'clinic-landscape' ) ),
	);
	// extract image srcs for team/corridor/landscape on zavisimosti
	if ( 'zavisimosti' === $slug ) {
		preg_match_all( '/service-subdivision-team-stats-v1__(staff|corridor)-image[^>]+src="([^"]+)"/', $body, $m, PREG_SET_ORDER );
		preg_match_all( '/clinic-landscape[^>]*>[\s\S]*?<img[^>]+src="([^"]+)"/', $body, $lm );
		file_put_contents(
			$backup . '/exports/zavisimosti-image-srcs-before.json',
			wp_json_encode(
				array(
					'team_corridor_matches' => $m,
					'landscape_candidates'  => $lm[1] ?? array(),
				),
				JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
			)
		);
	}
}
file_put_contents( $backup . '/frontend/snapshot-summary-before.json', wp_json_encode( $snap_summary, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Fallback source map (static description for audit CSV generation later).
$fallback_map = array(
	array( 'block' => 'dependencies', 'fields' => array( 'section_dependencies_heading', 'section_dependencies_lead', 'section_dependencies_footer' ), 'type' => 'text' ),
	array( 'block' => 'nature', 'fields' => array( 'section_nature_heading', 'section_nature_lead', 'section_nature_text_blocks', 'section_nature_cards' ), 'type' => 'mixed' ),
	array( 'block' => 'program', 'fields' => array( 'section_program_heading', 'section_program_more_label', 'section_program_lead', 'section_program_intro_items' ), 'type' => 'mixed' ),
	array( 'block' => 'stages', 'fields' => array( 'section_stages_heading', 'section_stages_lead', 'section_stages_items', 'section_stages_support_heading', 'section_stages_support_items' ), 'type' => 'mixed' ),
	array( 'block' => 'approach', 'fields' => array( 'section_approach_heading', 'section_approach_more_label', 'section_approach_highlight', 'section_approach_intro', 'section_approach_cards', 'section_approach_corridor_image', 'section_approach_staff_image' ), 'type' => 'mixed' ),
	array( 'block' => 'clinic_landscape', 'fields' => array( 'section_clinic_landscape_image' ), 'type' => 'image' ),
);
file_put_contents( $backup . '/exports/current-fallback-source-map-before.json', wp_json_encode( $fallback_map, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

$out = array(
	'backup'           => $backup,
	'meta_rows'        => count( (array) $rows ),
	'home_imgs'        => $home_imgs,
	'media_hits'       => $media_hits,
	'snap_summary'     => $snap_summary,
	'admin_field_count'=> $admin_inv['field_count'],
	'fallback_wording_count' => count( $admin_inv['instructions_with_fallback'] ),
);
file_put_contents( $evidence . '/_v9-06e46-fix05-backup-audit-result.json', wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
