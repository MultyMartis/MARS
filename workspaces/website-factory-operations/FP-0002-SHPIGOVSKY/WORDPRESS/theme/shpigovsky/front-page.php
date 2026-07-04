<?php
/**
 * Front page — home section orchestration boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

get_template_part( 'template-parts/home/hero' );

if ( is_front_page() ) {
	echo '</div>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped — closes .intro-section opened in layout/header.php
}
?>
<main class="site-main site-main--front" id="main-content">
	<?php
	get_template_part( 'template-parts/home/feature-grid' );
	get_template_part( 'template-parts/home/treatment-prevention' );
	get_template_part( 'template-parts/home/rehabilitation-program' );
	get_template_part( 'template-parts/home/gallery' );
	get_template_part( 'template-parts/home/articles-teaser' );
	get_template_part( 'template-parts/home/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</main>
<?php
get_footer();
