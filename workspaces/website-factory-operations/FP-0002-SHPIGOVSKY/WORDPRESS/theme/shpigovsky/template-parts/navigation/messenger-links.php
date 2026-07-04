<?php
/**
 * Messenger icon links — omitted when social option rows are empty.
 *
 * @package Shpigovsky
 *
 * @var array<string, mixed> $args Template args.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$context = isset( $args['context'] ) ? (string) $args['context'] : 'header';
$rows    = shpigovsky_get_social_link_rows();

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
		$icon = shpigovsky_social_icon_for_label( $row['label'] );
		$label = '' !== $row['label'] ? $row['label'] : __( 'Социальная сеть', 'shpigovsky' );
		?>
		<a class="<?php echo esc_attr( $link_class ); ?>" href="<?php echo esc_url( $row['url'] ); ?>" aria-label="<?php echo esc_attr( $label ); ?>">
			<?php if ( '' !== $icon ) : ?>
				<img class="<?php echo esc_attr( $icon_class ); ?>" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/social/' . $icon ) ); ?>" alt="">
			<?php else : ?>
				<i class="fab fa-youtube" aria-hidden="true"></i>
			<?php endif; ?>
		</a>
	<?php endforeach; ?>
</div>
