<?php
/**
 * Template part: home/articles-teaser.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_get_home_bool( 'home_blog_teaser_enabled' ) ) {
	return;
}

$posts = get_posts(
	array(
		'post_type'      => 'post',
		'post_status'    => 'publish',
		'posts_per_page' => 3,
		'orderby'        => 'date',
		'order'          => 'DESC',
		'no_found_rows'  => true,
	)
);

if ( empty( $posts ) ) {
	return;
}

$blog_url = get_post_type_archive_link( 'post' );

if ( ! is_string( $blog_url ) || '' === $blog_url ) {
	$blog_url = home_url( '/blog/' );
}
?>
<section class="home-articles" aria-labelledby="home-articles-heading">
	<div class="container">
		<div class="home-articles__head">
			<h2 class="home-articles__heading" id="home-articles-heading">
				<?php echo esc_html__( 'Статьи', 'shpigovsky' ); ?>
			</h2>
			<a class="home-articles__all-link" href="<?php echo esc_url( $blog_url ); ?>">
				<span class="home-articles__all-text"><?php echo esc_html__( 'все статьи', 'shpigovsky' ); ?></span>
				<span class="home-articles__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<div class="home-articles__grid" data-reveal-group>
			<?php foreach ( $posts as $post ) : ?>
				<?php
				if ( ! $post instanceof WP_Post ) {
					continue;
				}

				$permalink = get_permalink( $post );
				$thumb_id  = get_post_thumbnail_id( $post );
				$thumb_url = $thumb_id ? wp_get_attachment_image_url( $thumb_id, 'large' ) : '';
				?>
				<article class="home-articles__card" data-reveal>
					<a class="home-articles__card-link" href="<?php echo esc_url( $permalink ); ?>">
						<?php if ( is_string( $thumb_url ) && '' !== $thumb_url ) : ?>
							<img
								class="home-articles__image"
								src="<?php echo esc_url( $thumb_url ); ?>"
								alt=""
								loading="lazy"
								decoding="async"
							>
						<?php endif; ?>
						<h3 class="home-articles__title"><?php echo esc_html( get_the_title( $post ) ); ?></h3>
						<p class="home-articles__meta"><?php echo esc_html__( 'Читать', 'shpigovsky' ); ?></p>
					</a>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>
