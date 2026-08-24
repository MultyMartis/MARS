<?php
/**
 * ISEO form mail / security configuration.
 * TEST_MODE must be false in normal production.
 */
if (!defined("ISEO_FORM_CONFIG_LOADED")) {
    define("ISEO_FORM_CONFIG_LOADED", true);
}

return array(
    // TEMPORARY: true during controlled mail tests only.
    "test_mode" => false,

    "test_recipients" => array("im.work@mail.ru"),

    // Normal production recipients (original active set only).
    "production_recipients" => array(
        "nikel007i33@yandex.ru",
    ),

    "from_email" => "noreply@i-seo.su",
    // Production secret must come from a local-only PHP file.
    "hmac_secret" => null,
    "local_secret_path" => __DIR__ . "/.iseo-form-runtime/iseo-form-secrets.local.php",

    "honeypot_field" => "contact_company_url",

    "min_fill_seconds" => 3,
    "max_fill_seconds" => 86400,

    "rate_limit_burst_max" => 3,
    "rate_limit_burst_window" => 300,
    "rate_limit_hour_max" => 10,
    "rate_limit_hour_window" => 3600,

    "duplicate_window" => 600,

    "runtime_dir" => __DIR__ . "/.iseo-form-runtime",
);
