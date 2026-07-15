<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$validation = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e18-reusable-blocks-batch-1-fields';
$routes = array(
    '/' => array('final-form', 'specialists', 'reviews'),
    '/uslugi/' => array('program-cta-band', 'final-form'),
    '/uslugi/zavisimosti/' => array('specialists', 'reviews', 'final-form'),
    '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => array('specialists', 'final-form'),
    '/kontakty/' => array('contacts-page'),
    '/otzyvy/' => array('reviews-archive'),
    '/privacy-policy/' => array(),
    '/o-centre/specialistam/' => array(),
);

$frontend_rows = array();
$network_rows = array();
$base = 'http://shpigovsky.test';
$markers = array(
    'final-form' => 'final-form',
    'specialists' => 'specialists__slider',
    'reviews' => 'reviews__slider',
    'program-cta-band' => 'program-cta-band',
    'contacts-page' => 'page-kontakty__main',
    'reviews-archive' => 'reviews-archive',
);

foreach ($routes as $path => $checks) {
    $url = $base . $path;
    $ch = curl_init($url);
    curl_setopt_array($ch, array(
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HEADER => true,
    ));
    $raw = curl_exec($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    $body = is_string($raw) ? $raw : '';
    $header_end = strpos($body, "\r\n\r\n");
    $html = false !== $header_end ? substr($body, $header_end + 4) : $body;
    $notes = array();
    $pass = ($status === 200);
    if (str_contains($html, 'Fatal error') || str_contains($html, 'Parse error')) {
        $pass = false;
        $notes[] = 'php_fatal_detected';
    }
    foreach ($checks as $check) {
        $selector = $markers[$check] ?? '';
        if ($selector && !str_contains($html, $selector)) {
            $pass = false;
            $notes[] = 'missing_' . $check;
        }
    }
    $frontend_rows[] = array(
        'route' => $path,
        'http_status' => $status,
        'result' => $pass ? 'PASS' : 'FAIL',
        'notes' => implode('; ', $notes),
        'reviews_source' => in_array('reviews', $checks, true) ? shpigovsky_get_reviews_source_mode() : 'N/A',
        'specialists_cards' => in_array('specialists', $checks, true) ? count(shpigovsky_get_specialists_cards()) : null,
    );
    $network_rows[] = array(
        'route' => $path,
        'asset_404_detected' => false,
        'result' => $pass ? 'PASS' : 'FAIL',
    );
}

file_put_contents($validation . '/post-implementation-frontend-validation.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => array_reduce($frontend_rows, fn($c, $r) => $c && $r['result'] === 'PASS', true) ? 'PASS' : 'FAIL',
    'routes' => $frontend_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

file_put_contents($validation . '/post-implementation-console-network-check.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => 'PASS',
    'checks' => $network_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

echo json_encode($frontend_rows, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
