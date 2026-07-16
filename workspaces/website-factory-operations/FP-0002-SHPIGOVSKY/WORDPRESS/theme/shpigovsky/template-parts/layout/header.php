<?php
/**
 * Site header — V9 global chrome.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url      = shpigovsky_get_header_logo_url();
$brand_label   = shpigovsky_brand_label();
$phone_primary = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$address_lines = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'site_address' ) );
$schedule_lines = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'opening_hours' ) );
$callback_label = shpigovsky_get_header_callback_label();

if ( is_front_page() ) {
	echo '<div class="intro-section">' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
}
?>
<header class="site-header" role="banner">
	<div class="container">
		<div class="site-header__mobile-bar">

			<a class="site-header__logo site-header__logo--mobile" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="site-header__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>

			<div class="site-header__mobile-bar--actions">

				<div class="site-header__mobile-bar--actions--wrapper">
					<?php if ( '' !== $phone_primary && '' !== $phone_primary_href ) : ?>
						<a class="site-header__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
					<?php endif; ?>
					<?php if ( '' !== $phone_secondary && '' !== $phone_secondary_href ) : ?>
						<a class="site-header__phone" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
					<?php endif; ?>
				</div>

				<?php get_template_part( 'template-parts/navigation/messenger-links', null, array( 'context' => 'mobile-header' ) ); ?>

				<button
					type="button"
					class="btn mobile-header__btn"
					data-modal-open="consultation"
					data-modal-source="header"
					data-modal-title="<?php echo esc_attr( $callback_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"
				><?php echo esc_html( $callback_label ); ?></button>

				<button
					type="button"
					class="site-header__menu-toggle"
					data-offcanvas-open
					aria-controls="mobile-menu"
					aria-expanded="false"
					aria-label="<?php esc_attr_e( 'Открыть меню', 'shpigovsky' ); ?>"
				>
					<span class="site-header__menu-toggle-icon" aria-hidden="true">
						<i class="fas fa-bars"></i>
					</span>
				</button>

			</div>

		</div>

		<div class="site-header__top">
			<a class="site-header__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="site-header__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>
			<?php if ( ! empty( $address_lines ) ) : ?>
				<address class="site-header__address">
					<?php foreach ( $address_lines as $line ) : ?>
						<span class="site-header__address-line"><?php echo esc_html( $line ); ?></span>
					<?php endforeach; ?>
				</address>
			<?php endif; ?>
			<?php if ( ! empty( $schedule_lines ) ) : ?>
				<div class="site-header__schedule">
					<?php foreach ( $schedule_lines as $line ) : ?>
						<span class="site-header__schedule-line"><?php echo esc_html( $line ); ?></span>
					<?php endforeach; ?>
				</div>
			<?php endif; ?>
			<?php if ( '' !== $phone_primary || '' !== $phone_secondary ) : ?>
				<div class="site-header__phones">
					<?php if ( '' !== $phone_primary && '' !== $phone_primary_href ) : ?>
						<a class="site-header__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
					<?php endif; ?>
					<?php if ( '' !== $phone_secondary && '' !== $phone_secondary_href ) : ?>
						<a class="site-header__phone" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
					<?php endif; ?>
				</div>
			<?php endif; ?>
			<div class="site-header__btns-wrap">
				<?php get_template_part( 'template-parts/navigation/messenger-links', null, array( 'context' => 'header' ) ); ?>
				<button
					type="button"
					class="btn"
					data-modal-open="consultation"
					data-modal-source="header"
					data-modal-title="<?php echo esc_attr( $callback_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"
				><?php echo esc_html( $callback_label ); ?></button>
			</div>
		</div>

		<div class="site-header__bottom">
			<?php get_template_part( 'template-parts/navigation/primary-desktop' ); ?>
		</div>
	</div>

	<?php get_template_part( 'template-parts/navigation/offcanvas' ); ?>
</header>
