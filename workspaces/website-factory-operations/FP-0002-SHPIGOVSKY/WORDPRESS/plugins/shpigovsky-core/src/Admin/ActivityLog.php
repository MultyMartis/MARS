<?php
/**
 * Bounded WordPress user activity log — PROD-P12.
 *
 * Stores create/update events for editable content types.
 * Not an enterprise SIEM; Administrator-only Admin UI.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\ContentTypes\Specialist;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Activity log storage + Admin page.
 */
final class ActivityLog implements ModuleInterface {

	public const DB_VERSION      = '1';
	public const DB_VERSION_KEY  = 'fp02_activity_log_db_version';
	public const RETENTION_MAX   = 8000;
	public const MENU_SLUG       = 'fp02-activity-log';
	public const PER_PAGE        = 50;

	/**
	 * In-request de-dupe keys.
	 *
	 * @var array<string, bool>
	 */
	private static $logged_keys = array();

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.activity-log';
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
		add_action( 'admin_menu', array( __CLASS__, 'register_menu' ) );
		add_action( 'save_post', array( __CLASS__, 'on_save_post' ), 30, 3 );
		add_action( 'transition_post_status', array( __CLASS__, 'on_transition' ), 20, 3 );
	}

	/**
	 * Table name with WP prefix.
	 *
	 * @return string
	 */
	public static function table_name() {
		global $wpdb;
		return $wpdb->prefix . 'user_activity_log';
	}

	/**
	 * Tracked public/editable post types.
	 *
	 * @return array<int, string>
	 */
	public static function tracked_post_types() {
		return array(
			'page',
			'post',
			Service::POST_TYPE,
			Specialist::POST_TYPE,
		);
	}

	/**
	 * Human type labels (RU).
	 *
	 * @return array<string, string>
	 */
	public static function type_labels() {
		return array(
			'page'       => __( 'Page', 'shpigovsky-core' ),
			'post'       => __( 'Article', 'shpigovsky-core' ),
			'service'    => __( 'Service', 'shpigovsky-core' ),
			'specialist' => __( 'Specialist', 'shpigovsky-core' ),
			'review'     => __( 'Review', 'shpigovsky-core' ),
			'setting'    => __( 'Настройка', 'shpigovsky-core' ),
		);
	}

	/**
	 * Create/upgrade table via dbDelta.
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
			user_id bigint(20) unsigned NOT NULL DEFAULT 0,
			action varchar(32) NOT NULL DEFAULT '',
			object_id bigint(20) unsigned NOT NULL DEFAULT 0,
			object_type varchar(32) NOT NULL DEFAULT '',
			object_title varchar(255) NOT NULL DEFAULT '',
			object_status varchar(32) NOT NULL DEFAULT '',
			created_at datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
			PRIMARY KEY  (id),
			KEY created_at (created_at),
			KEY user_id (user_id),
			KEY object_type (object_type),
			KEY action (action)
		) {$charset};";

		dbDelta( $sql );
		update_option( self::DB_VERSION_KEY, self::DB_VERSION, false );
	}

	/**
	 * Admin menu.
	 */
	public static function register_menu() {
		add_menu_page(
			__( 'Журнал действий', 'shpigovsky-core' ),
			__( 'Журнал действий', 'shpigovsky-core' ),
			'manage_options',
			self::MENU_SLUG,
			array( __CLASS__, 'render_page' ),
			'dashicons-backup',
			58
		);
	}

	/**
	 * save_post logger (create/update).
	 *
	 * @param int      $post_id Post ID.
	 * @param \WP_Post $post Post.
	 * @param bool     $update Whether updating.
	 */
	public static function on_save_post( $post_id, $post, $update ) {
		if ( ! $post instanceof \WP_Post ) {
			return;
		}

		if ( ! self::should_log_post( $post ) ) {
			return;
		}

		if ( 'trash' === $post->post_status ) {
			return;
		}

		$action = $update ? 'updated' : 'created';
		self::log_event( $action, $post );
	}

	/**
	 * Status transition for trash / restore only (avoids duplicate create noise).
	 *
	 * @param string   $new_status New status.
	 * @param string   $old_status Old status.
	 * @param \WP_Post $post Post.
	 */
	public static function on_transition( $new_status, $old_status, $post ) {
		if ( ! $post instanceof \WP_Post ) {
			return;
		}

		if ( ! self::should_log_post( $post ) && 'trash' !== $new_status ) {
			return;
		}

		if ( ! in_array( $post->post_type, self::tracked_post_types(), true ) ) {
			return;
		}

		if ( wp_is_post_autosave( $post->ID ) || wp_is_post_revision( $post->ID ) ) {
			return;
		}

		if ( 'trash' === $new_status && 'trash' !== $old_status ) {
			self::log_event( 'trashed', $post );
			return;
		}

		if ( 'trash' === $old_status && 'trash' !== $new_status ) {
			self::log_event( 'restored', $post );
		}
	}

	/**
	 * Whether this post should be logged.
	 *
	 * @param \WP_Post $post Post.
	 * @return bool
	 */
	private static function should_log_post( \WP_Post $post ) {
		if ( ! in_array( $post->post_type, self::tracked_post_types(), true ) ) {
			return false;
		}

		if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
			return false;
		}

		if ( wp_is_post_autosave( $post->ID ) || wp_is_post_revision( $post->ID ) ) {
			return false;
		}

		if ( in_array( $post->post_status, array( 'auto-draft', 'inherit' ), true ) ) {
			return false;
		}

		// Skip bulk programmatic migrations unless flagged intentionally.
		if ( defined( 'FP02_ACTIVITY_LOG_SKIP' ) && FP02_ACTIVITY_LOG_SKIP ) {
			return false;
		}

		return true;
	}

	/**
	 * Insert one log row with de-dupe.
	 *
	 * @param string   $action Action key.
	 * @param \WP_Post $post Post.
	 */
	public static function log_event( $action, \WP_Post $post ) {
		self::maybe_install_table();

		$user_id = get_current_user_id();
		$key     = $action . ':' . (int) $post->ID . ':' . (int) $user_id;

		if ( isset( self::$logged_keys[ $key ] ) ) {
			return;
		}
		self::$logged_keys[ $key ] = true;

		global $wpdb;
		$table = self::table_name();

		$wpdb->insert(
			$table,
			array(
				'user_id'       => (int) $user_id,
				'action'        => sanitize_key( $action ),
				'object_id'     => (int) $post->ID,
				'object_type'   => sanitize_key( $post->post_type ),
				'object_title'  => mb_substr( wp_strip_all_tags( $post->post_title ), 0, 255 ),
				'object_status' => sanitize_key( $post->post_status ),
				'created_at'    => current_time( 'mysql' ),
			),
			array( '%d', '%s', '%d', '%s', '%s', '%s', '%s' )
		);

		self::maybe_prune();
	}

	/**
	 * Log a non-content operational action (indexing, settings).
	 *
	 * @param string $action Action key.
	 * @param string $object_type Object type key.
	 * @param string $object_title Short label, no secrets.
	 * @param int    $object_id Optional object id.
	 */
	public static function log_system_event( $action, $object_type, $object_title, $object_id = 0 ) {
		self::maybe_install_table();

		$user_id = get_current_user_id();
		$key     = sanitize_key( $action ) . ':' . sanitize_key( $object_type ) . ':' . (int) $object_id . ':' . (int) $user_id;

		if ( isset( self::$logged_keys[ $key ] ) ) {
			return;
		}
		self::$logged_keys[ $key ] = true;

		global $wpdb;
		$table = self::table_name();

		$wpdb->insert(
			$table,
			array(
				'user_id'       => (int) $user_id,
				'action'        => sanitize_key( $action ),
				'object_id'     => (int) $object_id,
				'object_type'   => sanitize_key( $object_type ),
				'object_title'  => mb_substr( wp_strip_all_tags( (string) $object_title ), 0, 255 ),
				'object_status' => 'system',
				'created_at'    => current_time( 'mysql' ),
			),
			array( '%d', '%s', '%d', '%s', '%s', '%s', '%s' )
		);

		self::maybe_prune();
	}

	/**
	 * Retain newest N rows.
	 */
	private static function maybe_prune() {
		global $wpdb;
		$table = self::table_name();
		$max   = (int) self::RETENTION_MAX;

		$count = (int) $wpdb->get_var( "SELECT COUNT(*) FROM {$table}" ); // phpcs:ignore WordPress.DB.PreparedSQL.InterpolatedNotPrepared
		if ( $count <= $max ) {
			return;
		}

		$delete = $count - $max;
		$wpdb->query( // phpcs:ignore WordPress.DB.PreparedSQL.InterpolatedNotPrepared
			$wpdb->prepare(
				"DELETE FROM {$table} ORDER BY id ASC LIMIT %d",
				$delete
			)
		);
	}

	/**
	 * Action label RU.
	 *
	 * @param string $action Action key.
	 * @return string
	 */
	public static function action_label( $action ) {
		$map = array(
			'created'           => __( 'Created', 'shpigovsky-core' ),
			'updated'           => __( 'Updated', 'shpigovsky-core' ),
			'trashed'           => __( 'Moved to trash', 'shpigovsky-core' ),
			'restored'          => __( 'Restored', 'shpigovsky-core' ),
			'indexing_opened'     => __( 'Индексация открыта', 'shpigovsky-core' ),
			'indexing_closed'     => __( 'Индексация закрыта', 'shpigovsky-core' ),
			'smtp_config_updated' => __( 'Почта: настройки сохранены', 'shpigovsky-core' ),
			'smtp_test_ok'        => __( 'Проверка SMTP: успех', 'shpigovsky-core' ),
			'smtp_test_fail'      => __( 'Проверка SMTP: ошибка', 'shpigovsky-core' ),
			'smtp_activated'      => __( 'Почта: отправка включена', 'shpigovsky-core' ),
			'smtp_deactivated'    => __( 'Почта: отправка выключена', 'shpigovsky-core' ),
		);
		return isset( $map[ $action ] ) ? $map[ $action ] : $action;
	}

	/**
	 * Resolve a log user label. User 0 is system/CLI, never "#0".
	 *
	 * @param int $user_id User ID.
	 * @return string
	 */
	public static function user_label( $user_id ) {
		$user_id = (int) $user_id;
		if ( $user_id <= 0 ) {
			return __( 'System', 'shpigovsky-core' );
		}

		$user = get_userdata( $user_id );
		if ( ! $user ) {
			return __( 'System', 'shpigovsky-core' );
		}

		$name = $user->display_name ? $user->display_name : $user->user_login;
		return $name . ' (' . $user->user_login . ')';
	}

	/**
	 * Admin list page.
	 */
	public static function render_page() {
		if ( ! current_user_can( 'manage_options' ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ) );
		}

		self::maybe_install_table();

		global $wpdb;
		$table = self::table_name();

		$user_filter   = isset( $_GET['fp02_user'] ) ? sanitize_text_field( wp_unslash( $_GET['fp02_user'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$action_filter = isset( $_GET['fp02_action'] ) ? sanitize_key( wp_unslash( $_GET['fp02_action'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$type_filter   = isset( $_GET['fp02_type'] ) ? sanitize_key( wp_unslash( $_GET['fp02_type'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$page          = isset( $_GET['paged'] ) ? max( 1, absint( $_GET['paged'] ) ) : 1; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$per_page      = self::PER_PAGE;
		$offset        = ( $page - 1 ) * $per_page;

		$where  = array( '1=1' );
		$params = array();

		if ( '0' === $user_filter || 'system' === $user_filter ) {
			$where[]  = 'user_id = %d';
			$params[] = 0;
		} elseif ( '' !== $user_filter && ctype_digit( $user_filter ) ) {
			$where[]  = 'user_id = %d';
			$params[] = (int) $user_filter;
		}
		if ( '' !== $action_filter ) {
			$where[]  = 'action = %s';
			$params[] = $action_filter;
		}
		if ( '' !== $type_filter ) {
			$where[]  = 'object_type = %s';
			$params[] = $type_filter;
		}

		$where_sql = implode( ' AND ', $where );

		$count_sql = "SELECT COUNT(*) FROM {$table} WHERE {$where_sql}";
		$total     = empty( $params )
			? (int) $wpdb->get_var( $count_sql ) // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared
			: (int) $wpdb->get_var( $wpdb->prepare( $count_sql, $params ) ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared

		$list_sql = "SELECT * FROM {$table} WHERE {$where_sql} ORDER BY id DESC LIMIT %d OFFSET %d";
		$list_params = array_merge( $params, array( $per_page, $offset ) );
		$rows = $wpdb->get_results( $wpdb->prepare( $list_sql, $list_params ) ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared

		$type_labels = self::type_labels();
		$users       = get_users( array( 'fields' => array( 'ID', 'display_name', 'user_login' ) ) );

		echo '<div class="wrap">';
		echo '<h1>' . esc_html__( 'Журнал действий', 'shpigovsky-core' ) . '</h1>';
		echo '<p class="description">' . esc_html__( 'Базовый журнал создания и изменения контента. Хранит до 8000 последних записей. Не фиксирует пароли и тела записей.', 'shpigovsky-core' ) . '</p>';

		echo '<form method="get" class="fp02-activity-log-filters" style="margin:16px 0;">';
		echo '<input type="hidden" name="page" value="' . esc_attr( self::MENU_SLUG ) . '" />';
		echo '<select name="fp02_user"><option value="">' . esc_html__( 'All users', 'shpigovsky-core' ) . '</option>';
		printf(
			'<option value="0"%s>%s</option>',
			selected( $user_filter, '0', false ),
			esc_html__( 'System', 'shpigovsky-core' )
		);
		foreach ( $users as $u ) {
			printf(
				'<option value="%1$d"%2$s>%3$s (%4$s)</option>',
				(int) $u->ID,
				selected( $user_filter, (string) $u->ID, false ),
				esc_html( $u->display_name ? $u->display_name : $u->user_login ),
				esc_html( $u->user_login )
			);
		}
		echo '</select> ';

		echo '<select name="fp02_action"><option value="">' . esc_html__( 'Все действия', 'shpigovsky-core' ) . '</option>';
		foreach ( array( 'created', 'updated', 'trashed', 'restored', 'indexing_opened', 'indexing_closed', 'smtp_config_updated', 'smtp_test_ok', 'smtp_test_fail', 'smtp_activated', 'smtp_deactivated' ) as $act ) {
			printf(
				'<option value="%1$s"%2$s>%3$s</option>',
				esc_attr( $act ),
				selected( $action_filter, $act, false ),
				esc_html( self::action_label( $act ) )
			);
		}
		echo '</select> ';

		echo '<select name="fp02_type"><option value="">' . esc_html__( 'Все типы', 'shpigovsky-core' ) . '</option>';
		foreach ( $type_labels as $key => $label ) {
			printf(
				'<option value="%1$s"%2$s>%3$s</option>',
				esc_attr( $key ),
				selected( $type_filter, $key, false ),
				esc_html( $label )
			);
		}
		echo '</select> ';
		submit_button( __( 'Фильтр', 'shpigovsky-core' ), 'secondary', '', false );
		echo '</form>';

		echo '<table class="wp-list-table widefat striped"><thead><tr>';
		echo '<th>' . esc_html__( 'Date and time', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'User', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Action', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Type', 'shpigovsky-core' ) . '</th>';
		echo '<th>' . esc_html__( 'Object', 'shpigovsky-core' ) . '</th>';
		echo '</tr></thead><tbody>';

		if ( empty( $rows ) ) {
			echo '<tr><td colspan="5">' . esc_html__( 'Записей пока нет.', 'shpigovsky-core' ) . '</td></tr>';
		} else {
			foreach ( $rows as $row ) {
				$user_label = self::user_label( (int) $row->user_id );
				$type_label = isset( $type_labels[ $row->object_type ] ) ? $type_labels[ $row->object_type ] : $row->object_type;
				$edit_link  = get_edit_post_link( (int) $row->object_id, 'raw' );
				$title      = $row->object_title !== '' ? $row->object_title : ( '#' . (int) $row->object_id );

				echo '<tr>';
				echo '<td>' . esc_html( $row->created_at ) . '</td>';
				echo '<td>' . esc_html( $user_label ) . '</td>';
				echo '<td>' . esc_html( self::action_label( $row->action ) ) . '</td>';
				echo '<td>' . esc_html( $type_label ) . '</td>';
				echo '<td>';
				if ( $edit_link ) {
					printf( '<a href="%1$s">%2$s</a>', esc_url( $edit_link ), esc_html( $title ) );
				} else {
					echo esc_html( $title );
				}
				echo ' <span class="description">#' . (int) $row->object_id . '</span>';
				echo '</td>';
				echo '</tr>';
			}
		}

		echo '</tbody></table>';

		$total_pages = (int) ceil( $total / $per_page );
		if ( $total_pages > 1 ) {
			echo '<div class="tablenav"><div class="tablenav-pages">';
			echo paginate_links(
				array(
					'base'      => add_query_arg( 'paged', '%#%' ),
					'format'    => '',
					'prev_text' => '&laquo;',
					'next_text' => '&raquo;',
					'total'     => $total_pages,
					'current'   => $page,
				)
			);
			echo '</div></div>';
		}

		echo '</div>';
	}
}
