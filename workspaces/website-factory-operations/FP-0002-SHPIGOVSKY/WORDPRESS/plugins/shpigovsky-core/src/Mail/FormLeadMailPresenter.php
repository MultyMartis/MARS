<?php
/**
 * Scoped HTML + plain-text templates for form lead notification emails.
 *
 * Presentation only — does not alter lead persistence or SMTP transport.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Mail;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Human-readable Russian notification mail builder for site forms.
 */
final class FormLeadMailPresenter {

	public const SITE_HOST = 'shpigovsky.ru';

	/**
	 * Build subject, bodies, and headers for wp_mail().
	 *
	 * @param string               $form_key Machine form key (internal).
	 * @param array<string, string> $payload  Sanitized lead payload.
	 * @return array{subject:string,html:string,plain:string,headers:array<int,string>}
	 */
	public static function build( $form_key, array $payload ) {
		$type_label = FormTypeLabels::label( $form_key );
		$subject    = sprintf(
			'[%s] %s — %s',
			MailOps::from_name(),
			__( 'Новая заявка', 'shpigovsky-core' ),
			$type_label
		);

		return array(
			'subject' => $subject,
			'html'    => self::build_html( $payload, $type_label ),
			'plain'   => self::build_plain( $payload, $type_label ),
			'headers' => self::build_headers( $payload ),
		);
	}

	/**
	 * @param array<string, string> $payload    Payload.
	 * @param string                $type_label Localized form type.
	 * @return string
	 */
	private static function build_plain( array $payload, $type_label ) {
		$lines   = array();
		$lines[] = sprintf(
			/* translators: %s: site brand name */
			__( 'Новая заявка с сайта «%s»', 'shpigovsky-core' ),
			MailOps::from_name()
		);
		$lines[] = '';
		$lines[] = __( 'Имя:', 'shpigovsky-core' ) . ' ' . $payload['name'];
		$lines[] = __( 'Телефон:', 'shpigovsky-core' ) . ' ' . $payload['phone'];

		if ( '' !== $payload['email'] ) {
			$lines[] = __( 'Email:', 'shpigovsky-core' ) . ' ' . $payload['email'];
		}

		if ( '' !== trim( $payload['message'] ) ) {
			$lines[] = __( 'Сообщение:', 'shpigovsky-core' );
			$lines[] = $payload['message'];
			$lines[] = '';
		}

		$page_url = self::normalize_page_url( $payload['page_url'] );
		if ( '' !== $page_url ) {
			$lines[] = __( 'Страница заявки:', 'shpigovsky-core' );
			$lines[] = $page_url;
			$lines[] = '';
		}

		$lines[] = __( 'Тип обращения:', 'shpigovsky-core' ) . ' ' . $type_label;
		$lines[] = __( 'Дата и время:', 'shpigovsky-core' ) . ' ' . self::format_datetime();
		$lines[] = '';
		$lines[] = '---';
		$lines[] = sprintf(
			/* translators: %s: site hostname */
			__( 'Сайт: %s', 'shpigovsky-core' ),
			self::SITE_HOST
		);

		return implode( "\n", $lines );
	}

	/**
	 * @param array<string, string> $payload    Payload.
	 * @param string                $type_label Localized form type.
	 * @return string
	 */
	private static function build_html( array $payload, $type_label ) {
		$page_url  = self::normalize_page_url( $payload['page_url'] );
		$datetime  = esc_html( self::format_datetime() );
		$name      = esc_html( $payload['name'] );
		$phone     = esc_html( $payload['phone'] );
		$phone_href = preg_replace( '/[^\d+]/', '', $payload['phone'] );
		$phone_href = is_string( $phone_href ) ? $phone_href : '';

		$rows = array(
			self::html_row( __( 'Имя', 'shpigovsky-core' ), $name ),
			self::html_row(
				__( 'Телефон', 'shpigovsky-core' ),
				'' !== $phone_href
					? '<a href="tel:' . esc_attr( $phone_href ) . '" style="color:#2271b1;text-decoration:none;">' . $phone . '</a>'
					: $phone,
				true
			),
		);

		if ( '' !== $payload['email'] && is_email( $payload['email'] ) ) {
			$email = esc_html( $payload['email'] );
			$rows[] = self::html_row(
				__( 'Email', 'shpigovsky-core' ),
				'<a href="mailto:' . esc_attr( $payload['email'] ) . '" style="color:#2271b1;text-decoration:none;">' . $email . '</a>',
				true
			);
		}

		$rows[] = self::html_row( __( 'Тип обращения', 'shpigovsky-core' ), esc_html( $type_label ) );
		$rows[] = self::html_row( __( 'Дата и время', 'shpigovsky-core' ), $datetime );

		if ( '' !== $page_url ) {
			$rows[] = self::html_row(
				__( 'Страница заявки', 'shpigovsky-core' ),
				'<a href="' . esc_url( $page_url ) . '" style="color:#2271b1;text-decoration:none;word-break:break-all;">' . esc_html( $page_url ) . '</a>',
				true
			);
		}

		$message_block = '';
		if ( '' !== trim( $payload['message'] ) ) {
			$message_block = '<tr><td colspan="2" style="padding:16px 0 8px;font-size:13px;font-weight:600;color:#1d2327;">'
				. esc_html__( 'Сообщение', 'shpigovsky-core' )
				. '</td></tr><tr><td colspan="2" style="padding:0 0 16px;font-size:14px;line-height:1.5;color:#1d2327;white-space:pre-wrap;">'
				. nl2br( esc_html( $payload['message'] ), false )
				. '</td></tr>';
		}

		$brand = esc_html( MailOps::from_name() );

		return '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>'
			. '<body style="margin:0;padding:24px 16px;background:#f6f7f7;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Oxygen-Sans,Ubuntu,Cantarell,\'Helvetica Neue\',sans-serif;">'
			. '<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="max-width:560px;margin:0 auto;background:#ffffff;border:1px solid #dcdcde;border-radius:4px;">'
			. '<tr><td style="padding:24px 24px 8px;">'
			. '<h1 style="margin:0 0 4px;font-size:20px;line-height:1.3;color:#1d2327;">' . esc_html__( 'Новая заявка с сайта', 'shpigovsky-core' ) . '</h1>'
			. '<p style="margin:0;font-size:14px;color:#646970;">' . $brand . '</p>'
			. '</td></tr>'
			. '<tr><td style="padding:8px 24px 16px;"><table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;">'
			. implode( '', $rows )
			. $message_block
			. '</table></td></tr>'
			. '<tr><td style="padding:16px 24px;border-top:1px solid #dcdcde;font-size:12px;color:#646970;">'
			. sprintf(
				/* translators: %s: site hostname */
				esc_html__( 'Отправлено с сайта %s', 'shpigovsky-core' ),
				esc_html( self::SITE_HOST )
			)
			. '</td></tr>'
			. '</table></body></html>';
	}

	/**
	 * @param string $label Row label.
	 * @param string $value Cell HTML (pre-escaped when $raw_html).
	 * @param bool   $raw_html Value is safe HTML.
	 * @return string
	 */
	private static function html_row( $label, $value, $raw_html = false ) {
		$value_out = $raw_html ? $value : esc_html( $value );

		return '<tr>'
			. '<td style="padding:8px 12px 8px 0;font-size:13px;color:#646970;vertical-align:top;width:38%;">' . esc_html( $label ) . '</td>'
			. '<td style="padding:8px 0;font-size:14px;color:#1d2327;vertical-align:top;">' . $value_out . '</td>'
			. '</tr>';
	}

	/**
	 * @param array<string, string> $payload Payload.
	 * @return array<int, string>
	 */
	private static function build_headers( array $payload ) {
		$headers = array(
			'Content-Type: text/html; charset=UTF-8',
			'From: ' . MailOps::from_name() . ' <' . MailOps::from_email() . '>',
		);

		if ( '' !== $payload['email'] && is_email( $payload['email'] ) ) {
			$headers[] = 'Reply-To: ' . $payload['email'];
		}

		return $headers;
	}

	/**
	 * Human-readable site-local datetime for recipients.
	 *
	 * @return string
	 */
	private static function format_datetime() {
		if ( function_exists( 'wp_date' ) ) {
			return wp_date( 'd.m.Y, H:i', time() );
		}

		return gmdate( 'd.m.Y, H:i' );
	}

	/**
	 * Normalize page URL to production host; omit invalid/staging URLs.
	 *
	 * @param string $url Raw page URL from form.
	 * @return string
	 */
	private static function normalize_page_url( $url ) {
		$url = trim( (string) $url );
		if ( '' === $url ) {
			return '';
		}

		$parsed = wp_parse_url( $url );
		if ( ! is_array( $parsed ) ) {
			return '';
		}

		$host = isset( $parsed['host'] ) ? strtolower( (string) $parsed['host'] ) : '';
		if ( '' !== $host && false !== strpos( $host, 'beget.tech' ) ) {
			return '';
		}

		$path  = isset( $parsed['path'] ) ? (string) $parsed['path'] : '/';
		$query = isset( $parsed['query'] ) && '' !== $parsed['query'] ? '?' . $parsed['query'] : '';

		if ( '' === $path ) {
			$path = '/';
		}

		return 'https://' . self::SITE_HOST . $path . $query;
	}
}
