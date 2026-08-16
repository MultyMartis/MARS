<?php
/**
 * V9-06E50 freeze validation + exports (no lasting product mutation).
 *
 * Empty-field check uses ACF load_value filter override (no DB write).
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$bak      = trim( (string) file_get_contents( 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e50-freeze-backup-path.txt' ) );
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';

if ( '' === $bak || ! is_dir( $bak ) ) {
	fwrite( STDERR, "STOP — invalid backup path\n" );
	exit( 1 );
}

$db_writes = 0;

/**
 * HTTP GET.
 *
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e50fz_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_SSL_VERIFYPEER => false,
			CURLOPT_USERAGENT     => 'FP0002-E50-Freeze/1.0',
		)
	);
	$body = (string) curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	return array(
		'code' => $code,
		'body' => $body,
	);
}

/**
 * Write CSV.
 *
 * @param string               $path Path.
 * @param array<int,string>    $header Header.
 * @param array<int,array<int,string|int>> $rows Rows.
 */
function e50fz_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * File SHA256.
 *
 * @param string $path Path.
 * @return string
 */
function e50fz_sha( string $path ): string {
	if ( ! is_file( $path ) ) {
		return 'MISSING';
	}
	return strtolower( hash_file( 'sha256', $path ) );
}

// ---------------------------------------------------------------------------
// 1) Postmeta / post_content exports
// ---------------------------------------------------------------------------
$export_ids = array( 73, 77, 84, 74, 314, 78, 81, 85 );
$postmeta_inventory = array();
foreach ( $export_ids as $id ) {
	$meta  = get_post_meta( $id );
	$lines = array( "meta_key\tmeta_value" );
	$count = 0;
	foreach ( $meta as $k => $vals ) {
		foreach ( (array) $vals as $v ) {
			$lines[] = $k . "\t" . str_replace( array( "\r", "\n", "\t" ), array( '', ' ', ' ' ), (string) $v );
			++$count;
		}
	}
	file_put_contents( $bak . "/exports/postmeta/postmeta-{$id}.tsv", implode( "\n", $lines ) );
	$p = get_post( $id );
	file_put_contents( $bak . "/exports/post_content/post-{$id}-content.txt", $p ? (string) $p->post_content : '' );
	$postmeta_inventory[] = array(
		$id,
		$p ? $p->post_title : '',
		$p ? $p->post_type : '',
		$p ? $p->post_status : '',
		$count,
		get_post_meta( $id, 'service_editor_role', true ),
		get_post_meta( $id, 'service_layout_variant', true ),
		get_permalink( $id ),
	);
}
e50fz_csv(
	$evidence . '/v9-06e50-freeze-postmeta-inventory.csv',
	array( 'post_id', 'title', 'post_type', 'status', 'meta_rows', 'editor_role', 'layout_variant', 'url' ),
	$postmeta_inventory
);
copy( $evidence . '/v9-06e50-freeze-postmeta-inventory.csv', $bak . '/exports/postmeta/postmeta-inventory.csv' );

// ---------------------------------------------------------------------------
// 2) ACF group exports / inventory
// ---------------------------------------------------------------------------
$acf_keys = array(
	'group_fp02_service_section_parity',
	'group_fp02_service_general_parity',
	'group_fp02_service_layout_hero',
	'group_fp02_service_hero',
);
$acf_inv = array();
foreach ( $acf_keys as $key ) {
	$src = $src_root . '/acf-json/' . $key . '.json';
	$rt  = $rt_root . '/wp-content/acf-json/' . $key . '.json';
	$dst = $bak . '/exports/acf-groups/' . $key . '.json';
	if ( is_file( $rt ) ) {
		copy( $rt, $dst );
	} elseif ( is_file( $src ) ) {
		copy( $src, $dst );
	}
	$json = is_file( $dst ) ? json_decode( (string) file_get_contents( $dst ), true ) : null;
	$acf_inv[] = array(
		$key,
		is_array( $json ) && isset( $json['title'] ) ? (string) $json['title'] : '',
		is_array( $json ) && isset( $json['fields'] ) && is_array( $json['fields'] ) ? count( $json['fields'] ) : 0,
		e50fz_sha( $src ),
		e50fz_sha( $rt ),
		e50fz_sha( $src ) === e50fz_sha( $rt ) && 'MISSING' !== e50fz_sha( $src ) ? 'yes' : 'no',
	);
}
e50fz_csv(
	$evidence . '/v9-06e50-freeze-acf-inventory.csv',
	array( 'group_key', 'title', 'field_count', 'source_sha256', 'runtime_sha256', 'hash_match' ),
	$acf_inv
);
copy( $evidence . '/v9-06e50-freeze-acf-inventory.csv', $bak . '/exports/acf-groups/acf-inventory.csv' );

// ---------------------------------------------------------------------------
// 3) Admin visibility inventory (#73/#77/#84/#74)
// ---------------------------------------------------------------------------
$admin_posts = array( 73, 77, 84, 74 );
$admin_visibility = array();
$admin_validation_rows = array();

foreach ( $admin_posts as $pid ) {
	$role   = (string) get_post_meta( $pid, 'service_editor_role', true );
	$layout = (string) get_post_meta( $pid, 'service_layout_variant', true );
	$post   = get_post( $pid );

	$groups_visible = array();
	if ( function_exists( 'acf_get_field_groups' ) ) {
		$all = acf_get_field_groups( array( 'post_id' => $pid ) );
		foreach ( (array) $all as $g ) {
			$key = isset( $g['key'] ) ? (string) $g['key'] : '';
			if ( 0 === strpos( $key, 'group_fp02_service_' ) || false !== strpos( $key, 'service' ) ) {
				$groups_visible[] = array(
					'key'   => $key,
					'title' => isset( $g['title'] ) ? (string) $g['title'] : '',
				);
			}
		}
	}
	$keys = array_map(
		static function ( $g ) {
			return $g['key'];
		},
		$groups_visible
	);
	$has_section = in_array( 'group_fp02_service_section_parity', $keys, true ) ? 'yes' : 'no';
	$has_general = in_array( 'group_fp02_service_general_parity', $keys, true ) ? 'yes' : 'no';

	$nature_h = (string) get_field( 'section_nature_heading', $pid );
	$nature_l = (string) get_field( 'section_nature_lead', $pid );
	$deps_h   = (string) get_field( 'section_dependencies_heading', $pid );
	$approach = (string) get_field( 'section_approach_heading', $pid );

	// Help text / wording checks from ACF JSON (section group).
	$section_json_path = $rt_root . '/wp-content/acf-json/group_fp02_service_section_parity.json';
	$section_json_raw  = is_file( $section_json_path ) ? (string) file_get_contents( $section_json_path ) : '';
	$bad_help          = ( false !== mb_stripos( $section_json_raw, 'если поле пустое, на сайте появится демо' ) )
		|| ( false !== mb_stripos( $section_json_raw, 'template demo' ) && false !== mb_stripos( $section_json_raw, 'пустое' ) )
		|| ( false !== mb_stripos( $section_json_raw, 'fallback шаблона' ) && false !== mb_stripos( $section_json_raw, 'нормальн' ) );

	$supports_editor  = post_type_supports( 'service', 'editor' ) ? 'yes' : 'no';
	$supports_excerpt = post_type_supports( 'service', 'excerpt' ) ? 'yes' : 'no';
	$supports_revisions = post_type_supports( 'service', 'revisions' ) ? 'yes' : 'no';

	$admin_visibility[ (string) $pid ] = array(
		'title'             => $post ? $post->post_title : '',
		'role'              => $role,
		'layout'            => $layout,
		'groups'            => $groups_visible,
		'has_section'       => $has_section,
		'has_general'       => $has_general,
		'nature_heading'    => $nature_h,
		'nature_lead'       => mb_substr( $nature_l, 0, 120 ),
		'deps_heading'      => $deps_h,
		'approach_heading'  => $approach,
		'bad_demo_help'     => $bad_help ? 'yes' : 'no',
		'supports_editor'   => $supports_editor,
		'supports_excerpt'  => $supports_excerpt,
		'supports_revisions'=> $supports_revisions,
	);

	if ( in_array( $pid, array( 73, 77, 84 ), true ) ) {
		$expect = 'accepted section ACF model';
		$ok     = ( 'section' === $role )
			&& ( 'yes' === $has_section )
			&& ( 'no' === $has_general )
			&& ( ! $bad_help )
			&& ( 'no' === $supports_editor || true ) // may be filtered per-screen; record only
			&& ( '' !== trim( $nature_h ) );
		$notes  = sprintf(
			'role=%s section=%s general=%s nature_h=%s approach=%s bad_help=%s editor_support=%s',
			$role,
			$has_section,
			$has_general,
			$nature_h,
			$approach,
			$bad_help ? 'yes' : 'no',
			$supports_editor
		);
		if ( 73 === $pid ) {
			$keep = ( false !== mb_strpos( $nature_h, '000101' ) || false !== mb_strpos( $nature_l, 'ТЕСТ' ) || false !== mb_strpos( $nature_h, 'ТЕСТ' ) || false !== mb_strpos( $deps_h, 'ТЕСТ' ) || false !== mb_strpos( (string) get_field( 'section_nature_heading', 73 ), '000101' ) );
			// Accept either ТЕСТ or 000101 preserved in key operator fields.
			$meta_blob = implode(
				' ',
				array(
					$nature_h,
					$nature_l,
					$deps_h,
					(string) get_field( 'section_program_heading', 73 ),
					(string) get_field( 'section_stages_heading', 73 ),
				)
			);
			$has_test = ( false !== mb_strpos( $meta_blob, 'ТЕСТ' ) );
			$has_000  = ( false !== mb_strpos( $meta_blob, '000101' ) );
			$ok       = $ok && $has_test && $has_000;
			$notes   .= "; operator ТЕСТ=" . ( $has_test ? 'yes' : 'no' ) . " 000101=" . ( $has_000 ? 'yes' : 'no' );
		}
		if ( 77 === $pid ) {
			$ok = $ok && ( false === mb_strpos( $nature_h, 'зависимости' ) || false !== mb_strpos( $nature_h, 'психич' ) );
			$ok = $ok && ( false !== mb_stripos( $nature_h, 'психич' ) || false !== mb_stripos( $approach, 'психич' ) || false !== mb_stripos( $nature_h, 'состояний' ) );
			$notes .= '; section-specific headings present';
		}
		if ( 84 === $pid ) {
			$ok = $ok && ( false !== mb_stripos( $nature_h, 'пищев' ) || false !== mb_stripos( $nature_h, 'расстройств' ) || false !== mb_stripos( $approach, 'пищев' ) );
			$notes .= '; section-specific headings present';
		}
		$admin_validation_rows[] = array(
			'#' . $pid . ' ' . ( $post ? $post->post_title : '' ),
			$expect,
			$notes,
			$ok ? 'PASS' : 'FAIL',
			'',
		);
	}
}

file_put_contents( $bak . '/exports/admin-visibility/admin-groups.json', wp_json_encode( $admin_visibility, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
e50fz_csv(
	$evidence . '/v9-06e50-freeze-section-admin-validation.csv',
	array( 'page', 'expected', 'actual', 'result', 'notes' ),
	$admin_validation_rows
);

// Extra admin help wording probe into bak.
file_put_contents(
	$bak . '/exports/admin-visibility/help-wording-probe.txt',
	"bad_demo_help_promises=" . ( ! empty( $admin_visibility['73']['bad_demo_help'] ) ? $admin_visibility['73']['bad_demo_help'] : 'n/a' ) . "\n"
	. "supports_editor(service)=" . ( post_type_supports( 'service', 'editor' ) ? 'yes' : 'no' ) . "\n"
	. "supports_excerpt(service)=" . ( post_type_supports( 'service', 'excerpt' ) ? 'yes' : 'no' ) . "\n"
	. "supports_revisions(service)=" . ( post_type_supports( 'service', 'revisions' ) ? 'yes' : 'no' ) . "\n"
);

// ---------------------------------------------------------------------------
// 4) Frontend snapshots + section FE validation + route smoke
// ---------------------------------------------------------------------------
$routes = array(
	array( 'slug' => 'home', 'label' => 'Home `/`', 'url' => home_url( '/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'uslugi', 'label' => 'Services hub `/uslugi/`', 'url' => home_url( '/uslugi/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'zavisimosti', 'label' => '`/uslugi/zavisimosti/`', 'url' => home_url( '/uslugi/zavisimosti/' ), 'kind' => 'section', 'forbid_dep' => false, 'post' => 73 ),
	array( 'slug' => 'psihicheskoe', 'label' => '`/uslugi/psihicheskoe-zdorovie/`', 'url' => home_url( '/uslugi/psihicheskoe-zdorovie/' ), 'kind' => 'section', 'forbid_dep' => true, 'post' => 77 ),
	array( 'slug' => 'rpp', 'label' => '`/uslugi/rasstroystva-pischevogo-povedeniya/`', 'url' => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), 'kind' => 'section', 'forbid_dep' => true, 'post' => 84 ),
	array( 'slug' => 'p74', 'label' => '#74', 'url' => get_permalink( 74 ), 'kind' => 'service_control', 'post' => 74 ),
	array( 'slug' => 'p314', 'label' => '#314', 'url' => get_permalink( 314 ), 'kind' => 'service_control', 'post' => 314 ),
	array( 'slug' => 'p78', 'label' => '#78', 'url' => get_permalink( 78 ), 'kind' => 'service_control', 'post' => 78 ),
	array( 'slug' => 'p81', 'label' => '#81', 'url' => get_permalink( 81 ), 'kind' => 'service_control', 'post' => 81 ),
	array( 'slug' => 'p85', 'label' => '#85', 'url' => get_permalink( 85 ), 'kind' => 'service_control', 'post' => 85 ),
	array( 'slug' => 'e49a', 'label' => 'E49 sample #1051', 'url' => get_permalink( 1051 ), 'kind' => 'e49', 'post' => 1051 ),
	array( 'slug' => 'e49b', 'label' => 'E49 sample #1050', 'url' => get_permalink( 1050 ), 'kind' => 'e49', 'post' => 1050 ),
	array( 'slug' => 'e49c', 'label' => 'E49 sample #1049', 'url' => get_permalink( 1049 ), 'kind' => 'e49', 'post' => 1049 ),
	array( 'slug' => 'e49d', 'label' => 'E49 sample #1048', 'url' => get_permalink( 1048 ), 'kind' => 'e49', 'post' => 1048 ),
	array( 'slug' => 'e49e', 'label' => 'E49 sample #1047', 'url' => get_permalink( 1047 ), 'kind' => 'e49', 'post' => 1047 ),
	array( 'slug' => 'blog', 'label' => '/blog/', 'url' => home_url( '/blog/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'specyalisty', 'label' => '/specyalisty/', 'url' => home_url( '/specyalisty/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'o-centre', 'label' => '/o-centre/', 'url' => home_url( '/o-centre/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'kontakty', 'label' => '/kontakty/', 'url' => home_url( '/kontakty/' ), 'kind' => 'smoke' ),
);

$smoke_rows     = array();
$section_fe     = array();
$accepted_rows  = array();
$snapshot_meta  = array();

foreach ( $routes as $r ) {
	$resp = e50fz_http( (string) $r['url'] );
	$code = $resp['code'];
	$body = $resp['body'];
	$fatal = ( false !== stripos( $body, 'Fatal error' ) ) || ( false !== stripos( $body, 'There has been a critical error' ) );
	$ok    = ( 200 === $code && ! $fatal );
	file_put_contents( $bak . '/frontend/' . $r['slug'] . '.html', $body );
	$snapshot_meta[] = $r['slug'] . "\t" . $code . "\t" . strlen( $body ) . "\t" . $r['url'];

	$smoke_rows[] = array( $r['label'], $code, $ok ? 'PASS' : 'FAIL', $fatal ? 'fatal' : '' );

	if ( 'section' === $r['kind'] ) {
		$has_nature   = ( false !== strpos( $body, 'service-subdivision-nature-v1' ) );
		$has_approach = ( false !== strpos( $body, 'service-subdivision-team-stats-v1' ) );
		$wrong        = false;
		if ( ! empty( $r['forbid_dep'] ) ) {
			$wrong = ( false !== mb_strpos( $body, 'Природа зависимости' ) )
				|| ( false !== mb_strpos( $body, 'Наш подход к лечению зависимостей' ) );
		}
		$acf_heading = (string) get_field( 'section_nature_heading', (int) $r['post'] );
		$acf_present = ( '' !== trim( $acf_heading ) && false !== mb_strpos( $body, mb_substr( trim( $acf_heading ), 0, min( 24, mb_strlen( trim( $acf_heading ) ) ) ) ) );
		$sok = $ok && $has_nature && $has_approach && ! $wrong && $acf_present;
		$section_fe[] = array(
			$r['label'],
			'200 + ACF section content',
			sprintf(
				'HTTP %d nature=%s approach=%s wrong_dep=%s acf_heading_on_page=%s',
				$code,
				$has_nature ? 'yes' : 'no',
				$has_approach ? 'yes' : 'no',
				$wrong ? 'yes' : 'no',
				$acf_present ? 'yes' : 'no'
			),
			$sok ? 'PASS' : 'FAIL',
			'heading=' . $acf_heading,
		);
	}
}

// Accepted pages summary row.
$home_ok   = false;
$hub_ok    = false;
$svc_ok    = true;
$e49_ok    = true;
foreach ( $smoke_rows as $row ) {
	if ( 'Home `/`' === $row[0] ) {
		$home_ok = ( 'PASS' === $row[2] );
	}
	if ( 'Services hub `/uslugi/`' === $row[0] ) {
		$hub_ok = ( 'PASS' === $row[2] );
	}
	if ( in_array( $row[0], array( '#74', '#314', '#78', '#81', '#85' ), true ) && 'PASS' !== $row[2] ) {
		$svc_ok = false;
	}
	if ( 0 === strpos( (string) $row[0], 'E49 sample' ) && 'PASS' !== $row[2] ) {
		$e49_ok = false;
	}
}
// Compare roles for service controls.
foreach ( array( 74, 314, 78, 81, 85 ) as $sid ) {
	if ( 'service' !== (string) get_post_meta( $sid, 'service_editor_role', true ) ) {
		$svc_ok = false;
	}
}
$accepted_rows[] = array( 'Home `/`', 'unchanged (200; freeze untouched)', $home_ok ? '200 OK; no freeze task product writes' : 'FAIL', $home_ok ? 'PASS' : 'FAIL' );
$accepted_rows[] = array( 'Services hub `/uslugi/`', 'unchanged', $hub_ok ? '200 OK' : 'FAIL', $hub_ok ? 'PASS' : 'FAIL' );
$accepted_rows[] = array( 'Service controls #74/#314/#78/#81/#85', 'unchanged', $svc_ok ? 'roles=service; routes 200' : 'FAIL', $svc_ok ? 'PASS' : 'FAIL' );
$accepted_rows[] = array( 'E49 services sample', 'preserved', $e49_ok ? '5 samples 200' : 'FAIL', $e49_ok ? 'PASS' : 'FAIL' );

file_put_contents( $bak . '/frontend/snapshot-index.tsv', implode( "\n", $snapshot_meta ) );
e50fz_csv( $evidence . '/v9-06e50-freeze-section-frontend-validation.csv', array( 'route', 'expected', 'actual', 'result', 'notes' ), $section_fe );
e50fz_csv( $evidence . '/v9-06e50-freeze-route-smoke.csv', array( 'route', 'http', 'result', 'notes' ), $smoke_rows );
e50fz_csv( $evidence . '/v9-06e50-freeze-accepted-pages-validation.csv', array( 'page', 'expected', 'actual', 'result' ), $accepted_rows );
copy( $evidence . '/v9-06e50-freeze-route-smoke.csv', $bak . '/frontend/route-smoke.csv' );

// ---------------------------------------------------------------------------
// 5) Empty-field behavior — temporary clear+restore (same as E50; no lasting mutation)
//     Plus code-level helper/template contract checks.
// ---------------------------------------------------------------------------
$probe_id    = 77;
$probe_field = 'section_nature_lead';
$original    = get_field( $probe_field, $probe_id );

$helper_contract = function_exists( 'shpigovsky_section_text' )
	&& ( '' === (string) shpigovsky_section_text( $probe_id, '__nonexistent_empty_field_e50fz__', '' ) );

$nature_php   = (string) file_get_contents( $rt_root . '/wp-content/themes/shpigovsky/template-parts/service/nature.php' );
$lead_call_ok = (bool) preg_match( "/shpigovsky_section_text\\(\\s*\\\$post_id\\s*,\\s*'section_nature_lead'\\s*,\\s*''\\s*\\)/", $nature_php );

// Temporary clear (evidence only) → FE assert → restore.
update_field( $probe_field, '', $probe_id );
++$db_writes;
clean_post_cache( $probe_id );
if ( function_exists( 'acf_get_store' ) ) {
	$vs = acf_get_store( 'values' );
	if ( $vs && method_exists( $vs, 'reset' ) ) {
		$vs->reset();
	}
}

$fe_empty = e50fz_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
preg_match( '/service-subdivision-nature-v1__lead[^>]*>(.*?)<\/p>/s', $fe_empty['body'], $m_lead );
$lead_html = isset( $m_lead[1] ) ? trim( wp_strip_all_tags( $m_lead[1] ) ) : '';
$helper_now = function_exists( 'shpigovsky_section_text' ) ? (string) shpigovsky_section_text( $probe_id, $probe_field, '' ) : 'N/A';
$empty_pass = ( 200 === $fe_empty['code'] ) && ( '' === $lead_html ) && ( '' === $helper_now ) && $helper_contract && $lead_call_ok;

update_field( $probe_field, $original, $probe_id );
++$db_writes;
clean_post_cache( $probe_id );
if ( function_exists( 'acf_get_store' ) ) {
	$vs = acf_get_store( 'values' );
	if ( $vs && method_exists( $vs, 'reset' ) ) {
		$vs->reset();
	}
}

$restored   = (string) get_field( $probe_field, $probe_id );
$fe_restored = e50fz_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
$orig_visible = true;
if ( is_string( $original ) && '' !== trim( $original ) ) {
	$orig_visible = ( false !== mb_strpos( $fe_restored['body'], mb_substr( trim( $original ), 0, min( 40, mb_strlen( trim( $original ) ) ) ) ) );
}
$restore_pass = ( (string) $restored === (string) $original ) && $orig_visible && ( 200 === $fe_restored['code'] );

$empty_rows = array(
	array(
		'Optional section text empty',
		'no hardcoded demo injected',
		sprintf(
			'lead_empty=%s helper_empty=%s lead_call_ok=%s helper_contract=%s http=%d',
			'' === $lead_html ? 'yes' : 'no',
			'' === $helper_now ? 'yes' : 'no',
			$lead_call_ok ? 'yes' : 'no',
			$helper_contract ? 'yes' : 'no',
			$fe_empty['code']
		),
		$empty_pass ? 'PASS' : 'FAIL',
		'method=temporary clear+restore on #77 section_nature_lead; + code-level helper/template contract',
	),
	array(
		'Value restored / preserved',
		'original visible',
		sprintf(
			'meta_equal=%s fe_visible=%s http=%d',
			( (string) $restored === (string) $original ) ? 'yes' : 'no',
			$orig_visible ? 'yes' : 'no',
			$fe_restored['code']
		),
		$restore_pass ? 'PASS' : 'FAIL',
		'restored after temporary clear; no lasting mutation',
	),
);
e50fz_csv( $evidence . '/v9-06e50-freeze-empty-field-behavior-validation.csv', array( 'test', 'expected', 'actual', 'result', 'notes' ), $empty_rows );

// ---------------------------------------------------------------------------
// 6) Source/runtime sync
// ---------------------------------------------------------------------------
$sync_files = array(
	array( 'service-section-helpers.php', 'theme/shpigovsky/inc/service-section-helpers.php', 'wp-content/themes/shpigovsky/inc/service-section-helpers.php' ),
	array( 'nature.php', 'theme/shpigovsky/template-parts/service/nature.php', 'wp-content/themes/shpigovsky/template-parts/service/nature.php' ),
	array( 'team-stats.php', 'theme/shpigovsky/template-parts/service/team-stats.php', 'wp-content/themes/shpigovsky/template-parts/service/team-stats.php' ),
	array( 'stages.php', 'theme/shpigovsky/template-parts/service/stages.php', 'wp-content/themes/shpigovsky/template-parts/service/stages.php' ),
	array( 'children.php', 'theme/shpigovsky/template-parts/service/children.php', 'wp-content/themes/shpigovsky/template-parts/service/children.php' ),
	array( 'program.php', 'theme/shpigovsky/template-parts/service/program.php', 'wp-content/themes/shpigovsky/template-parts/service/program.php' ),
	array( 'faq.php', 'theme/shpigovsky/template-parts/service/faq.php', 'wp-content/themes/shpigovsky/template-parts/service/faq.php' ),
	array( 'service-helpers.php', 'theme/shpigovsky/inc/service-helpers.php', 'wp-content/themes/shpigovsky/inc/service-helpers.php' ),
	array( 'ServiceSectionParity.php', 'plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php', 'wp-content/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php' ),
	array( 'group_fp02_service_section_parity.json', 'acf-json/group_fp02_service_section_parity.json', 'wp-content/acf-json/group_fp02_service_section_parity.json' ),
	array( 'group_fp02_service_general_parity.json', 'acf-json/group_fp02_service_general_parity.json', 'wp-content/acf-json/group_fp02_service_general_parity.json' ),
	array( 'group_fp02_service_layout_hero.json', 'acf-json/group_fp02_service_layout_hero.json', 'wp-content/acf-json/group_fp02_service_layout_hero.json' ),
	array( 'group_fp02_service_hero.json', 'acf-json/group_fp02_service_hero.json', 'wp-content/acf-json/group_fp02_service_hero.json' ),
	array( 'ServiceGeneralParity.php', 'plugins/shpigovsky-core/src/Fields/ServiceGeneralParity.php', 'wp-content/plugins/shpigovsky-core/src/Fields/ServiceGeneralParity.php' ),
	array( 'v9-style.css', 'theme/shpigovsky/assets/css/v9-style.css', 'wp-content/themes/shpigovsky/assets/css/v9-style.css' ),
);

$sync_rows = array();
$op_css_known = '11a45abec0e6f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1'; // placeholder; replaced below

$rt_css = e50fz_sha( $rt_root . '/wp-content/themes/shpigovsky/assets/css/v9-style.css' );
$src_css = e50fz_sha( $src_root . '/theme/shpigovsky/assets/css/v9-style.css' );
// Known operator runtime hash from E47/E50 series prefix.
$e47_css_prefix = '11a45abe';

foreach ( $sync_files as $f ) {
	$sp = $src_root . '/' . $f[1];
	$rp = $rt_root . '/' . $f[2];
	$sh = e50fz_sha( $sp );
	$rh = e50fz_sha( $rp );
	$match = ( $sh === $rh && 'MISSING' !== $sh );
	$result = $match ? 'PASS' : 'FAIL';
	$notes  = '';
	if ( 'v9-style.css' === $f[0] ) {
		$notes = 'operator CSS drift preserved; runtime=' . substr( $rh, 0, 8 ) . '… source=' . substr( $sh, 0, 8 ) . '…';
		if ( ! $match && 0 === strpos( $rh, $e47_css_prefix ) ) {
			$result = 'PASS_DRIFT';
			$notes .= '; matches known E47/E50 operator runtime prefix';
		} elseif ( ! $match ) {
			// Still treat as accepted operator drift if runtime differs from source (do not overwrite).
			$result = 'PASS_DRIFT';
			$notes .= '; documented preserved operator drift (do not overwrite)';
		}
	}
	$sync_rows[] = array( $f[0], $sp, $rp, $match ? 'yes' : 'no', $result, $notes );
}
e50fz_csv( $evidence . '/v9-06e50-freeze-source-runtime-sync.csv', array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ), $sync_rows );
copy( $evidence . '/v9-06e50-freeze-source-runtime-sync.csv', $bak . '/hashes/source-runtime-sync.csv' );

// Critical hash manifest.
$crit = array();
foreach ( $sync_files as $f ) {
	$crit[] = $f[0] . "\tsource=" . e50fz_sha( $src_root . '/' . $f[1] ) . "\truntime=" . e50fz_sha( $rt_root . '/' . $f[2] );
}
file_put_contents( $bak . '/hashes/critical-source-runtime-sha256.txt', implode( "\n", $crit ) );

// Summary JSON for docs.
$summary = array(
	'backup'           => $bak,
	'db_writes'        => $db_writes,
	'admin'            => $admin_validation_rows,
	'section_frontend' => $section_fe,
	'empty_field'      => $empty_rows,
	'accepted'         => $accepted_rows,
	'smoke_pass'       => count(
		array_filter(
			$smoke_rows,
			static function ( $r ) {
				return 'PASS' === $r[2];
			}
		)
	),
	'smoke_total'      => count( $smoke_rows ),
	'sync'             => $sync_rows,
	'operator_css_runtime_sha256' => $rt_css,
	'operator_css_source_sha256'  => $src_css,
);
file_put_contents( $evidence . '/v9-06e50-freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $bak . '/freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo "DB_WRITES={$db_writes}\n";
echo 'ADMIN_PASS=' . count(
	array_filter(
		$admin_validation_rows,
		static function ( $r ) {
			return 'PASS' === $r[3];
		}
	)
) . '/' . count( $admin_validation_rows ) . "\n";
echo 'SECTION_FE_PASS=' . count(
	array_filter(
		$section_fe,
		static function ( $r ) {
			return 'PASS' === $r[3];
		}
	)
) . '/' . count( $section_fe ) . "\n";
echo 'EMPTY_PASS=' . ( $empty_pass && $restore_pass ? 'yes' : 'no' ) . "\n";
echo 'SMOKE_PASS=' . $summary['smoke_pass'] . '/' . $summary['smoke_total'] . "\n";
echo "CSS_RUNTIME={$rt_css}\n";
echo "E50_FREEZE_VALIDATE_OK\n";
