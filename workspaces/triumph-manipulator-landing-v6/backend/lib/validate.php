<?php

declare(strict_types=1);

const TRIUMPH_NAME_MIN = 2;
const TRIUMPH_NAME_MAX = 100;
const TRIUMPH_PHONE_DIGITS_MIN = 10;
const TRIUMPH_PHONE_DIGITS_MAX = 15;
const TRIUMPH_META_MAX = 500;

/**
 * @param array<string, mixed> $input
 * @return array{data: array<string, string>, errors: array<string, string>}
 */
function triumph_validate_lead(array $input): array
{
    $errors = [];
    $data = [];

    $name = triumph_sanitize_text((string) ($input['name'] ?? ''), TRIUMPH_NAME_MAX);
    if (mb_strlen($name, 'UTF-8') < TRIUMPH_NAME_MIN) {
        $errors['name'] = 'Укажите имя (минимум 2 символа).';
    } else {
        $data['name'] = $name;
    }

    $phoneRaw = triumph_sanitize_text((string) ($input['phone'] ?? ''), 64);
    $phoneNormalized = triumph_normalize_phone($phoneRaw);
    if ($phoneNormalized === '') {
        $errors['phone'] = 'Укажите корректный номер телефона.';
    } else {
        $data['phone'] = $phoneNormalized;
        $data['phone_display'] = triumph_format_phone_display($phoneNormalized);
    }

    $metaFields = [
        'page_url' => 2048,
        'page_type' => 64,
        'form_id' => 64,
        'form_name' => 128,
        'cta_source' => 128,
        'timestamp' => 64,
        'form_started_at' => 64,
    ];

    foreach ($metaFields as $field => $maxLength) {
        $value = triumph_sanitize_text((string) ($input[$field] ?? ''), $maxLength);
        if ($value === '') {
            $errors[$field] = 'Некорректные служебные данные формы.';
            continue;
        }
        $data[$field] = $value;
    }

    if (!isset($errors['page_url']) && !preg_match('#^https?://#i', $data['page_url'])) {
        $errors['page_url'] = 'Некорректный адрес страницы.';
    }

    if (!isset($errors['timestamp']) && strtotime($data['timestamp']) === false) {
        $errors['timestamp'] = 'Некорректная метка времени.';
    }

    if (!isset($errors['form_started_at']) && strtotime($data['form_started_at']) === false) {
        $errors['form_started_at'] = 'Некорректная метка начала заполнения.';
    }

    return ['data' => $data, 'errors' => $errors];
}

function triumph_sanitize_text(string $value, int $maxLength): string
{
    $value = trim($value);
    $value = strip_tags($value);
    $value = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $value) ?? '';
    $value = mb_convert_encoding($value, 'UTF-8', 'UTF-8');

    if (mb_strlen($value, 'UTF-8') > $maxLength) {
        $value = mb_substr($value, 0, $maxLength, 'UTF-8');
    }

    return $value;
}

function triumph_normalize_phone(string $value): string
{
    $digits = preg_replace('/\D+/', '', $value) ?? '';

    if ($digits === '') {
        return '';
    }

    if (strlen($digits) === 11 && $digits[0] === '8') {
        $digits = '7' . substr($digits, 1);
    }

    if (strlen($digits) === 10) {
        $digits = '7' . $digits;
    }

    $length = strlen($digits);
    if ($length < TRIUMPH_PHONE_DIGITS_MIN || $length > TRIUMPH_PHONE_DIGITS_MAX) {
        return '';
    }

    return '+' . $digits;
}

function triumph_format_phone_display(string $normalized): string
{
    $digits = preg_replace('/\D+/', '', $normalized) ?? '';

    if (strlen($digits) !== 11 || $digits[0] !== '7') {
        return $normalized;
    }

    $local = substr($digits, 1);

    return sprintf(
        '+7 (%s) %s-%s-%s',
        substr($local, 0, 3),
        substr($local, 3, 3),
        substr($local, 6, 2),
        substr($local, 8, 2)
    );
}
