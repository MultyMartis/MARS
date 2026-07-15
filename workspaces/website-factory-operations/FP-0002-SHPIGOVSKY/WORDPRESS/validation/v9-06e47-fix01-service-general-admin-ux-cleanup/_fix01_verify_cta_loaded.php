<?php
require_once "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
if (function_exists("acf_set_form_data")) acf_set_form_data("post_id", 74);
$_GET["post"] = "74";
$fields = acf_get_fields("group_fp02_service_general_parity");
echo "loaded_fields=" . count($fields) . "\n";
$names = array();
foreach ($fields as $f) { if (!empty($f["name"])) $names[] = $f["name"]; }
echo "cta_title=" . (in_array("cta_title", $names, true) ? "yes" : "no") . "\n";
echo "cta_text=" . (in_array("cta_text", $names, true) ? "yes" : "no") . "\n";
$g = acf_get_field_groups(array("post_id"=>74));
foreach ($g as $x) echo $x["menu_order"]."|".$x["title"]."|".$x["key"]."\n";
