<?php
/**
 * Template part: institutional/institutional-narrative.php
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
$context = shpigovsky_get_about_narrative_context( $page_id );
?>
<section data-reveal class="institutional-narrative" id="who-we-are" aria-labelledby="institutional-narrative-heading">
	<div class="container institutional-narrative__container">
		<div class="institutional-narrative__intro">
			<h2 class="institutional-narrative__heading" id="institutional-narrative-heading"><?php echo esc_html( $context['heading'] ); ?></h2>
			<p class="institutional-narrative__lead block-whith-red-line"><?php echo esc_html( $context['lead'] ); ?></p>
		</div>
		<div class="institutional-narrative__body">
			<?php foreach ( $context['paragraphs'] as $paragraph ) : ?>
				<p class="institutional-narrative__text"><?php echo esc_html( $paragraph ); ?></p>
			<?php endforeach; ?>
		</div>
	</div>
</section>
