<?php
/**
 * Footer social links — canonical social_platforms SoT (PROD-P13).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$rows = shpigovsky_get_social_platform_rows( 'footer' );

if ( empty( $rows ) ) {
	return;
}
?>
<div class="site-footer__social">
	<?php foreach ( $rows as $row ) : ?>
		<?php
		$icon  = isset( $row['icon'] ) ? (string) $row['icon'] : '';
		$label = isset( $row['label'] ) ? (string) $row['label'] : '';
		$type  = isset( $row['type'] ) ? (string) $row['type'] : '';
		$is_fa = 'youtube' === $type || ( '' === $icon && str_contains( mb_strtolower( $label ), 'youtube' ) );
		?>
		<a class="site-footer__social-link<?php echo $is_fa ? ' site-footer__social-link--fa' : ''; ?>" href="<?php echo esc_url( $row['url'] ); ?>" aria-label="<?php echo esc_attr( $label ); ?>">
			<?php if ( $is_fa ) : ?>
				<i class="fab fa-youtube site-footer__social-fa" aria-hidden="true"></i>
			<?php elseif ( '' !== $icon ) : ?>
				<img class="site-footer__social-icon" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/social/' . $icon ) ); ?>" alt="">
			<?php else : ?>
				<span class="site-footer__social-fallback"><?php echo esc_html( $label ); ?></span>
			<?php endif; ?>
		</a>
	<?php endforeach; ?>
</div>
