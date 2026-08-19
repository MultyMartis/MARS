<?php
/**
 * Plugin Name: FP-0002 PRE-CUTOVER mail suppression
 * Description: Outbound mail suppression until SMTP is verified and operator activates sending. Owner: Shpigovsky Core mail.ops. Temporary MU — retire after VERIFIED/ACTIVE.
 * Version: 0.3.12-p18c
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Suppress wp_mail unless SMTP delivery is explicitly active or a one-shot test is running.
 *
 * @param mixed $pre Current short-circuit value.
 * @return mixed Null to continue, false to suppress.
 */
function fp02_p15_suppress_outgoing_mail_until_smtp( $pre = null ) {
	if ( defined( 'FP02_MAIL_ALLOW_ONCE' ) && FP02_MAIL_ALLOW_ONCE ) {
		return $pre;
	}

	if ( class_exists( '\Shpigovsky\Core\Mail\MailOps' ) ) {
		return \Shpigovsky\Core\Mail\MailOps::should_suppress() ? false : $pre;
	}

	$ops = get_option( 'fp02_mail_ops', array() );
	if ( is_array( $ops ) && ! empty( $ops['delivery_active'] ) ) {
		return $pre;
	}

	return false;
}
add_filter( 'pre_wp_mail', 'fp02_p15_suppress_outgoing_mail_until_smtp', 1, 1 );

// Historical aliases (P13/P06): Admin local-runtime notices and siteurl/home write guards remain retired.
// Do not open indexing here. Do not treat saving SMTP fields as activation.
