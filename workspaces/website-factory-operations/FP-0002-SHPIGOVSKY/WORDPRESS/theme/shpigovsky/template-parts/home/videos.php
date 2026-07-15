<?php
/**
 * Template part: home/videos.php
 *
 * V9-06E40: Media Library video/poster fields with theme asset fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading = shpigovsky_home_text_or_fallback(
	'home_videos_heading',
	'Видео о&nbsp;нашем центре'
);
$videos = shpigovsky_get_home_videos_items();

if ( empty( $videos ) ) {
	return;
}

?>
<section data-reveal class="home-videos" aria-labelledby="home-videos-heading">
  <div class="container">
    <h2 class="home-videos__heading" id="home-videos-heading"><?php echo wp_kses_post( $heading ); ?></h2>

    <div class="home-videos__grid">
      <?php foreach ( $videos as $video ) : ?>
        <?php
			$title      = isset( $video['title'] ) ? (string) $video['title'] : '';
			$video_url  = isset( $video['video_url'] ) ? (string) $video['video_url'] : '';
			$poster_url = isset( $video['poster_url'] ) ? (string) $video['poster_url'] : '';
			$width      = isset( $video['width'] ) ? (int) $video['width'] : 1280;
			$height     = isset( $video['height'] ) ? (int) $video['height'] : 720;
			if ( '' === $video_url ) {
				continue;
			}
			$plain_title = wp_strip_all_tags( html_entity_decode( $title, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) );
			?>
      <figure class="home-videos__card">
        <a
          class="home-videos__link"
          href="<?php echo esc_url( $video_url ); ?>"
          data-fancybox="home-videos"
          data-home-video
          data-video-title="<?php echo esc_attr( $title ); ?>"
          aria-label="<?php echo esc_attr( sprintf( 'Смотреть видео: %s', $plain_title ) ); ?>"
        >
          <?php if ( '' !== $poster_url ) : ?>
          <img
            class="home-videos__preview-image"
            src="<?php echo esc_url( $poster_url ); ?>"
            width="<?php echo esc_attr( (string) $width ); ?>"
            height="<?php echo esc_attr( (string) $height ); ?>"
            alt="<?php echo esc_attr( sprintf( 'Превью видео: %s', $plain_title ) ); ?>"
            loading="lazy"
            decoding="async"
          >
          <?php endif; ?>
          <span class="home-videos__play" aria-hidden="true">
            <span class="home-videos__play-button">
              <span class="home-videos__play-icon"><i class="fas fa-play"></i></span>
            </span>
          </span>
        </a>
      </figure>
      <?php endforeach; ?>
    </div>
  </div>
</section>
