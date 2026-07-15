<?php
require_once "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$group = acf_get_field_group("group_fp02_service_general_parity");
$fields = acf_get_fields("group_fp02_service_general_parity");
if (!$group) { fwrite(STDERR, "no group\n"); exit(1); }
$group["fields"] = $fields ? $fields : array();
$group["modified"] = time();
unset($group["ID"], $group["local"], $group["local_file"], $group["local_types"]);
$path_src = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_service_general_parity.json";
$path_rt  = "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_service_general_parity.json";
$json = wp_json_encode($group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
file_put_contents($path_src, $json . "\n");
file_put_contents($path_rt, $json . "\n");
echo "fields=" . count($group["fields"]) . "\n";
$names = array();
foreach ($group["fields"] as $f) { if (!empty($f["name"])) $names[] = $f["name"]; }
echo "has_cta_title=" . (in_array("cta_title", $names, true) ? "yes" : "no") . "\n";
echo "DONE\n";
