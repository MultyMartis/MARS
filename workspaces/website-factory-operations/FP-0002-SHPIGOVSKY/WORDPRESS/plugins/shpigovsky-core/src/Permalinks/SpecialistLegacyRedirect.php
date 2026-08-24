<?php
/**
 * Deprecated /specyalisty/ → /specialisty/ migration redirects.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Permalinks;

use Shpigovsky\Core\ContentTypes\Specialist;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Permanent path-preserving redirects for the old specialists URL family.
 *
 * Complements the production `.htaccess` legacy-redirect fragment. Either layer
 * alone is sufficient; both must emit the same single 301 target (no chains).
 */
final class SpecialistLegacyRedirect implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'permalinks.specialist-legacy-redirect';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'template_redirect', array( __CLASS__, 'maybe_redirect' ), 0 );
	}

	/**
	 * 301 /specyalisty/ and /specyalisty/{slug}/ to /specialisty/ equivalents.
	 */
	public static function maybe_redirect() {
		if ( is_admin() || wp_doing_ajax() || wp_doing_cron() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
			return;
		}

		$uri = isset( $_SERVER['REQUEST_URI'] ) ? (string) wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
		if ( '' === $uri ) {
			return;
		}

		$path = (string) wp_parse_url( $uri, PHP_URL_PATH );
		if ( '' === $path ) {
			return;
		}

		$legacy = '/' . Specialist::LEGACY_REWRITE_SLUG;
		$canonical = '/' . Specialist::REWRITE_SLUG;

		// Exact hub: /specyalisty or /specyalisty/
		if ( $path === $legacy || $path === $legacy . '/' ) {
			self::redirect_permanent( home_url( $canonical . '/' ) );
			return;
		}

		// Singles: /specyalisty/{slug}/… → /specialisty/{slug}/
		$prefix = $legacy . '/';
		if ( 0 !== strpos( $path, $prefix ) ) {
			return;
		}

		$rest = substr( $path, strlen( $prefix ) );
		$rest = trim( (string) $rest, '/' );
		if ( '' === $rest ) {
			self::redirect_permanent( home_url( $canonical . '/' ) );
			return;
		}

		// Only the first path segment is the specialist slug; ignore deeper junk.
		$parts = explode( '/', $rest );
		$slug  = sanitize_title( (string) $parts[0] );
		if ( '' === $slug ) {
			return;
		}

		self::redirect_permanent( home_url( $canonical . '/' . $slug . '/' ) );
	}

	/**
	 * Issue a single 301 and exit.
	 *
	 * @param string $target Absolute target URL.
	 */
	private static function redirect_permanent( $target ) {
		$target = esc_url_raw( $target );
		if ( '' === $target ) {
			return;
		}

		// Preserve query string when present (UTM etc.).
		$query = isset( $_SERVER['QUERY_STRING'] ) ? (string) wp_unslash( $_SERVER['QUERY_STRING'] ) : '';
		if ( '' !== $query && false === strpos( $target, '?' ) ) {
			$target .= '?' . $query;
		}

		wp_safe_redirect( $target, 301 );
		exit;
	}
}
