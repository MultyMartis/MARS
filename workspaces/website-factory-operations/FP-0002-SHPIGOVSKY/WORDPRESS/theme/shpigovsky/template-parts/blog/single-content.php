<?php
/**
 * Blog single body typography — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$content = get_the_content();

if ( '' === trim( wp_strip_all_tags( $content ) ) ) {
	return;
}
?>
<section class="blog-article-body">
	<div class="blog-article-body__content entry-content">
		<?php the_content(); ?>
	</div>
</section>
