<?php
/**
 * Export split comfort ACF JSON via reflection (no WP bootstrap).
 */

namespace {
	define( 'ABSPATH', true );
	function esc_html__( $t, $d = null ) { return $t; }
	function __( $t, $d = null ) { return $t; }
	function shpigovsky_core_is_skeleton_mode() { return false; }
	function shpigovsky_core_mode() { return 'content_model'; }
	function shpigovsky_core_acf_pro_is_active() { return true; }
}

namespace Shpigovsky\Core {
	// Minimal stubs for ModuleRegistry dependencies if autoload pulls them — load files directly.
}

namespace {
	$base = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugins/shpigovsky-core/src';
	require_once $base . '/Contracts/ModuleInterface.php';
	require_once $base . '/ModuleRegistry.php';
	require_once $base . '/Fields/ServiceGeneralParity.php';
	require_once $base . '/Fields/ServiceSectionParity.php';
	require_once $base . '/Fields/FieldGroups.php';

	$ref = new ReflectionClass( \Shpigovsky\Core\Fields\FieldGroups::class );
	$methods = array( 'block_comfort_intro', 'block_comfort_gallery', 'block_comfort_requirements' );
	$dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json';

	foreach ( $methods as $m ) {
		$method = $ref->getMethod( $m );
		$method->setAccessible( true );
		$group = $method->invoke( null );
		$key   = $group['key'];
		$fields = array();
		foreach ( $group['fields'] as $i => $field ) {
			$field['ID']         = 0;
			$field['prefix']     = 'acf';
			$field['value']      = null;
			$field['menu_order'] = $i;
			$field['id']         = '';
			$field['class']      = '';
			$field['parent']     = $key;
			$field['_name']      = $field['name'];
			$field['_valid']     = 1;
			if ( isset( $field['sub_fields'] ) && is_array( $field['sub_fields'] ) ) {
				foreach ( $field['sub_fields'] as $si => &$sub ) {
					$sub['ID']         = 0;
					$sub['prefix']     = 'acf';
					$sub['value']      = null;
					$sub['menu_order'] = $si;
					$sub['id']         = '';
					$sub['class']      = '';
					$sub['parent']     = $field['key'];
					$sub['_name']      = $sub['name'];
					$sub['_valid']     = 1;
				}
				unset( $sub );
			}
			$fields[] = $field;
		}
		$group['fields']          = $fields;
		$group['ID']              = 0;
		$group['display_title']   = '';
		$group['allow_ai_access'] = false;
		$group['ai_description']  = '';
		$group['local']           = 'php';
		$group['_valid']          = true;

		$path = $dir . '/' . $key . '.json';
		file_put_contents( $path, json_encode( $group, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES ) );
		echo "wrote $path\n";
	}

	$legacy = $dir . '/group_fp02_block_comfort.json';
	if ( is_file( $legacy ) ) {
		$bak = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e56-operator-refinements/group_fp02_block_comfort.pre-split.json.bak';
		copy( $legacy, $bak );
		unlink( $legacy );
		echo "archived+removed legacy $legacy -> $bak\n";
	}

	echo "done\n";
}
