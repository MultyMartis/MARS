<?php
/**
 * Template part: components/internal-page-nav.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$trail = get_query_var( 'shpigovsky_breadcrumb_trail', array() );
$items = get_query_var( 'shpigovsky_subnav_items', array() );

if ( empty( $trail ) && empty( $items ) ) {
	return;
}
?>
<div class="internal-page-nav">
	<div class="container">
		<?php if ( ! empty( $trail ) ) : ?>
			<nav class="breadcrumbs" aria-label="<?php esc_attr_e( 'Хлебные крошки', 'shpigovsky' ); ?>">
				<ol class="breadcrumbs__list">
					<?php foreach ( $trail as $index => $crumb ) : ?>
						<?php
						$label = isset( $crumb['label'] ) ? trim( (string) $crumb['label'] ) : '';
						$url   = isset( $crumb['url'] ) ? trim( (string) $crumb['url'] ) : '';
						$last  = $index === count( $trail ) - 1;

						if ( '' === $label ) {
							continue;
						}
						?>
						<li class="breadcrumbs__item">
							<?php if ( ! $last && '' !== $url ) : ?>
								<a class="breadcrumbs__link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $label ); ?></a>
							<?php else : ?>
								<span class="breadcrumbs__current" aria-current="page"><?php echo esc_html( $label ); ?></span>
							<?php endif; ?>
						</li>
					<?php endforeach; ?>
				</ol>
			</nav>
		<?php endif; ?>

		<?php if ( ! empty( $items ) ) : ?>
			<nav class="services-page-subnav" aria-label="<?php esc_attr_e( 'Разделы страницы услуг', 'shpigovsky' ); ?>">
				<ul class="services-page-subnav__list">
					<?php foreach ( $items as $item ) : ?>
						<?php
						$id    = isset( $item['id'] ) ? trim( (string) $item['id'] ) : '';
						$label = isset( $item['label'] ) ? trim( (string) $item['label'] ) : '';

						if ( '' === $id || '' === $label ) {
							continue;
						}
						?>
						<li class="services-page-subnav__item">
							<a class="services-page-subnav__link" href="#<?php echo esc_attr( $id ); ?>"><?php echo esc_html( $label ); ?></a>
						</li>
					<?php endforeach; ?>
				</ul>
			</nav>
		<?php endif; ?>
	</div>
</div>
