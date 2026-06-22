<?php
/**
 * Service card component.
 *
 * @package FWS_Synthetic
 *
 * @var array $args {
 *     @type string $title Card title.
 *     @type string $text  Card text.
 *     @type string $url   Card URL.
 * }
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$title = isset( $args['title'] ) ? $args['title'] : '';
$text  = isset( $args['text'] ) ? $args['text'] : '';
$url   = isset( $args['url'] ) ? $args['url'] : '#';
?>
<article class="service-card">
	<h3 class="service-card__title">
		<a href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
	</h3>
	<p class="service-card__text"><?php echo esc_html( $text ); ?></p>
	<a class="service-card__link" href="<?php echo esc_url( $url ); ?>">
		<?php esc_html_e( 'Подробнее', 'fws-synthetic' ); ?>
	</a>
</article>
