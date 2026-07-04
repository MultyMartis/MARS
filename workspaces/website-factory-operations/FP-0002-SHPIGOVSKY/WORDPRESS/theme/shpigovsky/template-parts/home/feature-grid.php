<?php
/**
 * Template part: home/feature-grid.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$advantages = shpigovsky_get_home_repeater( 'home_advantages' );

if ( empty( $advantages ) ) {
	return;
}
?>
<section data-reveal class="home-feature-grid" aria-label="<?php echo esc_attr__( 'Преимущества центра', 'shpigovsky' ); ?>">
	<div class="container">
		<ul class="home-feature-grid__card-grid">
			<?php foreach ( $advantages as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}
				?>
				<li class="home-feature-grid__card">
					<?php if ( '' !== $title ) : ?>
						<h3 class="home-feature-grid__card-title"><?php echo esc_html( $title ); ?></h3>
					<?php endif; ?>
					<?php if ( '' !== $text ) : ?>
						<p class="home-feature-grid__card-text"><?php echo wp_kses_post( $text ); ?></p>
					<?php endif; ?>
				</li>
			<?php endforeach; ?>
		</ul>
	</div>
</section>
