<?php
$_SERVER['HTTP_HOST']     = 'shpigovsky.test';
$_SERVER['REQUEST_METHOD'] = 'POST';
$_SERVER['REMOTE_ADDR']   = '127.0.0.1';

$mode = $argv[1] ?? 'first';
$token_file = __DIR__ . '/_smoke_token.txt';

define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$nonce = wp_create_nonce( 'fp02_lead_submit' );

if ( 'first' === $mode ) {
	$token = 'dup' . wp_generate_password( 28, false, false );
	file_put_contents( $token_file, $token );
} elseif ( 'second' === $mode ) {
	$token = trim( (string) file_get_contents( $token_file ) );
} else {
	$token = 'hp' . wp_generate_password( 28, false, false );
}

$_POST = array(
	'action'          => 'fp02_lead_submit',
	'fp02_lead_nonce' => $nonce,
	'name'            => 'Guard',
	'phone'           => '+7 925 111-22-33',
	'message'         => 'Проверка guard',
	'consent'         => '1',
	'company_url'     => ( 'honeypot' === $mode ) ? 'http://spam.example' : '',
	'form_started_at' => (string) ( time() - 5 ),
	'timestamp'       => (string) time(),
	'request_token'   => $token,
	'form_context'    => 'modal',
	'lead_source'     => 'e56-guard-' . $mode,
);

do_action( 'wp_ajax_nopriv_fp02_lead_submit' );
