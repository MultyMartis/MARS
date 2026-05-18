<?php
/**
 * Read-only WordPress data access for WPilot endpoints.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Site_Reader {
	const MAX_PAGES = WPilot_Constants::RESPONSE_MAX_PAGES;

	/**
	 * Get safe site metadata.
	 *
	 * @return array
	 */
	public function get_site_info() {
		global $wp_version;

		$theme = wp_get_theme();

		return array(
			'site_url'        => site_url(),
			'home_url'        => home_url(),
			'wp_version'      => $wp_version,
			'php_version'     => PHP_VERSION,
			'active_theme'    => $theme->get( 'Name' ),
			'is_multisite'    => is_multisite(),
			'bridge_enabled'  => (bool) WPilot_Settings::get_options()['bridge_enabled'],
			'write_enabled'   => ! empty( WPilot_Settings::get_options()['write_enabled'] ),
		);
	}

	/**
	 * Get active theme metadata only.
	 *
	 * @return array
	 */
	public function get_themes() {
		$theme = wp_get_theme();

		return array(
			'active_theme' => array(
				'name'       => $theme->get( 'Name' ),
				'version'    => $theme->get( 'Version' ),
				'template'   => $theme->get_template(),
				'stylesheet' => $theme->get_stylesheet(),
			),
		);
	}

	/**
	 * Get active plugins metadata.
	 *
	 * @return array
	 */
	public function get_plugins() {
		if ( ! function_exists( 'get_plugin_data' ) ) {
			require_once ABSPATH . 'wp-admin/includes/plugin.php';
		}

		$active_plugins = (array) get_option( 'active_plugins', array() );
		$items          = array();

		foreach ( $active_plugins as $plugin_file ) {
			$plugin_path = WP_PLUGIN_DIR . '/' . $plugin_file;
			$data        = file_exists( $plugin_path ) ? get_plugin_data( $plugin_path, false, false ) : array();

			$items[] = array(
				'name'        => isset( $data['Name'] ) ? $data['Name'] : '',
				'version'     => isset( $data['Version'] ) ? $data['Version'] : '',
				'plugin_file' => $plugin_file,
			);
		}

		return array(
			'plugins' => $items,
		);
	}

	/**
	 * Get a capped list of pages.
	 *
	 * @return array
	 */
	public function get_pages() {
		$posts = get_posts(
			array(
				'post_type'      => 'page',
				'post_status'    => array( 'publish', 'draft', 'private', 'pending', 'future' ),
				'posts_per_page' => self::MAX_PAGES,
				'orderby'        => 'modified',
				'order'          => 'DESC',
				'no_found_rows'  => true,
			)
		);

		$items = array();

		foreach ( $posts as $post ) {
			$items[] = $this->format_page_summary( $post );
		}

		return array(
			'items' => $items,
			'limit' => self::MAX_PAGES,
		);
	}

	/**
	 * Read a single page.
	 *
	 * @param int $id Page ID.
	 * @return array|WP_REST_Response
	 */
	public function get_page( $id ) {
		$post = get_post( absint( $id ) );

		if ( ! $this->is_readable_page( $post ) ) {
			return WPilot_Errors::target_not_found();
		}

		$content = $this->safe_content( $post );

		return array(
			'id'               => (int) $post->ID,
			'title'            => $this->safe_title( $post ),
			'status'           => $this->safe_status( $post ),
			'modified'         => $this->safe_modified_time( $post ),
			'content_raw'      => $content,
			'content_checksum' => $this->checksum( $content ),
			'has_wpbakery'     => WPilot_WPBakery_Detector::has_wpbakery( $content ),
		);
	}

	/**
	 * Read deterministic page structure signals.
	 *
	 * @param int $id Page ID.
	 * @return array|WP_REST_Response
	 */
	public function get_page_structure( $id ) {
		$post = get_post( absint( $id ) );

		if ( ! $this->is_readable_page( $post ) ) {
			return WPilot_Errors::target_not_found();
		}

		$content = $this->safe_content( $post );

		return array(
			'id'               => (int) $post->ID,
			'has_wpbakery'     => WPilot_WPBakery_Detector::has_wpbakery( $content ),
			'shortcode_counts' => WPilot_WPBakery_Detector::shortcode_counts( $content ),
			'basic_integrity'  => WPilot_WPBakery_Detector::basic_integrity( $content ),
			'warnings'         => WPilot_WPBakery_Detector::warnings( $content ),
		);
	}

	/**
	 * Get indexing-related read-only signals.
	 *
	 * @return array
	 */
	public function get_indexing_state() {
		$blog_public = get_option( 'blog_public' );

		return array(
			'blog_public'                => (string) $blog_public,
			'robots_txt_available'       => $this->robots_txt_available(),
			'discourage_search_engines'  => '0' === (string) $blog_public,
			'notes'                      => array( 'robots_txt_available is a local WordPress routing signal, not an external crawl.' ),
		);
	}

	/**
	 * Format compact page metadata.
	 *
	 * @param WP_Post $post Page post.
	 * @return array
	 */
	private function format_page_summary( WP_Post $post ) {
		return array(
			'id'           => (int) $post->ID,
			'title'        => $this->safe_title( $post ),
			'status'       => $this->safe_status( $post ),
			'modified'     => $this->safe_modified_time( $post ),
			'link'         => $this->safe_permalink( $post ),
			'has_wpbakery' => WPilot_WPBakery_Detector::has_wpbakery( $this->safe_content( $post ) ),
		);
	}

	/**
	 * Check MVP page readability.
	 *
	 * @param mixed $post Potential post object.
	 * @return bool
	 */
	private function is_readable_page( $post ) {
		return $post instanceof WP_Post && 'page' === $post->post_type;
	}

	/**
	 * Generate content checksum.
	 *
	 * @param string $content Content.
	 * @return string
	 */
	private function checksum( $content ) {
		return 'sha256:' . hash( 'sha256', (string) $content );
	}

	/**
	 * Safely read post content as JSON-safe UTF-8.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function safe_content( WP_Post $post ) {
		$content = isset( $post->post_content ) && is_string( $post->post_content ) ? $post->post_content : '';

		if ( function_exists( 'wp_check_invalid_utf8' ) ) {
			$content = wp_check_invalid_utf8( $content, true );
		}

		return is_string( $content ) ? $content : '';
	}

	/**
	 * Return a plain-text title suitable for API JSON.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function safe_title( WP_Post $post ) {
		$title = get_the_title( $post );
		$title = is_string( $title ) ? $title : '';

		return wp_strip_all_tags( $title );
	}

	/**
	 * Return a bounded post status string.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function safe_status( WP_Post $post ) {
		$status = get_post_status( $post );

		return is_string( $status ) ? sanitize_key( $status ) : '';
	}

	/**
	 * Return ISO-like modified time or an empty fallback.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function safe_modified_time( WP_Post $post ) {
		$modified = get_post_modified_time( 'c', true, $post );

		return is_string( $modified ) ? $modified : '';
	}

	/**
	 * Return permalink as a string without assuming permalink generation succeeds.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function safe_permalink( WP_Post $post ) {
		$link = get_permalink( $post );

		return is_string( $link ) ? esc_url_raw( $link ) : '';
	}

	/**
	 * Safely detect whether WordPress can produce robots.txt output.
	 *
	 * @return bool
	 */
	private function robots_txt_available() {
		return function_exists( 'do_robots' );
	}
}
