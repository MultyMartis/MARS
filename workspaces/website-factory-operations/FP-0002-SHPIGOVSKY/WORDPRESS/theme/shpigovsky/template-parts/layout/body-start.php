<?php
/**
 * Body start — site page shell wrapper.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<body <?php body_class(); ?><?php do_action( 'shpigovsky_body_attributes' ); ?>>
<?php wp_body_open(); ?>
<div class="site-page-shell" data-page-shell>
