<?php
$_SERVER['HTTP_HOST']      = 'shpigovsky.test';
$_SERVER['REQUEST_METHOD'] = 'POST';
$_SERVER['REMOTE_ADDR']    = '127.0.0.1';
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$nonce = wp_create_nonce( 'fp02_lead_submit' );
$_POST = array(
	'action'          => 'fp02_lead_submit',
	'fp02_lead_nonce' => $nonce,
	'name'            => 'Smoke E56',
	'phone'           => '+7 925 183-64-64',
	'message'         => 'Проверка локального обработчика',
	'consent'         => '1',
	'company_url'     => '',
	'form_started_at' => (string) ( time() - 5 ),
	'timestamp'       => (string) time(),
	'request_token'   => 'smoke' . wp_generate_password( 24, false, false ),
	'form_context'    => 'final',
	'lead_source'     => 'e56-smoke-final',
);

// Capture JSON by temporarily preventing exit via filter if available.
add_filter(
	'wp_die_ajax_handler',
	static function () {
		return static function ( $message ) {
			// wp_send_json already echoed; swallow die.
		};
	}
);

ob_start();
do_action( 'wp_ajax_nopriv_fp02_lead_submit' );
$buf = ob_get_clean();

$uploads = wp_upload_dir();
$dir     = trailingslashit( $uploads['basedir'] ) . 'fp02-leads-local';
$files   = is_dir( $dir ) ? glob( $dir . '/receipt-*.json' ) : array();

$out = array(
	'response'           => json_decode( $buf, true ),
	'raw'                => $buf,
	'module_enabled'     => \Shpigovsky\Core\ModuleRegistry::is_enabled( 'forms.consultation' ),
	'future_recipient'   => \Shpigovsky\Core\Forms\ConsultationHandler::FUTURE_RECIPIENT,
	'receipt_count'      => is_array( $files ) ? count( $files ) : 0,
	'htaccess_deny'      => is_file( $dir . '/.htaccess' ) ? trim( (string) file_get_contents( $dir . '/.htaccess' ) ) : null,
	'localized_action'   => \Shpigovsky\Core\Forms\ConsultationHandler::AJAX_ACTION,
);

file_put_contents( __DIR__ . '/lead-ajax-smoke.json', json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . PHP_EOL;
