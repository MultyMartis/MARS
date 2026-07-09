<?php
/**
 * Blog archive pagination — V9-06E26B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

global $wp_query;

$total_pages = (int) $wp_query->max_num_pages;

if ( $total_pages <= 1 ) {
	return;
}

$current = max( 1, (int) get_query_var( 'paged', 1 ) );
$links   = paginate_links(
	array(
		'total'     => $total_pages,
		'current'   => $current,
		'type'      => 'array',
		'prev_next' => false,
		'end_size'  => 1,
		'mid_size'  => 2,
	)
);

if ( empty( $links ) || ! is_array( $links ) ) {
	return;
}
?>
<nav class="blog-archive-pagination" aria-label="<?php esc_attr_e( 'Пагинация статей', 'shpigovsky' ); ?>">
	<ol class="blog-archive-pagination__list">
		<?php foreach ( $links as $link ) : ?>
			<?php
			$is_current = false !== strpos( $link, 'current' );
			$is_dots    = false !== strpos( $link, 'dots' );
			$label      = wp_strip_all_tags( $link );
			$href       = '';

			if ( preg_match( '/href=["\']([^"\']+)["\']/', $link, $matches ) ) {
				$href = $matches[1];
			}
			?>
			<li class="blog-archive-pagination__item<?php echo $is_dots ? ' blog-archive-pagination__item--ellipsis' : ''; ?>"<?php echo $is_dots ? ' aria-hidden="true"' : ''; ?>>
				<?php if ( $is_dots ) : ?>
					<span class="blog-archive-pagination__ellipsis">...</span>
				<?php elseif ( $is_current ) : ?>
					<span class="blog-archive-pagination__link blog-archive-pagination__link--active" aria-current="page"><?php echo esc_html( $label ); ?></span>
				<?php else : ?>
					<a class="blog-archive-pagination__link" href="<?php echo esc_url( $href ); ?>"><?php echo esc_html( $label ); ?></a>
				<?php endif; ?>
			</li>
		<?php endforeach; ?>
	</ol>
</nav>
