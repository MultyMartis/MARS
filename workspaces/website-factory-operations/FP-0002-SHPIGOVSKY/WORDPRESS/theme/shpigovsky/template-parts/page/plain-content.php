<?php
/**
 * Plain page content wrapper — native editor output boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<div class="shpigovsky-skeleton__content">
	<?php the_content(); ?>
</div>
