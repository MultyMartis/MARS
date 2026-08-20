<?php
require_once __DIR__ . "/iseo-form-security.php";
header("Content-Type: application/json; charset=utf-8");
header("Cache-Control: no-store");
echo json_encode(iseo_form_issue_token());
