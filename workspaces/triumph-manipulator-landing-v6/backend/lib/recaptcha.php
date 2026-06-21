<?php

declare(strict_types=1);

require_once __DIR__ . '/config-loader.php';

/**
 * @return list<string>
 */
function triumph_recaptcha_last_error_codes(): array
{
    /** @var list<string>|null $codes */
    $codes = $GLOBALS['triumph_recaptcha_last_error_codes'] ?? null;

    return is_array($codes) ? $codes : [];
}

/**
 * @param list<string> $codes
 */
function triumph_recaptcha_set_error_codes(array $codes): void
{
    $filtered = [];

    foreach ($codes as $code) {
        if (is_string($code) && $code !== '') {
            $filtered[] = $code;
        }
    }

    $GLOBALS['triumph_recaptcha_last_error_codes'] = $filtered;
}

/**
 * @param list<string> $codes
 * @param array<string, mixed> $config
 */
function triumph_recaptcha_log_failure(array $config, array $codes): void
{
    triumph_recaptcha_set_error_codes($codes);

    $label = $codes !== [] ? implode(', ', $codes) : 'unknown';
    error_log('[triumph] recaptcha verify failed: ' . $label);

    if (!empty($config['recaptcha_debug_public_error'])) {
        error_log('[triumph] recaptcha debug enabled: safe error code for troubleshooting: ' . $label);
    }
}

/**
 * @param array<string, mixed> $config
 */
function triumph_verify_recaptcha(string $token, array $config): bool
{
    triumph_recaptcha_set_error_codes([]);

    $secret = trim((string) ($config['recaptcha_secret_key'] ?? ''));

    if ($secret === '' || $secret === 'PASTE_SECRET_KEY_HERE') {
        if (triumph_is_production_host()) {
            error_log('[triumph] recaptcha_secret_key missing on production host');
            triumph_recaptcha_log_failure($config, ['missing-secret']);

            return false;
        }

        error_log('[triumph] WARNING: recaptcha_secret_key not configured; skipping verification (non-production)');

        return true;
    }

    if ($token === '') {
        if (triumph_is_production_host()) {
            triumph_recaptcha_log_failure($config, ['missing-token']);

            return false;
        }

        return true;
    }

    $payload = http_build_query(
        [
            'secret' => $secret,
            'response' => $token,
            'remoteip' => triumph_get_client_ip(),
        ]
    );

    $context = stream_context_create(
        [
            'http' => [
                'method' => 'POST',
                'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
                'content' => $payload,
                'timeout' => 8,
            ],
        ]
    );

    $raw = @file_get_contents('https://www.google.com/recaptcha/api/siteverify', false, $context);

    if (!is_string($raw) || $raw === '') {
        triumph_recaptcha_log_failure($config, ['request-failed']);

        return false;
    }

    /** @var array<string, mixed>|null $decoded */
    $decoded = json_decode($raw, true);

    if (is_array($decoded) && !empty($decoded['success'])) {
        return true;
    }

    $codes = [];
    if (is_array($decoded) && isset($decoded['error-codes']) && is_array($decoded['error-codes'])) {
        foreach ($decoded['error-codes'] as $code) {
            if (is_string($code) && $code !== '') {
                $codes[] = $code;
            }
        }
    }

    triumph_recaptcha_log_failure($config, $codes !== [] ? $codes : ['unknown']);

    return false;
}

function triumph_get_client_ip(): string
{
    $candidates = [
        $_SERVER['HTTP_CF_CONNECTING_IP'] ?? null,
        $_SERVER['HTTP_X_FORWARDED_FOR'] ?? null,
        $_SERVER['REMOTE_ADDR'] ?? null,
    ];

    foreach ($candidates as $candidate) {
        if (!is_string($candidate) || $candidate === '') {
            continue;
        }

        $parts = array_map('trim', explode(',', $candidate));
        $ip = $parts[0] ?? '';

        if (filter_var($ip, FILTER_VALIDATE_IP)) {
            return $ip;
        }
    }

    return '';
}
