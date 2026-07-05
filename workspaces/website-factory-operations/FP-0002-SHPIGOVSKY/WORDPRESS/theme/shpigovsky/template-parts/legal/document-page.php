<?php
/**
 * Template part: legal/document-page.php
 * V9-06E1 — native post_content renderer for legal pages.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<section class="legal-document plain-page-content" data-content-status="legal-demo-document">
	<div class="container legal-document__container">
		<p class="legal-document__demo-notice">Документ подготовлен для демонстрационной версии сайта. Данные, отмеченные как «ДЕМО», подлежат замене перед публикацией.</p>
		<h1 class="legal-document__title"><?php the_title(); ?></h1>
		<div class="legal-document__body">
			<?php the_content(); ?>
		</div>
	</div>
</section>
