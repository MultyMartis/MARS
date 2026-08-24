<?php
/**
 * Template part: specialist/hub-content.php
 *
 * Specialists Hub page shell: optional ACF intro/body, specialist listing,
 * then the same Page-owned reusable blocks as Generic Content.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$page_id        = (int) get_the_ID();
$lead           = '';
$body           = '';
$content_source = 'empty';

if ( function_exists( 'get_field' ) ) {
	$lead_raw = get_field( 'generic_page_lead', $page_id );
	$body_raw = get_field( 'generic_page_body', $page_id );
	$lead     = is_string( $lead_raw ) ? trim( $lead_raw ) : '';
	$body     = is_string( $body_raw ) ? trim( $body_raw ) : '';
	if ( '' !== $body || '' !== $lead ) {
		$content_source = 'acf';
	}
}

?>
<section class="plain-page-content specialists-hub" data-content-status="specialists-hub" data-content-source="<?php echo esc_attr( $content_source ); ?>">
	<div class="container plain-page-content__container">
		<h1 class="plain-page-content__title"><?php the_title(); ?></h1>

		<?php if ( '' !== $lead || '' !== $body ) : ?>
		<div class="plain-page-content__body">
			<?php if ( '' !== $lead ) : ?>
			<p class="generic-content-page__lead"><?php echo nl2br( esc_html( $lead ) ); ?></p>
			<?php endif; ?>
			<?php
			if ( '' !== $body ) {
				echo apply_filters( 'the_content', $body ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- WP content filters.
			}
			?>
		</div>
		<?php endif; ?>

		<?php get_template_part( 'template-parts/specialist/hub-list' ); ?>

		<?php
		$reusable = array();
		if ( function_exists( 'get_field' ) ) {
			$raw_reusable = get_field( 'generic_page_reusable_blocks', $page_id );
			if ( is_array( $raw_reusable ) ) {
				foreach ( $raw_reusable as $item ) {
					$key = is_string( $item ) ? trim( $item ) : '';
					if ( '' !== $key ) {
						$reusable[] = $key;
					}
				}
			}
		}

		// Fixed render order — same owner/storage as Generic Content (PROD-P07).
		$order    = array( 'rehab_requirements', 'about_home' );
		$selected = array_values( array_intersect( $order, $reusable ) );
		if ( ! empty( $selected ) ) :
			?>
		<div class="generic-content-page__reusable">
			<?php
			foreach ( $selected as $block_key ) {
				if ( 'rehab_requirements' === $block_key ) {
					get_template_part( 'template-parts/home/rehabilitation-requirements' );
				} elseif ( 'about_home' === $block_key ) {
					get_template_part(
						'template-parts/home/comfort',
						null,
						array(
							'section_id' => 'specialists-hub-about-home',
							'heading_id' => 'specialists-hub-about-home-heading',
						)
					);
				}
			}
			?>
		</div>
			<?php
		endif;
		?>
	</div>
</section>
