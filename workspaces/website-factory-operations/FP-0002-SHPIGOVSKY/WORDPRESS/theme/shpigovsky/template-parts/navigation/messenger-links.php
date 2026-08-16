<?php
/**
 * Messenger icon links — canonical social_platforms SoT (PROD-P13).
 *
 * @package Shpigovsky
 *
 * @var array<string, mixed> $args Template args.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$context = isset( $args['context'] ) ? (string) $args['context'] : 'header';
$rows    = shpigovsky_get_messenger_link_rows( $context );

if ( empty( $rows ) ) {
	return;
}

$wrapper_class = 'offcanvas' === $context || 'mobile-header' === $context ? 'offcanvas__messengers' : 'site-header__messengers';
$link_class    = 'offcanvas' === $context || 'mobile-header' === $context ? 'offcanvas__messenger-link' : 'site-header__messenger-link';
$icon_class    = 'offcanvas' === $context || 'mobile-header' === $context ? 'offcanvas__messenger-icon' : 'site-header__messenger-icon';

if ( 'mobile-header' === $context ) {
	$wrapper_class = 'mobile-header__messengers';
}
?>
<div class="<?php echo esc_attr( $wrapper_class ); ?>">
	<?php foreach ( $rows as $row ) : ?>
		<?php
		$icon  = isset( $row['icon'] ) ? (string) $row['icon'] : '';
		$label = isset( $row['label'] ) ? (string) $row['label'] : '';
		$type  = isset( $row['type'] ) ? (string) $row['type'] : '';
		$is_fa = 'youtube' === $type;
		?>
		<a class="<?php echo esc_attr( $link_class ); ?>" href="<?php echo esc_url( $row['url'] ); ?>" aria-label="<?php echo esc_attr( $label ); ?>">
			<?php if ( $is_fa ) : ?>
				<i class="fab fa-youtube" aria-hidden="true"></i>
			<?php elseif ( '' !== $icon ) : ?>
				<img class="<?php echo esc_attr( $icon_class ); ?>" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/social/' . $icon ) ); ?>" alt="">
			<?php else : ?>
				<span class="site-header__messenger-fallback"><?php echo esc_html( $label ); ?></span>
			<?php endif; ?>
		</a>
	<?php endforeach; ?>
</div>
