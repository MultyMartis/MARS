<?php
/**
 * Central constants for the WPilot read-only MVP.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Constants {
	const VERSION        = '0.3.0';
	const SCHEMA_VERSION = '0.2.0';

	const PLUGIN_SLUG = 'metacode-wpilot';
	const TEXT_DOMAIN = 'metacode-wpilot';
	const DEV_LABEL   = 'DEV/test';

	const REST_NAMESPACE = 'wpilot/v1';

	const OPTION_NAME = 'wpilot_options';

	const TRANSIENT_PREFIX = 'wpilot_';

	const STATE_EMERGENCY_DISABLED                = 'emergency-disabled';
	const STATE_DISABLED                          = 'disabled';
	const STATE_ENABLED_WITHOUT_DEV_CONFIRMATION = 'enabled-without-dev-confirmation';
	const STATE_TOKEN_GENERATED                   = 'token-generated';
	const STATE_ENABLED_DEV                       = 'enabled-dev';

	const CAPABILITY_MANAGE_OPTIONS = 'manage_options';

	const TOKEN_HEADER_NAME     = 'X-WPilot-Token';
	const TOKEN_HEADER_FALLBACK = 'x_wpilot_token';
	const TOKEN_PREFIX          = 'wpilot_';
	const TOKEN_LENGTH          = 48;

	const RESPONSE_MAX_PAGES = 50;

	const CONTENT_TYPE_JSON = 'application/json; charset=UTF-8';
}
