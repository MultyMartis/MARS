<?php
/**
 * Template part: contacts/map-body.php
 *
 * V9 contacts-map-body section with ACF/site-option bindings.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading   = get_the_title();
$intro     = shpigovsky_get_contacts_intro();
$phone     = shpigovsky_get_contacts_primary_phone();
$messengers = shpigovsky_get_contacts_messenger_rows();
$locations = shpigovsky_get_contacts_locations();

if ( '' === trim( $heading ) ) {
	$heading = __( 'Контакты', 'shpigovsky' );
}
?>
<section data-reveal class="contacts-body" aria-labelledby="contacts-page-heading">
	<div class="container contacts-body__container">
		<h1 class="contacts-body__heading" id="contacts-page-heading"><?php echo esc_html( $heading ); ?></h1>

		<?php if ( '' !== $intro ) : ?>
			<p class="contacts-body__intro block-whith-red-line"><?php echo esc_html( $intro ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $phone['display'] || ! empty( $messengers ) ) : ?>
			<div class="contacts-body__phone-row">
				<?php if ( '' !== $phone['display'] && '' !== $phone['href'] ) : ?>
					<a class="contacts-body__phone" href="<?php echo esc_url( $phone['href'] ); ?>"><?php echo esc_html( $phone['display'] ); ?></a>
				<?php elseif ( '' !== $phone['display'] ) : ?>
					<span class="contacts-body__phone"><?php echo esc_html( $phone['display'] ); ?></span>
				<?php endif; ?>

				<?php if ( ! empty( $messengers ) ) : ?>
					<div class="contacts-body__messengers" aria-label="<?php esc_attr_e( 'Мессенджеры', 'shpigovsky' ); ?>">
						<?php foreach ( $messengers as $messenger ) : ?>
							<?php
							$url   = isset( $messenger['url'] ) ? trim( (string) $messenger['url'] ) : '';
							$label = isset( $messenger['label'] ) ? trim( (string) $messenger['label'] ) : '';
							$icon  = isset( $messenger['icon'] ) ? trim( (string) $messenger['icon'] ) : '';

							if ( '' === $url ) {
								continue;
							}

							$aria_label = '' !== $label ? $label : __( 'Мессенджер', 'shpigovsky' );
							?>
							<a class="contacts-body__messenger-link" href="<?php echo esc_url( $url ); ?>" aria-label="<?php echo esc_attr( $aria_label ); ?>">
								<?php if ( '' !== $icon ) : ?>
									<img class="contacts-body__messenger-icon" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/social/' . $icon ) ); ?>" alt="" width="24" height="24">
								<?php else : ?>
									<span class="contacts-body__messenger-fallback"><?php echo esc_html( $aria_label ); ?></span>
								<?php endif; ?>
							</a>
						<?php endforeach; ?>
					</div>
				<?php endif; ?>
			</div>
		<?php endif; ?>

		<?php foreach ( $locations as $location ) : ?>
			<?php
			set_query_var( 'shpigovsky_contacts_location', $location );
			get_template_part( 'template-parts/contacts/location-card' );
			?>
		<?php endforeach; ?>
	</div>
</section>
