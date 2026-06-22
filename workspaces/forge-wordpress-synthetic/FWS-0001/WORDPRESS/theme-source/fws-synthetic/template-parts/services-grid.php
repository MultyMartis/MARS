<?php
/**
 * Services grid (archive loop).
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<section class="services-archive">
	<div class="container">
		<div class="services-grid">
			<?php if ( have_posts() ) : ?>
				<?php
				while ( have_posts() ) :
					the_post();
					get_template_part(
						'template-parts/service-card',
						null,
						array(
							'title' => get_the_title(),
							'text'  => fws_get_service_excerpt( get_the_ID() ),
							'url'   => get_permalink(),
						)
					);
				endwhile;
				?>
			<?php else : ?>
				<p><?php esc_html_e( 'Услуги пока не добавлены.', 'fws-synthetic' ); ?></p>
			<?php endif; ?>
		</div>
		<?php the_posts_pagination(); ?>
	</div>
</section>
