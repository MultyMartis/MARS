<?php
/**
 * Admin: Настройки сайта → Почта и формы.
 *
 * One operator-facing source of truth for SMTP / form delivery config.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Mail and forms settings screen.
 */
final class MailFormsSettings implements ModuleInterface {

	public const MENU_SLUG        = 'fp02-site-settings-mail-forms';
	public const CAPABILITY       = 'manage_options';
	public const SAVE_ACTION      = 'fp02_save_mail_forms';
	public const SAVE_NONCE       = 'fp02_save_mail_forms';
	public const TEST_ACTION      = 'fp02_test_smtp';
	public const TEST_NONCE       = 'fp02_test_smtp';
	public const ACTIVATE_ACTION  = 'fp02_activate_smtp';
	public const ACTIVATE_NONCE   = 'fp02_activate_smtp';
	public const NOTICE_QUERY     = 'fp02_mail';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.mail-forms';
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
		add_action( 'admin_menu', array( __CLASS__, 'register_menu' ), 100 );
		add_action( 'admin_enqueue_scripts', array( __CLASS__, 'enqueue_assets' ) );
		add_action( 'admin_post_' . self::SAVE_ACTION, array( __CLASS__, 'handle_save' ) );
		add_action( 'admin_post_' . self::TEST_ACTION, array( __CLASS__, 'handle_test' ) );
		add_action( 'admin_post_' . self::ACTIVATE_ACTION, array( __CLASS__, 'handle_activate' ) );
		add_action( 'admin_notices', array( __CLASS__, 'render_notice' ) );
	}

	/**
	 * Submenu under the visible Настройки сайта parent.
	 *
	 * Priority 100: after ACF options pages (99). Parent slug is the
	 * resolved ACF menu slug, not the logical PARENT_SLUG.
	 */
	public static function register_menu() {
		add_submenu_page(
			OptionsPage::visible_menu_slug(),
			__( 'Почта и формы', 'shpigovsky-core' ),
			__( 'Почта и формы', 'shpigovsky-core' ),
			self::CAPABILITY,
			self::MENU_SLUG,
			array( __CLASS__, 'render_page' ),
			3
		);
	}

	/**
	 * Settings page.
	 */
	public static function render_page() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ) );
		}

		$cfg        = MailOps::get_config();
		$state      = MailOps::state();
		$state_label = MailOps::state_label( $state );
		$pw_set     = MailOps::password_is_configured();
		$recipients = $cfg['recipients'];
		if ( empty( $recipients ) ) {
			$recipients[] = array(
				'email' => '',
				'label' => '',
			);
		}

		$errors = array();
		if ( isset( $_GET['fp02_mail_errors'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			$raw = wp_unslash( $_GET['fp02_mail_errors'] ); // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			if ( is_string( $raw ) ) {
				$decoded = json_decode( $raw, true );
				if ( is_array( $decoded ) ) {
					$errors = $decoded;
				}
			}
		}

		echo '<div class="wrap fp02-mail-forms">';
		echo '<h1>' . esc_html__( 'Почта и формы', 'shpigovsky-core' ) . '</h1>';
		echo '<p>' . esc_html__( 'Единственное место для настройки исходящей почты и доставки заявок. Пароль ящика здесь не показывается и не попадает в журнал.', 'shpigovsky-core' ) . '</p>';

		printf(
			'<div class="notice notice-info" style="padding:12px;"><p><strong>%s</strong> %s</p><p>%s</p></div>',
			esc_html__( 'Статус SMTP:', 'shpigovsky-core' ),
			esc_html( $state_label ),
			esc_html__( 'Сохранение полей не включает боевую отправку и не считается проверкой SMTP.', 'shpigovsky-core' )
		);

		if ( 0 === (int) $cfg['lead_retention_days'] ) {
			echo '<div class="notice notice-warning"><p><strong>' . esc_html__( 'FORM LEAD RETENTION PERIOD — OPERATOR DECISION REQUIRED', 'shpigovsky-core' ) . '</strong> ';
			echo esc_html__( 'Заявки сохраняются. Срок хранения ещё не задан — автоудаление не выполняется. P18H рекомендует 730 дней для заявок с форм (см. DECISION-MATRIX); включение не удаляет исторические заявки автоматически в этой волне.', 'shpigovsky-core' ) . '</p></div>';
		}

		if ( ! empty( $errors ) ) {
			echo '<div class="notice notice-error"><p>' . esc_html__( 'Исправьте поля и сохраните снова.', 'shpigovsky-core' ) . '</p></div>';
		}

		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" autocomplete="off">';
		echo '<input type="hidden" name="action" value="' . esc_attr( self::SAVE_ACTION ) . '" />';
		wp_nonce_field( self::SAVE_NONCE );

		echo '<h2>' . esc_html__( 'Отправка почты', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_html(
			__( 'Статус SMTP', 'shpigovsky-core' ),
			'<code>' . esc_html( $state_label ) . '</code>'
		);
		self::row_checkbox( 'smtp_enabled', __( 'Готовим SMTP', 'shpigovsky-core' ), (bool) $cfg['smtp_enabled'], __( 'Отметьте, когда заполняете боевые поля. Само по себе не включает отправку.', 'shpigovsky-core' ) );
		self::row_text( 'smtp_host', __( 'SMTP-сервер', 'shpigovsky-core' ), (string) $cfg['smtp_host'], 'smtp.example.com', isset( $errors['smtp_host'] ) ? $errors['smtp_host'] : '' );
		self::row_number( 'smtp_port', __( 'Порт', 'shpigovsky-core' ), (int) $cfg['smtp_port'], isset( $errors['smtp_port'] ) ? $errors['smtp_port'] : '' );
		echo '<tr><th><label for="smtp_encryption">' . esc_html__( 'Шифрование', 'shpigovsky-core' ) . '</label></th><td>';
		echo '<select name="smtp_encryption" id="smtp_encryption">';
		foreach ( array(
			MailOps::ENCRYPTION_NONE => __( 'Нет', 'shpigovsky-core' ),
			MailOps::ENCRYPTION_TLS  => 'TLS',
			MailOps::ENCRYPTION_SSL  => 'SSL',
		) as $val => $label ) {
			printf(
				'<option value="%1$s"%2$s>%3$s</option>',
				esc_attr( $val ),
				selected( $cfg['smtp_encryption'], $val, false ),
				esc_html( $label )
			);
		}
		echo '</select></td></tr>';
		self::row_checkbox( 'smtp_auth', __( 'Аутентификация', 'shpigovsky-core' ), (bool) $cfg['smtp_auth'], '' );
		self::row_text( 'smtp_username', __( 'Имя пользователя SMTP', 'shpigovsky-core' ), (string) $cfg['smtp_username'], MailOps::DEFAULT_FROM_EMAIL, isset( $errors['smtp_username'] ) ? $errors['smtp_username'] : '' );

		$pw_status = $pw_set
			? '<strong>' . esc_html__( 'CONFIGURED', 'shpigovsky-core' ) . '</strong>'
			: '<strong>' . esc_html__( 'NOT CONFIGURED', 'shpigovsky-core' ) . '</strong>';
		echo '<tr><th>' . esc_html__( 'Пароль SMTP', 'shpigovsky-core' ) . '</th><td>';
		echo '<p>' . wp_kses_post( $pw_status ) . '</p>';
		echo '<p><label>' . esc_html__( 'Новый пароль', 'shpigovsky-core' ) . '<br />';
		echo '<input type="password" name="smtp_password" value="" autocomplete="new-password" class="regular-text" /></label></p>';
		echo '<p class="description">' . esc_html__( 'Оставьте пустым, чтобы сохранить уже введённый пароль. Существующий пароль никогда не показывается.', 'shpigovsky-core' ) . '</p>';
		if ( $pw_set ) {
			echo '<p><label><input type="checkbox" name="smtp_password_clear" value="1" /> ' . esc_html__( 'Сбросить сохранённый пароль', 'shpigovsky-core' ) . '</label></p>';
		}
		if ( isset( $errors['smtp_password'] ) ) {
			echo '<p class="notice notice-error">' . esc_html( $errors['smtp_password'] ) . '</p>';
		}
		echo '</td></tr>';

		self::row_text( 'smtp_from_email', __( 'Отправитель', 'shpigovsky-core' ), (string) $cfg['smtp_from_email'], MailOps::DEFAULT_FROM_EMAIL, isset( $errors['smtp_from_email'] ) ? $errors['smtp_from_email'] : '' );
		self::row_text( 'smtp_from_name', __( 'Имя отправителя', 'shpigovsky-core' ), (string) $cfg['smtp_from_name'] !== '' ? (string) $cfg['smtp_from_name'] : MailOps::from_name(), '', '' );
		echo '</table>';

		echo '<h2>' . esc_html__( 'Получатели', 'shpigovsky-core' ) . '</h2>';
		echo '<p class="description">' . esc_html__( 'Первый адрес — основной. Дополнительные строки — копии той же заявки. Reply-To ставится на email посетителя только если он указал корректный адрес. Сейчас в форме консультации email необязателен.', 'shpigovsky-core' ) . '</p>';
		if ( isset( $errors['recipients'] ) ) {
			echo '<p class="notice notice-error">' . esc_html( $errors['recipients'] ) . '</p>';
		}
		echo '<div class="fp02-recipients" data-fp02-recipients data-fp02-max="' . esc_attr( (string) MailOps::MAX_RECIPIENTS ) . '">';
		echo '<table class="widefat striped fp02-recipients__table"><thead><tr>';
		echo '<th scope="col">' . esc_html__( 'Email', 'shpigovsky-core' ) . '</th>';
		echo '<th scope="col">' . esc_html__( 'Подпись', 'shpigovsky-core' ) . '</th>';
		echo '<th scope="col"><span class="screen-reader-text">' . esc_html__( 'Действия', 'shpigovsky-core' ) . '</span></th>';
		echo '</tr></thead><tbody data-fp02-recipients-list>';
		foreach ( $recipients as $i => $row ) {
			self::render_recipient_row( (int) $i, (string) $row['email'], (string) $row['label'] );
		}
		echo '</tbody></table>';
		echo '<p><button type="button" class="button" data-fp02-recipient-add>+ ' . esc_html__( 'Добавить получателя', 'shpigovsky-core' ) . '</button></p>';
		echo '<template id="fp02-recipient-row-template">';
		self::render_recipient_row( '__i__', '', '' );
		echo '</template>';
		echo '<p class="description">' . esc_html__( 'Не больше 20 получателей. Пустые строки при сохранении отбрасываются.', 'shpigovsky-core' ) . '</p>';
		echo '</div>';

		echo '<h2>' . esc_html__( 'Формы', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_html(
			__( 'Форма', 'shpigovsky-core' ),
			esc_html__( 'Консультация', 'shpigovsky-core' ) . ' <code>consultation</code>'
		);
		self::row_html(
			__( 'Получатели формы', 'shpigovsky-core' ),
			esc_html__( 'Глобальные (отдельный маршрутизатор не нужен — одна форма).', 'shpigovsky-core' )
		);
		self::row_html(
			__( 'Журнал заявок', 'shpigovsky-core' ),
			esc_html__( 'Включён системой. Заявка сохраняется до попытки отправить письмо.', 'shpigovsky-core' )
		);

		$as = class_exists( '\\Shpigovsky\\Core\\Forms\\AntiSpam' )
			? \Shpigovsky\Core\Forms\AntiSpam::admin_status()
			: array( 'active' => false, 'layers' => array(), 'rejected_24h' => 0, 'rejected_7d' => 0 );
		$as_html  = '<strong>' . esc_html__( 'Антиспам: Активен', 'shpigovsky-core' ) . '</strong>';
		$as_html .= '<ul style="margin:8px 0 0 1.2em;list-style:disc;">';
		foreach ( (array) $as['layers'] as $layer ) {
			$as_html .= '<li>' . esc_html( (string) $layer ) . '</li>';
		}
		$as_html .= '</ul>';
		$as_html .= '<p class="description">' . esc_html(
			sprintf(
				/* translators: 1: 24h count, 2: 7d count */
				__( 'Отклонено (без персональных данных): за 24 ч — %1$d, за 7 дн. — %2$d. Внешние CAPTCHA не используются.', 'shpigovsky-core' ),
				(int) $as['rejected_24h'],
				(int) $as['rejected_7d']
			)
		) . '</p>';
		self::row_html( __( 'Антиспам', 'shpigovsky-core' ), $as_html );

		self::row_text(
			'form_metrika_goal',
			__( 'Цель Яндекс.Метрики', 'shpigovsky-core' ),
			(string) $cfg['form_metrika_goal'],
			'consultation_submit',
			''
		);
		echo '<tr><th>' . esc_html__( 'Счётчик Метрики', 'shpigovsky-core' ) . '</th><td>';
		$counter = MailOps::metrika_counter_id();
		echo '' !== $counter
			? '<code>' . esc_html( $counter ) . '</code> — ' . esc_html__( 'из Настройки сайта → SEO и интеграции', 'shpigovsky-core' )
			: esc_html__( 'Не задан в SEO и интеграциях. Цель не стреляет, пока нет счётчика — это безопасно.', 'shpigovsky-core' );
		echo '</td></tr>';
		echo '<tr><th><label for="lead_retention_days">' . esc_html__( 'Срок хранения заявок (дней)', 'shpigovsky-core' ) . '</label></th><td>';
		printf(
			'<input type="number" min="0" max="3650" name="lead_retention_days" id="lead_retention_days" value="%d" />',
			(int) $cfg['lead_retention_days']
		);
		echo '<p class="description">' . esc_html__( '0 — срок не задан (решение оператора). Автоудаление не выполняется, пока не будет явного срока.', 'shpigovsky-core' ) . '</p>';
		echo '</td></tr>';
		echo '</table>';

		echo '<h2>' . esc_html__( 'Проверка', 'shpigovsky-core' ) . '</h2>';
		echo '<p>' . esc_html__( 'Готовность конфигурации:', 'shpigovsky-core' ) . ' <strong>' . esc_html( MailOps::is_complete() ? __( 'поля заполнены', 'shpigovsky-core' ) : __( 'неполная', 'shpigovsky-core' ) ) . '</strong></p>';
		if ( '' !== (string) $cfg['verified_at'] ) {
			echo '<p>' . esc_html__( 'Последняя успешная проверка:', 'shpigovsky-core' ) . ' ' . esc_html( (string) $cfg['verified_at'] ) . '</p>';
		}
		if ( 'fail' === (string) $cfg['last_test_status'] ) {
			echo '<p>' . esc_html__( 'Последняя ошибка (категория):', 'shpigovsky-core' ) . ' <code>' . esc_html( (string) $cfg['last_test_error_category'] ) . '</code></p>';
		}

		submit_button( __( 'Сохранить настройки', 'shpigovsky-core' ) );
		echo '</form>';

		$emails = MailOps::recipient_emails();
		if ( MailOps::is_complete() && ! empty( $emails ) ) {
			echo '<hr /><h2>' . esc_html__( 'Проверить SMTP', 'shpigovsky-core' ) . '</h2>';
			echo '<p>' . esc_html__( 'Отдельное тестовое письмо. Не включает боевую отправку заявок. Сначала сохраните настройки.', 'shpigovsky-core' ) . '</p>';
			echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '">';
			echo '<input type="hidden" name="action" value="' . esc_attr( self::TEST_ACTION ) . '" />';
			wp_nonce_field( self::TEST_NONCE );
			echo '<p><label>' . esc_html__( 'Получатель теста', 'shpigovsky-core' ) . '<br /><select name="test_recipient">';
			foreach ( $emails as $email ) {
				printf( '<option value="%1$s">%1$s</option>', esc_attr( $email ) );
			}
			echo '</select></label></p>';
			submit_button( __( 'Отправить тестовое письмо', 'shpigovsky-core' ), 'secondary' );
			echo '</form>';
		} else {
			echo '<p class="description">' . esc_html__( 'Кнопка проверки появится, когда заполнены сервер, порт, отправитель, получатель и пароль.', 'shpigovsky-core' ) . '</p>';
		}

		if ( MailOps::STATE_VERIFIED_READY === $state ) {
			echo '<hr /><h2>' . esc_html__( 'Боевая отправка', 'shpigovsky-core' ) . '</h2>';
			echo '<p>' . esc_html__( 'SMTP проверен. Чтобы заявки начали уходить письмом, включите отправку явно. Подавление до этого момента остаётся включённым.', 'shpigovsky-core' ) . '</p>';
			echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" onsubmit="return window.confirm(this.getAttribute(\'data-fp02-confirm\'));" data-fp02-confirm="' . esc_attr__( 'Включить реальную отправку писем с сайта?', 'shpigovsky-core' ) . '">';
			echo '<input type="hidden" name="action" value="' . esc_attr( self::ACTIVATE_ACTION ) . '" />';
			echo '<input type="hidden" name="fp02_delivery" value="on" />';
			wp_nonce_field( self::ACTIVATE_NONCE );
			submit_button( __( 'Включить отправку писем', 'shpigovsky-core' ) );
			echo '</form>';
		}

		if ( MailOps::STATE_VERIFIED_ACTIVE === $state ) {
			echo '<hr /><p>' . esc_html__( 'Боевая отправка включена.', 'shpigovsky-core' ) . '</p>';
			echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '">';
			echo '<input type="hidden" name="action" value="' . esc_attr( self::ACTIVATE_ACTION ) . '" />';
			echo '<input type="hidden" name="fp02_delivery" value="off" />';
			wp_nonce_field( self::ACTIVATE_NONCE );
			submit_button( __( 'Выключить отправку писем', 'shpigovsky-core' ), 'secondary' );
			echo '</form>';
		}

		echo '</div>';
	}

	/**
	 * Save settings.
	 */
	public static function handle_save() {
		self::require_post_cap();
		check_admin_referer( self::SAVE_NONCE );

		$result = MailOps::save_from_post( wp_unslash( $_POST ) );
		$url    = admin_url( 'admin.php?page=' . self::MENU_SLUG );
		if ( ! $result['ok'] ) {
			$url = add_query_arg(
				array(
					self::NOTICE_QUERY   => 'invalid',
					'fp02_mail_errors'   => wp_json_encode( $result['errors'] ),
				),
				$url
			);
		} else {
			$url = add_query_arg( self::NOTICE_QUERY, 'saved', $url );
		}
		wp_safe_redirect( $url );
		exit;
	}

	/**
	 * SMTP test: one-shot allow, no delivery_active change.
	 */
	public static function handle_test() {
		self::require_post_cap();
		check_admin_referer( self::TEST_NONCE );

		$wanted = isset( $_POST['test_recipient'] ) ? sanitize_email( wp_unslash( $_POST['test_recipient'] ) ) : '';
		$ok_list = MailOps::recipient_emails();
		$url     = admin_url( 'admin.php?page=' . self::MENU_SLUG );

		if ( ! is_email( $wanted ) || ! in_array( $wanted, $ok_list, true ) ) {
			wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'test_bad_recipient', $url ) );
			exit;
		}
		if ( ! MailOps::is_complete() ) {
			wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'test_incomplete', $url ) );
			exit;
		}

		if ( ! defined( 'FP02_MAIL_ALLOW_ONCE' ) ) {
			define( 'FP02_MAIL_ALLOW_ONCE', true );
		}

		$subject = sprintf(
			'FP-0002 SMTP test %s',
			gmdate( 'Y-m-d H:i:s' ) . ' UTC'
		);
		$body    = "FP-0002 SMTP test.\nThis is not a client lead.\nTimestamp: " . gmdate( 'c' ) . "\n";
		$headers = array(
			'Content-Type: text/plain; charset=UTF-8',
			'From: ' . MailOps::from_name() . ' <' . MailOps::from_email() . '>',
		);

		$sent = wp_mail( $wanted, $subject, $body, $headers );
		if ( $sent ) {
			MailOps::record_test_result( true, '' );
			if ( class_exists( ActivityLog::class ) ) {
				ActivityLog::log_system_event( 'smtp_test_ok', 'setting', 'Проверка SMTP: успех', 0 );
			}
			wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'test_ok', $url ) );
			exit;
		}

		global $phpmailer;
		$raw = ( is_object( $phpmailer ) && ! empty( $phpmailer->ErrorInfo ) ) ? (string) $phpmailer->ErrorInfo : 'send_failed';
		$cat = MailOps::sanitize_error_category( $raw );
		MailOps::record_test_result( false, $cat );
		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event( 'smtp_test_fail', 'setting', 'Проверка SMTP: ошибка (' . $cat . ')', 0 );
		}
		wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'test_fail', $url ) );
		exit;
	}

	/**
	 * Activate or deactivate outbound delivery.
	 */
	public static function handle_activate() {
		self::require_post_cap();
		check_admin_referer( self::ACTIVATE_NONCE );
		$mode = isset( $_POST['fp02_delivery'] ) ? sanitize_key( wp_unslash( $_POST['fp02_delivery'] ) ) : '';
		$url  = admin_url( 'admin.php?page=' . self::MENU_SLUG );
		if ( 'off' === $mode ) {
			MailOps::deactivate_delivery();
			wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'deactivated', $url ) );
			exit;
		}
		if ( MailOps::activate_delivery() ) {
			wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'activated', $url ) );
			exit;
		}
		wp_safe_redirect( add_query_arg( self::NOTICE_QUERY, 'activate_blocked', $url ) );
		exit;
	}

	/**
	 * Notices on the settings screen.
	 */
	public static function render_notice() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			return;
		}
		$page = isset( $_GET['page'] ) ? sanitize_key( wp_unslash( $_GET['page'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		if ( self::MENU_SLUG !== $page || ! isset( $_GET[ self::NOTICE_QUERY ] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			return;
		}
		$code = sanitize_key( wp_unslash( $_GET[ self::NOTICE_QUERY ] ) ); // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$map  = array(
			'saved'               => array( 'success', __( 'Настройки почты и форм сохранены. SMTP не считается проверенным.', 'shpigovsky-core' ) ),
			'invalid'             => array( 'error', __( 'Настройки не сохранены: проверьте поля.', 'shpigovsky-core' ) ),
			'test_ok'             => array( 'success', __( 'Тестовое письмо принято SMTP-сервером. Боевая отправка ещё не включена.', 'shpigovsky-core' ) ),
			'test_fail'           => array( 'error', __( 'Тестовое письмо не отправлено. Пароль не показывается. См. категорию ошибки на странице.', 'shpigovsky-core' ) ),
			'test_bad_recipient'  => array( 'error', __( 'Получатель теста должен быть из списка сохранённых адресов.', 'shpigovsky-core' ) ),
			'test_incomplete'     => array( 'error', __( 'Сначала заполните и сохраните SMTP.', 'shpigovsky-core' ) ),
			'activated'           => array( 'success', __( 'Исходящая отправка включена. Временное подавление больше не блокирует wp_mail.', 'shpigovsky-core' ) ),
			'deactivated'         => array( 'warning', __( 'Исходящая отправка выключена. Подавление снова активно.', 'shpigovsky-core' ) ),
			'activate_blocked'    => array( 'error', __( 'Нельзя включить отправку, пока SMTP не проверен.', 'shpigovsky-core' ) ),
		);
		if ( ! isset( $map[ $code ] ) ) {
			return;
		}
		printf(
			'<div class="notice notice-%1$s is-dismissible"><p>%2$s</p></div>',
			esc_attr( $map[ $code ][0] ),
			esc_html( $map[ $code ][1] )
		);
	}

	/**
	 * Gate POST handlers.
	 */
	private static function require_post_cap() {
		if ( ! is_user_logged_in() || ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ), 403 );
		}
		if ( 'POST' !== strtoupper( (string) ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) ) {
			wp_die( esc_html__( 'Только POST.', 'shpigovsky-core' ), 405 );
		}
	}

	/**
	 * Admin CSS/JS for the recipient repeater. Loaded only on this screen.
	 *
	 * @param string $hook Current admin hook.
	 */
	public static function enqueue_assets( $hook ) {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			return;
		}
		$page = isset( $_GET['page'] ) ? sanitize_key( wp_unslash( $_GET['page'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		if ( self::MENU_SLUG !== $page ) {
			return;
		}
		wp_enqueue_style(
			'fp02-mail-forms-admin',
			SHPIGOVSKY_CORE_URI . 'assets/css/mail-forms-admin.css',
			array(),
			SHPIGOVSKY_CORE_VERSION
		);
		wp_enqueue_script(
			'fp02-mail-forms-admin',
			SHPIGOVSKY_CORE_URI . 'assets/js/mail-forms-admin.js',
			array(),
			SHPIGOVSKY_CORE_VERSION,
			true
		);
	}

	/**
	 * One recipient row. $index may be the JS template token `__i__`.
	 *
	 * @param int|string $index Row index or placeholder.
	 * @param string     $email Email.
	 * @param string     $label Label.
	 */
	private static function render_recipient_row( $index, $email, $label ) {
		$index_attr = is_int( $index ) ? (string) $index : (string) $index;
		$email_id   = 'fp02-recipient-email-' . $index_attr;
		$label_id   = 'fp02-recipient-label-' . $index_attr;
		printf(
			'<tr class="fp02-recipients__row" data-fp02-recipient-row><td><label class="screen-reader-text" for="%1$s">%2$s</label><input type="email" class="regular-text" id="%1$s" name="recipients[%3$s][email]" value="%4$s" autocomplete="off" /></td><td><label class="screen-reader-text" for="%5$s">%6$s</label><input type="text" class="regular-text" id="%5$s" name="recipients[%3$s][label]" value="%7$s" autocomplete="off" /></td><td><button type="button" class="button-link-delete" data-fp02-recipient-remove>%8$s</button></td></tr>',
			esc_attr( $email_id ),
			esc_html__( 'Email', 'shpigovsky-core' ),
			esc_attr( $index_attr ),
			esc_attr( $email ),
			esc_attr( $label_id ),
			esc_html__( 'Подпись', 'shpigovsky-core' ),
			esc_attr( $label ),
			esc_html__( 'Удалить', 'shpigovsky-core' )
		);
	}

	/**
	 * @param string $label Label.
	 * @param string $html Html.
	 */
	private static function row_html( $label, $html ) {
		echo '<tr><th>' . esc_html( $label ) . '</th><td>' . $html . '</td></tr>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
	}

	/**
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param bool   $checked Checked.
	 * @param string $help Help.
	 */
	private static function row_checkbox( $name, $label, $checked, $help ) {
		echo '<tr><th>' . esc_html( $label ) . '</th><td>';
		printf(
			'<label><input type="checkbox" name="%1$s" value="1"%2$s /> %3$s</label>',
			esc_attr( $name ),
			checked( $checked, true, false ),
			esc_html( $label )
		);
		if ( '' !== $help ) {
			echo '<p class="description">' . esc_html( $help ) . '</p>';
		}
		echo '</td></tr>';
	}

	/**
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param string $value Value.
	 * @param string $placeholder Placeholder.
	 * @param string $error Error.
	 */
	private static function row_text( $name, $label, $value, $placeholder, $error ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		printf(
			'<input type="text" class="regular-text" id="%1$s" name="%1$s" value="%2$s" placeholder="%3$s" autocomplete="off" />',
			esc_attr( $name ),
			esc_attr( $value ),
			esc_attr( $placeholder )
		);
		if ( '' !== $error ) {
			echo '<p style="color:#b32d2e;">' . esc_html( $error ) . '</p>';
		}
		echo '</td></tr>';
	}

	/**
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param int    $value Value.
	 * @param string $error Error.
	 */
	private static function row_number( $name, $label, $value, $error ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		printf(
			'<input type="number" id="%1$s" name="%1$s" value="%2$s" min="0" max="65535" />',
			esc_attr( $name ),
			$value > 0 ? (int) $value : ''
		);
		if ( '' !== $error ) {
			echo '<p style="color:#b32d2e;">' . esc_html( $error ) . '</p>';
		}
		echo '</td></tr>';
	}
}
