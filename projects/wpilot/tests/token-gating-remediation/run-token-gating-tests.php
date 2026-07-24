<?php
/**
 * Bounded static/unit tests for WPilot production token-gating remediation (RC6).
 *
 * Run:
 *   php projects/wpilot/tests/token-gating-remediation/run-token-gating-tests.php
 *
 * No WordPress Localhost boot. No network. No production access.
 *
 * @package MetaCode_WPilot_Tests
 */

declare(strict_types=1);

$root = dirname( __DIR__, 2 );
$plugin = $root . '/plugin/metacode-wpilot';
$php = getenv( 'WPILOT_TEST_PHP' ) ?: 'php';

require_once __DIR__ . '/bootstrap-stubs.php';

require_once $plugin . '/includes/class-wpilot-constants.php';
require_once $plugin . '/includes/class-wpilot-errors.php';
require_once $plugin . '/includes/class-wpilot-response.php';
require_once $plugin . '/includes/class-wpilot-connection-tracker.php';
require_once $plugin . '/includes/class-wpilot-settings.php';
require_once $plugin . '/includes/class-wpilot-environment.php';

$failures = array();
$passes = 0;

/**
 * @param string $name Case name.
 * @param bool   $ok   Assertion result.
 * @param string $detail Failure detail.
 * @return void
 */
function wpilot_assert( string $name, bool $ok, string $detail = '' ): void {
	global $failures, $passes;
	if ( $ok ) {
		++$passes;
		echo "PASS  {$name}\n";
		return;
	}
	$failures[] = $name . ( $detail !== '' ? " — {$detail}" : '' );
	echo "FAIL  {$name}" . ( $detail !== '' ? " — {$detail}" : '' ) . "\n";
}

/**
 * Safe defaults used by activation / pre-token production state.
 *
 * @return array
 */
function wpilot_safe_defaults(): array {
	return array(
		'bridge_enabled'     => false,
		'write_enabled'      => false,
		'emergency_disabled' => false,
		'dev_confirmed'      => false,
		'token_hash'         => '',
		'token_created_at'   => '',
		'token_revoked_at'   => '',
		'last_token_used_at' => '',
		'last_connection_status'         => 'never',
		'last_connection_success_at'     => '',
		'last_authorized_connection_at'  => '2026-07-01 12:00:00',
		'last_authorized_endpoint'       => 'site-info',
		'last_connection_failure_at'     => '',
		'last_connection_failure_reason' => '',
		'plugin_version'     => WPilot_Constants::VERSION,
		'schema_version'     => WPilot_Constants::SCHEMA_VERSION,
		'last_safety_error'  => '',
		'allowed_post_types' => array( 'page' ),
		'retention_days'     => 30,
		'backup_retention_max' => 10,
	);
}

// ---------------------------------------------------------------------------
// 1. Admin can generate token with all operational flags false.
// ---------------------------------------------------------------------------
wpilot_test_reset_options( wpilot_safe_defaults() );
$GLOBALS['wpilot_test_current_user_can'] = true;
$opts = WPilot_Settings::get_options();
wpilot_assert(
	'can_manage_token allows admin when bridge/dev/write are false',
	WPilot_Environment::can_manage_token( $opts ) === true
);
wpilot_assert(
	'is_operationally_ready still false without bridge+dev',
	WPilot_Environment::is_operationally_ready( $opts ) === false
);

$token = WPilot_Settings::generate_token();
$after = WPilot_Settings::get_options();
wpilot_assert(
	'token generated while flags false',
	is_string( $token ) && str_starts_with( $token, WPilot_Constants::TOKEN_PREFIX ) && $after['token_hash'] !== ''
);
wpilot_assert(
	'token generation leaves bridge disabled',
	$after['bridge_enabled'] === false
);
wpilot_assert(
	'token generation leaves write_enabled false',
	$after['write_enabled'] === false
);
wpilot_assert(
	'token generation leaves dev_confirmed false',
	$after['dev_confirmed'] === false
);

// ---------------------------------------------------------------------------
// 2. Unauthorized user cannot manage token.
// ---------------------------------------------------------------------------
wpilot_test_reset_options( wpilot_safe_defaults() );
$GLOBALS['wpilot_test_current_user_can'] = false;
wpilot_assert(
	'unauthorized user cannot manage token',
	WPilot_Environment::can_manage_token() === false
);

// ---------------------------------------------------------------------------
// 3. Emergency disable blocks token management.
// ---------------------------------------------------------------------------
$emergency = wpilot_safe_defaults();
$emergency['emergency_disabled'] = true;
wpilot_test_reset_options( $emergency );
$GLOBALS['wpilot_test_current_user_can'] = true;
wpilot_assert(
	'emergency disable blocks can_manage_token',
	WPilot_Environment::can_manage_token() === false
);

// ---------------------------------------------------------------------------
// 4. Invalid nonce gate is enforced in admin POST path (source contract).
// ---------------------------------------------------------------------------
$admin_src = file_get_contents( $plugin . '/admin/class-wpilot-admin-page.php' );
wpilot_assert(
	'admin POST verifies nonce before actions',
	is_string( $admin_src )
		&& str_contains( $admin_src, 'check_admin_referer( self::NONCE_ACTION, self::NONCE_NAME )' )
);
wpilot_assert(
	'generate_token action uses can_manage_token not is_operationally_ready',
	is_string( $admin_src )
		&& str_contains( $admin_src, 'WPilot_Environment::can_manage_token' )
		&& ! preg_match( '/case\s+[\'"]generate_token[\'"].*?is_operationally_ready/s', $admin_src )
);

// ---------------------------------------------------------------------------
// 5. Protected REST readiness still requires bridge + dev_confirmed.
// ---------------------------------------------------------------------------
wpilot_test_reset_options( array_merge( wpilot_safe_defaults(), array( 'token_hash' => 'hash:deadbeef' ) ) );
$readiness = WPilot_Environment::operational_readiness( WPilot_Settings::get_options(), array() );
wpilot_assert(
	'REST operational_readiness blocked while bridge disabled (even with token hash)',
	$readiness instanceof WP_REST_Response || ( is_object( $readiness ) && ! ( true === $readiness ) )
);

// Force bridge on but write off — still need to verify write gate separately.
$ready_opts = array_merge(
	wpilot_safe_defaults(),
	array(
		'bridge_enabled' => true,
		'dev_confirmed'  => true,
		'write_enabled'  => false,
		'token_hash'     => 'hash:deadbeef',
	)
);
wpilot_test_reset_options( $ready_opts );
wpilot_assert(
	'is_operationally_ready true when bridge+dev and not emergency',
	WPilot_Environment::is_operationally_ready() === true
);
wpilot_assert(
	'write_disabled remains true when write_enabled false',
	WPilot_Environment::write_disabled() === true
);

// Auth dry-run path still gates writes — source contract.
$auth_src = file_get_contents( $plugin . '/includes/class-wpilot-auth.php' );
wpilot_assert(
	'write endpoints still gate on write_enabled',
	is_string( $auth_src )
		&& str_contains( $auth_src, "empty( \$options['write_enabled'] )" )
		&& str_contains( $auth_src, 'WRITE_DISABLED' )
);
wpilot_assert(
	'REST auth still calls operational_readiness',
	is_string( $auth_src )
		&& substr_count( $auth_src, 'WPilot_Environment::operational_readiness' ) >= 2
);

// ---------------------------------------------------------------------------
// 6. Token plaintext is not logged by generate_token / settings path.
// ---------------------------------------------------------------------------
wpilot_test_reset_options( wpilot_safe_defaults() );
$token2 = WPilot_Settings::generate_token();
$settings_src = file_get_contents( $plugin . '/includes/class-wpilot-settings.php' );
$env_src = file_get_contents( $plugin . '/includes/class-wpilot-environment.php' );
$logged_plaintext = false;
foreach ( $GLOBALS['wpilot_test_update_log'] as $entry ) {
	$encoded = json_encode( $entry['value'] );
	if ( is_string( $encoded ) && str_contains( $encoded, $token2 ) ) {
		$logged_plaintext = true;
	}
}
wpilot_assert( 'token plaintext not persisted in options update log', $logged_plaintext === false );
wpilot_assert(
	'generate_token source does not error_log token',
	is_string( $settings_src ) && ! preg_match( '/error_log\s*\(.*\$token/', $settings_src )
);

// ---------------------------------------------------------------------------
// 7. Token generation does not call an external endpoint.
// ---------------------------------------------------------------------------
wpilot_assert(
	'token generation recorded no external calls',
	empty( $GLOBALS['wpilot_test_external_calls'] )
);
wpilot_assert(
	'generate_token source has no wp_remote_* / curl',
	is_string( $settings_src )
		&& ! str_contains( $settings_src, 'wp_remote_' )
		&& ! str_contains( $settings_src, 'curl_' )
);

// ---------------------------------------------------------------------------
// 8. Rotation replaces previous hash (new hash, cleared revoked_at).
// ---------------------------------------------------------------------------
wpilot_test_reset_options(
	array_merge(
		wpilot_safe_defaults(),
		array(
			'token_hash'       => 'hash:oldtoken',
			'token_created_at' => '2026-01-01 00:00:00',
			'token_revoked_at' => '2026-01-02 00:00:00',
		)
	)
);
$old_hash = WPilot_Settings::get_options()['token_hash'];
$rotated = WPilot_Settings::generate_token();
$rotated_opts = WPilot_Settings::get_options();
wpilot_assert(
	'token rotation replaces previous hash',
	$rotated_opts['token_hash'] !== $old_hash
		&& $rotated_opts['token_hash'] !== ''
		&& $rotated_opts['token_revoked_at'] === ''
		&& is_string( $rotated )
);

// ---------------------------------------------------------------------------
// 9. Safe defaults unchanged after activation semantics.
// ---------------------------------------------------------------------------
wpilot_test_reset_options( array() );
WPilot_Settings::activate();
$activated = WPilot_Settings::get_options();
wpilot_assert(
	'activation keeps bridge/write/dev false and no token',
	$activated['bridge_enabled'] === false
		&& $activated['write_enabled'] === false
		&& $activated['dev_confirmed'] === false
		&& $activated['token_hash'] === ''
);

// ---------------------------------------------------------------------------
// 10. Stale-options regression: token update must not wipe connection metadata.
// ---------------------------------------------------------------------------
$stale_base = array_merge(
	wpilot_safe_defaults(),
	array(
		'last_authorized_connection_at' => '2026-07-01 12:00:00',
		'last_authorized_endpoint'      => 'site-info',
		'last_connection_status'        => 'success',
		'last_connection_success_at'    => '2026-07-01 12:00:00',
	)
);
wpilot_test_reset_options( $stale_base );
WPilot_Settings::generate_token();
$preserved = WPilot_Settings::get_options();
wpilot_assert(
	'token generation preserves last_authorized_connection_at',
	$preserved['last_authorized_connection_at'] === '2026-07-01 12:00:00'
);
wpilot_assert(
	'token generation preserves last_authorized_endpoint',
	$preserved['last_authorized_endpoint'] === 'site-info'
);
wpilot_assert(
	'generate_token uses partial update_options (no full stale snapshot write)',
	is_string( $settings_src )
		&& preg_match(
			'/function generate_token\(\)[\s\S]*?update_options\(\s*array\s*\(/',
			$settings_src
		)
);

// ---------------------------------------------------------------------------
// 11. Version / release label distinguishable from RC5 package identity.
// ---------------------------------------------------------------------------
wpilot_assert(
	'release label is 0.3.0-RC6',
	WPilot_Constants::RELEASE_LABEL === '0.3.0-RC6'
		&& WPilot_Constants::RELEASE_CANDIDATE === 'RC6'
);
wpilot_assert(
	'plugin VERSION remains 0.3.0 (WP header compatibility)',
	WPilot_Constants::VERSION === '0.3.0'
);

// ---------------------------------------------------------------------------
// Source: can_manage_token must not require bridge/dev/write.
// ---------------------------------------------------------------------------
wpilot_assert(
	'can_manage_token source omits bridge/dev/write requirements',
	is_string( $env_src )
		&& str_contains( $env_src, 'function can_manage_token' )
		&& preg_match(
			'/function can_manage_token[\s\S]*?return true;/m',
			$env_src,
			$m
		)
		&& isset( $m[0] )
		&& ! str_contains( $m[0], 'bridge_enabled' )
		&& ! str_contains( $m[0], 'dev_confirmed' )
		&& ! str_contains( $m[0], 'write_enabled' )
);

echo "\n";
echo 'Passed: ' . $passes . "\n";
echo 'Failed: ' . count( $failures ) . "\n";
if ( $failures ) {
	echo "Failures:\n- " . implode( "\n- ", $failures ) . "\n";
	exit( 1 );
}

echo "ALL TESTS PASSED (static/unit harness; not WordPress runtime proof)\n";
exit( 0 );
