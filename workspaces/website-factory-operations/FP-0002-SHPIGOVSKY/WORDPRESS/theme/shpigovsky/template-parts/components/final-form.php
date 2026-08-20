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

$parsed_args = wp_parse_args(
	$args ?? array(),
	array(
		'heading_id'  => 'final-form-heading',
		'heading_text' => '',
		'lead_text'   => '',
		'lead_source' => 'final-section',
		'section_modifier_class' => '',
	)
);

$heading_id = trim( (string) $parsed_args['heading_id'] );
$heading    = trim( (string) $parsed_args['heading_text'] );
$lead       = trim( (string) $parsed_args['lead_text'] );
$lead_source = trim( (string) $parsed_args['lead_source'] );
$section_modifier_class = trim( (string) $parsed_args['section_modifier_class'] );

if ( '' === $heading ) {
	$heading = shpigovsky_get_final_form_heading();
}

if ( '' === $lead ) {
	$lead = shpigovsky_get_final_form_lead();
}

if ( '' === $lead_source ) {
	$lead_source = 'final-section';
}

$submit_label = shpigovsky_get_final_form_submit_label();
$name_label   = shpigovsky_get_final_form_field_label( 'final_form_name_label', __( 'Ваше имя', 'shpigovsky' ) );
$phone_label  = shpigovsky_get_final_form_field_label( 'final_form_phone_label', __( 'Ваш телефон', 'shpigovsky' ) );
$message_label = shpigovsky_get_final_form_field_label( 'final_form_message_label', __( 'Опишите ситуацию', 'shpigovsky' ) );
$name_placeholder = shpigovsky_get_final_form_field_label( 'final_form_name_placeholder', __( 'Ваше имя', 'shpigovsky' ) );
$phone_placeholder = shpigovsky_get_block_option_scalar( 'final_form_phone_placeholder', shpigovsky_get_final_form_block_context() );
$message_placeholder = shpigovsky_get_final_form_field_label( 'final_form_message_placeholder', __( 'Опишите ситуацию', 'shpigovsky' ) );

if ( '' === $phone_placeholder || '+7 999 999 - 99 - 99' === $phone_placeholder ) {
	$phone_placeholder = '+7 (___) ___-__-__';
}

$consent_url = home_url( '/consent-personal-data/' );
$privacy_url = home_url( '/privacy-policy/' );
?>
<section data-reveal class="final-form<?php echo '' !== $section_modifier_class ? ' ' . esc_attr( $section_modifier_class ) : ''; ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container">
		<div class="final-form__band">
			<div class="final-form__copy">
				<h2 class="final-form__heading" id="<?php echo esc_attr( $heading_id ); ?>"><?php echo esc_html( $heading ); ?></h2>
				<p class="final-form__lead"><?php echo esc_html( $lead ); ?></p>
			</div>

			<form class="final-form__form" data-lead-form data-form-context="final" novalidate>
				<div class="final-form__hidden" data-lead-form-hidden aria-hidden="true">
					<input type="hidden" name="action" data-lead-hidden="action" value="fp02_lead_submit">
					<input type="hidden" name="fp02_lead_nonce" data-lead-hidden="fp02_lead_nonce" value="<?php echo esc_attr( wp_create_nonce( 'fp02_lead_submit' ) ); ?>">
					<input type="hidden" name="form_context" data-lead-hidden="form_context" value="final">
					<input type="hidden" name="lead_source" data-lead-hidden="lead_source" value="<?php echo esc_attr( $lead_source ); ?>">
					<input type="hidden" name="page_url" data-lead-hidden="page_url" value="">
					<input type="hidden" name="page_title" data-lead-hidden="page_title" value="">
					<input type="hidden" name="fp02_fs" data-lead-hidden="fp02_fs" value="<?php echo esc_attr( class_exists( '\\Shpigovsky\\Core\\Forms\\AntiSpam' ) ? \Shpigovsky\Core\Forms\AntiSpam::issue_token( 'consultation', 'final' ) : '' ); ?>">
					<input type="hidden" name="request_token" data-lead-hidden="request_token" value="">
					<label class="final-form__honeypot" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;" aria-hidden="true">
						<span><?php esc_html_e( 'Не заполняйте это поле', 'shpigovsky' ); ?></span>
						<input type="text" name="company_url" data-lead-hidden="company_url" value="" tabindex="-1" autocomplete="new-password">
					</label>
				</div>
				<div class="final-form__row">
					<div class="final-form__field" data-lead-field-wrap>
						<label class="final-form__label" for="final-form-name"><?php echo esc_html( $name_label ); ?></label>
						<input
							class="final-form__input"
							type="text"
							id="final-form-name"
							name="name"
							autocomplete="name"
							placeholder="<?php echo esc_attr( $name_placeholder ); ?>"
							required
							aria-describedby="final-form-name-error"
						>
						<span class="final-form__field-error" data-lead-field-error id="final-form-name-error" hidden></span>
					</div>
					<div class="final-form__field" data-lead-field-wrap>
						<label class="final-form__label" for="final-form-phone"><?php echo esc_html( $phone_label ); ?></label>
						<input
							class="final-form__input"
							type="tel"
							id="final-form-phone"
							name="phone"
							data-phone-input
							inputmode="tel"
							placeholder="<?php echo esc_attr( $phone_placeholder ); ?>"
							autocomplete="tel"
							required
							aria-describedby="final-form-phone-error"
						>
						<span class="final-form__field-error" data-lead-field-error id="final-form-phone-error" hidden></span>
					</div>
				</div>
				<div class="final-form__field final-form__field_message" data-lead-field-wrap>
					<label class="final-form__label" for="final-form-message"><?php echo esc_html( $message_label ); ?></label>
					<textarea
						class="final-form__textarea"
						id="final-form-message"
						name="message"
						rows="4"
						placeholder="<?php echo esc_attr( $message_placeholder ); ?>"
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
