<?php
/**
 * Template Name: Contacts
 * Route family: /kontakty/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--contacts" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class(); ?>>
			<h1><?php the_title(); ?></h1>
		</article>
		<?php
	endwhile;
	get_template_part( 'template-parts/contacts/map-body' );
	get_template_part( 'template-parts/contacts/rehabilitation-steps' );
	?>
</main>
<?php
get_footer();
