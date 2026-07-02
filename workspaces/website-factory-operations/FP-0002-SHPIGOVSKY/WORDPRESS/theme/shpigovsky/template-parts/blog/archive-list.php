<?php
/**
 * Blog archive list — entity query boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<div class="shpigovsky-skeleton__blog-archive">
	<?php if ( have_posts() ) : ?>
		<?php
		while ( have_posts() ) :
			the_post();
			get_template_part( 'template-parts/components/blog-archive-card' );
		endwhile;
		?>
	<?php else : ?>
		<p><?php esc_html_e( 'Записей пока нет.', 'shpigovsky' ); ?></p>
	<?php endif; ?>
</div>
