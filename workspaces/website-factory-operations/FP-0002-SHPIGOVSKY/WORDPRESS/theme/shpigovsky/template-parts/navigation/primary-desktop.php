<?php
/**
 * Primary desktop navigation — `primary` menu location with V9 classes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$search_button = sprintf(
	'<li class="site-header__nav-item site-header__nav-item--search"><button type="button" class="site-header__search" data-search-toggle aria-expanded="false" aria-controls="site-header-search" aria-label="%1$s"><i class="fas fa-search" aria-hidden="true"></i></button></li>',
	esc_attr__( 'Открыть поиск', 'shpigovsky' )
);
?>
<nav class="site-header__nav" aria-label="<?php esc_attr_e( 'Основная навигация', 'shpigovsky' ); ?>">
	<?php
	wp_nav_menu(
		array(
			'theme_location'        => 'primary',
			'container'             => false,
			'menu_class'            => 'site-header__nav-list',
			'fallback_cb'           => 'shpigovsky_primary_nav_fallback',
			'shpigovsky_item_class' => 'site-header__nav-item',
			'shpigovsky_link_class' => 'site-header__nav-link',
			'depth'                 => 1,
			'items_wrap'            => '<ul class="%2$s">%3$s' . $search_button . '</ul>',
		)
	);
	?>
</nav>
