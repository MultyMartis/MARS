<?php
/**
 * Plugin Name: FP-0002 PRE-CUTOVER mail suppression
 * Description: Deliberate outbound mail suppression until SMTP after final domain/DNS cutover. Not a local-runtime identity claim. Runtime is Production/Beget on the temporary host.
 * Version: 0.3.6-p15
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * PRE-CUTOVER MAIL SUPPRESSION — keep until SMTP wave after domain cutover.
 * Forms must not silently deliver via unintended PHP mail() paths.
 *
 * @return false Short-circuit wp_mail.
 */
function fp02_p15_suppress_outgoing_mail_until_smtp() {
	return false;
}
add_filter( 'pre_wp_mail', 'fp02_p15_suppress_outgoing_mail_until_smtp', 1 );

// Historical aliases (P13/P06): Admin local-runtime notices and siteurl/home write guards remain retired.
// Do not re-enable outbound mail or indexing here.
