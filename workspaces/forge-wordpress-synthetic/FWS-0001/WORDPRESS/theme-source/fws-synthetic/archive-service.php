<?php
/**
 * Service post type archive.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<section class="page-intro">
	<div class="container">
		<h1 class="page-intro__title"><?php post_type_archive_title(); ?></h1>
		<p class="page-intro__lead">
			<?php esc_html_e( 'Синтетический архив для проверки partial mapping и CPT service.', 'fws-synthetic' ); ?>
		</p>
	</div>
</section>
<?php get_template_part( 'template-parts/services-grid' ); ?>
<?php get_template_part( 'template-parts/cta-global' ); ?>
<?php
get_footer();
