<?php
/**
 * Template part: services-hub/rehabilitation-program.php
 *
 * V9 services hub variant — services-program-v2 with static V9 copy authority.
 * V9-06E31: direction title/image link to program pages.
 * V9-06E43: ACF editable copy + visibility toggle; cards remain program pages.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_services_hub_list_enabled( 'services_hub_program_visible' ) ) {
	return;
}

$program_url = home_url( '/o-centre/programma-lecheniya/' );
$v9_program  = shpigovsky_get_v9_services_hub_program_copy();
$cta_phone   = shpigovsky_get_site_option( 'phone_primary' );
$cta_phone   = '' !== $cta_phone ? $cta_phone : '8 (925) 183-64-64';
$items       = shpigovsky_get_program_direction_items( 'service' );

$heading = shpigovsky_get_services_hub_field( 'services_hub_program_heading' );
$lead    = shpigovsky_get_services_hub_field( 'services_hub_program_lead' );
$intro   = shpigovsky_get_services_hub_field( 'services_hub_program_intro' );
$cta_title  = shpigovsky_get_services_hub_field( 'services_hub_program_cta_title' );
$cta_sub    = shpigovsky_get_services_hub_field( 'services_hub_program_cta_subtitle' );
$cta_button = shpigovsky_get_services_hub_field( 'services_hub_program_cta_button' );

if ( '' === $heading ) {
	$heading = $v9_program['heading'];
}
if ( '' === $lead ) {
	$lead = $v9_program['lead'];
}
if ( '' === $intro ) {
	$intro = $v9_program['intro'];
}
if ( '' === $cta_title ) {
	$cta_title = $v9_program['cta']['title'];
}
if ( '' === $cta_sub ) {
	$cta_sub = $v9_program['cta']['subtitle'];
}
if ( '' === $cta_button ) {
	$cta_button = $v9_program['cta']['button_label'];
}
?>
<section data-reveal class="services-program-v2 services-program-v2--media-frame-fixed services-program-v2--item-image-stack-tall services-program-v2--item-body-mobile-pad services-program-v2--item-media-mobile-pad" id="services-program" aria-labelledby="services-program-v2-heading">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="services-program-v2-heading">
				<?php echo esc_html( $heading ); ?>
			</h2>
			<a class="services-program-v2__head-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="services-program-v2__head-link-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="services-program-v2__head-link-icon" aria-hidden="true"><img class="services-program-v2__head-link-icon-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'svg/external-link.svg' ) ); ?>" width="20" height="20" alt=""></span>
			</a>
		</header>

		<p class="services-program-v2__lead">
			<?php echo esc_html( $lead ); ?>
		</p>

		<p class="services-program-v2__intro">
			<?php echo esc_html( $intro ); ?>
		</p>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<h3 class="services-program-v2__item-title">
							<a class="services-program-v2__item-title-link" href="<?php echo esc_url( $item['url'] ); ?>"><?php echo esc_html( $item['title_display'] ); ?></a>
						</h3>
					</div>
					<div class="services-program-v2__item-media">
						<a class="services-program-v2__item-image-link" href="<?php echo esc_url( $item['url'] ); ?>">
						<img
							class="services-program-v2__item-image"
							src="<?php echo esc_url( $item['image'] ); ?>"
							width="<?php echo (int) $item['width']; ?>"
							height="<?php echo (int) $item['height']; ?>"
							alt="<?php echo esc_attr( $item['alt'] ); ?>"
							loading="lazy"
							decoding="async"
						>
						</a>
					</div>
				</article>
			<?php endforeach; ?>
		</div>

		<?php
		set_query_var(
			'shpigovsky_program_cta_band',
			array(
				'title'          => $cta_title,
				'subtitle'       => $cta_sub,
				'phone'          => $cta_phone,
				'phone_hint'     => '',
				'button_label'   => $cta_button,
				'modal_source'   => $v9_program['cta']['source'],
				'section_id'     => '',
				'heading_id'     => '',
				'heading_text'   => '',
				'wrap_section'   => false,
				'wrap_container' => false,
				'button_first'   => false,
				'margin_flush'   => false,
			)
		);
		get_template_part( 'template-parts/components/program-cta-band' );
		?>

		<a class="services-program-v2__foot-link" href="<?php echo esc_url( $program_url ); ?>">
			<span class="services-program-v2__foot-link-text"><?php echo esc_html__( 'подробнее о программе', 'shpigovsky' ); ?></span>
			<span class="services-program-v2__foot-link-icon" aria-hidden="true"><img class="services-program-v2__foot-link-icon-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'svg/external-link.svg' ) ); ?>" width="20" height="20" alt=""></span>
		</a>
	</div>
</section>
