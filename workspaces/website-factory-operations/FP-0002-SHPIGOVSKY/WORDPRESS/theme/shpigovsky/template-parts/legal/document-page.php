<?php
/**
 * Template part: legal/document-page.php
 * V9-06E1 — native post_content renderer for legal pages.
 * PROD-P18A — DEMO banner owned solely by legal_demo_marker (explicit false stays off).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$legal_post_id   = (int) get_the_ID();
$legal_demo_on   = function_exists( 'shpigovsky_legal_demo_marker_enabled' )
	? shpigovsky_legal_demo_marker_enabled( $legal_post_id )
	: false;
$legal_status_attr = $legal_demo_on ? 'legal-demo-document' : 'legal-document';
?>
<section class="legal-document plain-page-content" data-content-status="<?php echo esc_attr( $legal_status_attr ); ?>">
	<div class="container legal-document__container">
		<?php if ( $legal_demo_on ) : ?>
		<p class="legal-document__demo-notice">Документ подготовлен для демонстрационной версии сайта. Данные, отмеченные как «ДЕМО», подлежат замене перед публикацией.</p>
		<?php endif; ?>
		<h1 class="legal-document__title"><?php the_title(); ?></h1>
		<div class="legal-document__body">
			<?php the_content(); ?>
		</div>
	</div>
</section>
