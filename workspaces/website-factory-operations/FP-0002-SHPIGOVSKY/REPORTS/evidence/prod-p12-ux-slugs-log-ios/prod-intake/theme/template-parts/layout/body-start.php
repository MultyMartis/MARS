<?php
/**
 * Body start — site page shell wrapper + global decorative lifebuoy layer (V9-06E57).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$fp02_lifebuoy_uri = SHPIGOVSKY_THEME_URI . '/assets/img/decor/lifebuoy.webp';
?>
<body <?php body_class(); ?><?php do_action( 'shpigovsky_body_attributes' ); ?>>
<?php wp_body_open(); ?>
<div
	class="fp02-lifebuoy-parallax"
	data-fp02-lifebuoy-parallax
	aria-hidden="true"
>
	<img
		class="fp02-lifebuoy-parallax__img"
		src="<?php echo esc_url( $fp02_lifebuoy_uri ); ?>"
		alt=""
		width="1075"
		height="1093"
		decoding="async"
		draggable="false"
	>
</div>
<div class="site-page-shell" data-page-shell>
