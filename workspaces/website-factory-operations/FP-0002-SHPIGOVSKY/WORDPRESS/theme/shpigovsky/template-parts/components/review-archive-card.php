<?php
/**
 * Template part: components/review-archive-card.php
 *
 * Static V9 archive card — V9-06D9-W.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$item = wp_parse_args(
	$args ?? array(),
	array(
		'author'       => '',
		'text'         => '',
		'context'      => '',
		'source'       => '',
		'date'         => '',
		'rating'       => 5,
		'service_href' => '',
	)
);

$author = trim( (string) $item['author'] );
$text   = trim( (string) $item['text'] );

if ( '' === $author && '' === $text ) {
	return;
}

$rating       = shpigovsky_normalize_review_rating( $item['rating'] ?? 5 );
$date_parts   = shpigovsky_format_review_archive_date( $item['date'] ?? '' );
$service_text = trim( (string) ( $item['context'] ?: $item['source'] ) );
$service_href = trim( (string) $item['service_href'] );
$rating_label = sprintf( 'Оценка %d из 5', $rating );

?>
<article class="review-archive-card" data-reveal>
  <header class="review-archive-card__header">
    <ul class="review-archive-card__rating" aria-label="<?php echo esc_attr( $rating_label ); ?>">
	  <?php for ( $star = 0; $star < $rating; $star++ ) : ?>
      <li class="review-archive-card__star" aria-hidden="true"><i class="fas fa-star"></i></li>
	  <?php endfor; ?>
    </ul>
	<?php if ( '' !== $date_parts['formatted'] ) : ?>
    <time class="review-archive-card__date"<?php echo '' !== $date_parts['iso'] ? ' datetime="' . esc_attr( $date_parts['iso'] ) . '"' : ''; ?>><?php echo esc_html( $date_parts['formatted'] ); ?></time>
	<?php endif; ?>
  </header>
  <h2 class="review-archive-card__name"><?php echo esc_html( $author ); ?></h2>
	<?php if ( '' !== $service_text ) : ?>
  <p class="review-archive-card__service">
    Повод обращения:
		<?php if ( '' !== $service_href ) : ?>
    <a class="review-archive-card__service-link" href="<?php echo esc_url( $service_href ); ?>"><?php echo esc_html( $service_text ); ?></a>
		<?php else : ?>
    <span><?php echo esc_html( $service_text ); ?></span>
		<?php endif; ?>
  </p>
	<?php endif; ?>
  <div class="review-archive-card__body">
	<?php echo wp_kses_post( wpautop( $text ) ); ?>
  </div>
</article>
