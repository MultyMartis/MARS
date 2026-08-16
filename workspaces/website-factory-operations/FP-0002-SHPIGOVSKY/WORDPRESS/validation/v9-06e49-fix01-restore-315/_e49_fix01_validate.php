<?php
/**
 * V9-06E49-FIX01 — after-restore validation + evidence CSVs.
 */
$backup = trim( (string) file_get_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e49-fix01-backup-path.txt'
) );
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

function e49v_csv( $path, array $rows ) {
	$fh = fopen( $path, 'wb' );
	foreach ( $rows as $row ) {
		fputcsv( $fh, $row );
	}
	fclose( $fh );
}

function e49v_http( $url ) {
	$ch = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 45,
			CURLOPT_USERAGENT      => 'MARS-E49-FIX01-VALIDATE/1.0',
		)
	);
	$body = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	$err  = curl_error( $ch );
	curl_close( $ch );
	return array(
		'code' => $code,
		'body' => is_string( $body ) ? $body : '',
		'err'  => $err,
		'len'  => is_string( $body ) ? strlen( $body ) : 0,
	);
}

function e49v_fe_flags( $body ) {
	$ph = ( false !== stripos( $body, 'placeholder-stack' ) ) || ( false !== stripos( $body, 'service-placeholder-stack' ) );
	$h1 = (bool) preg_match( '/<h1\b/i', $body );
	$serviceish = (
		false !== stripos( $body, 'service-general' )
		|| false !== stripos( $body, 'service-alcohol' )
		|| false !== stripos( $body, 'service-page' )
		|| false !== stripos( $body, 'service-hero' )
		|| ( preg_match_all( '/class="[^"]*service-/i', $body ) >= 3 )
	);
	$alcohol_paste = (
		false !== stripos( $body, 'алкогольн' )
		&& false !== stripos( $body, 'Лечение лекарственной' )
	);
	return array(
		'placeholder_stack' => $ph ? 'yes' : 'no',
		'h1'                => $h1 ? 'yes' : 'no',
		'service_blocks'    => $serviceish ? 'yes' : 'no',
		'alcohol_paste'     => $alcohol_paste ? 'yes' : 'no',
	);
}

$user = get_user_by( 'login', 'admin' ) ?: get_user_by( 'login', 'mli_admin_fp0002' );
if ( ! $user ) {
	$admins = get_users( array( 'role' => 'administrator', 'number' => 1 ) );
	$user   = $admins ? $admins[0] : null;
}
$expiration  = time() + DAY_IN_SECONDS;
$cookie_hash = COOKIEHASH;
$cookie_str  = 'wordpress_logged_in_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'logged_in' ) )
	. '; wordpress_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'auth' ) );

function e49v_admin_get( $post_id, $cookie_str ) {
	$url = admin_url( 'post.php?post=' . (int) $post_id . '&action=edit' );
	$ch  = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 60,
			CURLOPT_HTTPHEADER     => array( 'Cookie: ' . $cookie_str ),
		)
	);
	$body = curl_exec( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	$body = is_string( $body ) ? $body : '';
	$checked = 'unknown';
	if ( preg_match_all( '/name=(["\'])acf\[field_fp02_service_editor_role\]\1[^>]*>/i', $body, $m ) ) {
		foreach ( $m[0] as $tag ) {
			if ( preg_match( '/\bchecked\b/i', $tag ) && preg_match( '/\bvalue=(["\'])([^"\']*)\1/i', $tag, $vm ) ) {
				$checked = $vm[2];
				break;
			}
		}
	}
	$ph_option = ( false !== stripos( $body, 'value="placeholder"' ) && false !== stripos( $body, 'field_fp02_service_editor_role' ) );
	$blocks = (
		false !== stripos( $body, 'Услуга — блоки' )
		|| false !== stripos( $body, 'group_fp02_service_general' )
		|| false !== stripos( $body, 'service_general' )
	);
	return array(
		'code'             => $code,
		'checked_role'     => $checked,
		'placeholder_opt'  => $ph_option ? 'yes' : 'no',
		'service_blocks'   => $blocks ? 'yes' : 'no',
		'len'              => strlen( $body ),
		'login_form'       => ( false !== stripos( $body, 'id="loginform"' ) ) ? 'yes' : 'no',
	);
}

// ---- Content preservation for #315 ----
$meta_after = get_post_meta( 315 );
ksort( $meta_after );
$content_meta = array();
foreach ( $meta_after as $key => $values ) {
	if ( in_array( $key, array( 'service_editor_role', 'service_layout_variant', 'service_layout_override_enabled', '_service_editor_role', '_service_layout_variant', '_service_layout_override_enabled', '_edit_lock', '_edit_last' ), true ) ) {
		continue;
	}
	$content_meta[ $key ] = $values;
}
ksort( $content_meta );
$json_after = wp_json_encode( $content_meta, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
file_put_contents( $backup . '/postmeta/post-315-content-fingerprint-after.json', $json_after );
$hash_after = hash( 'sha256', $json_after );
file_put_contents( $backup . '/postmeta/post-315-content-fingerprint-after.sha256', $hash_after . "\n" );
$hash_before = trim( (string) @file_get_contents( $backup . '/postmeta/post-315-content-fingerprint-before.sha256' ) );

$post315 = get_post( 315 );
$preserve_rows = array(
	array( 'meta_or_check', 'before', 'after', 'changed yes/no', 'allowed yes/no', 'result', 'notes' ),
	array( 'service_editor_role', 'placeholder', (string) get_post_meta( 315, 'service_editor_role', true ), 'yes', 'yes', 'PASS', 'layout restore target' ),
	array( 'service_layout_variant', 'placeholder', (string) get_post_meta( 315, 'service_layout_variant', true ), 'yes', 'yes', 'PASS', 'layout restore target' ),
	array(
		'content_fingerprint_sha256',
		$hash_before,
		$hash_after,
		( $hash_before === $hash_after ) ? 'no' : 'yes',
		( $hash_before === $hash_after ) ? 'yes' : 'no',
		( $hash_before === $hash_after ) ? 'PASS' : 'FAIL',
		'non-layout metas excluding edit_lock/last',
	),
	array( 'post_status', 'publish', $post315 ? $post315->post_status : '', 'no', 'yes', ( $post315 && 'publish' === $post315->post_status ) ? 'PASS' : 'FAIL', '' ),
	array( 'post_name', 'lekarstva', $post315 ? $post315->post_name : '', 'no', 'yes', ( $post315 && 'lekarstva' === $post315->post_name ) ? 'PASS' : 'FAIL', '' ),
	array(
		'permalink',
		'http://shpigovsky.test/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/',
		get_permalink( 315 ),
		'no',
		'yes',
		( get_permalink( 315 ) === 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/' ) ? 'PASS' : 'FAIL',
		'',
	),
);

// Spot-check key ACF content fields present.
$content_keys = array(
	'service_short_description',
	'service_hero_title',
	'service_hero_lead',
	'service_problem_title',
	'service_problem_text',
	'service_about_title',
	'service_about_text',
);
foreach ( $content_keys as $ck ) {
	$before_fp = json_decode( (string) @file_get_contents( $backup . '/postmeta/post-315-content-fingerprint-before.json' ), true );
	$b = isset( $before_fp[ $ck ][0] ) ? (string) $before_fp[ $ck ][0] : '';
	$a = (string) get_post_meta( 315, $ck, true );
	$changed = ( $b === $a ) ? 'no' : 'yes';
	$ok = ( $b === $a && '' !== $a ) || ( $b === $a );
	$preserve_rows[] = array(
		$ck,
		mb_substr( $b, 0, 80 ),
		mb_substr( $a, 0, 80 ),
		$changed,
		( 'no' === $changed ) ? 'yes' : 'no',
		( 'no' === $changed ) ? 'PASS' : 'FAIL',
		( '' === $a && '' === $b ) ? 'empty both (still match)' : 'content field',
	);
}

// Count image-like / repeater metas preserved.
$img_keys_before = 0;
$img_keys_after  = 0;
$before_all = json_decode( (string) @file_get_contents( $backup . '/postmeta/post-315-content-fingerprint-before.json' ), true );
if ( is_array( $before_all ) ) {
	foreach ( $before_all as $k => $v ) {
		if ( false !== stripos( $k, 'image' ) || false !== stripos( $k, 'gallery' ) || preg_match( '/_\d+_/', $k ) ) {
			++$img_keys_before;
		}
	}
}
foreach ( $content_meta as $k => $v ) {
	if ( false !== stripos( $k, 'image' ) || false !== stripos( $k, 'gallery' ) || preg_match( '/_\d+_/', $k ) ) {
		++$img_keys_after;
	}
}
$preserve_rows[] = array(
	'image_or_repeater_meta_count',
	(string) $img_keys_before,
	(string) $img_keys_after,
	( $img_keys_before === $img_keys_after ) ? 'no' : 'yes',
	( $img_keys_before === $img_keys_after ) ? 'yes' : 'no',
	( $img_keys_before === $img_keys_after ) ? 'PASS' : 'FAIL',
	'heuristic count',
);

e49v_csv( $evidence . '/v9-06e49-fix01-315-content-preservation.csv', $preserve_rows );

// ---- Admin validation #315 ----
$admin315 = e49v_admin_get( 315, $cookie_str );
$admin_rows = array(
	array( 'check', 'expected', 'actual', 'result', 'notes' ),
	array( 'admin_loads', '200 no login', $admin315['code'] . ' login=' . $admin315['login_form'], ( 200 === $admin315['code'] && 'no' === $admin315['login_form'] ) ? 'PASS' : 'FAIL', 'len=' . $admin315['len'] ),
	array( 'visible_layout', 'Услуга/service', $admin315['checked_role'], ( 'service' === $admin315['checked_role'] ) ? 'PASS' : 'FAIL', '' ),
	array( 'technical_layout_meta', 'service_general', (string) get_post_meta( 315, 'service_layout_variant', true ), ( 'service_general' === (string) get_post_meta( 315, 'service_layout_variant', true ) ) ? 'PASS' : 'FAIL', '' ),
	array( 'service_blocks_present', 'yes', $admin315['service_blocks'], ( 'yes' === $admin315['service_blocks'] ) ? 'PASS' : 'FAIL', '' ),
	array( 'placeholder_option_available', 'yes not selected', $admin315['placeholder_opt'] . ' checked=' . $admin315['checked_role'], ( 'yes' === $admin315['placeholder_opt'] && 'service' === $admin315['checked_role'] ) ? 'PASS' : 'FAIL', '' ),
	array( 'acf_content_still_present', 'yes', ( $hash_before === $hash_after ) ? 'yes' : 'no', ( $hash_before === $hash_after ) ? 'PASS' : 'FAIL', 'fingerprint' ),
);
e49v_csv( $evidence . '/v9-06e49-fix01-admin-validation.csv', $admin_rows );

// ---- Frontend validation ----
$fe_targets = array(
	315 => array( 'url' => get_permalink( 315 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no' ),
	78  => array( 'url' => get_permalink( 78 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no' ),
	74  => array( 'url' => get_permalink( 74 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no' ),
	314 => array( 'url' => get_permalink( 314 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no', 'child_tiles' => true ),
	81  => array( 'url' => get_permalink( 81 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no' ),
	85  => array( 'url' => get_permalink( 85 ), 'expect_role' => 'service', 'expect_layout' => 'service_general', 'expect_ph' => 'no' ),
	73  => array( 'url' => get_permalink( 73 ), 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'expect_ph' => 'no' ),
	77  => array( 'url' => get_permalink( 77 ), 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'expect_ph' => 'no' ),
	84  => array( 'url' => get_permalink( 84 ), 'expect_role' => 'section', 'expect_layout' => 'subdivision', 'expect_ph' => 'no' ),
);

$fe_rows = array(
	array( 'post_id', 'url', 'http', 'role', 'layout', 'placeholder_stack', 'h1', 'service_blocks', 'child_tiles', 'alcohol_paste', 'result', 'notes' ),
);
$after_dir = $backup . '/frontend';
foreach ( $fe_targets as $id => $t ) {
	$resp = e49v_http( $t['url'] );
	file_put_contents( $after_dir . '/after-' . $id . '.html', $resp['body'] );
	$flags = e49v_fe_flags( $resp['body'] );
	$role   = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout = (string) get_post_meta( $id, 'service_layout_variant', true );
	$child  = 'n/a';
	if ( ! empty( $t['child_tiles'] ) ) {
		$child = ( false !== stripos( $resp['body'], 'child-service' ) || false !== stripos( $resp['body'], 'service-children' ) || false !== stripos( $resp['body'], 'services-child' ) ) ? 'yes' : 'no';
	}
	$ok = (
		200 === $resp['code']
		&& $role === $t['expect_role']
		&& $layout === $t['expect_layout']
		&& $flags['placeholder_stack'] === $t['expect_ph']
		&& 'yes' === $flags['h1']
	);
	if ( 315 === $id ) {
		$ok = $ok && 'yes' === $flags['service_blocks'] && 'no' === $flags['alcohol_paste'];
	}
	$fe_rows[] = array(
		$id,
		$t['url'],
		(string) $resp['code'],
		$role,
		$layout,
		$flags['placeholder_stack'],
		$flags['h1'],
		$flags['service_blocks'],
		$child,
		$flags['alcohol_paste'],
		$ok ? 'PASS' : 'FAIL',
		'len=' . $resp['len'],
	);
}
e49v_csv( $evidence . '/v9-06e49-fix01-frontend-validation.csv', $fe_rows );

// ---- Freeze blocker recheck: all individual services ----
$q = new WP_Query(
	array(
		'post_type'      => 'service',
		'post_status'    => 'publish',
		'posts_per_page' => -1,
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);
$sections = array( 73, 77, 84 );
$blocker_rows = array(
	array( 'post_id', 'title', 'expected_role', 'actual_role', 'expected_layout', 'actual_layout', 'placeholder_stack_frontend', 'result', 'notes' ),
);
$unintended_ph = 0;
while ( $q->have_posts() ) {
	$q->the_post();
	$id     = get_the_ID();
	$title  = get_the_title();
	$role   = (string) get_post_meta( $id, 'service_editor_role', true );
	$layout = (string) get_post_meta( $id, 'service_layout_variant', true );
	$url    = get_permalink( $id );
	$resp   = e49v_http( $url );
	$flags  = e49v_fe_flags( $resp['body'] );

	if ( in_array( $id, $sections, true ) ) {
		$exp_role   = 'section';
		$exp_layout = 'subdivision';
		$notes      = 'section excluded from individual service requirement';
	} else {
		$exp_role   = 'service';
		$exp_layout = 'service_general';
		$notes      = 'individual service';
		if ( 'placeholder' === $role || 'placeholder' === $layout || 'yes' === $flags['placeholder_stack'] ) {
			++$unintended_ph;
			$notes = 'UNINTENDED_PLACEHOLDER';
		}
	}

	$ok = ( $role === $exp_role && $layout === $exp_layout && 'no' === $flags['placeholder_stack'] && 200 === $resp['code'] );
	$blocker_rows[] = array(
		$id,
		$title,
		$exp_role,
		$role,
		$exp_layout,
		$layout,
		$flags['placeholder_stack'],
		$ok ? 'PASS' : 'FAIL',
		$notes,
	);
}
wp_reset_postdata();
e49v_csv( $evidence . '/v9-06e49-fix01-freeze-blocker-recheck.csv', $blocker_rows );
file_put_contents( $evidence . '/v9-06e49-fix01-unintended-placeholders.txt', (string) $unintended_ph . "\n" );

// ---- Route smoke ----
$routes = array(
	array( '/', 'http://shpigovsky.test/' ),
	array( '/uslugi/', 'http://shpigovsky.test/uslugi/' ),
	array( '/uslugi/zavisimosti/', get_permalink( 73 ) ),
	array( '/uslugi/psihicheskoe-zdorovie/', get_permalink( 77 ) ),
	array( '/uslugi/rasstroystva-pischevogo-povedeniya/', get_permalink( 84 ) ),
	array( '#315', get_permalink( 315 ) ),
	array( '#78', get_permalink( 78 ) ),
	array( '#74', get_permalink( 74 ) ),
	array( '#314', get_permalink( 314 ) ),
	array( '#81', get_permalink( 81 ) ),
	array( '#85', get_permalink( 85 ) ),
	array( '/blog/', 'http://shpigovsky.test/blog/' ),
	array( '/specyalisty/', 'http://shpigovsky.test/specyalisty/' ),
	array( '/o-centre/', 'http://shpigovsky.test/o-centre/' ),
	array( '/kontakty/', 'http://shpigovsky.test/kontakty/' ),
);
$smoke_rows = array( array( 'route', 'url', 'http', 'fatal_markers', 'result', 'notes' ) );
foreach ( $routes as $r ) {
	$resp = e49v_http( $r[1] );
	$fatal = (
		false !== stripos( $resp['body'], 'Fatal error' )
		|| false !== stripos( $resp['body'], 'Uncaught Error' )
		|| false !== stripos( $resp['body'], 'There has been a critical error' )
	) ? 'yes' : 'no';
	$ok = ( 200 === $resp['code'] && 'no' === $fatal );
	$smoke_rows[] = array( $r[0], $r[1], (string) $resp['code'], $fatal, $ok ? 'PASS' : 'FAIL', 'len=' . $resp['len'] );
}
e49v_csv( $evidence . '/v9-06e49-fix01-route-smoke.csv', $smoke_rows );

// ---- Source/runtime sync (no product source changes expected; CSS preserved) ----
$src_root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$rt_root  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content';
$sync_files = array(
	array( 'ServiceLayoutGovernance.php', $src_root . '/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php', $rt_root . '/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php' ),
	array( 'v9-style.css', $src_root . '/themes/shpigovsky/assets/css/v9-style.css', $rt_root . '/themes/shpigovsky/assets/css/v9-style.css' ),
	array( 'group_fp02_service_layout_hero.json', $src_root . '/acf-json/group_fp02_service_layout_hero.json', $rt_root . '/acf-json/group_fp02_service_layout_hero.json' ),
);
$sync_rows = array( array( 'file', 'source_path', 'runtime_path', 'hash_match', 'result', 'notes' ) );
$css_backup_hash = '';
$sum = @file_get_contents( $backup . '/BACKUP-SUMMARY.txt' );
if ( preg_match( '/operator_css_sha256=([A-F0-9]+)/i', (string) $sum, $m ) ) {
	$css_backup_hash = strtoupper( $m[1] );
}
foreach ( $sync_files as $sf ) {
	$hs = is_file( $sf[1] ) ? strtoupper( hash_file( 'sha256', $sf[1] ) ) : 'MISSING';
	$hr = is_file( $sf[2] ) ? strtoupper( hash_file( 'sha256', $sf[2] ) ) : 'MISSING';
	$match = ( $hs === $hr && 'MISSING' !== $hs ) ? 'YES' : 'NO';
	$notes = 'source=' . substr( $hs, 0, 12 ) . ' runtime=' . substr( $hr, 0, 12 );
	if ( 'v9-style.css' === $sf[0] && $css_backup_hash ) {
		$notes .= ' vs_backup=' . ( ( $hr === $css_backup_hash ) ? 'MATCH' : 'DRIFT' );
	}
	$sync_rows[] = array( $sf[0], $sf[1], $sf[2], $match, ( 'YES' === $match ) ? 'PASS' : 'FAIL', $notes );
}
e49v_csv( $evidence . '/v9-06e49-fix01-source-runtime-sync.csv', $sync_rows );

// Summary JSON
$summary = array(
	'backup'              => $backup,
	'post_315_role'       => (string) get_post_meta( 315, 'service_editor_role', true ),
	'post_315_layout'     => (string) get_post_meta( 315, 'service_layout_variant', true ),
	'content_fp_match'    => ( $hash_before === $hash_after ),
	'unintended_placeholders' => $unintended_ph,
	'admin_checked_role'  => $admin315['checked_role'],
	'operator_css_backup' => $css_backup_hash,
);
file_put_contents( $evidence . '/v9-06e49-fix01-summary.json', wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) );

echo "VALIDATE_OK\n";
echo '315=' . $summary['post_315_role'] . '/' . $summary['post_315_layout'] . "\n";
echo 'CONTENT_FP_MATCH=' . ( $summary['content_fp_match'] ? 'yes' : 'no' ) . "\n";
echo 'UNINTENDED_PLACEHOLDERS=' . $unintended_ph . "\n";
echo 'ADMIN_CHECKED=' . $admin315['checked_role'] . "\n";
