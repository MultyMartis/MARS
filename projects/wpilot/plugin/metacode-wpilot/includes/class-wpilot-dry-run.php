<?php
/**
 * Dry-run scoped replacement analysis for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Dry_Run {
	const MAX_CONTENT_BYTES = 1048576;
	const MAX_VALUE_BYTES   = 8192;

	/**
	 * Allowed request fields for Phase 2A.
	 *
	 * @var array
	 */
	private static $allowed_fields = array(
		'find',
		'replace',
		'expected_occurrences',
		'scope',
		'operation_note',
	);

	/**
	 * Validate an exact replacement for execute path without mutating content.
	 *
	 * @param int    $page_id Page ID.
	 * @param string $find Exact source text.
	 * @param string $replace Replacement text.
	 * @return array|WP_Error
	 */
	public function validate_exact_replacement( $page_id, $find, $replace ) {
		$page_id = absint( $page_id );
		$find    = is_string( $find ) ? $find : '';
		$replace = is_string( $replace ) ? $replace : '';

		if ( '' === $find ) {
			return new WP_Error( 'INVALID_REQUEST', 'search is required and must be a non-empty string.' );
		}

		if ( strlen( $find ) > self::MAX_VALUE_BYTES || strlen( $replace ) > self::MAX_VALUE_BYTES ) {
			return new WP_Error( 'CONTENT_TOO_LARGE', 'search or replace exceeds the scoped replace value limit.' );
		}

		if ( ! $this->is_valid_utf8( $find ) || ! $this->is_valid_utf8( $replace ) ) {
			return new WP_Error( 'INVALID_REQUEST', 'search and replace must be safe UTF-8 strings.' );
		}

		if ( false !== strpos( $replace, '[' ) || false !== strpos( $replace, ']' ) ) {
			return new WP_Error( 'UNSAFE_WPBAKERY_ZONE', 'Replacement text must not introduce shortcode-like syntax.' );
		}

		if ( preg_match( '/<\s*(script|style)\b/i', $replace ) ) {
			return new WP_Error( 'UNSAFE_CONTENT_TYPE', 'Replacement text must not introduce script or style content.' );
		}

		$post = get_post( $page_id );
		if ( ! $this->is_supported_page( $post ) ) {
			return new WP_Error( 'TARGET_NOT_FOUND', 'Target page was not found.' );
		}

		$content = $this->safe_content( $post );
		if ( null === $content ) {
			return new WP_Error( 'UNSAFE_CONTENT_TYPE', 'Target content is not safe UTF-8 content for scoped replace.' );
		}

		if ( strlen( $content ) > self::MAX_CONTENT_BYTES ) {
			return new WP_Error( 'CONTENT_TOO_LARGE', 'Target content exceeds the scoped replace scan limit.' );
		}

		$positions = $this->exact_positions( $content, $find );
		$count     = count( $positions );

		if ( 0 === $count ) {
			return new WP_Error( 'ZERO_MATCHES', 'Source text does not appear in current content.' );
		}

		if ( 1 < $count ) {
			return new WP_Error( 'MULTIPLE_MATCHES', 'Source text appears more than once.' );
		}

		$wpbakery = $this->validate_wpbakery_zone( $content, $positions[0], strlen( $find ), $replace, array() );
		if ( $wpbakery instanceof WP_REST_Response ) {
			$data = $wpbakery->get_data();
			$code = is_array( $data ) && isset( $data['error']['code'] ) ? (string) $data['error']['code'] : 'SAFE_UNKNOWN';
			$msg  = is_array( $data ) && isset( $data['error']['message'] ) ? (string) $data['error']['message'] : 'Scoped replace validation refused.';

			return new WP_Error( $code, $msg );
		}

		return array(
			'page_id'                 => (int) $post->ID,
			'match_count'             => 1,
			'content_checksum_before' => $this->checksum( $content ),
			'find_checksum'           => $this->checksum( $find ),
			'replace_checksum'        => $this->checksum( $replace ),
			'wpbakery'                => array(
				'has_wpbakery' => WPilot_WPBakery_Detector::has_wpbakery( $content ),
				'safe_zone'    => true,
				'warnings'     => $wpbakery['warnings'],
			),
		);
	}

	/**
	 * Analyze an exact replacement without mutating content.
	 *
	 * @param int             $page_id Page ID.
	 * @param WP_REST_Request $request REST request.
	 * @param array           $meta Response metadata.
	 * @return array|WP_REST_Response
	 */
	public function analyze( $page_id, WP_REST_Request $request, array $meta ) {
		$payload = $request->get_json_params();

		if ( ! is_array( $payload ) ) {
			return $this->refusal( 'INVALID_REQUEST', 'Request body must be a JSON object.', 'request', $meta, 400 );
		}

		$request_error = $this->validate_request( $payload, $meta );
		if ( $request_error instanceof WP_REST_Response ) {
			return $request_error;
		}

		$post = get_post( absint( $page_id ) );
		if ( ! $this->is_supported_page( $post ) ) {
			return $this->refusal( 'PAGE_NOT_FOUND', 'Target page was not found or is outside the MVP page scope.', 'validation', $meta, 404 );
		}

		$content = $this->safe_content( $post );
		if ( null === $content ) {
			return $this->refusal( 'UNSAFE_CONTENT_TYPE', 'Target content is not safe UTF-8 content for deterministic dry-run.', 'validation', $meta, 422 );
		}

		if ( strlen( $content ) > self::MAX_CONTENT_BYTES ) {
			return $this->refusal( 'CONTENT_TOO_LARGE', 'Target content exceeds the dry-run scan limit.', 'validation', $meta, 413 );
		}

		$find      = $payload['find'];
		$replace   = $payload['replace'];
		$positions = $this->exact_positions( $content, $find );
		$count     = count( $positions );

		if ( 0 === $count ) {
			return $this->refusal( 'ZERO_MATCHES', 'Source text does not appear in current content.', 'dry_run', $meta, 404 );
		}

		if ( 1 < $count ) {
			return $this->refusal( 'MULTIPLE_MATCHES', 'Source text appears more than once.', 'dry_run', $meta, 409 );
		}

		$wpbakery = $this->validate_wpbakery_zone( $content, $positions[0], strlen( $find ), $replace, $meta );
		if ( $wpbakery instanceof WP_REST_Response ) {
			return $wpbakery;
		}

		return array(
			'dry_run'                 => true,
			'page_id'                 => (int) $post->ID,
			'would_replace'           => true,
			'match_count'             => 1,
			'expected_occurrences'    => 1,
			'content_checksum_before' => $this->checksum( $content ),
			'find_checksum'           => $this->checksum( $find ),
			'replace_checksum'        => $this->checksum( $replace ),
			'wpbakery'                => array(
				'has_wpbakery' => WPilot_WPBakery_Detector::has_wpbakery( $content ),
				'safe_zone'    => true,
				'warnings'     => $wpbakery['warnings'],
			),
		);
	}

	/**
	 * Validate request payload shape and allowed MVP values.
	 *
	 * @param array $payload Request JSON.
	 * @param array $meta Response metadata.
	 * @return true|WP_REST_Response
	 */
	private function validate_request( array $payload, array $meta ) {
		$unknown_fields = array_diff( array_keys( $payload ), self::$allowed_fields );
		if ( ! empty( $unknown_fields ) ) {
			return $this->refusal( 'INVALID_REQUEST', 'Request contains unsupported fields.', 'request', $meta, 400 );
		}

		if ( ! array_key_exists( 'find', $payload ) || ! is_string( $payload['find'] ) || '' === $payload['find'] ) {
			return $this->refusal( 'INVALID_REQUEST', 'find is required and must be a non-empty string.', 'request', $meta, 400 );
		}

		if ( ! array_key_exists( 'replace', $payload ) || ! is_string( $payload['replace'] ) ) {
			return $this->refusal( 'INVALID_REQUEST', 'replace is required and must be a string.', 'request', $meta, 400 );
		}

		if ( ! array_key_exists( 'expected_occurrences', $payload ) || 1 !== $payload['expected_occurrences'] ) {
			return $this->refusal( 'INVALID_REQUEST', 'expected_occurrences must be exactly 1 for the MVP.', 'request', $meta, 400 );
		}

		if ( ! array_key_exists( 'scope', $payload ) || 'content_raw' !== $payload['scope'] ) {
			return $this->refusal( 'INVALID_REQUEST', 'scope must be content_raw for the MVP.', 'request', $meta, 400 );
		}

		if ( strlen( $payload['find'] ) > self::MAX_VALUE_BYTES || strlen( $payload['replace'] ) > self::MAX_VALUE_BYTES ) {
			return $this->refusal( 'CONTENT_TOO_LARGE', 'find or replace exceeds the dry-run value limit.', 'validation', $meta, 413 );
		}

		if ( ! $this->is_valid_utf8( $payload['find'] ) || ! $this->is_valid_utf8( $payload['replace'] ) ) {
			return $this->refusal( 'INVALID_REQUEST', 'find and replace must be safe UTF-8 strings.', 'request', $meta, 400 );
		}

		if ( false !== strpos( $payload['replace'], '[' ) || false !== strpos( $payload['replace'], ']' ) ) {
			return $this->refusal( 'UNSAFE_WPBAKERY_ZONE', 'Replacement text must not introduce shortcode-like syntax.', 'wpbakery', $meta, 422 );
		}

		if ( preg_match( '/<\s*(script|style)\b/i', $payload['replace'] ) ) {
			return $this->refusal( 'UNSAFE_CONTENT_TYPE', 'Replacement text must not introduce script or style content.', 'validation', $meta, 422 );
		}

		if ( isset( $payload['operation_note'] ) && ! is_string( $payload['operation_note'] ) ) {
			return $this->refusal( 'INVALID_REQUEST', 'operation_note must be a string when provided.', 'request', $meta, 400 );
		}

		return true;
	}

	/**
	 * Validate conservative WPBakery and markup safety around the match.
	 *
	 * @param string $content Content.
	 * @param int    $offset Match offset.
	 * @param int    $length Match length.
	 * @param string $replace Replacement text.
	 * @param array  $meta Response metadata.
	 * @return array|WP_REST_Response
	 */
	private function validate_wpbakery_zone( $content, $offset, $length, $replace, array $meta ) {
		if ( $this->contains_unclosed_wpbakery_fragment( $content ) ) {
			return $this->refusal( 'SAFE_UNKNOWN', 'WPBakery shortcode structure cannot be classified safely.', 'safe_unknown', $meta, 422 );
		}

		if ( ! $this->known_shortcodes_balanced( $content ) ) {
			return $this->refusal( 'UNSAFE_WPBAKERY_ZONE', 'WPBakery shortcode structure appears malformed.', 'wpbakery', $meta, 422 );
		}

		if ( $this->span_overlaps_ranges( $offset, $length, $this->shortcode_tag_ranges( $content ) ) ) {
			return $this->refusal( 'UNSAFE_WPBAKERY_ZONE', 'Source text overlaps shortcode tag or attributes.', 'wpbakery', $meta, 422 );
		}

		if ( $this->span_overlaps_ranges( $offset, $length, $this->raw_shortcode_ranges( $content ) ) ) {
			return $this->refusal( 'UNSAFE_WPBAKERY_ZONE', 'Source text is inside a raw WPBakery block.', 'wpbakery', $meta, 422 );
		}

		if ( $this->span_overlaps_ranges( $offset, $length, $this->html_tag_ranges( $content ) ) ) {
			return $this->refusal( 'UNSAFE_CONTENT_TYPE', 'Source text overlaps HTML tag syntax.', 'validation', $meta, 422 );
		}

		if ( $this->span_overlaps_ranges( $offset, $length, $this->script_style_ranges( $content ) ) ) {
			return $this->refusal( 'UNSAFE_CONTENT_TYPE', 'Source text is inside script or style content.', 'validation', $meta, 422 );
		}

		if ( preg_match( '/<\s*(script|style)\b/i', $replace ) ) {
			return $this->refusal( 'UNSAFE_CONTENT_TYPE', 'Replacement text must not introduce script or style content.', 'validation', $meta, 422 );
		}

		return array(
			'warnings' => WPilot_WPBakery_Detector::warnings( $content ),
		);
	}

	/**
	 * Return exact non-overlapping match offsets.
	 *
	 * @param string $content Content.
	 * @param string $needle Exact source string.
	 * @return array
	 */
	private function exact_positions( $content, $needle ) {
		$positions = array();
		$offset    = 0;
		$length    = strlen( $needle );

		while ( false !== ( $position = strpos( $content, $needle, $offset ) ) ) {
			$positions[] = $position;
			$offset      = $position + $length;

			if ( count( $positions ) > 1 ) {
				break;
			}
		}

		return $positions;
	}

	/**
	 * Identify shortcode tag ranges.
	 *
	 * @param string $content Content.
	 * @return array
	 */
	private function shortcode_tag_ranges( $content ) {
		$opening = $this->regex_ranges( '/\[(?:\/)?[A-Za-z0-9_:-]+/', $content );
		$closing = $this->regex_ranges( '/\[\/[A-Za-z0-9_:-]+\]/', $content );

		return array_merge( $opening, $closing );
	}

	/**
	 * Identify raw WPBakery shortcode block ranges.
	 *
	 * @param string $content Content.
	 * @return array
	 */
	private function raw_shortcode_ranges( $content ) {
		$opening = $this->regex_ranges( '/\[vc_raw_(?:html|js)(?:\s[^\]]*)?\]/', $content );
		$closing = $this->regex_ranges( '/\[\/vc_raw_(?:html|js)\]/', $content );

		return array_merge( $opening, $closing );
	}

	/**
	 * Identify HTML tag syntax ranges.
	 *
	 * @param string $content Content.
	 * @return array
	 */
	private function html_tag_ranges( $content ) {
		return $this->regex_ranges( '/<[^>]+>/', $content );
	}

	/**
	 * Identify script and style block ranges.
	 *
	 * @param string $content Content.
	 * @return array
	 */
	private function script_style_ranges( $content ) {
		return $this->regex_ranges( '/<\s*(script|style)\b[^>]*>.*?<\s*\/\s*\1\s*>/is', $content );
	}

	/**
	 * Extract regex match ranges without exposing content.
	 *
	 * @param string $pattern Regex pattern.
	 * @param string $content Content.
	 * @return array
	 */
	private function regex_ranges( $pattern, $content ) {
		$matches = array();
		$result  = @preg_match_all( $pattern, $content, $matches, PREG_OFFSET_CAPTURE );

		if ( false === $result || empty( $matches[0] ) ) {
			return array();
		}

		$ranges = array();
		foreach ( $matches[0] as $match ) {
			$ranges[] = array(
				'start' => (int) $match[1],
				'end'   => (int) $match[1] + strlen( $match[0] ),
			);
		}

		return $ranges;
	}

	/**
	 * Check whether a span overlaps any unsafe range.
	 *
	 * @param int   $offset Span offset.
	 * @param int   $length Span length.
	 * @param array $ranges Ranges.
	 * @return bool
	 */
	private function span_overlaps_ranges( $offset, $length, array $ranges ) {
		$end = $offset + $length;

		foreach ( $ranges as $range ) {
			if ( $offset < $range['end'] && $end > $range['start'] ) {
				return true;
			}
		}

		return false;
	}

	/**
	 * Conservative balance check for supported paired shortcodes.
	 *
	 * @param string $content Content.
	 * @return bool
	 */
	private function known_shortcodes_balanced( $content ) {
		$paired = array( 'vc_row', 'vc_column', 'vc_column_text', 'vc_section', 'vc_raw_html', 'vc_raw_js' );

		foreach ( $paired as $shortcode ) {
			$open_matches  = array();
			$close_matches = array();
			$open          = preg_match_all( '/\[' . preg_quote( $shortcode, '/' ) . '(?:\s|\])/', $content, $open_matches );
			$close         = preg_match_all( '/\[\/' . preg_quote( $shortcode, '/' ) . '\]/', $content, $close_matches );

			if ( false === $open || false === $close || $open !== $close ) {
				return false;
			}
		}

		return true;
	}

	/**
	 * Detect unclosed WPBakery-looking fragments that cannot be classified safely.
	 *
	 * @param string $content Content.
	 * @return bool
	 */
	private function contains_unclosed_wpbakery_fragment( $content ) {
		return 1 === preg_match( '/\[(?:\/)?vc_[^\]]*$/i', $content );
	}

	/**
	 * Check MVP page support.
	 *
	 * @param mixed $post Potential post.
	 * @return bool
	 */
	private function is_supported_page( $post ) {
		return $post instanceof WP_Post && 'page' === $post->post_type;
	}

	/**
	 * Read content only when it is safe UTF-8 without repair.
	 *
	 * @param WP_Post $post Page post.
	 * @return string|null
	 */
	private function safe_content( WP_Post $post ) {
		$content = isset( $post->post_content ) && is_string( $post->post_content ) ? $post->post_content : '';

		return $this->is_valid_utf8( $content ) ? $content : null;
	}

	/**
	 * Check UTF-8 validity without hidden repair.
	 *
	 * @param string $value Value.
	 * @return bool
	 */
	private function is_valid_utf8( $value ) {
		if ( ! is_string( $value ) ) {
			return false;
		}

		if ( function_exists( 'wp_check_invalid_utf8' ) ) {
			return wp_check_invalid_utf8( $value, true ) === $value;
		}

		return true;
	}

	/**
	 * Generate deterministic checksum.
	 *
	 * @param string $value Value.
	 * @return string
	 */
	private function checksum( $value ) {
		return 'sha256:' . hash( 'sha256', (string) $value );
	}

	/**
	 * Build deterministic dry-run refusal response.
	 *
	 * @param string $code Error code.
	 * @param string $message Error message.
	 * @param string $stage Refusal stage.
	 * @param array  $meta Response metadata.
	 * @param int    $status HTTP status.
	 * @return WP_REST_Response
	 */
	private function refusal( $code, $message, $stage, array $meta, $status ) {
		return WPilot_Response::error(
			$code,
			$message,
			$meta,
			$status,
			array(
				'stage'              => $stage,
				'mutation_performed' => false,
				'rollback_available' => false,
			)
		);
	}
}
