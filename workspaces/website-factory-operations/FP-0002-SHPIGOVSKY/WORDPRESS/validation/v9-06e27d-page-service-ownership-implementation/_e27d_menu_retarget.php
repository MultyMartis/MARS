<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$item_id = 301;
$before_meta = [];
foreach (['_menu_item_type','_menu_item_object','_menu_item_object_id','_menu_item_url','_menu_item_menu_item_parent','_menu_item_classes','_menu_item_target','_menu_item_xfn'] as $key) {
    $before_meta[$key] = get_post_meta($item_id, $key, true);
}
$before_item = get_post($item_id);
$before_nav = wp_get_nav_menu_items('primary');
$before_match = null;
foreach ((array)$before_nav as $nav) {
    if ((int)$nav->ID === $item_id) {
        $before_match = [
            'ID' => $nav->ID,
            'title' => $nav->title,
            'url' => $nav->url,
            'object_id' => $nav->object_id,
            'object' => $nav->object,
            'type' => $nav->type,
            'menu_order' => $nav->menu_order,
            'menu_item_parent' => $nav->menu_item_parent,
        ];
        break;
    }
}
update_post_meta($item_id, '_menu_item_type', 'custom');
update_post_meta($item_id, '_menu_item_object', 'custom');
update_post_meta($item_id, '_menu_item_object_id', '0');
update_post_meta($item_id, '_menu_item_url', '/uslugi/zavisimosti/');
$after_meta = [];
foreach (['_menu_item_type','_menu_item_object','_menu_item_object_id','_menu_item_url','_menu_item_menu_item_parent','_menu_item_classes','_menu_item_target','_menu_item_xfn'] as $key) {
    $after_meta[$key] = get_post_meta($item_id, $key, true);
}
$after_nav = wp_get_nav_menu_items('primary');
$after_match = null;
foreach ((array)$after_nav as $nav) {
    if ((int)$nav->ID === $item_id) {
        $after_match = [
            'ID' => $nav->ID,
            'title' => $nav->title,
            'url' => $nav->url,
            'object_id' => $nav->object_id,
            'object' => $nav->object,
            'type' => $nav->type,
            'menu_order' => $nav->menu_order,
            'menu_item_parent' => $nav->menu_item_parent,
        ];
        break;
    }
}
echo json_encode([
    'method' => 'custom_url_binding',
    'menu_item_id' => $item_id,
    'before_meta' => $before_meta,
    'after_meta' => $after_meta,
    'before_nav_item' => $before_match,
    'after_nav_item' => $after_match,
    'before_post_title' => $before_item ? $before_item->post_title : null,
    'after_post_title' => get_post($item_id)->post_title,
], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
