<?php
/**
 * Blog archive — posts page at /blog/.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-blog__main" id="main-content">
	<div class="blog-page__breadcrumbs">
		<div class="container">
			<?php
			$trail = shpigovsky_get_blog_breadcrumb_trail();
			?>
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
		</div>
	</div>
	<?php
	get_template_part( 'template-parts/blog/archive-list' );
	get_template_part( 'template-parts/blog/lower-stack' );
	?>
</main>
<?php
get_footer();
