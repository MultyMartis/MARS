<?php
/**
 * Template part: reviews/archive-list.php
 *
 * Static V9 reviews archive list — V9-06D9-W / V9-06E62B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_reviews_enabled() ) {
	return;
}

$items = shpigovsky_get_reviews_items(
	array(
		'featured_only' => false,
		'limit'         => 0,
	)
);

if ( empty( $items ) ) {
	return;
}

$pagination = shpigovsky_paginate_reviews_items( $items );
$items      = $pagination['items'];

?>
<section class="reviews-archive" aria-labelledby="reviews-archive-heading">
  <div class="container reviews-archive__container">
    <h1 class="reviews-archive__heading" id="reviews-archive-heading">Отзывы о&nbsp;центре лечения и&nbsp;профилактики зависимостей</h1>

    <p class="reviews-archive__intro block-whith-red-line">
      В&nbsp;виду важности сохранения конфиденциальности и&nbsp;анонимности наших клиентов мы&nbsp;не&nbsp;собираем отзывы на&nbsp;сторонних площадках, где возможна идентификация пользователя.
    </p>

    <div class="reviews-archive__list" data-reveal-group>
	<?php foreach ( $items as $item ) : ?>
		<?php
		get_template_part(
			'template-parts/components/review-archive-card',
			null,
			array(
				'author'       => $item['author'] ?? '',
				'text'         => $item['text'] ?? '',
				'context'      => $item['context'] ?? '',
				'source'       => $item['source'] ?? '',
				'date'         => $item['date'] ?? '',
				'rating'       => $item['rating'] ?? 5,
				'service_href' => $item['service_href'] ?? '',
				'review_id'    => $item['review_id'] ?? 0,
				'review_uid'   => $item['review_uid'] ?? '',
			)
		);
		?>
	<?php endforeach; ?>
    </div>
	<?php if ( $pagination['total'] > 1 ) : ?>
		<?php
		$links = paginate_links(
			array(
				'total'     => (int) $pagination['total'],
				'current'   => (int) $pagination['current'],
				'type'      => 'array',
				'prev_next' => false,
				'end_size'  => 1,
				'mid_size'  => 2,
			)
		);
		?>
		<?php if ( is_array( $links ) && ! empty( $links ) ) : ?>
			<nav class="reviews-archive-pagination" aria-label="<?php esc_attr_e( 'Пагинация отзывов', 'shpigovsky' ); ?>">
				<ol class="reviews-archive-pagination__list">
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
						<li class="reviews-archive-pagination__item<?php echo $is_dots ? ' reviews-archive-pagination__item--ellipsis' : ''; ?>"<?php echo $is_dots ? ' aria-hidden="true"' : ''; ?>>
							<?php if ( $is_dots ) : ?>
								<span class="reviews-archive-pagination__ellipsis">...</span>
							<?php elseif ( $is_current ) : ?>
								<span class="reviews-archive-pagination__link reviews-archive-pagination__link--active" aria-current="page"><?php echo esc_html( $label ); ?></span>
							<?php else : ?>
								<a class="reviews-archive-pagination__link" href="<?php echo esc_url( $href ); ?>"><?php echo esc_html( $label ); ?></a>
							<?php endif; ?>
						</li>
					<?php endforeach; ?>
				</ol>
			</nav>
		<?php endif; ?>
	<?php endif; ?>
  </div>
</section>
