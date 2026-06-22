<?php
/**
 * Theme header.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="site-header">
	<div class="container site-header__inner">
		<a class="site-header__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
			<?php echo esc_html( get_bloginfo( 'name' ) ); ?>
		</a>
		<button class="site-header__toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">
			<?php esc_html_e( 'Меню', 'fws-synthetic' ); ?>
		</button>
		<nav class="site-header__nav" id="site-nav" data-nav aria-label="<?php esc_attr_e( 'Главная навигация', 'fws-synthetic' ); ?>">
			<?php if ( has_nav_menu( 'primary' ) ) : ?>
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'primary',
						'container'      => false,
						'menu_class'     => 'site-header__menu',
						'fallback_cb'    => false,
						'depth'          => 1,
					)
				);
				?>
			<?php else : ?>
				<ul class="site-header__menu">
					<li><a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Главная', 'fws-synthetic' ); ?></a></li>
					<li><a href="<?php echo esc_url( fws_get_services_url() ); ?>"><?php esc_html_e( 'Услуги', 'fws-synthetic' ); ?></a></li>
					<li><a href="<?php echo esc_url( fws_get_contacts_url() ); ?>"><?php esc_html_e( 'Контакты', 'fws-synthetic' ); ?></a></li>
				</ul>
			<?php endif; ?>
			<a class="btn btn--primary site-header__cta" href="<?php echo esc_url( fws_get_contacts_url() ); ?>">
				<?php esc_html_e( 'Связаться', 'fws-synthetic' ); ?>
			</a>
		</nav>
	</div>
</header>
<main class="main" id="main">
