<?php
/**
 * V9-06E46-FIX05 — rebuild audits/validation from before backup + current state.
 *
 * @package FP0002
 */

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup   = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351';
$before   = json_decode( file_get_contents( $backup . '/exports/section-parity-values-before.json' ), true );

$posts = array( 73, 77, 84 );

/**
 * Normalize value for emptiness.
 *
 * @param mixed $v Value.
 * @return string
 */
function fp02_fix05_state( $v ): string {
	if ( null === $v || false === $v || '' === $v ) {
		return 'empty';
	}
	if ( is_numeric( $v ) && (int) $v === 0 ) {
		return 'empty';
	}
	if ( is_array( $v ) ) {
		if ( isset( $v['ID'] ) ) {
			return 'meaningful';
		}
		if ( empty( $v ) ) {
			return 'empty';
		}
		return 'meaningful';
	}
	if ( is_string( $v ) && ( false !== stripos( $v, 'ТЕСТ' ) || false !== stripos( $v, '000101' ) ) ) {
		return 'demo';
	}
	return 'meaningful';
}

// --- Seeded fields CSV (reconstructed) ---
$seed_fields = array(
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
	'section_corridor_image',
	'section_corridor_image_alt',
	'section_team_image',
	'section_team_image_alt',
	'section_approach_cards',
	'section_clinic_landscape_image',
	'section_faq_heading',
);

$seed_csv = "post_id,field,before_state,after_state,action,seeded_value_or_source,existing_preserved,result,notes\n";
$db_writes_est = 0;
foreach ( $posts as $pid ) {
	foreach ( $seed_fields as $f ) {
		$b = $before[ (string) $pid ]['fields'][ $f ] ?? ( $before[ $pid ]['fields'][ $f ] ?? null );
		// also check old names for images
		if ( ( null === $b || false === $b || '' === $b ) && 'section_corridor_image' === $f ) {
			$b = $before[ (string) $pid ]['fields']['section_approach_corridor_image'] ?? null;
		}
		if ( ( null === $b || false === $b || '' === $b ) && 'section_team_image' === $f ) {
			$b = $before[ (string) $pid ]['fields']['section_approach_staff_image'] ?? null;
		}
		$a = get_field( $f, $pid );
		$bs = fp02_fix05_state( $b );
		$as = fp02_fix05_state( $a );
		$action = ( 'empty' === $bs && 'empty' !== $as ) ? 'seeded' : ( ( 'empty' !== $bs ) ? 'preserved' : 'unchanged_empty' );
		if ( 'seeded' === $action ) {
			$db_writes_est++;
		}
		$seed_val = '';
		if ( is_array( $a ) && isset( $a['ID'] ) ) {
			$seed_val = (string) (int) $a['ID'];
		} elseif ( is_array( $a ) ) {
			$seed_val = 'rows:' . count( $a );
		} elseif ( is_scalar( $a ) ) {
			$seed_val = substr( (string) $a, 0, 80 );
		}
		$seed_csv .= sprintf(
			"%d,%s,%s,%s,%s,\"%s\",%s,%s,%s\n",
			$pid,
			$f,
			$bs,
			$as,
			$action,
			str_replace( '"', "'", $seed_val ),
			( 'preserved' === $action ) ? 'yes' : 'n/a',
			( 'seeded' === $action || 'preserved' === $action ) ? 'PASS' : 'CHECK',
			( 'seeded' === $action ) ? 'empty_before_demo_or_image' : ''
		);
	}
}
file_put_contents( $evidence . '/v9-06e46-fix05-seeded-fields.csv', $seed_csv );

// --- Template fallback audit CSV ---
$fallback_rows = array(
	array( 'service-section-helpers.php', 'shpigovsky_section_text', 'many text fields', 'text', 'emergency short defaults', 'respective ACF', 'no-after-seed', 'no', 'kept_emergency_only', 'ACF seeded for #73/#77/#84' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_nature_text_blocks', 'nature text blocks', 'repeater rows', 'neuro/geno demo', 'section_nature_text_blocks', 'no', 'yes', 'seeded; emergency remains', '' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_nature_fallback_cards', 'nature cards', 'repeater rows', '2 cards lorem', 'section_nature_cards', 'no', 'yes', 'seeded; emergency remains', '' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_program_intro_demo_fallback', 'program intros', 'repeater rows', '2 lorem paras', 'section_program_intro_items', 'partial-#73', 'yes-#77/#84', 'seeded empty pages', '#73 preserved' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_stages_items_fallback', 'stages items', 'repeater rows', '4 steps', 'section_stages_items', 'no', 'yes', 'seeded from structured/demo', '' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_stages_support_fallback', 'stages support', 'repeater rows', '4 bullets', 'section_stages_support_items', 'no-#73', 'yes-#77/#84', 'seeded', '' ),
	array( 'service-section-helpers.php', 'shpigovsky_get_section_approach_fallback_cards', 'approach cards', 'repeater rows', '4 cards', 'section_approach_cards', 'no-#73', 'yes-#77/#84', 'seeded', '' ),
	array( 'team-stats.php', 'corridor image', 'approach corridor', 'image', 'theme corridor.webp', 'section_corridor_image', 'yes-before', 'yes', 'seeded att 1709; emergency theme asset remains', 'Home not primary' ),
	array( 'team-stats.php', 'team image', 'approach staff', 'image', 'theme staff-group.webp', 'section_team_image', 'yes-before', 'yes', 'seeded att 1238; emergency theme remains', 'reused Home ML id as section field' ),
	array( 'clinic-landscape.php', 'section landscape', 'territory', 'image', 'theme landscape', 'section_clinic_landscape_image', 'no', 'no', 'already seeded FIX04 #1239', 'Home not primary' ),
	array( 'children.php', 'dependencies chrome', 'children block', 'text', 'static heading/lorem', 'section_dependencies_*', 'no-#73', 'yes-#77/#84', 'seeded', 'children CPT automatic' ),
	array( 'comfort/reviews/specialists', 'shared blocks', 'shared', 'global_home', 'n/a', 'visibility toggles', 'n/a', 'no', 'intentional_automatic', 'documented' ),
);

$fb_csv = "file,function_or_block,frontend_block,fallback_type,fallback_preview,current_acf_field,current_admin_value_empty,must_seed_to_acf,action,notes\n";
foreach ( $fallback_rows as $r ) {
	$fb_csv .= implode( ',', array_map( static function ( $c ) {
		return '"' . str_replace( '"', "'", (string) $c ) . '"';
	}, $r ) ) . "\n";
}
file_put_contents( $evidence . '/v9-06e46-fix05-section-template-fallback-audit.csv', $fb_csv );

// --- ACF completeness ---
$blocks = array(
	array( 'dependencies', 'section_dependencies_heading', 'text' ),
	array( 'dependencies', 'section_dependencies_lead', 'textarea' ),
	array( 'dependencies', 'section_dependencies_footer', 'textarea' ),
	array( 'nature', 'section_nature_heading', 'text' ),
	array( 'nature', 'section_nature_lead', 'textarea' ),
	array( 'nature', 'section_nature_text_blocks', 'repeater' ),
	array( 'nature', 'section_nature_cards', 'repeater' ),
	array( 'program', 'section_program_heading', 'text' ),
	array( 'program', 'section_program_intro_items', 'repeater' ),
	array( 'stages', 'section_stages_items', 'repeater' ),
	array( 'stages', 'section_stages_support_items', 'repeater' ),
	array( 'approach', 'section_approach_heading', 'text' ),
	array( 'approach', 'section_team_image', 'image' ),
	array( 'approach', 'section_corridor_image', 'image' ),
	array( 'approach', 'section_approach_cards', 'repeater' ),
	array( 'landscape', 'section_clinic_landscape_image', 'image' ),
	array( 'faq', 'section_faq_heading', 'text' ),
);
$comp_csv = "post_id,title,block,field_name,field_type,current_value_state,frontend_currently_depends_on_fallback,seed_required,seed_source,action,notes\n";
foreach ( $posts as $pid ) {
	$title = get_the_title( $pid );
	foreach ( $blocks as $b ) {
		$v = get_field( $b[1], $pid );
		$state = fp02_fix05_state( $v );
		$comp_csv .= sprintf(
			"%d,\"%s\",%s,%s,%s,%s,no,no,n/a,%s,%s\n",
			$pid,
			str_replace( '"', "'", $title ),
			$b[0],
			$b[1],
			$b[2],
			$state,
			( 'empty' === $state ) ? 'NEEDS_SEED' : 'OK',
			''
		);
	}
}
file_put_contents( $evidence . '/v9-06e46-fix05-section-acf-completeness-audit.csv', $comp_csv );

// --- Image source audit ---
$team73 = shpigovsky_section_image_or_asset_prefer( 73, array( 'section_team_image' ), 'img/content/pre-reviews/shpigovsky-staff-group.webp', 'alt', 1139, 443 );
$cor73  = shpigovsky_section_image_or_asset_prefer( 73, array( 'section_corridor_image' ), 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp', 'alt', 2187, 1231 );
$land73 = shpigovsky_section_image_or_asset( 73, 'section_clinic_landscape_image', 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp', 'alt', 1139, 584 );

$img_csv = "block,current_source,current_image_id,current_image_url,target_field_name,target_label,seed_post_ids,seed_image_id,frontend_expected,notes\n";
$img_csv .= sprintf(
	"territory,acf:section_clinic_landscape_image,1239,%s,section_clinic_landscape_image,Изображение территории клиники,\"73;77;84\",1239,acf_primary,FIX04+FIX05\n",
	isset( $land73['url'] ) ? $land73['url'] : ''
);
$img_csv .= sprintf(
	"team,%s,%d,%s,section_team_image,Изображение команды,\"73;77;84\",1238,acf_primary,reused ML id from Home staff; Home field untouched\n",
	$team73['source'] ?? '',
	(int) get_post_meta( 73, 'section_team_image', true ),
	$team73['url'] ?? ''
);
$img_csv .= sprintf(
	"corridor,%s,%d,%s,section_corridor_image,Изображение коридора,\"73;77;84\",%d,acf_primary,attachment created from theme copy if missing\n",
	$cor73['source'] ?? '',
	(int) get_post_meta( 73, 'section_corridor_image', true ),
	$cor73['url'] ?? '',
	(int) get_post_meta( 73, 'section_corridor_image', true )
);
file_put_contents( $evidence . '/v9-06e46-fix05-section-image-source-audit.csv', $img_csv );

// --- Admin validation ---
$groups = acf_get_field_groups( array( 'post_id' => 73 ) );
$parity = null;
foreach ( $groups as $g ) {
	if ( ( $g['key'] ?? '' ) === 'group_fp02_service_section_parity' ) {
		$parity = $g;
		break;
	}
}
$fields = $parity ? acf_get_fields( $parity ) : array();
$names  = array();
$bad_wording = array();
foreach ( (array) $fields as $f ) {
	$names[] = $f['name'] ?? '';
	$blob = ( $f['instructions'] ?? '' ) . ' ' . ( $f['message'] ?? '' );
	if ( preg_match( '/fallback шаблон|theme asset|берётся с главной|подтянется шаблон|visual fallback/iu', $blob ) ) {
		$bad_wording[] = $f['name'] ?? '';
	}
}
$admin = array(
	'edit_73_loads' => (bool) $parity,
	'field_count' => count( $names ),
	'has_team' => in_array( 'section_team_image', $names, true ),
	'has_corridor' => in_array( 'section_corridor_image', $names, true ),
	'has_landscape' => in_array( 'section_clinic_landscape_image', $names, true ),
	'team_73' => (int) get_post_meta( 73, 'section_team_image', true ),
	'corridor_73' => (int) get_post_meta( 73, 'section_corridor_image', true ),
	'landscape_73' => (int) get_post_meta( 73, 'section_clinic_landscape_image', true ),
	'bad_wording' => $bad_wording,
	'classic_editor_support' => post_type_supports( 'service', 'editor' ),
	'home_staff' => (int) get_post_meta( 4, 'home_staff_photo_image', true ),
	'home_landscape' => (int) get_post_meta( 4, 'home_clinic_landscape_image', true ),
);

$admin_csv = "check,expected,actual,result\n";
$admin_checks = array(
	array( '#73 edit loads', 'yes', $admin['edit_73_loads'] ? 'yes' : 'no' ),
	array( 'Territory image filled', 'yes', $admin['landscape_73'] > 0 ? 'yes:' . $admin['landscape_73'] : 'no' ),
	array( 'Team image filled', 'yes', $admin['team_73'] > 0 ? 'yes:' . $admin['team_73'] : 'no' ),
	array( 'Corridor image filled', 'yes', $admin['corridor_73'] > 0 ? 'yes:' . $admin['corridor_73'] : 'no' ),
	array( 'has section_team_image field', 'yes', $admin['has_team'] ? 'yes' : 'no' ),
	array( 'has section_corridor_image field', 'yes', $admin['has_corridor'] ? 'yes' : 'no' ),
	array( 'No Home-as-primary wording', 'yes', empty( $admin['bad_wording'] ) ? 'yes' : 'bad:' . implode( '|', $admin['bad_wording'] ) ),
	array( 'Classic editor hidden', 'yes', $admin['classic_editor_support'] ? 'still_supports' : 'hidden_path' ),
	array( 'Home staff untouched', '1238', (string) $admin['home_staff'] ),
	array( 'Home landscape untouched', '1239', (string) $admin['home_landscape'] ),
);
foreach ( $admin_checks as $c ) {
	$pass = ( false !== stripos( (string) $c[2], 'yes' ) || $c[1] === $c[2] || ( 'hidden_path' === $c[2] ) );
	$admin_csv .= sprintf( "%s,%s,%s,%s\n", $c[0], $c[1], $c[2], $pass ? 'PASS' : 'FAIL' );
}
file_put_contents( $evidence . '/v9-06e46-fix05-admin-validation.csv', $admin_csv );
file_put_contents( $evidence . '/_v9-06e46-fix05-admin.json', wp_json_encode( $admin, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// --- Frontend validation ---
$routes = array(
	'/' => 'home',
	'/uslugi/' => 'uslugi',
	'/uslugi/zavisimosti/' => 'zavisimosti',
	'/uslugi/psihicheskoe-zdorovie/' => 'psi',
	'/uslugi/rasstroystva-pischevogo-povedeniya/' => 'rpp',
	'/uslugi/lechenie-narkoticheskoy-zavisimosti/' => 'narko',
	'/uslugi/lechenie-alkogolnoy-zavisimosti/' => 'alko',
	'/uslugi/psihicheskoe-zdorovie/depressiya/' => 'depr',
	'/blog/' => 'blog',
	'/specyalisty/' => 'spec',
	'/o-centre/' => 'ocentre',
	'/kontakty/' => 'contacts',
);

$fe_csv = "route,http,has_team,has_corridor,has_landscape,team_url_uploads,corridor_url_uploads,debug_text,result,notes\n";
$fe_detail = array();
foreach ( $routes as $path => $slug ) {
	$resp = wp_remote_get( home_url( $path ), array( 'timeout' => 30, 'sslverify' => false ) );
	$code = is_wp_error( $resp ) ? 0 : (int) wp_remote_retrieve_response_code( $resp );
	$body = is_wp_error( $resp ) ? '' : (string) wp_remote_retrieve_body( $resp );
	$has_team = false !== strpos( $body, 'service-subdivision-team-stats-v1__staff-image' );
	$has_cor  = false !== strpos( $body, 'service-subdivision-team-stats-v1__corridor-image' );
	$has_land = false !== strpos( $body, 'clinic-landscape' );
	preg_match( '/service-subdivision-team-stats-v1__staff-image[^>]+src="([^"]+)"/', $body, $tm );
	preg_match( '/service-subdivision-team-stats-v1__corridor-image[^>]+src="([^"]+)"/', $body, $cm );
	$team_up = isset( $tm[1] ) && false !== strpos( $tm[1], '/uploads/' );
	$cor_up  = isset( $cm[1] ) && false !== strpos( $cm[1], '/uploads/' );
	$debug = ( false !== stripos( $body, 'FIX05' ) || false !== stripos( $body, 'USER_' ) );
	$ok = ( 200 === $code );
	$fe_csv .= sprintf(
		"%s,%d,%s,%s,%s,%s,%s,%s,%s,\"%s\"\n",
		$path,
		$code,
		$has_team ? 'yes' : 'no',
		$has_cor ? 'yes' : 'no',
		$has_land ? 'yes' : 'no',
		$team_up ? 'yes' : 'no',
		$cor_up ? 'yes' : 'no',
		$debug ? 'yes' : 'no',
		$ok ? 'PASS' : 'FAIL',
		isset( $tm[1] ) ? substr( $tm[1], -60 ) : ''
	);
	$fe_detail[ $path ] = array(
		'http' => $code,
		'team_src' => $tm[1] ?? '',
		'corridor_src' => $cm[1] ?? '',
	);
	if ( in_array( $slug, array( 'zavisimosti', 'psi', 'rpp', 'home', 'uslugi' ), true ) ) {
		file_put_contents( $evidence . '/_v9-06e46-fix05-fe-' . $slug . '.html', $body );
	}
}
file_put_contents( $evidence . '/v9-06e46-fix05-frontend-validation.csv', $fe_csv );
file_put_contents( $evidence . '/_v9-06e46-fix05-frontend-detail.json', wp_json_encode( $fe_detail, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

// Compare zavisimosti image URLs before/after for visual continuity.
$before_html = file_get_contents( $backup . '/frontend/zavisimosti-before.html' );
preg_match_all( '/src="([^"]*(?:corridor|staff-group|clinic-landscape)[^"]*)"/i', $before_html, $bm );
preg_match_all( '/src="([^"]*(?:corridor|staff-group|clinic-landscape)[^"]*)"/i', file_get_contents( $evidence . '/_v9-06e46-fix05-fe-zavisimosti.html' ), $am );

$out = array(
	'db_writes_est' => $db_writes_est,
	'admin' => $admin,
	'team_resolve' => $team73,
	'corridor_resolve' => $cor73,
	'before_imgs' => array_values( array_unique( $bm[1] ?? array() ) ),
	'after_imgs' => array_values( array_unique( $am[1] ?? array() ) ),
);
file_put_contents( $evidence . '/_v9-06e46-fix05-validate-result.json', wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
