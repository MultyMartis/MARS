<?php
/**
 * Template part: services-hub/rehabilitation-program.php
 *
 * V9 services hub variant — services-program-v2 with static V9 copy authority.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$program_url = home_url( '/o-centre/programma-lecheniya/' );
$v9_program  = shpigovsky_get_v9_services_hub_program_copy();
$cta_phone   = shpigovsky_get_site_option( 'phone_primary' );
$cta_phone   = '' !== $cta_phone ? $cta_phone : '8 (925) 183-64-64';

$items = array(
	array(
		'title' => '01 — Генотипирование',
		'image' => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-genotyping.webp' ),
		'width' => 1216,
		'height' => 1632,
		'alt'   => 'Генотипирование',
	),
	array(
		'title' => '02 — Нейропсихологическая коррекция',
		'image' => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-neuropsychology.webp' ),
		'width' => 1632,
		'height' => 1216,
		'alt'   => 'Нейропсихологическая коррекция',
	),
	array(
		'title' => '03 — Психокоррекция',
		'image' => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-psychocorrection.webp' ),
		'width' => 880,
		'height' => 1184,
		'alt'   => 'Психокоррекция',
	),
	array(
		'title' => '04 — Кинезиотерапия',
		'image' => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-kinesiotherapy.webp' ),
		'width' => 880,
		'height' => 1184,
		'alt'   => 'Кинезиотерапия',
	),
);
?>
<section data-reveal class="services-program-v2 services-program-v2--media-frame-fixed services-program-v2--item-image-stack-tall services-program-v2--item-body-mobile-pad services-program-v2--item-media-mobile-pad" id="services-program" aria-labelledby="services-program-v2-heading">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="services-program-v2-heading">
				<?php echo esc_html( $v9_program['heading'] ); ?>
			</h2>
			<a class="services-program-v2__head-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="services-program-v2__head-link-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="services-program-v2__head-link-icon" aria-hidden="true"><img class="services-program-v2__head-link-icon-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'svg/external-link.svg' ) ); ?>" width="20" height="20" alt=""></span>
			</a>
		</header>

		<p class="services-program-v2__lead">
			<?php echo esc_html( $v9_program['lead'] ); ?>
		</p>

		<p class="services-program-v2__intro">
			<?php echo esc_html( $v9_program['intro'] ); ?>
		</p>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<h3 class="services-program-v2__item-title"><?php echo esc_html( $item['title'] ); ?></h3>
					</div>
					<div class="services-program-v2__item-media">
						<img
							class="services-program-v2__item-image"
							src="<?php echo esc_url( $item['image'] ); ?>"
							width="<?php echo (int) $item['width']; ?>"
							height="<?php echo (int) $item['height']; ?>"
							alt="<?php echo esc_attr( $item['alt'] ); ?>"
							loading="lazy"
							decoding="async"
						>
					</div>
				</article>
			<?php endforeach; ?>
		</div>

		<?php
		set_query_var(
			'shpigovsky_program_cta_band',
			array(
				'title'          => $v9_program['cta']['title'],
				'subtitle'       => $v9_program['cta']['subtitle'],
				'phone'          => $cta_phone,
				'phone_hint'     => '',
				'button_label'   => $v9_program['cta']['button_label'],
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
