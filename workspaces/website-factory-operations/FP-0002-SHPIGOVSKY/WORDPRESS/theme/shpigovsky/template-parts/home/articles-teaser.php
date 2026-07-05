<?php
/**
 * Template part: home/articles-teaser.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

?>
<section class="home-articles" aria-labelledby="home-articles-heading">
  <div class="container">
    <div class="home-articles__head">
      <h2 class="home-articles__heading" id="home-articles-heading">Статьи</h2>
      <a class="home-articles__all-link" href="<?php echo esc_url( home_url( '/blog/' ) ); ?>">
        <span class="home-articles__all-text">все статьи</span>
        <span class="home-articles__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <div class="home-articles__grid" data-reveal-group>
      <article class="home-articles__card" data-reveal>
        <a class="home-articles__card-link" href="<?php echo esc_url( home_url( '/blog/nazvanie-stati/' ) ); ?>">
          <img class="home-articles__image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-articles/article-alcohol-dependence.webp' ) ); ?>" width="1216" height="1632" alt="" loading="lazy" decoding="async">
          <h3 class="home-articles__title">Лечение алкогольной зависимости: почему сила воли здесь ни&nbsp;при чём</h3>
          <p class="home-articles__meta">Читать</p>
        </a>
      </article>
      <article class="home-articles__card" data-reveal>
        <a class="home-articles__card-link" href="<?php echo esc_url( home_url( '/blog/nazvanie-stati/' ) ); ?>">
          <img class="home-articles__image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-articles/article-yoga-therapy.webp' ) ); ?>" width="1920" height="1280" alt="Йога в терапии" loading="lazy" decoding="async">
          <h3 class="home-articles__title">Йога в&nbsp;терапии: снятие абстинентного синдрома, снижение кортизола</h3>
          <p class="home-articles__meta">Читать</p>
        </a>
      </article>
      <article class="home-articles__card" data-reveal>
        <a class="home-articles__card-link" href="<?php echo esc_url( home_url( '/blog/nazvanie-stati/' ) ); ?>">
          <img class="home-articles__image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-articles/article-bos-therapy.webp' ) ); ?>" width="2048" height="1365" alt="БОС-терапия" loading="lazy" decoding="async">
          <h3 class="home-articles__title">БОС-терапия: тренировка конкретных зон мозга с&nbsp;помощью технологий</h3>
          <p class="home-articles__meta">Читать</p>
        </a>
      </article>
    </div>
  </div>
</section>
