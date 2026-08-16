<?php
define("WP_USE_THEMES", false);
$_SERVER["REQUEST_URI"] = "/wp-admin/post.php?post=74&action=edit";
$_SERVER["PHP_SELF"] = "/wp-admin/post.php";
$_GET["post"] = "74";
$_GET["action"] = "edit";
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
// Force admin context flags used by is_admin().
if (!defined("WP_ADMIN")) { define("WP_ADMIN", true); }
$GLOBALS["current_screen"] = null;
require_once ABSPATH . "wp-admin/includes/admin.php";
set_current_screen("service");
$post_id = 74;
acf_set_form_data("post_id", $post_id);
$nested = \Shpigovsky\Core\Admin\ServiceLayoutGovernance::is_nested_service($post_id);
$depth = \Shpigovsky\Core\Admin\ServiceLayoutGovernance::get_service_depth($post_id);
$role_field = acf_get_field("field_fp02_service_editor_role");
$prepared = \Shpigovsky\Core\Admin\ServiceLayoutGovernance::prepare_editor_role_field($role_field);
echo "is_admin=" . (is_admin()?"1":"0") . " nested=" . ($nested?"1":"0") . " depth=$depth prepared_type=" . $prepared["type"] . " prepared_name=[" . $prepared["name"] . "]" . PHP_EOL;

// Count how many parity fields would survive prepare_field as-is (conditionals remain)
$fields = acf_get_fields("group_fp02_service_general_parity");
$with = 0; foreach ($fields as $f) { if (!empty($f["conditional_logic"])) $with++; }
echo "parity_fields=" . count($fields) . " with_cond=$with" . PHP_EOL;
