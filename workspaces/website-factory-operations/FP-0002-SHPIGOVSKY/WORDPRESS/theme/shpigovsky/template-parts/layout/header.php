<?php
/**
 * Site header region — navigation integration boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<header class="shpigovsky-skeleton-header" role="banner">
	<div class="shpigovsky-skeleton-header__inner">
		<a class="shpigovsky-skeleton-header__brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">
			<?php bloginfo( 'name' ); ?>
		</a>
		<?php get_template_part( 'template-parts/navigation/primary-desktop' ); ?>
		<?php get_template_part( 'template-parts/navigation/primary-mobile' ); ?>
	</div>
</header>
