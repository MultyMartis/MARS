<?php
/**
 * Contact block with form stub.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$phone   = fws_get_option( 'phone', '+7 (000) 000-00-00' );
$email   = fws_get_option( 'email', 'synthetic@example.invalid' );
$address = fws_get_option( 'address', __( 'синтетический, без реальной геолокации', 'fws-synthetic' ) );
?>
<section class="contact-block">
	<div class="container contact-block__inner">
		<div class="contact-block__info">
			<h2 class="section-title"><?php esc_html_e( 'Связаться с нами', 'fws-synthetic' ); ?></h2>
			<p>
				<?php esc_html_e( 'Телефон:', 'fws-synthetic' ); ?>
				<a href="<?php echo esc_url( fws_phone_href( $phone ) ); ?>"><?php echo esc_html( $phone ); ?></a>
			</p>
			<p>
				<?php esc_html_e( 'Email:', 'fws-synthetic' ); ?>
				<a href="<?php echo esc_url( 'mailto:' . $email ); ?>"><?php echo esc_html( $email ); ?></a>
			</p>
			<p>
				<?php esc_html_e( 'Адрес:', 'fws-synthetic' ); ?>
				<?php echo esc_html( $address ); ?>
			</p>
		</div>
		<form class="contact-form" data-contact-form action="#" method="post" novalidate>
			<label class="contact-form__field">
				<span><?php esc_html_e( 'Имя', 'fws-synthetic' ); ?></span>
				<input type="text" name="name" required autocomplete="name">
			</label>
			<label class="contact-form__field">
				<span><?php esc_html_e( 'Email', 'fws-synthetic' ); ?></span>
				<input type="email" name="email" required autocomplete="email">
			</label>
			<label class="contact-form__field">
				<span><?php esc_html_e( 'Сообщение', 'fws-synthetic' ); ?></span>
				<textarea name="message" rows="4" required></textarea>
			</label>
			<button class="btn btn--primary" type="submit"><?php esc_html_e( 'Отправить', 'fws-synthetic' ); ?></button>
			<p class="contact-form__note" data-form-status hidden role="status"></p>
		</form>
	</div>
</section>
