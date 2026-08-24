<?php
/**
 * Template part: contacts/location-card.php
 *
 * Expects query var shpigovsky_contacts_location.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$location = get_query_var( 'shpigovsky_contacts_location', array() );

if ( ! is_array( $location ) || empty( $location ) ) {
	return;
}

$title            = isset( $location['title'] ) ? trim( (string) $location['title'] ) : '';
$address          = isset( $location['address'] ) ? trim( (string) $location['address'] ) : '';
$address_label    = isset( $location['address_label'] ) ? trim( (string) $location['address_label'] ) : '';
$hours_html       = isset( $location['hours_html'] ) ? (string) $location['hours_html'] : '';
$hours_label      = isset( $location['hours_label'] ) ? trim( (string) $location['hours_label'] ) : '';
$email            = isset( $location['email'] ) ? sanitize_email( (string) $location['email'] ) : '';
$email_label      = isset( $location['email_label'] ) ? trim( (string) $location['email_label'] ) : '';
$map_image        = isset( $location['map_image'] ) ? trim( (string) $location['map_image'] ) : '';
$map_embed        = isset( $location['map_embed'] ) ? trim( (string) $location['map_embed'] ) : '';
$map_embed_code   = isset( $location['map_embed_code'] ) ? (string) $location['map_embed_code'] : '';
$map_scroll       = ! empty( $location['map_scroll'] );
$map_script       = '' !== trim( $map_embed_code ) ? shpigovsky_normalize_yandex_constructor_embed( $map_embed_code, $map_scroll ) : '';
$map_alt          = isset( $location['map_alt'] ) ? trim( (string) $location['map_alt'] ) : '';
$map_fallback_url = '' !== $address ? 'https://yandex.ru/maps/?text=' . rawurlencode( $address ) : home_url( '/kontakty/' );
$simplified       = ! empty( $location['simplified'] );

if ( '' === $title && '' === $address ) {
	return;
}
?>
<article class="contacts-location">
	<?php if ( '' !== $title ) : ?>
		<h2 class="contacts-location__title"><?php echo esc_html( $title ); ?></h2>
	<?php endif; ?>

	<?php if ( $simplified ) : ?>
		<?php if ( '' !== $address ) : ?>
			<div class="contacts-location__detail-body">
				<p class="contacts-location__text"><?php echo wp_kses_post( nl2br( esc_html( $address ) ) ); ?></p>
			</div>
		<?php endif; ?>
	<?php else : ?>
		<ul class="contacts-location__details">
			<?php if ( '' !== $address ) : ?>
				<li class="contacts-location__detail">
					<span class="contacts-location__icon" aria-hidden="true">
						<i class="fas fa-map-marker-alt"></i>
					</span>
					<div class="contacts-location__detail-body">
						<address class="contacts-location__address contacts-location__text"><?php echo esc_html( $address ); ?></address>
						<?php if ( '' !== $address_label ) : ?>
							<p class="contacts-location__label"><?php echo esc_html( $address_label ); ?></p>
						<?php endif; ?>
					</div>
				</li>
			<?php endif; ?>

			<?php if ( '' !== $hours_html && '' !== $hours_label ) : ?>
				<li class="contacts-location__detail">
					<span class="contacts-location__icon" aria-hidden="true">
						<i class="fas fa-clock"></i>
					</span>
					<div class="contacts-location__detail-body">
						<p class="contacts-location__text"><?php echo wp_kses_post( $hours_html ); ?></p>
						<p class="contacts-location__label"><?php echo esc_html( $hours_label ); ?></p>
					</div>
				</li>
			<?php endif; ?>

			<?php if ( '' !== $email && is_email( $email ) ) : ?>
				<li class="contacts-location__detail">
					<span class="contacts-location__icon" aria-hidden="true">
						<i class="fas fa-envelope"></i>
					</span>
					<div class="contacts-location__detail-body">
						<p class="contacts-location__text">
							<a class="contacts-location__email" href="<?php echo esc_url( 'mailto:' . $email ); ?>"><?php echo esc_html( $email ); ?></a>
						</p>
						<?php if ( '' !== $email_label ) : ?>
							<p class="contacts-location__label"><?php echo esc_html( $email_label ); ?></p>
						<?php endif; ?>
					</div>
				</li>
			<?php endif; ?>
		</ul>
	<?php endif; ?>

	<?php if ( '' !== $map_script ) : ?>
		<figure class="contacts-location__map contacts-location__map--constructor">
			<div class="contacts-location__map-embed contacts-location__map-embed--constructor">
				<?php echo $map_script; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- sanitized Yandex Constructor script. ?>
			</div>
		</figure>
	<?php elseif ( '' !== $map_image ) : ?>
		<figure class="contacts-location__map">
			<img
				class="contacts-location__map-image"
				src="<?php echo esc_url( shpigovsky_asset_uri( $map_image ) ); ?>"
				width="1170"
				height="458"
				alt="<?php echo esc_attr( $map_alt ); ?>"
				loading="lazy"
				decoding="async"
			>
		</figure>
	<?php elseif ( '' !== $map_embed && shpigovsky_is_allowed_map_embed_url( $map_embed ) ) : ?>
		<figure class="contacts-location__map contacts-location__map--privacy-safe">
			<div class="contacts-location__map-fallback">
				<p class="contacts-location__map-fallback-title"><?php echo esc_html( $map_alt ); ?></p>
				<p class="contacts-location__map-fallback-text"><?php esc_html_e( 'Интерактивная карта открывается по вашему запросу, чтобы сторонний сервис не загружался автоматически.', 'shpigovsky' ); ?></p>
				<a class="btn btn_dark btn--primary contacts-location__map-fallback-link" href="<?php echo esc_url( $map_fallback_url ); ?>" target="_blank" rel="noopener noreferrer"><?php esc_html_e( 'Открыть карту', 'shpigovsky' ); ?></a>
			</div>
		</figure>
	<?php elseif ( '' !== trim( $map_embed_code ) ) : ?>
		<figure class="contacts-location__map contacts-location__map--privacy-safe">
			<div class="contacts-location__map-fallback">
				<p class="contacts-location__map-fallback-title"><?php echo esc_html( $map_alt ); ?></p>
				<p class="contacts-location__map-fallback-text"><?php esc_html_e( 'Карта временно недоступна. Откройте адрес в Яндекс Картах.', 'shpigovsky' ); ?></p>
				<a class="btn btn_dark btn--primary contacts-location__map-fallback-link" href="<?php echo esc_url( $map_fallback_url ); ?>" target="_blank" rel="noopener noreferrer"><?php esc_html_e( 'Открыть карту в Яндекс Картах', 'shpigovsky' ); ?></a>
			</div>
		</figure>
	<?php endif; ?>
</article>
