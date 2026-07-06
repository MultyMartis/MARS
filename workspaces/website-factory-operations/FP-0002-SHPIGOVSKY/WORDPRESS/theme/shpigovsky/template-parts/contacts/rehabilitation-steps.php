<?php
/**
 * Template part: contacts/rehabilitation-steps.php
 *
 * V9 contacts-rehabilitation-steps section with static structure and CTA band.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$steps         = shpigovsky_get_contacts_rehabilitation_steps();
$support_items = shpigovsky_get_contacts_support_items();
$cta_band      = shpigovsky_get_contacts_cta_band();
?>
<section data-reveal class="contacts-rehabilitation-steps" aria-labelledby="contacts-rehabilitation-steps-heading">
	<div class="container contacts-rehabilitation-steps__container">
		<h2 class="contacts-rehabilitation-steps__heading" id="contacts-rehabilitation-steps-heading">
			<?php echo esc_html__( 'Сделайте шаг к выздоровлению — мы поможем', 'shpigovsky' ); ?>
		</h2>
		<p class="contacts-rehabilitation-steps__lead block-whith-red-line">
			<?php echo esc_html__( 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'shpigovsky' ); ?>
		</p>

		<ol class="home-rehabilitation-requirements__steps contacts-rehabilitation-steps__steps">
			<?php foreach ( $steps as $step ) : ?>
				<li class="home-rehabilitation-requirements__step">
					<span class="home-rehabilitation-requirements__step-number" aria-hidden="true"><?php echo esc_html( $step['number'] ); ?></span>
					<div class="home-rehabilitation-requirements__step-body">
						<h3 class="home-rehabilitation-requirements__step-title"><?php echo esc_html( $step['title'] ); ?></h3>
						<p class="home-rehabilitation-requirements__step-text"><?php echo esc_html( $step['text'] ); ?></p>
					</div>
				</li>
			<?php endforeach; ?>
		</ol>

		<div class="contacts-rehabilitation-steps__cta-wrap">
			<div class="contacts-rehabilitation-steps__decor" aria-hidden="true"></div>
			<?php
			set_query_var( 'shpigovsky_program_cta_band', $cta_band );
			get_template_part( 'template-parts/components/program-cta-band' );
			?>
		</div>

		<?php if ( ! empty( $support_items ) ) : ?>
			<div class="home-rehabilitation-requirements__support contacts-rehabilitation-steps__support">
				<p class="home-rehabilitation-requirements__support-heading">
					<?php echo esc_html__( 'Поддержка осуществляется на всех этапах:', 'shpigovsky' ); ?>
				</p>
				<ul class="home-rehabilitation-requirements__support-list">
					<?php foreach ( $support_items as $item ) : ?>
						<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html( $item ); ?></li>
					<?php endforeach; ?>
				</ul>
			</div>
		<?php endif; ?>

		<div class="home-rehabilitation-requirements__photo-bleed contacts-rehabilitation-steps__photo-bleed">
			<img
				class="home-rehabilitation-requirements__photo contacts-rehabilitation-steps__photo"
				src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/contacts/contacts-rehabilitation-interior.png' ) ); ?>"
				width="1170"
				height="580"
				alt="<?php esc_attr_e( 'Интерьер клиники', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>
	</div>
</section>
