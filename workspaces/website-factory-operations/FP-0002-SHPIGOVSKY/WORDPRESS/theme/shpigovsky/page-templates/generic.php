<?php
/**
 * Template Name: Generic Content
 * Route family: placeholder / interim content pages without dedicated Figma layout.
 *
 * V9-06E51: optional ACF page_layout_mode=placeholder renders H1 only
 * (header / nav / footer stay in the theme shell).
 * V9-06E52: full mode content SoT = ACF generic_page_* (see content-page.php).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

$layout_mode = 'full';
if ( function_exists( 'get_field' ) ) {
	$mode = get_field( 'page_layout_mode' );
	if ( is_string( $mode ) && '' !== $mode ) {
		$layout_mode = $mode;
	}
}
?>
<main class="page-plain-content__main<?php echo 'placeholder' === $layout_mode ? ' page-plain-content__main--placeholder' : ''; ?>" id="main-content" data-layout-mode="<?php echo esc_attr( $layout_mode ); ?>">
	<?php
	if ( 'placeholder' === $layout_mode ) {
		while ( have_posts() ) :
			the_post();
			$h1 = get_the_title();
			?>
	<section class="plain-page-content generic-content-page" data-content-status="page-placeholder">
		<div class="container plain-page-content__container">
			<h1 class="plain-page-content__title"><?php echo esc_html( $h1 ); ?></h1>
		</div>
	</section>
			<?php
		endwhile;
	} else {
		shpigovsky_render_breadcrumbs();
		while ( have_posts() ) :
			the_post();
			get_template_part( 'template-parts/generic/content-page' );
		endwhile;
	}
	?>
</main>
<?php
get_footer();
