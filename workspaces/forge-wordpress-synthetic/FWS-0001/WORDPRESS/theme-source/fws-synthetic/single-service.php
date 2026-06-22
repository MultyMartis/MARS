<?php
/**
 * Single service template.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

while ( have_posts() ) :
	the_post();
	?>
<article <?php post_class( 'service-single' ); ?>>
	<div class="container">
		<nav class="breadcrumb" aria-label="<?php esc_attr_e( 'Хлебные крошки', 'fws-synthetic' ); ?>">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Главная', 'fws-synthetic' ); ?></a>
			<span aria-hidden="true">/</span>
			<a href="<?php echo esc_url( fws_get_services_url() ); ?>"><?php esc_html_e( 'Услуги', 'fws-synthetic' ); ?></a>
			<span aria-hidden="true">/</span>
			<span><?php the_title(); ?></span>
		</nav>
		<h1 class="service-single__title"><?php the_title(); ?></h1>
		<?php
		$excerpt = fws_get_service_excerpt( get_the_ID() );
		if ( $excerpt ) :
			?>
		<p class="service-single__excerpt"><?php echo esc_html( $excerpt ); ?></p>
		<?php endif; ?>
		<div class="service-single__content">
			<?php the_content(); ?>
		</div>
		<a class="btn btn--primary" href="<?php echo esc_url( fws_get_contacts_url() ); ?>">
			<?php esc_html_e( 'Заказать консультацию', 'fws-synthetic' ); ?>
		</a>
	</div>
</article>
	<?php
endwhile;

get_footer();
