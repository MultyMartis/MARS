<?php
/**
 * Phase-aware module activation registry.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core;

use Shpigovsky\Core\Admin\AcfeCheckboxCompat;
use Shpigovsky\Core\Admin\EditorRestrictions;
use Shpigovsky\Core\Admin\OptionsPage;
use Shpigovsky\Core\Admin\ServiceDuplicate;
use Shpigovsky\Core\Admin\ServiceLayoutGovernance;
use Shpigovsky\Core\Admin\PermalinkSlugUX;
use Shpigovsky\Core\Admin\ActivityLog;
use Shpigovsky\Core\Admin\AdminMenuHygiene;
use Shpigovsky\Core\Admin\SystemDashboard;
use Shpigovsky\Core\Admin\IndexingControl;
use Shpigovsky\Core\Admin\IndexingState;
use Shpigovsky\Core\Admin\IndexingWatchdog;
use Shpigovsky\Core\Admin\DocxImporter;
use Shpigovsky\Core\Admin\MailFormsSettings;
use Shpigovsky\Core\Admin\LeadsAdmin;
use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\ContentTypes\Specialist;
use Shpigovsky\Core\Fields\AcfIntegration;
use Shpigovsky\Core\Fields\FieldGroups;
use Shpigovsky\Core\Fields\RepeaterValidation;
use Shpigovsky\Core\Forms\ConsultationHandler;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\Mail\SmtpTransport;
use Shpigovsky\Core\Migrations\MigrationRunner;
use Shpigovsky\Core\Permalinks\ServicePermalinks;
use Shpigovsky\Core\Privacy\LeadPersonalData;
use Shpigovsky\Core\Privacy\PrivacyConsent;
use Shpigovsky\Core\Settings\SiteSettings;
use Shpigovsky\Core\Typography\TypographyFilters;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Deterministic activation decisions for source and delivery phases.
 */
final class ModuleRegistry {

	public const ENABLED_IN_CONTENT_MODEL          = 'ENABLED_IN_CONTENT_MODEL';
	public const DISABLED_UNTIL_V9_06D2_OR_LATER  = 'DISABLED_UNTIL_V9_06D2_OR_LATER';
	public const DISABLED_UNTIL_LATER_PHASE       = 'DISABLED_UNTIL_LATER_PHASE';
	public const REJECTED                         = 'REJECTED';

	/**
	 * Module registry keyed by ModuleInterface::id().
	 *
	 * @var array<string, array{module:string,class?:class-string,status:string,runtime_delivered:bool}>
	 */
	private const MODULES = array(
		'content-types.service'      => array(
			'module'            => 'ContentTypes',
			'class'             => Service::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'content-types.specialist'   => array(
			'module'            => 'ContentTypes',
			'class'             => Specialist::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'permalinks.service'         => array(
			'module'            => 'Permalinks',
			'class'             => ServicePermalinks::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'fields.acf'                => array(
			'module'            => 'Fields',
			'class'             => AcfIntegration::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'fields.field-groups'       => array(
			'module'            => 'Fields',
			'class'             => FieldGroups::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'fields.repeater-validation' => array(
			'module'            => 'Validation',
			'class'             => RepeaterValidation::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'settings.site'             => array(
			'module'            => 'Settings',
			'class'             => SiteSettings::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.options-page'        => array(
			'module'            => 'Admin',
			'class'             => OptionsPage::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.editor-restrictions' => array(
			'module'            => 'Admin',
			'class'             => EditorRestrictions::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.acfe-checkbox-compat' => array(
			'module'            => 'Admin',
			'class'             => AcfeCheckboxCompat::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'admin.service-layout-governance' => array(
			'module'            => 'Admin',
			'class'             => ServiceLayoutGovernance::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.service-duplicate'   => array(
			'module'            => 'Admin',
			'class'             => ServiceDuplicate::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.permalink-slug-ux'   => array(
			'module'            => 'Admin',
			'class'             => PermalinkSlugUX::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.activity-log'        => array(
			'module'            => 'Admin',
			'class'             => ActivityLog::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.menu-hygiene'        => array(
			'module'            => 'Admin',
			'class'             => AdminMenuHygiene::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.system-dashboard'    => array(
			'module'            => 'Admin',
			'class'             => SystemDashboard::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.indexing-control'    => array(
			'module'            => 'Admin',
			'class'             => IndexingControl::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'admin.indexing-watchdog' => array(
			'module'            => 'Admin',
			'class'             => IndexingWatchdog::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'admin.docx-importer'       => array(
			'module'            => 'Admin',
			'class'             => DocxImporter::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => false,
		),
		'mail.ops'                  => array(
			'module'            => 'Mail',
			'class'             => MailOps::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'mail.smtp-transport'       => array(
			'module'            => 'Mail',
			'class'             => SmtpTransport::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'admin.mail-forms'          => array(
			'module'            => 'Admin',
			'class'             => MailFormsSettings::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'leads.registry'            => array(
			'module'            => 'Leads',
			'class'             => LeadRegistry::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'admin.leads'               => array(
			'module'            => 'Admin',
			'class'             => LeadsAdmin::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'privacy.lead-personal-data' => array(
			'module'            => 'Privacy',
			'class'             => LeadPersonalData::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'privacy.consent'           => array(
			'module'            => 'Privacy',
			'class'             => PrivacyConsent::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'migrations.runner'         => array(
			'module'            => 'Migrations',
			'class'             => MigrationRunner::class,
			'status'            => self::DISABLED_UNTIL_V9_06D2_OR_LATER,
			'runtime_delivered' => false,
		),
		'forms.consultation'        => array(
			'module'            => 'Forms',
			'class'             => ConsultationHandler::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'typography.russian'        => array(
			'module'            => 'Typography',
			'class'             => TypographyFilters::class,
			'status'            => self::ENABLED_IN_CONTENT_MODEL,
			'runtime_delivered' => true,
		),
		'taxonomies'                => array(
			'module'            => 'Taxonomies',
			'status'            => self::REJECTED,
			'runtime_delivered' => false,
		),
	);

	/**
	 * Return module classes in registration order.
	 *
	 * @return array<int, class-string>
	 */
	public static function get_module_classes() {
		$classes = array();

		foreach ( self::MODULES as $entry ) {
			if ( isset( $entry['class'] ) ) {
				$classes[] = $entry['class'];
			}
		}

		return $classes;
	}

	/**
	 * Return the public registry for validation evidence.
	 *
	 * @return array<string, array{module:string,class?:class-string,status:string,runtime_delivered:bool}>
	 */
	public static function get_registry() {
		return self::MODULES;
	}

	/**
	 * Return source status for a module id.
	 *
	 * @param string $module_id Module identifier.
	 * @return string
	 */
	public static function get_status( $module_id ) {
		return isset( self::MODULES[ $module_id ] ) ? self::MODULES[ $module_id ]['status'] : 'UNKNOWN';
	}

	/**
	 * Whether a module can register hooks in the current source mode.
	 *
	 * @param string $module_id Module identifier.
	 * @return bool
	 */
	public static function is_enabled( $module_id ) {
		if ( shpigovsky_core_is_skeleton_mode() ) {
			return false;
		}

		return self::ENABLED_IN_CONTENT_MODEL === self::get_status( $module_id )
			&& in_array( shpigovsky_core_mode(), array( 'content_model', 'runtime_delivered' ), true );
	}
}
