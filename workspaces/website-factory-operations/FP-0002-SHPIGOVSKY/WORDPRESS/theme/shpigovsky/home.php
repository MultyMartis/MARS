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
<main class="shpigovsky-skeleton shpigovsky-skeleton--blog-archive" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<header class="shpigovsky-skeleton__page-header">
		<h1><?php esc_html_e( 'Блог', 'shpigovsky' ); ?></h1>
	</header>
	<?php get_template_part( 'template-parts/blog/archive-list' ); ?>
</main>
<?php
get_footer();
