<?php

/**

 * Template part: institutional/clinic-landscape.php

 *

 * @package Shpigovsky

 */



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



if ( ! shpigovsky_is_about_hub_page() ) {

	return;

}



$page_id = (int) get_queried_object_id();

$context = shpigovsky_get_about_clinic_landscape_context( $page_id );

?>

<section data-reveal class="clinic-landscape" aria-label="<?php esc_attr_e( 'Территория клиники', 'shpigovsky' ); ?>">

	<div class="container">

		<div class="clinic-landscape__bleed">

			<img

				class="clinic-landscape__image"

				src="<?php echo esc_url( $context['image'] ); ?>"

				width="<?php echo (int) $context['width']; ?>"

				height="<?php echo (int) $context['height']; ?>"

				alt="<?php echo esc_attr( $context['alt'] ); ?>"

				loading="lazy"

				decoding="async"

			>

		</div>

	</div>

</section>


