<?php

declare(strict_types=1);

require_once __DIR__ . '/config-loader.php';

/**
 * @param array<string, mixed> $config
 */
function triumph_verify_recaptcha(string $token, array $config): bool
{
    $secret = trim((string) ($config['recaptcha_secret_key'] ?? ''));

    if ($secret === '' || $secret === 'PASTE_SECRET_KEY_HERE') {
        if (triumph_is_production_host()) {
            error_log('[triumph] recaptcha_secret_key missing on production host');

            return false;
        }

        error_log('[triumph] WARNING: recaptcha_secret_key not configured; skipping verification (non-production)');

        return true;
    }

    if ($token === '') {
        return !triumph_is_production_host();
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
        error_log('[triumph] recaptcha siteverify request failed');

        return false;
    }

    /** @var array<string, mixed>|null $decoded */
    $decoded = json_decode($raw, true);

    return is_array($decoded) && !empty($decoded['success']);
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
