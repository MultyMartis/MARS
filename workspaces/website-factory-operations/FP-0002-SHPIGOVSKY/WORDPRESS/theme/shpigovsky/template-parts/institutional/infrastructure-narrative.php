<?php
/**
 * Template part: institutional/infrastructure-narrative.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_is_about_hub_page() ) {
	return;
}

$page_id  = (int) get_queried_object_id();
$context  = shpigovsky_get_about_infrastructure_context( $page_id );
$groups   = isset( $context['groups'] ) ? $context['groups'] : array();
$g5_items = isset( $context['comfort_gallery'] ) ? $context['comfort_gallery'] : array();
$fb_group = isset( $context['fancybox_group'] ) ? (string) $context['fancybox_group'] : 'o-centre-infrastructure';
?>
<section data-reveal class="infrastructure-narrative" id="our-home" aria-labelledby="infrastructure-narrative-heading">
	<div class="container infrastructure-narrative__container">
		<?php if ( isset( $groups['g0'] ) ) : ?>
			<div class="infrastructure-narrative__group infrastructure-narrative__group--intro" data-inf-group="g0">
				<header class="infrastructure-narrative__head">
					<h2 class="infrastructure-narrative__heading" id="infrastructure-narrative-heading"><?php echo esc_html( $groups['g0']['heading'] ); ?></h2>
				</header>
				<p class="infrastructure-narrative__lead block-whith-red-line"><?php echo esc_html( $groups['g0']['lead'] ); ?></p>
				<?php if ( ! empty( $groups['g0']['bullet_intro'] ) ) : ?>
					<p class="infrastructure-narrative__bullet"><span><?php echo esc_html( $groups['g0']['bullet_intro'] ); ?></span></p>
				<?php endif; ?>
			</div>
		<?php endif; ?>

		<?php foreach ( array( 'g1', 'g2', 'g3', 'g4' ) as $group_key ) : ?>
			<?php
			if ( ! isset( $groups[ $group_key ] ) ) {
				continue;
			}

			$group = $groups[ $group_key ];
			?>
			<div class="infrastructure-narrative__group infrastructure-narrative__group--<?php echo esc_attr( $group_key ); ?>" data-inf-group="<?php echo esc_attr( $group_key ); ?>">
				<?php if ( ! empty( $group['gallery'] ) ) : ?>
					<div class="infrastructure-narrative__subgallery infrastructure-narrative__subgallery--row-3 swiper" data-inf-slider>
						<div class="infrastructure-narrative__subgallery-wrapper swiper-wrapper">
							<?php foreach ( $group['gallery'] as $image ) : ?>
								<?php
								$src = shpigovsky_asset_uri( (string) $image['src'] );
								?>
								<figure class="infrastructure-narrative__figure swiper-slide">
									<a href="<?php echo esc_url( $src ); ?>" data-fancybox="<?php echo esc_attr( $fb_group ); ?>">
										<img
											class="infrastructure-narrative__image"
											src="<?php echo esc_url( $src ); ?>"
											width="<?php echo (int) $image['width']; ?>"
											height="<?php echo (int) $image['height']; ?>"
											alt="<?php echo esc_attr( (string) $image['alt'] ); ?>"
											loading="lazy"
											decoding="async"
										>
									</a>
								</figure>
							<?php endforeach; ?>
						</div>
					</div>
				<?php endif; ?>
				<?php if ( ! empty( $group['bullet'] ) ) : ?>
					<p class="infrastructure-narrative__bullet"><span><?php echo esc_html( $group['bullet'] ); ?></span></p>
				<?php endif; ?>
			</div>
		<?php endforeach; ?>

		<?php if ( ! empty( $g5_items ) ) : ?>
			<div class="infrastructure-narrative__group infrastructure-narrative__group--g5" data-inf-group="g5">
				<div class="comfort__gallery-stage">
					<div class="comfort__gallery-decor" aria-hidden="true">
						<img
							class="comfort__gallery-decor-image"
							src="<?php echo esc_url( shpigovsky_asset_uri( 'img/branding/logo.svg' ) ); ?>"
							width="auto"
							height="auto"
							alt=""
							loading="lazy"
							decoding="async"
						>
					</div>
					<div class="comfort__gallery">
						<?php
						$wide_indexes = array( 0, 5 );
						foreach ( $g5_items as $index => $image ) :
							$src         = shpigovsky_asset_uri( (string) $image['src'] );
							$item_class  = 'comfort__gallery-item';
							$item_class .= in_array( $index, $wide_indexes, true ) ? ' comfort__gallery-item--wide' : '';
							?>
							<a class="<?php echo esc_attr( $item_class ); ?>" href="<?php echo esc_url( $src ); ?>" data-fancybox="<?php echo esc_attr( $fb_group ); ?>-g5">
								<img
									class="comfort__gallery-image"
									src="<?php echo esc_url( $src ); ?>"
									width="<?php echo (int) $image['width']; ?>"
									height="<?php echo (int) $image['height']; ?>"
									alt="<?php echo esc_attr( (string) $image['alt'] ); ?>"
									loading="lazy"
									decoding="async"
								>
							</a>
						<?php endforeach; ?>
					</div>
				</div>
			</div>
		<?php endif; ?>
	</div>
</section>
