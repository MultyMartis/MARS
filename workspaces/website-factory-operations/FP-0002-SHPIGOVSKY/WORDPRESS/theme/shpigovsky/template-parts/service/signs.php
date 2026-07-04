<?php
/**
 * Template part: service/signs.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$items   = shpigovsky_get_service_repeater( $post_id, 'signs_items' );

if ( empty( $items ) ) {
	return;
}

$heading = __( 'Признаки зависимости', 'shpigovsky' );
?>
<section data-reveal class="service-leaf-signs-v1" id="service-leaf-signs" aria-labelledby="service-leaf-signs-heading">
	<div class="container service-leaf-signs-v1__container">
		<h2 class="service-leaf-signs-v1__heading" id="service-leaf-signs-heading"><?php echo esc_html( $heading ); ?></h2>
		<div class="service-leaf-signs-v1__list-panel">
			<ul class="service-leaf-signs-v1__list">
				<?php foreach ( $items as $item ) : ?>
					<?php
					$text = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';
					$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';

					if ( '' === $text && '' === $title ) {
						continue;
					}

					$list_text = '' !== $text ? $text : $title;
					?>
					<li class="service-leaf-signs-v1__list-item"><?php echo wp_kses_post( $list_text ); ?></li>
				<?php endforeach; ?>
			</ul>
		</div>
	</div>
</section>
