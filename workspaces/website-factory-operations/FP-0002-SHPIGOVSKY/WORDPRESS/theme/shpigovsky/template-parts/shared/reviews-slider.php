<?php
/**
 * Template part: shared/reviews-slider.php
 *
 * Shared reviews slider — V9-06D9-R Hybrid E / V9-06E62B full-review links.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args = wp_parse_args(
	$args ?? array(),
		array(
		'context'       => 'home',
		'limit'         => 0,
		'featured_only' => false,
		'section_class' => 'reviews',
		'section_id'    => '',
		'show_heading'  => true,
		'show_all_link' => true,
	)
);

if ( ! shpigovsky_reviews_enabled() ) {
	return;
}

$query_args = array(
	'featured_only' => (bool) $args['featured_only'],
	'limit'         => (int) $args['limit'],
);

if ( 'home' === $args['context'] ) {
	if ( 0 === $query_args['limit'] ) {
		$query_args['limit'] = 10;
	}
	$query_args['featured_only'] = true;
}

$items = shpigovsky_get_reviews_items( $query_args );

if ( empty( $items ) ) {
	return;
}

$section_class = trim( (string) $args['section_class'] );
$section_id    = trim( (string) $args['section_id'] );
$heading       = shpigovsky_get_reviews_heading( 'Отзывы' );
$aria_label    = wp_strip_all_tags( $heading );

?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>"<?php echo '' !== $section_id ? ' id="' . esc_attr( $section_id ) . '"' : ''; ?> aria-label="<?php echo esc_attr( $aria_label ); ?>">
  <div class="container">
	<?php if ( ! empty( $args['show_heading'] ) ) : ?>
    <div class="reviews__heading">
      <h2 class="reviews__title"><?php echo esc_html( $heading ); ?></h2>
	  <?php if ( ! empty( $args['show_all_link'] ) ) : ?>
      <a class="reviews__all-link" href="<?php echo esc_url( home_url( '/otzyvy/' ) ); ?>">
        <span class="reviews__all-text">Смотреть отзывы</span>
        <span class="reviews__all-icon" aria-hidden="true"><i class="fas fa-caret-right"></i></span>
      </a>
	  <?php endif; ?>
    </div>
	<?php endif; ?>

    <div class="reviews__slider swiper" data-reviews-slider>
      <div class="reviews__wrapper swiper-wrapper">
		<?php foreach ( $items as $item ) : ?>
			<?php
			$rating     = shpigovsky_normalize_review_rating( $item['rating'] ?? 5 );
			$review_uid = isset( $item['review_uid'] ) ? (string) $item['review_uid'] : '';
			if ( function_exists( 'shpigovsky_sanitize_review_uid' ) ) {
				$review_uid = shpigovsky_sanitize_review_uid( $review_uid );
			}
			$full_url = '' !== $review_uid && function_exists( 'shpigovsky_get_review_archive_url' )
				? shpigovsky_get_review_archive_url( $review_uid )
				: home_url( '/otzyvy/' );
			?>
        <article class="reviews__slide swiper-slide" data-review-slider-card<?php echo '' !== $review_uid ? ' data-review-uid="' . esc_attr( $review_uid ) . '"' : ''; ?>>
          <div class="reviews__card">
            <ul class="reviews__rating" aria-label="<?php echo esc_attr( sprintf( 'Оценка %d из 5', $rating ) ); ?>">
			  <?php for ( $star = 0; $star < $rating; $star++ ) : ?>
              <li class="reviews__star" aria-hidden="true"><i class="fas fa-star"></i></li>
			  <?php endfor; ?>
            </ul>
            <cite class="reviews__author-name"><?php echo esc_html( $item['author'] ); ?></cite>
            <blockquote class="reviews__quote">
              <p class="reviews__text" data-review-slider-text><?php echo wp_kses_post( $item['text'] ); ?></p>
            </blockquote>
            <footer class="reviews__read-all" data-review-slider-read-more hidden>
              <a class="reviews__read-more-link" href="<?php echo esc_url( $full_url ); ?>" data-review-slider-full-link aria-label="<?php echo esc_attr( sprintf( 'Читать весь отзыв — %s', wp_strip_all_tags( (string) ( $item['author'] ?? '' ) ) ) ); ?>">Читать весь отзыв</a>
            </footer>
          </div>
        </article>
		<?php endforeach; ?>
      </div>

      <div class="reviews__pagination swiper-pagination" data-reviews-pagination></div>
      <?php get_template_part( 'template-parts/components/fp02-slider-mobile-nav' ); ?>
    </div>
  </div>
</section>
