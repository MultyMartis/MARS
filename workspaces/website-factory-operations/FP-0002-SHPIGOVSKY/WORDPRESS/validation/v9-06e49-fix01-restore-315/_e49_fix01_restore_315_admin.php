<?php
/**
 * V9-06E49-FIX01 — restore #315 via real wp-admin form POST (ACF nonce + acf[field…]).
 * Mirrors E51-FIX02 validated save path.
 */
$backup = trim( (string) file_get_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e49-fix01-backup-path.txt'
) );
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence';
$snap_dir = $backup . '/snapshots';
if ( ! is_dir( $snap_dir ) ) {
	mkdir( $snap_dir, 0777, true );
}
if ( ! is_dir( $evidence ) ) {
	mkdir( $evidence, 0777, true );
}

require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$post_id = 315;
$user    = get_user_by( 'login', 'admin' );
if ( ! $user ) {
	$user = get_user_by( 'login', 'mli_admin_fp0002' );
}
if ( ! $user ) {
	$admins = get_users( array( 'role' => 'administrator', 'number' => 1 ) );
	$user   = $admins ? $admins[0] : null;
}
if ( ! $user ) {
	fwrite( STDERR, "NO_ADMIN_USER\n" );
	exit( 2 );
}

$expiration  = time() + DAY_IN_SECONDS;
$cookie_hash = COOKIEHASH;
$cookie_str  = 'wordpress_logged_in_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'logged_in' ) )
	. '; wordpress_' . $cookie_hash . '=' . rawurlencode( wp_generate_auth_cookie( $user->ID, $expiration, 'auth' ) );

function e49fix01_http( $url, $cookie_str, $post_fields = null ) {
	$ch = curl_init( $url );
	$opts = array(
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_FOLLOWLOCATION => false,
		CURLOPT_HEADER         => true,
		CURLOPT_TIMEOUT        => 60,
		CURLOPT_HTTPHEADER     => array(
			'Cookie: ' . $cookie_str,
			'User-Agent: MARS-E49-FIX01/1.0',
		),
	);
	if ( null !== $post_fields ) {
		$opts[ CURLOPT_POST ]       = true;
		$opts[ CURLOPT_POSTFIELDS ] = http_build_query( $post_fields );
		$opts[ CURLOPT_HTTPHEADER ][] = 'Content-Type: application/x-www-form-urlencoded';
		$opts[ CURLOPT_HTTPHEADER ][] = 'Referer: ' . $url;
	}
	curl_setopt_array( $ch, $opts );
	$raw  = curl_exec( $ch );
	$err  = curl_error( $ch );
	$code = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	if ( false === $raw ) {
		return array( 'code' => 0, 'headers' => '', 'body' => '', 'error' => $err );
	}
	$parts = explode( "\r\n\r\n", $raw, 2 );
	if ( count( $parts ) < 2 ) {
		$parts = explode( "\n\n", $raw, 2 );
	}
	return array(
		'code'    => $code,
		'headers' => $parts[0] ?? '',
		'body'    => $parts[1] ?? '',
		'error'   => '',
	);
}

function e49fix01_parse_inputs( $html ) {
	$fields = array();
	if ( preg_match_all( '/<input\b[^>]*>/i', $html, $m ) ) {
		foreach ( $m[0] as $tag ) {
			if ( ! preg_match( '/\bname=(["\'])([^"\']+)\1/i', $tag, $nm ) ) {
				continue;
			}
			$name = html_entity_decode( $nm[2], ENT_QUOTES );
			$type = 'text';
			if ( preg_match( '/\btype=(["\'])([^"\']+)\1/i', $tag, $tm ) ) {
				$type = strtolower( $tm[2] );
			}
			$value = '';
			if ( preg_match( '/\bvalue=(["\'])([^"\']*)\1/i', $tag, $vm ) ) {
				$value = html_entity_decode( $vm[2], ENT_QUOTES );
			}
			$checked = (bool) preg_match( '/\bchecked\b/i', $tag );
			if ( in_array( $type, array( 'checkbox', 'radio' ), true ) ) {
				if ( ! $checked ) {
					continue;
				}
			}
			if ( 'file' === $type ) {
				continue;
			}
			// Prefer last occurrence for duplicates (typical for WP forms).
			$fields[ $name ] = $value;
		}
	}
	if ( preg_match_all( '/<textarea\b[^>]*name=(["\'])([^"\']+)\1[^>]*>(.*?)<\/textarea>/is', $html, $tm, PREG_SET_ORDER ) ) {
		foreach ( $tm as $row ) {
			$fields[ html_entity_decode( $row[2], ENT_QUOTES ) ] = html_entity_decode( $row[3], ENT_QUOTES );
		}
	}
	if ( preg_match_all( '/<select\b[^>]*name=(["\'])([^"\']+)\1[^>]*>(.*?)<\/select>/is', $html, $sm, PREG_SET_ORDER ) ) {
		foreach ( $sm as $row ) {
			$name = html_entity_decode( $row[2], ENT_QUOTES );
			$inner = $row[3];
			$val = '';
			if ( preg_match( '/<option[^>]*selected[^>]*value=(["\'])([^"\']*)\1/i', $inner, $om ) ) {
				$val = html_entity_decode( $om[2], ENT_QUOTES );
			} elseif ( preg_match( '/<option[^>]*value=(["\'])([^"\']*)\1[^>]*selected/i', $inner, $om ) ) {
				$val = html_entity_decode( $om[2], ENT_QUOTES );
			} elseif ( preg_match( '/<option[^>]*value=(["\'])([^"\']*)\1/i', $inner, $om ) ) {
				$val = html_entity_decode( $om[2], ENT_QUOTES );
			}
			$fields[ $name ] = $val;
		}
	}
	return $fields;
}

function e49fix01_role_checked( $html ) {
	$out = array(
		'service'     => false,
		'placeholder' => false,
		'section'     => false,
		'raw_samples' => array(),
	);
	if ( preg_match_all( '/name=(["\'])acf\[field_fp02_service_editor_role\]\1[^>]*>/i', $html, $m ) ) {
		foreach ( $m[0] as $tag ) {
			$val = '';
			if ( preg_match( '/\bvalue=(["\'])([^"\']*)\1/i', $tag, $vm ) ) {
				$val = $vm[2];
			}
			$checked = (bool) preg_match( '/\bchecked\b/i', $tag );
			$out['raw_samples'][] = $val . ( $checked ? ':checked' : '' );
			if ( $checked && isset( $out[ $val ] ) ) {
				$out[ $val ] = true;
			}
		}
	}
	return $out;
}

$edit_url = admin_url( 'post.php?post=' . $post_id . '&action=edit' );
$before   = e49fix01_http( $edit_url, $cookie_str );
file_put_contents( $snap_dir . '/admin-315-edit-before.html', $before['body'] );
file_put_contents( $evidence . '/v9-06e49-fix01-admin-315-edit-before.html', $before['body'] );

$role_before = e49fix01_role_checked( $before['body'] );
$meta_before = array(
	'role'   => (string) get_post_meta( $post_id, 'service_editor_role', true ),
	'layout' => (string) get_post_meta( $post_id, 'service_layout_variant', true ),
	'ovr'    => (string) get_post_meta( $post_id, 'service_layout_override_enabled', true ),
);

echo "ADMIN_GET code={$before['code']} len=" . strlen( $before['body'] ) . "\n";
echo 'META_BEFORE role=' . $meta_before['role'] . ' layout=' . $meta_before['layout'] . "\n";
echo 'ROLE_UI_BEFORE service=' . ( $role_before['service'] ? '1' : '0' ) . ' placeholder=' . ( $role_before['placeholder'] ? '1' : '0' ) . "\n";

if ( $before['code'] < 200 || $before['code'] >= 400 || false !== stripos( $before['body'], 'id="loginform"' ) ) {
	fwrite( STDERR, "ADMIN_AUTH_OR_LOAD_FAILED\n" );
	exit( 3 );
}

$fields = e49fix01_parse_inputs( $before['body'] );
if ( empty( $fields['_wpnonce'] ) && empty( $fields['_acf_nonce'] ) ) {
	fwrite( STDERR, "NO_NONCE_IN_FORM\n" );
	exit( 4 );
}

// Force role to service (ACF field key path).
$fields['acf[field_fp02_service_editor_role]'] = 'service';
// Also set technical layout explicitly for robustness.
$fields['acf[field_fp02_service_layout_variant]'] = 'service_general';
if ( isset( $fields['acf[field_fp02_service_layout_override_enabled]'] ) ) {
	$fields['acf[field_fp02_service_layout_override_enabled]'] = '0';
}

// Ensure core WP update fields.
$fields['post_ID']   = (string) $post_id;
$fields['post_type'] = 'service';
$fields['action']    = 'editpost';
$fields['save']      = 'Update';
if ( empty( $fields['originalaction'] ) ) {
	$fields['originalaction'] = 'editpost';
}

$post_url = admin_url( 'post.php' );
$save     = e49fix01_http( $post_url, $cookie_str, $fields );
file_put_contents( $snap_dir . '/admin-315-save-headers.txt', $save['headers'] );
file_put_contents( $evidence . '/v9-06e49-fix01-admin-315-save-headers.txt', $save['headers'] );

$loc = '';
if ( preg_match( '/^Location:\s*(.+)$/mi', $save['headers'], $lm ) ) {
	$loc = trim( $lm[1] );
}
echo "ADMIN_POST code={$save['code']} location=$loc\n";

// Reload WP object cache / meta.
clean_post_cache( $post_id );
wp_cache_flush();

$meta_mid = array(
	'role'   => (string) get_post_meta( $post_id, 'service_editor_role', true ),
	'layout' => (string) get_post_meta( $post_id, 'service_layout_variant', true ),
	'ovr'    => (string) get_post_meta( $post_id, 'service_layout_override_enabled', true ),
);
echo 'META_AFTER_POST role=' . $meta_mid['role'] . ' layout=' . $meta_mid['layout'] . "\n";

// If form POST did not persist (edge case), fall back to update_field (still admin-compatible ACF path).
$db_writes = 0;
$path_used = 'wp-admin-form-post';
if ( 'service' !== $meta_mid['role'] || 'service_general' !== $meta_mid['layout'] ) {
	$path_used = 'update_field-fallback';
	if ( function_exists( 'update_field' ) ) {
		update_field( 'field_fp02_service_editor_role', 'service', $post_id );
		++$db_writes;
		// sync_layout_when_role_updated should set layout; enforce explicitly if needed.
		$layout_now = (string) get_post_meta( $post_id, 'service_layout_variant', true );
		if ( 'service_general' !== $layout_now ) {
			update_field( 'field_fp02_service_layout_variant', 'service_general', $post_id );
			++$db_writes;
		}
		update_field( 'field_fp02_service_layout_override_enabled', 0, $post_id );
		++$db_writes;
	} else {
		update_post_meta( $post_id, 'service_editor_role', 'service' );
		update_post_meta( $post_id, 'service_layout_variant', 'service_general' );
		update_post_meta( $post_id, 'service_layout_override_enabled', 0 );
		$db_writes += 3;
		$path_used = 'update_post_meta-fallback';
	}
	clean_post_cache( $post_id );
	wp_cache_flush();
} else {
	// Count layout/meta keys that likely changed from placeholder→service.
	$db_writes = 2;
}

$after = e49fix01_http( $edit_url, $cookie_str );
file_put_contents( $snap_dir . '/admin-315-edit-after.html', $after['body'] );
file_put_contents( $evidence . '/v9-06e49-fix01-admin-315-edit-after.html', $after['body'] );
$role_after = e49fix01_role_checked( $after['body'] );

$meta_after = array(
	'role'   => (string) get_post_meta( $post_id, 'service_editor_role', true ),
	'layout' => (string) get_post_meta( $post_id, 'service_layout_variant', true ),
	'ovr'    => (string) get_post_meta( $post_id, 'service_layout_override_enabled', true ),
);

// Placeholder option still available?
$placeholder_choice_present = ( false !== stripos( $after['body'], 'value="placeholder"' ) && false !== stripos( $after['body'], 'field_fp02_service_editor_role' ) );

$trace = array(
	array( 'step', 'value' ),
	array( 'user', $user->user_login ),
	array( 'path_used', $path_used ),
	array( 'admin_get_code', (string) $before['code'] ),
	array( 'admin_post_code', (string) $save['code'] ),
	array( 'admin_post_location', $loc ),
	array( 'meta_before_role', $meta_before['role'] ),
	array( 'meta_before_layout', $meta_before['layout'] ),
	array( 'meta_after_role', $meta_after['role'] ),
	array( 'meta_after_layout', $meta_after['layout'] ),
	array( 'ui_before_placeholder_checked', $role_before['placeholder'] ? 'yes' : 'no' ),
	array( 'ui_after_service_checked', $role_after['service'] ? 'yes' : 'no' ),
	array( 'ui_after_placeholder_checked', $role_after['placeholder'] ? 'yes' : 'no' ),
	array( 'placeholder_option_still_available', $placeholder_choice_present ? 'yes' : 'no' ),
	array( 'db_writes_estimated', (string) $db_writes ),
);
$csv = '';
foreach ( $trace as $row ) {
	$csv .= implode( ',', $row ) . "\n";
}
file_put_contents( $evidence . '/v9-06e49-fix01-restore-trace.csv', $csv );
file_put_contents( $backup . '/exports/restore-trace.csv', $csv );

echo "META_FINAL role={$meta_after['role']} layout={$meta_after['layout']}\n";
echo 'ROLE_UI_AFTER service=' . ( $role_after['service'] ? '1' : '0' ) . ' placeholder=' . ( $role_after['placeholder'] ? '1' : '0' ) . "\n";
echo 'PLACEHOLDER_OPTION_AVAILABLE=' . ( $placeholder_choice_present ? 'yes' : 'no' ) . "\n";
echo "PATH_USED=$path_used DB_WRITES=$db_writes\n";
echo ( 'service' === $meta_after['role'] && 'service_general' === $meta_after['layout'] && $role_after['service'] ) ? "RESTORE_OK\n" : "RESTORE_PARTIAL_OR_FAIL\n";
