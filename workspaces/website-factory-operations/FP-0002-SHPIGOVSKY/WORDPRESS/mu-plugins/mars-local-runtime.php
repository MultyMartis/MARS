<?php
/**
 * Plugin Name: FP-0002 runtime residue (P13 neutralized)
 * Description: Historical local-runtime MU-plugin. P13 removed global Admin notices and the siteurl/home write guard. Outgoing mail remains suppressed until a dedicated SMTP/P06 wave. Not a claim that this host is a local MARS runtime.
 * Version: 0.3.4-p13
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Historical local-stage mail suppression. SMTP remains out of P13 scope.
 *
 * @return false
 */
function fp02_p13_suppress_outgoing_mail() {
	return false;
}
add_filter( 'pre_wp_mail', 'fp02_p13_suppress_outgoing_mail', 1 );

// P13: do not print LOCAL MARS / Not production notices on Admin screens.
// P13: do not block updates to home/siteurl (that guard is a domain-cutover risk).
// WP_ENVIRONMENT_TYPE=local in wp-config.php is leftover residue — P06 cleanup, not hidden here.
