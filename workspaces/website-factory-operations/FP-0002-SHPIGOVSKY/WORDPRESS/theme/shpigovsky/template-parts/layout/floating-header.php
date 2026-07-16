<?php
/**
 * Floating utility header — appears on scroll (V9-06E54).
 *
 * Separate from the primary site header; fixed 90px panel.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url           = shpigovsky_get_header_logo_url();
$brand_label        = shpigovsky_brand_label();
$phone_primary      = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary    = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$callback_label     = shpigovsky_get_header_callback_label();
?>
<header
	class="fp02-floating-header"
	data-fp02-floating-header
	role="banner"
	aria-label="<?php esc_attr_e( 'Быстрый доступ', 'shpigovsky' ); ?>"
	aria-hidden="true"
>
	<div class="container fp02-floating-header__inner">
		<a class="fp02-floating-header__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
			<img
				class="fp02-floating-header__logo-image"
				src="<?php echo esc_url( $logo_url ); ?>"
				alt="<?php echo esc_attr( $brand_label ); ?>"
			>
		</a>

		<div class="fp02-floating-header__contacts">

			<div class="fp02-floating-header__contacts__wrapper">
			<?php if ( '' !== $phone_primary && '' !== $phone_primary_href ) : ?>
				<a
					class="fp02-floating-header__phone fp02-floating-header__phone--primary"
					href="<?php echo esc_url( $phone_primary_href ); ?>"
				><?php echo esc_html( $phone_primary ); ?></a>
			<?php endif; ?>

			<?php if ( '' !== $phone_secondary && '' !== $phone_secondary_href ) : ?>
				<a
					class="fp02-floating-header__phone fp02-floating-header__phone--secondary"
					href="<?php echo esc_url( $phone_secondary_href ); ?>"
				><?php echo esc_html( $phone_secondary ); ?></a>
			<?php endif; ?>
			</div>

			<div class="fp02-floating-header__messengers">
				<?php get_template_part( 'template-parts/navigation/messenger-links', null, array( 'context' => 'header' ) ); ?>
			</div>

			<button
				type="button"
				class="btn fp02-floating-header__callback"
				data-modal-open="consultation"
				data-modal-source="floating-header"
				data-modal-title="<?php echo esc_attr( $callback_label ); ?>"
				data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"
			><?php echo esc_html( $callback_label ); ?></button>
		</div>

		<button
			type="button"
			class="fp02-floating-header__menu-button site-header__menu-toggle"
			data-offcanvas-open
			aria-controls="mobile-menu"
			aria-expanded="false"
			aria-label="<?php esc_attr_e( 'Меню', 'shpigovsky' ); ?>"
		>
			<span class="site-header__menu-toggle-icon fp02-floating-header__menu-icon" aria-hidden="true">
				<i class="fas fa-bars"></i>
			</span>
			<span class="fp02-floating-header__menu-label"><?php esc_html_e( 'Меню', 'shpigovsky' ); ?></span>
		</button>
	</div>
</header>
