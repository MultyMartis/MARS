<?php
/**
 * Template part: components/program-cta-band.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$band = get_query_var( 'shpigovsky_program_cta_band', array() );

if ( empty( $band ) ) {
	$post_id = shpigovsky_get_current_service_id();
	$band    = shpigovsky_get_service_cta_band( $post_id > 0 ? $post_id : 0 );
	$band    = array_merge(
		$band,
		array(
			'section_id'   => 'program-cta-band',
			'heading_id'   => 'program-cta-band-heading',
			'heading_text' => $band['title'],
			'wrap_section' => true,
			'button_first' => true,
			'margin_flush' => true,
		)
	);
}

$title        = isset( $band['title'] ) ? trim( (string) $band['title'] ) : '';
$subtitle     = isset( $band['subtitle'] ) ? trim( (string) $band['subtitle'] ) : '';
$phone        = isset( $band['phone'] ) ? trim( (string) $band['phone'] ) : '';
$phone_hint   = isset( $band['phone_hint'] ) ? trim( (string) $band['phone_hint'] ) : '';
$button_label = isset( $band['button_label'] ) ? trim( (string) $band['button_label'] ) : '';
$source       = isset( $band['source'] ) ? trim( (string) $band['source'] ) : 'program-cta-band';
$section_id   = isset( $band['section_id'] ) ? trim( (string) $band['section_id'] ) : 'program-cta-band';
$heading_id   = isset( $band['heading_id'] ) ? trim( (string) $band['heading_id'] ) : 'program-cta-band-heading';
$heading_text = isset( $band['heading_text'] ) ? trim( (string) $band['heading_text'] ) : $title;
$wrap_section = ! empty( $band['wrap_section'] );
$button_first = ! empty( $band['button_first'] );
$margin_flush = ! empty( $band['margin_flush'] );

if ( '' === $title && '' === $button_label ) {
	return;
}

$phone_href = shpigovsky_phone_href( $phone );
$band_class = 'program-cta-band';

if ( $button_first ) {
	$band_class .= ' program-cta-band--button-first';
}

if ( $margin_flush ) {
	$band_class .= ' program-cta-band--flush';
}

if ( $wrap_section ) :
	?>
<section class="program-cta-band-section" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container program-cta-band-section__container">
		<?php if ( '' !== $heading_text ) : ?>
			<h2 class="visually-hidden" id="<?php echo esc_attr( $heading_id ); ?>"><?php echo esc_html( $heading_text ); ?></h2>
		<?php endif; ?>
<?php endif; ?>

	<div class="<?php echo esc_attr( $band_class ); ?>">
		<div class="program-cta-band__copy">
			<?php if ( '' !== $title ) : ?>
				<p class="program-cta-band__title"><?php echo wp_kses_post( $title ); ?></p>
			<?php endif; ?>
			<?php if ( '' !== $subtitle ) : ?>
				<p class="program-cta-band__subtitle"><?php echo wp_kses_post( $subtitle ); ?></p>
			<?php endif; ?>
		</div>

		<?php if ( '' !== $phone && '' !== $phone_href ) : ?>
			<a class="program-cta-band__phone" href="<?php echo esc_url( $phone_href ); ?>">
				<span class="program-cta-band__phone-number"><?php echo wp_kses_post( $phone ); ?></span>
				<?php if ( '' !== $phone_hint ) : ?>
					<span class="program-cta-band__phone-hint"><?php echo esc_html( $phone_hint ); ?></span>
				<?php endif; ?>
			</a>
		<?php endif; ?>

		<button
			type="button"
			class="btn btn_dark btn--primary program-cta-band__button"
			data-modal-open="consultation"
			data-modal-source="<?php echo esc_attr( $source ); ?>"
			data-modal-title="<?php echo esc_attr( $button_label ); ?>"
			data-modal-submit-text="<?php echo esc_attr( $button_label ); ?>"
		><?php echo esc_html( $button_label ); ?></button>
	</div>

<?php if ( $wrap_section ) : ?>
	</div>
</section>
<?php endif; ?>
