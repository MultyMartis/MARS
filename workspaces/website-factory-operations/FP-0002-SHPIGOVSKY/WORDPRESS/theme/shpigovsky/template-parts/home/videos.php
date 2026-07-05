<?php
/**
 * Template part: home/videos.php
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
<section data-reveal class="home-videos" aria-labelledby="home-videos-heading">
  <div class="container">
    <h2 class="home-videos__heading" id="home-videos-heading">Видео о&nbsp;нашем центре</h2>

    <div class="home-videos__grid">
      <figure class="home-videos__card">
        <a
          class="home-videos__link"
          href="<?php echo esc_url( shpigovsky_asset_uri( 'video/sergey-shpigovsky-interview.mp4' ) ); ?>"
          data-fancybox="home-videos"
          data-home-video
          data-video-title="Интервью с&nbsp;Сергеем Шпиговским"
          aria-label="Смотреть видео: интервью с&nbsp;Сергеем Шпиговским"
        >
          <img
            class="home-videos__preview-image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/videos/sergey-shpigovsky-interview-poster.webp' ) ); ?>"
            width="1280"
            height="720"
            alt="Превью видео: интервью с&nbsp;Сергеем Шпиговским"
            loading="lazy"
            decoding="async"
          >
          <span class="home-videos__play" aria-hidden="true">
            <span class="home-videos__play-button">
              <span class="home-videos__play-icon"><i class="fas fa-play"></i></span>
            </span>
          </span>
        </a>
      </figure>

      <figure class="home-videos__card">
        <a
          class="home-videos__link"
          href="<?php echo esc_url( shpigovsky_asset_uri( 'video/shpigovsky-center.mp4' ) ); ?>"
          data-fancybox="home-videos"
          data-home-video
          data-video-title="Центр профилактики зависимостей Сергея Шпиговского"
          aria-label="Смотреть видео: центр профилактики зависимостей Сергея Шпиговского"
        >
          <img
            class="home-videos__preview-image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/videos/shpigovsky-center-poster.webp' ) ); ?>"
            width="1920"
            height="1080"
            alt="Превью видео: центр профилактики зависимостей Сергея Шпиговского"
            loading="lazy"
            decoding="async"
          >
          <span class="home-videos__play" aria-hidden="true">
            <span class="home-videos__play-button">
              <span class="home-videos__play-icon"><i class="fas fa-play"></i></span>
            </span>
          </span>
        </a>
      </figure>
    </div>
  </div>
</section>
