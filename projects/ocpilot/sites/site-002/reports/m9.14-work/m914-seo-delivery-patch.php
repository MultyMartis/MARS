<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='delivery' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) { echo json_encode(['ok'=>false,'error'=>'no_row']); exit; }
$old = $row['query'];
if ($old !== 'information/delivery') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/delivery' WHERE keyword='delivery'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='delivery' LIMIT 1");
echo json_encode(['ok'=>true,'before'=>$row,'after'=>$after?$after->fetch_assoc():null]);
