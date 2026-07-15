<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$ids = json_decode('[9, 10, 17, 21, 25]', true);
$approved = array_map('intval', $ids);
$results = [];
foreach ($approved as $id) {
    $post = get_post($id);
    if (!$post || $post->post_type !== 'page') {
        $results[] = ['id' => $id, 'result' => 'FAIL', 'error' => 'not_page_or_missing'];
        continue;
    }
    $before = $post->post_status;
    if ($before === 'trash') {
        $results[] = ['id' => $id, 'before' => $before, 'after' => 'trash', 'result' => 'SKIP_ALREADY_TRASH', 'command' => 'none'];
        continue;
    }
    $trashed = wp_trash_post($id);
    $after_post = get_post($id);
    $after = $after_post ? $after_post->post_status : null;
    $results[] = [
        'id' => $id,
        'before' => $before,
        'after' => $after,
        'result' => ($after === 'trash') ? 'PASS' : 'FAIL',
        'command' => 'wp_trash_post(' . $id . ')',
        'trashed_return' => (bool)$trashed,
    ];
}
echo json_encode(['results' => $results], JSON_UNESCAPED_UNICODE);
