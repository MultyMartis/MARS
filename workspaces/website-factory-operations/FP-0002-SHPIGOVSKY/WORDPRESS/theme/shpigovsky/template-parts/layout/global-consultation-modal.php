<?php
/**
 * Global consultation modal — markup boundary only in D7-A.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$consent_url = home_url( '/consent-personal-data/' );
$privacy_url = home_url( '/privacy-policy/' );
?>
<div
	class="modal-consultation"
	data-modal="consultation"
	aria-hidden="true"
	hidden
>
	<div class="modal-consultation__overlay" data-modal-close tabindex="-1" aria-hidden="true"></div>
	<div
		class="modal-consultation__dialog"
		role="dialog"
		aria-modal="true"
		aria-labelledby="modal-consultation-title"
	>
		<button class="modal-consultation__close" type="button" data-modal-close aria-label="<?php esc_attr_e( 'Закрыть окно', 'shpigovsky' ); ?>">
			<i class="fas fa-times" aria-hidden="true"></i>
		</button>
		<h2 class="modal-consultation__title" id="modal-consultation-title" data-modal-title-target><?php esc_html_e( 'Записаться на консультацию', 'shpigovsky' ); ?></h2>
		<p class="modal-consultation__subtitle" data-modal-subtitle-target hidden></p>
		<form class="modal-consultation__form" data-lead-form data-form-context="modal" novalidate>
			<div class="modal-consultation__hidden" data-lead-form-hidden aria-hidden="true">
				<input type="hidden" name="action" data-lead-hidden="action" value="fp02_lead_submit">
				<input type="hidden" name="fp02_lead_nonce" data-lead-hidden="fp02_lead_nonce" value="<?php echo esc_attr( wp_create_nonce( 'fp02_lead_submit' ) ); ?>">
				<input type="hidden" name="form_context" data-lead-hidden="form_context" value="modal">
				<input type="hidden" name="lead_source" data-lead-hidden="lead_source" value="">
				<input type="hidden" name="page_url" data-lead-hidden="page_url" value="">
				<input type="hidden" name="page_title" data-lead-hidden="page_title" value="">
				<input type="hidden" name="fp02_fs" data-lead-hidden="fp02_fs" value="<?php echo esc_attr( class_exists( '\\Shpigovsky\\Core\\Forms\\AntiSpam' ) ? \Shpigovsky\Core\Forms\AntiSpam::issue_token( 'consultation', 'modal' ) : '' ); ?>">
				<input type="hidden" name="request_token" data-lead-hidden="request_token" value="">
				<label class="modal-consultation__honeypot" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;" aria-hidden="true">
					<span><?php esc_html_e( 'Не заполняйте это поле', 'shpigovsky' ); ?></span>
					<input type="text" name="company_url" data-lead-hidden="company_url" value="" tabindex="-1" autocomplete="new-password">
				</label>
			</div>
			<div class="modal-consultation__row">
				<div class="modal-consultation__field" data-lead-field-wrap>
					<label class="modal-consultation__label" for="modal-consultation-name"><?php esc_html_e( 'Ваше имя', 'shpigovsky' ); ?></label>
					<input class="modal-consultation__input" type="text" id="modal-consultation-name" name="name" autocomplete="name" placeholder="<?php esc_attr_e( 'Ваше имя', 'shpigovsky' ); ?>" required data-modal-focus>
					<span class="modal-consultation__field-error" data-lead-field-error id="modal-consultation-name-error" hidden></span>
				</div>
				<div class="modal-consultation__field" data-lead-field-wrap>
					<label class="modal-consultation__label" for="modal-consultation-phone"><?php esc_html_e( 'Ваш телефон', 'shpigovsky' ); ?></label>
					<input class="modal-consultation__input" type="tel" id="modal-consultation-phone" name="phone" data-phone-input inputmode="tel" placeholder="+7 (___) ___-__-__" autocomplete="tel" required>
					<span class="modal-consultation__field-error" data-lead-field-error id="modal-consultation-phone-error" hidden></span>
				</div>
			</div>
			<div class="modal-consultation__field modal-consultation__field_message" data-lead-field-wrap>
				<label class="modal-consultation__label" for="modal-consultation-message"><?php esc_html_e( 'Опишите ситуацию', 'shpigovsky' ); ?></label>
				<textarea class="modal-consultation__textarea" id="modal-consultation-message" name="message" rows="4" placeholder="<?php esc_attr_e( 'Опишите ситуацию', 'shpigovsky' ); ?>" required aria-describedby="modal-consultation-message-error"></textarea>
				<span class="modal-consultation__field-error" data-lead-field-error id="modal-consultation-message-error" hidden></span>
			</div>
			<label class="modal-consultation__consent" data-lead-field-wrap>
				<input class="modal-consultation__consent-input" type="checkbox" name="consent" value="1" required aria-describedby="modal-consultation-consent-error">
				<span class="modal-consultation__consent-control" aria-hidden="true"></span>
				<span class="modal-consultation__consent-text">
					<?php
					printf(
						wp_kses(
							/* translators: 1: consent page URL, 2: privacy policy URL */
							__( 'Я даю согласие на обработку персональных данных в соответствии с <a class="modal-consultation__consent-link" href="%1$s">Согласием на обработку персональных данных</a> и соглашаюсь с <a class="modal-consultation__consent-link" href="%2$s">Политикой конфиденциальности</a>.', 'shpigovsky' ),
							array(
								'a' => array(
									'class' => array(),
									'href'  => array(),
								),
							)
						),
						esc_url( $consent_url ),
						esc_url( $privacy_url )
					);
					?>
				</span>
				<span class="modal-consultation__field-error modal-consultation__field-error_consent" data-lead-field-error id="modal-consultation-consent-error" hidden></span>
			</label>
			<button type="submit" class="btn btn_dark btn--primary modal-consultation__submit" data-modal-submit-target><?php esc_html_e( 'Записаться на консультацию', 'shpigovsky' ); ?></button>
			<div class="modal-consultation__status" data-lead-form-status role="status" aria-live="polite" hidden></div>
		</form>
	</div>
</div>
