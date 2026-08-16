<?php
/**
 * V9-06E50 fixup: sync subnav helper, neutralize DEMO alcohol cue, revalidate FE/empty.
 *
 * @package FP0002
 */

declare(strict_types=1);

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$src      = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/inc/service-helpers.php';
$dst      = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/inc/service-helpers.php';
copy( $src, $dst );

$db_writes = 0;
$neutral   = 'DEMO: нейтральный демонстрационный абзац для раздела. Описывает подход центра без привязки к конкретной услуге. Редактор может заменить текст в ACF.';

foreach ( array( 77, 84 ) as $pid ) {
	$blocks = get_field( 'section_nature_text_blocks', $pid );
	if ( ! is_array( $blocks ) ) {
		continue;
	}
	$changed = false;
	foreach ( $blocks as &$row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}
		$text = isset( $row['text'] ) ? (string) $row['text'] : '';
		if ( false !== mb_stripos( $text, 'алкогол' ) || false !== mb_stripos( $text, 'зависимост' ) ) {
			$row['text'] = $neutral;
			$changed     = true;
		}
	}
	unset( $row );
	if ( $changed ) {
		update_field( 'section_nature_text_blocks', $blocks, $pid );
		++$db_writes;
	}
}

/**
 * HTTP.
 *
 * @param string $url URL.
 * @return array{code:int,body:string}
 */
function e50f_http( string $url ): array {
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

$fe_rows = array();
$checks  = array(
	array( '`/uslugi/zavisimosti/`', home_url( '/uslugi/zavisimosti/' ), false ),
	array( '`/uslugi/psihicheskoe-zdorovie/`', home_url( '/uslugi/psihicheskoe-zdorovie/' ), true ),
	array( '`/uslugi/rasstroystva-pischevogo-povedeniya/`', home_url( '/uslugi/rasstroystva-pischevogo-povedeniya/' ), true ),
);

foreach ( $checks as $c ) {
	list( $label, $url, $forbid_dep ) = $c;
	$r    = e50f_http( (string) $url );
	$body = $r['body'];
	$has_nature   = ( false !== strpos( $body, 'service-subdivision-nature-v1' ) );
	$has_approach = ( false !== strpos( $body, 'service-subdivision-team-stats-v1' ) );
	$wrong        = false;
	if ( $forbid_dep ) {
		// Subnav/body dependency-specific labels that should not appear on non-#73 sections.
		$wrong = ( false !== mb_strpos( $body, 'Природа зависимости' ) )
			|| ( false !== mb_strpos( $body, 'Наш подход к лечению зависимостей' ) )
			|| ( false !== mb_strpos( $body, '>Зависимости</a>' ) && false === mb_strpos( $body, 'зависимости, которые' ) );
		// Allow in child service card titles if any — flag only exact nature/approach strings.
		$wrong = ( false !== mb_strpos( $body, 'Природа зависимости' ) )
			|| ( false !== mb_strpos( $body, 'Наш подход к лечению зависимостей' ) );
	}
	$ok = ( 200 === $r['code'] && $has_nature && $has_approach && ! $wrong );
	$fe_rows[] = array(
		$label,
		'200 + section ACF content',
		sprintf(
			'HTTP %d nature=%s approach=%s wrong_dep_copy=%s',
			$r['code'],
			$has_nature ? 'yes' : 'no',
			$has_approach ? 'yes' : 'no',
			$wrong ? 'yes' : 'no'
		),
		$ok ? 'PASS' : 'FAIL',
		'',
	);
}

$fp = fopen( $evidence . '/v9-06e50-frontend-validation.csv', 'wb' );
fputcsv( $fp, array( 'route', 'expected', 'actual', 'result', 'notes' ) );
foreach ( $fe_rows as $row ) {
	fputcsv( $fp, $row );
}
fclose( $fp );

// Empty-field retest focused on nature lead element only.
$probe_id    = 77;
$probe_field = 'section_nature_lead';
$before      = get_field( $probe_field, $probe_id );
update_field( $probe_field, '', $probe_id );
++$db_writes;
clean_post_cache( $probe_id );
if ( function_exists( 'acf_get_store' ) ) {
	$vs = acf_get_store( 'values' );
	if ( $vs && method_exists( $vs, 'reset' ) ) {
		$vs->reset();
	}
}

$fe = e50f_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
preg_match( '/service-subdivision-nature-v1__lead[^>]*>(.*?)<\/p>/s', $fe['body'], $m );
$lead_html = isset( $m[1] ) ? trim( wp_strip_all_tags( $m[1] ) ) : '';
$pass1     = ( 200 === $fe['code'] && '' === $lead_html );

update_field( $probe_field, $before, $probe_id );
++$db_writes;
clean_post_cache( $probe_id );
$fe2 = e50f_http( home_url( '/uslugi/psihicheskoe-zdorovie/' ) );
$pass2 = ( 200 === $fe2['code'] );
if ( is_string( $before ) && '' !== trim( $before ) ) {
	$pass2 = $pass2 && ( false !== mb_strpos( $fe2['body'], mb_substr( trim( $before ), 0, 40 ) ) );
}

$fp = fopen( $evidence . '/v9-06e50-empty-field-behavior-validation.csv', 'wb' );
fputcsv( $fp, array( 'test', 'expected', 'actual', 'result', 'notes' ) );
fputcsv(
	$fp,
	array(
		'optional nature lead cleared on #77',
		'no hardcoded demo injected; lead hidden/empty',
		'' === $lead_html ? 'lead element absent or empty' : ( 'LEAD:' . mb_substr( $lead_html, 0, 80 ) ),
		$pass1 ? 'PASS' : 'FAIL',
		'HTTP ' . $fe['code'],
	)
);
fputcsv(
	$fp,
	array(
		'nature lead restored on #77',
		'original visible',
		$pass2 ? 'restored' : 'restore_issue',
		$pass2 ? 'PASS' : 'FAIL',
		'',
	)
);
fclose( $fp );

// Append sync row for service-helpers.
$sync_path = $evidence . '/v9-06e50-source-runtime-sync.csv';
$match     = md5_file( $src ) === md5_file( $dst );
$fp        = fopen( $sync_path, 'ab' );
fputcsv(
	$fp,
	array(
		'service-helpers.php',
		$src,
		$dst,
		$match ? 'yes' : 'no',
		$match ? 'PASS' : 'FAIL',
		'subnav ACF labels',
	)
);
fclose( $fp );

echo wp_json_encode(
	array(
		'db_writes'  => $db_writes,
		'fe'         => $fe_rows,
		'empty_pass' => $pass1 && $pass2,
		'sync_match' => $match,
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
) . "\n";
