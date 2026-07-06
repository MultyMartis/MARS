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
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( 'alcohol-special' === $variant ) {
	$v9        = shpigovsky_get_v9_alcohol_signs_copy();
	$heading   = $v9['heading'];
	$intro     = $v9['intro'];
	$list_items = $v9['items'];
	$editorial = $v9['editorial'];
} else {
	$items = shpigovsky_get_service_repeater( $post_id, 'signs_items' );

	if ( empty( $items ) ) {
		return;
	}

	$heading    = __( 'Признаки зависимости', 'shpigovsky' );
	$intro      = '';
	$list_items = array();
	$editorial  = '';

	foreach ( $items as $item ) {
		$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';
		$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';

		if ( '' === $text && '' === $title ) {
			continue;
		}

		$list_items[] = '' !== $text ? $text : $title;
	}
}
?>
<section data-reveal class="service-leaf-signs-v1" id="service-leaf-signs" aria-labelledby="service-leaf-signs-heading">
	<div class="container service-leaf-signs-v1__container">
		<h2 class="service-leaf-signs-v1__heading" id="service-leaf-signs-heading"><?php echo esc_html( $heading ); ?></h2>
		<?php if ( '' !== $intro ) : ?>
			<p class="service-leaf-signs-v1__intro"><?php echo esc_html( $intro ); ?></p>
		<?php endif; ?>
		<div class="service-leaf-signs-v1__list-panel">
			<ul class="service-leaf-signs-v1__list">
				<?php foreach ( $list_items as $list_text ) : ?>
					<li class="service-leaf-signs-v1__list-item"><?php echo wp_kses_post( $list_text ); ?></li>
				<?php endforeach; ?>
			</ul>
		</div>
		<?php if ( '' !== $editorial ) : ?>
			<p class="service-leaf-signs-v1__editorial"><?php echo esc_html( $editorial ); ?></p>
			<p class="service-leaf-signs-v1__read-more"><?php echo esc_html__( 'Читать больше', 'shpigovsky' ); ?></p>
		<?php endif; ?>
	</div>
</section>
