<?php
/**
 * Template part: generic/content-page.php
 * V9-06E29C — neutral content shell (legal layout family, without legal demo chrome).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<section class="plain-page-content generic-content-page" data-content-status="generic-interim-page">
	<div class="container plain-page-content__container">
		<h1 class="plain-page-content__title"><?php the_title(); ?></h1>
		<?php
		$page_id             = (int) get_the_ID();
		$parent_id           = (int) wp_get_post_parent_id( $page_id );
		$specialists_parent  = function_exists( 'shpigovsky_get_specialists_parent_page_id' ) ? (int) shpigovsky_get_specialists_parent_page_id() : 0;
		$is_specialist_child = $specialists_parent > 0 && $parent_id === $specialists_parent;
		$thumb_id            = $is_specialist_child ? (int) get_post_thumbnail_id( $page_id ) : 0;

		if ( $is_specialist_child ) {
			$photo_url    = '';
			$photo_width  = 640;
			$photo_height = 640;
			$photo_alt    = get_the_title( $page_id );

			if ( $thumb_id > 0 ) {
				$src = wp_get_attachment_image_src( $thumb_id, 'large' );
				if ( is_array( $src ) && ! empty( $src[0] ) ) {
					$photo_url    = (string) $src[0];
					$photo_width  = ! empty( $src[1] ) ? (int) $src[1] : $photo_width;
					$photo_height = ! empty( $src[2] ) ? (int) $src[2] : $photo_height;
				}
			}

			if ( '' === $photo_url && function_exists( 'shpigovsky_get_specialist_placeholder_image' ) ) {
				$placeholder  = shpigovsky_get_specialist_placeholder_image();
				$photo_url    = (string) $placeholder['url'];
				$photo_width  = (int) $placeholder['width'];
				$photo_height = (int) $placeholder['height'];
			}

			if ( '' !== $photo_url ) :
				?>
		<figure class="generic-content-page__specialist-photo">
			<img
				src="<?php echo esc_url( $photo_url ); ?>"
				width="<?php echo esc_attr( (string) $photo_width ); ?>"
				height="<?php echo esc_attr( (string) $photo_height ); ?>"
				alt="<?php echo esc_attr( $photo_alt ); ?>"
				loading="eager"
				decoding="async"
			>
		</figure>
				<?php
			endif;
		}
		?>
		<div class="plain-page-content__body">
			<?php
			if ( trim( (string) get_the_content() ) !== '' ) {
				the_content();
			} else {
				echo '<p>' . esc_html__( 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.', 'shpigovsky' ) . '</p>';
			}
			?>
		</div>
	</div>
</section>
