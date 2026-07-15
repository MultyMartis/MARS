<?php
/**
 * Template part: home/articles-teaser.php
 *
 * V9-06E35: published blog posts + Swiper (gallery options pattern; dots, no arrows).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_home_list_enabled( 'home_articles_visible' ) ) {
	return;
}

$articles_heading = shpigovsky_home_text_or_fallback( 'home_articles_heading', 'Статьи' );
$cards            = shpigovsky_get_home_articles_cards( 6 );
$link_label       = function_exists( 'shpigovsky_get_blog_archive_card_link_label' )
	? shpigovsky_get_blog_archive_card_link_label()
	: 'Читать';

if ( empty( $cards ) ) {
	return;
}

?>
<section class="home-articles" aria-labelledby="home-articles-heading">
  <div class="container">
    <div class="home-articles__head">
      <h2 class="home-articles__heading" id="home-articles-heading"><?php echo esc_html( $articles_heading ); ?></h2>
      <a class="home-articles__all-link" href="<?php echo esc_url( home_url( '/blog/' ) ); ?>">
        <span class="home-articles__all-text">все статьи</span>
        <span class="home-articles__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <div class="home-articles__slider swiper" data-articles-slider data-reveal-group>
      <div class="home-articles__wrapper swiper-wrapper">
        <?php foreach ( $cards as $index => $card ) : ?>
          <?php
			$title        = isset( $card['title'] ) ? (string) $card['title'] : '';
			$url          = isset( $card['url'] ) ? (string) $card['url'] : '';
			$image_url    = isset( $card['image_url'] ) ? (string) $card['image_url'] : '';
			$image_width  = isset( $card['image_width'] ) ? (int) $card['image_width'] : 1200;
			$image_height = isset( $card['image_height'] ) ? (int) $card['image_height'] : 800;
			$image_alt    = isset( $card['image_alt'] ) && '' !== trim( (string) $card['image_alt'] ) ? (string) $card['image_alt'] : $title;
			$meta_label   = isset( $card['link_label'] ) && '' !== trim( (string) $card['link_label'] ) ? (string) $card['link_label'] : $link_label;
			$is_lazy      = $index > 0;
			?>
        <article class="home-articles__card swiper-slide" data-reveal>
          <a class="home-articles__card-link" href="<?php echo esc_url( $url ); ?>">
            <?php if ( '' !== $image_url ) : ?>
            <img
              class="home-articles__image"
              src="<?php echo esc_url( $image_url ); ?>"
              width="<?php echo esc_attr( (string) $image_width ); ?>"
              height="<?php echo esc_attr( (string) $image_height ); ?>"
              alt="<?php echo esc_attr( $image_alt ); ?>"
              <?php echo $is_lazy ? 'loading="lazy"' : ''; ?>
              decoding="async"
            >
            <?php endif; ?>
            <h3 class="home-articles__title"><?php echo esc_html( $title ); ?></h3>
            <p class="home-articles__meta"><?php echo esc_html( $meta_label ); ?></p>
          </a>
        </article>
        <?php endforeach; ?>
      </div>
      <div class="home-articles__pagination swiper-pagination" data-articles-pagination data-gallery-pagination></div>
    </div>
  </div>
</section>
