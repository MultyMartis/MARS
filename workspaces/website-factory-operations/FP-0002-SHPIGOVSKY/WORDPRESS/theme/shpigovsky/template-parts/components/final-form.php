<?php
/**
 * Template part: components/final-form.php
 *
 * Markup-only lead form; submission deferred to later integration wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading = shpigovsky_get_home_field( 'home_cta_title' );
$lead    = shpigovsky_get_home_field( 'home_cta_text' );

if ( '' === $heading ) {
	$heading = __( 'Остались вопросы?', 'shpigovsky' );
}

if ( '' === $lead ) {
	$lead = __( 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь', 'shpigovsky' );
}

$submit_label = shpigovsky_get_site_option( 'default_button_label' );
$submit_label = '' !== $submit_label ? $submit_label : __( 'Записаться на консультацию', 'shpigovsky' );

$consent_url = home_url( '/consent-personal-data/' );
$privacy_url = home_url( '/privacy-policy/' );
?>
<section data-reveal class="final-form" aria-labelledby="final-form-heading">
	<div class="container">
		<div class="final-form__band">
			<div class="final-form__copy">
				<h2 class="final-form__heading" id="final-form-heading"><?php echo esc_html( $heading ); ?></h2>
				<p class="final-form__lead"><?php echo esc_html( $lead ); ?></p>
			</div>

			<form class="final-form__form" data-lead-form data-form-context="final" novalidate>
				<div class="final-form__hidden" data-lead-form-hidden aria-hidden="true">
					<input type="hidden" name="form_context" data-lead-hidden="form_context" value="final">
					<input type="hidden" name="lead_source" data-lead-hidden="lead_source" value="final-section">
					<input type="hidden" name="page_url" data-lead-hidden="page_url" value="">
					<input type="hidden" name="page_title" data-lead-hidden="page_title" value="">
					<input type="hidden" name="g-recaptcha-response" data-lead-hidden="g-recaptcha-response" value="">
				</div>
				<div class="final-form__row">
					<div class="final-form__field" data-lead-field-wrap>
						<label class="final-form__label" for="final-form-name"><?php echo esc_html__( 'Ваше имя', 'shpigovsky' ); ?></label>
						<input
							class="final-form__input"
							type="text"
							id="final-form-name"
							name="name"
							autocomplete="name"
							placeholder="<?php echo esc_attr__( 'Ваше имя', 'shpigovsky' ); ?>"
							required
							aria-describedby="final-form-name-error"
						>
						<span class="final-form__field-error" data-lead-field-error id="final-form-name-error" hidden></span>
					</div>
					<div class="final-form__field" data-lead-field-wrap>
						<label class="final-form__label" for="final-form-phone"><?php echo esc_html__( 'Ваш телефон', 'shpigovsky' ); ?></label>
						<input
							class="final-form__input"
							type="tel"
							id="final-form-phone"
							name="phone"
							data-phone-input
							inputmode="tel"
							placeholder="+7 999 999 - 99 - 99"
							autocomplete="tel"
							required
							aria-describedby="final-form-phone-error"
						>
						<span class="final-form__field-error" data-lead-field-error id="final-form-phone-error" hidden></span>
					</div>
				</div>
				<div class="final-form__field final-form__field_message" data-lead-field-wrap>
					<label class="final-form__label" for="final-form-message"><?php echo esc_html__( 'Опишите ситуацию', 'shpigovsky' ); ?></label>
					<textarea
						class="final-form__textarea"
						id="final-form-message"
						name="message"
						rows="4"
						placeholder="<?php echo esc_attr__( 'Опишите ситуацию', 'shpigovsky' ); ?>"
						required
						aria-describedby="final-form-message-error"
					></textarea>
					<span class="final-form__field-error" data-lead-field-error id="final-form-message-error" hidden></span>
				</div>
				<label class="final-form__consent" data-lead-field-wrap>
					<input
						class="final-form__consent-input"
						type="checkbox"
						name="consent"
						value="1"
						required
					>
					<span class="final-form__consent-control" aria-hidden="true"></span>
					<span class="final-form__consent-text">
						<?php
						printf(
							/* translators: 1: consent URL, 2: privacy URL */
							wp_kses_post( __( 'Я даю согласие на обработку персональных данных в соответствии с <a class="final-form__consent-link" href="%1$s">Согласием на обработку персональных данных</a> и соглашаюсь с <a class="final-form__consent-link" href="%2$s">Политикой конфиденциальности</a>.', 'shpigovsky' ) ),
							esc_url( $consent_url ),
							esc_url( $privacy_url )
						);
						?>
					</span>
					<span class="final-form__field-error final-form__field-error_consent" data-lead-field-error id="final-form-consent-error" hidden></span>
				</label>
				<button type="submit" class="btn btn_dark btn--primary final-form__submit"><?php echo esc_html( $submit_label ); ?></button>
				<div class="final-form__status" data-lead-form-status role="status" aria-live="polite" hidden></div>
			</form>
		</div>
	</div>
</section>
