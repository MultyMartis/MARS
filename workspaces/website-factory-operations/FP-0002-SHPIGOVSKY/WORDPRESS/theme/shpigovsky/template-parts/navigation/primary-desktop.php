<?php
/**
 * Primary desktop navigation — `primary` menu location.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<nav class="shpigovsky-skeleton-nav shpigovsky-skeleton-nav--desktop" aria-label="<?php esc_attr_e( 'Главное меню', 'shpigovsky' ); ?>">
	<?php
	wp_nav_menu(
		array(
			'theme_location' => 'primary',
			'container'      => false,
			'fallback_cb'    => false,
		)
	);
	?>
</nav>
