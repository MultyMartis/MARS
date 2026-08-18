<?php
/**
 * Admin: Заявки с сайта — business-facing lead history.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Leads list / detail / lightweight stats.
 */
final class LeadsAdmin implements ModuleInterface {

	public const MENU_SLUG   = 'fp02-form-leads';
	public const CAPABILITY  = 'manage_options';
	public const PER_PAGE    = 40;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.leads';
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
		add_action( 'admin_menu', array( __CLASS__, 'register_menu' ) );
	}

	/**
	 * Top-level business menu.
	 */
	public static function register_menu() {
		add_menu_page(
			__( 'Заявки с сайта', 'shpigovsky-core' ),
			__( 'Заявки', 'shpigovsky-core' ),
			self::CAPABILITY,
			self::MENU_SLUG,
			array( __CLASS__, 'render_page' ),
			'dashicons-email-alt',
			56
		);
	}

	/**
	 * List or detail.
	 */
	public static function render_page() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ) );
		}

		LeadRegistry::maybe_install_table();

		$view_id = isset( $_GET['lead'] ) ? absint( $_GET['lead'] ) : 0; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		if ( $view_id > 0 ) {
			self::render_detail( $view_id );
			return;
		}

		self::render_list();
	}

	/**
	 * List + stats + filters.
	 */
	private static function render_list() {
		global $wpdb;
		$table = LeadRegistry::table_name();

		$from   = isset( $_GET['fp02_from'] ) ? sanitize_text_field( wp_unslash( $_GET['fp02_from'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$to     = isset( $_GET['fp02_to'] ) ? sanitize_text_field( wp_unslash( $_GET['fp02_to'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$form   = isset( $_GET['fp02_form'] ) ? sanitize_key( wp_unslash( $_GET['fp02_form'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$status = isset( $_GET['fp02_status'] ) ? sanitize_key( wp_unslash( $_GET['fp02_status'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$utm    = isset( $_GET['fp02_utm'] ) ? sanitize_text_field( wp_unslash( $_GET['fp02_utm'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$path   = isset( $_GET['fp02_path'] ) ? sanitize_text_field( wp_unslash( $_GET['fp02_path'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$show_qa = isset( $_GET['fp02_qa'] ) && '1' === $_GET['fp02_qa']; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$page    = isset( $_GET['paged'] ) ? max( 1, absint( $_GET['paged'] ) ) : 1; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$offset  = ( $page - 1 ) * self::PER_PAGE;

		$where  = array( '1=1' );
		$params = array();
		if ( ! $show_qa ) {
			$where[] = 'is_qa = 0';
		}
		if ( preg_match( '/^\d{4}-\d{2}-\d{2}$/', $from ) ) {
			$where[]  = 'created_at >= %s';
			$params[] = $from . ' 00:00:00';
		}
		if ( preg_match( '/^\d{4}-\d{2}-\d{2}$/', $to ) ) {
			$where[]  = 'created_at <= %s';
			$params[] = $to . ' 23:59:59';
		}
		if ( '' !== $form ) {
			$where[]  = 'form_key = %s';
			$params[] = $form;
		}
		if ( '' !== $status ) {
			$where[]  = 'delivery_status = %s';
			$params[] = strtoupper( $status );
		}
		if ( '' !== $utm ) {
			$where[]  = 'utm_source = %s';
			$params[] = $utm;
		}
		if ( '' !== $path ) {
			$where[]  = 'source_path LIKE %s';
			$params[] = '%' . $wpdb->esc_like( $path ) . '%';
		}

		$where_sql = implode( ' AND ', $where );
		$count_sql = "SELECT COUNT(*) FROM {$table} WHERE {$where_sql}";
		$total     = empty( $params )
			? (int) $wpdb->get_var( $count_sql ) // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared
			: (int) $wpdb->get_var( $wpdb->prepare( $count_sql, $params ) ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared

		$list_sql    = "SELECT * FROM {$table} WHERE {$where_sql} ORDER BY id DESC LIMIT %d OFFSET %d";
		$list_params = array_merge( $params, array( self::PER_PAGE, $offset ) );
		$rows        = $wpdb->get_results( $wpdb->prepare( $list_sql, $list_params ) ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared

		$stats = LeadRegistry::stats( false );

		echo '<div class="wrap">';
		echo '<h1>' . esc_html__( 'Заявки с сайта', 'shpigovsky-core' ) . '</h1>';
		echo '<p class="description">' . esc_html__( 'Внутренний журнал заявок. Письмо — транспорт, не доказательство, что заявка существовала.', 'shpigovsky-core' ) . '</p>';

		echo '<div class="fp02-lead-stats" style="display:flex;flex-wrap:wrap;gap:12px;margin:16px 0;">';
		self::stat_card( __( 'Всего', 'shpigovsky-core' ), $stats['total'] );
		self::stat_card( __( 'Сегодня', 'shpigovsky-core' ), $stats['today'] );
		self::stat_card( __( '7 дней', 'shpigovsky-core' ), $stats['days_7'] );
		self::stat_card( __( '30 дней', 'shpigovsky-core' ), $stats['days_30'] );
		self::stat_card( __( 'Письмо принято SMTP', 'shpigovsky-core' ), $stats['mail_ok'] );
		self::stat_card( __( 'Ошибки отправки', 'shpigovsky-core' ), $stats['mail_error'] );
		echo '</div>';

		if ( 0 === (int) MailOps::get_config()['lead_retention_days'] ) {
			echo '<p class="description"><strong>' . esc_html__( 'FORM LEAD RETENTION PERIOD — OPERATOR DECISION REQUIRED', 'shpigovsky-core' ) . '</strong></p>';
		}

		echo '<form method="get" style="margin:12px 0;">';
		echo '<input type="hidden" name="page" value="' . esc_attr( self::MENU_SLUG ) . '" />';
		echo '<input type="date" name="fp02_from" value="' . esc_attr( $from ) . '" /> ';
		echo '<input type="date" name="fp02_to" value="' . esc_attr( $to ) . '" /> ';
		echo '<select name="fp02_form"><option value="">' . esc_html__( 'Все формы', 'shpigovsky-core' ) . '</option>';
		printf(
			'<option value="consultation"%s>%s</option>',
			selected( $form, 'consultation', false ),
			esc_html__( 'Консультация', 'shpigovsky-core' )
		);
		echo '</select> ';
		echo '<select name="fp02_status"><option value="">' . esc_html__( 'Все статусы', 'shpigovsky-core' ) . '</option>';
		foreach ( array(
			LeadRegistry::STATUS_RECEIVED,
			LeadRegistry::STATUS_MAIL_SUPPRESSED,
			LeadRegistry::STATUS_SMTP_PENDING,
			LeadRegistry::STATUS_MAIL_ACCEPTED,
			LeadRegistry::STATUS_MAIL_ERROR,
		) as $st ) {
			printf(
				'<option value="%1$s"%2$s>%3$s</option>',
				esc_attr( $st ),
				selected( strtoupper( $status ), $st, false ),
				esc_html( LeadRegistry::status_label( $st ) )
			);
		}
		echo '</select> ';
		echo '<input type="text" name="fp02_path" value="' . esc_attr( $path ) . '" placeholder="' . esc_attr__( 'Страница', 'shpigovsky-core' ) . '" /> ';
		echo '<input type="text" name="fp02_utm" value="' . esc_attr( $utm ) . '" placeholder="utm_source" /> ';
		echo '<label><input type="checkbox" name="fp02_qa" value="1"' . checked( $show_qa, true, false ) . ' /> ' . esc_html__( 'QA', 'shpigovsky-core' ) . '</label> ';
		submit_button( __( 'Фильтр', 'shpigovsky-core' ), 'secondary', '', false );
		echo '</form>';

		echo '<table class="wp-list-table widefat striped"><thead><tr>';
		echo '<th>' . esc_html__( 'Дата', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Форма', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Имя', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Телефон', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Email', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Страница', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Статус отправки', 'shpigovsky-core' ) . '</th>';
		echo '<th>UTM</th>';
		echo '</tr></thead><tbody>';

		if ( empty( $rows ) ) {
			echo '<tr><td colspan="8">' . esc_html__( 'Заявок пока нет.', 'shpigovsky-core' ) . '</td></tr>';
		} else {
			foreach ( $rows as $row ) {
				$detail = add_query_arg(
					array(
						'page' => self::MENU_SLUG,
						'lead' => (int) $row->id,
					),
					admin_url( 'admin.php' )
				);
				echo '<tr>';
				echo '<td><a href="' . esc_url( $detail ) . '">' . esc_html( $row->created_at ) . '</a></td>';
				echo '<td>' . esc_html( self::form_label( $row->form_key ) ) . '</td>';
				echo '<td>' . esc_html( $row->visitor_name ) . '</td>';
				echo '<td>' . esc_html( $row->phone ) . '</td>';
				echo '<td>' . esc_html( $row->email ) . '</td>';
				echo '<td>' . esc_html( $row->source_path !== '' ? $row->source_path : $row->source_url ) . '</td>';
				echo '<td>' . esc_html( LeadRegistry::status_label( $row->delivery_status ) ) . '</td>';
				echo '<td>' . esc_html( $row->utm_source ) . '</td>';
				echo '</tr>';
			}
		}
		echo '</tbody></table>';

		$pages = (int) ceil( $total / self::PER_PAGE );
		if ( $pages > 1 ) {
			echo '<p>';
			for ( $i = 1; $i <= $pages; $i++ ) {
				$url = add_query_arg( 'paged', $i );
				printf(
					'<a class="button%1$s" href="%2$s">%3$d</a> ',
					$i === $page ? ' button-primary' : '',
					esc_url( $url ),
					$i
				);
			}
			echo '</p>';
		}

		echo '</div>';
	}

	/**
	 * Safe detail. No SMTP password. No raw dumps.
	 *
	 * @param int $id Lead ID.
	 */
	private static function render_detail( $id ) {
		$row = LeadRegistry::get( $id );
		echo '<div class="wrap">';
		echo '<h1>' . esc_html__( 'Заявка', 'shpigovsky-core' ) . '</h1>';
		echo '<p><a href="' . esc_url( admin_url( 'admin.php?page=' . self::MENU_SLUG ) ) . '">&larr; ' . esc_html__( 'К списку', 'shpigovsky-core' ) . '</a></p>';
		if ( ! $row ) {
			echo '<p>' . esc_html__( 'Заявка не найдена.', 'shpigovsky-core' ) . '</p></div>';
			return;
		}

		$pairs = array(
			__( 'Дата', 'shpigovsky-core' )             => $row->created_at,
			__( 'Форма', 'shpigovsky-core' )            => self::form_label( $row->form_key ) . ' (' . $row->form_context . ')',
			__( 'Имя', 'shpigovsky-core' )              => $row->visitor_name,
			__( 'Телефон', 'shpigovsky-core' )          => $row->phone,
			__( 'Email', 'shpigovsky-core' )            => $row->email,
			__( 'Сообщение', 'shpigovsky-core' )        => $row->message,
			__( 'Страница', 'shpigovsky-core' )         => $row->source_url,
			__( 'Путь', 'shpigovsky-core' )             => $row->source_path,
			__( 'ID страницы', 'shpigovsky-core' )      => (string) $row->source_post_id,
			__( 'Статус отправки', 'shpigovsky-core' )  => LeadRegistry::status_label( $row->delivery_status ),
			__( 'SMTP', 'shpigovsky-core' )             => $row->smtp_status,
			__( 'Категория ошибки', 'shpigovsky-core' )  => $row->error_code,
			__( 'Цель Метрики', 'shpigovsky-core' )     => $row->metrika_goal,
			'utm_source'                                  => $row->utm_source,
			'utm_medium'                                  => $row->utm_medium,
			'utm_campaign'                                => $row->utm_campaign,
			'utm_content'                                 => $row->utm_content,
			'utm_term'                                    => $row->utm_term,
			__( 'Referrer', 'shpigovsky-core' )           => $row->referrer,
			__( 'Класс устройства', 'shpigovsky-core' )   => $row->ua_class,
			__( 'Попыток', 'shpigovsky-core' )            => (string) $row->attempt_count,
			'QA'                                          => $row->is_qa ? 'yes' : 'no',
		);

		echo '<table class="widefat striped" style="max-width:860px;">';
		foreach ( $pairs as $label => $value ) {
			echo '<tr><th style="width:240px;">' . esc_html( $label ) . '</th><td>' . nl2br( esc_html( (string) $value ) ) . '</td></tr>';
		}
		echo '</table>';
		echo '<p class="description">' . esc_html__( 'Пароль SMTP и сырые дампы сервера здесь не хранятся и не показываются.', 'shpigovsky-core' ) . '</p>';
		echo '</div>';
	}

	/**
	 * @param string $label Label.
	 * @param int    $value Value.
	 */
	private static function stat_card( $label, $value ) {
		echo '<div style="min-width:120px;padding:10px 14px;background:#fff;border:1px solid #dcdcde;">';
		echo '<div style="font-size:22px;font-weight:600;">' . esc_html( (string) $value ) . '</div>';
		echo '<div>' . esc_html( $label ) . '</div></div>';
	}

	/**
	 * @param string $key Form key.
	 * @return string
	 */
	private static function form_label( $key ) {
		if ( 'consultation' === $key ) {
			return __( 'Консультация', 'shpigovsky-core' );
		}
		return $key;
	}
}
