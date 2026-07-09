<?php
/**
 * Template part: institutional/founder-quote.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_is_about_hub_page() ) {
	return;
}

ob_start();
get_template_part( 'template-parts/home/founder-quote' );
$markup = (string) ob_get_clean();

if ( '' === $markup ) {
	return;
}

echo str_replace(
	'class="founder-quote founder-quote--variant-b"',
	'class="founder-quote founder-quote--variant-b founder-quote--institutional-context"',
	$markup
); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
