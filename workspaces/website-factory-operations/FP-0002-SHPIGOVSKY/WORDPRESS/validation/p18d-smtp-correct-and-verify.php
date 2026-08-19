<?php
/**
 * P18D — SMTP transport correction + SMTP test bypass script.
 *
 * Purpose: correct smtp_encryption from 'none' to 'ssl' (Beget port-465 requirement),
 * then run the bounded SMTP test and record result in MailOps.
 * Does NOT activate delivery — that is a separate Admin action after test passes.
 * Does NOT expose the SMTP password.
 *
 * Run via WP-CLI: wp eval-file p18d-smtp-correct-and-verify.php
 * (requires WordPress bootstrap / WP-CLI context)
 *
 * SAFE: read-only until config correction confirmed; no live mail to form recipients;
 * uses FP02_MAIL_ALLOW_ONCE bounded bypass; no password in output.
 *
 * @package Shpigovsky_P18D
 */

if ( ! defined( 'ABSPATH' ) ) {
	die( "Must run inside WordPress (WP-CLI or bootstrap).\n" );
}

if ( ! class_exists( '\Shpigovsky\Core\Mail\MailOps' ) ) {
	die( "[P18D] ERROR: MailOps class not found. Plugin not active?\n" );
}

// ─── 1. PRE-CORRECTION INTAKE ─────────────────────────────────────────────────

$cfg_before = \Shpigovsky\Core\Mail\MailOps::get_config();
echo "[P18D] PRE-CORRECTION STATE:\n";
echo "  smtp_host       = " . $cfg_before['smtp_host'] . "\n";
echo "  smtp_port       = " . $cfg_before['smtp_port'] . "\n";
echo "  smtp_encryption = " . $cfg_before['smtp_encryption'] . "\n";
echo "  smtp_auth       = " . $cfg_before['smtp_auth'] . "\n";
echo "  smtp_username   = " . $cfg_before['smtp_username'] . "\n";
echo "  password_configured = " . ( \Shpigovsky\Core\Mail\MailOps::password_is_configured() ? 'YES' : 'NO' ) . "\n";
echo "  recipients      = " . \Shpigovsky\Core\Mail\MailOps::recipient_count() . "\n";
echo "  verified        = " . $cfg_before['verified'] . "\n";
echo "  delivery_active = " . $cfg_before['delivery_active'] . "\n";
echo "  state           = " . MailOps::state() . "\n";
echo "\n";

// ─── 2. TRANSPORT MISMATCH CHECK ──────────────────────────────────────────────

$mismatch = false;
if ( 'smtp.beget.com' === $cfg_before['smtp_host']
	&& 465 === (int) $cfg_before['smtp_port']
	&& \Shpigovsky\Core\Mail\MailOps::ENCRYPTION_NONE === $cfg_before['smtp_encryption']
) {
	echo "[P18D] MISMATCH DETECTED: Beget port 465 requires ssl, not none.\n";
	$mismatch = true;
}

if ( $mismatch ) {
	// Correct encryption to 'ssl'. Preserve all other settings.
	$cfg_corrected                    = \Shpigovsky\Core\Mail\MailOps::get_config();
	$cfg_corrected['smtp_encryption'] = \Shpigovsky\Core\Mail\MailOps::ENCRYPTION_SSL;
	// Save via option directly (MailOps::save_from_post not used — password rewrite avoided).
	update_option( \Shpigovsky\Core\Mail\MailOps::OPTION_CONFIG, $cfg_corrected, false );
	echo "[P18D] CORRECTED: smtp_encryption set to 'ssl'.\n";
} else {
	echo "[P18D] No transport mismatch — no correction applied.\n";
}

// ─── 3. POST-CORRECTION STATE ─────────────────────────────────────────────────

$cfg_after = \Shpigovsky\Core\Mail\MailOps::get_config();
echo "[P18D] POST-CORRECTION STATE:\n";
echo "  smtp_host       = " . $cfg_after['smtp_host'] . "\n";
echo "  smtp_port       = " . $cfg_after['smtp_port'] . "\n";
echo "  smtp_encryption = " . $cfg_after['smtp_encryption'] . "\n";
echo "  smtp_auth       = " . $cfg_after['smtp_auth'] . "\n";
echo "  smtp_username   = " . $cfg_after['smtp_username'] . "\n";
echo "  password_configured = " . ( \Shpigovsky\Core\Mail\MailOps::password_is_configured() ? 'YES' : 'NO' ) . "\n";
echo "  is_complete     = " . ( \Shpigovsky\Core\Mail\MailOps::is_complete() ? 'YES' : 'NO' ) . "\n";
echo "  state           = " . \Shpigovsky\Core\Mail\MailOps::state() . "\n";
echo "\n";

// ─── 4. COMPLETENESS CHECK ────────────────────────────────────────────────────

if ( ! \Shpigovsky\Core\Mail\MailOps::is_complete() ) {
	echo "[P18D] BLOCKED: config not complete. Fill host/port/username/password/recipient in Admin.\n";
	exit( 1 );
}

$recipients = \Shpigovsky\Core\Mail\MailOps::recipient_emails();
if ( empty( $recipients ) ) {
	echo "[P18D] BLOCKED: no valid recipients configured.\n";
	exit( 1 );
}

// ─── 5. BOUNDED SMTP TEST ─────────────────────────────────────────────────────

echo "[P18D] Attempting SMTP test to first recipient...\n";
echo "  (password not shown; recipient count = " . count( $recipients ) . ")\n\n";

// Bounded one-shot allow (bypasses MU suppression for this one wp_mail call).
if ( ! defined( 'FP02_MAIL_ALLOW_ONCE' ) ) {
	define( 'FP02_MAIL_ALLOW_ONCE', true );
}

$test_to = $recipients[0];
$subject = 'FP-0002 SMTP test ' . gmdate( 'Y-m-d H:i:s' ) . ' UTC (P18D)';
$body    = "FP-0002 SMTP verification test.\nThis is not a client lead.\nTimestamp: " . gmdate( 'c' ) . "\nSender: " . \Shpigovsky\Core\Mail\MailOps::from_email() . "\n";
$headers = array(
	'Content-Type: text/plain; charset=UTF-8',
	'From: ' . \Shpigovsky\Core\Mail\MailOps::from_name() . ' <' . \Shpigovsky\Core\Mail\MailOps::from_email() . '>',
);

$sent = wp_mail( $test_to, $subject, $body, $headers );

if ( $sent ) {
	\Shpigovsky\Core\Mail\MailOps::record_test_result( true, '' );
	echo "[P18D] SMTP TEST RESULT: PASS\n";
	echo "  SMTP ACCEPTED the message.\n";
	echo "  MailOps state is now: " . \Shpigovsky\Core\Mail\MailOps::state() . "\n";
	echo "\n";
	echo "[P18D] NOTE: SMTP ACCEPTED does not mean INBOX DELIVERED.\n";
	echo "[P18D] NEXT: use Admin 'Включить отправку писем' to activate delivery (or run p18d-activate-delivery.php).\n";
} else {
	global $phpmailer;
	$raw = ( is_object( $phpmailer ) && ! empty( $phpmailer->ErrorInfo ) ) ? (string) $phpmailer->ErrorInfo : 'send_failed';
	// Sanitize — never print raw error that might contain credentials.
	$cat = \Shpigovsky\Core\Mail\MailOps::sanitize_error_category( $raw );
	\Shpigovsky\Core\Mail\MailOps::record_test_result( false, $cat );
	echo "[P18D] SMTP TEST RESULT: FAIL\n";
	echo "  Error category: " . $cat . "\n";
	echo "  (Raw error sanitized — no credentials shown)\n";
	echo "  MailOps state is now: " . \Shpigovsky\Core\Mail\MailOps::state() . "\n";
	exit( 1 );
}
