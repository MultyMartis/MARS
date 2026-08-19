<?php
/**
 * P18D — Activate production outbound mail delivery.
 *
 * Run ONLY after p18d-smtp-correct-and-verify.php confirms SMTP ACCEPTED.
 * Sets delivery_active=1 (VERIFIED/ACTIVE state).
 * The temporary MU fp02-pre-cutover-mail-suppression.php then defers to
 * MailOps::should_suppress() which returns false when delivery_active=1.
 * The MU file may then be removed as a separate cleanup step.
 *
 * Run via WP-CLI: wp eval-file p18d-activate-delivery.php
 *
 * @package Shpigovsky_P18D
 */

if ( ! defined( 'ABSPATH' ) ) {
	die( "Must run inside WordPress (WP-CLI or bootstrap).\n" );
}

if ( ! class_exists( '\Shpigovsky\Core\Mail\MailOps' ) ) {
	die( "[P18D] ERROR: MailOps class not found.\n" );
}

$state_before = \Shpigovsky\Core\Mail\MailOps::state();
echo "[P18D] State before activation: " . $state_before . "\n";

if ( \Shpigovsky\Core\Mail\MailOps::STATE_VERIFIED_READY !== $state_before ) {
	echo "[P18D] BLOCKED: activation requires state VERIFIED/NOT ACTIVE.\n";
	echo "  Current state: " . $state_before . "\n";
	echo "  Run SMTP test first (p18d-smtp-correct-and-verify.php).\n";
	exit( 1 );
}

$ok = \Shpigovsky\Core\Mail\MailOps::activate_delivery();
if ( $ok ) {
	echo "[P18D] DELIVERY ACTIVATED.\n";
	echo "  State is now: " . \Shpigovsky\Core\Mail\MailOps::state() . "\n";
	echo "  MailOps::should_suppress() = " . ( \Shpigovsky\Core\Mail\MailOps::should_suppress() ? 'true (suppressed)' : 'false (mail flows)' ) . "\n";
	echo "\n";
	echo "[P18D] IMPORTANT: The MU plugin fp02-pre-cutover-mail-suppression.php\n";
	echo "  now defers to MailOps (delivery_active=1 → not suppressed).\n";
	echo "  It is safe to remove the MU file as a cleanup step.\n";
	echo "  Do NOT remove before confirming delivery_active=1 in DB.\n";
} else {
	echo "[P18D] ACTIVATION FAILED. SMTP may not be verified yet.\n";
	exit( 1 );
}
