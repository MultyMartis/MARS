<?php
/**
 * Template part: service/stages.php
 *
 * Subdivision stages: ACF SoT (V9-06E50). No normal hardcoded demo inject when empty.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$stages  = shpigovsky_get_service_repeater( $post_id, 'stages' );
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
// This block is the repeated «Что нужно для прохождения реабилитации и лечения» owner:
// Guest Visit CTA only here — do not use generic «Остались вопросы?» service CTA defaults.
$cta = function_exists( 'shpigovsky_get_about_guest_cta_band' )
	? shpigovsky_get_about_guest_cta_band( 'service-stages-guest-cta' )
	: shpigovsky_get_service_cta_band( $post_id );

if ( 'subdivision' === $variant ) {
	$section_id    = 'service-subdivision-stages';
	$heading_id    = 'service-subdivision-stages-heading';
	$section_class = 'service-subdivision-stages-v1';
	$steps_class   = 'service-subdivision-stages-v1__steps';
	$cta_wrap      = 'service-subdivision-stages-v1__cta';
	$support_wrap  = 'service-subdivision-stages-v1__support';
} else {
	$section_id    = 'service-leaf-start';
	$heading_id    = $section_id . '-heading';
	$section_class = 'service-leaf-stages-v1';
	$steps_class   = 'service-leaf-stages-v1__steps';
	$cta_wrap      = 'service-leaf-stages-v1__cta';
	$support_wrap  = '';
}

if ( 'subdivision' === $variant ) {
	$stages = shpigovsky_get_section_stages_items( $post_id );
} elseif ( empty( $stages ) ) {
	return;
}

$stages_heading  = '';
$stages_lead     = '';
$support_heading = '';
$support_items   = array();

if ( 'subdivision' === $variant ) {
	$stages_heading  = shpigovsky_section_text( $post_id, 'section_stages_heading', '' );
	$stages_lead     = shpigovsky_section_text( $post_id, 'section_stages_lead', '' );
	$support_heading = shpigovsky_section_text( $post_id, 'section_stages_support_heading', '' );

	$support_rows = shpigovsky_get_section_field_raw( $post_id, 'section_stages_support_items' );
	if ( is_array( $support_rows ) && ! empty( $support_rows ) ) {
		foreach ( $support_rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' !== $text ) {
				$support_items[] = $text;
			}
		}
	}
} else {
	$stages_heading = __( 'Что нужно для прохождения реабилитации и лечения', 'shpigovsky' );
}

if ( 'subdivision' === $variant && empty( $stages ) && '' === $stages_heading && '' === $stages_lead ) {
	return;
}
?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container <?php echo esc_attr( $section_class ); ?>__container">
		<?php if ( '' !== $stages_heading ) : ?>
			<h2 class="<?php echo esc_attr( $section_class ); ?>__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html( $stages_heading ); ?>
			</h2>
		<?php else : ?>
			<h2 class="<?php echo esc_attr( $section_class ); ?>__heading screen-reader-text" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php esc_html_e( 'Этапы', 'shpigovsky' ); ?>
			</h2>
		<?php endif; ?>

		<?php if ( 'subdivision' === $variant && '' !== $stages_lead ) : ?>
			<p class="service-subdivision-stages-v1__lead block-whith-red-line">
				<?php echo esc_html( $stages_lead ); ?>
			</p>
		<?php endif; ?>

		<?php if ( ! empty( $stages ) ) : ?>
			<ol class="home-rehabilitation-requirements__steps <?php echo esc_attr( $steps_class ); ?>">
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
		<?php endif; ?>

		<div class="<?php echo esc_attr( $cta_wrap ); ?>">
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

		<?php if ( 'subdivision' === $variant && ( '' !== $support_heading || ! empty( $support_items ) ) ) : ?>
			<div class="home-rehabilitation-requirements__support <?php echo esc_attr( $support_wrap ); ?>">
				<?php if ( '' !== $support_heading ) : ?>
					<p class="home-rehabilitation-requirements__support-heading"><?php echo esc_html( $support_heading ); ?></p>
				<?php endif; ?>
				<?php if ( ! empty( $support_items ) ) : ?>
					<ul class="home-rehabilitation-requirements__support-list">
						<?php foreach ( $support_items as $support_item ) : ?>
							<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html( $support_item ); ?></li>
						<?php endforeach; ?>
					</ul>
				<?php endif; ?>
			</div>
		<?php endif; ?>
	</div>
</section>
