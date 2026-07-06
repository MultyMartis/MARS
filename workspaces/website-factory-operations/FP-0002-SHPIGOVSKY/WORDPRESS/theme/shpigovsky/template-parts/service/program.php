<?php
/**
 * Template part: service/program.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id    = shpigovsky_get_current_service_id();
$variant    = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$section_id = 'subdivision' === $variant ? 'service-subdivision-program' : 'service-leaf-program';
$heading_id = $section_id . '-heading';
$program_url = home_url( '/o-centre/programma-lecheniya/' );

if ( 'subdivision' === $variant ) {
	$items = shpigovsky_get_service_repeater( $post_id, 'programme_items' );
	$fallback_items = shpigovsky_get_service_subdivision_programme_fallback_items();

	if ( empty( $items ) ) {
		$items = $fallback_items;
	} else {
		foreach ( $items as $index => $item ) {
			$has_image = ! empty( $item['image'] );
			if ( ! $has_image && isset( $fallback_items[ $index ] ) ) {
				$items[ $index ]['image']  = $fallback_items[ $index ]['image'];
				$items[ $index ]['width']   = $fallback_items[ $index ]['width'];
				$items[ $index ]['height']  = $fallback_items[ $index ]['height'];
				$items[ $index ]['alt']     = $fallback_items[ $index ]['alt'];
			}
		}
	}

	$lead   = shpigovsky_get_service_field( $post_id, 'hero_lead' );
	$intro  = '';
	$intro2 = '';

	if ( '' === $lead ) {
		$lead = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.';
	}

	$intro  = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.';
	$intro2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.';

	$section_class = 'services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked services-program-v2--grid-compact services-program-v2--media-contain services-program-v2--title-block services-program-v2--media-frame-fixed services-program-v2--item-image-mobile-short';
	?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html__( 'Наша программа включает 4 направления', 'shpigovsky' ); ?>
			</h2>
			<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</header>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-program-v2__lead"><?php echo esc_html( $lead ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $intro ) : ?>
			<p class="services-program-v2__intro"><?php echo esc_html( $intro ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $intro2 ) : ?>
			<p class="services-program-v2__intro services-program-v2__intro--continued"><?php echo esc_html( $intro2 ); ?></p>
		<?php endif; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';
				$image = isset( $item['image'] ) ? trim( (string) $item['image'] ) : '';
				$width = isset( $item['width'] ) ? (int) $item['width'] : 0;
				$height = isset( $item['height'] ) ? (int) $item['height'] : 0;
				$alt   = isset( $item['alt'] ) ? trim( (string) $item['alt'] ) : $title;

				if ( '' === $title && '' === $text && '' === $image ) {
					continue;
				}
				?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="services-program-v2__item-title"><?php echo esc_html( $title ); ?></h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="services-program-v2__item-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
					<?php if ( '' !== $image ) : ?>
						<div class="services-program-v2__item-media">
							<img
								class="services-program-v2__item-image"
								src="<?php echo esc_url( $image ); ?>"
								<?php if ( $width > 0 ) : ?>
									width="<?php echo esc_attr( (string) $width ); ?>"
								<?php endif; ?>
								<?php if ( $height > 0 ) : ?>
									height="<?php echo esc_attr( (string) $height ); ?>"
								<?php endif; ?>
								alt="<?php echo esc_attr( $alt ); ?>"
								loading="lazy"
								decoding="async"
							>
						</div>
					<?php endif; ?>
				</article>
			<?php endforeach; ?>
		</div>

		<a class="services-program-v2__foot-link" href="<?php echo esc_url( $program_url ); ?>">
			<span class="services-program-v2__foot-link-text"><?php echo esc_html__( 'подробнее о программе', 'shpigovsky' ); ?></span>
			<span class="services-program-v2__foot-link-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
		</a>
	</div>
</section>
	<?php
	return;
}

$items = shpigovsky_get_service_repeater( $post_id, 'programme_items' );

if ( empty( $items ) ) {
	$items = shpigovsky_get_service_programme_fallback_items();
}

$lead = shpigovsky_get_service_field( $post_id, 'hero_lead' );
?>
<section data-reveal class="services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container services-program-v2__container">
		<div class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html__( 'Наша программа включает 4 направления', 'shpigovsky' ); ?>
			</h2>
			<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-program-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
		<?php endif; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}
				?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="services-program-v2__item-title"><?php echo esc_html( $title ); ?></h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="services-program-v2__item-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>
