<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) {
  $mysqli->query("INSERT INTO " . DB_PREFIX . "seo_url SET store_id=0, language_id=1, query='information/guarantee', keyword='guarantee'");
  $after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
  echo json_encode(['ok'=>true,'action'=>'insert','after'=>$after?$after->fetch_assoc():null]);
  exit;
}
$old = $row['query'];
if ($old !== 'information/guarantee') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/guarantee' WHERE keyword='guarantee'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
echo json_encode(['ok'=>true,'before'=>$row,'after'=>$after?$after->fetch_assoc():null]);
