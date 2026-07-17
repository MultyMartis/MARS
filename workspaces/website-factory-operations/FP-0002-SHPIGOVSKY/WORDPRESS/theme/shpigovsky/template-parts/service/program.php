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

$program_url = home_url( '/o-centre/programma-lecheniya/' );
$cta_phone   = shpigovsky_get_site_option( 'phone_primary' );
$cta_phone   = '' !== $cta_phone ? $cta_phone : '8 (925) 183-64-64';

if ( shpigovsky_is_service_general_variant( $variant ) ) {
	$program = function_exists( 'shpigovsky_get_general_program_copy' )
		? shpigovsky_get_general_program_copy( $post_id )
		: array(
			'heading'    => __( 'Наша программа включает 4 направления', 'shpigovsky' ),
			'more_label' => __( 'подробнее', 'shpigovsky' ),
			'lead'       => '',
			'intros'     => array(),
		);

	$has_program_chrome = '' !== (string) ( $program['lead'] ?? '' ) || ! empty( $program['intros'] );
	$is_alcohol_leaf    = function_exists( 'shpigovsky_is_known_alcohol_service_page' )
		&& shpigovsky_is_known_alcohol_service_page( $post_id );

	if ( $has_program_chrome || $is_alcohol_leaf ) {
		$items         = shpigovsky_get_service_subdivision_programme_fallback_items();
		$section_class = 'services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked services-program-v2--title-flush services-program-v2--item-body-spaced services-program-v2--item-image-stack-tall services-program-v2--media-frame-fixed';
		$intros        = isset( $program['intros'] ) && is_array( $program['intros'] ) ? $program['intros'] : array();
		?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html( (string) $program['heading'] ); ?>
			</h2>
			<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html( (string) $program['more_label'] ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</header>

		<?php if ( '' !== (string) ( $program['lead'] ?? '' ) ) : ?>
			<p class="services-program-v2__lead"><?php echo esc_html( (string) $program['lead'] ); ?></p>
		<?php endif; ?>
		<?php foreach ( $intros as $intro_index => $intro_text ) : ?>
			<p class="services-program-v2__intro<?php echo $intro_index > 0 ? ' services-program-v2__intro--continued' : ''; ?>"><span><?php echo esc_html( (string) $intro_text ); ?></span></p>
		<?php endforeach; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<?php
				$title  = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$image  = isset( $item['image'] ) ? trim( (string) $item['image'] ) : '';
				$width  = isset( $item['width'] ) ? (int) $item['width'] : 0;
				$height = isset( $item['height'] ) ? (int) $item['height'] : 0;
				$alt    = isset( $item['alt'] ) ? trim( (string) $item['alt'] ) : $title;
				$url    = isset( $item['url'] ) ? trim( (string) $item['url'] ) : '';
				?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<h3 class="services-program-v2__item-title">
							<?php if ( '' !== $url ) : ?>
								<a class="services-program-v2__item-title-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
							<?php else : ?>
								<?php echo esc_html( $title ); ?>
							<?php endif; ?>
						</h3>
					</div>
					<?php if ( '' !== $image ) : ?>
						<div class="services-program-v2__item-media">
							<?php if ( '' !== $url ) : ?>
								<a class="services-program-v2__item-image-link" href="<?php echo esc_url( $url ); ?>">
							<?php endif; ?>
							<img class="services-program-v2__item-image" src="<?php echo esc_url( $image ); ?>" width="<?php echo esc_attr( (string) $width ); ?>" height="<?php echo esc_attr( (string) $height ); ?>" alt="<?php echo esc_attr( $alt ); ?>" loading="lazy" decoding="async">
							<?php if ( '' !== $url ) : ?>
								</a>
							<?php endif; ?>
						</div>
					<?php endif; ?>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>
		<?php
		return;
	}
}

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
			if ( empty( $items[ $index ]['url'] ) && isset( $fallback_items[ $index ]['url'] ) ) {
				$items[ $index ]['url'] = $fallback_items[ $index ]['url'];
			}
		}
	}

	// V9-06E50: program chrome from ACF; empty optional text is hidden (no Lorem demo inject).
	$program_heading = shpigovsky_section_text( $post_id, 'section_program_heading', '' );
	$program_more    = shpigovsky_section_text( $post_id, 'section_program_more_label', '' );
	$program_footer  = shpigovsky_section_text( $post_id, 'section_program_footer_label', '' );

	$lead = shpigovsky_get_section_field( $post_id, 'section_program_lead' );
	if ( '' === $lead ) {
		$lead = shpigovsky_get_service_field( $post_id, 'hero_lead' );
	}

	$intro_items = shpigovsky_get_section_program_intro_items( $post_id );

	$section_class = 'services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked services-program-v2--grid-compact services-program-v2--media-contain services-program-v2--title-block services-program-v2--media-frame-fixed services-program-v2--item-image-mobile-short';
	?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<?php if ( '' !== $program_heading ) : ?>
				<h2 class="services-program-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
					<?php echo esc_html( $program_heading ); ?>
				</h2>
			<?php else : ?>
				<h2 class="services-program-v2__heading screen-reader-text" id="<?php echo esc_attr( $heading_id ); ?>">
					<?php esc_html_e( 'Программа', 'shpigovsky' ); ?>
				</h2>
			<?php endif; ?>
			<?php if ( '' !== $program_more ) : ?>
				<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $program_url ); ?>">
					<span class="home-rehabilitation-program__all-text"><?php echo esc_html( $program_more ); ?></span>
					<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
				</a>
			<?php endif; ?>
		</header>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-program-v2__lead"><?php echo esc_html( $lead ); ?></p>
		<?php endif; ?>

		<?php foreach ( $intro_items as $intro_index => $intro_text ) : ?>
			<?php
			$intro_class = 0 === (int) $intro_index
				? 'services-program-v2__intro'
				: 'services-program-v2__intro services-program-v2__intro--continued';
			?>
			<p class="<?php echo esc_attr( $intro_class ); ?>"><span><?php echo esc_html( $intro_text ); ?></span></p>
		<?php endforeach; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';
				$image = isset( $item['image'] ) ? trim( (string) $item['image'] ) : '';
				$width = isset( $item['width'] ) ? (int) $item['width'] : 0;
				$height = isset( $item['height'] ) ? (int) $item['height'] : 0;
				$alt   = isset( $item['alt'] ) ? trim( (string) $item['alt'] ) : $title;
				$url   = isset( $item['url'] ) ? trim( (string) $item['url'] ) : '';

				if ( '' === $title && '' === $text && '' === $image ) {
					continue;
				}
				?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="services-program-v2__item-title">
								<?php if ( '' !== $url ) : ?>
									<a class="services-program-v2__item-title-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
								<?php else : ?>
									<?php echo esc_html( $title ); ?>
								<?php endif; ?>
							</h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="services-program-v2__item-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
					<?php if ( '' !== $image ) : ?>
						<div class="services-program-v2__item-media">
							<?php if ( '' !== $url ) : ?>
								<a class="services-program-v2__item-image-link" href="<?php echo esc_url( $url ); ?>">
							<?php endif; ?>
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
							<?php if ( '' !== $url ) : ?>
								</a>
							<?php endif; ?>
						</div>
					<?php endif; ?>
				</article>
			<?php endforeach; ?>
		</div>

		<a class="services-program-v2__foot-link" href="<?php echo esc_url( $program_url ); ?>">
			<span class="services-program-v2__foot-link-text"><?php echo esc_html( $program_footer ); ?></span>
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
