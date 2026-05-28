<?php

declare(strict_types=1);

/**
 * @param array<string, string> $lead
 */
function triumph_send_lead_email(array $lead): bool
{
    /** @var array<string, mixed> $config */
    $config = require dirname(__DIR__) . '/config/mail.config.php';

    $to = (string) ($config['to'] ?? '');
    $fromAddress = (string) ($config['from_address'] ?? '');
    $fromName = (string) ($config['from_name'] ?? 'Triumph');
    $subjectPrefix = (string) ($config['subject_prefix'] ?? '[Triumph]');
    $useSmtp = (bool) ($config['use_smtp'] ?? false);

    if ($to === '' || $fromAddress === '') {
        return false;
    }

    $formName = $lead['form_name'] ?? 'Форма';
    $subject = sprintf('%s Новая заявка — %s', rtrim($subjectPrefix), $formName);

    $body = triumph_build_lead_email_body($lead);
    $headers = triumph_build_mail_headers($fromAddress, $fromName);

    if ($useSmtp) {
        // Reserved for future SMTP transport on hosting.
        return false;
    }

    return mail($to, triumph_encode_mail_subject($subject), $body, $headers);
}

/**
 * @param array<string, string> $lead
 */
function triumph_build_lead_email_body(array $lead): string
{
    $lines = [
        'Новая заявка с сайта Triumph Manipulator',
        str_repeat('—', 40),
        'Имя: ' . ($lead['name'] ?? ''),
        'Телефон: ' . ($lead['phone_display'] ?? $lead['phone'] ?? ''),
        '',
        'Страница: ' . ($lead['page_url'] ?? ''),
        'Тип страницы: ' . ($lead['page_type'] ?? ''),
        'Форма: ' . ($lead['form_name'] ?? '') . ' (' . ($lead['form_id'] ?? '') . ')',
        'Источник CTA: ' . ($lead['cta_source'] ?? '—'),
        'Время отправки: ' . ($lead['timestamp'] ?? ''),
        str_repeat('—', 40),
        'Письмо сформировано автоматически.',
    ];

    return implode("\r\n", $lines);
}

function triumph_build_mail_headers(string $fromAddress, string $fromName): string
{
    $encodedFromName = triumph_encode_mail_header_value($fromName);

    return implode("\r\n", [
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=UTF-8',
        'Content-Transfer-Encoding: 8bit',
        sprintf('From: %s <%s>', $encodedFromName, $fromAddress),
        'X-Mailer: Triumph-Form-Handler',
    ]);
}

function triumph_encode_mail_subject(string $subject): string
{
    if (function_exists('mb_encode_mimeheader')) {
        return mb_encode_mimeheader($subject, 'UTF-8', 'B', "\r\n");
    }

    return $subject;
}

function triumph_encode_mail_header_value(string $value): string
{
    if (function_exists('mb_encode_mimeheader')) {
        return mb_encode_mimeheader($value, 'UTF-8', 'B', "\r\n");
    }

    return $value;
}
