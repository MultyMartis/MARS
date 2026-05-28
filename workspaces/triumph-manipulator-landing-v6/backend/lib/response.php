<?php

declare(strict_types=1);

/**
 * @param array<string, mixed> $payload
 */
function json_response(int $statusCode, array $payload): void
{
    if (!headers_sent()) {
        http_response_code($statusCode);
        header('Content-Type: application/json; charset=utf-8');
        header('X-Content-Type-Options: nosniff');
        header('Cache-Control: no-store');
    }

    echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
    exit;
}

/**
 * @param array<string, string> $errors
 */
function json_success(string $message, int $statusCode = 200): void
{
    json_response($statusCode, [
        'success' => true,
        'message' => $message,
    ]);
}

/**
 * @param array<string, string> $errors
 */
function json_error(int $statusCode, string $message, array $errors = []): void
{
    $payload = [
        'success' => false,
        'message' => $message,
    ];

    if ($errors !== []) {
        $payload['errors'] = $errors;
    }

    json_response($statusCode, $payload);
}
