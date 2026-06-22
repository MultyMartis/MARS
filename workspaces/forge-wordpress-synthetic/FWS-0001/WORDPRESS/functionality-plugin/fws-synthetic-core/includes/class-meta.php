<?php
/**
 * Register post meta for service fields (ACF fallback storage).
 *
 * @package FWS_Synthetic_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Post meta registration.
 */
class FWS_Synthetic_Meta {

	/**
	 * Meta keys exposed via REST and used by ACF fallback.
	 *
	 * @var array<int, string>
	 */
	private static $keys = array(
		'short_description',
		'hero_eyebrow',
		'hero_title',
		'hero_text',
		'hero_btn_primary_label',
		'hero_btn_primary_url',
		'hero_btn_secondary_label',
		'hero_btn_secondary_url',
		'faq_q1',
		'faq_a1',
		'faq_q2',
		'faq_a2',
		'faq_q3',
		'faq_a3',
	);

	/**
	 * Hook registration.
	 */
	public static function init() {
		add_action( 'init', array( __CLASS__, 'register_meta' ) );
		add_action( 'add_meta_boxes', array( __CLASS__, 'add_service_meta_box' ) );
		add_action( 'save_post_service', array( __CLASS__, 'save_service_meta' ) );
	}

	/**
	 * Register post meta for pages and services.
	 */
	public static function register_meta() {
		$post_types = array( 'service', 'page' );

		foreach ( self::$keys as $key ) {
			foreach ( $post_types as $post_type ) {
				register_post_meta(
					$post_type,
					$key,
					array(
						'single'            => true,
						'type'              => 'string',
						'show_in_rest'      => true,
						'auth_callback'     => array( __CLASS__, 'auth_callback' ),
						'sanitize_callback' => 'sanitize_textarea_field',
					)
				);
			}
		}
	}

	/**
	 * Auth callback for meta updates.
	 *
	 * @return bool
	 */
	public static function auth_callback() {
		return current_user_can( 'edit_posts' );
	}

	/**
	 * Meta box when ACF is inactive.
	 */
	public static function add_service_meta_box() {
		if ( function_exists( 'acf_add_local_field_group' ) || function_exists( 'get_field' ) ) {
			return;
		}

		add_meta_box(
			'fws_service_short_description',
			__( 'Краткое описание', 'fws-synthetic' ),
			array( __CLASS__, 'render_service_meta_box' ),
			'service',
			'normal',
			'high'
		);
	}

	/**
	 * Render short description field.
	 *
	 * @param WP_Post $post Current post.
	 */
	public static function render_service_meta_box( $post ) {
		wp_nonce_field( 'fws_service_meta', 'fws_service_meta_nonce' );
		$value = get_post_meta( $post->ID, 'short_description', true );
		?>
		<p>
			<label for="fws_short_description"><?php esc_html_e( 'Краткое описание (override excerpt)', 'fws-synthetic' ); ?></label>
		</p>
		<textarea id="fws_short_description" name="fws_short_description" rows="4" class="large-text"><?php echo esc_textarea( $value ); ?></textarea>
		<?php
	}

	/**
	 * Save service meta when ACF is inactive.
	 *
	 * @param int $post_id Post ID.
	 */
	public static function save_service_meta( $post_id ) {
		if ( function_exists( 'acf_add_local_field_group' ) || function_exists( 'get_field' ) ) {
			return;
		}

		if ( ! isset( $_POST['fws_service_meta_nonce'] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['fws_service_meta_nonce'] ) ), 'fws_service_meta' ) ) {
			return;
		}

		if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
			return;
		}

		if ( ! current_user_can( 'edit_post', $post_id ) ) {
			return;
		}

		if ( isset( $_POST['fws_short_description'] ) ) {
			update_post_meta(
				$post_id,
				'short_description',
				sanitize_textarea_field( wp_unslash( $_POST['fws_short_description'] ) )
			);
		}
	}

	/**
	 * Return registered meta keys.
	 *
	 * @return array<int, string>
	 */
	public static function get_keys() {
		return self::$keys;
	}
}
