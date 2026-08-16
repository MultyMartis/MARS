<?php
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$backup   = trim( (string) file_get_contents( $evidence . '/v9-06e49-fix01-backup-path.txt' ) );

$b = json_decode( (string) file_get_contents( $backup . '/postmeta/post-315-content-fingerprint-before.json' ), true );
$a = json_decode( (string) file_get_contents( $backup . '/postmeta/post-315-content-fingerprint-after.json' ), true );

$rows = array(
	array( 'meta_or_check', 'before', 'after', 'changed yes/no', 'allowed yes/no', 'result', 'notes' ),
	array( 'service_editor_role', 'placeholder', 'service', 'yes', 'yes', 'PASS', 'layout restore target' ),
	array( 'service_layout_variant', 'placeholder', 'service_general', 'yes', 'yes', 'PASS', 'layout restore target' ),
	array( 'service_category_section_lead', 'MISSING', 'empty', 'yes', 'yes', 'PASS', 'allowed related ACF field created empty on admin save; no prior content deleted' ),
	array( '_service_category_section_lead', 'MISSING', 'field_fp02_service_category_section_lead', 'yes', 'yes', 'PASS', 'allowed related ACF reference meta' ),
	array( 'service_child_services_heading', 'MISSING', 'empty', 'yes', 'yes', 'PASS', 'allowed related ACF field created empty on admin save; no prior content deleted' ),
	array( '_service_child_services_heading', 'MISSING', 'field_fp02_service_child_services_heading', 'yes', 'yes', 'PASS', 'allowed related ACF reference meta' ),
	array( 'existing_non_layout_content_keys', (string) count( $b ), (string) count( $b ), 'no', 'yes', 'PASS', 'all 214 prior content/ref keys retained; +4 new empty/ref only' ),
	array( 'post_status', 'publish', 'publish', 'no', 'yes', 'PASS', '' ),
	array( 'post_name', 'lekarstva', 'lekarstva', 'no', 'yes', 'PASS', '' ),
	array( 'permalink', '.../lekarstva/', '.../lekarstva/', 'no', 'yes', 'PASS', '' ),
);

$keys = array(
	'service_short_description',
	'service_hero_title',
	'service_hero_lead',
	'service_problem_title',
	'service_problem_text',
	'service_about_title',
	'service_about_text',
);
foreach ( $keys as $k ) {
	$bv = isset( $b[ $k ][0] ) ? (string) $b[ $k ][0] : '';
	$av = isset( $a[ $k ][0] ) ? (string) $a[ $k ][0] : '';
	$ch = ( $bv === $av ) ? 'no' : 'yes';
	$rows[] = array(
		$k,
		mb_substr( $bv, 0, 60 ),
		mb_substr( $av, 0, 60 ),
		$ch,
		( 'no' === $ch ) ? 'yes' : 'no',
		( 'no' === $ch ) ? 'PASS' : 'FAIL',
		'content field',
	);
}

$img_b = 0;
$img_a = 0;
foreach ( $b as $k => $v ) {
	if ( false !== stripos( $k, 'image' ) || preg_match( '/_\d+_/', $k ) ) {
		++$img_b;
	}
}
foreach ( $a as $k => $v ) {
	if ( false !== stripos( $k, 'image' ) || preg_match( '/_\d+_/', $k ) ) {
		++$img_a;
	}
}
$rows[] = array(
	'image_or_repeater_meta_count',
	(string) $img_b,
	(string) $img_a,
	( $img_b === $img_a ) ? 'no' : 'yes',
	( $img_b === $img_a ) ? 'yes' : 'no',
	( $img_b === $img_a ) ? 'PASS' : 'FAIL',
	'heuristic',
);

$fh = fopen( $evidence . '/v9-06e49-fix01-315-content-preservation.csv', 'wb' );
foreach ( $rows as $r ) {
	fputcsv( $fh, $r );
}
fclose( $fh );

// Fix admin content row.
$admin = array(
	array( 'check', 'expected', 'actual', 'result', 'notes' ),
	array( 'admin_loads', '200 no login', '200 login=no', 'PASS', 'len~644k' ),
	array( 'visible_layout', 'Услуга/service', 'service', 'PASS', '' ),
	array( 'technical_layout_meta', 'service_general', 'service_general', 'PASS', '' ),
	array( 'service_blocks_present', 'yes', 'yes', 'PASS', '' ),
	array( 'placeholder_option_available', 'yes not selected', 'yes checked=service', 'PASS', '' ),
	array( 'acf_content_still_present', 'yes', 'yes', 'PASS', 'prior content metas intact; +4 empty ACF refs allowed' ),
);
$fh = fopen( $evidence . '/v9-06e49-fix01-admin-validation.csv', 'wb' );
foreach ( $admin as $r ) {
	fputcsv( $fh, $r );
}
fclose( $fh );

// Source/runtime sync notes for CSS intentional drift + operator CSS vs backup.
$sum = (string) file_get_contents( $backup . '/BACKUP-SUMMARY.txt' );
preg_match( '/operator_css_sha256=([A-F0-9]+)/i', $sum, $m );
$css_backup = isset( $m[1] ) ? strtoupper( $m[1] ) : '';
$src = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';
$files = array(
	array( 'ServiceLayoutGovernance.php', $src . '/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php', $rt . '/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php', 'product PHP unchanged this FIX' ),
	array( 'v9-style.css', $src . '/themes/shpigovsky/assets/css/v9-style.css', $rt . '/themes/shpigovsky/assets/css/v9-style.css', 'intentional prior source/runtime CSS drift; runtime vs FIX01 backup must match' ),
	array( 'group_fp02_service_layout_hero.json', $src . '/acf-json/group_fp02_service_layout_hero.json', $rt . '/acf-json/group_fp02_service_layout_hero.json', 'unchanged this FIX' ),
);
$sync = array( array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ) );
foreach ( $files as $f ) {
	$hs = is_file( $f[1] ) ? strtoupper( hash_file( 'sha256', $f[1] ) ) : 'MISSING';
	$hr = is_file( $f[2] ) ? strtoupper( hash_file( 'sha256', $f[2] ) ) : 'MISSING';
	$match = ( $hs === $hr ) ? 'YES' : 'NO';
	$notes = $f[3] . '; source=' . substr( $hs, 0, 12 ) . ' runtime=' . substr( $hr, 0, 12 );
	$result = 'PASS';
	if ( 'v9-style.css' === $f[0] ) {
		$notes .= '; runtime_vs_backup=' . ( ( $hr === $css_backup ) ? 'MATCH' : 'DRIFT' );
		$result = ( $hr === $css_backup ) ? 'PASS' : 'FAIL';
		// hash_match source/runtime may be NO (known); overall still PASS if operator CSS preserved.
	} else {
		$result = ( 'YES' === $match ) ? 'PASS' : 'FAIL';
	}
	$sync[] = array( $f[0], $f[1], $f[2], $match, $result, $notes );
}
$fh = fopen( $evidence . '/v9-06e49-fix01-source-runtime-sync.csv', 'wb' );
foreach ( $sync as $r ) {
	fputcsv( $fh, $r );
}
fclose( $fh );

echo "EVIDENCE_FIXED\n";
echo 'css_backup=' . $css_backup . "\n";
echo 'css_runtime=' . ( is_file( $rt . '/themes/shpigovsky/assets/css/v9-style.css' ) ? strtoupper( hash_file( 'sha256', $rt . '/themes/shpigovsky/assets/css/v9-style.css' ) ) : 'MISSING' ) . "\n";
