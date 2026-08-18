<?php
/**
 * WordPress personal-data exporter/eraser for form leads.
 *
 * Compatibility with Tools → Export/Erase personal data. Not a legal compliance claim.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Privacy;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Export / erase leads matched by email.
 */
final class LeadPersonalData implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'privacy.lead-personal-data';
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
		add_filter( 'wp_privacy_personal_data_exporters', array( __CLASS__, 'register_exporter' ) );
		add_filter( 'wp_privacy_personal_data_erasers', array( __CLASS__, 'register_eraser' ) );
	}

	/**
	 * @param array<string, mixed> $exporters Exporters.
	 * @return array<string, mixed>
	 */
	public static function register_exporter( $exporters ) {
		$exporters['fp02-form-leads'] = array(
			'exporter_friendly_name' => __( 'Заявки с сайта', 'shpigovsky-core' ),
			'callback'               => array( __CLASS__, 'export' ),
		);
		return $exporters;
	}

	/**
	 * @param array<string, mixed> $erasers Erasers.
	 * @return array<string, mixed>
	 */
	public static function register_eraser( $erasers ) {
		$erasers['fp02-form-leads'] = array(
			'eraser_friendly_name' => __( 'Заявки с сайта', 'shpigovsky-core' ),
			'callback'             => array( __CLASS__, 'erase' ),
		);
		return $erasers;
	}

	/**
	 * @param string $email Email.
	 * @param int    $page Page.
	 * @return array<string, mixed>
	 */
	public static function export( $email, $page = 1 ) {
		unset( $page );
		LeadRegistry::maybe_install_table();
		global $wpdb;
		$table = LeadRegistry::table_name();
		$rows  = $wpdb->get_results(
			$wpdb->prepare( "SELECT * FROM {$table} WHERE email = %s ORDER BY id ASC", sanitize_email( $email ) ) // phpcs:ignore WordPress.DB.PreparedSQL.InterpolatedNotPrepared
		);
		$items = array();
		if ( is_array( $rows ) ) {
			foreach ( $rows as $row ) {
				$items[] = array(
					'group_id'    => 'fp02-form-leads',
					'group_label' => __( 'Заявки с сайта', 'shpigovsky-core' ),
					'item_id'     => 'lead-' . (int) $row->id,
					'data'        => array(
						array(
							'name'  => __( 'Дата', 'shpigovsky-core' ),
							'value' => $row->created_at,
						),
						array(
							'name'  => __( 'Имя', 'shpigovsky-core' ),
							'value' => $row->visitor_name,
						),
						array(
							'name'  => __( 'Телефон', 'shpigovsky-core' ),
							'value' => $row->phone,
						),
						array(
							'name'  => __( 'Email', 'shpigovsky-core' ),
							'value' => $row->email,
						),
						array(
							'name'  => __( 'Сообщение', 'shpigovsky-core' ),
							'value' => $row->message,
						),
					),
				);
			}
		}
		return array(
			'data' => $items,
			'done' => true,
		);
	}

	/**
	 * @param string $email Email.
	 * @param int    $page Page.
	 * @return array<string, mixed>
	 */
	public static function erase( $email, $page = 1 ) {
		unset( $page );
		LeadRegistry::maybe_install_table();
		global $wpdb;
		$table = LeadRegistry::table_name();
		$n     = $wpdb->delete( $table, array( 'email' => sanitize_email( $email ) ), array( '%s' ) );
		$n     = false === $n ? 0 : (int) $n;
		return array(
			'items_removed'  => $n > 0,
			'items_retained' => false,
			'messages'       => array(),
			'done'           => true,
		);
	}
}
