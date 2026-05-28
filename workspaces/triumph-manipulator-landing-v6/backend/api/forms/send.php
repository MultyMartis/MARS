<?php

declare(strict_types=1);

/**
 * Lead form endpoint for Triumph manipulator landing (v5).
 * POST multipart/form-data or application/x-www-form-urlencoded.
 */

ini_set('display_errors', '0');
error_reporting(E_ALL);

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'message' => 'Метод не поддерживается'], JSON_UNESCAPED_UNICODE);
    exit;
}

/**
 * @return array<string, mixed>
 */
function load_mailer_config(): array
{
    $configPath = dirname(__DIR__, 2) . '/config.php';
    $localPath = dirname(__DIR__, 2) . '/config.local.php';

    if (!is_file($configPath)) {
        return [];
    }

    /** @var array<string, mixed> $config */
    $config = require $configPath;

    if (is_file($localPath)) {
        /** @var array<string, mixed> $local */
        $local = require $localPath;
        $config = array_merge($config, $local);
    }

    return $config;
}

/**
 * @param mixed $value
 */
function sanitize_text($value, int $maxLength): string
{
    if (!is_string($value)) {
        return '';
    }

    $value = trim(str_replace(["\0", "\r"], '', $value));
    $value = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $value) ?? '';

    if (function_exists('mb_substr')) {
        return mb_substr($value, 0, $maxLength, 'UTF-8');
    }

    return substr($value, 0, $maxLength);
}

function sanitize_header_value(string $value): string
{
    return str_replace(["\r", "\n"], '', trim($value));
}

/**
 * @param array<string, string> $fields
 */
function json_response(bool $ok, string $message, int $status = 200, array $fields = []): void
{
    http_response_code($status);
    $payload = array_merge(['ok' => $ok, 'message' => $message], $fields);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    exit;
}

/**
 * @param array<string, string> $data
 */
function escape_html(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

/**
 * @param array<string, string> $row
 */
function table_row(string $label, string $value): string
{
    if ($value === '') {
        return '';
    }

    return '<tr><th style="text-align:left;padding:8px 12px 8px 0;vertical-align:top;color:#555;width:38%;">'
        . escape_html($label)
        . '</th><td style="padding:8px 0;vertical-align:top;color:#111;">'
        . escape_html($value)
        . '</td></tr>';
}

/**
 * @param array<string, string> $rows
 */
function render_table(array $rows): string
{
    $body = '';
    foreach ($rows as $label => $value) {
        $body .= table_row($label, $value);
    }

    if ($body === '') {
        return '<p style="margin:0;color:#666;">—</p>';
    }

    return '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px;line-height:1.45;">'
        . $body
        . '</table>';
}

function phone_digits(string $phone): string
{
    return preg_replace('/\D+/', '', $phone) ?? '';
}

function is_valid_email(string $email): bool
{
    return $email !== '' && filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

function resolve_host(): string
{
    $host = $_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? 'localhost';
    return sanitize_header_value((string) $host);
}

function resolve_client_ip(): string
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

        $parts = explode(',', $candidate);
        $ip = trim($parts[0]);
        if (filter_var($ip, FILTER_VALIDATE_IP) !== false) {
            return $ip;
        }
    }

    return 'unknown';
}

/**
 * @param array<string, mixed> $config
 * @param array<string, string> $payload
 */
function build_subject(array $config, array $payload): string
{
    $base = sanitize_text((string) ($config['subject_base'] ?? 'Заявка с лендинга Триумф'), 160);
    $sourceParts = array_filter([
        $payload['form_name'] ?? '',
        $payload['form_id'] ?? '',
        $payload['cta_source'] ?? '',
    ]);

    $source = sanitize_text(implode(' / ', array_unique($sourceParts)), 120);

    if ($source === '') {
        return $base;
    }

    return $base . ' — ' . $source;
}

/**
 * @param array<string, string> $payload
 * @param array<string, string> $technical
 */
function build_html_body(array $payload, array $technical, array $extraLeadFields): string
{
    $leadRows = [
        'Имя отправителя' => $payload['name'] ?? '',
        'Телефон' => $payload['phone'] ?? '',
    ];

    foreach ($extraLeadFields as $label => $value) {
        $leadRows[$label] = $value;
    }

    $sourceRows = [
        'ID формы' => $payload['form_id'] ?? '',
        'Название формы' => $payload['form_name'] ?? '',
        'CTA / источник' => $payload['cta_source'] ?? '',
        'Тип страницы' => $payload['page_type'] ?? '',
        'URL страницы' => $payload['page_url'] ?? '',
        'Заголовок страницы' => $payload['page_title'] ?? '',
        'Referrer' => $payload['page_referrer'] ?? '',
    ];

    $techRows = [
        'Дата и время' => $technical['submitted_at'] ?? '',
        'IP' => $technical['ip'] ?? '',
        'User-Agent' => $technical['user_agent'] ?? '',
        'Хост' => $technical['host'] ?? '',
    ];

    return '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>Заявка</title></head><body style="margin:0;padding:24px;background:#f4f6f8;font-family:Arial,sans-serif;color:#111;">'
        . '<div style="max-width:640px;margin:0 auto;background:#fff;border:1px solid #e3e7ee;border-radius:8px;padding:24px;">'
        . '<h1 style="margin:0 0 20px;font-size:20px;line-height:1.3;">Новая заявка с лендинга</h1>'
        . '<h2 style="margin:24px 0 12px;font-size:15px;color:#333;">1. Данные заявки</h2>'
        . render_table($leadRows)
        . '<h2 style="margin:24px 0 12px;font-size:15px;color:#333;">2. Источник</h2>'
        . render_table($sourceRows)
        . '<h2 style="margin:24px 0 12px;font-size:15px;color:#333;">3. Техническая информация</h2>'
        . render_table($techRows)
        . '</div></body></html>';
}

/**
 * @param array<string, string> $payload
 * @param array<string, string> $technical
 */
function build_plain_body(array $payload, array $technical, array $extraLeadFields): string
{
    $lines = ["=== Данные заявки ==="];

    $lines[] = 'Имя: ' . ($payload['name'] ?? '');
    $lines[] = 'Телефон: ' . ($payload['phone'] ?? '');

    foreach ($extraLeadFields as $label => $value) {
        $lines[] = $label . ': ' . $value;
    }

    $lines[] = '';
    $lines[] = '=== Источник ===';
    $lines[] = 'ID формы: ' . ($payload['form_id'] ?? '');
    $lines[] = 'Название формы: ' . ($payload['form_name'] ?? '');
    $lines[] = 'CTA / источник: ' . ($payload['cta_source'] ?? '');
    $lines[] = 'Тип страницы: ' . ($payload['page_type'] ?? '');
    $lines[] = 'URL: ' . ($payload['page_url'] ?? '');
    $lines[] = 'Заголовок: ' . ($payload['page_title'] ?? '');
    $lines[] = 'Referrer: ' . ($payload['page_referrer'] ?? '');
    $lines[] = '';
    $lines[] = '=== Техническая информация ===';
    $lines[] = 'Дата и время: ' . ($technical['submitted_at'] ?? '');
    $lines[] = 'IP: ' . ($technical['ip'] ?? '');
    $lines[] = 'User-Agent: ' . ($technical['user_agent'] ?? '');
    $lines[] = 'Хост: ' . ($technical['host'] ?? '');

    return implode("\n", $lines);
}

/**
 * @param array<string, string> $headers
 */
function send_multipart_mail(string $to, string $subject, string $htmlBody, string $plainBody, array $headers): bool
{
    $boundary = 'mars_' . bin2hex(random_bytes(8));
    $message = "--{$boundary}\r\n"
        . "Content-Type: text/plain; charset=UTF-8\r\n"
        . "Content-Transfer-Encoding: 8bit\r\n\r\n"
        . $plainBody . "\r\n\r\n"
        . "--{$boundary}\r\n"
        . "Content-Type: text/html; charset=UTF-8\r\n"
        . "Content-Transfer-Encoding: 8bit\r\n\r\n"
        . $htmlBody . "\r\n\r\n"
        . "--{$boundary}--";

    $headerLines = array_merge($headers, [
        'MIME-Version: 1.0',
        'Content-Type: multipart/alternative; boundary="' . $boundary . '"',
    ]);

    return mail($to, $subject, $message, implode("\r\n", $headerLines));
}

$config = load_mailer_config();
$maxField = (int) ($config['max_field_length'] ?? 2000);
$maxPhone = (int) ($config['max_phone_length'] ?? 32);
$maxName = (int) ($config['max_name_length'] ?? 120);

$reserved = [
    'page_url',
    'page_title',
    'page_referrer',
    'page_type',
    'form_id',
    'form_name',
    'cta_source',
    'timestamp',
    'form_started_at',
    'company_url',
    'consent',
];

/** @var array<string, string> $payload */
$payload = [];
$extraLeadFields = [];

foreach ($_POST as $key => $value) {
    if (!is_string($key) || !is_scalar($value)) {
        continue;
    }

    $normalizedKey = sanitize_text($key, 64);
    $normalizedValue = sanitize_text((string) $value, $maxField);

    if ($normalizedKey === '') {
        continue;
    }

    if (in_array($normalizedKey, $reserved, true)) {
        $payload[$normalizedKey] = $normalizedValue;
        continue;
    }

    if ($normalizedKey === 'name') {
        $payload['name'] = sanitize_text($normalizedValue, $maxName);
        continue;
    }

    if ($normalizedKey === 'phone') {
        $payload['phone'] = sanitize_text($normalizedValue, $maxPhone);
        continue;
    }

    if ($normalizedKey === 'email' || $normalizedKey === 'mail') {
        $payload['email'] = sanitize_text($normalizedValue, 160);
        continue;
    }

    $label = ucfirst(str_replace('_', ' ', $normalizedKey));
    $extraLeadFields[$label] = $normalizedValue;
}

// Honeypot: bots that fill hidden company_url get a silent success.
$honeypot = $payload['company_url'] ?? '';
if ($honeypot !== '') {
    json_response(true, 'Заявка отправлена');
}

$phone = $payload['phone'] ?? '';
if ($phone === '' || strlen(phone_digits($phone)) < 10) {
    json_response(false, 'Заполните телефон', 422);
}

$payload['name'] = $payload['name'] ?? '';
$host = resolve_host();
$submittedAt = (new DateTimeImmutable('now', new DateTimeZone('Europe/Moscow')))->format('d.m.Y H:i:s (T)');

$technical = [
    'submitted_at' => $submittedAt,
    'ip' => resolve_client_ip(),
    'user_agent' => sanitize_text((string) ($_SERVER['HTTP_USER_AGENT'] ?? ''), $maxField),
    'host' => $host,
];

$recipient = sanitize_header_value((string) ($config['recipient'] ?? ''));
if ($recipient === '' || !is_valid_email($recipient)) {
    json_response(false, 'Не удалось отправить заявку. Позвоните нам напрямую.', 500);
}

$fromLocal = sanitize_header_value((string) ($config['from_local_part'] ?? 'noreply'));
$fromEmail = $fromLocal . '@' . preg_replace('/:\d+$/', '', $host);
if (!is_valid_email($fromEmail)) {
    $fromEmail = $fromLocal . '@localhost.localdomain';
}

$subject = sanitize_header_value(build_subject($config, $payload));
$htmlBody = build_html_body($payload, $technical, $extraLeadFields);
$plainBody = build_plain_body($payload, $technical, $extraLeadFields);

$headers = [
    'From: ' . $fromEmail,
];

$userEmail = $payload['email'] ?? '';
if (is_valid_email($userEmail)) {
    $headers[] = 'Reply-To: ' . sanitize_header_value($userEmail);
}

$sent = send_multipart_mail($recipient, $subject, $htmlBody, $plainBody, $headers);

if (!$sent) {
    json_response(false, 'Не удалось отправить заявку. Позвоните нам напрямую.', 500);
}

json_response(true, 'Заявка отправлена');
