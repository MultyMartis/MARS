<?php
require_once "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$group = \Shpigovsky\Core\Fields\ServiceGeneralParity::group();
echo "php_fields=" . count($group["fields"]) . "\n";
$has = false;
foreach ($group["fields"] as $f) {
  if (!empty($f["name"]) && $f["name"] === "cta_title") { $has = true; }
}
echo "php_has_cta_title=" . ($has ? "yes" : "no") . "\n";
// Force export PHP group as JSON with high modified
$group["modified"] = 1784454900;
$path_src = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_service_general_parity.json";
$path_rt  = "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_service_general_parity.json";
$json = wp_json_encode($group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
file_put_contents($path_src, $json);
file_put_contents($path_rt, $json);
// Also check what acf resolves after clearing cache
if (function_exists("acf_get_store")) {
  $store = acf_get_store("local-groups");
  if ($store) { /* noop */ }
}
// Re-get after write — CLI process already loaded old; report php truth only
echo "exported\n";
