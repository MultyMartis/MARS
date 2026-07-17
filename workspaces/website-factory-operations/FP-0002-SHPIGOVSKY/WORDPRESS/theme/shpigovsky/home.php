<?php
/**
 * Blog archive — posts page at /blog/.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-blog__main" id="main-content">
	<?php if ( shpigovsky_breadcrumbs_enabled_for_context() ) : ?>
		<div class="blog-page__breadcrumbs">
			<div class="container">
				<?php
				set_query_var( 'shpigovsky_breadcrumb_trail', shpigovsky_get_blog_breadcrumb_trail() );
				shpigovsky_render_breadcrumbs();
				?>
			</div>
		</div>
	<?php endif; ?>
	<?php
	get_template_part( 'template-parts/blog/archive-list' );
	get_template_part( 'template-parts/blog/lower-stack' );
	?>
</main>
<?php
get_footer();
