<?php
/**
 * Front page — foundation placeholder.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-foundation shpigovsky-foundation--front" id="main-content">
	<div class="shpigovsky-foundation__inner">
		<h1><?php esc_html_e( 'FP-0002 LOCAL WORDPRESS FOUNDATION', 'shpigovsky' ); ?></h1>
		<p><?php esc_html_e( 'Frontend integration has not started.', 'shpigovsky' ); ?></p>
	</div>
</main>
<?php
get_footer();
