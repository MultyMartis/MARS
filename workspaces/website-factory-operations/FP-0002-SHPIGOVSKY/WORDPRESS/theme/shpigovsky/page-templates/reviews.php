<?php
/**
 * Template Name: Reviews
 * Route family: /otzyvy/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-otzyvy__main" id="main-content">
	<?php if ( shpigovsky_breadcrumbs_enabled_for_context() ) : ?>
		<div class="reviews-page__breadcrumbs">
			<div class="container">
				<?php shpigovsky_render_breadcrumbs(); ?>
			</div>
		</div>
	<?php endif; ?>
	<?php
	get_template_part( 'template-parts/reviews/archive-list' );
	get_template_part( 'template-parts/reviews/rehabilitation-requirements' );
	?>
</main>
<?php
get_footer();
