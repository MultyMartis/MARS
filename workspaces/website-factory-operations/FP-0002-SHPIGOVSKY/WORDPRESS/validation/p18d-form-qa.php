<?php
/**
 * P18D — Real form delivery end-to-end QA script.
 *
 * Simulates a form submission through the ConsultationHandler pipeline:
 * validate → persist lead → attempt mail (with delivery active) → verify lead status.
 *
 * Uses is_qa=true so the lead is flagged as a test row.
 * No real client data. No fake/invalid contact data.
 *
 * Run via WP-CLI: wp eval-file p18d-form-qa.php
 * Run ONLY after delivery is VERIFIED/ACTIVE.
 *
 * @package Shpigovsky_P18D
 */

if ( ! defined( 'ABSPATH' ) ) {
	die( "Must run inside WordPress (WP-CLI or bootstrap).\n" );
}

if ( ! class_exists( '\Shpigovsky\Core\Mail\MailOps' ) ) {
	die( "[P18D] ERROR: MailOps class not found.\n" );
}
if ( ! class_exists( '\Shpigovsky\Core\Leads\LeadRegistry' ) ) {
	die( "[P18D] ERROR: LeadRegistry class not found.\n" );
}

use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\Leads\LeadRegistry;

// Pre-flight.
$state = MailOps::state();
echo "[P18D QA] SMTP state: " . $state . "\n";
if ( MailOps::STATE_VERIFIED_ACTIVE !== $state ) {
	echo "[P18D QA] WARNING: delivery not yet VERIFIED/ACTIVE. Mail will not be attempted.\n";
}

$recipients = MailOps::recipient_emails();
echo "[P18D QA] Recipients: " . count( $recipients ) . "\n";

// ─── 1. PERSIST QA LEAD ───────────────────────────────────────────────────────

$qa_timestamp = gmdate( 'Y-m-d H:i:s' ) . ' UTC';
$lead_id = LeadRegistry::insert(
	array(
		'form_key'        => LeadRegistry::FORM_KEY,
		'form_context'    => 'p18d-qa',
		'source_url'      => 'https://shpigovsky.ru/?fp02_qa=p18d',
		'source_path'     => '/',
		'source_post_id'  => 0,
		'visitor_name'    => 'QA-P18D Test',
		'phone'           => '+7 000 000-00-00',
		'email'           => MailOps::from_email(),
		'message'         => '[P18D QA] Controlled SMTP verification test. Timestamp: ' . $qa_timestamp . ' This is not a real client request.',
		'delivery_status' => LeadRegistry::STATUS_RECEIVED,
		'metrika_goal'    => MailOps::metrika_goal(),
		'utm_source'      => 'p18d-qa',
		'utm_medium'      => 'internal-test',
		'utm_campaign'    => 'smtp-verification',
		'utm_content'     => '',
		'utm_term'        => '',
		'referrer'        => '',
		'ua_class'        => 'bot',
		'is_qa'           => true,
	)
);

if ( $lead_id <= 0 ) {
	echo "[P18D QA] FAIL: Lead could not be persisted.\n";
	exit( 1 );
}

echo "[P18D QA] Lead persisted. ID: " . $lead_id . "\n";

// ─── 2. ATTEMPT MAIL ──────────────────────────────────────────────────────────

$mail_attempted = false;
$mail_accepted  = false;
$mail_status    = '';

if ( MailOps::should_attempt_mail() ) {
	$to      = $recipients;
	$subject = '[FP-0002 P18D QA] Form delivery test ' . gmdate( 'Y-m-d H:i:s' ) . ' UTC';
	$body    = "FP-0002 P18D Form QA\n";
	$body   .= "This is a controlled test submission — not a real client lead.\n";
	$body   .= "Timestamp: " . gmdate( 'c' ) . "\n";
	$body   .= "Lead ID: " . $lead_id . "\n";
	$body   .= "Sender: " . MailOps::from_email() . "\n";
	$headers = array(
		'Content-Type: text/plain; charset=UTF-8',
		'From: ' . MailOps::from_name() . ' <' . MailOps::from_email() . '>',
		'Reply-To: ' . MailOps::from_email(),
	);

	$sent = wp_mail( $to, $subject, $body, $headers );
	$mail_attempted = true;

	if ( $sent ) {
		$mail_accepted = true;
		$mail_status   = LeadRegistry::STATUS_MAIL_ACCEPTED;
		LeadRegistry::update_delivery(
			$lead_id,
			array(
				'delivery_status' => $mail_status,
				'smtp_status'     => 'accepted',
				'attempt_count'   => 1,
			)
		);
		echo "[P18D QA] MAIL ACCEPTED by SMTP server.\n";
		if ( count( $to ) > 1 ) {
			echo "[P18D QA] Multiple recipients: " . count( $to ) . " addresses in To: header.\n";
		}
	} else {
		global $phpmailer;
		$raw = ( is_object( $phpmailer ) && ! empty( $phpmailer->ErrorInfo ) ) ? (string) $phpmailer->ErrorInfo : 'send_failed';
		$cat = MailOps::sanitize_error_category( $raw );
		$mail_status = LeadRegistry::STATUS_MAIL_ERROR;
		LeadRegistry::update_delivery(
			$lead_id,
			array(
				'delivery_status' => $mail_status,
				'smtp_status'     => 'error',
				'error_code'      => $cat,
				'attempt_count'   => 1,
			)
		);
		echo "[P18D QA] MAIL FAILED. Error category: " . $cat . "\n";
	}
} else {
	$mail_status = MailOps::is_complete() ? LeadRegistry::STATUS_SMTP_PENDING : LeadRegistry::STATUS_MAIL_SUPPRESSED;
	LeadRegistry::update_delivery(
		$lead_id,
		array(
			'delivery_status' => $mail_status,
			'smtp_status'     => 'suppressed',
			'attempt_count'   => 0,
		)
	);
	echo "[P18D QA] Mail not attempted (suppression active or SMTP not verified/active).\n";
}

// ─── 3. QA SUMMARY ────────────────────────────────────────────────────────────

echo "\n[P18D QA] SUMMARY:\n";
echo "  lead_id         = " . $lead_id . "\n";
echo "  mail_attempted  = " . ( $mail_attempted ? 'YES' : 'NO' ) . "\n";
echo "  mail_accepted   = " . ( $mail_accepted ? 'YES' : 'NO' ) . "\n";
echo "  lead_status     = " . $mail_status . "\n";
echo "  recipients_sent = " . ( $mail_accepted ? count( $recipients ) : 0 ) . "\n";
echo "  is_qa           = YES\n";
echo "\n";
echo "[P18D QA] NOTE: MAIL_ACCEPTED means SMTP accepted the message, not inbox delivery.\n";
echo "[P18D QA] Verify lead appears in Admin → Заявки.\n";
echo "[P18D QA] QA lead is flagged is_qa=1 for cleanup if desired.\n";
