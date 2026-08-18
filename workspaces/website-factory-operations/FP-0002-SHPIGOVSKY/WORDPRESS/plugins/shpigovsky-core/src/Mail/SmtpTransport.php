<?php
/**
 * Single SMTP transport owner — PHPMailer via phpmailer_init.
 *
 * Do not install a competing SMTP plugin for FP-0002.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Mail;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Configures PHPMailer from MailOps settings.
 */
final class SmtpTransport implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'mail.smtp-transport';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'phpmailer_init', array( __CLASS__, 'configure_phpmailer' ) );
	}

	/**
	 * Apply stored SMTP settings to PHPMailer.
	 *
	 * @param \PHPMailer\PHPMailer\PHPMailer $phpmailer Mailer.
	 */
	public static function configure_phpmailer( $phpmailer ) {
		if ( ! is_object( $phpmailer ) || ! method_exists( $phpmailer, 'isSMTP' ) ) {
			return;
		}

		if ( ! MailOps::is_complete() ) {
			return;
		}

		$cfg = MailOps::get_config();

		$phpmailer->isSMTP();
		$phpmailer->Host       = (string) $cfg['smtp_host'];
		$phpmailer->Port       = (int) $cfg['smtp_port'];
		$phpmailer->SMTPAuth   = (bool) $cfg['smtp_auth'];
		$phpmailer->Timeout    = 15;
		$phpmailer->SMTPAutoTLS = true;

		$enc = MailOps::sanitize_encryption( (string) $cfg['smtp_encryption'] );
		if ( MailOps::ENCRYPTION_NONE === $enc ) {
			$phpmailer->SMTPSecure = '';
		} elseif ( MailOps::ENCRYPTION_SSL === $enc ) {
			$phpmailer->SMTPSecure = 'ssl';
		} else {
			$phpmailer->SMTPSecure = 'tls';
		}

		if ( $cfg['smtp_auth'] ) {
			$phpmailer->Username = (string) $cfg['smtp_username'];
			$phpmailer->Password = MailOps::get_password_for_transport();
		}

		$from = MailOps::from_email();
		$name = MailOps::from_name();
		if ( is_email( $from ) ) {
			try {
				$phpmailer->setFrom( $from, $name, false );
			} catch ( \Exception $e ) { // phpcs:ignore Generic.CodeAnalysis.EmptyStatement.DetectedCatch
				// Leave PHPMailer defaults; do not log the exception body (may contain host details).
			}
		}
	}
}
