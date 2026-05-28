<?php

declare(strict_types=1);

const TRIUMPH_SPAM_MIN_SECONDS = 3;
const TRIUMPH_SPAM_MAX_SECONDS = 86400;

/**
 * @param array<string, mixed> $input
 * @return array{ok: bool, message: string}
 */
function triumph_check_antispam(array $input): array
{
    $honeypot = trim((string) ($input['company_url'] ?? ''));
    if ($honeypot !== '') {
        return ['ok' => false, 'message' => 'Заявка отклонена.'];
    }

    $startedAt = strtotime((string) ($input['form_started_at'] ?? ''));
    $submittedAt = strtotime((string) ($input['timestamp'] ?? ''));

    if ($startedAt === false || $submittedAt === false) {
        return ['ok' => false, 'message' => 'Некорректные данные формы.'];
    }

    $delta = $submittedAt - $startedAt;

    if ($delta < TRIUMPH_SPAM_MIN_SECONDS) {
        return ['ok' => false, 'message' => 'Форма отправлена слишком быстро. Попробуйте ещё раз.'];
    }

    if ($delta > TRIUMPH_SPAM_MAX_SECONDS) {
        return ['ok' => false, 'message' => 'Сессия формы устарела. Обновите страницу и отправьте снова.'];
    }

    return ['ok' => true, 'message' => ''];
}
