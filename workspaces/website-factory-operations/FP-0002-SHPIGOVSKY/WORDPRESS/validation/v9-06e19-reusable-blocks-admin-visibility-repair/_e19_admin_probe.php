<?php
$pages = array(
    'fp02-site-settings-general',
    'fp02-site-settings-blocks',
    'fp02-block-final-form',
    'fp02-block-specialists',
    'fp02-block-reviews',
    'fp02-block-cta-bands',
    'fp02-reviews',
);
$rows = array();
foreach ($pages as $page) {
    $url = 'http://shpigovsky.test/wp-admin/admin.php?page=' . $page;
    $ch = curl_init($url);
    curl_setopt_array($ch, array(
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 20,
    ));
    $body = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $final = (string) curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
    curl_close($ch);
    $state = 'unknown';
    if (is_string($body)) {
        if (stripos($body, 'wp-login') !== false || stripos($final, 'wp-login') !== false) {
            $state = 'login_redirect';
        } elseif (stripos($body, 'acf-field') !== false) {
            $state = 'fields_present';
        } elseif (stripos($body, 'не связаны группы полей') !== false || stripos($body, 'No Custom Field Groups') !== false) {
            $state = 'no_field_groups';
        }
    }
    $rows[] = array('page' => $page, 'http' => $code, 'state' => $state, 'final_url' => $final);
}
echo json_encode($rows, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
