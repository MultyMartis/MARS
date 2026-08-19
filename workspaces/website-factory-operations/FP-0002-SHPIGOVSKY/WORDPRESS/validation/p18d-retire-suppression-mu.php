<?php
/**
 * P18D — Suppression MU retirement script.
 *
 * After SMTP is VERIFIED/ACTIVE, the temporary MU plugin
 * fp02-pre-cutover-mail-suppression.php already defers to
 * MailOps::should_suppress() → false (delivery_active=1).
 * The MU file is therefore inert but still executable.
 *
 * This script verifies readiness and provides removal instructions.
 * It does NOT delete files automatically — file removal is a destructive
 * operation and requires explicit operator action per MARS governance.
 *
 * Run via WP-CLI: wp eval-file p18d-retire-suppression-mu.php
 *
 * @package Shpigovsky_P18D
 */

if ( ! defined( 'ABSPATH' ) ) {
	die( "Must run inside WordPress (WP-CLI or bootstrap).\n" );
}

if ( ! class_exists( '\Shpigovsky\Core\Mail\MailOps' ) ) {
	die( "[P18D] ERROR: MailOps class not found.\n" );
}

use Shpigovsky\Core\Mail\MailOps;

$state = MailOps::state();
$suppressed = MailOps::should_suppress();

echo "[P18D RETIRE-MU] Current SMTP state: " . $state . "\n";
echo "[P18D RETIRE-MU] should_suppress(): " . ( $suppressed ? 'true (mail blocked)' : 'false (mail flows)' ) . "\n";
echo "\n";

if ( MailOps::STATE_VERIFIED_ACTIVE !== $state ) {
	echo "[P18D RETIRE-MU] NOT READY: SMTP must be VERIFIED/ACTIVE before retiring suppression MU.\n";
	exit( 1 );
}

if ( $suppressed ) {
	echo "[P18D RETIRE-MU] WARNING: should_suppress() still returns true. Check delivery_active option.\n";
	exit( 1 );
}

echo "[P18D RETIRE-MU] READY FOR RETIREMENT.\n";
echo "  The MU plugin fp02-pre-cutover-mail-suppression.php defers to MailOps.\n";
echo "  Since delivery_active=1, the MU is inert — mail is NOT being blocked by it.\n";
echo "\n";
echo "[P18D RETIRE-MU] OPERATOR ACTION REQUIRED to remove the file:\n";
echo "  File: {wp-content}/mu-plugins/fp02-pre-cutover-mail-suppression.php\n";
echo "  Action: delete the file from the server via FTP or Beget File Manager.\n";
echo "  Do NOT use git clean or broad directory commands.\n";
echo "  After deletion: confirm no pre_wp_mail filter remains from this MU.\n";
echo "\n";
echo "[P18D RETIRE-MU] The active suppression owner after deletion:\n";
echo "  MailOps::should_suppress() → controlled by fp02_mail_ops.delivery_active in DB.\n";
echo "  The operator can toggle via Admin → Почта и формы → Выключить отправку писем.\n";
