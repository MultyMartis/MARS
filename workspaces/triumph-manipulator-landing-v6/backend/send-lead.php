<?php
declare(strict_types=1);

/**
 * Triumph V5 landing — lead form mailer (PHP mail() or SMTP).
 * POST only, JSON responses, no secrets in repo.
 */

const SUBJECT_LINE = 'Заявка на МАНИПУЛЯТОР';
const ACCENT_COLOR = '#e1002d';
const EMAIL_MAX_WIDTH = '600px';
const MAX_FIELD_LENGTH = 500;
const MAX_EXTRA_FIELDS = 20;

const META_FIELDS = [
    'page_url',
    'page_title',
    'page_referrer',
    'page_type',
    'form_id',
    'form_name',
    'cta_source',
    'timestamp',
    'form_started_at',
    'landing_id',
    'company_url',
    'g-recaptcha-response',
    'consent',
];

const FIELD_LABELS = [
    'name' => 'Имя',
    'phone' => 'Телефон',
    'email' => 'Email',
    'message' => 'Сообщение',
    'comment' => 'Комментарий',
];

require_once __DIR__ . '/lib/config-loader.php';
require_once __DIR__ . '/lib/recaptcha.php';
require_once __DIR__ . '/lib/smtp-mailer.php';

ini_set('display_errors', '0');
error_reporting(E_ALL);

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    jsonResponse(false, 'Метод не поддерживается', 405);
}

$input = collectInput();

if (honeypotTriggered($input)) {
    jsonResponse(true, 'Заявка отправлена');
}

$config = triumph_load_config();
$recaptchaToken = trim((string) ($input['g-recaptcha-response'] ?? ''));

if (!triumph_verify_recaptcha($recaptchaToken, $config)) {
    $debugExtra = null;
    if (!empty($config['recaptcha_debug_public_error'])) {
        $codes = triumph_recaptcha_last_error_codes();
        if ($codes !== []) {
            $debugExtra = ['recaptchaError' => implode(', ', $codes)];
        }
    }

    jsonResponse(
        false,
        'Проверка безопасности не пройдена. Обновите страницу и попробуйте снова.',
        422,
        $debugExtra
    );
}

$phone = sanitizeField((string) ($input['phone'] ?? ''));
if ($phone === '') {
    jsonResponse(false, 'Заполните телефон', 422);
}

if (phoneDigitsCount($phone) < 10) {
    jsonResponse(false, 'Заполните телефон', 422);
}

$name = sanitizeField((string) ($input['name'] ?? ''));
$meta = extractMeta($input);
$extra = extractExtraFields($input);
$technical = buildTechnicalContext();

$subject = buildSubject($phone, $meta);
[$htmlBody, $textBody] = buildEmailBodies($name, $phone, $extra, $meta, $technical);

$sent = sendMail($subject, $htmlBody, $textBody, $input);

if (!$sent) {
    jsonResponse(false, 'Не удалось отправить заявку. Позвоните нам напрямую.', 500);
}

jsonResponse(true, 'Заявка отправлена');

/**
 * @return array<string, string>
 */
function collectInput(): array
{
    $data = [];

    foreach ($_POST as $key => $value) {
        if (!is_string($key)) {
            continue;
        }
        if (is_array($value)) {
            continue;
        }
        $data[$key] = is_string($value) ? $value : (string) $value;
    }

    return $data;
}

/**
 * @param array<string, string> $input
 */
function honeypotTriggered(array $input): bool
{
    $honeypot = trim((string) ($input['company_url'] ?? ''));

    return $honeypot !== '';
}

function sanitizeField(string $value): string
{
    $value = str_replace("\0", '', $value);
    $value = trim($value);

    if (mb_strlen($value, 'UTF-8') > MAX_FIELD_LENGTH) {
        $value = mb_substr($value, 0, MAX_FIELD_LENGTH, 'UTF-8');
    }

    return $value;
}

function phoneDigitsCount(string $phone): int
{
    return strlen(preg_replace('/\D+/', '', $phone) ?? '');
}

/**
 * @param array<string, string> $input
 * @return array<string, string>
 */
function extractMeta(array $input): array
{
    $meta = [];

    foreach (META_FIELDS as $field) {
        if (!array_key_exists($field, $input)) {
            continue;
        }
        $value = sanitizeField($input[$field]);
        if ($value !== '') {
            $meta[$field] = $value;
        }
    }

    return $meta;
}

/**
 * @param array<string, string> $input
 * @return array<string, string>
 */
function extractExtraFields(array $input): array
{
    $extra = [];

    foreach ($input as $key => $value) {
        if (!is_string($key) || in_array($key, META_FIELDS, true)) {
            continue;
        }
        if (in_array($key, ['name', 'phone'], true)) {
            continue;
        }

        $clean = sanitizeField($value);
        if ($clean === '') {
            continue;
        }

        $extra[$key] = $clean;

        if (count($extra) >= MAX_EXTRA_FIELDS) {
            break;
        }
    }

    return $extra;
}

/**
 * @return array<string, string>
 */
function buildTechnicalContext(): array
{
    return [
        'submitted_at' => date('d.m.Y H:i:s'),
        'ip' => getClientIp(),
        'user_agent' => sanitizeField((string) ($_SERVER['HTTP_USER_AGENT'] ?? '')),
        'host' => sanitizeField((string) ($_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? '')),
    ];
}

/**
 * @param array<string, string> $meta
 */
function buildSubject(string $phone, array $meta): string
{
    unset($phone, $meta);

    return SUBJECT_LINE;
}

function formatPhoneForDisplay(string $phone): string
{
    $digits = preg_replace('/\D+/', '', $phone) ?? '';

    if (strlen($digits) === 11 && ($digits[0] === '7' || $digits[0] === '8')) {
        if ($digits[0] === '8') {
            $digits = '7' . substr($digits, 1);
        }

        return sprintf(
            '+7 (%s) %s-%s-%s',
            substr($digits, 1, 3),
            substr($digits, 4, 3),
            substr($digits, 7, 2),
            substr($digits, 9, 2)
        );
    }

    return sanitizeField($phone);
}

function phoneTelHref(string $phone): string
{
    $digits = preg_replace('/\D+/', '', $phone) ?? '';

    if ($digits === '') {
        return '';
    }

    if (strlen($digits) === 11 && $digits[0] === '8') {
        $digits = '7' . substr($digits, 1);
    }

    if (strlen($digits) === 10) {
        $digits = '7' . $digits;
    }

    return 'tel:+' . ltrim($digits, '+');
}

/**
 * @param array<string, string> $extra
 * @param array<string, string> $meta
 * @param array<string, string> $technical
 * @return array{0: string, 1: string}
 */
function buildEmailBodies(string $name, string $phone, array $extra, array $meta, array $technical): array
{
    $phoneDisplay = formatPhoneForDisplay($phone);
    $telHref = phoneTelHref($phone);
    $formLabel = metaValue($meta, 'form_name', 'form_id');
    $ctaLabel = metaValue($meta, 'cta_source');
    $landingLabel = metaValue($meta, 'landing_id', 'page_type');
    $pageLabel = metaValue($meta, 'page_title', 'page_url');
    $submittedAt = metaValue($meta, 'timestamp') !== '—'
        ? metaValue($meta, 'timestamp')
        : $technical['submitted_at'];

    $html = '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>'
        . '<body style="margin:0;padding:0;background:#f4f4f4;">'
        . '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#f4f4f4;padding:16px 0;">'
        . '<tr><td align="center">'
        . '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:' . EMAIL_MAX_WIDTH . ';width:100%;background:#ffffff;border:1px solid #e6e6e6;">'
        . operatorBlockHtml($name, $phoneDisplay, $telHref, $formLabel, $ctaLabel, $landingLabel, $pageLabel)
        . detailsBlockHtml($extra, $meta, $submittedAt, $formLabel, $ctaLabel, $landingLabel, $pageLabel)
        . technicalBlockHtml($extra, $meta, $technical)
        . '</table>'
        . '</td></tr></table>'
        . '</body></html>';

    $text = buildPlainTextBody(
        $name,
        $phoneDisplay,
        $telHref,
        $extra,
        $meta,
        $technical,
        $submittedAt,
        $formLabel,
        $ctaLabel,
        $landingLabel,
        $pageLabel
    );

    return [$html, $text];
}

function metaValue(array $meta, string ...$keys): string
{
    foreach ($keys as $key) {
        if (!empty($meta[$key])) {
            return $meta[$key];
        }
    }

    return '—';
}

function operatorBlockHtml(
    string $name,
    string $phoneDisplay,
    string $telHref,
    string $formLabel,
    string $ctaLabel,
    string $landingLabel,
    string $pageLabel
): string {
    $phoneCell = $telHref !== ''
        ? '<a href="' . e($telHref) . '" style="color:' . ACCENT_COLOR . ';text-decoration:none;font-size:32px;line-height:1.2;font-weight:bold;">' . e($phoneDisplay) . '</a>'
        : '<span style="font-size:32px;line-height:1.2;font-weight:bold;color:#111111;">' . e($phoneDisplay) . '</span>';

    $ctaBlock = $telHref !== ''
        ? '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:20px 0 0;">'
            . '<tr><td align="center" style="background:' . ACCENT_COLOR . ';border-radius:4px;padding:16px 20px;">'
            . '<a href="' . e($telHref) . '" style="display:block;color:#ffffff;font-size:18px;font-weight:bold;text-decoration:none;">Перезвонить клиенту</a>'
            . '</td></tr></table>'
        : '<p style="margin:20px 0 0;padding:16px 20px;background:' . ACCENT_COLOR . ';color:#ffffff;font-size:18px;font-weight:bold;text-align:center;">Перезвонить клиенту</p>';

    return '<tr><td style="padding:28px 24px 24px;font-family:Arial,Helvetica,sans-serif;color:#111111;">'
        . '<p style="margin:0 0 20px;font-size:24px;line-height:1.25;font-weight:bold;color:#111111;">Новая заявка — ТРИУМФ</p>'
        . '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#fafafa;border:1px solid #ececec;border-left:4px solid ' . ACCENT_COLOR . ';margin:0 0 20px;">'
        . '<tr><td style="padding:18px 16px;">'
        . '<p style="margin:0 0 6px;font-size:12px;line-height:1.4;color:#666666;text-transform:uppercase;letter-spacing:0.04em;">Телефон клиента</p>'
        . '<p style="margin:0;">' . $phoneCell . '</p>'
        . '</td></tr></table>'
        . operatorLineHtml('Имя', $name !== '' ? $name : '—')
        . operatorLineHtml('Форма / CTA', $formLabel . ($ctaLabel !== '—' ? ' · ' . $ctaLabel : ''))
        . operatorLineHtml('Посадочная', $landingLabel)
        . operatorLineHtml('Страница', $pageLabel)
        . $ctaBlock
        . '</td></tr>';
}

function operatorLineHtml(string $label, string $value): string
{
    return '<p style="margin:0 0 10px;font-size:15px;line-height:1.45;color:#111111;">'
        . '<span style="display:block;font-size:12px;color:#666666;margin-bottom:2px;">' . e($label) . '</span>'
        . '<span style="font-weight:bold;">' . e($value) . '</span>'
        . '</p>';
}

/**
 * @param array<string, string> $extra
 * @param array<string, string> $meta
 */
function detailsBlockHtml(
    array $extra,
    array $meta,
    string $submittedAt,
    string $formLabel,
    string $ctaLabel,
    string $landingLabel,
    string $pageLabel
): string {
    $rows = [
        'Источник заявки' => metaValue($meta, 'landing_id', 'page_type'),
        'Тип формы' => $formLabel,
        'Посадочная страница' => $pageLabel,
        'Источник CTA' => $ctaLabel,
        'Дата и время' => $submittedAt,
    ];

    foreach ($extra as $key => $value) {
        $rows[fieldLabel($key)] = $value;
    }

    return blockHtml('Детали заявки', $rows, false);
}

/**
 * @param array<string, string> $extra
 * @param array<string, string> $meta
 * @param array<string, string> $technical
 */
function technicalBlockHtml(array $extra, array $meta, array $technical): string
{
    $rows = [
        'IP' => $technical['ip'],
        'User-Agent' => $technical['user_agent'],
        'Host' => $technical['host'],
        'Referrer' => metaValue($meta, 'page_referrer'),
        'URL страницы' => metaValue($meta, 'page_url'),
        'landing_id' => metaValue($meta, 'landing_id'),
        'page_type' => metaValue($meta, 'page_type'),
        'form_id' => metaValue($meta, 'form_id'),
        'form_name' => metaValue($meta, 'form_name'),
        'cta_source' => metaValue($meta, 'cta_source'),
        'page_title' => metaValue($meta, 'page_title'),
        'timestamp' => metaValue($meta, 'timestamp'),
        'form_started_at' => metaValue($meta, 'form_started_at'),
        'consent' => metaValue($meta, 'consent'),
        'Дата приёма (сервер)' => $technical['submitted_at'],
    ];

    foreach ($extra as $key => $value) {
        $label = fieldLabel($key) . ' (raw)';
        if (!isset($rows[$label])) {
            $rows[$label] = $value;
        }
    }

    return blockHtml('Системная информация', $rows, true);
}

/**
 * @param array<string, string> $rows
 */
function blockHtml(string $title, array $rows, bool $muted): string
{
    $titleColor = $muted ? '#888888' : '#111111';
    $labelColor = $muted ? '#999999' : '#666666';
    $valueColor = $muted ? '#777777' : '#111111';
    $fontSize = $muted ? '12px' : '14px';
    $padding = $muted ? '16px 24px 24px' : '0 24px 24px';
    $borderTop = $muted ? '1px solid #ececec' : '1px solid #ececec';

    $body = '';
    foreach ($rows as $label => $value) {
        if ($value === '—') {
            continue;
        }
        $body .= '<tr>'
            . '<td style="padding:5px 12px 5px 0;vertical-align:top;width:38%;font-size:' . $fontSize . ';line-height:1.4;color:' . $labelColor . ';">' . e((string) $label) . '</td>'
            . '<td style="padding:5px 0;vertical-align:top;font-size:' . $fontSize . ';line-height:1.4;color:' . $valueColor . ';word-break:break-word;">' . e($value) . '</td>'
            . '</tr>';
    }

    if ($body === '') {
        return '';
    }

    return '<tr><td style="padding:' . $padding . ';border-top:' . $borderTop . ';font-family:Arial,Helvetica,sans-serif;">'
        . '<p style="margin:0 0 10px;font-size:' . ($muted ? '13px' : '16px') . ';font-weight:bold;color:' . $titleColor . ';">' . e($title) . '</p>'
        . '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;">'
        . $body
        . '</table>'
        . '</td></tr>';
}

/**
 * @param array<string, string> $extra
 * @param array<string, string> $meta
 * @param array<string, string> $technical
 */
function buildPlainTextBody(
    string $name,
    string $phoneDisplay,
    string $telHref,
    array $extra,
    array $meta,
    array $technical,
    string $submittedAt,
    string $formLabel,
    string $ctaLabel,
    string $landingLabel,
    string $pageLabel
): string {
    $lines = [
        'Новая заявка — ТРИУМФ',
        '',
        '=== ОПЕРАТОР ===',
        'Телефон: ' . $phoneDisplay . ($telHref !== '' ? ' (' . $telHref . ')' : ''),
        'Имя: ' . ($name !== '' ? $name : '—'),
        'Форма / CTA: ' . $formLabel . ($ctaLabel !== '—' ? ' · ' . $ctaLabel : ''),
        'Посадочная: ' . $landingLabel,
        'Страница: ' . $pageLabel,
        '>>> Перезвонить клиенту',
        '',
        sectionText('Детали заявки', plainDetailsRows($extra, $meta, $submittedAt, $formLabel, $ctaLabel, $pageLabel)),
        sectionText('Системная информация', [
            'IP' => $technical['ip'],
            'User-Agent' => $technical['user_agent'],
            'Host' => $technical['host'],
            'Referrer' => metaValue($meta, 'page_referrer'),
            'URL страницы' => metaValue($meta, 'page_url'),
            'landing_id' => metaValue($meta, 'landing_id'),
            'page_type' => metaValue($meta, 'page_type'),
            'form_id' => metaValue($meta, 'form_id'),
            'timestamp' => metaValue($meta, 'timestamp'),
            'form_started_at' => metaValue($meta, 'form_started_at'),
            'consent' => metaValue($meta, 'consent'),
            'Дата приёма (сервер)' => $technical['submitted_at'],
        ]),
    ];

    return implode("\n", $lines);
}

/**
 * @param array<string, string> $extra
 * @param array<string, string> $meta
 * @return array<string, string>
 */
function plainDetailsRows(
    array $extra,
    array $meta,
    string $submittedAt,
    string $formLabel,
    string $ctaLabel,
    string $pageLabel
): array {
    $rows = [
        'Источник заявки' => metaValue($meta, 'landing_id', 'page_type'),
        'Тип формы' => $formLabel,
        'Посадочная страница' => $pageLabel,
        'Источник CTA' => $ctaLabel,
        'Дата и время' => $submittedAt,
    ];

    foreach ($extra as $key => $value) {
        $rows[fieldLabel($key)] = $value;
    }

    return $rows;
}

/**
 * @param array<string, string> $rows
 */
function sectionText(string $title, array $rows): string
{
    $out = $title . "\n";

    foreach ($rows as $label => $value) {
        $out .= $label . ': ' . $value . "\n";
    }

    return $out . "\n";
}

function fieldLabel(string $key): string
{
    if (isset(FIELD_LABELS[$key])) {
        return FIELD_LABELS[$key];
    }

    $label = str_replace(['_', '-'], ' ', $key);

    return mb_convert_case($label, MB_CASE_TITLE, 'UTF-8');
}

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

/**
 * @param array<string, string> $input
 */
function sendMail(string $subject, string $htmlBody, string $textBody, array $input): bool
{
    $config = triumph_load_config();
    $fromAddress = buildFromAddress($config);
    $fromName = sanitizeField((string) ($config['from_name'] ?? ''));
    $boundary = 'b_' . bin2hex(random_bytes(8));

    $headers = [
        'MIME-Version: 1.0',
        'Content-Type: multipart/alternative; boundary="' . $boundary . '"',
    ];

    $replyTo = resolveReplyTo($input);
    if ($replyTo !== '') {
        $headers[] = 'Reply-To: ' . $replyTo;
    }

    $encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
    $body = "--{$boundary}\r\n"
        . "Content-Type: text/plain; charset=UTF-8\r\n"
        . "Content-Transfer-Encoding: base64\r\n\r\n"
        . chunk_split(base64_encode($textBody))
        . "--{$boundary}\r\n"
        . "Content-Type: text/html; charset=UTF-8\r\n"
        . "Content-Transfer-Encoding: base64\r\n\r\n"
        . chunk_split(base64_encode($htmlBody))
        . "--{$boundary}--";

    $recipients = resolveLeadRecipients($config);
    if ($recipients === []) {
        return false;
    }

    if (!empty($config['use_smtp'])) {
        /** @var array<string, mixed> $smtpConfig */
        $smtpConfig = is_array($config['smtp'] ?? null) ? $config['smtp'] : [];

        return triumph_smtp_send_message(
            $smtpConfig,
            $recipients,
            $fromAddress,
            $fromName,
            $encodedSubject,
            $headers,
            $body
        );
    }

    $headers[] = 'From: ' . formatFromHeader($fromAddress, $fromName);

    return @mail(implode(', ', $recipients), $encodedSubject, $body, implode("\r\n", $headers));
}

/**
 * @param array<string, mixed> $config
 * @return list<string>
 */
function resolveLeadRecipients(array $config): array
{
    $recipients = [];

    if (isset($config['recipients']) && is_array($config['recipients'])) {
        foreach ($config['recipients'] as $recipient) {
            if (!is_string($recipient)) {
                continue;
            }

            $email = stripHeaderInjection(trim($recipient));
            if ($email !== '' && filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $recipients[] = $email;
            }
        }
    }

    if ($recipients !== []) {
        return array_values(array_unique($recipients));
    }

    $fallback = stripHeaderInjection(trim((string) ($config['recipient'] ?? '')));
    if ($fallback !== '' && filter_var($fallback, FILTER_VALIDATE_EMAIL)) {
        return [$fallback];
    }

    return [];
}

/**
 * @param array<string, mixed> $config
 */
function buildFromAddress(array $config): string
{
    $configured = stripHeaderInjection(trim((string) ($config['from_address'] ?? '')));
    if ($configured !== '' && filter_var($configured, FILTER_VALIDATE_EMAIL)) {
        return $configured;
    }

    $host = sanitizeField((string) ($_SERVER['HTTP_HOST'] ?? $_SERVER['SERVER_NAME'] ?? 'localhost'));
    $host = preg_replace('/[^a-zA-Z0-9.\-]/', '', $host) ?? 'localhost';
    $localPart = sanitizeField((string) ($config['from_local_part'] ?? 'noreply'));

    return $localPart . '@' . $host;
}

function formatFromHeader(string $fromAddress, string $fromName): string
{
    if ($fromName === '') {
        return $fromAddress;
    }

    return '=?UTF-8?B?' . base64_encode($fromName) . '?= <' . $fromAddress . '>';
}

/**
 * @param array<string, string> $input
 */
function resolveReplyTo(array $input): string
{
    $email = sanitizeField((string) ($input['email'] ?? ''));

    if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return '';
    }

    return stripHeaderInjection($email);
}

function stripHeaderInjection(string $value): string
{
    return str_replace(["\r", "\n", "%0a", "%0d"], '', $value);
}

function getClientIp(): string
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

    return 'unknown';
}

function jsonResponse(bool $ok, string $message, int $status = 200, ?array $extra = null): void
{
    http_response_code($status);
    $payload = [
        'ok' => $ok,
        'message' => $message,
    ];

    if ($extra !== null) {
        foreach ($extra as $key => $value) {
            if (is_string($key) && is_string($value)) {
                $payload[$key] = $value;
            }
        }
    }

    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    exit;
}
