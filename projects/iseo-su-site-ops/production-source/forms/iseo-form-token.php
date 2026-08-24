<?php
require_once __DIR__ . "/iseo-form-security.php";
header("Content-Type: application/json; charset=utf-8");
header("Cache-Control: no-store");
$token = iseo_form_issue_token();
if (!is_array($token)) {
    http_response_code(503);
    echo json_encode(array("error" => "unavailable"));
    exit;
}
echo json_encode($token);
