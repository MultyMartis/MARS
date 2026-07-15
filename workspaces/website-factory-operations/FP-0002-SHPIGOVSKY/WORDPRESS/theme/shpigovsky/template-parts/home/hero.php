<?php
/**
 * Template part: home/hero.php
 *
 * V9-06E41: multi-slide Hero from home_hero_slides + Swiper when count > 1.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$raw_slides = shpigovsky_get_home_repeater( 'home_hero_slides' );
$slides     = array();

if ( is_array( $raw_slides ) ) {
	foreach ( $raw_slides as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
		$image = shpigovsky_resolve_hero_image( isset( $row['image'] ) ? $row['image'] : null, 'home' );

		if ( '' === $title && '' === $text && '' === $image['url'] ) {
			continue;
		}

		$slides[] = array(
			'title' => $title,
			'text'  => $text,
			'image' => $image,
		);
	}
}

if ( empty( $slides ) ) {
	$fallback_image = shpigovsky_get_home_hero_image();
	$slides[]       = array(
		'title' => 'Шпиговский дом',
		'text'  => 'Центр профилактики и&nbsp;лечения зависимостей',
		'image' => $fallback_image,
	);
}

$slide_count = count( $slides );
$is_slider   = $slide_count > 1;
$cta_label   = shpigovsky_get_local_hero_cta_label( shpigovsky_get_front_page_id() );

$autoplay_enabled = $is_slider && shpigovsky_home_list_enabled( 'home_hero_autoplay_enabled' );
$arrows_enabled   = $is_slider && shpigovsky_home_list_enabled( 'home_hero_arrows_enabled' );
$dots_enabled     = $is_slider && shpigovsky_home_list_enabled( 'home_hero_dots_enabled' );
$autoplay_delay   = (int) shpigovsky_get_home_field( 'home_hero_autoplay_delay' );
if ( $autoplay_delay < 1000 ) {
	$autoplay_delay = 5000;
}

$slider_attrs = '';
if ( $is_slider ) {
	$slider_attrs = sprintf(
		' data-hero-slider data-hero-autoplay="%s" data-hero-delay="%d" data-hero-arrows="%s" data-hero-dots="%s"',
		$autoplay_enabled ? '1' : '0',
		$autoplay_delay,
		$arrows_enabled ? '1' : '0',
		$dots_enabled ? '1' : '0'
	);
}
?>
<section class="hero hero--home<?php echo $is_slider ? ' hero--home-slider' : ''; ?>">
	<div class="hero__slider<?php echo $is_slider ? ' swiper' : ''; ?>"<?php echo $slider_attrs; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>>
		<div class="hero__slides<?php echo $is_slider ? ' swiper-wrapper' : ''; ?>">
			<?php foreach ( $slides as $index => $slide ) : ?>
				<?php
				$hero_title = '' !== $slide['title'] ? $slide['title'] : 'Шпиговский дом';
				$hero_text  = '' !== $slide['text'] ? $slide['text'] : 'Центр профилактики и&nbsp;лечения зависимостей';
				$hero_image = $slide['image'];
				$slide_class = $is_slider ? 'hero__slide swiper-slide' : 'hero__slide';
				?>
			<div class="<?php echo esc_attr( $slide_class ); ?>">
				<?php if ( '' !== $hero_image['url'] ) : ?>
					<div class="hero__media" aria-hidden="true">
						<img
							class="hero__image"
							src="<?php echo esc_url( $hero_image['url'] ); ?>"
							width="<?php echo esc_attr( (string) $hero_image['width'] ); ?>"
							height="<?php echo esc_attr( (string) $hero_image['height'] ); ?>"
							alt="<?php echo esc_attr( $hero_image['alt'] ); ?>"
							<?php echo $index > 0 ? 'loading="lazy" decoding="async"' : ''; ?>
						>
					</div>
				<?php endif; ?>

				<div class="hero__content">
					<div class="hero__container">
						<div class="hero__panel">
							<div class="hero__content-inner">
								<p class="hero__tagline"><?php echo wp_kses_post( $hero_text ); ?></p>
								<?php if ( 0 === $index ) : ?>
								<h1 class="hero__title"><?php echo esc_html( $hero_title ); ?></h1>
								<?php else : ?>
								<p class="hero__title"><?php echo esc_html( $hero_title ); ?></p>
								<?php endif; ?>
							</div>
						</div>
						<div class="hero__actions">
							<button
								class="btn btn_dark btn--primary hero__button"
								type="button"
								data-modal-open="consultation"
								data-modal-source="hero"
								data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
								data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
							>
								<?php echo esc_html( $cta_label ); ?>
							</button>
						</div>
					</div>
				</div>
			</div>
			<?php endforeach; ?>
		</div>

		<?php if ( $arrows_enabled ) : ?>
		<button class="hero__nav hero__nav--prev" type="button" data-hero-prev aria-label="<?php echo esc_attr__( 'Предыдущий слайд', 'shpigovsky' ); ?>">
			<span aria-hidden="true">‹</span>
		</button>
		<button class="hero__nav hero__nav--next" type="button" data-hero-next aria-label="<?php echo esc_attr__( 'Следующий слайд', 'shpigovsky' ); ?>">
			<span aria-hidden="true">›</span>
		</button>
		<?php endif; ?>

		<?php if ( $dots_enabled ) : ?>
		<div class="hero__pagination swiper-pagination" data-hero-pagination></div>
		<?php endif; ?>
	</div>
</section>
