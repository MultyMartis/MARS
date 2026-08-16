<?php
/**
 * PROD-P13-FU01 QA: native slug persist / clear / collision on drafts, then cleanup.
 * Does not mass-regenerate production URLs.
 */
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

function fp02_rows($type) {
    $posts = get_posts(array(
        'post_type'              => $type,
        'post_status'            => array('publish', 'draft', 'pending', 'private', 'future'),
        'numberposts'            => -1,
        'orderby'                => 'ID',
        'order'                  => 'ASC',
        'suppress_filters'       => true,
    ));
    $out = array();
    foreach ($posts as $p) {
        $out[] = array(
            'ID'          => (int) $p->ID,
            'post_type'   => $p->post_type,
            'post_status' => $p->post_status,
            'post_parent' => (int) $p->post_parent,
            'title'       => $p->post_title,
            'post_name'   => $p->post_name,
            'permalink'   => get_permalink($p),
        );
    }
    return $out;
}

function fp02_fingerprint($rows) {
    $map = array();
    foreach ($rows as $row) {
        $map[(string) $row['ID']] = $row['post_name'] . '|' . $row['permalink'];
    }
    ksort($map);
    return $map;
}

function fp02_clear_post_globals() {
    unset($_POST['post_name'], $_POST['fp02_post_name'], $_REQUEST['post_name']);
}

$before_services     = fp02_rows('service');
$before_specialists  = fp02_rows('specialist');
$qa_ids              = array();
$out                 = array(
    'utc'      => gmdate('c'),
    'wpilot'   => array(),
    'hooks'    => array(),
    'service'  => array(),
    'specialist' => array(),
    'collision'  => array(),
    'cleanup'    => array(),
    'url_safety' => array(),
);

$wpilot_opts = get_option('metacode_wpilot', get_option('wpilot', null));
$out['wpilot'] = array(
    'write_enabled_option'     => get_option('wpilot_write_enabled', get_option('metacode_wpilot_write_enabled', null)),
    'write_enabled_from_opts'  => (is_array($wpilot_opts) && array_key_exists('write_enabled', $wpilot_opts)) ? (bool) $wpilot_opts['write_enabled'] : null,
);

$out['hooks']['has_metabox_action'] = has_action('add_meta_boxes', array('Shpigovsky\\Core\\Admin\\PermalinkSlugUX', 'register_metabox'));
$out['hooks']['has_after_title']    = has_action('edit_form_after_title', array('Shpigovsky\\Core\\Admin\\PermalinkSlugUX', 'render_native_permalink_box'));
$out['hooks']['has_admin_css']      = has_action('admin_head', array('Shpigovsky\\Core\\Admin\\PermalinkSlugUX', 'admin_css'));
$out['hooks']['has_insert_data']    = has_filter('wp_insert_post_data', array('Shpigovsky\\Core\\Admin\\PermalinkSlugUX', 'filter_insert_post_data'));
$out['hooks']['has_unique_slug']    = has_filter('wp_unique_post_slug', array('Shpigovsky\\Core\\Admin\\PermalinkSlugUX', 'filter_unique_slug'));

// --- Service persist ---
fp02_clear_post_globals();
$svc_id = wp_insert_post(array(
    'post_type'   => 'service',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Service Persist',
    'post_name'   => 'fp02-fu01-qa-service-persist',
), true);
if (is_wp_error($svc_id)) {
    $out['service']['create_error'] = $svc_id->get_error_message();
} else {
    $qa_ids[] = (int) $svc_id;
    $created = get_post((int) $svc_id);
    $_POST['post_name'] = 'fp02-fu01-qa-service-native';
    $upd = wp_update_post(array(
        'ID'        => (int) $svc_id,
        'post_name' => 'fp02-fu01-qa-service-native',
        'post_title'=> 'FP02 FU01 QA Service Persist',
    ), true);
    $reloaded = get_post((int) $svc_id);
    $out['service']['persist'] = array(
        'ID'            => (int) $svc_id,
        'created_slug'  => $created ? $created->post_name : null,
        'update_result' => is_wp_error($upd) ? $upd->get_error_message() : (int) $upd,
        'reloaded_slug' => $reloaded ? $reloaded->post_name : null,
        'permalink'     => $reloaded ? get_permalink($reloaded) : null,
        'pass'          => $reloaded && 'fp02-fu01-qa-service-native' === $reloaded->post_name,
    );

    // Unrelated title edit must not regenerate slug.
    fp02_clear_post_globals();
    wp_update_post(array(
        'ID'         => (int) $svc_id,
        'post_title' => 'FP02 FU01 QA Service Persist Title Only',
    ));
    $after_title = get_post((int) $svc_id);
    $out['service']['unrelated_title_edit'] = array(
        'slug' => $after_title ? $after_title->post_name : null,
        'pass' => $after_title && 'fp02-fu01-qa-service-native' === $after_title->post_name,
    );

    // Clear → regenerate from title.
    $_POST['post_name'] = '';
    wp_update_post(array(
        'ID'         => (int) $svc_id,
        'post_title' => 'FP02 FU01 QA Service Regen Title',
        'post_name'  => '',
    ));
    $after_clear = get_post((int) $svc_id);
    $expected    = sanitize_title('FP02 FU01 QA Service Regen Title');
    $out['service']['clear_regenerate'] = array(
        'slug'     => $after_clear ? $after_clear->post_name : null,
        'expected' => $expected,
        'pass'     => $after_clear && $expected === $after_clear->post_name,
    );
}

// --- Specialist persist ---
fp02_clear_post_globals();
$sp_id = wp_insert_post(array(
    'post_type'   => 'specialist',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Specialist Persist',
    'post_name'   => 'fp02-fu01-qa-specialist-persist',
), true);
if (is_wp_error($sp_id)) {
    $out['specialist']['create_error'] = $sp_id->get_error_message();
} else {
    $qa_ids[] = (int) $sp_id;
    $_POST['post_name'] = 'fp02-fu01-qa-spec-native';
    wp_update_post(array(
        'ID'        => (int) $sp_id,
        'post_name' => 'fp02-fu01-qa-spec-native',
        'post_title'=> 'FP02 FU01 QA Specialist Persist',
    ));
    $reloaded = get_post((int) $sp_id);
    $permalink = $reloaded ? get_permalink($reloaded) : '';
    $out['specialist']['persist'] = array(
        'ID'            => (int) $sp_id,
        'reloaded_slug' => $reloaded ? $reloaded->post_name : null,
        'permalink'     => $permalink,
        'rewrite_ok'    => is_string($permalink) && false !== strpos($permalink, '/specyalisty/fp02-fu01-qa-spec-native'),
        'pass'          => $reloaded && 'fp02-fu01-qa-spec-native' === $reloaded->post_name,
    );

    fp02_clear_post_globals();
    wp_update_post(array(
        'ID'         => (int) $sp_id,
        'post_title' => 'FP02 FU01 QA Specialist Persist Title Only',
    ));
    $after_title = get_post((int) $sp_id);
    $out['specialist']['unrelated_title_edit'] = array(
        'slug' => $after_title ? $after_title->post_name : null,
        'pass' => $after_title && 'fp02-fu01-qa-spec-native' === $after_title->post_name,
    );

    $_POST['post_name'] = '';
    wp_update_post(array(
        'ID'         => (int) $sp_id,
        'post_title' => 'FP02 FU01 QA Specialist Regen Title',
        'post_name'  => '',
    ));
    $after_clear = get_post((int) $sp_id);
    $expected    = sanitize_title('FP02 FU01 QA Specialist Regen Title');
    $out['specialist']['clear_regenerate'] = array(
        'slug'     => $after_clear ? $after_clear->post_name : null,
        'expected' => $expected,
        'pass'     => $after_clear && $expected === $after_clear->post_name,
    );
}

// --- Collision drafts ---
fp02_clear_post_globals();
$c1 = wp_insert_post(array(
    'post_type'   => 'service',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Collision',
    'post_name'   => 'fp02-fu01-qa-collision',
), true);
$c2 = wp_insert_post(array(
    'post_type'   => 'service',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Collision',
    'post_name'   => 'fp02-fu01-qa-collision',
), true);
$c3 = wp_insert_post(array(
    'post_type'   => 'service',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Collision',
    'post_name'   => 'fp02-fu01-qa-collision',
), true);
foreach (array($c1, $c2, $c3) as $cid) {
    if (!is_wp_error($cid) && $cid) {
        $qa_ids[] = (int) $cid;
    }
}
$s1 = is_wp_error($c1) ? null : get_post((int) $c1);
$s2 = is_wp_error($c2) ? null : get_post((int) $c2);
$s3 = is_wp_error($c3) ? null : get_post((int) $c3);
$out['collision']['service'] = array(
    'first'  => $s1 ? $s1->post_name : null,
    'second' => $s2 ? $s2->post_name : null,
    'third'  => $s3 ? $s3->post_name : null,
    'pass'   => $s1 && $s2 && $s3
        && 'fp02-fu01-qa-collision' === $s1->post_name
        && 'fp02-fu01-qa-collision-copy-01' === $s2->post_name
        && 'fp02-fu01-qa-collision-copy-02' === $s3->post_name,
);

fp02_clear_post_globals();
$sp1 = wp_insert_post(array(
    'post_type'   => 'specialist',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Spec Collision',
    'post_name'   => 'fp02-fu01-qa-spec-collision',
), true);
$sp2 = wp_insert_post(array(
    'post_type'   => 'specialist',
    'post_status' => 'draft',
    'post_title'  => 'FP02 FU01 QA Spec Collision',
    'post_name'   => 'fp02-fu01-qa-spec-collision',
), true);
foreach (array($sp1, $sp2) as $cid) {
    if (!is_wp_error($cid) && $cid) {
        $qa_ids[] = (int) $cid;
    }
}
$p1 = is_wp_error($sp1) ? null : get_post((int) $sp1);
$p2 = is_wp_error($sp2) ? null : get_post((int) $sp2);
$out['collision']['specialist'] = array(
    'first'  => $p1 ? $p1->post_name : null,
    'second' => $p2 ? $p2->post_name : null,
    'pass'   => $p1 && $p2
        && 'fp02-fu01-qa-spec-collision' === $p1->post_name
        && 'fp02-fu01-qa-spec-collision-copy-01' === $p2->post_name,
);

// Cleanup QA objects (force delete).
foreach ($qa_ids as $id) {
    $deleted = wp_delete_post((int) $id, true);
    $out['cleanup'][] = array(
        'ID'      => (int) $id,
        'deleted' => (bool) $deleted,
    );
}

global $wpdb;
$log_table = $wpdb->prefix . 'user_activity_log';
$exists    = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $log_table));
$log_deleted = 0;
if ($exists === $log_table) {
    $log_deleted = (int) $wpdb->query("DELETE FROM {$log_table} WHERE object_title LIKE 'FP02 FU01 QA%'");
}
$out['cleanup_activity_log_rows'] = $log_deleted;

$after_services    = fp02_rows('service');
$after_specialists = fp02_rows('specialist');
$bf_s = fp02_fingerprint($before_services);
$af_s = fp02_fingerprint($after_services);
$bf_p = fp02_fingerprint($before_specialists);
$af_p = fp02_fingerprint($after_specialists);

$changed_services = array();
foreach (array_unique(array_merge(array_keys($bf_s), array_keys($af_s))) as $id) {
    if (!isset($bf_s[$id]) || !isset($af_s[$id]) || $bf_s[$id] !== $af_s[$id]) {
        $changed_services[] = $id;
    }
}
$changed_specialists = array();
foreach (array_unique(array_merge(array_keys($bf_p), array_keys($af_p))) as $id) {
    if (!isset($bf_p[$id]) || !isset($af_p[$id]) || $bf_p[$id] !== $af_p[$id]) {
        $changed_specialists[] = $id;
    }
}

$out['url_safety'] = array(
    'service_count_before'     => count($before_services),
    'service_count_after'      => count($after_services),
    'specialist_count_before'  => count($before_specialists),
    'specialist_count_after'   => count($after_specialists),
    'service_accidental'       => $changed_services,
    'specialist_accidental'    => $changed_specialists,
    'pass'                     => 0 === count($changed_services) && 0 === count($changed_specialists)
        && count($before_services) === count($after_services)
        && count($before_specialists) === count($after_specialists),
);

$out['after_inventory'] = array(
    'services'    => $after_services,
    'specialists' => $after_specialists,
);

echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
echo "\n";
