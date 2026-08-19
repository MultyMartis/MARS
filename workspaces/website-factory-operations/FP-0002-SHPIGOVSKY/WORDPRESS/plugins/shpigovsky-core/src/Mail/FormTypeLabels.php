<?php
/**
 * Recipient-facing Russian labels for internal form keys.
 *
 * Machine keys remain internal (lead registry, logs). Labels are presentation-only.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Mail;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical form-type localization map (presentation boundary).
 */
final class FormTypeLabels {

	/**
	 * Known machine form keys → Russian operator/recipient labels.
	 *
	 * @var array<string, string>
	 */
	private const LABELS = array(
		'consultation' => 'Консультация',
		'callback'     => 'Обратный звонок',
		'contact'      => 'Обращение с сайта',
		'question'     => 'Вопрос',
		'appointment'  => 'Запись на консультацию',
	);

	/**
	 * Localized label for a machine form key.
	 *
	 * @param string $form_key Internal form identifier.
	 * @return string
	 */
	public static function label( $form_key ) {
		$key = sanitize_key( (string) $form_key );
		if ( isset( self::LABELS[ $key ] ) ) {
			return self::LABELS[ $key ];
		}

		return __( 'Обращение с сайта', 'shpigovsky-core' );
	}

	/**
	 * Registered machine keys (for admin/docs; not exhaustive of DB history).
	 *
	 * @return array<int, string>
	 */
	public static function known_keys() {
		return array_keys( self::LABELS );
	}
}
