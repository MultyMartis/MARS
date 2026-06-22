<?php
/**
 * FAQ accordion section.
 *
 * @package FWS_Synthetic
 *
 * @var array $args {
 *     @type string $faq_id  Unique accordion root id.
 *     @type int    $post_id Post ID for field source.
 * }
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$faq_id       = isset( $args['faq_id'] ) ? sanitize_html_class( $args['faq_id'] ) : 'faq';
$field_post_id = isset( $args['post_id'] ) ? (int) $args['post_id'] : get_queried_object_id();

$defaults = array(
	array(
		'q' => __( 'Что это за проект?', 'fws-synthetic' ),
		'a' => __( 'Это синтетический демонстрационный проект для валидации Forge WordPress без клиентских данных.', 'fws-synthetic' ),
	),
	array(
		'q' => __( 'Используются ли реальные услуги?', 'fws-synthetic' ),
		'a' => __( 'Нет. Все услуги и тексты искусственные: «Тестовая услуга», «Демонстрационный проект».', 'fws-synthetic' ),
	),
	array(
		'q' => __( 'Есть ли production target?', 'fws-synthetic' ),
		'a' => __( 'Нет. WPilot handoff выполняется только в режиме simulation.', 'fws-synthetic' ),
	),
);

$items = array();
for ( $i = 1; $i <= 3; $i++ ) {
	$question = fws_get_field( 'faq_q' . $i, $field_post_id, $defaults[ $i - 1 ]['q'] );
	$answer   = fws_get_field( 'faq_a' . $i, $field_post_id, $defaults[ $i - 1 ]['a'] );

	if ( '' === trim( $question ) && '' === trim( $answer ) ) {
		continue;
	}

	$items[] = array(
		'q' => $question,
		'a' => $answer,
	);
}

if ( empty( $items ) ) {
	$items = $defaults;
}
?>
<section class="faq" data-accordion="<?php echo esc_attr( $faq_id ); ?>">
	<div class="container">
		<h2 class="section-title"><?php esc_html_e( 'Частые вопросы', 'fws-synthetic' ); ?></h2>
		<div class="faq__list">
			<?php foreach ( $items as $index => $item ) : ?>
				<?php
				$panel_id = $faq_id . '-q' . ( $index + 1 );
				?>
			<div class="faq__item" data-accordion-item>
				<button
					class="faq__button"
					type="button"
					data-accordion-button
					aria-expanded="false"
					aria-controls="<?php echo esc_attr( $panel_id ); ?>"
				>
					<?php echo esc_html( $item['q'] ); ?>
				</button>
				<div class="faq__panel" id="<?php echo esc_attr( $panel_id ); ?>" data-accordion-panel hidden>
					<p><?php echo esc_html( $item['a'] ); ?></p>
				</div>
			</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>
