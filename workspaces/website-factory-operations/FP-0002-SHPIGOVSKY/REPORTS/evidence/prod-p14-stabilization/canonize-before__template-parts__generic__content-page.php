<?php

/**

 * Template part: generic/content-page.php

 * V9-06E29C — neutral content shell (legal layout family, without legal demo chrome).

 * V9-06E52 — ACF SoT (generic_page_lead / generic_page_body); empty optional fields hide;

 *            hardcoded template demo is not a normal primary source.

 * PROD-P08 — specialist children render structured specialist/profile template.

 *

 * @package Shpigovsky

 */



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



$page_id             = (int) get_the_ID();

$parent_id           = (int) wp_get_post_parent_id( $page_id );

$specialists_parent  = function_exists( 'shpigovsky_get_specialists_parent_page_id' ) ? (int) shpigovsky_get_specialists_parent_page_id() : 0;

$is_specialist_child = $specialists_parent > 0 && $parent_id === $specialists_parent;



if ( $is_specialist_child ) {

	get_template_part( 'template-parts/specialist/profile' );



	$reusable = array();

	if ( function_exists( 'get_field' ) ) {

		$raw_reusable = get_field( 'generic_page_reusable_blocks', $page_id );

		if ( is_array( $raw_reusable ) ) {

			foreach ( $raw_reusable as $item ) {

				$key = is_string( $item ) ? trim( $item ) : '';

				if ( '' !== $key ) {

					$reusable[] = $key;

				}

			}

		}

	}

	$order    = array( 'rehab_requirements', 'about_home' );

	$selected = array_values( array_intersect( $order, $reusable ) );

	if ( ! empty( $selected ) ) :

		?>

		<div class="container generic-content-page__reusable">

			<?php

			foreach ( $selected as $block_key ) {

				if ( 'rehab_requirements' === $block_key ) {

					get_template_part( 'template-parts/home/rehabilitation-requirements' );

				} elseif ( 'about_home' === $block_key ) {

					get_template_part(

						'template-parts/home/comfort',

						null,

						array(

							'section_id' => 'generic-about-home',

							'heading_id' => 'generic-about-home-heading',

						)

					);

				}

			}

			?>

		</div>

		<?php

	endif;

	return;

}



$thumb_id       = 0;

$lead           = '';

$body           = '';

$content_source = 'empty';



if ( function_exists( 'get_field' ) ) {

	$lead_raw = get_field( 'generic_page_lead', $page_id );

	$body_raw = get_field( 'generic_page_body', $page_id );

	$lead     = is_string( $lead_raw ) ? trim( $lead_raw ) : '';

	$body     = is_string( $body_raw ) ? trim( $body_raw ) : '';

	if ( '' !== $body || '' !== $lead ) {

		$content_source = 'acf';

	}

	// Empty ACF optional fields: hide. No hardcoded demo. No post_content inject on normal path.

} else {

	// Technical reserve only when ACF unavailable.

	$pc = trim( (string) get_post_field( 'post_content', $page_id ) );

	if ( '' !== $pc ) {

		$body           = $pc;

		$content_source = 'post_content_emergency_no_acf';

	}

}

?>

<section class="plain-page-content generic-content-page" data-content-status="generic-acf-sot" data-content-source="<?php echo esc_attr( $content_source ); ?>">

	<div class="container plain-page-content__container">

		<h1 class="plain-page-content__title"><?php the_title(); ?></h1>

		<div class="plain-page-content__body">

			<?php if ( '' !== $lead ) : ?>

			<p class="generic-content-page__lead"><?php echo nl2br( esc_html( $lead ) ); ?></p>

			<?php endif; ?>

			<?php

			if ( '' !== $body ) {

				echo apply_filters( 'the_content', $body ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- WP content filters.

			}

			// Empty optional body/lead: hide — no hardcoded demo injection (V9-06E52).

			?>

		</div>

		<?php

		$reusable = array();

		if ( function_exists( 'get_field' ) ) {

			$raw_reusable = get_field( 'generic_page_reusable_blocks', $page_id );

			if ( is_array( $raw_reusable ) ) {

				foreach ( $raw_reusable as $item ) {

					$key = is_string( $item ) ? trim( $item ) : '';

					if ( '' !== $key ) {

						$reusable[] = $key;

					}

				}

			}

		}

		// Fixed render order — page stores selection only (no content duplication).

		$order    = array( 'rehab_requirements', 'about_home' );

		$selected = array_values( array_intersect( $order, $reusable ) );

		if ( ! empty( $selected ) ) :

			?>

		<div class="generic-content-page__reusable">

			<?php

			foreach ( $selected as $block_key ) {

				if ( 'rehab_requirements' === $block_key ) {

					get_template_part( 'template-parts/home/rehabilitation-requirements' );

				} elseif ( 'about_home' === $block_key ) {

					get_template_part(

						'template-parts/home/comfort',

						null,

						array(

							'section_id' => 'generic-about-home',

							'heading_id' => 'generic-about-home-heading',

						)

					);

				}

			}

			?>

		</div>

			<?php

		endif;

		?>

	</div>

</section>


