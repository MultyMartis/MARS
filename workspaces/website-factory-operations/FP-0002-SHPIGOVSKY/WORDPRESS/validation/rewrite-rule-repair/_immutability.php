<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
if (!function_exists("get_plugins")) {
  require_once ABSPATH . "wp-admin/includes/plugin.php";
}
global $wpdb;
$theme = wp_get_theme();
$active = (array) get_option("active_plugins", []);
sort($active);
$menus = wp_get_nav_menus();
$menu_snapshot = [];
foreach ($menus as $menu) {
  $items = wp_get_nav_menu_items($menu->term_id);
  $menu_snapshot[] = [
    "term_id" => (int) $menu->term_id,
    "name" => $menu->name,
    "slug" => $menu->slug,
    "count" => is_array($items) ? count($items) : 0,
  ];
}
$wpilot_write = null;
if (class_exists("WPilot_Settings")) {
  $opts = WPilot_Settings::get_options();
  $wpilot_write = !empty($opts["write_enabled"]);
}
$acf_groups = [];
if (function_exists("acf_get_local_field_groups")) {
  foreach ((array) acf_get_local_field_groups() as $group) {
    $acf_groups[] = $group["key"] ?? "";
  }
}
sort($acf_groups);

$ids = [4,5,20,73,74,77,84];
$objects = [];
foreach ($ids as $id) {
  $p = get_post($id);
  if (!$p) { $objects[(string)$id] = null; continue; }
  $meta = get_post_meta($id);
  $meta_hashes = [];
  foreach ($meta as $k => $vals) {
    if (strpos($k, "_") === 0) continue;
    $meta_hashes[$k] = hash("sha256", (string)($vals[0] ?? ""));
  }
  ksort($meta_hashes);
  $objects[(string)$id] = [
    "ID" => (int)$p->ID,
    "post_type" => $p->post_type,
    "title" => $p->post_title,
    "slug" => $p->post_name,
    "parent" => (int)$p->post_parent,
    "status" => $p->post_status,
    "content_hash" => hash("sha256", (string)$p->post_content),
    "excerpt_hash" => hash("sha256", (string)$p->post_excerpt),
    "meta_hashes" => $meta_hashes,
    "modified_gmt" => $p->post_modified_gmt,
  ];
}

$r = get_option("rewrite_rules");
$depth2 = null;
if (is_array($r)) {
  foreach ($r as $p => $q) {
    if ($p === "^uslugi/([^/]+)/([^/]+)/?$") { $depth2 = $q; break; }
  }
}

// WP main query for service 74 URL
$prev = $_SERVER;
$_SERVER["REQUEST_URI"] = "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/";
$_SERVER["HTTP_HOST"] = "shpigovsky.test";
$wp = new WP();
$wp->main();
$qo = get_queried_object();
$main_query = [
  "is_404" => is_404(),
  "is_singular" => is_singular(),
  "is_singular_service" => is_singular("service"),
  "queried_object_id" => $qo ? (int)$qo->ID : null,
  "queried_object_type" => $qo ? $qo->post_type : null,
  "query_vars_service" => get_query_var("service"),
  "query_vars_post_type" => get_query_var("post_type"),
];
$_SERVER = $prev;

$identity = [
  "phase" => "REWRITE-RULE-REPAIR",
  "timestamp" => gmdate("c"),
  "runtime" => "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky",
  "domain" => home_url("/"),
  "db_name" => DB_NAME,
  "db_prefix" => $wpdb->prefix,
  "active_theme" => $theme->get_stylesheet(),
  "shpigovsky_core_active" => is_plugin_active("shpigovsky-core/shpigovsky-core.php"),
  "shpigovsky_core_mode" => defined("SHPIGOVSKY_CORE_MODE") ? SHPIGOVSKY_CORE_MODE : null,
  "service_cpt_registered" => (bool) get_post_type_object("service"),
  "pages_total" => (int)$wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status!='trash'"),
  "services_total" => (int)$wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status!='trash'"),
  "posts_total" => (int)$wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status!='trash'"),
  "menus" => count($menus),
  "menu_snapshot" => $menu_snapshot,
  "acf_groups_count" => count($acf_groups),
  "wpilot_write_enabled" => $wpilot_write,
  "depth2_query" => $depth2,
  "rewrite_rules_hash" => hash("sha256", wp_json_encode($r)),
  "rewrite_rules_count" => is_array($r) ? count($r) : 0,
  "service_74_main_query" => $main_query,
  "seeded_objects" => $objects,
];

$pass = $identity["db_name"] === "mars_wp_fp0002"
  && $identity["db_prefix"] === "fp02_"
  && $identity["active_theme"] === "shpigovsky"
  && $identity["shpigovsky_core_active"]
  && $identity["shpigovsky_core_mode"] === "content_model"
  && $identity["services_total"] === 15
  && $identity["pages_total"] === 23
  && $identity["menus"] === 3
  && $identity["acf_groups_count"] === 13
  && $identity["wpilot_write_enabled"] === false
  && $main_query["queried_object_id"] === 74
  && $main_query["is_404"] === false
  && $depth2 === "index.php?post_type=service&service=\$matches[1]/\$matches[2]";
$identity["result"] = $pass ? "PASS" : "FAIL";

$evidence = "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/rewrite-rule-repair";
file_put_contents($evidence . "/post-repair-identity-and-immutability.json", json_encode($identity, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
echo json_encode([
  "result" => $identity["result"],
  "pages" => $identity["pages_total"],
  "services" => $identity["services_total"],
  "posts" => $identity["posts_total"],
  "menus" => $identity["menus"],
  "queried_74" => $main_query["queried_object_id"],
  "is_404" => $main_query["is_404"],
  "service_qv" => $main_query["query_vars_service"],
  "depth2_ok" => $depth2 === "index.php?post_type=service&service=\$matches[1]/\$matches[2]",
], JSON_UNESCAPED_SLASHES), "\n";
