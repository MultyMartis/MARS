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

if ( shpigovsky_is_service_general_variant( $variant ) ) {
	$v9 = function_exists( 'shpigovsky_get_general_signs_copy' )
		? shpigovsky_get_general_signs_copy( $post_id )
		: null;

	if ( ! is_array( $v9 ) || empty( $v9['items'] ) ) {
		return;
	}

	$heading    = (string) ( $v9['heading'] ?? '' );
	$intro      = (string) ( $v9['intro'] ?? '' );
	$list_items = isset( $v9['items'] ) && is_array( $v9['items'] ) ? $v9['items'] : array();
	$editorial  = (string) ( $v9['editorial'] ?? '' );
} else {
	$items = shpigovsky_get_service_repeater( $post_id, 'signs_items' );

	if ( empty( $items ) ) {
		return;
	}

	$heading     = __( 'Признаки зависимости', 'shpigovsky' );
	$intro       = '';
	$list_items  = array();
	$editorial   = '';

	foreach ( $items as $item ) {
		$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';
		$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';

		if ( '' === $text && '' === $title ) {
			continue;
		}

		$list_items[] = '' !== $text ? $text : $title;
	}

	if ( empty( $list_items ) ) {
		return;
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
			<p class="service-leaf-signs-v1__editorial" id="service-leaf-signs-editorial"><?php echo esc_html( $editorial ); ?></p>
			<button
				type="button"
				class="service-leaf-signs-v1__read-more"
				aria-controls="service-leaf-signs-editorial"
				aria-expanded="false"
				hidden
			><?php echo esc_html__( 'Читать больше', 'shpigovsky' ); ?></button>
		<?php endif; ?>
	</div>
</section>
