<?php
/**
 * ISEO-SU Metrika visitor IP param — read-only same-origin endpoint.
 *
 * Returns the server-seen client IP for the current request while enabled.
 * Authority: REMOTE_ADDR only (no untrusted forwarded headers).
 *
 * Cache-safe: private / no-store — never share one visitor IP with another.
 */
header("X-Content-Type-Options: nosniff");
header("Cache-Control: no-store, no-cache, must-revalidate, private, max-age=0");
header("Pragma: no-cache");
header("Expires: 0");
header("Vary: *");

$configPath = __DIR__ . "/metrika-visitor-ip-config.php";
$config = is_file($configPath) ? include $configPath : array("enabled" => false);

$enabled = is_array($config) && !empty($config["enabled"]);

if (!$enabled) {
    http_response_code(204);
    exit;
}

$raw = isset($_SERVER["REMOTE_ADDR"]) ? trim((string)$_SERVER["REMOTE_ADDR"]) : "";
$ip = filter_var($raw, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_IPV6);

if ($ip === false) {
    http_response_code(204);
    exit;
}

header("Content-Type: application/json; charset=UTF-8");
echo json_encode(
    array(
        "enabled" => true,
        "ipaddress" => $ip,
    ),
    JSON_UNESCAPED_SLASHES
);
exit;
