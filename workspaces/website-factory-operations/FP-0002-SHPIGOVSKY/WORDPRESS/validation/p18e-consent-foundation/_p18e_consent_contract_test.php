<?php
declare(strict_types=1);

define('ABSPATH', __DIR__ . '/');
define('DAY_IN_SECONDS', 86400);
define('OBJECT', 'OBJECT');

if (!function_exists('__')) {
	function __($text, $domain = null) { return $text; }
}
if (!function_exists('wp_parse_args')) {
	function wp_parse_args($args, $defaults = array()) {
		return array_merge((array) $defaults, (array) $args);
	}
}
if (!function_exists('get_option')) {
	function get_option($name, $default = false) {
		if ('fp02_cookie_privacy_settings' === $name) {
			return array(
				'consent_version' => 2,
				'consent_lifetime_days' => 365,
			);
		}
		return $default;
	}
}
if (!function_exists('get_page_by_path')) {
	function get_page_by_path($path, $output = OBJECT, $post_type = 'page') { return null; }
}
if (!function_exists('is_ssl')) {
	function is_ssl() { return true; }
}
if (!function_exists('sanitize_key')) {
	function sanitize_key($key) {
		$key = strtolower((string) $key);
		return preg_replace('/[^a-z0-9_\-]/', '', $key);
	}
}

require_once dirname(__DIR__, 2) . '/plugins/shpigovsky-core/src/Contracts/ModuleInterface.php';
require_once dirname(__DIR__, 2) . '/plugins/shpigovsky-core/src/Privacy/PrivacyConsent.php';

use Shpigovsky\Core\Privacy\PrivacyConsent;

$results = array();

$assert = static function (string $name, bool $condition, array $context = array()) use (&$results): void {
	$results[] = array(
		'test' => $name,
		'status' => $condition ? 'PASS' : 'FAIL',
		'context' => $context,
	);
};

$necessaryOnly = PrivacyConsent::build_record_for_state(PrivacyConsent::STATE_NECESSARY_ONLY, '2026-08-19T10:00:00+00:00', 2);
$necessaryOnlyParsed = PrivacyConsent::parse_browser_record(PrivacyConsent::encode_record($necessaryOnly));
$assert(
	'necessary_only_parse',
	$necessaryOnlyParsed['is_valid'] === true
	&& $necessaryOnlyParsed['state'] === PrivacyConsent::STATE_NECESSARY_ONLY
	&& $necessaryOnlyParsed['requires_redecision'] === false,
	$necessaryOnlyParsed
);

$analyticsAllowed = PrivacyConsent::build_record_for_state(PrivacyConsent::STATE_ANALYTICS_ALLOWED, '2026-08-19T10:00:00+00:00', 2);
$analyticsAllowedParsed = PrivacyConsent::parse_browser_record(PrivacyConsent::encode_record($analyticsAllowed));
$assert(
	'analytics_allowed_parse',
	$analyticsAllowedParsed['is_valid'] === true
	&& $analyticsAllowedParsed['state'] === PrivacyConsent::STATE_ANALYTICS_ALLOWED
	&& $analyticsAllowedParsed['requires_redecision'] === false,
	$analyticsAllowedParsed
);

$undecidedParsed = PrivacyConsent::parse_browser_record('');
$assert(
	'undecided_parse',
	$undecidedParsed['is_valid'] === false
	&& $undecidedParsed['state'] === PrivacyConsent::STATE_UNDECIDED,
	$undecidedParsed
);

$tamperedParsed = PrivacyConsent::parse_browser_record('{"version":2,"necessary":true,"analytics":true,"decided_at":"2026-08-19T10:00:00+00:00","evil":"1"}');
$assert(
	'tampered_payload_to_undecided',
	$tamperedParsed['is_valid'] === false
	&& $tamperedParsed['state'] === PrivacyConsent::STATE_UNDECIDED,
	$tamperedParsed
);

$impossibleParsed = PrivacyConsent::parse_browser_record('{"version":2,"necessary":false,"analytics":true,"decided_at":"2026-08-19T10:00:00+00:00"}');
$assert(
	'necessary_false_rejected',
	$impossibleParsed['is_valid'] === false
	&& $impossibleParsed['state'] === PrivacyConsent::STATE_UNDECIDED,
	$impossibleParsed
);

$invalidTimestampParsed = PrivacyConsent::parse_browser_record('{"version":2,"necessary":true,"analytics":false,"decided_at":"2010-01-01T00:00:00+00:00"}');
$assert(
	'invalid_timestamp_rejected',
	$invalidTimestampParsed['is_valid'] === false
	&& $invalidTimestampParsed['state'] === PrivacyConsent::STATE_UNDECIDED,
	$invalidTimestampParsed
);

$oldVersionParsed = PrivacyConsent::parse_browser_record('{"version":1,"necessary":true,"analytics":true,"decided_at":"2026-08-19T10:00:00+00:00"}');
$assert(
	'old_version_requires_redecision',
	$oldVersionParsed['is_valid'] === true
	&& $oldVersionParsed['requires_redecision'] === true
	&& PrivacyConsent::is_allowed('analytics', $oldVersionParsed) === false,
	$oldVersionParsed
);

$assert(
	'current_version_accepted',
	PrivacyConsent::current_version() === 2
	&& PrivacyConsent::is_allowed('analytics', $analyticsAllowedParsed) === true,
	array(
		'current_version' => PrivacyConsent::current_version(),
		'parsed' => $analyticsAllowedParsed,
	)
);

$assert(
	'unknown_category_rejected',
	PrivacyConsent::is_allowed('marketing', $analyticsAllowedParsed) === false
	&& PrivacyConsent::is_allowed('necessary', $analyticsAllowedParsed) === true,
	array(
		'necessary_allowed' => PrivacyConsent::is_allowed('necessary', $analyticsAllowedParsed),
		'unknown_allowed' => PrivacyConsent::is_allowed('marketing', $analyticsAllowedParsed),
	)
);

$attributes = PrivacyConsent::cookie_attributes();
$assert(
	'cookie_attributes_contract',
	$attributes['path'] === '/'
	&& $attributes['secure'] === true
	&& $attributes['httponly'] === false
	&& $attributes['samesite'] === 'Lax'
	&& $attributes['max_age'] === 365 * DAY_IN_SECONDS,
	$attributes
);

$failures = array_values(array_filter(
	$results,
	static fn(array $row): bool => 'FAIL' === $row['status']
));

echo json_encode(
	array(
		'status' => empty($failures) ? 'PASS' : 'FAIL',
		'php' => PHP_VERSION,
		'tests' => $results,
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE
);
