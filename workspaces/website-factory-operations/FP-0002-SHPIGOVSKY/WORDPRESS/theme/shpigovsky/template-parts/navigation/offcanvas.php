<?php
/**
 * Mobile offcanvas navigation panel.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url        = shpigovsky_asset_uri( 'img/branding/logo.svg' );
$brand_label     = shpigovsky_brand_label();
$phone_primary   = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href   = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$callback_label  = shpigovsky_get_site_option( 'default_button_label' );
$callback_label  = '' !== $callback_label ? $callback_label : __( 'Заказать звонок', 'shpigovsky' );
?>
<div
	class="offcanvas"
	id="mobile-menu"
	data-offcanvas
	data-offcanvas-state="closed"
	aria-hidden="true"
>
	<div class="offcanvas__overlay" data-offcanvas-overlay></div>
	<div
		class="offcanvas__panel"
		data-offcanvas-panel
		role="dialog"
		aria-modal="true"
		aria-label="<?php esc_attr_e( 'Мобильное меню', 'shpigovsky' ); ?>"
	>
		<div class="offcanvas__header">
			<a class="offcanvas__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="offcanvas__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>
			<button
				type="button"
				class="offcanvas__close"
				data-offcanvas-close
				aria-label="<?php esc_attr_e( 'Закрыть меню', 'shpigovsky' ); ?>"
			>
				<span class="offcanvas__close-icon" aria-hidden="true">
					<i class="fas fa-times"></i>
				</span>
			</button>
		</div>
		<nav class="offcanvas__nav" aria-label="<?php esc_attr_e( 'Мобильная навигация', 'shpigovsky' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location'        => 'primary',
					'container'             => false,
					'menu_class'            => 'offcanvas__nav-list',
					'fallback_cb'           => 'shpigovsky_offcanvas_nav_fallback',
					'shpigovsky_item_class' => 'offcanvas__nav-item',
					'shpigovsky_link_class' => 'offcanvas__nav-link',
					'depth'                 => 1,
				)
			);
			?>
			<ul class="offcanvas__nav-list offcanvas__nav-list--actions">
				<li class="offcanvas__nav-item">
					<a
						class="offcanvas__nav-link offcanvas__nav-link--search"
						href="<?php echo esc_url( home_url( '/?s=' ) ); ?>"
					>
						<i class="fas fa-search" aria-hidden="true"></i>
						<span><?php esc_html_e( 'Поиск', 'shpigovsky' ); ?></span>
					</a>
				</li>
			</ul>
		</nav>
		<div class="offcanvas__contacts">
			<?php if ( '' !== $phone_primary || '' !== $phone_secondary ) : ?>
				<div class="offcanvas__phones">
					<?php if ( '' !== $phone_primary && '' !== $phone_primary_href ) : ?>
						<a class="offcanvas__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
					<?php endif; ?>
					<?php if ( '' !== $phone_secondary && '' !== $phone_secondary_href ) : ?>
						<a class="offcanvas__phone" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
					<?php endif; ?>
				</div>
			<?php endif; ?>
			<?php get_template_part( 'template-parts/navigation/messenger-links', null, array( 'context' => 'offcanvas' ) ); ?>
			<button
				type="button"
				class="btn offcanvas__cta"
				data-modal-open="consultation"
				data-modal-source="mobile-header"
				data-modal-title="<?php echo esc_attr( $callback_label ); ?>"
				data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"
			><?php echo esc_html( $callback_label ); ?></button>
		</div>
	</div>
</div>
