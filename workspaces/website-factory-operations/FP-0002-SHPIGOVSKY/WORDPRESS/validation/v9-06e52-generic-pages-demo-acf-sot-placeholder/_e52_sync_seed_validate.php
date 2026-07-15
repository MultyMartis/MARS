<?php
/**
 * V9-06E52 — sync source→runtime, seed ACF, placeholder switch test, frontend+regression validation.
 *
 * @package FP0002
 */

declare(strict_types=1);

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require $wp_load;

$evidence    = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root    = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root     = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';
$bak_file    = $evidence . '/v9-06e52-backup-path.txt';
$backup_root = is_file( $bak_file ) ? trim( (string) file_get_contents( $bak_file ) ) : '';
$backup_root = preg_replace( '/^\xEF\xBB\xBF/', '', $backup_root );
$backup_root = trim( (string) $backup_root );

if ( '' === $backup_root || ! is_dir( $backup_root ) ) {
	fwrite( STDERR, "STOP — backup root missing\n" );
	exit( 2 );
}

if ( ! function_exists( 'update_field' ) || ! function_exists( 'get_field' ) ) {
	fwrite( STDERR, "ACF missing\n" );
	exit( 1 );
}

$db_writes = 0;
$ids       = array( 12, 13, 14, 15, 16, 1030, 1031, 1032, 1033, 1039, 1053, 1054, 1055, 1056, 1097 );
$hardcoded = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';

/**
 * @param string            $path Path.
 * @param array<int,string> $header Header.
 * @param array<int,array>  $rows Rows.
 */
function e52_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	if ( ! $fp ) {
		fwrite( STDERR, "Cannot write $path\n" );
		exit( 1 );
	}
	fprintf( $fp, "\xEF\xBB\xBF" );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * @param string $rel Relative under WORDPRESS/.
 * @return array<string,mixed>
 */
function e52_sync( string $rel ): array {
	global $src_root, $rt_root;
	$src = $src_root . '/' . $rel;
	$map = array(
		'theme/shpigovsky/'        => 'themes/shpigovsky/',
		'plugins/shpigovsky-core/' => 'plugins/shpigovsky-core/',
		'acf-json/'                => 'acf-json/',
	);
	$dst = $rt_root . '/' . $rel;
	foreach ( $map as $from => $to ) {
		if ( str_starts_with( $rel, $from ) ) {
			$dst = $rt_root . '/' . $to . substr( $rel, strlen( $from ) );
			break;
		}
	}
	$hash_src = is_file( $src ) ? (string) md5_file( $src ) : '';
	$hash_dst = is_file( $dst ) ? (string) md5_file( $dst ) : '';
	$copied   = false;
	if ( $hash_src && $hash_src !== $hash_dst ) {
		$dir = dirname( $dst );
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}
		copy( $src, $dst );
		$copied   = true;
		$hash_dst = (string) md5_file( $dst );
	}
	return array(
		'file'         => basename( $rel ),
		'source_path'  => $src,
		'runtime_path' => $dst,
		'source_hash'  => $hash_src,
		'runtime_hash' => $hash_dst,
		'match'        => ( $hash_src !== '' && $hash_src === $hash_dst ) ? 'yes' : 'no',
		'result'       => ( $hash_src !== '' && $hash_src === $hash_dst ) ? 'PASS' : 'FAIL',
		'notes'        => $copied ? 'copied' : ( is_file( $dst ) ? 'already_match' : 'missing' ),
	);
}

/**
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e52_http( string $url ): array {
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

/**
 * @param mixed $v Value.
 */
function e52_state( $v ): string {
	if ( null === $v || false === $v || '' === $v || array() === $v ) {
		return 'empty';
	}
	$s = is_string( $v ) ? trim( $v ) : (string) wp_json_encode( $v );
	if ( '' === $s ) {
		return 'empty';
	}
	return 'meaningful';
}

/**
 * Normalize WP block markup to HTML comparable to rendered body text.
 *
 * @param string $html HTML.
 */
function e52_seed_html( string $html ): string {
	$html = trim( $html );
	if ( '' === $html ) {
		return '';
	}
	// Keep Gutenberg blocks — FE applies the_content filters.
	return $html;
}

// ---------------------------------------------------------------------------
// 1. Sync deliverables
// ---------------------------------------------------------------------------
$sync_rels = array(
	'theme/shpigovsky/page-templates/generic.php',
	'theme/shpigovsky/template-parts/generic/content-page.php',
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'plugins/shpigovsky-core/src/Admin/EditorRestrictions.php',
	'acf-json/group_fp02_page_layout_mode.json',
	'acf-json/group_fp02_page_generic_content.json',
);

$sync_rows = array();
foreach ( $sync_rels as $rel ) {
	$sync_rows[] = array_values( e52_sync( $rel ) );
}

// Flush ACF local JSON / field cache by touching load.
if ( function_exists( 'acf_get_store' ) ) {
	$store = acf_get_store( 'local-groups' );
	if ( $store ) {
		$store->reset();
	}
}
if ( function_exists( 'acf_get_field_groups' ) ) {
	acf_get_field_groups();
}

// ---------------------------------------------------------------------------
/* 2. Seed included pages */
// ---------------------------------------------------------------------------
$seed_rows = array();

foreach ( $ids as $id ) {
	$post  = get_post( $id );
	$title = $post ? (string) $post->post_title : (string) $id;
	$pc    = $post ? trim( (string) $post->post_content ) : '';

	$fields = array(
		'generic_page_lead' => array( 'key' => 'field_fp02_generic_page_lead', 'type' => 'lead' ),
		'generic_page_body' => array( 'key' => 'field_fp02_generic_page_body', 'type' => 'body' ),
	);

	foreach ( $fields as $name => $meta ) {
		$before = get_field( $name, $id );
		$bstate = e52_state( $before );
		$seeded_from = '';
		$result      = 'skipped';
		$preserved   = 'n/a';
		$notes       = '';

		if ( 'generic_page_lead' === $name ) {
			// Lead stays empty unless already set — current pages have no separate lead.
			if ( 'empty' !== $bstate ) {
				$preserved = 'yes';
				$result    = 'preserved';
				$notes     = 'existing lead kept';
			} else {
				$preserved = 'n/a';
				$result    = 'left_empty_hide';
				$notes     = 'optional lead empty → hide on FE';
			}
		} else {
			// body
			if ( 'empty' !== $bstate ) {
				$preserved = 'yes';
				$result    = 'preserved';
				$notes     = 'existing ACF body kept';
			} else {
				$seed_val = '';
				if ( '' !== $pc ) {
					$seed_val    = e52_seed_html( $pc );
					$seeded_from = 'post_content';
				} else {
					$seed_val    = '<p>' . esc_html( $hardcoded ) . '</p>';
					$seeded_from = 'previous_hardcoded_demo_text';
				}
				$ok = update_field( $meta['key'], $seed_val, $id );
				if ( $ok ) {
					++$db_writes;
					$result    = 'seeded';
					$preserved = 'no';
					$notes     = 'len=' . strlen( $seed_val );
				} else {
					// Fallback direct meta.
					update_post_meta( $id, $name, $seed_val );
					update_post_meta( $id, '_' . $name, $meta['key'] );
					++$db_writes;
					$result    = 'seeded_meta';
					$preserved = 'no';
					$notes     = 'update_field false; direct meta';
				}
			}
		}

		$after = get_field( $name, $id );
		$seed_rows[] = array(
			$id,
			$title,
			$name,
			$bstate,
			$seeded_from,
			e52_state( $after ),
			$preserved,
			$result,
			$notes,
		);
	}

	// Ensure layout mode = full (do not mass-enable placeholder).
	$mode = get_field( 'page_layout_mode', $id );
	if ( ! is_string( $mode ) || '' === $mode ) {
		update_field( 'field_fp02_page_layout_mode', 'full', $id );
		++$db_writes;
		$seed_rows[] = array( $id, $title, 'page_layout_mode', 'empty', 'default_full', 'meaningful', 'n/a', 'seeded', 'set default full' );
	} elseif ( 'placeholder' === $mode ) {
		$seed_rows[] = array( $id, $title, 'page_layout_mode', 'meaningful', '', 'meaningful', 'yes', 'preserved_placeholder', 'was placeholder — left as-is for operator' );
	} else {
		$seed_rows[] = array( $id, $title, 'page_layout_mode', 'meaningful', '', e52_state( $mode ), 'yes', 'preserved', (string) $mode );
	}
}

e52_csv(
	$evidence . '/v9-06e52-generic-pages-seeding.csv',
	array( 'post_id', 'title', 'field_name', 'before_value_state', 'seeded_from', 'after_value_state', 'preserved_existing', 'result', 'notes' ),
	$seed_rows
);

e52_csv(
	$evidence . '/v9-06e52-source-runtime-sync.csv',
	array( 'file', 'source_path', 'runtime_path', 'source_hash', 'runtime_hash', 'match', 'result', 'notes' ),
	$sync_rows
);

// ---------------------------------------------------------------------------
// 3. Placeholder switch validation on #1039 (Интервью и СМИ)
// ---------------------------------------------------------------------------
$test_id    = 1039;
$test_title = (string) get_the_title( $test_id );
$switch_rows = array();

$mode0 = get_field( 'page_layout_mode', $test_id );
$mode0 = is_string( $mode0 ) && '' !== $mode0 ? $mode0 : 'full';
$switch_rows[] = array( 1, $test_id, $test_title, 'full', $mode0, ( 'full' === $mode0 ? 'PASS' : 'FAIL' ), 'start mode' );

$url_test = (string) get_permalink( $test_id );
$fe0      = e52_http( $url_test );
$has_h1_0 = (bool) preg_match( '/<h1[^>]*>/i', $fe0['body'] );
$has_body_class_0 = false !== strpos( $fe0['body'], 'data-content-status="generic-acf-sot"' ) || false !== strpos( $fe0['body'], 'plain-page-content__body' );
$placeholder_attr_0 = false !== strpos( $fe0['body'], 'data-layout-mode="placeholder"' );
$switch_rows[] = array(
	2,
	$test_id,
	$test_title,
	'full_frontend_content',
	sprintf( 'http=%d;h1=%s;placeholder_attr=%s;body=%s', $fe0['code'], $has_h1_0 ? 'yes' : 'no', $placeholder_attr_0 ? 'yes' : 'no', $has_body_class_0 ? 'yes' : 'no' ),
	( 200 === $fe0['code'] && $has_h1_0 && ! $placeholder_attr_0 ? 'PASS' : 'FAIL' ),
	'before switch',
);

update_field( 'field_fp02_page_layout_mode', 'placeholder', $test_id );
++$db_writes;
$mode1 = get_field( 'page_layout_mode', $test_id );
$switch_rows[] = array( 3, $test_id, $test_title, 'placeholder', (string) $mode1, ( 'placeholder' === $mode1 ? 'PASS' : 'FAIL' ), 'admin-compatible ACF update_field' );

$fe1 = e52_http( $url_test );
$ph1 = false !== strpos( $fe1['body'], 'data-layout-mode="placeholder"' ) || false !== strpos( $fe1['body'], 'data-content-status="page-placeholder"' );
$no_acf_body = false === strpos( $fe1['body'], 'data-content-status="generic-acf-sot"' );
$has_h1_1 = (bool) preg_match( '/<h1[^>]*>/i', $fe1['body'] );
$switch_rows[] = array(
	4,
	$test_id,
	$test_title,
	'shell_h1_only',
	sprintf( 'http=%d;h1=%s;placeholder=%s;acf_block=%s', $fe1['code'], $has_h1_1 ? 'yes' : 'no', $ph1 ? 'yes' : 'no', $no_acf_body ? 'hidden' : 'present' ),
	( 200 === $fe1['code'] && $has_h1_1 && $ph1 && $no_acf_body ? 'PASS' : 'FAIL' ),
	'placeholder frontend',
);

// Confirm ACF body preserved while placeholder.
$body_while = get_field( 'generic_page_body', $test_id );
$switch_rows[] = array(
	5,
	$test_id,
	$test_title,
	'acf_body_preserved',
	e52_state( $body_while ),
	( 'meaningful' === e52_state( $body_while ) ? 'PASS' : 'FAIL' ),
	'content not deleted',
);

update_field( 'field_fp02_page_layout_mode', 'full', $test_id );
++$db_writes;
$mode2 = get_field( 'page_layout_mode', $test_id );
$switch_rows[] = array( 6, $test_id, $test_title, 'full', (string) $mode2, ( 'full' === $mode2 ? 'PASS' : 'FAIL' ), 'restore full' );

$fe2 = e52_http( $url_test );
$ph2 = false !== strpos( $fe2['body'], 'data-layout-mode="placeholder"' );
$acf2 = false !== strpos( $fe2['body'], 'data-content-status="generic-acf-sot"' );
$has_h1_2 = (bool) preg_match( '/<h1[^>]*>/i', $fe2['body'] );
$switch_rows[] = array(
	7,
	$test_id,
	$test_title,
	'full_content_restored',
	sprintf( 'http=%d;h1=%s;placeholder=%s;acf=%s', $fe2['code'], $has_h1_2 ? 'yes' : 'no', $ph2 ? 'yes' : 'no', $acf2 ? 'yes' : 'no' ),
	( 200 === $fe2['code'] && $has_h1_2 && ! $ph2 && $acf2 ? 'PASS' : 'FAIL' ),
	'final must be full',
);

e52_csv(
	$evidence . '/v9-06e52-generic-placeholder-switch-validation.csv',
	array( 'step', 'post_id', 'title', 'expected', 'actual', 'result', 'notes' ),
	$switch_rows
);

// ---------------------------------------------------------------------------
// 4. Frontend validation for included pages
// ---------------------------------------------------------------------------
$fe_rows = array();
foreach ( $ids as $id ) {
	$url  = (string) get_permalink( $id );
	$resp = e52_http( $url );
	$mode = get_field( 'page_layout_mode', $id );
	$mode = is_string( $mode ) && '' !== $mode ? $mode : 'full';
	$h1   = (bool) preg_match( '/<h1[^>]*>/i', $resp['body'] );
	$ph   = false !== strpos( $resp['body'], 'data-layout-mode="placeholder"' );
	$full = false !== strpos( $resp['body'], 'data-content-status="generic-acf-sot"' );
	$broken = ( false !== strpos( $resp['body'], 'Раздел находится в подготовке' ) && e52_state( get_field( 'generic_page_body', $id ) ) === 'empty' );
	// Broken empty demo blocks = body empty but hardcoded still injected (should not happen).
	$body_acf = get_field( 'generic_page_body', $id );
	$broken_empty = ( e52_state( $body_acf ) === 'empty' && false !== strpos( $resp['body'], 'Раздел находится в подготовке' ) && ! $ph );
	$ok = ( 200 === $resp['code'] && $h1 && 'full' === $mode && ! $ph && $full && ! $broken_empty );
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
		$ph ? 'unexpected_placeholder' : '',
	);
}

e52_csv(
	$evidence . '/v9-06e52-generic-pages-frontend-validation.csv',
	array( 'post_id', 'title', 'url', 'http_status', 'h1_present', 'full_content_present', 'placeholder_mode', 'broken_empty_blocks', 'result', 'notes' ),
	$fe_rows
);

// ---------------------------------------------------------------------------
// 5. Regression
// ---------------------------------------------------------------------------
$reg = array(
	array( 'slug' => '/', 'url' => home_url( '/' ), 'expect' => '200' ),
	array( 'slug' => '/uslugi/', 'url' => home_url( '/uslugi/' ), 'expect' => '200' ),
	array( 'slug' => '/uslugi/zavisimosti/', 'url' => home_url( '/uslugi/zavisimosti/' ), 'expect' => '200;not_placeholder' ),
	array( 'slug' => '/uslugi/psihicheskoe-zdorovie/', 'url' => home_url( '/uslugi/psihicheskoe-zdorovie/' ), 'expect' => '200;not_placeholder' ),
	array( 'slug' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'url' => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), 'expect' => '200;not_placeholder' ),
	array( 'slug' => '#74', 'url' => get_permalink( 74 ), 'expect' => '200;role_service' ),
	array( 'slug' => '#314', 'url' => get_permalink( 314 ), 'expect' => '200;role_service' ),
	array( 'slug' => '#315', 'url' => get_permalink( 315 ), 'expect' => '200;Услуга' ),
	array( 'slug' => '#78', 'url' => get_permalink( 78 ), 'expect' => '200;Услуга' ),
	array( 'slug' => '#81', 'url' => get_permalink( 81 ), 'expect' => '200;role_service' ),
	array( 'slug' => '#85', 'url' => get_permalink( 85 ), 'expect' => '200;role_service' ),
	array( 'slug' => '/blog/', 'url' => home_url( '/blog/' ), 'expect' => '200' ),
	array( 'slug' => '/specyalisty/', 'url' => home_url( '/specyalisty/' ), 'expect' => '200' ),
	array( 'slug' => '/o-centre/', 'url' => home_url( '/o-centre/' ), 'expect' => '200' ),
	array( 'slug' => '/kontakty/', 'url' => home_url( '/kontakty/' ), 'expect' => '200' ),
);

$reg_rows = array();
foreach ( $reg as $r ) {
	$url  = (string) $r['url'];
	$resp = e52_http( $url );
	$fatal = false !== stripos( $resp['body'], 'Fatal error' ) || false !== stripos( $resp['body'], 'Uncaught Error' );
	$ph    = false !== strpos( $resp['body'], 'data-layout-mode="placeholder"' ) || false !== strpos( $resp['body'], 'placeholder-stack' );
	$role  = '';
	$notes = '';
	$id_m  = array();
	if ( preg_match( '/#(\\d+)/', $r['slug'], $id_m ) ) {
		$pid  = (int) $id_m[1];
		$role = (string) get_field( 'service_editor_role', $pid );
		$var  = (string) get_field( 'service_layout_variant', $pid );
		$notes = "role=$role;variant=$var";
		if ( in_array( $pid, array( 315, 78 ), true ) ) {
			$ok_role = ( 'service' === $role && 'service_general' === $var );
		} else {
			$ok_role = ( 'placeholder' !== $role && 'placeholder' !== $var );
		}
	} else {
		$ok_role = true;
	}
	$ok = ( 200 === $resp['code'] && ! $fatal && $ok_role );
	if ( false !== strpos( $r['expect'], 'not_placeholder' ) && $ph && false !== strpos( $url, '/uslugi/' ) ) {
		// section pages shouldn't be placeholder layout
		$ok = false;
		$notes .= ';unexpected_ph';
	}
	if ( in_array( $r['slug'], array( '#315', '#78' ), true ) && ( 'service' !== $role ) ) {
		$ok = false;
	}
	$reg_rows[] = array(
		$r['slug'],
		$url,
		$r['expect'],
		sprintf( 'http=%d;fatal=%s;%s', $resp['code'], $fatal ? 'yes' : 'no', $notes ),
		$ok ? 'PASS' : 'FAIL',
		$notes,
	);
}

e52_csv(
	$evidence . '/v9-06e52-regression-validation.csv',
	array( 'route', 'url', 'expected', 'actual', 'result', 'notes' ),
	$reg_rows
);

// Empty-field spot check: temporarily clear lead on a page (already empty) — clear body on temp copy? 
// Safer: create temporary clear of lead only (already empty) and verify no demo for empty lead section.
// Also verify optional empty lead does not inject text.

$summary = array(
	'backup_root' => $backup_root,
	'db_writes'   => $db_writes,
	'sync_pass'   => count( array_filter( $sync_rows, static fn( $r ) => 'PASS' === $r[6] ) ),
	'sync_total'  => count( $sync_rows ),
	'fe_pass'     => count( array_filter( $fe_rows, static fn( $r ) => 'PASS' === $r[8] ) ),
	'fe_total'    => count( $fe_rows ),
	'reg_pass'    => count( array_filter( $reg_rows, static fn( $r ) => 'PASS' === $r[4] ) ),
	'reg_total'   => count( $reg_rows ),
	'switch_pass' => count( array_filter( $switch_rows, static fn( $r ) => 'PASS' === $r[5] ) ),
	'switch_total'=> count( $switch_rows ),
	'seeded_body' => count( array_filter( $seed_rows, static fn( $r ) => 'generic_page_body' === $r[2] && str_starts_with( (string) $r[7], 'seeded' ) ) ),
);

file_put_contents( $evidence . '/v9-06e52-run-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo 'E52_RUN_OK db_writes=' . $db_writes . ' sync=' . $summary['sync_pass'] . '/' . $summary['sync_total']
	. ' fe=' . $summary['fe_pass'] . '/' . $summary['fe_total']
	. ' reg=' . $summary['reg_pass'] . '/' . $summary['reg_total']
	. ' switch=' . $summary['switch_pass'] . '/' . $summary['switch_total']
	. ' seeded_body=' . $summary['seeded_body'] . PHP_EOL;
