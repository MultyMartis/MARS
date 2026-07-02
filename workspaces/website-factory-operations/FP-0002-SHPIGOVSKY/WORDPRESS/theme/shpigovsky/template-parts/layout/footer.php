<?php
/**
 * Site footer region — footer menu columns.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<footer class="shpigovsky-skeleton-footer" role="contentinfo">
	<div class="shpigovsky-skeleton-footer__inner">
		<nav class="shpigovsky-skeleton-footer__nav shpigovsky-skeleton-footer__nav--services" aria-label="<?php esc_attr_e( 'Услуги', 'shpigovsky' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'footer_services',
					'container'      => false,
					'fallback_cb'    => false,
				)
			);
			?>
		</nav>
		<nav class="shpigovsky-skeleton-footer__nav shpigovsky-skeleton-footer__nav--o-centre" aria-label="<?php esc_attr_e( 'О центре', 'shpigovsky' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'footer_o_centre',
					'container'      => false,
					'fallback_cb'    => false,
				)
			);
			?>
		</nav>
		<nav class="shpigovsky-skeleton-footer__nav shpigovsky-skeleton-footer__nav--legal" aria-label="<?php esc_attr_e( 'Правовая информация', 'shpigovsky' ); ?>">
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'legal',
					'container'      => false,
					'fallback_cb'    => false,
				)
			);
			?>
		</nav>
		<p class="shpigovsky-skeleton-footer__note"><?php esc_html_e( 'V9-06B skeleton — not production markup.', 'shpigovsky' ); ?></p>
	</div>
</footer>
