<?php
/**
 * Global CTA section (options-driven).
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$title = fws_get_option( 'cta_title', __( 'Готовы проверить pipeline?', 'fws-synthetic' ) );
$text  = fws_get_option( 'cta_text', __( 'Синтетический CTA-блок для global options mapping.', 'fws-synthetic' ) );
?>
<section class="cta-global">
	<div class="container cta-global__inner">
		<h2 class="cta-global__title"><?php echo esc_html( $title ); ?></h2>
		<p class="cta-global__text"><?php echo esc_html( $text ); ?></p>
		<a class="btn btn--primary" href="<?php echo esc_url( fws_get_contacts_url() ); ?>">
			<?php esc_html_e( 'Связаться', 'fws-synthetic' ); ?>
		</a>
	</div>
</section>
