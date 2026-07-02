<?php
/**
 * 404 template.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--404" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<h1><?php esc_html_e( 'Страница не найдена', 'shpigovsky' ); ?></h1>
	<p><?php esc_html_e( 'Запрошенная страница недоступна.', 'shpigovsky' ); ?></p>
</main>
<?php
get_footer();
