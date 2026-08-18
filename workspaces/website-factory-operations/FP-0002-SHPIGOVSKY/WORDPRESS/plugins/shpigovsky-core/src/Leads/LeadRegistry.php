<?php
/**
 * Internal form lead registry — dedicated table, persist before mail.
 *
 * Email is transport, not the source of truth for whether a submission existed.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Leads;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Form lead storage.
 */
final class LeadRegistry implements ModuleInterface {

	public const DB_VERSION     = '1';
	public const DB_VERSION_KEY = 'fp02_form_leads_schema';
	public const FORM_KEY       = 'consultation';

	public const STATUS_RECEIVED        = 'RECEIVED';
	public const STATUS_MAIL_SUPPRESSED = 'MAIL_SUPPRESSED';
	public const STATUS_SMTP_PENDING    = 'SMTP_PENDING';
	public const STATUS_MAIL_ACCEPTED   = 'MAIL_ACCEPTED';
	public const STATUS_MAIL_ERROR      = 'MAIL_ERROR';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'leads.registry';
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
		add_action( 'admin_init', array( __CLASS__, 'maybe_install_table' ) );
		add_action( 'init', array( __CLASS__, 'maybe_install_table' ), 5 );
	}

	/**
	 * Table name with WP prefix (fp02_form_leads on this site).
	 *
	 * @return string
	 */
	public static function table_name() {
		global $wpdb;
		return $wpdb->prefix . 'form_leads';
	}

	/**
	 * Idempotent versioned schema.
	 */
	public static function maybe_install_table() {
		if ( get_option( self::DB_VERSION_KEY ) === self::DB_VERSION ) {
			return;
		}

		global $wpdb;
		$table   = self::table_name();
		$charset = $wpdb->get_charset_collate();

		require_once ABSPATH . 'wp-admin/includes/upgrade.php';

		$sql = "CREATE TABLE {$table} (
			id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
			created_at datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
			form_key varchar(32) NOT NULL DEFAULT '',
			form_context varchar(64) NOT NULL DEFAULT '',
			source_url varchar(500) NOT NULL DEFAULT '',
			source_path varchar(255) NOT NULL DEFAULT '',
			source_post_id bigint(20) unsigned NOT NULL DEFAULT 0,
			visitor_name varchar(120) NOT NULL DEFAULT '',
			phone varchar(40) NOT NULL DEFAULT '',
			email varchar(120) NOT NULL DEFAULT '',
			message text NULL,
			delivery_status varchar(32) NOT NULL DEFAULT '',
			smtp_status varchar(32) NOT NULL DEFAULT '',
			metrika_goal varchar(80) NOT NULL DEFAULT '',
			utm_source varchar(120) NOT NULL DEFAULT '',
			utm_medium varchar(120) NOT NULL DEFAULT '',
			utm_campaign varchar(120) NOT NULL DEFAULT '',
			utm_content varchar(120) NOT NULL DEFAULT '',
			utm_term varchar(120) NOT NULL DEFAULT '',
			referrer varchar(255) NOT NULL DEFAULT '',
			ua_class varchar(32) NOT NULL DEFAULT '',
			error_code varchar(64) NOT NULL DEFAULT '',
			attempt_count smallint(5) unsigned NOT NULL DEFAULT 0,
			is_qa tinyint(1) unsigned NOT NULL DEFAULT 0,
			PRIMARY KEY  (id),
			KEY created_at (created_at),
			KEY form_key (form_key),
			KEY delivery_status (delivery_status)
		) {$charset};";

		dbDelta( $sql );
		update_option( self::DB_VERSION_KEY, self::DB_VERSION, false );
	}

	/**
	 * Insert a lead before mail is attempted.
	 *
	 * @param array<string, mixed> $row Row.
	 * @return int Lead ID or 0.
	 */
	public static function insert( array $row ) {
		self::maybe_install_table();

		global $wpdb;
		$table = self::table_name();

		$data = array(
			'created_at'       => current_time( 'mysql' ),
			'form_key'         => self::sanitize_key_value( isset( $row['form_key'] ) ? $row['form_key'] : self::FORM_KEY, 32 ),
			'form_context'     => self::sanitize_text( isset( $row['form_context'] ) ? $row['form_context'] : '', 64 ),
			'source_url'       => self::sanitize_text( isset( $row['source_url'] ) ? $row['source_url'] : '', 500 ),
			'source_path'      => self::sanitize_text( isset( $row['source_path'] ) ? $row['source_path'] : '', 255 ),
			'source_post_id'   => isset( $row['source_post_id'] ) ? absint( $row['source_post_id'] ) : 0,
			'visitor_name'     => self::sanitize_text( isset( $row['visitor_name'] ) ? $row['visitor_name'] : '', 120 ),
			'phone'            => self::sanitize_text( isset( $row['phone'] ) ? $row['phone'] : '', 40 ),
			'email'            => self::sanitize_text( isset( $row['email'] ) ? $row['email'] : '', 120 ),
			'message'          => isset( $row['message'] ) ? self::sanitize_message( $row['message'] ) : '',
			'delivery_status'  => self::sanitize_status( isset( $row['delivery_status'] ) ? $row['delivery_status'] : self::STATUS_RECEIVED ),
			'smtp_status'      => self::sanitize_text( isset( $row['smtp_status'] ) ? $row['smtp_status'] : '', 32 ),
			'metrika_goal'     => self::sanitize_text( isset( $row['metrika_goal'] ) ? $row['metrika_goal'] : MailOps::metrika_goal(), 80 ),
			'utm_source'       => self::sanitize_text( isset( $row['utm_source'] ) ? $row['utm_source'] : '', 120 ),
			'utm_medium'       => self::sanitize_text( isset( $row['utm_medium'] ) ? $row['utm_medium'] : '', 120 ),
			'utm_campaign'     => self::sanitize_text( isset( $row['utm_campaign'] ) ? $row['utm_campaign'] : '', 120 ),
			'utm_content'      => self::sanitize_text( isset( $row['utm_content'] ) ? $row['utm_content'] : '', 120 ),
			'utm_term'         => self::sanitize_text( isset( $row['utm_term'] ) ? $row['utm_term'] : '', 120 ),
			'referrer'         => self::sanitize_text( isset( $row['referrer'] ) ? $row['referrer'] : '', 255 ),
			'ua_class'         => self::sanitize_text( isset( $row['ua_class'] ) ? $row['ua_class'] : '', 32 ),
			'error_code'       => self::sanitize_text( isset( $row['error_code'] ) ? $row['error_code'] : '', 64 ),
			'attempt_count'    => isset( $row['attempt_count'] ) ? absint( $row['attempt_count'] ) : 0,
			'is_qa'            => ! empty( $row['is_qa'] ) ? 1 : 0,
		);

		$ok = $wpdb->insert(
			$table,
			$data,
			array(
				'%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s',
				'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
				'%s', '%d', '%d',
			)
		);

		return false === $ok ? 0 : (int) $wpdb->insert_id;
	}

	/**
	 * Update delivery fields after mail attempt.
	 *
	 * @param int                  $id Lead ID.
	 * @param array<string, mixed> $fields Fields.
	 * @return bool
	 */
	public static function update_delivery( $id, array $fields ) {
		$id = (int) $id;
		if ( $id <= 0 ) {
			return false;
		}

		global $wpdb;
		$table = self::table_name();
		$data  = array();
		$fmt   = array();

		if ( isset( $fields['delivery_status'] ) ) {
			$data['delivery_status'] = self::sanitize_status( $fields['delivery_status'] );
			$fmt[]                   = '%s';
		}
		if ( isset( $fields['smtp_status'] ) ) {
			$data['smtp_status'] = self::sanitize_text( $fields['smtp_status'], 32 );
			$fmt[]               = '%s';
		}
		if ( isset( $fields['error_code'] ) ) {
			$data['error_code'] = self::sanitize_text( $fields['error_code'], 64 );
			$fmt[]              = '%s';
		}
		if ( isset( $fields['attempt_count'] ) ) {
			$data['attempt_count'] = absint( $fields['attempt_count'] );
			$fmt[]                 = '%d';
		}

		if ( empty( $data ) ) {
			return false;
		}

		$result = $wpdb->update( $table, $data, array( 'id' => $id ), $fmt, array( '%d' ) );
		return false !== $result;
	}

	/**
	 * @param int $id Lead ID.
	 * @return object|null
	 */
	public static function get( $id ) {
		self::maybe_install_table();
		global $wpdb;
		$table = self::table_name();
		$row   = $wpdb->get_row( $wpdb->prepare( "SELECT * FROM {$table} WHERE id = %d", (int) $id ) ); // phpcs:ignore WordPress.DB.PreparedSQL.InterpolatedNotPrepared
		return $row instanceof \stdClass ? $row : null;
	}

	/**
	 * Russian delivery status label.
	 *
	 * @param string $status Status.
	 * @return string
	 */
	public static function status_label( $status ) {
		$map = array(
			self::STATUS_RECEIVED        => __( 'Получена', 'shpigovsky-core' ),
			self::STATUS_MAIL_SUPPRESSED => __( 'Почта подавлена', 'shpigovsky-core' ),
			self::STATUS_SMTP_PENDING    => __( 'SMTP не подтверждён', 'shpigovsky-core' ),
			self::STATUS_MAIL_ACCEPTED   => __( 'Письмо принято SMTP', 'shpigovsky-core' ),
			self::STATUS_MAIL_ERROR      => __( 'Ошибка отправки', 'shpigovsky-core' ),
		);
		return isset( $map[ $status ] ) ? $map[ $status ] : $status;
	}

	/**
	 * Lightweight stats. QA rows excluded unless requested.
	 *
	 * @param bool $include_qa Include QA.
	 * @return array<string, int>
	 */
	public static function stats( $include_qa = false ) {
		self::maybe_install_table();
		global $wpdb;
		$table = self::table_name();
		$qa    = $include_qa ? '' : ' AND is_qa = 0';

		$now_local = current_time( 'timestamp' );
		$today     = wp_date( 'Y-m-d 00:00:00', $now_local );
		$d7        = wp_date( 'Y-m-d 00:00:00', $now_local - 7 * DAY_IN_SECONDS );
		$d30       = wp_date( 'Y-m-d 00:00:00', $now_local - 30 * DAY_IN_SECONDS );

		$count = static function ( $extra ) use ( $wpdb, $table, $qa ) {
			$sql = "SELECT COUNT(*) FROM {$table} WHERE 1=1 {$qa} {$extra}";
			return (int) $wpdb->get_var( $sql ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared
		};

		return array(
			'total'        => $count( '' ),
			'today'        => $count( $wpdb->prepare( ' AND created_at >= %s', $today ) ),
			'days_7'       => $count( $wpdb->prepare( ' AND created_at >= %s', $d7 ) ),
			'days_30'      => $count( $wpdb->prepare( ' AND created_at >= %s', $d30 ) ),
			'mail_ok'      => $count( $wpdb->prepare( ' AND delivery_status = %s', self::STATUS_MAIL_ACCEPTED ) ),
			'mail_error'   => $count( $wpdb->prepare( ' AND delivery_status = %s', self::STATUS_MAIL_ERROR ) ),
			'suppressed'   => $count( $wpdb->prepare( ' AND delivery_status = %s', self::STATUS_MAIL_SUPPRESSED ) ),
		);
	}

	/**
	 * Delete QA rows created by this wave.
	 *
	 * @return int Deleted count.
	 */
	public static function delete_qa_rows() {
		self::maybe_install_table();
		global $wpdb;
		$table = self::table_name();
		$n     = $wpdb->query( "DELETE FROM {$table} WHERE is_qa = 1" ); // phpcs:ignore WordPress.DB.PreparedSQL.InterpolatedNotPrepared
		return false === $n ? 0 : (int) $n;
	}

	/**
	 * UA class from user-agent string. Stores class only, not the raw UA.
	 *
	 * @param string $ua User agent.
	 * @return string
	 */
	public static function ua_class_from( $ua ) {
		$ua = strtolower( (string) $ua );
		if ( '' === $ua ) {
			return 'unknown';
		}
		if ( preg_match( '/bot|crawl|spider|slurp/i', $ua ) ) {
			return 'bot';
		}
		if ( preg_match( '/tablet|ipad/i', $ua ) ) {
			return 'tablet';
		}
		if ( preg_match( '/mobile|iphone|android/i', $ua ) ) {
			return 'mobile';
		}
		return 'desktop';
	}

	/**
	 * @param mixed $status Status.
	 * @return string
	 */
	private static function sanitize_status( $status ) {
		$status = strtoupper( sanitize_key( (string) $status ) );
		$allowed = array(
			self::STATUS_RECEIVED,
			self::STATUS_MAIL_SUPPRESSED,
			self::STATUS_SMTP_PENDING,
			self::STATUS_MAIL_ACCEPTED,
			self::STATUS_MAIL_ERROR,
		);
		return in_array( $status, $allowed, true ) ? $status : self::STATUS_RECEIVED;
	}

	/**
	 * @param mixed $value Value.
	 * @param int   $max Max.
	 * @return string
	 */
	private static function sanitize_text( $value, $max ) {
		if ( ! is_string( $value ) && ! is_numeric( $value ) ) {
			return '';
		}
		$value = sanitize_text_field( (string) $value );
		if ( function_exists( 'mb_substr' ) ) {
			return mb_substr( $value, 0, $max, 'UTF-8' );
		}
		return substr( $value, 0, $max );
	}

	/**
	 * @param mixed $value Key.
	 * @param int   $max Max.
	 * @return string
	 */
	private static function sanitize_key_value( $value, $max ) {
		$key = sanitize_key( (string) $value );
		return substr( $key, 0, $max );
	}

	/**
	 * @param mixed $message Message.
	 * @return string
	 */
	private static function sanitize_message( $message ) {
		if ( ! is_string( $message ) && ! is_numeric( $message ) ) {
			return '';
		}
		$text = sanitize_textarea_field( (string) $message );
		if ( function_exists( 'mb_substr' ) ) {
			return mb_substr( $text, 0, 4000, 'UTF-8' );
		}
		return substr( $text, 0, 4000 );
	}
}
