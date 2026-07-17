<?php
/**
 * Template Name: Contacts
 * Route family: /kontakty/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-kontakty__main site-main site-main--contacts" id="main-content">
	<?php if ( shpigovsky_breadcrumbs_enabled_for_context() ) : ?>
		<div class="contacts-page__breadcrumbs">
			<div class="container">
				<?php shpigovsky_render_breadcrumbs(); ?>
			</div>
		</div>
	<?php endif; ?>
	<?php
	get_template_part( 'template-parts/contacts/map-body' );
	get_template_part( 'template-parts/contacts/rehabilitation-steps' );
	?>
</main>
<?php
get_footer();
