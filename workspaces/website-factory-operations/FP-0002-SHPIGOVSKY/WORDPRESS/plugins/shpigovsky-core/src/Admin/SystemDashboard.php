<?php

/**

 * Dashboard widget: MetaCODE / system state — client-facing PROD-P18J.

 *

 * Compact operator summary for site owners. Internal engineering telemetry

 * belongs in reports, not this widget.

 *

 * @package Shpigovsky_Core

 */



namespace Shpigovsky\Core\Admin;



use Shpigovsky\Core\Contracts\ModuleInterface;

use Shpigovsky\Core\Leads\LeadRegistry;

use Shpigovsky\Core\Mail\MailOps;

use Shpigovsky\Core\ModuleRegistry;

use Shpigovsky\Core\Privacy\PrivacyConsent;



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



/**

 * Single non-secret system widget on the main dashboard.

 */

final class SystemDashboard implements ModuleInterface {



	/**

	 * Baseline ID (internal bookkeeping — not shown in client widget).

	 */

	const BASELINE_ID = 'FP-0002-PROD-BASELINE-2026-08-20-P23';



	/**

	 * Latest accepted production wave label (internal bookkeeping).

	 */

	const LATEST_ACCEPTED_WAVE = 'P23 Dashboard attribution + form mail UX';



	/**

	 * {@inheritdoc}

	 */

	public static function id() {

		return 'admin.system-dashboard';

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

		add_action( 'wp_dashboard_setup', array( __CLASS__, 'register_widget' ) );

		add_action( 'admin_enqueue_scripts', array( __CLASS__, 'enqueue_assets' ) );

	}



	/**

	 * Scheme-aware widget styles on the main dashboard only.

	 *

	 * @param string $hook Current admin hook.

	 */

	public static function enqueue_assets( $hook ) {

		if ( 'index.php' !== $hook || ! current_user_can( 'manage_options' ) ) {

			return;

		}



		wp_enqueue_style(

			'fp02-system-dashboard-widget',

			SHPIGOVSKY_CORE_URI . 'assets/css/system-dashboard-widget.css',

			array(),

			SHPIGOVSKY_CORE_VERSION

		);

	}



	/**

	 * Register the dashboard widget.

	 */

	public static function register_widget() {

		if ( ! current_user_can( 'manage_options' ) ) {

			return;

		}



		wp_add_dashboard_widget(

			'fp02_metacode_system_state',

			__( 'MetaCODE / Состояние системы', 'shpigovsky-core' ),

			array( __CLASS__, 'render_widget' )

		);

	}



	/**

	 * Widget body — client-facing summary.

	 */

	public static function render_widget() {

		$summary = self::client_summary();



		echo '<div class="fp02-metacode-system">';



		if ( class_exists( IndexingControl::class ) ) {

			IndexingControl::render_banner();

		}



		echo '<div class="fp02-metacode-system__grid" role="list">';

		foreach ( $summary['chips'] as $chip ) {

			self::render_chip( $chip['label'], $chip['value'], ! empty( $chip['html'] ) );

		}

		echo '</div>';



		if ( ! empty( $summary['actions'] ) ) {

			echo '<div class="fp02-metacode-system__section">';

			echo '<h4 class="fp02-metacode-system__section-title">' . esc_html__( 'Важно', 'shpigovsky-core' ) . '</h4>';

			echo '<ul class="fp02-metacode-system__actions">';

			foreach ( $summary['actions'] as $action ) {

				echo '<li>' . esc_html( $action ) . '</li>';

			}

			echo '</ul>';

			echo '</div>';

		}



		echo '<footer class="fp02-metacode-system__footer">';

		printf(

			'<p style="margin:0;">%s <a href="%s" target="_blank" rel="noopener noreferrer">Overseo</a></p>',

			esc_html__( 'Разработка:', 'shpigovsky-core' ),

			esc_url( 'https://overseo.ru/' )

		);

		echo '</footer>';



		echo '<p class="fp02-metacode-system__note" style="margin-top:10px;">';

		echo esc_html__( 'Пароли, токены и другие секреты здесь не показываются.', 'shpigovsky-core' );

		echo '</p>';



		echo '</div>';

	}



	/**

	 * Client-facing status model.

	 *

	 * @return array<string, mixed>

	 */

	private static function client_summary() {

		$mail_label    = self::client_mail_label();

		$leads_label   = class_exists( LeadRegistry::class )

			? __( 'принимаются', 'shpigovsky-core' )

			: __( 'не активны', 'shpigovsky-core' );

		$privacy_label = class_exists( PrivacyConsent::class )

			? __( 'активно', 'shpigovsky-core' )

			: __( 'не установлено', 'shpigovsky-core' );



		$chips = array(

			array(

				'label' => __( 'Сайт', 'shpigovsky-core' ),

				'value' => __( 'Работает в боевом режиме', 'shpigovsky-core' ),

			),

			array(

				'label' => __( 'Боевой домен', 'shpigovsky-core' ),

				'value' => sprintf(

					'<a href="%1$s" target="_blank" rel="noopener noreferrer">%2$s</a>',

					esc_url( 'https://shpigovsky.ru/' ),

					esc_html( 'shpigovsky.ru' )

				),

				'html'  => true,

			),

			array(

				'label' => __( 'Заявки', 'shpigovsky-core' ),

				'value' => $leads_label,

			),

			array(

				'label' => __( 'Почта', 'shpigovsky-core' ),

				'value' => $mail_label,

			),

			array(

				'label' => __( 'Cookie / конфиденциальность', 'shpigovsky-core' ),

				'value' => $privacy_label,

			),

			array(

				'label' => __( 'Sitemap', 'shpigovsky-core' ),

				'value' => __( 'готов', 'shpigovsky-core' ),

			),

			array(

				'label' => __( 'Статус проекта', 'shpigovsky-core' ),

				'value' => __( 'поддержка / сопровождение', 'shpigovsky-core' ),

			),

		);



		$actions = array(

			__( 'Проверить отправку sitemap в Google Search Console и Яндекс Вебмастер', 'shpigovsky-core' ),

			__( 'При необходимости настроить срок хранения заявок', 'shpigovsky-core' ),

			__( 'При необходимости согласовать финальную юридическую формулировку Cookie Policy', 'shpigovsky-core' ),

		);



		return array(

			'chips'   => $chips,

			'actions' => $actions,

		);

	}



	/**

	 * Human-readable mail status for site owners.

	 *

	 * @return string

	 */

	private static function client_mail_label() {

		if ( ! class_exists( MailOps::class ) ) {

			return __( 'требует настройки', 'shpigovsky-core' );

		}



		$state = MailOps::state();

		if ( MailOps::STATE_VERIFIED_ACTIVE === $state || MailOps::STATE_VERIFIED_READY === $state ) {

			return __( 'настроена', 'shpigovsky-core' );

		}

		if ( MailOps::STATE_CONFIGURED_NOT_VERIFIED === $state ) {

			return __( 'требует проверки', 'shpigovsky-core' );

		}

		if ( MailOps::STATE_ERROR === $state ) {

			return __( 'ошибка — свяжитесь с поддержкой', 'shpigovsky-core' );

		}



		return __( 'требует настройки', 'shpigovsky-core' );

	}



	/**

	 * Compact status chip.

	 *

	 * @param string $label Label.

	 * @param string $value Value (plain or safe HTML when $is_html).

	 * @param bool   $is_html Whether value is pre-escaped HTML.

	 */

	private static function render_chip( $label, $value, $is_html = false ) {

		echo '<div class="fp02-metacode-system__chip" role="listitem">';

		echo '<span class="fp02-metacode-system__chip-label">' . esc_html( $label ) . '</span>';

		echo '<span class="fp02-metacode-system__chip-value">';

		if ( $is_html ) {

			echo $value; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- built with esc_url/esc_html.

		} else {

			echo esc_html( $value );

		}

		echo '</span>';

		echo '</div>';

	}

}

