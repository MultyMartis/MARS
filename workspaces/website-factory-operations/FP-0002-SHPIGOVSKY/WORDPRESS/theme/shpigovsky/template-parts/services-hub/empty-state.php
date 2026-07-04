<?php
/**
 * Template part: services-hub/empty-state.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_get_services_hub_bool( 'services_hub_show_placeholders' ) ) {
	return;
}
?>
<section class="services-hub-empty-state" aria-live="polite">
	<div class="container">
		<p class="services-hub-empty-state__text">
			<?php echo esc_html__( 'Раздел услуг будет доступен после наполнения каталога.', 'shpigovsky' ); ?>
		</p>
	</div>
</section>
