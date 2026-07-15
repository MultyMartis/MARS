<?php
/**
 * Template part: shared/services-inner-hero-v2.php
 *
 * Canonical V9 services-inner-hero-v2 renderer.
 * V9-06E43: optional multi-slide mode for Services hub (services_hero_slides).
 *
 * @package Shpigovsky
 *
 * @var array<string, mixed> $args {
 *     Classic single-slide args (subdivision/leaf) OR hub slides mode.
 * }
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args = wp_parse_args(
	isset( $args ) ? $args : array(),
	array(
		'title_id'          => 'services-inner-hero-v2-title',
		'eyebrow'           => '',
		'title'             => '',
		'lead'              => '',
		'cta_label'         => shpigovsky_get_hero_default_cta_label(),
		'cta_source'        => 'services-hero-v2',
		'image_url'         => '',
		'image_alt'         => '',
		'image_width'       => 1400,
		'image_height'      => 628,
		'default_cta_label' => '',
		'slides'            => array(),
		'is_slider'         => false,
		'autoplay_enabled'  => false,
		'autoplay_delay'    => 5000,
		'arrows_enabled'    => false,
		'dots_enabled'      => false,
	)
);

$title_id          = (string) $args['title_id'];
$cta_source        = (string) $args['cta_source'];
$default_cta_label = '' !== (string) $args['default_cta_label']
	? (string) $args['default_cta_label']
	: (string) $args['cta_label'];

$slides = array();
if ( ! empty( $args['slides'] ) && is_array( $args['slides'] ) ) {
	foreach ( $args['slides'] as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}
		$slides[] = $row;
	}
}

if ( empty( $slides ) ) {
	$slides[] = array(
		'eyebrow'   => (string) $args['eyebrow'],
		'title'     => (string) $args['title'],
		'lead'      => (string) $args['lead'],
		'cta_label' => (string) $args['cta_label'],
		'image'     => array(
			'url'    => (string) $args['image_url'],
			'alt'    => (string) $args['image_alt'],
			'width'  => (int) $args['image_width'],
			'height' => (int) $args['image_height'],
		),
	);
}

$slide_count = count( $slides );
$is_slider   = ! empty( $args['is_slider'] ) && $slide_count > 1;
$autoplay_enabled = $is_slider && ! empty( $args['autoplay_enabled'] );
$arrows_enabled   = $is_slider && ! empty( $args['arrows_enabled'] );
$dots_enabled     = $is_slider && ! empty( $args['dots_enabled'] );
$autoplay_delay   = (int) $args['autoplay_delay'];
if ( $autoplay_delay < 1000 ) {
	$autoplay_delay = 5000;
}

$section_class = 'services-inner-hero-v2';
if ( $is_slider ) {
	$section_class .= ' services-inner-hero-v2--slider';
}

$slider_attrs = '';
if ( $is_slider ) {
	$slider_attrs = sprintf(
		' data-services-hero-slider data-services-hero-autoplay="%s" data-services-hero-delay="%d" data-services-hero-arrows="%s" data-services-hero-dots="%s"',
		$autoplay_enabled ? '1' : '0',
		$autoplay_delay,
		$arrows_enabled ? '1' : '0',
		$dots_enabled ? '1' : '0'
	);
}

/**
 * Normalize one slide row for shell render.
 *
 * @param array<string,mixed> $slide Slide data.
 * @param string              $default_cta Default CTA.
 * @return array{eyebrow:string,title:string,lead:string,cta:string,image_url:string,image_alt:string,image_width:int,image_height:int}
 */
$normalize = static function ( $slide, $default_cta ) {
	$cta = isset( $slide['cta_label'] ) ? trim( (string) $slide['cta_label'] ) : '';
	if ( '' === $cta ) {
		$cta = $default_cta;
	}
	$image = isset( $slide['image'] ) && is_array( $slide['image'] ) ? $slide['image'] : array();

	return array(
		'eyebrow'       => isset( $slide['eyebrow'] ) ? trim( (string) $slide['eyebrow'] ) : '',
		'title'         => isset( $slide['title'] ) ? trim( (string) $slide['title'] ) : '',
		'lead'          => isset( $slide['lead'] ) ? trim( (string) $slide['lead'] ) : '',
		'cta'           => $cta,
		'image_url'     => isset( $image['url'] ) ? (string) $image['url'] : '',
		'image_alt'     => isset( $image['alt'] ) ? (string) $image['alt'] : '',
		'image_width'   => isset( $image['width'] ) ? (int) $image['width'] : 1400,
		'image_height'  => isset( $image['height'] ) ? (int) $image['height'] : 628,
	);
};

/**
 * Print shell inner markup for one slide.
 *
 * @param array<string,mixed> $n Normalized slide.
 * @param int                 $index Index.
 * @param string              $title_id Title id.
 * @param string              $cta_source Source.
 * @return void
 */
$print_shell = static function ( $n, $index, $title_id, $cta_source ) {
	?>
	<div class="services-inner-hero-v2__shell">
		<?php if ( '' !== $n['image_url'] ) : ?>
			<div class="services-inner-hero-v2__media" aria-hidden="true">
				<img
					class="services-inner-hero-v2__image"
					src="<?php echo esc_url( $n['image_url'] ); ?>"
					width="<?php echo (int) $n['image_width']; ?>"
					height="<?php echo (int) $n['image_height']; ?>"
					alt="<?php echo esc_attr( $n['image_alt'] ); ?>"
					<?php echo $index > 0 ? 'loading="lazy" decoding="async"' : ''; ?>
				>
				<div class="services-inner-hero-v2__overlay"></div>
			</div>
		<?php endif; ?>

		<div class="services-inner-hero-v2__content">
			<div class="container services-inner-hero-v2__container">
				<div class="services-inner-hero-v2__copy">
					<?php if ( '' !== $n['eyebrow'] ) : ?>
						<p class="services-inner-hero-v2__eyebrow"><?php echo wp_kses_post( $n['eyebrow'] ); ?></p>
					<?php endif; ?>
					<div class="services-inner-hero-v2__scene">
						<div class="services-inner-hero-v2__main">
							<?php if ( 0 === $index ) : ?>
								<h1 class="services-inner-hero-v2__title" id="<?php echo esc_attr( $title_id ); ?>"><?php echo esc_html( $n['title'] ); ?></h1>
							<?php else : ?>
								<p class="services-inner-hero-v2__title"><?php echo esc_html( $n['title'] ); ?></p>
							<?php endif; ?>
							<?php if ( '' !== $n['lead'] ) : ?>
								<p class="services-inner-hero-v2__lead"><?php echo wp_kses_post( $n['lead'] ); ?></p>
							<?php endif; ?>
						</div>
						<div class="services-inner-hero-v2__actions">
							<button
								class="btn btn_dark btn--primary services-inner-hero-v2__cta"
								type="button"
								data-modal-open="consultation"
								data-modal-source="<?php echo esc_attr( $cta_source ); ?>"
								data-modal-title="<?php echo esc_attr( $n['cta'] ); ?>"
								data-modal-submit-text="<?php echo esc_attr( $n['cta'] ); ?>"
							>
								<?php echo esc_html( $n['cta'] ); ?>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<?php
};
?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" aria-labelledby="<?php echo esc_attr( $title_id ); ?>">
	<?php if ( $is_slider ) : ?>
		<div class="services-inner-hero-v2__slider swiper"<?php echo $slider_attrs; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>>
			<div class="services-inner-hero-v2__slides swiper-wrapper">
				<?php foreach ( $slides as $index => $slide ) : ?>
					<?php $n = $normalize( $slide, $default_cta_label ); ?>
					<div class="services-inner-hero-v2__slide swiper-slide">
						<?php $print_shell( $n, (int) $index, $title_id, $cta_source ); ?>
					</div>
				<?php endforeach; ?>
			</div>
			<?php if ( $arrows_enabled ) : ?>
				<button class="services-inner-hero-v2__nav services-inner-hero-v2__nav--prev" type="button" data-services-hero-prev aria-label="<?php echo esc_attr__( 'Предыдущий слайд', 'shpigovsky' ); ?>">
					<span aria-hidden="true">‹</span>
				</button>
				<button class="services-inner-hero-v2__nav services-inner-hero-v2__nav--next" type="button" data-services-hero-next aria-label="<?php echo esc_attr__( 'Следующий слайд', 'shpigovsky' ); ?>">
					<span aria-hidden="true">›</span>
				</button>
			<?php endif; ?>
			<?php if ( $dots_enabled ) : ?>
				<div class="services-inner-hero-v2__pagination swiper-pagination" data-services-hero-pagination></div>
			<?php endif; ?>
		</div>
	<?php else : ?>
		<?php
		$n = $normalize( $slides[0], $default_cta_label );
		$print_shell( $n, 0, $title_id, $cta_source );
		?>
	<?php endif; ?>
</section>
