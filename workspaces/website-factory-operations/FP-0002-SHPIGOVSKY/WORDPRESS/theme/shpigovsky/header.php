<?php
/**
 * Header — minimal foundation markup.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="shpigovsky-foundation-header" role="banner">
	<div class="shpigovsky-foundation-header__inner">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php bloginfo( 'name' ); ?></a>
		<?php
		wp_nav_menu(
			array(
				'theme_location' => 'primary',
				'container'      => 'nav',
				'container_class'  => 'shpigovsky-foundation-nav',
				'fallback_cb'    => false,
			)
		);
		?>
	</div>
</header>
