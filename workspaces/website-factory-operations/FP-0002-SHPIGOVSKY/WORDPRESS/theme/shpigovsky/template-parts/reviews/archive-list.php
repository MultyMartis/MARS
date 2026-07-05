<?php
/**
 * Template part: reviews/archive-list.php
 *
 * Static V9 reviews archive list — V9-06D9-W.
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
				'service_href' => '',
			)
		);
		?>
	<?php endforeach; ?>
    </div>
  </div>
</section>
