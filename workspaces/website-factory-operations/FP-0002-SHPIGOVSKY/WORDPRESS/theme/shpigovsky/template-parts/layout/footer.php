<?php
/**
 * Site footer — static V9 visual authority (D9-D).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url            = shpigovsky_get_footer_logo_url();
$brand_label         = shpigovsky_brand_label();
$phone_primary       = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary     = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href  = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$site_email          = sanitize_email( shpigovsky_get_site_option( 'site_email' ) );
$address_lines       = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'site_address' ) );
$schedule_lines      = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'opening_hours' ) );

// D9-D static V9 fallbacks when options empty.
if ( '' === $phone_primary ) {
	$phone_primary      = '8 (925) 183-64-64';
	$phone_primary_href = 'tel:+79251836464';
}
if ( '' === $phone_secondary ) {
	$phone_secondary      = '8 (995) 023-92-26';
	$phone_secondary_href = 'tel:+79950239226';
}
if ( '' === $site_email || ! is_email( $site_email ) ) {
	$site_email = 'Info@shpigovsky.ru';
}
if ( empty( $address_lines ) ) {
	$address_lines = array( 'Москва и Московская область' );
}
if ( empty( $schedule_lines ) ) {
	$schedule_lines = array( 'пн-пт 09:00-19:00,', 'сб-вс 09:00-20:00' );
}

$callback_label    = shpigovsky_get_footer_callback_label();
$appointment_label = shpigovsky_get_footer_appointment_label();
$footer_credit_url = shpigovsky_get_footer_credit_url();
$footer_credit_text = shpigovsky_get_footer_credit_text();
$footer_copyright_suffix = shpigovsky_get_footer_copyright_suffix();
?>
<footer class="site-footer" data-reveal role="contentinfo">
	<div class="container">
		<div class="site-footer__top">
			<a class="site-footer__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="site-footer__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>
			<?php get_template_part( 'template-parts/navigation/footer-social' ); ?>
			<div class="site-footer__phones">
				<a class="site-footer__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
				<a class="site-footer__phone site-footer__phone--secondary" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
			</div>
			<div class="site-footer__actions">
				<button type="button" class="btn" data-modal-open="consultation" data-modal-source="footer-callback" data-modal-title="<?php echo esc_attr( $callback_label ); ?>" data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"><?php echo esc_html( $callback_label ); ?></button>
				<button type="button" class="btn btn_dark btn--primary" data-modal-open="consultation" data-modal-source="footer-appointment" data-modal-title="<?php echo esc_attr( $appointment_label ); ?>" data-modal-submit-text="<?php echo esc_attr( $appointment_label ); ?>"><?php echo esc_html( $appointment_label ); ?></button>
			</div>
		</div>
		<div class="site-footer__main">
			<div class="site-footer__contacts">
				<div class="site-footer__contact-item">
					<span class="site-footer__contact-icon" aria-hidden="true"><i class="fas fa-map-marker-alt"></i></span>
					<div class="site-footer__contact-body">
						<?php foreach ( $address_lines as $line ) : ?>
							<p class="site-footer__contact-label"><?php echo esc_html( $line ); ?></p>
						<?php endforeach; ?>
						<p class="site-footer__contact-meta">
							<em><?php esc_html_e( 'Режим работы:', 'shpigovsky' ); ?></em>
							<?php foreach ( $schedule_lines as $line ) : ?>
								<em><?php echo esc_html( $line ); ?></em>
							<?php endforeach; ?>
						</p>
					</div>
				</div>
				<div class="site-footer__contact-item">
					<span class="site-footer__contact-icon" aria-hidden="true"><i class="fas fa-envelope"></i></span>
					<div class="site-footer__contact-body">
						<a class="site-footer__contact-label" href="<?php echo esc_url( 'mailto:' . $site_email ); ?>"><?php echo esc_html( $site_email ); ?></a>
						<p class="site-footer__contact-meta"><?php esc_html_e( 'почта для заявок', 'shpigovsky' ); ?></p>
					</div>
				</div>
				<div class="site-footer__copyr-privacy">
					<p class="site-footer__privacy">
						<?php
						printf(
							wp_kses_post( __( 'По вопросам, связанным с обработкой ваших персональных данных, обращайтесь на <a href="mailto:%1$s">%2$s</a>', 'shpigovsky' ) ),
							esc_attr( strtolower( $site_email ) ),
							esc_html( $site_email )
						);
						?>
					</p>
				</div>
			</div>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — услуги', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading">
					<a class="site-footer__nav-heading-link" href="<?php echo esc_url( home_url( '/uslugi/' ) ); ?>"><?php esc_html_e( 'Услуги', 'shpigovsky' ); ?></a>
				</h2>
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
				<h2 class="site-footer__nav-heading">
					<a class="site-footer__nav-heading-link" href="<?php echo esc_url( home_url( '/o-centre/' ) ); ?>"><?php esc_html_e( 'О центре', 'shpigovsky' ); ?></a>
				</h2>
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
			<p class="site-footer__copyright">&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php echo esc_html( $footer_copyright_suffix ); ?></p>
			<p class="site-footer__credit">
				<?php if ( '' !== $footer_credit_url ) : ?>
					<a
						href="<?php echo esc_url( $footer_credit_url ); ?>"
						target="_blank"
						rel="noopener noreferrer"
					><?php echo esc_html( $footer_credit_text ); ?></a>
				<?php else : ?>
					<?php echo esc_html( $footer_credit_text ); ?>
				<?php endif; ?>
			</p>
		</div>
	</div>
</footer>
<?php get_template_part( 'template-parts/components/scroll-to-top' ); ?>
