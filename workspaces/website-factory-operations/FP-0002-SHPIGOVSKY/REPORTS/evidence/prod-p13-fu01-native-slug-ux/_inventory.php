<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

function fp02_rows($type) {
    $posts = get_posts(array(
        'post_type' => $type,
        'post_status' => array('publish', 'draft', 'pending', 'private', 'future'),
        'numberposts' => -1,
        'orderby' => 'ID',
        'order' => 'ASC',
        'suppress_filters' => true,
    ));
    $out = array();
    foreach ($posts as $p) {
        $out[] = array(
            'ID' => (int) $p->ID,
            'post_type' => $p->post_type,
            'post_status' => $p->post_status,
            'post_parent' => (int) $p->post_parent,
            'title' => $p->post_title,
            'post_name' => $p->post_name,
            'permalink' => get_permalink($p),
        );
    }
    return $out;
}

$wpilot = get_option('wpilot_write_enabled', get_option('metacode_wpilot_write_enabled', null));
$wpilot_opts = get_option('metacode_wpilot', get_option('wpilot', null));
$wpilot_from_opts = null;
if (is_array($wpilot_opts) && array_key_exists('write_enabled', $wpilot_opts)) {
    $wpilot_from_opts = (bool) $wpilot_opts['write_enabled'];
}

$cpts = get_post_types(array(), 'objects');
$cpt_inv = array();
foreach ($cpts as $name => $obj) {
    $public_single = (bool) $obj->public && (bool) $obj->publicly_queryable && false !== $obj->rewrite;
    $class = 'C';
    if (!empty($obj->_builtin) && in_array($name, array('post', 'page'), true)) {
        $class = 'C';
    } elseif ($public_single) {
        $class = 'A';
    } elseif ((bool) $obj->public && ! $obj->publicly_queryable) {
        $class = 'B';
    }
    $cpt_inv[] = array(
        'name' => $name,
        'public' => (bool) $obj->public,
        'publicly_queryable' => (bool) $obj->publicly_queryable,
        'has_archive' => $obj->has_archive,
        'rewrite' => $obj->rewrite,
        'viewable' => is_post_type_viewable($obj),
        'supports_title' => post_type_supports($name, 'title'),
        '_builtin' => (bool) $obj->_builtin,
        'class' => $class,
    );
}

echo json_encode(array(
    'utc' => gmdate('c'),
    'wpilot_write_enabled_option' => $wpilot,
    'wpilot_write_enabled_from_opts' => $wpilot_from_opts,
    'services' => fp02_rows('service'),
    'specialists' => fp02_rows('specialist'),
    'cpts' => $cpt_inv,
    'permalink_structure' => get_option('permalink_structure'),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
echo "\n";
