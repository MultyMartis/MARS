<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\MonthlyReportWorkEntryRepository;
use Iseo\Repositories\SeoWorkCategoryRepository;
use Iseo\Repositories\SeoWorkItemRepository;

/**
 * Thin validation + persistence for monthly report work entries.
 * No physical delete; no catalogue / block / export mutation.
 */
final class MonthlyReportWorkEntryService
{
    /** @var list<string> */
    public const STATUSES = [
        'planned',
        'in_progress',
        'done',
        'blocked',
        'cancelled',
        'deferred',
    ];

    /** @var list<string> */
    public const PERIOD_ROLES = [
        'done',
        'planned_next',
        'risk',
        'note',
    ];

    /** @var list<string> */
    public const VISIBILITIES = [
        'internal',
        'client_safe',
        'client_facing',
    ];

    private const TITLE_MAX = 240;
    private const SORT_DEFAULT = 100;
    private const SORT_MIN = -999999;
    private const SORT_MAX = 999999;

    public function __construct(
        private MonthlyReportWorkEntryRepository $entries,
        private MonthlyReportContentRepository $monthlyReports,
        private SeoWorkCategoryRepository $categories,
        private SeoWorkItemRepository $items,
        private DatabaseService $db
    ) {
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getMonthlyReport(int $id): ?array
    {
        return $this->monthlyReports->findById($id);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getEntry(int $id): ?array
    {
        return $this->entries->findById($id);
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function activeCategories(): array
    {
        return $this->categories->listActive();
    }

    /**
     * Active items for forms; optionally keep current inactive item visible on edit.
     *
     * @return list<array<string, mixed>>
     */
    public function selectableWorkItems(?int $currentWorkItemId = null): array
    {
        $rows = $this->items->listActive();
        if ($currentWorkItemId === null || $currentWorkItemId <= 0) {
            return $rows;
        }

        foreach ($rows as $row) {
            if ((int) ($row['id'] ?? 0) === $currentWorkItemId) {
                return $rows;
            }
        }

        $current = $this->items->findById($currentWorkItemId);
        if ($current === null) {
            return $rows;
        }

        array_unshift($rows, $current);
        return $rows;
    }

    /**
     * Specialist may mutate work entries only while monthly report is not finalized.
     * Admin/lead retain access on finalized reports for recovery edits.
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $monthly
     */
    public function canMutateWorkEntries(array $user, array $monthly): bool
    {
        $roles = $user['roles'] ?? [];
        if (!is_array($roles)) {
            return false;
        }
        $isPrivileged = in_array('admin_owner', $roles, true)
            || in_array('seo_lead_reviewer', $roles, true);
        if ($isPrivileged) {
            return true;
        }
        if (!in_array('seo_specialist', $roles, true)) {
            return false;
        }

        return (string) ($monthly['status'] ?? '') !== 'finalized';
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $input
     * @return array{ok:bool,id?:int,errors?:array<string,string>,message?:string,warning?:string}
     */
    public function create(array $user, array $monthly, array $input): array
    {
        if (!$this->canMutateWorkEntries($user, $monthly)) {
            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Отчет финализирован. Для SEO-специалиста он открыт только для просмотра.',
            ];
        }

        $validated = $this->validatePayload($input, null);
        if ($validated['errors'] !== []) {
            return [
                'ok' => false,
                'errors' => $validated['errors'],
                'message' => 'Исправьте ошибки в форме.',
            ];
        }

        $row = $validated['row'];
        $row['monthly_report_id'] = (int) $monthly['id'];
        $row['created_by_user_id'] = isset($user['id']) ? (int) $user['id'] : null;
        $row['updated_by_user_id'] = $row['created_by_user_id'];

        $id = $this->entries->create($row);
        $result = ['ok' => true, 'id' => $id];
        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            $result['warning'] = 'Месячный отчет уже финализирован. Изменения в работах не пересобирают PDF и снимки автоматически.';
        }

        return $result;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $monthly
     * @param array<string, mixed> $input
     * @return array{ok:bool,errors?:array<string,string>,message?:string,warning?:string}
     */
    public function update(array $user, array $existing, array $monthly, array $input): array
    {
        if (!$this->canMutateWorkEntries($user, $monthly)) {
            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Отчет финализирован. Для SEO-специалиста он открыт только для просмотра.',
            ];
        }

        $validated = $this->validatePayload($input, $existing);
        if ($validated['errors'] !== []) {
            return [
                'ok' => false,
                'errors' => $validated['errors'],
                'message' => 'Исправьте ошибки в форме.',
            ];
        }

        $row = $validated['row'];
        $row['updated_by_user_id'] = isset($user['id']) ? (int) $user['id'] : null;

        $this->entries->update((int) $existing['id'], $row);
        $result = ['ok' => true];
        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            $result['warning'] = 'Месячный отчет уже финализирован. Изменения в работах не пересобирают PDF и снимки автоматически.';
        }

        return $result;
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{
     *   errors:array<string,string>,
     *   row:array{
     *     work_item_id:?int,
     *     category_id:?int,
     *     title:string,
     *     description:?string,
     *     status:string,
     *     period_role:string,
     *     client_visibility:string,
     *     client_summary:?string,
     *     internal_note:?string,
     *     evidence_note:?string,
     *     sort_order:int
     *   }
     * }
     */
    private function validatePayload(array $input, ?array $existing): array
    {
        $errors = [];

        $workItemId = $this->parseOptionalId($input['work_item_id'] ?? '');
        $categoryId = $this->parseOptionalId($input['category_id'] ?? '');
        $title = trim((string) ($input['title'] ?? ''));
        $description = $this->nullableText($input['description'] ?? null);
        $status = trim((string) ($input['status'] ?? ''));
        $periodRole = trim((string) ($input['period_role'] ?? ''));
        $visibility = trim((string) ($input['client_visibility'] ?? ''));
        $clientSummary = $this->nullableText($input['client_summary'] ?? null);
        $internalNote = $this->nullableText($input['internal_note'] ?? null);
        $evidenceNote = $this->nullableText($input['evidence_note'] ?? null);
        $sortOrder = $this->parseSortOrder($input['sort_order'] ?? null, $errors);

        $workItem = null;
        if ($workItemId !== null) {
            $workItem = $this->items->findById($workItemId);
            $existingItemId = $existing !== null ? (int) ($existing['work_item_id'] ?? 0) : 0;
            $allowInactiveCurrent = $existingItemId > 0 && $existingItemId === $workItemId;
            if ($workItem === null || ((int) ($workItem['is_active'] ?? 0) !== 1 && !$allowInactiveCurrent)) {
                $errors['work_item_id'] = 'Работа каталога не найдена или неактивна.';
                $workItemId = null;
                $workItem = null;
            }
        }

        if ($workItem !== null) {
            $categoryId = (int) $workItem['category_id'];
            if ($title === '') {
                $title = trim((string) ($workItem['name'] ?? ''));
            }
        } elseif ($categoryId !== null) {
            $category = $this->categories->findById($categoryId);
            if ($category === null || (int) ($category['is_active'] ?? 0) !== 1) {
                $errors['category_id'] = 'Категория не найдена или неактивна.';
                $categoryId = null;
            }
        }

        if ($title === '') {
            $errors['title'] = 'Укажите название работы.';
        } elseif (mb_strlen($title) > self::TITLE_MAX) {
            $errors['title'] = 'Название не длиннее 240 символов.';
        }

        if (!in_array($status, self::STATUSES, true)) {
            $errors['status'] = 'Выберите допустимый статус.';
        }

        if (!in_array($periodRole, self::PERIOD_ROLES, true)) {
            $errors['period_role'] = 'Выберите роль в периоде.';
        }

        if (!in_array($visibility, self::VISIBILITIES, true)) {
            $errors['client_visibility'] = 'Выберите видимость.';
        }

        return [
            'errors' => $errors,
            'row' => [
                'work_item_id' => $workItemId,
                'category_id' => $categoryId,
                'title' => $title,
                'description' => $description,
                'status' => $status,
                'period_role' => $periodRole,
                'client_visibility' => $visibility,
                'client_summary' => $clientSummary,
                'internal_note' => $internalNote,
                'evidence_note' => $evidenceNote,
                'sort_order' => $sortOrder,
            ],
        ];
    }

    private function parseOptionalId(mixed $raw): ?int
    {
        if ($raw === null || $raw === '') {
            return null;
        }
        if (!is_numeric($raw)) {
            return null;
        }
        $id = (int) $raw;
        return $id > 0 ? $id : null;
    }

    private function nullableText(mixed $raw): ?string
    {
        $text = trim((string) ($raw ?? ''));
        return $text === '' ? null : $text;
    }

    /**
     * @param array<string, string> $errors
     */
    private function parseSortOrder(mixed $raw, array &$errors): int
    {
        if ($raw === null || $raw === '') {
            return self::SORT_DEFAULT;
        }

        if (!is_numeric($raw) || (string) (int) $raw !== trim((string) $raw)) {
            $errors['sort_order'] = 'Порядок должен быть целым числом.';
            return self::SORT_DEFAULT;
        }

        $value = (int) $raw;
        if ($value < self::SORT_MIN || $value > self::SORT_MAX) {
            $errors['sort_order'] = 'Порядок должен быть целым числом.';
            return self::SORT_DEFAULT;
        }

        return $value;
    }
}
