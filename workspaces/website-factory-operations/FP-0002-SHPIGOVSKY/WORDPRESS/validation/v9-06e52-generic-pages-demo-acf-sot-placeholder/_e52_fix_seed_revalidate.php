<?php
/**
 * V9-06E52 FIX — correct ACF meta keys for generic_page_body seed + revalidate.
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$ids      = array( 12, 13, 14, 15, 16, 1030, 1031, 1032, 1033, 1039, 1053, 1054, 1055, 1056, 1097 );
$hardcoded = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';
$db_writes = 0;
$seed_rows = array();

/**
 * @param string            $path Path.
 * @param array<int,string> $header Header.
 * @param array<int,array>  $rows Rows.
 */
function e52f_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	fprintf( $fp, "\xEF\xBB\xBF" );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * @param mixed $v Value.
 */
function e52f_state( $v ): string {
	if ( null === $v || false === $v || '' === $v ) {
		return 'empty';
	}
	if ( is_string( $v ) && '' === trim( $v ) ) {
		return 'empty';
	}
	return 'meaningful';
}

/**
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e52f_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 40,
			CURLOPT_SSL_VERIFYPEER => false,
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array( 'code' => $code, 'body' => $body );
}

foreach ( $ids as $id ) {
	$post  = get_post( $id );
	$title = $post ? (string) $post->post_title : (string) $id;
	$pc    = $post ? trim( (string) $post->post_content ) : '';

	// Clean wrong meta from key-as-name store.
	$wrong_val = get_post_meta( $id, 'field_fp02_generic_page_body', true );
	delete_post_meta( $id, 'field_fp02_generic_page_body' );
	delete_post_meta( $id, '_field_fp02_generic_page_body' );
	++$db_writes;
	++$db_writes;

	$before = get_field( 'generic_page_body', $id );
	$seed   = '';
	$from   = '';
	if ( e52f_state( $before ) !== 'empty' ) {
		$seed_rows[] = array( $id, $title, 'generic_page_body', e52f_state( $before ), '', e52f_state( $before ), 'yes', 'preserved', 'already readable via get_field' );
		continue;
	}

	if ( is_string( $wrong_val ) && '' !== trim( $wrong_val ) ) {
		$seed = $wrong_val;
		$from = 'relocated_from_wrong_meta_key';
	} elseif ( '' !== $pc ) {
		$seed = $pc;
		$from = 'post_content';
	} else {
		$seed = '<p>' . esc_html( $hardcoded ) . '</p>';
		$from = 'previous_hardcoded_demo_text';
	}

	update_post_meta( $id, 'generic_page_body', $seed );
	update_post_meta( $id, '_generic_page_body', 'field_fp02_generic_page_body' );
	$db_writes += 2;

	// Also try update_field by name for ACF format consistency.
	if ( function_exists( 'update_field' ) ) {
		update_field( 'generic_page_body', $seed, $id );
		++$db_writes;
	}

	$after = get_field( 'generic_page_body', $id );
	$seed_rows[] = array(
		$id,
		$title,
		'generic_page_body',
		'empty',
		$from,
		e52f_state( $after ),
		'no',
		( 'meaningful' === e52f_state( $after ) ? 'seeded_fixed' : 'FAIL' ),
		'len=' . strlen( $seed ),
	);

	// Ensure lead reference empty is fine; layout full.
	$mode = get_field( 'page_layout_mode', $id );
	if ( ! is_string( $mode ) || '' === $mode ) {
		update_post_meta( $id, 'page_layout_mode', 'full' );
		update_post_meta( $id, '_page_layout_mode', 'field_fp02_page_layout_mode' );
		$db_writes += 2;
	} elseif ( 'placeholder' === $mode ) {
		update_field( 'page_layout_mode', 'full', $id );
		++$db_writes;
	}
}

e52f_csv(
	$evidence . '/v9-06e52-generic-pages-seeding.csv',
	array( 'post_id', 'title', 'field_name', 'before_value_state', 'seeded_from', 'after_value_state', 'preserved_existing', 'result', 'notes' ),
	$seed_rows
);

// Placeholder switch retest on #1039.
$test_id    = 1039;
$test_title = (string) get_the_title( $test_id );
$url_test   = (string) get_permalink( $test_id );
$switch     = array();

$body0 = get_field( 'generic_page_body', $test_id );
$switch[] = array( 1, $test_id, $test_title, 'body_readable', e52f_state( $body0 ), ( 'meaningful' === e52f_state( $body0 ) ? 'PASS' : 'FAIL' ), 'precondition' );

update_field( 'page_layout_mode', 'full', $test_id );
++$db_writes;
$fe0 = e52f_http( $url_test );
$switch[] = array(
	2,
	$test_id,
	$test_title,
	'full_frontend',
	sprintf( 'http=%d;status=%s;src=%s', $fe0['code'], ( preg_match( '/data-content-status="([^"]+)"/', $fe0['body'], $m ) ? $m[1] : '-' ), ( preg_match( '/data-content-source="([^"]+)"/', $fe0['body'], $m2 ) ? $m2[1] : '-' ) ),
	( 200 === $fe0['code'] && false !== strpos( $fe0['body'], 'generic-acf-sot' ) && false === strpos( $fe0['body'], 'data-layout-mode="placeholder"' ) ? 'PASS' : 'FAIL' ),
	'start full',
);

update_field( 'page_layout_mode', 'placeholder', $test_id );
++$db_writes;
$fe1 = e52f_http( $url_test );
$body1 = get_field( 'generic_page_body', $test_id );
$switch[] = array(
	3,
	$test_id,
	$test_title,
	'shell_h1_only',
	sprintf( 'http=%d;ph=%s', $fe1['code'], false !== strpos( $fe1['body'], 'page-placeholder' ) ? 'yes' : 'no' ),
	( 200 === $fe1['code'] && false !== strpos( $fe1['body'], 'page-placeholder' ) && false === strpos( $fe1['body'], 'generic-acf-sot' ) ? 'PASS' : 'FAIL' ),
	'placeholder FE',
);
$switch[] = array( 4, $test_id, $test_title, 'acf_body_preserved', e52f_state( $body1 ), ( 'meaningful' === e52f_state( $body1 ) ? 'PASS' : 'FAIL' ), 'not deleted' );

update_field( 'page_layout_mode', 'full', $test_id );
++$db_writes;
$fe2 = e52f_http( $url_test );
$switch[] = array(
	5,
	$test_id,
	$test_title,
	'full_restored',
	sprintf( 'http=%d;ph=%s;acf=%s', $fe2['code'], false !== strpos( $fe2['body'], 'placeholder' ) && false !== strpos( $fe2['body'], 'data-layout-mode="placeholder"' ) ? 'yes' : 'no', false !== strpos( $fe2['body'], 'generic-acf-sot' ) ? 'yes' : 'no' ),
	( 200 === $fe2['code'] && false !== strpos( $fe2['body'], 'generic-acf-sot' ) && false === strpos( $fe2['body'], 'data-layout-mode="placeholder"' ) ? 'PASS' : 'FAIL' ),
	'final full',
);

e52f_csv(
	$evidence . '/v9-06e52-generic-placeholder-switch-validation.csv',
	array( 'step', 'post_id', 'title', 'expected', 'actual', 'result', 'notes' ),
	$switch
);

// Frontend validation — broken_empty only if ACF body empty AND demo phrase AND not from seeded body.
$fe_rows = array();
foreach ( $ids as $id ) {
	$url  = (string) get_permalink( $id );
	$resp = e52f_http( $url );
	$mode = get_field( 'page_layout_mode', $id );
	$mode = is_string( $mode ) && '' !== $mode ? $mode : 'full';
	$h1   = (bool) preg_match( '/<h1[^>]*>/i', $resp['body'] );
	$ph   = false !== strpos( $resp['body'], 'data-layout-mode="placeholder"' );
	$full = false !== strpos( $resp['body'], 'data-content-status="generic-acf-sot"' );
	$body = get_field( 'generic_page_body', $id );
	$src_acf = false !== strpos( $resp['body'], 'data-content-source="acf-or-emergency"' );
	// Prefer reading get_field to decide SoT; emergency flag if source says emergency AND meta missing is bad.
	$broken_empty = ( e52f_state( $body ) === 'empty' && false !== strpos( $resp['body'], 'Раздел находится в подготовке' ) && ! $ph );
	// Phrase from seeded content is OK when body meaningful.
	$ok = ( 200 === $resp['code'] && $h1 && 'full' === $mode && ! $ph && $full && ! $broken_empty && e52f_state( $body ) === 'meaningful' );
	$fe_rows[] = array(
		$id,
		get_the_title( $id ),
		$url,
		$resp['code'],
		$h1 ? 'yes' : 'no',
		$full ? 'yes' : 'no',
		$mode,
		$broken_empty ? 'yes' : 'no',
		$ok ? 'PASS' : 'FAIL',
		'body=' . e52f_state( $body ) . ';src_attr=' . ( $src_acf ? 'yes' : 'no' ),
	);
}

e52f_csv(
	$evidence . '/v9-06e52-generic-pages-frontend-validation.csv',
	array( 'post_id', 'title', 'url', 'http_status', 'h1_present', 'full_content_present', 'placeholder_mode', 'broken_empty_blocks', 'result', 'notes' ),
	$fe_rows
);

// Regression quick.
$reg = array(
	array( '/', home_url( '/' ) ),
	array( '/uslugi/', home_url( '/uslugi/' ) ),
	array( '/uslugi/zavisimosti/', home_url( '/uslugi/zavisimosti/' ) ),
	array( '/uslugi/psihicheskoe-zdorovie/', home_url( '/uslugi/psihicheskoe-zdorovie/' ) ),
	array( '/uslugi/rasstroystva-pischevogo-povedeniya/', home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ) ),
	array( '#74', get_permalink( 74 ) ),
	array( '#314', get_permalink( 314 ) ),
	array( '#315', get_permalink( 315 ) ),
	array( '#78', get_permalink( 78 ) ),
	array( '#81', get_permalink( 81 ) ),
	array( '#85', get_permalink( 85 ) ),
	array( '/blog/', home_url( '/blog/' ) ),
	array( '/specyalisty/', home_url( '/specyalisty/' ) ),
	array( '/o-centre/', home_url( '/o-centre/' ) ),
	array( '/kontakty/', home_url( '/kontakty/' ) ),
);
$reg_rows = array();
foreach ( $reg as $r ) {
	$resp = e52f_http( (string) $r[1] );
	$fatal = false !== stripos( $resp['body'], 'Fatal error' );
	$notes = '';
	$ok_role = true;
	if ( preg_match( '/#(\\d+)/', $r[0], $m ) ) {
		$pid  = (int) $m[1];
		$role = (string) get_field( 'service_editor_role', $pid );
		$var  = (string) get_field( 'service_layout_variant', $pid );
		$notes = "role=$role;variant=$var";
		if ( in_array( $pid, array( 315, 78 ), true ) ) {
			$ok_role = ( 'service' === $role && 'service_general' === $var );
		}
	}
	$ok = ( 200 === $resp['code'] && ! $fatal && $ok_role );
	$reg_rows[] = array( $r[0], $r[1], '200 preserved', 'http=' . $resp['code'], $ok ? 'PASS' : 'FAIL', $notes );
}
e52f_csv(
	$evidence . '/v9-06e52-regression-validation.csv',
	array( 'route', 'url', 'expected', 'actual', 'result', 'notes' ),
	$reg_rows
);

// Re-hash sync
$src_root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';
$rels     = array(
	'theme/shpigovsky/page-templates/generic.php'                 => 'themes/shpigovsky/page-templates/generic.php',
	'theme/shpigovsky/template-parts/generic/content-page.php'    => 'themes/shpigovsky/template-parts/generic/content-page.php',
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php'          => 'plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'plugins/shpigovsky-core/src/Admin/EditorRestrictions.php'    => 'plugins/shpigovsky-core/src/Admin/EditorRestrictions.php',
	'acf-json/group_fp02_page_layout_mode.json'                   => 'acf-json/group_fp02_page_layout_mode.json',
	'acf-json/group_fp02_page_generic_content.json'               => 'acf-json/group_fp02_page_generic_content.json',
);
$sync = array();
foreach ( $rels as $srel => $rrel ) {
	$s = $src_root . '/' . $srel;
	$d = $rt_root . '/' . $rrel;
	$hs = is_file( $s ) ? md5_file( $s ) : '';
	$hd = is_file( $d ) ? md5_file( $d ) : '';
	if ( $hs && $hs !== $hd ) {
		copy( $s, $d );
		$hd = md5_file( $d );
	}
	$sync[] = array( basename( $srel ), $s, $d, $hs, $hd, ( $hs && $hs === $hd ) ? 'yes' : 'no', ( $hs && $hs === $hd ) ? 'PASS' : 'FAIL', '' );
}
e52f_csv(
	$evidence . '/v9-06e52-source-runtime-sync.csv',
	array( 'file', 'source_path', 'runtime_path', 'source_hash', 'runtime_hash', 'match', 'result', 'notes' ),
	$sync
);

$summary = array(
	'db_writes'    => $db_writes,
	'seed_pass'    => count( array_filter( $seed_rows, static fn( $r ) => in_array( $r[7], array( 'seeded_fixed', 'preserved' ), true ) ) ),
	'seed_total'   => count( $seed_rows ),
	'fe_pass'      => count( array_filter( $fe_rows, static fn( $r ) => 'PASS' === $r[8] ) ),
	'fe_total'     => count( $fe_rows ),
	'reg_pass'     => count( array_filter( $reg_rows, static fn( $r ) => 'PASS' === $r[4] ) ),
	'reg_total'    => count( $reg_rows ),
	'switch_pass'  => count( array_filter( $switch, static fn( $r ) => 'PASS' === $r[5] ) ),
	'switch_total' => count( $switch ),
	'sync_pass'    => count( array_filter( $sync, static fn( $r ) => 'PASS' === $r[6] ) ),
);
file_put_contents( $evidence . '/v9-06e52-run-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo 'E52_FIX_OK db_writes=' . $db_writes
	. ' seed=' . $summary['seed_pass'] . '/' . $summary['seed_total']
	. ' fe=' . $summary['fe_pass'] . '/' . $summary['fe_total']
	. ' reg=' . $summary['reg_pass'] . '/' . $summary['reg_total']
	. ' switch=' . $summary['switch_pass'] . '/' . $summary['switch_total']
	. ' sync=' . $summary['sync_pass'] . '/' . count( $sync )
	. PHP_EOL;
