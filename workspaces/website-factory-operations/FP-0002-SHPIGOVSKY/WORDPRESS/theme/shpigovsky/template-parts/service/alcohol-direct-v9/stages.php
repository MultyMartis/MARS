<?php
/**
 * Service-leaf stages — ACF SoT (V9-06E47); visual parity with usluga-konechnaya-v1.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$v9      = function_exists( 'shpigovsky_get_general_stages_copy' )
	? shpigovsky_get_general_stages_copy( $post_id )
	: null;

if ( ! is_array( $v9 ) || empty( $v9['steps'] ) ) {
	return;
}

$phone = shpigovsky_get_site_option( 'phone_primary' );
$phone = '' !== $phone ? $phone : '8 (925) 183-64-64';
?>
<section data-reveal class="service-leaf-stages-v1" id="service-leaf-start" aria-labelledby="service-leaf-start-heading">
	<div class="container service-leaf-stages-v1__container">
		<h2 class="service-leaf-stages-v1__heading" id="service-leaf-start-heading"><?php echo esc_html( $v9['heading'] ); ?></h2>
		<?php if ( ! empty( $v9['lead'] ) ) : ?>
			<p class="service-leaf-stages-v1__lead block-whith-red-line"><?php echo esc_html( $v9['lead'] ); ?></p>
		<?php endif; ?>

		<ol class="home-rehabilitation-requirements__steps service-leaf-stages-v1__steps">
			<?php foreach ( $v9['steps'] as $index => $step ) : ?>
				<?php $number = str_pad( (string) ( $index + 1 ), 2, '0', STR_PAD_LEFT ); ?>
				<li class="home-rehabilitation-requirements__step">
					<span class="home-rehabilitation-requirements__step-number" aria-hidden="true"><?php echo esc_html( $number ); ?></span>
					<div class="home-rehabilitation-requirements__step-body">
						<h3 class="home-rehabilitation-requirements__step-title"><?php echo esc_html( $step['title'] ); ?></h3>
						<p class="home-rehabilitation-requirements__step-text"><?php echo esc_html( $step['text'] ); ?></p>
					</div>
				</li>
			<?php endforeach; ?>
		</ol>

		<div class="service-leaf-stages-v1__cta">
			<?php
			$guest_cta = function_exists( 'shpigovsky_get_about_guest_cta_band' )
				? shpigovsky_get_about_guest_cta_band( 'service-leaf-stages-cta-v1' )
				: array(
					'title'        => 'Запишитесь на гостевой визит',
					'subtitle'     => 'Вы сможете все посмотреть и задать вопросы лично',
					'phone'        => $phone,
					'phone_hint'   => 'Или позвоните нам',
					'button_label' => 'Записаться',
					'source'       => 'service-leaf-stages-cta-v1',
				);
			set_query_var(
				'shpigovsky_program_cta_band',
				array_merge(
					$guest_cta,
					array(
						'section_id'     => '',
						'heading_id'     => '',
						'heading_text'   => '',
						'wrap_section'   => false,
						'wrap_container' => false,
						'button_first'   => true,
						'margin_flush'   => true,
					)
				)
			);
			get_template_part( 'template-parts/components/program-cta-band' );
			?>
		</div>

		<?php if ( ! empty( $v9['support_heading'] ) || ! empty( $v9['support_items'] ) ) : ?>
			<div class="home-rehabilitation-requirements__support service-leaf-stages-v1__support">
				<?php if ( ! empty( $v9['support_heading'] ) ) : ?>
					<p class="home-rehabilitation-requirements__support-heading"><?php echo esc_html( $v9['support_heading'] ); ?></p>
				<?php endif; ?>
				<?php if ( ! empty( $v9['support_items'] ) ) : ?>
					<ul class="home-rehabilitation-requirements__support-list">
						<?php foreach ( $v9['support_items'] as $item ) : ?>
							<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html( $item ); ?></li>
						<?php endforeach; ?>
					</ul>
				<?php endif; ?>
			</div>
		<?php endif; ?>
	</div>
</section>
