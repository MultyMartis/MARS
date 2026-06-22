<?php
/**
 * Template Name: Contacts
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
<section class="page-intro">
	<div class="container">
		<h1 class="page-intro__title"><?php the_title(); ?></h1>
		<?php if ( has_excerpt() ) : ?>
		<p class="page-intro__lead"><?php echo esc_html( get_the_excerpt() ); ?></p>
		<?php else : ?>
		<p class="page-intro__lead">
			<?php esc_html_e( 'Синтетические контактные данные для локальной валидации.', 'fws-synthetic' ); ?>
		</p>
		<?php endif; ?>
	</div>
</section>
	<?php get_template_part( 'template-parts/contact-block' ); ?>
	<?php
	get_template_part(
		'template-parts/faq',
		null,
		array(
			'faq_id'  => 'contacts-faq',
			'post_id' => get_the_ID(),
		)
	);
endwhile;

get_footer();
