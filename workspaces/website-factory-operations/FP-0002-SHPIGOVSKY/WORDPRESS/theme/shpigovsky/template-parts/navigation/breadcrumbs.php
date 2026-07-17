<?php
/**
 * Breadcrumbs — derived trail boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$trail        = get_query_var( 'shpigovsky_breadcrumb_trail', array() );
$allow_empty  = (bool) get_query_var( 'shpigovsky_breadcrumbs_allow_empty', false );

if ( ( empty( $trail ) || ! is_array( $trail ) ) && ! $allow_empty ) {
	return;
}

if ( ! is_array( $trail ) ) {
	$trail = array();
}
?>
<nav class="breadcrumbs" aria-label="<?php esc_attr_e( 'Хлебные крошки', 'shpigovsky' ); ?>"<?php echo empty( $trail ) ? ' data-breadcrumbs-empty="1"' : ''; ?>>
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
			<li class="breadcrumbs__item<?php echo $last ? ' breadcrumbs__item--current' : ''; ?>"<?php echo $last ? ' aria-current="page"' : ''; ?>>
				<?php if ( ! $last && '' !== $url ) : ?>
					<a class="breadcrumbs__link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $label ); ?></a>
				<?php else : ?>
					<span class="breadcrumbs__current"><?php echo esc_html( $label ); ?></span>
				<?php endif; ?>
			</li>
		<?php endforeach; ?>
	</ol>
</nav>
