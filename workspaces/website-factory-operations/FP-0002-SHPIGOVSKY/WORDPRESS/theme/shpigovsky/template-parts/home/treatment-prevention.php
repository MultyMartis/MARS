<?php
/**
 * Template part: home/treatment-prevention.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$groups = shpigovsky_get_home_service_accordion_groups();

if ( empty( $groups ) ) {
	$nav_fallback = shpigovsky_get_home_nav_accordion_fallback();

	if ( empty( $nav_fallback ) ) {
		return;
	}

	$groups = $nav_fallback;
}

$services_hub_url = home_url( '/uslugi/' );
?>
<section data-reveal class="home-treatment-prevention" aria-labelledby="home-treatment-prevention-heading">
	<div class="container">
		<div class="home-treatment-prevention__head">
			<h2 class="home-treatment-prevention__heading" id="home-treatment-prevention-heading">
				<?php echo esc_html__( 'Лечение и профилактика', 'shpigovsky' ); ?>
			</h2>
			<a class="home-treatment-prevention__all-link" href="<?php echo esc_url( $services_hub_url ); ?>">
				<span class="home-treatment-prevention__all-text"><?php echo esc_html__( 'Смотреть все', 'shpigovsky' ); ?></span>
				<span class="home-treatment-prevention__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<p class="home-treatment-prevention__lead">
			<?php echo esc_html__( 'Мы работаем с зависимостью не как с проступком, а как с состоянием, у которого есть биологические, психологические и социальные причины.', 'shpigovsky' ); ?>
		</p>

		<div class="home-treatment-prevention__accordion" data-accordion>
			<?php foreach ( $groups as $index => $group ) : ?>
				<?php
				$panel_id    = 'home-treatment-prevention-panel-' . ( $index + 1 );
				$trigger_id  = 'home-treatment-prevention-trigger-' . ( $index + 1 );
				$is_expanded = 0 === $index;
				$group_title = isset( $group['title'] ) ? trim( (string) $group['title'] ) : '';
				$items       = isset( $group['items'] ) && is_array( $group['items'] ) ? $group['items'] : array();

				if ( '' === $group_title || empty( $items ) ) {
					continue;
				}
				?>
				<div class="home-treatment-prevention__item" data-accordion-item>
					<h3 class="home-treatment-prevention__item-title">
						<button
							type="button"
							class="home-treatment-prevention__toggle"
							data-accordion-button
							aria-expanded="<?php echo $is_expanded ? 'true' : 'false'; ?>"
							aria-controls="<?php echo esc_attr( $panel_id ); ?>"
							id="<?php echo esc_attr( $trigger_id ); ?>"
						>
							<span class="home-treatment-prevention__toggle-label"><?php echo esc_html( $group_title ); ?></span>
							<span class="home-treatment-prevention__toggle-icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
						</button>
					</h3>
					<div
						class="home-treatment-prevention__panel"
						data-accordion-panel
						id="<?php echo esc_attr( $panel_id ); ?>"
						role="region"
						aria-labelledby="<?php echo esc_attr( $trigger_id ); ?>"
						<?php echo $is_expanded ? '' : 'hidden'; ?>
					>
						<ul class="home-treatment-prevention__service-list">
							<?php foreach ( $items as $item ) : ?>
								<?php
								$item_title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
								$item_url   = isset( $item['url'] ) ? trim( (string) $item['url'] ) : '';
								$item_text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

								if ( '' === $item_title && '' === $item_text ) {
									continue;
								}
								?>
								<li class="home-treatment-prevention__service-list-item">
									<?php if ( '' !== $item_url ) : ?>
										<a class="home-treatment-prevention__service-item" href="<?php echo esc_url( $item_url ); ?>">
											<span class="home-treatment-prevention__service-name"><?php echo esc_html( $item_title ); ?></span>
											<span class="home-treatment-prevention__service-leader" aria-hidden="true"></span>
											<span class="home-treatment-prevention__service-icon" aria-hidden="true"><i class="fas fa-external-link-alt"></i></span>
										</a>
									<?php else : ?>
										<div class="home-treatment-prevention__service-item">
											<?php if ( '' !== $item_title ) : ?>
												<span class="home-treatment-prevention__service-name"><?php echo esc_html( $item_title ); ?></span>
											<?php endif; ?>
											<?php if ( '' !== $item_text ) : ?>
												<p class="home-treatment-prevention__service-text"><?php echo wp_kses_post( $item_text ); ?></p>
											<?php endif; ?>
										</div>
									<?php endif; ?>
								</li>
							<?php endforeach; ?>
						</ul>
					</div>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>
