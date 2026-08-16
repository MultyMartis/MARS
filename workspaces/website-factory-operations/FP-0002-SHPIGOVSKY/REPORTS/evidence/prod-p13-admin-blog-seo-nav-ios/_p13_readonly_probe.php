<?php
/**
 * PROD-P13 read-only intake probe. Delete after run.
 */
require dirname(__DIR__, 2) . '/wp-load.php';

header('Content-Type: application/json; charset=utf-8');

global $wpdb, $menu, $submenu;

$out = array(
	'utc' => gmdate('c'),
	'home' => home_url('/'),
	'siteurl' => site_url('/'),
	'wp_version' => get_bloginfo('version'),
	'stylesheet' => get_stylesheet(),
	'environment_type' => function_exists('wp_get_environment_type') ? wp_get_environment_type() : null,
	'wp_environment_constant' => defined('WP_ENVIRONMENT_TYPE') ? WP_ENVIRONMENT_TYPE : null,
	'blog_public' => get_option('blog_public'),
	'users' => array(),
	'metacode_exists' => false,
	'mli_admin' => null,
	'admin_user' => null,
	'social_links' => null,
	'social_platforms' => null,
	'activity_log' => null,
	'plugins' => array(),
	'mu_plugins' => array(),
	'admin_menu_top' => array(),
	'admin_menu_options_hits' => array(),
	'cpts' => array(),
	'wpilot' => array(),
);

$users = get_users(array('fields' => 'all'));
foreach ($users as $u) {
	$roles = is_array($u->roles) ? $u->roles : array();
	$row = array(
		'ID' => (int) $u->ID,
		'login' => $u->user_login,
		'email' => $u->user_email,
		'display_name' => $u->display_name,
		'roles' => $roles,
		'post_counts' => array(),
	);
	foreach (array('post', 'page', 'service', 'specialist', 'attachment') as $pt) {
		$q = new WP_Query(array(
			'author' => (int) $u->ID,
			'post_type' => $pt,
			'post_status' => 'any',
			'posts_per_page' => 1,
			'fields' => 'ids',
		));
		$row['post_counts'][$pt] = (int) $q->found_posts;
	}
	$out['users'][] = $row;
	if ($u->user_login === 'metacode') {
		$out['metacode_exists'] = true;
	}
	if ($u->user_login === 'mli_admin_fp0002') {
		$out['mli_admin'] = $row;
	}
	if ($u->user_login === 'admin') {
		$out['admin_user'] = $row;
	}
}

if (function_exists('get_field')) {
	$out['social_links'] = get_field('social_links', 'option');
	$out['social_platforms'] = get_field('social_platforms', 'option');
}

$table = $wpdb->prefix . 'user_activity_log';
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $table));
if ($exists === $table) {
	$out['activity_log'] = array(
		'table' => $table,
		'count' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$table}"),
		'user0_count' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$table} WHERE user_id = 0"),
		'sample' => $wpdb->get_results("SELECT id, user_id, action, object_id, object_type, LEFT(object_title,80) AS object_title, created_at FROM {$table} ORDER BY id DESC LIMIT 15", ARRAY_A),
		'qa_like' => $wpdb->get_results("SELECT id, user_id, action, object_id, object_type, object_title, created_at FROM {$table} WHERE object_title LIKE '%fp02-p12%' OR object_title LIKE '%collision-qa%' OR object_title LIKE '%P12%' LIMIT 50", ARRAY_A),
	);
}

$active = (array) get_option('active_plugins', array());
$out['plugins'] = $active;
if (function_exists('get_mu_plugins')) {
	$out['mu_plugins'] = array_keys(get_mu_plugins());
}

require_once ABSPATH . 'wp-admin/includes/admin.php';
do_action('admin_menu');
if (is_array($menu)) {
	foreach ($menu as $item) {
		$slug = isset($item[2]) ? (string) $item[2] : '';
		$title = isset($item[0]) ? wp_strip_all_tags((string) $item[0]) : '';
		$out['admin_menu_top'][] = array('title' => $title, 'slug' => $slug);
		if (stripos($title, 'option') !== false || stripos($slug, 'option') !== false || stripos($title, 'Options') !== false) {
			$out['admin_menu_options_hits'][] = array('where' => 'top', 'title' => $title, 'slug' => $slug);
		}
	}
}
if (is_array($submenu)) {
	foreach ($submenu as $parent => $items) {
		foreach ($items as $item) {
			$slug = isset($item[2]) ? (string) $item[2] : '';
			$title = isset($item[0]) ? wp_strip_all_tags((string) $item[0]) : '';
			if (stripos($title, 'option') !== false || stripos($slug, 'option') !== false) {
				$out['admin_menu_options_hits'][] = array('where' => $parent, 'title' => $title, 'slug' => $slug);
			}
		}
	}
}

$cpts = get_post_types(array(), 'objects');
foreach ($cpts as $pt) {
	if (! $pt instanceof WP_Post_Type) {
		continue;
	}
	if (! $pt->_builtin || in_array($pt->name, array('post', 'page'), true)) {
		$out['cpts'][] = array(
			'name' => $pt->name,
			'public' => (bool) $pt->public,
			'publicly_queryable' => (bool) $pt->publicly_queryable,
			'has_archive' => $pt->has_archive,
			'rewrite' => $pt->rewrite,
			'supports' => get_all_post_type_supports($pt->name),
		);
	}
}

$out['wpilot'] = array(
	'active' => in_array('metacode-wpilot/metacode-wpilot.php', $active, true) || in_array('wpilot/wpilot.php', $active, true),
	'write_enabled_option' => get_option('wpilot_write_enabled', get_option('metacode_wpilot_write_enabled')),
);

$out['seo_yoast'] = in_array('wordpress-seo/wp-seo.php', $active, true);
$out['seo_rankmath'] = false;
foreach ($active as $p) {
	if (strpos($p, 'seo') !== false) {
		$out['seo_plugins'][] = $p;
	}
	if (strpos($p, 'acf-extended') !== false || strpos($p, 'acfe') !== false) {
		$out['acfe_plugin'] = $p;
	}
}

echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
exit;
