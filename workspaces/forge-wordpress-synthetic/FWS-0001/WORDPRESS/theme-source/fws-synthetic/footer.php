<?php
/**
 * Theme footer.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
</main>
<footer class="site-footer">
	<div class="container site-footer__inner">
		<div class="site-footer__brand">
			<strong><?php echo esc_html( get_bloginfo( 'name' ) ); ?></strong>
			<p><?php echo esc_html( get_bloginfo( 'description' ) ); ?></p>
		</div>
		<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Нижнее меню', 'fws-synthetic' ); ?>">
			<?php if ( has_nav_menu( 'footer' ) ) : ?>
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'footer',
						'container'      => false,
						'items_wrap'     => '%3$s',
						'fallback_cb'    => false,
						'depth'          => 1,
					)
				);
				?>
			<?php else : ?>
				<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Главная', 'fws-synthetic' ); ?></a>
				<a href="<?php echo esc_url( fws_get_services_url() ); ?>"><?php esc_html_e( 'Услуги', 'fws-synthetic' ); ?></a>
				<a href="<?php echo esc_url( fws_get_contacts_url() ); ?>"><?php esc_html_e( 'Контакты', 'fws-synthetic' ); ?></a>
			<?php endif; ?>
		</nav>
		<p class="site-footer__copy">
			&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?>
			<?php echo esc_html( get_bloginfo( 'name' ) ); ?>.
			<?php esc_html_e( 'Все права защищены.', 'fws-synthetic' ); ?>
		</p>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
