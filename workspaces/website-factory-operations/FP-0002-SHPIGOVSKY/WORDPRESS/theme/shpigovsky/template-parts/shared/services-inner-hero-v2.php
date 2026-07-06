<?php
/**
 * Template part: shared/services-inner-hero-v2.php
 *
 * Canonical V9 services-inner-hero-v2 renderer.
 *
 * @package Shpigovsky
 *
 * @var array<string, mixed> $args {
 *     @type string $title_id    H1 element id.
 *     @type string $eyebrow     Eyebrow copy (HTML allowed).
 *     @type string $title       H1 text.
 *     @type string $lead        Lead copy (HTML allowed).
 *     @type string $cta_label   CTA button label.
 *     @type string $cta_source  data-modal-source value.
 *     @type string $image_url   Hero image URL.
 *     @type string $image_alt   Hero image alt.
 *     @type int    $image_width Image width attribute.
 *     @type int    $image_height Image height attribute.
 * }
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args = wp_parse_args(
	isset( $args ) ? $args : array(),
	array(
		'title_id'     => 'services-inner-hero-v2-title',
		'eyebrow'      => '',
		'title'        => '',
		'lead'         => '',
		'cta_label'    => shpigovsky_get_hero_default_cta_label(),
		'cta_source'   => 'services-hero-v2',
		'image_url'    => '',
		'image_alt'    => '',
		'image_width'  => 1400,
		'image_height' => 628,
	)
);

$title_id     = (string) $args['title_id'];
$eyebrow      = (string) $args['eyebrow'];
$title        = (string) $args['title'];
$lead         = (string) $args['lead'];
$cta_label    = (string) $args['cta_label'];
$cta_source   = (string) $args['cta_source'];
$image_url    = (string) $args['image_url'];
$image_alt    = (string) $args['image_alt'];
$image_width  = (int) $args['image_width'];
$image_height = (int) $args['image_height'];
?>
<section data-reveal class="services-inner-hero-v2" aria-labelledby="<?php echo esc_attr( $title_id ); ?>">
	<div class="services-inner-hero-v2__shell">
		<?php if ( '' !== $image_url ) : ?>
			<div class="services-inner-hero-v2__media" aria-hidden="true">
				<img
					class="services-inner-hero-v2__image"
					src="<?php echo esc_url( $image_url ); ?>"
					width="<?php echo (int) $image_width; ?>"
					height="<?php echo (int) $image_height; ?>"
					alt="<?php echo esc_attr( $image_alt ); ?>"
				>
				<div class="services-inner-hero-v2__overlay"></div>
			</div>
		<?php endif; ?>

		<div class="services-inner-hero-v2__content">
			<div class="container services-inner-hero-v2__container">
				<div class="services-inner-hero-v2__copy">
					<?php if ( '' !== $eyebrow ) : ?>
						<p class="services-inner-hero-v2__eyebrow"><?php echo wp_kses_post( $eyebrow ); ?></p>
					<?php endif; ?>
					<div class="services-inner-hero-v2__scene">
						<div class="services-inner-hero-v2__main">
							<h1 class="services-inner-hero-v2__title" id="<?php echo esc_attr( $title_id ); ?>"><?php echo esc_html( $title ); ?></h1>
							<?php if ( '' !== $lead ) : ?>
								<p class="services-inner-hero-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
							<?php endif; ?>
						</div>
						<div class="services-inner-hero-v2__actions">
							<button
								class="btn btn_dark btn--primary services-inner-hero-v2__cta"
								type="button"
								data-modal-open="consultation"
								data-modal-source="<?php echo esc_attr( $cta_source ); ?>"
								data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
								data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
							>
								<?php echo esc_html( $cta_label ); ?>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
