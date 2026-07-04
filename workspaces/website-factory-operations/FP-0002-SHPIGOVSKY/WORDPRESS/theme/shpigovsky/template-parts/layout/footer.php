<?php
/**
 * Site footer — V9 global chrome.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url          = shpigovsky_asset_uri( 'img/branding/logo.svg' );
$brand_label       = shpigovsky_brand_label();
$phone_primary     = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary   = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href   = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$site_email        = sanitize_email( shpigovsky_get_site_option( 'site_email' ) );
$address_lines     = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'site_address' ) );
$schedule_lines    = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'opening_hours' ) );
$callback_label    = shpigovsky_get_site_option( 'default_button_label' );
$callback_label    = '' !== $callback_label ? $callback_label : __( 'Заказать звонок', 'shpigovsky' );
$appointment_label = shpigovsky_get_site_option( 'default_secondary_button_label' );
$appointment_label = '' !== $appointment_label ? $appointment_label : __( 'Записаться', 'shpigovsky' );
?>
<footer class="site-footer" data-reveal role="contentinfo">
	<div class="container">
		<div class="site-footer__top">
			<a class="site-footer__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="site-footer__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>
			<?php get_template_part( 'template-parts/navigation/footer-social' ); ?>
			<?php if ( '' !== $phone_primary || '' !== $phone_secondary ) : ?>
				<div class="site-footer__phones">
					<?php if ( '' !== $phone_primary && '' !== $phone_primary_href ) : ?>
						<a class="site-footer__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
					<?php endif; ?>
					<?php if ( '' !== $phone_secondary && '' !== $phone_secondary_href ) : ?>
						<a class="site-footer__phone site-footer__phone--secondary" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
					<?php endif; ?>
				</div>
			<?php endif; ?>
			<div class="site-footer__actions">
				<button
					type="button"
					class="btn"
					data-modal-open="consultation"
					data-modal-source="footer-callback"
					data-modal-title="<?php echo esc_attr( $callback_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"
				><?php echo esc_html( $callback_label ); ?></button>
				<button
					type="button"
					class="btn btn_dark btn--primary"
					data-modal-open="consultation"
					data-modal-source="footer-appointment"
					data-modal-title="<?php echo esc_attr( $appointment_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $appointment_label ); ?>"
				><?php echo esc_html( $appointment_label ); ?></button>
			</div>
		</div>
		<div class="site-footer__main">
			<div class="site-footer__contacts">
				<?php if ( ! empty( $address_lines ) || ! empty( $schedule_lines ) ) : ?>
					<div class="site-footer__contact-item">
						<span class="site-footer__contact-icon" aria-hidden="true">
							<i class="fas fa-map-marker-alt"></i>
						</span>
						<div class="site-footer__contact-body">
							<?php if ( ! empty( $address_lines ) ) : ?>
								<?php foreach ( $address_lines as $line ) : ?>
									<p class="site-footer__contact-label"><?php echo esc_html( $line ); ?></p>
								<?php endforeach; ?>
							<?php endif; ?>
							<?php if ( ! empty( $schedule_lines ) ) : ?>
								<p class="site-footer__contact-meta">
									<?php foreach ( $schedule_lines as $line ) : ?>
										<em><?php echo esc_html( $line ); ?></em>
									<?php endforeach; ?>
								</p>
							<?php endif; ?>
						</div>
					</div>
				<?php endif; ?>
				<?php if ( '' !== $site_email && is_email( $site_email ) ) : ?>
					<div class="site-footer__contact-item">
						<span class="site-footer__contact-icon" aria-hidden="true">
							<i class="fas fa-envelope"></i>
						</span>
						<div class="site-footer__contact-body">
							<a class="site-footer__contact-label" href="<?php echo esc_url( 'mailto:' . $site_email ); ?>"><?php echo esc_html( $site_email ); ?></a>
							<p class="site-footer__contact-meta"><?php esc_html_e( 'почта для заявок', 'shpigovsky' ); ?></p>
						</div>
					</div>
				<?php endif; ?>
			</div>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — услуги', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'Услуги', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'footer_services',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_footer_services_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — о центре', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'О центре', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'footer_o_centre',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_footer_o_centre_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — информация', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'Информация', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'legal',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_legal_nav_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
		</div>
		<div class="site-footer__legal">
			<p class="site-footer__copyright">&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php esc_html_e( 'Все права защищены.', 'shpigovsky' ); ?></p>
		</div>
	</div>
</footer>
