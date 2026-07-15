<?php
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
global $wpdb;
if (!function_exists("get_plugins")) {
    require_once ABSPATH . "wp-admin/includes/plugin.php";
}
function fp02_content_len($post) { return strlen((string) $post->post_content); }
function fp02_excerpt_len($post) { return strlen((string) $post->post_excerpt); }
function fp02_path_from_url($url) {
    $path = parse_url($url, PHP_URL_PATH);
    if ($path === null || $path === false || $path === "") { return "/"; }
    if (substr($path, -1) !== "/") { $path .= "/"; }
    return $path === "//" ? "/" : $path;
}
function fp02_acf_keys_for_post($post_id) {
    $keys = array();
    if (!function_exists("get_fields")) { return $keys; }
    $fields = get_fields($post_id);
    if (!is_array($fields)) { return $keys; }
    foreach ($fields as $k => $v) {
        if ($v === null || $v === "" || $v === false || $v === array()) { continue; }
        $keys[] = $k;
    }
    return $keys;
}
function fp02_meta_presence($post_id) {
    $meta = get_post_meta($post_id);
    $out = array();
    foreach ($meta as $k => $vals) {
        if (strpos($k, "_") === 0) { continue; }
        $out[] = $k;
    }
    sort($out);
    return $out;
}
$active = (array) get_option("active_plugins", array());
$theme = wp_get_theme();
$service_obj = get_post_type_object("service");
$acf_groups = array();
if (function_exists("acf_get_local_field_groups")) {
    foreach ((array) acf_get_local_field_groups() as $group) {
        $acf_groups[] = array("key" => $group["key"] ?? "", "title" => $group["title"] ?? "");
    }
}
$acf_options_pages = array();
if (function_exists("acf_get_options_pages")) {
    foreach ((array) acf_get_options_pages() as $slug => $page) {
        $acf_options_pages[] = array(
            "slug" => is_array($page) ? ($page["menu_slug"] ?? $slug) : $slug,
            "registered" => true,
            "values_dumped" => false
        );
    }
}
$wpilot_write = null;
if (class_exists("WPilot_Settings")) {
    $wpilot_write = !empty(WPilot_Settings::get_options()["write_enabled"]);
}
$pages = array();
foreach (get_posts(array("post_type" => "page", "post_status" => "any", "numberposts" => -1, "orderby" => "ID", "order" => "ASC")) as $p) {
    $url = get_permalink($p);
    $template = get_page_template_slug($p->ID);
    if ($template === "") { $template = "default"; }
    $pages[] = array(
        "ID" => (int) $p->ID,
        "title" => $p->post_title,
        "slug" => $p->post_name,
        "parent" => (int) $p->post_parent,
        "path" => fp02_path_from_url($url),
        "status" => $p->post_status,
        "template" => $template,
        "content_length" => fp02_content_len($p),
        "excerpt_length" => fp02_excerpt_len($p),
        "modified_gmt" => $p->post_modified_gmt,
        "url" => $url,
        "meta_keys_non_underscore" => fp02_meta_presence($p->ID),
        "acf_nonempty_field_names" => fp02_acf_keys_for_post($p->ID)
    );
}
$services = array();
foreach (get_posts(array("post_type" => "service", "post_status" => "any", "numberposts" => -1, "orderby" => "ID", "order" => "ASC")) as $p) {
    $url = get_permalink($p);
    $parent_slug = "none";
    if ($p->post_parent) {
        $parent = get_post($p->post_parent);
        $parent_slug = $parent ? $parent->post_name : (string) $p->post_parent;
    }
    $services[] = array(
        "ID" => (int) $p->ID,
        "title" => $p->post_title,
        "slug" => $p->post_name,
        "parent" => $parent_slug,
        "parent_id" => (int) $p->post_parent,
        "path" => fp02_path_from_url($url),
        "status" => $p->post_status,
        "generated_permalink" => $url,
        "content_length" => fp02_content_len($p),
        "excerpt_length" => fp02_excerpt_len($p),
        "modified_gmt" => $p->post_modified_gmt,
        "meta_keys_non_underscore" => fp02_meta_presence($p->ID),
        "acf_nonempty_field_names" => fp02_acf_keys_for_post($p->ID),
        "registry_id_meta" => get_post_meta($p->ID, "fp02_service_registry_id", true),
        "layout_variant_meta" => get_post_meta($p->ID, "service_layout_variant", true)
    );
}
$posts = array();
foreach (get_posts(array("post_type" => "post", "post_status" => "any", "numberposts" => -1, "orderby" => "ID", "order" => "ASC")) as $p) {
    $url = get_permalink($p);
    $posts[] = array(
        "ID" => (int) $p->ID,
        "title" => $p->post_title,
        "slug" => $p->post_name,
        "path" => fp02_path_from_url($url),
        "status" => $p->post_status,
        "content_length" => fp02_content_len($p),
        "excerpt_length" => fp02_excerpt_len($p),
        "modified_gmt" => $p->post_modified_gmt,
        "url" => $url,
        "meta_keys_non_underscore" => fp02_meta_presence($p->ID),
        "acf_nonempty_field_names" => fp02_acf_keys_for_post($p->ID)
    );
}
$menus = array();
foreach (wp_get_nav_menus() as $menu) {
    $items = wp_get_nav_menu_items($menu->term_id);
    $menus[] = array(
        "term_id" => (int) $menu->term_id,
        "name" => $menu->name,
        "slug" => $menu->slug,
        "item_count" => is_array($items) ? count($items) : 0
    );
}
$options_field_presence = array(
    "contacts_group_fields_present" => false,
    "modal_cta_group_fields_present" => false,
    "values_dumped" => false,
    "options_page_group_count" => 0
);
if (function_exists("acf_get_field_groups")) {
    $opt_groups = acf_get_field_groups(array("options_page" => "fp02-site-settings"));
    $options_field_presence["options_page_group_count"] = count($opt_groups);
    foreach ($opt_groups as $g) {
        if (($g["key"] ?? "") === "group_fp02_site_options_contacts") { $options_field_presence["contacts_group_fields_present"] = true; }
        if (($g["key"] ?? "") === "group_fp02_site_options_modal_cta") { $options_field_presence["modal_cta_group_fields_present"] = true; }
    }
}
$out = array(
    "phase" => "V9-06D.3",
    "mode" => "READ_ONLY",
    "timestamp" => gmdate("c"),
    "identity" => array(
        "runtime" => "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky",
        "domain" => home_url("/"),
        "siteurl" => get_option("siteurl"),
        "db_name" => DB_NAME,
        "db_prefix" => $wpdb->prefix,
        "active_theme" => $theme->get_stylesheet(),
        "active_theme_version" => $theme->get("Version"),
        "active_plugins" => $active,
        "service_cpt_registered" => post_type_exists("service"),
        "service_cpt" => $service_obj ? array(
            "public" => (bool) $service_obj->public,
            "hierarchical" => (bool) $service_obj->hierarchical,
            "has_archive" => (bool) $service_obj->has_archive
        ) : null,
        "acf_pro_active" => in_array("advanced-custom-fields-pro/acf.php", $active, true),
        "acf_extended_pro_active" => in_array("acf-extended-pro/acf-extended.php", $active, true),
        "acf_free_active" => in_array("advanced-custom-fields/acf.php", $active, true),
        "acf_groups_count" => count($acf_groups),
        "acf_local_field_groups" => $acf_groups,
        "acf_options_pages" => $acf_options_pages,
        "wpilot_write_enabled" => $wpilot_write,
        "shpigovsky_core_mode" => defined("SHPIGOVSKY_CORE_MODE") ? SHPIGOVSKY_CORE_MODE : null
    ),
    "site_options" => array(
        "show_on_front" => get_option("show_on_front"),
        "page_on_front" => (int) get_option("page_on_front"),
        "page_for_posts" => (int) get_option("page_for_posts"),
        "permalink_structure" => get_option("permalink_structure"),
        "rewrite_flush_status" => "NOT_DETECTABLE_AS_BOOLEAN_ASSUME_NOT_FLUSHED_SINCE_D2",
        "options_page_fields_presence" => $options_field_presence
    ),
    "counts" => array(
        "pages" => count($pages),
        "services" => count($services),
        "posts" => count($posts),
        "menus" => count($menus)
    ),
    "pages" => $pages,
    "services" => $services,
    "posts" => $posts,
    "menus" => $menus,
    "mutations" => array(
        "runtime_content_writes" => 0,
        "database_writes" => 0,
        "wpilot_writes" => 0
    )
);
echo json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
