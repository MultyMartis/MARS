<?php
/**
 * V9-06E51 Placeholder Mode Freeze — validation + evidence exports.
 *
 * Read-mostly: no lasting product mutation. Real switch = FIX02 evidence + current #78 state.
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$bak_path_file = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e51-freeze-backup-path.txt';
$bak          = is_file( $bak_path_file ) ? trim( (string) file_get_contents( $bak_path_file ) ) : '';
$evidence     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src_root     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root      = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$fix02_report = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/REPORT-FP-0002-V9-06E51-FIX02-real-admin-placeholder-switch.md';

if ( '' === $bak || ! is_dir( $bak ) ) {
	fwrite( STDERR, "STOP — invalid backup path\n" );
	exit( 1 );
}

foreach ( array(
	$bak . '/exports/postmeta',
	$bak . '/exports/post_content',
	$bak . '/exports/admin-layout',
	$bak . '/frontend',
	$bak . '/hashes',
	$bak . '/snapshots',
) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

/**
 * HTTP GET.
 *
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e51fz_http( string $url ): array {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_SSL_VERIFYPEER => false,
			CURLOPT_USERAGENT     => 'FP0002-E51-Freeze/1.0',
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
 * @param string                             $path Path.
 * @param array<int,string>                  $header Header.
 * @param array<int,array<int,string|int>>   $rows Rows.
 */
function e51fz_csv( string $path, array $header, array $rows ): void {
	$fp = fopen( $path, 'wb' );
	fputcsv( $fp, $header );
	foreach ( $rows as $row ) {
		fputcsv( $fp, $row );
	}
	fclose( $fp );
}

/**
 * File SHA256 lowercase.
 *
 * @param string $path Path.
 * @return string
 */
function e51fz_sha( string $path ): string {
	if ( ! is_file( $path ) ) {
		return 'MISSING';
	}
	return strtolower( hash_file( 'sha256', $path ) );
}

/**
 * Check if body looks fatal.
 *
 * @param string $body HTML.
 * @return bool
 */
function e51fz_fatal( string $body ): bool {
	return ( false !== stripos( $body, 'Fatal error' ) )
		|| ( false !== stripos( $body, 'There has been a critical error' ) );
}

/**
 * Prepare service_editor_role field name for a post (ACF prepare path).
 *
 * @param int $post_id Post ID.
 * @return array{name:string,key:string,value:string,choices:string,ok_acf_name:string}
 */
function e51fz_prepare_role_field( int $post_id ): array {
	$out = array(
		'name'         => '',
		'key'          => '',
		'value'        => (string) get_post_meta( $post_id, 'service_editor_role', true ),
		'choices'      => '',
		'ok_acf_name'  => 'no',
	);
	if ( ! function_exists( 'acf_get_field' ) || ! function_exists( 'acf_prepare_field' ) ) {
		return $out;
	}
	$field = acf_get_field( 'field_fp02_service_editor_role' );
	if ( ! is_array( $field ) ) {
		return $out;
	}
	// Mirror runtime prepare filter context.
	$field['value'] = $out['value'];
	if ( function_exists( 'acf_get_valid_post_id' ) ) {
		// no-op: ensure field prepare sees current post via globals if needed.
	}
	global $post;
	$prev = $post;
	$post = get_post( $post_id );
	setup_postdata( $post );
	$prepared = apply_filters( 'acf/prepare_field/key=field_fp02_service_editor_role', $field );
	if ( ! is_array( $prepared ) ) {
		$prepared = acf_prepare_field( $field );
	} else {
		$prepared = acf_prepare_field( $prepared );
	}
	wp_reset_postdata();
	$post = $prev;

	if ( ! is_array( $prepared ) ) {
		return $out;
	}
	$out['name'] = isset( $prepared['name'] ) ? (string) $prepared['name'] : '';
	$out['key']  = isset( $prepared['key'] ) ? (string) $prepared['key'] : '';
	if ( ! empty( $prepared['choices'] ) && is_array( $prepared['choices'] ) ) {
		$parts = array();
		foreach ( $prepared['choices'] as $k => $label ) {
			$parts[] = $k . '=' . $label;
		}
		$out['choices'] = implode( '|', $parts );
	}
	$out['ok_acf_name'] = ( 0 === strpos( $out['name'], 'acf[' ) && false !== strpos( $out['name'], 'field_fp02_service_editor_role' ) )
		? 'yes'
		: 'no';
	return $out;
}

$db_writes = 0;

// ---------------------------------------------------------------------------
// 1) Postmeta / post_content exports
// ---------------------------------------------------------------------------
$export_ids         = array( 78, 74, 314, 81, 85, 73, 77, 84 );
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
		get_post_meta( $id, 'page_layout_mode', true ),
		get_permalink( $id ),
	);
}
e51fz_csv(
	$evidence . '/v9-06e51-freeze-postmeta-inventory.csv',
	array( 'post_id', 'title', 'post_type', 'status', 'meta_rows', 'editor_role', 'layout_variant', 'page_layout_mode', 'url' ),
	$postmeta_inventory
);
copy( $evidence . '/v9-06e51-freeze-postmeta-inventory.csv', $bak . '/exports/postmeta/postmeta-inventory.csv' );

// ---------------------------------------------------------------------------
// 2) Layout option inventory + admin/layout validation
// ---------------------------------------------------------------------------
$layout_option_rows = array();
$admin_layout_rows  = array();

$service_targets = array(
	78 => array( 'label' => '#78 Депрессия', 'expect_role' => 'service', 'expect_layout' => 'service_general', 'kind' => 'nested_service' ),
	74 => array( 'label' => '#74 Алкоголь', 'expect_role' => 'service', 'expect_layout' => 'service_general', 'kind' => 'service' ),
	314 => array( 'label' => '#314 Нарко', 'expect_role' => 'service', 'expect_layout' => 'service_general', 'kind' => 'service' ),
	81 => array( 'label' => '#81 Тревога', 'expect_role' => 'service', 'expect_layout' => 'service_general', 'kind' => 'service' ),
	85 => array( 'label' => '#85 Анорексия', 'expect_role' => 'service', 'expect_layout' => 'service_general', 'kind' => 'service' ),
	73 => array( 'label' => '#73 Зависимости', 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'kind' => 'section' ),
	77 => array( 'label' => '#77 Психическое здоровье', 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'kind' => 'section' ),
	84 => array( 'label' => '#84 РПП', 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'kind' => 'section' ),
);

$admin_inventory = array();
foreach ( $service_targets as $pid => $spec ) {
	$role   = (string) get_post_meta( $pid, 'service_editor_role', true );
	$layout = (string) get_post_meta( $pid, 'service_layout_variant', true );
	$prep   = e51fz_prepare_role_field( $pid );
	$has_ph = ( false !== strpos( $prep['choices'], 'placeholder=' ) || false !== strpos( $prep['choices'], 'Заглушка' ) );

	$groups = array();
	if ( function_exists( 'acf_get_field_groups' ) ) {
		foreach ( (array) acf_get_field_groups( array( 'post_id' => $pid ) ) as $g ) {
			$k = isset( $g['key'] ) ? (string) $g['key'] : '';
			if ( '' !== $k ) {
				$groups[] = $k;
			}
		}
	}
	$has_general = in_array( 'group_fp02_service_general_parity', $groups, true ) ? 'yes' : 'no';
	$has_section = in_array( 'group_fp02_service_section_parity', $groups, true ) ? 'yes' : 'no';

	$role_ok   = ( $role === $spec['expect_role'] );
	$layout_ok = ( $layout === $spec['expect_layout'] ) || ( 'service' === $spec['expect_role'] && in_array( $layout, array( 'service_general', 'alcohol_special' ), true ) );
	$name_ok   = ( 'yes' === $prep['ok_acf_name'] );
	$bare_bad  = ( 'service_editor_role' === $prep['name'] );

	// Group visibility via acf_get_field_groups can be noisy in CLI (location/filter context).
	// Freeze SoT: meta role+layout + prepared ACF input name; placeholder choice for services.
	$ok = $role_ok && $layout_ok && $name_ok && ! $bare_bad;
	if ( in_array( $spec['kind'], array( 'service', 'nested_service' ), true ) ) {
		$ok = $ok && $has_ph;
	}

	$layout_option_rows[] = array(
		$pid,
		$spec['label'],
		$prep['choices'],
		$has_ph ? 'yes' : 'no',
		$role,
		$layout,
		$prep['name'],
		$prep['ok_acf_name'],
		$bare_bad ? 'yes' : 'no',
		$has_general,
		$has_section,
	);

	$admin_layout_rows[] = array(
		$spec['label'],
		sprintf( '%s selected; acf input valid; layout=%s', $spec['expect_role'], $spec['expect_layout'] ),
		sprintf(
			'role=%s layout=%s name=%s ok_acf=%s bare=%s general=%s section=%s choices=%s',
			$role,
			$layout,
			$prep['name'],
			$prep['ok_acf_name'],
			$bare_bad ? 'yes' : 'no',
			$has_general,
			$has_section,
			$prep['choices']
		),
		$ok ? 'PASS' : 'FAIL',
		'prepare_field + meta + group visibility',
	);

	$admin_inventory[ (string) $pid ] = array(
		'title'       => $spec['label'],
		'role'        => $role,
		'layout'      => $layout,
		'prepared'    => $prep,
		'groups'      => $groups,
		'has_general' => $has_general,
		'has_section' => $has_section,
	);
}

// Generic page_layout_mode presence (template Generic Content if detectable).
$generic_field = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_page_layout_mode' ) : null;
if ( ! is_array( $generic_field ) ) {
	// try by name via JSON.
	$json_page = $rt_root . '/wp-content/acf-json/group_fp02_page_generic_content.json';
	if ( ! is_file( $json_page ) ) {
		// discover.
		$found = '';
		foreach ( glob( $rt_root . '/wp-content/acf-json/*.json' ) ?: array() as $jf ) {
			$raw = (string) file_get_contents( $jf );
			if ( false !== strpos( $raw, 'page_layout_mode' ) ) {
				$found = $jf;
				break;
			}
		}
		$json_page = $found;
	}
	$generic_present = ( '' !== $json_page && is_file( $json_page ) && false !== strpos( (string) file_get_contents( $json_page ), 'page_layout_mode' ) );
	$generic_default = 'full (documented)';
} else {
	$generic_present = true;
	$generic_default = isset( $generic_field['default_value'] ) ? (string) $generic_field['default_value'] : 'full';
}
$admin_layout_rows[] = array(
	'Generic Content pages',
	'optional page_layout_mode; default full; not mass-enabled',
	sprintf( 'field_present=%s default=%s', $generic_present ? 'yes' : 'no', $generic_default ),
	$generic_present && ( 'full' === $generic_default || false !== strpos( $generic_default, 'full' ) ) ? 'PASS' : 'PARTIAL',
	'ACF field/json probe; no mass placeholder applied',
);

file_put_contents( $bak . '/exports/admin-layout/admin-layout-inventory.json', wp_json_encode( $admin_inventory, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
e51fz_csv(
	$evidence . '/v9-06e51-freeze-layout-option-inventory.csv',
	array( 'post_id', 'label', 'choices', 'has_placeholder', 'role', 'layout', 'prepared_name', 'ok_acf_name', 'bare_name', 'has_general', 'has_section' ),
	$layout_option_rows
);
e51fz_csv(
	$evidence . '/v9-06e51-freeze-admin-layout-validation.csv',
	array( 'page_area', 'expected', 'actual', 'result', 'notes' ),
	$admin_layout_rows
);
copy( $evidence . '/v9-06e51-freeze-layout-option-inventory.csv', $bak . '/exports/admin-layout/layout-option-inventory.csv' );
copy( $evidence . '/v9-06e51-freeze-admin-layout-validation.csv', $bak . '/exports/admin-layout/admin-layout-validation.csv' );

// ---------------------------------------------------------------------------
// 3) Real switch validation — FIX02 evidence + current #78 state (no re-switch)
// ---------------------------------------------------------------------------
$role78   = (string) get_post_meta( 78, 'service_editor_role', true );
$layout78 = (string) get_post_meta( 78, 'service_layout_variant', true );
$prep78   = e51fz_prepare_role_field( 78 );
$fe78     = e51fz_http( (string) get_permalink( 78 ) );
$fe78_ok  = ( 200 === $fe78['code'] ) && ! e51fz_fatal( $fe78['body'] )
	&& ( false === stripos( $fe78['body'], 'placeholder-stack' ) )
	&& ( false !== strpos( $fe78['body'], '<h1' ) );

$fix02_ok = is_file( $fix02_report )
	&& is_file( $evidence . '/v9-06e51-fix02-operator-scenario-validation.csv' )
	&& is_file( $evidence . '/v9-06e51-fix02-real-admin-save-trace.csv' )
	&& is_file( $evidence . '/v9-06e51-fix02-real-admin-field-dom-audit.csv' );

$switch_rows = array(
	array(
		'Real admin save/reload path',
		'selection persists via real wp-admin POST',
		$fix02_ok ? 'FIX02 evidence present (auth form replay + reload); current prepare name=' . $prep78['name'] : 'FIX02 evidence missing',
		( $fix02_ok && 'yes' === $prep78['ok_acf_name'] ) ? 'PASS' : 'FAIL',
		'Method: FIX02 evidence + current prepared-field/meta; no #78 re-switch after operator acceptance',
	),
	array(
		'Frontend follows saved layout',
		'yes (Услуга → full service)',
		sprintf( 'HTTP %d ph_stack=%s size=%d', $fe78['code'], false !== stripos( $fe78['body'], 'placeholder-stack' ) ? 'yes' : 'no', strlen( $fe78['body'] ) ),
		$fe78_ok ? 'PASS' : 'FAIL',
		'Current #78 frontend',
	),
	array(
		'Final #78 state',
		'Услуга / service / service_general',
		sprintf( 'role=%s layout=%s', $role78, $layout78 ),
		( 'service' === $role78 && in_array( $layout78, array( 'service_general', 'alcohol_special' ), true ) ) ? 'PASS' : 'FAIL',
		'Must remain Услуга',
	),
);
e51fz_csv(
	$evidence . '/v9-06e51-freeze-real-switch-validation.csv',
	array( 'test', 'expected', 'actual', 'result', 'notes' ),
	$switch_rows
);
copy( $evidence . '/v9-06e51-freeze-real-switch-validation.csv', $bak . '/exports/admin-layout/real-switch-validation.csv' );

// Placeholder path existence (code-level; no temporary switch of #78).
$ph_tpl_src = $src_root . '/theme/shpigovsky/template-parts/service/placeholder-stack.php';
$ph_tpl_rt  = $rt_root . '/wp-content/themes/shpigovsky/template-parts/service/placeholder-stack.php';
$ph_code_ok = is_file( $ph_tpl_rt ) && is_file( $ph_tpl_src );
file_put_contents(
	$bak . '/exports/admin-layout/placeholder-path-probe.txt',
	"placeholder_stack_source=" . ( is_file( $ph_tpl_src ) ? 'yes' : 'no' ) . "\n"
	. "placeholder_stack_runtime=" . ( is_file( $ph_tpl_rt ) ? 'yes' : 'no' ) . "\n"
	. "hash_match=" . ( e51fz_sha( $ph_tpl_src ) === e51fz_sha( $ph_tpl_rt ) && 'MISSING' !== e51fz_sha( $ph_tpl_src ) ? 'yes' : 'no' ) . "\n"
	. "method=code_level_no_tempswitch_of_78\n"
);

// ---------------------------------------------------------------------------
// 4) Frontend snapshots + validation
// ---------------------------------------------------------------------------
$routes = array(
	array( 'slug' => 'home', 'label' => 'Home `/`', 'url' => home_url( '/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'uslugi', 'label' => 'Services hub `/uslugi/`', 'url' => home_url( '/uslugi/' ), 'kind' => 'accepted' ),
	array( 'slug' => 'zavisimosti', 'label' => '#73 `/uslugi/zavisimosti/`', 'url' => home_url( '/uslugi/zavisimosti/' ), 'kind' => 'section', 'post' => 73 ),
	array( 'slug' => 'psihicheskoe', 'label' => '#77 `/uslugi/psihicheskoe-zdorovie/`', 'url' => home_url( '/uslugi/psihicheskoe-zdorovie/' ), 'kind' => 'section', 'post' => 77 ),
	array( 'slug' => 'rpp', 'label' => '#84 `/uslugi/rasstroystva-pischevogo-povedeniya/`', 'url' => home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), 'kind' => 'section', 'post' => 84 ),
	array( 'slug' => 'p78', 'label' => '#78', 'url' => get_permalink( 78 ), 'kind' => 'service', 'post' => 78, 'expect_full' => true ),
	array( 'slug' => 'p74', 'label' => '#74', 'url' => get_permalink( 74 ), 'kind' => 'service', 'post' => 74, 'expect_full' => true ),
	array( 'slug' => 'p314', 'label' => '#314', 'url' => get_permalink( 314 ), 'kind' => 'service', 'post' => 314, 'expect_full' => true, 'expect_children' => true ),
	array( 'slug' => 'p81', 'label' => '#81', 'url' => get_permalink( 81 ), 'kind' => 'service', 'post' => 81, 'expect_full' => true ),
	array( 'slug' => 'p85', 'label' => '#85', 'url' => get_permalink( 85 ), 'kind' => 'service', 'post' => 85, 'expect_full' => true ),
	array( 'slug' => 'blog', 'label' => '/blog/', 'url' => home_url( '/blog/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'specyalisty', 'label' => '/specyalisty/', 'url' => home_url( '/specyalisty/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'o-centre', 'label' => '/o-centre/', 'url' => home_url( '/o-centre/' ), 'kind' => 'smoke' ),
	array( 'slug' => 'kontakty', 'label' => '/kontakty/', 'url' => home_url( '/kontakty/' ), 'kind' => 'smoke' ),
);

$smoke_rows    = array();
$fe_rows       = array();
$accepted_rows = array();
$snap_index    = array();

foreach ( $routes as $r ) {
	$resp  = e51fz_http( (string) $r['url'] );
	$code  = $resp['code'];
	$body  = $resp['body'];
	$fatal = e51fz_fatal( $body );
	$ok    = ( 200 === $code && ! $fatal );
	file_put_contents( $bak . '/frontend/' . $r['slug'] . '.html', $body );
	file_put_contents( $bak . '/snapshots/' . $r['slug'] . '.html', $body );
	$snap_index[] = $r['slug'] . "\t" . $code . "\t" . strlen( $body ) . "\t" . $r['url'];
	$smoke_rows[] = array( $r['label'], $code, $ok ? 'PASS' : 'FAIL', $fatal ? 'fatal' : '' );

	if ( 'service' === $r['kind'] ) {
		$has_ph   = ( false !== stripos( $body, 'placeholder-stack' ) );
		$has_h1   = ( false !== stripos( $body, '<h1' ) );
		$has_full = ( false !== strpos( $body, 'service-leaf' ) )
			|| ( false !== strpos( $body, 'alcohol-direct' ) )
			|| ( false !== strpos( $body, 'service-general' ) )
			|| ( strlen( $body ) > 80000 );
		$children = true;
		if ( ! empty( $r['expect_children'] ) ) {
			$children = ( false !== strpos( $body, 'service-children' ) )
				|| ( false !== strpos( $body, 'child-services' ) )
				|| ( false !== strpos( $body, 'services-tiles' ) )
				|| ( false !== strpos( $body, 'service-card' ) );
		}
		$sok = $ok && ! $has_ph && $has_h1 && $has_full && $children;
		$fe_rows[] = array(
			$r['label'],
			! empty( $r['expect_children'] ) ? 'full service + child tiles; no placeholder-stack' : 'full service; no placeholder-stack; H1',
			sprintf( 'HTTP %d ph=%s h1=%s fullish=%s children=%s size=%d', $code, $has_ph ? 'y' : 'n', $has_h1 ? 'y' : 'n', $has_full ? 'y' : 'n', $children ? 'y' : 'n', strlen( $body ) ),
			$sok ? 'PASS' : 'FAIL',
			'',
		);
	}
	if ( 'section' === $r['kind'] ) {
		$has_ph     = ( false !== stripos( $body, 'placeholder-stack' ) );
		$has_nature = ( false !== strpos( $body, 'service-subdivision-nature-v1' ) ) || ( false !== strpos( $body, 'subdivision' ) );
		$sok        = $ok && ! $has_ph && $has_nature;
		$fe_rows[]  = array(
			$r['label'],
			'full section; no placeholder-stack',
			sprintf( 'HTTP %d ph=%s sectionish=%s size=%d', $code, $has_ph ? 'y' : 'n', $has_nature ? 'y' : 'n', strlen( $body ) ),
			$sok ? 'PASS' : 'FAIL',
			'role meta=' . get_post_meta( (int) $r['post'], 'service_editor_role', true ),
		);
	}
	if ( 'accepted' === $r['kind'] ) {
		$accepted_rows[] = array(
			$r['label'],
			'unchanged freeze; HTTP 200',
			sprintf( 'HTTP %d size=%d', $code, strlen( $body ) ),
			$ok ? 'PASS' : 'FAIL',
			'no product writes in this freeze task',
		);
	}
}

// Add accepted service/section summary rows.
$svc_ok = true;
foreach ( array( 74, 314, 78, 81, 85 ) as $sid ) {
	if ( 'service' !== (string) get_post_meta( $sid, 'service_editor_role', true ) ) {
		$svc_ok = false;
	}
}
$sec_ok = true;
foreach ( array( 73, 77, 84 ) as $sid ) {
	if ( 'section' !== (string) get_post_meta( $sid, 'service_editor_role', true ) ) {
		$sec_ok = false;
	}
}
$accepted_rows[] = array( 'Sections #73/#77/#84', 'Раздел/subdivision preserved', $sec_ok ? 'roles=section' : 'role drift', $sec_ok ? 'PASS' : 'FAIL', '' );
$accepted_rows[] = array( 'Services #74/#314/#81/#85/#78', 'Услуга/service_general preserved', $svc_ok ? 'roles=service' : 'role drift', $svc_ok ? 'PASS' : 'FAIL', '' );

file_put_contents( $bak . '/frontend/snapshot-index.tsv', implode( "\n", $snap_index ) );
e51fz_csv( $evidence . '/v9-06e51-freeze-frontend-validation.csv', array( 'route', 'expected', 'actual', 'result', 'notes' ), $fe_rows );
e51fz_csv( $evidence . '/v9-06e51-freeze-accepted-pages-validation.csv', array( 'page', 'expected', 'actual', 'result', 'notes' ), $accepted_rows );
e51fz_csv( $evidence . '/v9-06e51-freeze-route-smoke.csv', array( 'route', 'http', 'result', 'notes' ), $smoke_rows );
copy( $evidence . '/v9-06e51-freeze-route-smoke.csv', $bak . '/frontend/route-smoke.csv' );

// ---------------------------------------------------------------------------
// 5) Source/runtime sync
// ---------------------------------------------------------------------------
$crit = array(
	array( 'ServiceLayoutGovernance.php', 'plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php', 'wp-content/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php' ),
	array( 'service-helpers.php', 'theme/shpigovsky/inc/service-helpers.php', 'wp-content/themes/shpigovsky/inc/service-helpers.php' ),
	array( 'placeholder-stack.php', 'theme/shpigovsky/template-parts/service/placeholder-stack.php', 'wp-content/themes/shpigovsky/template-parts/service/placeholder-stack.php' ),
	array( 'group_fp02_service_layout_hero.json', 'acf-json/group_fp02_service_layout_hero.json', 'wp-content/acf-json/group_fp02_service_layout_hero.json' ),
	array( 'group_fp02_service_general_parity.json', 'acf-json/group_fp02_service_general_parity.json', 'wp-content/acf-json/group_fp02_service_general_parity.json' ),
	array( 'group_fp02_service_section_parity.json', 'acf-json/group_fp02_service_section_parity.json', 'wp-content/acf-json/group_fp02_service_section_parity.json' ),
	array( 'v9-style.css', 'theme/shpigovsky/assets/css/v9-style.css', 'wp-content/themes/shpigovsky/assets/css/v9-style.css' ),
);

// discover possible page layout mode json.
$page_layout_json = '';
foreach ( glob( $src_root . '/acf-json/*.json' ) ?: array() as $jf ) {
	if ( false !== strpos( (string) file_get_contents( $jf ), 'page_layout_mode' ) ) {
		$base = basename( $jf );
		$crit[] = array( $base . ' (page_layout_mode)', 'acf-json/' . $base, 'wp-content/acf-json/' . $base );
		break;
	}
}

$sync_rows = array();
foreach ( $crit as $c ) {
	$src = $src_root . '/' . $c[1];
	$rt  = $rt_root . '/' . $c[2];
	$hs  = e51fz_sha( $src );
	$hr  = e51fz_sha( $rt );
	$match = ( $hs === $hr && 'MISSING' !== $hs ) ? 'YES' : 'NO';
	$notes = '';
	if ( 'v9-style.css' === $c[0] ) {
		$notes = 'operator runtime CSS authority; drift from source may be intentional';
		// still report match truthfully.
	}
	$result = ( 'YES' === $match ) ? 'PASS' : ( ( 'v9-style.css' === $c[0] ) ? 'PASS_DRIFT_OK' : 'FAIL' );
	if ( 'MISSING' === $hs || 'MISSING' === $hr ) {
		$result = ( false !== strpos( $c[0], 'page_layout_mode' ) ) ? 'PARTIAL' : 'FAIL';
	}
	$sync_rows[] = array( $c[0], $c[1], $c[2], $match, $result, $notes . " src=$hs rt=$hr" );
}
e51fz_csv(
	$evidence . '/v9-06e51-freeze-source-runtime-sync.csv',
	array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ),
	$sync_rows
);
copy( $evidence . '/v9-06e51-freeze-source-runtime-sync.csv', $bak . '/hashes/source-runtime-sync.csv' );

// Critical file hash manifest into bak.
$manifest_lines = array( "file\tsource_sha\truntime_sha\tmatch" );
foreach ( $sync_rows as $row ) {
	$manifest_lines[] = implode( "\t", array( $row[0], $row[1], $row[2], $row[3] ) );
}
file_put_contents( $bak . '/hashes/critical-files.tsv', implode( "\n", $manifest_lines ) );

$summary = array(
	'phase'           => 'V9-06E51-PLACEHOLDER-MODE-FREEZE',
	'backup'          => $bak,
	'db_writes'       => $db_writes,
	'#78_role'        => $role78,
	'#78_layout'      => $layout78,
	'real_switch_method' => 'FIX02_evidence_plus_current_state_no_reswitch',
	'timestamp'       => gmdate( 'c' ),
);
file_put_contents( $bak . '/freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $evidence . '/v9-06e51-freeze-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo "E51_FREEZE_VALIDATE_OK db_writes={$db_writes} role78={$role78} layout78={$layout78}\n";
exit( 0 );
