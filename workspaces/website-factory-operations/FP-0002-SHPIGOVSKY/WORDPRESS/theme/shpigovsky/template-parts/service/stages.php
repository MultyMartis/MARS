<?php
/**
 * Template part: service/stages.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$stages  = shpigovsky_get_service_repeater( $post_id, 'stages' );

if ( empty( $stages ) ) {
	return;
}

$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$section_id = 'subdivision' === $variant ? 'service-subdivision-start' : 'service-leaf-start';
$heading_id = $section_id . '-heading';
$cta        = shpigovsky_get_service_cta_band( $post_id );
?>
<section data-reveal class="service-leaf-stages-v1" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container service-leaf-stages-v1__container">
		<h2 class="service-leaf-stages-v1__heading" id="<?php echo esc_attr( $heading_id ); ?>">
			<?php echo esc_html__( 'Что нужно для прохождения реабилитации и лечения', 'shpigovsky' ); ?>
		</h2>

		<ol class="home-rehabilitation-requirements__steps service-leaf-stages-v1__steps">
			<?php foreach ( $stages as $index => $stage ) : ?>
				<?php
				$title = isset( $stage['title'] ) ? trim( (string) $stage['title'] ) : '';
				$text  = isset( $stage['text'] ) ? trim( (string) $stage['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}

				$number = str_pad( (string) ( $index + 1 ), 2, '0', STR_PAD_LEFT );
				?>
				<li class="home-rehabilitation-requirements__step">
					<span class="home-rehabilitation-requirements__step-number" aria-hidden="true"><?php echo esc_html( $number ); ?></span>
					<div class="home-rehabilitation-requirements__step-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="home-rehabilitation-requirements__step-title"><?php echo esc_html( $title ); ?></h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="home-rehabilitation-requirements__step-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
				</li>
			<?php endforeach; ?>
		</ol>

		<div class="service-leaf-stages-v1__cta">
			<?php
			set_query_var(
				'shpigovsky_program_cta_band',
				array_merge(
					$cta,
					array(
						'section_id'   => $section_id . '-cta',
						'heading_id'   => $section_id . '-cta-heading',
						'heading_text' => $cta['title'],
						'wrap_section' => false,
						'button_first' => true,
						'margin_flush' => true,
					)
				)
			);
			get_template_part( 'template-parts/components/program-cta-band' );
			?>
		</div>
	</div>
</section>
