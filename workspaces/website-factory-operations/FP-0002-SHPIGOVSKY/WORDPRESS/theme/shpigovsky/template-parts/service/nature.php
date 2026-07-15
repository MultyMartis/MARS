<?php
/**
 * Template part: service/nature.php
 *
 * Service subdivision nature block — ACF SoT (V9-06E50). Empty optional text is hidden.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();

$heading = shpigovsky_section_text( $post_id, 'section_nature_heading', '' );
$lead    = shpigovsky_section_text( $post_id, 'section_nature_lead', '' );

$text_blocks = shpigovsky_get_section_nature_text_blocks( $post_id );

$cards = shpigovsky_section_normalize_title_text_rows( shpigovsky_get_section_field_raw( $post_id, 'section_nature_cards' ) );
?>
<section data-reveal class="service-subdivision-nature-v1" id="service-subdivision-nature" aria-labelledby="service-subdivision-nature-heading">
	<div class="container service-subdivision-nature-v1__container">
		<?php if ( '' !== $heading ) : ?>
			<h2 class="service-subdivision-nature-v1__heading" id="service-subdivision-nature-heading"><?php echo esc_html( $heading ); ?></h2>
		<?php else : ?>
			<h2 class="service-subdivision-nature-v1__heading screen-reader-text" id="service-subdivision-nature-heading"><?php esc_html_e( 'Раздел', 'shpigovsky' ); ?></h2>
		<?php endif; ?>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-category-section-v2__lead service-subdivision-nature-v1__lead">
				<?php echo esc_html( $lead ); ?>
			</p>
		<?php endif; ?>

		<?php foreach ( $text_blocks as $block ) : ?>
			<?php
			$block_heading = isset( $block['heading'] ) ? (string) $block['heading'] : '';
			$block_text    = isset( $block['text'] ) ? (string) $block['text'] : '';
			$link_label    = isset( $block['link_label'] ) ? (string) $block['link_label'] : '';
			$link_url      = isset( $block['link_url'] ) ? (string) $block['link_url'] : '';
			$after_text    = isset( $block['after_text'] ) ? (string) $block['after_text'] : '';
			?>
			<div class="service-subdivision-nature-v1__subsection">
				<?php if ( '' !== $block_heading ) : ?>
					<h3 class="service-subdivision-nature-v1__subsection-heading"><?php echo esc_html( $block_heading ); ?></h3>
				<?php endif; ?>
				<?php if ( '' !== $block_text ) : ?>
					<p class="service-subdivision-nature-v1__text">
						<?php echo esc_html( $block_text ); ?>
					</p>
				<?php endif; ?>
				<?php if ( '' !== $link_label && '' !== $link_url ) : ?>
					<p class="service-subdivision-nature-v1__genotyping-link">
						<a class="home-rehabilitation-program__all-link" href="<?php echo esc_url( $link_url ); ?>">
							<span class="home-rehabilitation-program__all-text"><?php echo esc_html( $link_label ); ?></span>
							<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
						</a>
					</p>
				<?php endif; ?>
				<?php if ( '' !== $after_text ) : ?>
					<p class="service-subdivision-nature-v1__text">
						<?php echo esc_html( $after_text ); ?>
					</p>
				<?php endif; ?>
			</div>
		<?php endforeach; ?>

		<?php if ( ! empty( $cards ) ) : ?>
			<ul class="service-subdivision-nature-v1__cards">
				<?php foreach ( $cards as $card ) : ?>
					<li class="home-recovery-intro__card service-subdivision-nature-v1__card">
						<div class="home-recovery-intro__card-head">
							<span class="home-recovery-intro__card-icon" aria-hidden="true"><i class="fas fa-check"></i></span>
							<h3 class="home-recovery-intro__card-title"><?php echo esc_html( $card['title'] ); ?></h3>
						</div>
						<p class="home-recovery-intro__card-text">
							<?php echo esc_html( $card['text'] ); ?>
						</p>
					</li>
				<?php endforeach; ?>
			</ul>
		<?php endif; ?>
	</div>
</section>
