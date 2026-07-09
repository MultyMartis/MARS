<?php
/**
 * Blog archive empty state — V9-06E26B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$title = shpigovsky_get_blog_archive_empty_title();
$text  = shpigovsky_get_blog_archive_empty_text();
?>
<div class="blog-archive__empty-state" data-blog-archive-empty>
	<?php if ( '' !== $title ) : ?>
		<h2 class="blog-archive__empty-title"><?php echo esc_html( $title ); ?></h2>
	<?php endif; ?>
	<?php if ( '' !== $text ) : ?>
		<p class="blog-archive__empty-text"><?php echo esc_html( $text ); ?></p>
	<?php endif; ?>
</div>
