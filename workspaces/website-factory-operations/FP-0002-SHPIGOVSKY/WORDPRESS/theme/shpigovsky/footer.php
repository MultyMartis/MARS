<?php
/**
 * Footer — minimal foundation markup.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<footer class="shpigovsky-foundation-footer" role="contentinfo">
	<div class="shpigovsky-foundation-footer__inner">
		<?php
		wp_nav_menu(
			array(
				'theme_location' => 'footer',
				'container'      => 'nav',
				'container_class'  => 'shpigovsky-foundation-footer-nav',
				'fallback_cb'    => false,
			)
		);
		wp_nav_menu(
			array(
				'theme_location' => 'legal',
				'container'      => 'nav',
				'container_class'  => 'shpigovsky-foundation-legal-nav',
				'fallback_cb'    => false,
			)
		);
		?>
		<p class="shpigovsky-foundation-footer__note"><?php esc_html_e( 'Local development foundation — not production.', 'shpigovsky' ); ?></p>
	</div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
