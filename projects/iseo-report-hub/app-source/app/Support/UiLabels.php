<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Manager-facing Russian labels for Report Hub UI chrome.
 * Technical / machine keys stay available via tech* helpers for collapsed details.
 */
final class UiLabels
{
    /** @var array<string, string> */
    private const BLOCK_KEYS = [
        'executive_summary' => 'Краткое резюме',
        'work_completed' => 'Что сделали',
        'results_summary' => 'Результаты',
        'risks_and_blockers' => 'Риски и блокеры',
        'key_findings' => 'Ключевые выводы',
        'next_month_plan' => 'План на следующий месяц',
        'client_notes' => 'Заметки для клиента',
        'internal_notes' => 'Внутренние заметки',
    ];

    /** @var array<string, string> */
    private const READINESS_KEYS = [
        'monthly_exists' => 'Месячный отчет найден',
        'period_exists' => 'Отчетный период найден',
        'title_present' => 'Название заполнено',
        'preview_renderable' => 'Предпросмотр собирается',
        'render_mode_valid' => 'Режим генерации корректный',
        'has_non_archived_blocks' => 'Есть активные блоки отчета',
        'required_blocks_present' => 'Обязательные блоки есть',
        'required_blocks_reviewed' => 'Обязательные блоки проверены',
        'no_draft_or_in_progress_blocks' => 'Нет черновых блоков',
        'source_weekly_refs_resolve' => 'Связанные недельные заметки найдены',
        'status_finalized' => 'Статус — финализирован',
        'finalized_at_present' => 'Дата финализации заполнена',
    ];

    /** Exact / prefix maps for user-visible readiness and action messages. */
    /** @var array<string, string> */
    private const MESSAGES = [
        'Monthly report found.' => 'Месячный отчет найден.',
        'Monthly report missing.' => 'Месячный отчет не найден.',
        'Parent reporting period found.' => 'Отчетный период найден.',
        'Parent reporting period missing.' => 'Отчетный период не найден.',
        'Title missing.' => 'Название не заполнено.',
        'Title present.' => 'Название заполнено.',
        'Title empty.' => 'Название пустое.',
        'Preview not assembled.' => 'Предпросмотр не собирается.',
        'Preview assembles successfully.' => 'Предпросмотр собирается успешно.',
        'Preview assembly failed.' => 'Не удалось собрать предпросмотр.',
        'Render mode invalid for finalize.' => 'Режим генерации не подходит для финализации.',
        'Render mode invalid.' => 'Режим генерации некорректен.',
        'No non-archived blocks.' => 'Нет активных блоков отчета.',
        'At least one non-archived block is required.' => 'Нужен хотя бы один активный блок отчета.',
        'Required blocks missing.' => 'Не найдены обязательные блоки.',
        'All required blocks present.' => 'Все обязательные блоки есть.',
        'Required blocks not reviewed/approved.' => 'Обязательные блоки еще не проверены.',
        'Required blocks are reviewed or approved.' => 'Обязательные блоки проверены.',
        'Draft/in_progress blocks remain.' => 'Остаются черновые блоки.',
        'Draft/in_progress remain.' => 'Остаются черновые блоки.',
        'No non-archived draft/in_progress blocks.' => 'Черновых блоков нет.',
        'Source weekly refs unresolved.' => 'Связанные недельные заметки не найдены.',
        'Weekly refs unresolved.' => 'Связанные недельные заметки не найдены.',
        'All source weekly checkpoint refs resolve.' => 'Все связанные недельные заметки найдены.',
        'Status must be finalized.' => 'Статус должен быть «Финализирован».',
        'Status is finalized.' => 'Статус — финализирован.',
        'finalized_at required.' => 'Нужна дата финализации.',
        'finalized_at present.' => 'Дата финализации заполнена.',
        'finalized_at missing.' => 'Дата финализации не заполнена.',
        'Role cannot submit for review.' => 'Роль не позволяет отправить на проверку.',
        'Role cannot mark reviewed.' => 'Роль не позволяет отметить проверенным.',
        'Role cannot finalize.' => 'Роль не позволяет финализировать.',
        'Only admin_owner can reopen.' => 'Открыть снова может только admin_owner.',
        'Forbidden.' => 'Недостаточно прав.',
        'Export not found.' => 'Файл отчета не найден.',
        'Share not found.' => 'Ссылка не найдена.',
        'Not found.' => 'Не найдено.',
        'Share service unavailable.' => 'Сервис ссылок недоступен.',
        'Shares loaded.' => 'Ссылки загружены.',
    ];

    /** @var array<string, string> */
    private const STATUSES = [
        'draft' => 'Черновик',
        'in_progress' => 'В работе',
        'ready_for_review' => 'На проверке',
        'active' => 'Активен',
        'ACTIVE' => 'Активна',
        'reviewed' => 'Проверено',
        'REVIEWED' => 'Проверено',
        'finalized' => 'Финализирован',
        'FINALIZED' => 'Финализирован',
        'archived' => 'В архиве',
        'ARCHIVED' => 'В архиве',
        'closed' => 'Закрыт',
        'ready' => 'Готово',
        'READY' => 'Готово',
        'pending' => 'В работе',
        'failed' => 'Ошибка',
        'revoked' => 'Отозвана',
        'REVOKED' => 'Отозвана',
        'expired' => 'Истекла',
        'PASS' => 'ОК',
        'FAIL' => 'Не ОК',
        'pass' => 'ОК',
        'fail' => 'Не ОК',
        'done' => 'Выполнено',
        'planned' => 'Запланировано',
        'blocked' => 'Заблокировано',
        'cancelled' => 'Отменено',
        'deferred' => 'Отложено',
    ];

    /** Work-entry status labels (monthly_report_work_entries.status). */
    /** @var array<string, string> */
    private const WORK_ENTRY_STATUSES = [
        'done' => 'Выполнено',
        'planned' => 'Запланировано',
        'in_progress' => 'В работе',
        'blocked' => 'Заблокировано',
        'cancelled' => 'Отменено',
        'deferred' => 'Отложено',
    ];

    /** Work-entry period_role labels (distinct from status "done"). */
    /** @var array<string, string> */
    private const WORK_ENTRY_PERIOD_ROLES = [
        'done' => 'Сделано за месяц',
        'planned_next' => 'План на следующий период',
        'risk' => 'Риск / вопрос',
        'note' => 'Заметка',
    ];

    /** Work-entry client_visibility labels. */
    /** @var array<string, string> */
    private const WORK_ENTRY_VISIBILITY = [
        'internal' => 'Внутреннее',
        'client_safe' => 'Можно использовать в отчете',
        'client_facing' => 'Показывать клиенту',
    ];

    /** Visible role labels (DB role codes unchanged). */
    /** @var array<string, string> */
    private const ROLES = [
        'admin_owner' => 'Владелец',
        'seo_lead_reviewer' => 'SEO-лид / ревьюер',
        'seo_specialist' => 'SEO-специалист',
        'account_client_manager' => 'Аккаунт-менеджер',
        'internal_viewer' => 'Внутренний просмотр',
    ];

    public static function blockKey(string $key): string
    {
        return self::BLOCK_KEYS[$key] ?? $key;
    }

    /**
     * @return array<string, string>
     */
    public static function blockKeyMap(): array
    {
        return self::BLOCK_KEYS;
    }

    public static function readinessKey(string $key): string
    {
        return self::READINESS_KEYS[$key] ?? $key;
    }

    public static function status(string $status): string
    {
        if ($status === '') {
            return '—';
        }
        if (isset(self::STATUSES[$status])) {
            return self::STATUSES[$status];
        }
        $lower = strtolower($status);
        return self::STATUSES[$lower] ?? $status;
    }

    public static function workEntryStatus(string $status): string
    {
        if ($status === '') {
            return '—';
        }
        return self::WORK_ENTRY_STATUSES[$status] ?? self::status($status);
    }

    public static function workEntryPeriodRole(string $role): string
    {
        if ($role === '') {
            return '—';
        }
        return self::WORK_ENTRY_PERIOD_ROLES[$role] ?? $role;
    }

    public static function workEntryVisibility(string $visibility): string
    {
        if ($visibility === '') {
            return '—';
        }
        return self::WORK_ENTRY_VISIBILITY[$visibility] ?? $visibility;
    }

    public static function passFail(bool $pass): string
    {
        return $pass ? 'ОК' : 'Не ОК';
    }

    public static function fixtureBadge(): string
    {
        return 'Тестовые данные';
    }

    /** Display-only demotion for draft monthly reports with 0 blocks and 0 work entries. */
    public static function emptyDraftLabel(): string
    {
        return 'Пустой черновик';
    }

    public static function emptyDraftHeading(): string
    {
        return 'Пустой черновик отчета';
    }

    public static function emptyDraftWithoutWorkLabel(): string
    {
        return 'Черновик без работ';
    }

    public static function emptyDraftMessage(): string
    {
        return 'В этом отчете пока нет работ и блоков. Добавьте работы за месяц или создайте блоки отчета.';
    }

    public static function emptyDraftPreviewExpectation(): string
    {
        return 'Предпросмотр покажет пустые разделы, пока нет работ и блоков.';
    }

    public static function emptyDraftNotReadyToFinalize(): string
    {
        return 'Отчет пока не готов к финализации.';
    }

    public static function draftClientDisclaimer(): string
    {
        return 'Черновик. Это рабочая версия, ещё не выданный клиенту файл.';
    }

    public static function displayUserName(?string $name, ?string $email = null): string
    {
        $name = trim((string) $name);
        $email = trim((string) $email);
        $name = self::decodeLiteralUnicodeEscapes($name);
        $normalized = mb_strtolower($name);
        if ($normalized === 'polygon ws local test' || $normalized === 'polygon-ws local test') {
            return 'Локальный тестовый пользователь';
        }
        if ($name !== '') {
            return $name;
        }
        return $email !== '' ? $email : 'Пользователь';
    }

    public static function role(string $role): string
    {
        if ($role === '') {
            return '—';
        }
        return self::ROLES[$role] ?? $role;
    }

    /**
     * Decode literal \uXXXX sequences sometimes stored/displayed from JSON escapes.
     * Leaves normal UTF-8 names unchanged. Does not interpret HTML.
     */
    public static function decodeLiteralUnicodeEscapes(string $value): string
    {
        if ($value === '' || !str_contains($value, '\\u')) {
            return $value;
        }
        if (preg_match('/\\\\u[0-9a-fA-F]{4}/', $value) !== 1) {
            return $value;
        }

        $decoded = preg_replace_callback(
            '/\\\\u([0-9a-fA-F]{4})/',
            static function (array $m): string {
                $code = hexdec($m[1]);
                if (function_exists('mb_chr')) {
                    $ch = mb_chr($code, 'UTF-8');
                    return is_string($ch) ? $ch : '';
                }

                return html_entity_decode('&#x' . $m[1] . ';', ENT_QUOTES | ENT_HTML5, 'UTF-8');
            },
            $value
        );

        return is_string($decoded) && $decoded !== '' ? $decoded : $value;
    }

    public static function humanizeFixtureMarker(string $text): string
    {
        $cleaned = UiTextSanitizer::stripFixtureMarkers($text);
        if ($cleaned === '') {
            return self::fixtureBadge();
        }

        return $cleaned;
    }

    /**
     * Humanize a user-visible readiness/action/eligibility message.
     * Leaves already-Russian text and unknown phrases intact when no map matches.
     */
    public static function message(?string $text): string
    {
        if ($text === null) {
            return '';
        }
        $text = trim($text);
        if ($text === '') {
            return '';
        }
        if (isset(self::MESSAGES[$text])) {
            return self::MESSAGES[$text];
        }

        if (preg_match('/^Status is "([^"]+)"\.$/', $text, $m) === 1) {
            return 'Текущий статус: «' . self::status($m[1]) . '».';
        }
        if (preg_match('/^Status must be ([a-z_]+) \(current: ([a-z_]+)\)\.$/', $text, $m) === 1) {
            return 'Нужен статус «' . self::status($m[1]) . '» (сейчас: «' . self::status($m[2]) . '»).';
        }
        if (preg_match('/^Readiness failed: (.+)$/', $text, $m) === 1) {
            $parts = array_map(
                static fn (string $k): string => self::readinessKey(trim($k)),
                explode(',', $m[1])
            );
            return 'Готовность не пройдена: ' . implode(', ', $parts);
        }
        if (preg_match('/^Render mode "([^"]+)" is valid\.$/', $text, $m) === 1) {
            return 'Режим генерации «' . $m[1] . '» допустим.';
        }
        if (preg_match('/^Render mode "([^"]+)" is not allowed for finalize/', $text, $m) === 1) {
            return 'Режим генерации «' . $m[1] . '» не подходит для финализации.';
        }
        if (preg_match('/^Render mode "([^"]+)" not allowed\.$/', $text, $m) === 1) {
            return 'Режим генерации «' . $m[1] . '» не допускается.';
        }
        if (preg_match('/^(\d+) non-archived block\(s\)\.$/', $text, $m) === 1) {
            return 'Активных блоков: ' . $m[1] . '.';
        }
        if (preg_match('/^Missing required blocks: (.+)$/', $text, $m) === 1) {
            return 'Не найдены обязательные блоки: ' . self::humanizeKeyList($m[1]);
        }
        if (preg_match('/^Missing: (.+)$/', $text, $m) === 1) {
            return 'Не найдено: ' . self::humanizeKeyList($m[1]);
        }
        if (preg_match('/^Required blocks not ready: (.+)$/', $text, $m) === 1) {
            return 'Обязательные блоки не готовы: ' . self::humanizeKeyList($m[1]);
        }
        if (preg_match('/^Blocking blocks: (.+)$/', $text, $m) === 1) {
            return 'Мешают блоки: ' . self::humanizeKeyList($m[1]);
        }
        if (preg_match('/^Blocking: (.+)$/', $text, $m) === 1) {
            return 'Мешают: ' . self::humanizeKeyList($m[1]);
        }
        if (preg_match('/^Missing weekly ids: (.+)$/', $text, $m) === 1) {
            return 'Не найдены недельные заметки: ' . $m[1];
        }

        return $text;
    }

    private static function humanizeKeyList(string $list): string
    {
        $parts = array_map('trim', explode(',', $list));
        $out = [];
        foreach ($parts as $part) {
            if ($part === '') {
                continue;
            }
            if (str_contains($part, '=')) {
                [$key, $status] = array_pad(explode('=', $part, 2), 2, '');
                $out[] = self::blockKey($key) . '=' . self::status($status);
                continue;
            }
            $out[] = self::blockKey($part);
        }
        return implode(', ', $out);
    }
}
