<?php
/**
 * Hero section.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$field_post_id = get_queried_object_id();

$eyebrow = fws_get_field( 'hero_eyebrow', $field_post_id, __( 'Синтетический контент', 'fws-synthetic' ) );
$title   = fws_get_field( 'hero_title', $field_post_id, __( 'Демонстрационный проект Forge WordPress', 'fws-synthetic' ) );
$text    = fws_get_field( 'hero_text', $field_post_id, __( 'Тестовая услуга и синтетический frontend для проверки pipeline без клиентских данных.', 'fws-synthetic' ) );

$btn_primary_label   = fws_get_field( 'hero_btn_primary_label', $field_post_id, __( 'Смотреть услуги', 'fws-synthetic' ) );
$btn_primary_url     = fws_get_field( 'hero_btn_primary_url', $field_post_id, fws_get_services_url() );
$btn_secondary_label = fws_get_field( 'hero_btn_secondary_label', $field_post_id, __( 'Связаться', 'fws-synthetic' ) );
$btn_secondary_url   = fws_get_field( 'hero_btn_secondary_url', $field_post_id, fws_get_contacts_url() );
?>
<section class="hero">
	<div class="container hero__inner">
		<?php if ( $eyebrow ) : ?>
		<p class="hero__eyebrow"><?php echo esc_html( $eyebrow ); ?></p>
		<?php endif; ?>
		<h1 class="hero__title"><?php echo esc_html( $title ); ?></h1>
		<?php if ( $text ) : ?>
		<p class="hero__text"><?php echo esc_html( $text ); ?></p>
		<?php endif; ?>
		<div class="hero__actions">
			<a class="btn btn--primary" href="<?php echo esc_url( $btn_primary_url ); ?>">
				<?php echo esc_html( $btn_primary_label ); ?>
			</a>
			<a class="btn btn--ghost" href="<?php echo esc_url( $btn_secondary_url ); ?>">
				<?php echo esc_html( $btn_secondary_label ); ?>
			</a>
		</div>
	</div>
</section>
