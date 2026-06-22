<?php
/**
 * Native Settings API for global theme options (ACF Pro unavailable).
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register settings, section, and fields.
 */
function fws_synthetic_register_options() {
	register_setting(
		'fws_synthetic_options_group',
		'fws_synthetic_options',
		array(
			'type'              => 'array',
			'sanitize_callback' => 'fws_synthetic_sanitize_options',
			'default'           => fws_synthetic_default_options(),
		)
	);

	add_settings_section(
		'fws_synthetic_contacts',
		__( 'Контактные данные', 'fws-synthetic' ),
		'fws_synthetic_contacts_section_cb',
		'fws-synthetic-options'
	);

	$fields = array(
		'phone'     => __( 'Телефон', 'fws-synthetic' ),
		'email'     => __( 'Email', 'fws-synthetic' ),
		'address'   => __( 'Адрес', 'fws-synthetic' ),
		'cta_title' => __( 'Заголовок CTA', 'fws-synthetic' ),
		'cta_text'  => __( 'Текст CTA', 'fws-synthetic' ),
	);

	foreach ( $fields as $key => $label ) {
		add_settings_field(
			'fws_synthetic_' . $key,
			$label,
			'fws_synthetic_option_field_cb',
			'fws-synthetic-options',
			'fws_synthetic_contacts',
			array(
				'key'  => $key,
				'type' => 'cta_text' === $key || 'address' === $key ? 'textarea' : 'text',
			)
		);
	}
}
add_action( 'admin_init', 'fws_synthetic_register_options' );

/**
 * Default option values.
 *
 * @return array<string, string>
 */
function fws_synthetic_default_options() {
	return array(
		'phone'     => '+7 (000) 000-00-00',
		'email'     => 'synthetic@example.invalid',
		'address'   => 'синтетический, без реальной геолокации',
		'cta_title' => 'Готовы проверить pipeline?',
		'cta_text'  => 'Синтетический CTA-блок для global options mapping.',
	);
}

/**
 * Sanitize options array.
 *
 * @param array<string, mixed> $input Raw input.
 * @return array<string, string>
 */
function fws_synthetic_sanitize_options( $input ) {
	$defaults = fws_synthetic_default_options();
	$output   = array();

	foreach ( $defaults as $key => $default ) {
		if ( ! isset( $input[ $key ] ) ) {
			$output[ $key ] = $default;
			continue;
		}

		if ( 'email' === $key ) {
			$output[ $key ] = sanitize_email( $input[ $key ] );
		} elseif ( in_array( $key, array( 'cta_text', 'address' ), true ) ) {
			$output[ $key ] = sanitize_textarea_field( $input[ $key ] );
		} else {
			$output[ $key ] = sanitize_text_field( $input[ $key ] );
		}
	}

	return $output;
}

/**
 * Contacts section description.
 */
function fws_synthetic_contacts_section_cb() {
	echo '<p>' . esc_html__( 'Глобальные контакты и CTA. При отсутствии ACF Pro используется Settings API.', 'fws-synthetic' ) . '</p>';
}

/**
 * Render a single option field.
 *
 * @param array<string, string> $args Field args.
 */
function fws_synthetic_option_field_cb( $args ) {
	$options = get_option( 'fws_synthetic_options', fws_synthetic_default_options() );
	$key     = $args['key'];
	$value   = isset( $options[ $key ] ) ? $options[ $key ] : '';
	$name    = 'fws_synthetic_options[' . esc_attr( $key ) . ']';

	if ( 'textarea' === $args['type'] ) {
		printf(
			'<textarea name="%1$s" rows="3" class="large-text">%2$s</textarea>',
			esc_attr( $name ),
			esc_textarea( $value )
		);
	} else {
		printf(
			'<input type="text" name="%1$s" value="%2$s" class="regular-text" />',
			esc_attr( $name ),
			esc_attr( $value )
		);
	}
}

/**
 * Add options page under Appearance.
 */
function fws_synthetic_options_menu() {
	add_theme_page(
		__( 'FWS Synthetic — настройки', 'fws-synthetic' ),
		__( 'FWS Synthetic', 'fws-synthetic' ),
		'manage_options',
		'fws-synthetic-options',
		'fws_synthetic_options_page_cb'
	);
}
add_action( 'admin_menu', 'fws_synthetic_options_menu' );

/**
 * Render options page.
 */
function fws_synthetic_options_page_cb() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}
	?>
	<div class="wrap">
		<h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
		<form action="options.php" method="post">
			<?php
			settings_fields( 'fws_synthetic_options_group' );
			do_settings_sections( 'fws-synthetic-options' );
			submit_button();
			?>
		</form>
	</div>
	<?php
}
