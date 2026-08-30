<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\MonthlyReportWorkEntryRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Support\UiLabels;

/**
 * Classification of monthly work entries into client report shells.
 * Preview is SELECT-only. Apply text is generated here; writes live in MonthlyReportSummaryApplyService.
 */
final class MonthlyReportSummaryAssemblyService
{
    public const FINALIZED_APPLY_COPY = 'Отчет финализирован. Чтобы применить черновик, нужен отдельный безопасный процесс reopen/update/finalize/export.';
    public const EMPTY_RISKS_APPLY_COPY = 'Существенных рисков и блокеров на текущий момент не зафиксировано.';

    /** @var list<string> */
    public const WRITABLE_KEYS = ['work_completed', 'next_month_plan', 'risks_and_blockers'];

    /** @var list<string> */
    public const MANUAL_ONLY_KEYS = ['executive_summary', 'results_summary', 'key_findings'];

    private const CLIENT_VISIBILITIES = ['client_safe', 'client_facing'];
    private const PLAN_STATUSES = ['planned', 'in_progress', 'deferred'];
    private const DESCRIPTION_MAX = 280;

    /** @var array<string, string> */
    private const APPLY_INTROS = [
        'work_completed' => 'В течение месяца выполнены основные SEO-работы:',
        'next_month_plan' => 'В следующем периоде запланированы работы:',
        'risks_and_blockers' => 'На текущий момент требуют внимания:',
    ];

    /** @var array<string, string> */
    private const AUTO_KEYS = [
        'work_completed' => 'Что сделали',
        'next_month_plan' => 'План на следующий месяц',
        'risks_and_blockers' => 'Риски и блокеры',
    ];

    /** @var array<string, string> */
    private const EMPTY_COPY = [
        'work_completed' => 'Нет выполненных работ для клиентского раздела.',
        'next_month_plan' => 'Нет запланированных работ для следующего периода.',
        'risks_and_blockers' => 'Клиентских рисков и блокеров в работах нет.',
    ];

    public function __construct(
        private MonthlyReportWorkEntryRepository $entries,
        private MonthlyReportContentRepository $monthlyReports,
        private ReportBlockRepository $blocks,
        private DatabaseService $db
    ) {
    }

    /**
     * @return array<string, mixed>|null
     */
    public function preview(int $monthlyReportId): ?array
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();

        $monthly = $this->monthlyReports->findById($monthlyReportId);
        if ($monthly === null) {
            return null;
        }

        $entries = $this->entries->listByMonthlyReportId($monthlyReportId);
        $classified = $this->classify($entries);
        $existingBlocks = $this->indexExistingBlocks($monthlyReportId);

        $applyBlocks = $this->buildApplyBlocks($classified['drafts'], $existingBlocks);
        $status = (string) ($monthly['status'] ?? '');

        return [
            'monthly' => $monthly,
            'stats' => $classified['stats'],
            'drafts' => $classified['drafts'],
            'manual' => $classified['manual'],
            'candidates_key_findings' => $classified['candidates_key_findings'],
            'excluded' => $classified['excluded'],
            'existing_blocks' => $existingBlocks,
            'apply_blocks' => $applyBlocks,
            'warnings' => $this->warnings($monthly, $classified['stats']),
            'parent_finalized' => $status === 'finalized',
            'parent_archived' => $status === 'archived',
        ];
    }

    /**
     * @return array<string, mixed>|null
     */
    public function buildApplyPayload(int $monthlyReportId): ?array
    {
        $preview = $this->preview($monthlyReportId);
        if ($preview === null) {
            return null;
        }

        return [
            'monthly' => $preview['monthly'],
            'blocks' => $preview['apply_blocks'],
            'parent_status' => (string) ($preview['monthly']['status'] ?? ''),
            'finalized' => !empty($preview['parent_finalized']),
            'archived' => !empty($preview['parent_archived']),
        ];
    }

    /**
     * Client-facing plain text for one auto block. Null means not writable.
     *
     * @param list<array<string, mixed>> $items
     */
    public function formatBlockBody(string $blockKey, array $items): ?string
    {
        if (!in_array($blockKey, self::WRITABLE_KEYS, true)) {
            return null;
        }

        $bullets = [];
        foreach ($items as $item) {
            if (!is_array($item)) {
                continue;
            }
            $line = $this->applyBulletText($item);
            if ($line !== '') {
                $bullets[] = '- ' . $line;
            }
        }

        if ($bullets === []) {
            if ($blockKey === 'risks_and_blockers') {
                return self::EMPTY_RISKS_APPLY_COPY;
            }
            return null;
        }

        $intro = self::APPLY_INTROS[$blockKey] ?? '';
        if ($intro === '') {
            return null;
        }

        return $intro . "\n\n" . implode("\n", $bullets);
    }

    /**
     * @param list<array<string, mixed>> $items
     */
    public function formatApplyBody(string $blockKey, array $items): ?string
    {
        return $this->formatBlockBody($blockKey, $items);
    }

    /**
     * @param list<array<string, mixed>> $entries
     * @return array{
     *   stats: array<string, int>,
     *   drafts: array<string, array<string, mixed>>,
     *   manual: array<string, array<string, mixed>>,
     *   candidates_key_findings: list<array<string, mixed>>,
     *   excluded: list<array<string, mixed>>
     * }
     */
    private function classify(array $entries): array
    {
        $draftItems = [
            'work_completed' => [],
            'next_month_plan' => [],
            'risks_and_blockers' => [],
        ];
        $candidates = [];
        $excluded = [];
        $excludedInternal = 0;
        $excludedCancelled = 0;
        $unassigned = 0;
        $emptyTitle = 0;

        foreach ($entries as $entry) {
            $status = (string) ($entry['status'] ?? '');
            $role = (string) ($entry['period_role'] ?? '');
            $visibility = (string) ($entry['client_visibility'] ?? '');
            $title = trim((string) ($entry['title'] ?? ''));

            if ($status === 'cancelled') {
                $excluded[] = $this->excludedRow($entry, 'cancelled');
                $excludedCancelled++;
                continue;
            }

            if ($visibility === 'internal') {
                $excluded[] = $this->excludedRow($entry, 'internal');
                $excludedInternal++;
                continue;
            }

            if ($title === '') {
                $excluded[] = $this->excludedRow($entry, 'empty_title');
                $emptyTitle++;
                continue;
            }

            $item = $this->draftItem($entry);
            $assigned = null;

            if ($role === 'risk' || $status === 'blocked') {
                $assigned = 'risks_and_blockers';
            } elseif ($role === 'done' && $status === 'done' && $this->isClientUsable($visibility)) {
                $assigned = 'work_completed';
            } elseif (
                $role === 'planned_next'
                && in_array($status, self::PLAN_STATUSES, true)
                && $this->isClientUsable($visibility)
            ) {
                $assigned = 'next_month_plan';
            }

            if ($assigned !== null) {
                $draftItems[$assigned][] = $item;
                continue;
            }

            if ($role === 'note' && $this->isClientUsable($visibility)) {
                $candidates[] = $item;
            }

            $excluded[] = $this->excludedRow($entry, 'no_matching_rule');
            $unassigned++;
        }

        $drafts = [];
        foreach (self::AUTO_KEYS as $key => $titleRu) {
            $items = $draftItems[$key];
            $sourceIds = [];
            foreach ($items as $item) {
                $sourceIds[] = (int) $item['id'];
            }
            $drafts[$key] = [
                'key' => $key,
                'title_ru' => $titleRu,
                'items' => $items,
                'groups' => $this->groupItems($items),
                'source_entry_ids' => $sourceIds,
                'count' => count($items),
                'empty' => $items === [],
                'empty_copy' => self::EMPTY_COPY[$key],
                'manual_required' => false,
            ];
        }

        $included = $drafts['work_completed']['count']
            + $drafts['next_month_plan']['count']
            + $drafts['risks_and_blockers']['count'];

        $manualCopy = 'Требуется ручная редактура. В этой версии система только показывает кандидаты, но не генерирует финальный текст.';
        $manual = [
            'executive_summary' => [
                'key' => 'executive_summary',
                'title_ru' => UiLabels::blockKey('executive_summary'),
                'manual_required' => true,
                'copy' => $manualCopy,
            ],
            'results_summary' => [
                'key' => 'results_summary',
                'title_ru' => UiLabels::blockKey('results_summary'),
                'manual_required' => true,
                'copy' => $manualCopy,
            ],
            'key_findings' => [
                'key' => 'key_findings',
                'title_ru' => UiLabels::blockKey('key_findings'),
                'manual_required' => true,
                'copy' => $manualCopy,
            ],
        ];

        return [
            'stats' => [
                'total' => count($entries),
                'included' => $included,
                'work_completed' => $drafts['work_completed']['count'],
                'next_month_plan' => $drafts['next_month_plan']['count'],
                'risks_and_blockers' => $drafts['risks_and_blockers']['count'],
                'excluded' => count($excluded),
                'excluded_internal' => $excludedInternal,
                'excluded_cancelled' => $excludedCancelled,
                'unassigned' => $unassigned,
                'empty_title' => $emptyTitle,
                'key_findings_candidates' => count($candidates),
            ],
            'drafts' => $drafts,
            'manual' => $manual,
            'candidates_key_findings' => $candidates,
            'excluded' => $excluded,
        ];
    }

    /**
     * @param array<string, mixed> $entry
     * @return array<string, mixed>
     */
    private function draftItem(array $entry): array
    {
        return [
            'id' => (int) ($entry['id'] ?? 0),
            'title' => (string) ($entry['title'] ?? ''),
            'text' => $this->clientLineText($entry),
            'category_name' => trim((string) ($entry['category_name'] ?? '')),
            'sort_order' => (int) ($entry['sort_order'] ?? 0),
            'status' => (string) ($entry['status'] ?? ''),
            'period_role' => (string) ($entry['period_role'] ?? ''),
            'client_visibility' => (string) ($entry['client_visibility'] ?? ''),
        ];
    }

    /**
     * @param array<string, mixed> $entry
     * @return array<string, mixed>
     */
    private function excludedRow(array $entry, string $reason): array
    {
        return [
            'id' => (int) ($entry['id'] ?? 0),
            'title' => (string) ($entry['title'] ?? ''),
            'reason' => $reason,
        ];
    }

    /**
     * @param array<string, mixed> $entry
     */
    private function clientLineText(array $entry): string
    {
        $summary = trim((string) ($entry['client_summary'] ?? ''));
        if ($summary !== '') {
            return $summary;
        }

        $title = trim((string) ($entry['title'] ?? ''));
        $description = trim((string) ($entry['description'] ?? ''));
        if ($description === '') {
            return $title;
        }

        if (mb_strlen($description) > self::DESCRIPTION_MAX) {
            $description = mb_substr($description, 0, self::DESCRIPTION_MAX) . '…';
        }

        if ($title === '') {
            return $description;
        }

        return $title . ' — ' . $description;
    }

    /**
     * @param array<string, mixed> $item
     */
    private function applyBulletText(array $item): string
    {
        $raw = trim((string) ($item['text'] ?? ''));
        if ($raw === '') {
            $raw = $this->clientLineText($item);
        }
        $raw = $this->normalizeClientLine($raw);
        if ($raw === '') {
            return '';
        }
        if (!preg_match('/[.!?]$/u', $raw)) {
            $raw .= '.';
        }
        return $raw;
    }

    private function normalizeClientLine(string $text): string
    {
        $text = str_replace(["\r\n", "\r", "\n"], ' ', $text);
        $text = preg_replace('/\s+/u', ' ', $text) ?? $text;
        return trim($text);
    }

    /**
     * @param array<string, array<string, mixed>> $drafts
     * @param array<string, array<string, mixed>> $existingBlocks
     * @return array<string, array<string, mixed>>
     */
    private function buildApplyBlocks(array $drafts, array $existingBlocks): array
    {
        $out = [];
        foreach (self::AUTO_KEYS as $key => $titleRu) {
            $draft = $drafts[$key] ?? ['items' => [], 'source_entry_ids' => [], 'empty' => true];
            $items = is_array($draft['items'] ?? null) ? $draft['items'] : [];
            $body = $this->formatBlockBody($key, $items);
            $existing = $existingBlocks[$key] ?? null;
            $found = is_array($existing);
            $status = $found ? (string) ($existing['status'] ?? '') : '';
            $currentBody = $found ? (string) ($existing['body'] ?? '') : '';
            $currentSummary = $found ? (string) ($existing['summary'] ?? '') : '';
            $identical = $body !== null && $this->normalizeBodyCompare($body) === $this->normalizeBodyCompare($currentBody);
            $writable = $body !== null && $found && $status !== 'archived';

            $out[$key] = [
                'key' => $key,
                'title_ru' => $titleRu,
                'body' => $body,
                'writable' => $writable,
                'empty' => !empty($draft['empty']),
                'source_entry_ids' => is_array($draft['source_entry_ids'] ?? null) ? $draft['source_entry_ids'] : [],
                'block_found' => $found,
                'block_id' => $found ? (int) ($existing['id'] ?? 0) : null,
                'block_status' => $found ? $status : null,
                'current_body' => $found ? $currentBody : null,
                'current_summary' => $found ? $currentSummary : null,
                'current_body_empty' => !$found || trim($currentBody) === '',
                'identical' => $identical,
                'overwrite' => $found && trim($currentBody) !== '' && $body !== null && !$identical,
            ];
        }

        return $out;
    }

    private function normalizeBodyCompare(string $body): string
    {
        $body = str_replace(["\r\n", "\r"], "\n", $body);
        return trim($body);
    }

    private function isClientUsable(string $visibility): bool
    {
        return in_array($visibility, self::CLIENT_VISIBILITIES, true);
    }

    /**
     * @param list<array<string, mixed>> $items
     * @return list<array{category_name:string,items:list<array<string, mixed>>}>
     */
    private function groupItems(array $items): array
    {
        $groups = [];
        foreach ($items as $item) {
            $name = trim((string) ($item['category_name'] ?? ''));
            if ($name === '') {
                $name = 'Без категории';
            }
            if (!isset($groups[$name])) {
                $groups[$name] = [
                    'category_name' => $name,
                    'min_sort' => (int) ($item['sort_order'] ?? 0),
                    'items' => [],
                ];
            }
            $groups[$name]['items'][] = $item;
            $sort = (int) ($item['sort_order'] ?? 0);
            if ($sort < $groups[$name]['min_sort']) {
                $groups[$name]['min_sort'] = $sort;
            }
        }

        $list = array_values($groups);
        usort($list, static function (array $a, array $b): int {
            if ($a['min_sort'] !== $b['min_sort']) {
                return $a['min_sort'] <=> $b['min_sort'];
            }
            return strcmp((string) $a['category_name'], (string) $b['category_name']);
        });

        $out = [];
        foreach ($list as $group) {
            $out[] = [
                'category_name' => (string) $group['category_name'],
                'items' => $group['items'],
            ];
        }

        return $out;
    }

    /**
     * @return array<string, array<string, mixed>>
     */
    private function indexExistingBlocks(int $monthlyReportId): array
    {
        $rows = $this->blocks->listByMonthlyReportId($monthlyReportId);
        $out = [];
        foreach ($rows as $row) {
            $key = (string) ($row['block_key'] ?? '');
            if ($key === '') {
                continue;
            }
            $out[$key] = [
                'id' => (int) ($row['id'] ?? 0),
                'block_key' => $key,
                'title' => (string) ($row['title'] ?? ''),
                'summary' => (string) ($row['summary'] ?? ''),
                'body' => (string) ($row['body'] ?? ''),
                'status' => (string) ($row['status'] ?? ''),
                'data_json' => $row['data_json'] ?? null,
                'reviewed_at' => $row['reviewed_at'] ?? null,
                'approved_at' => $row['approved_at'] ?? null,
            ];
        }

        return $out;
    }

    /**
     * @param array<string, mixed> $monthly
     * @param array<string, int> $stats
     * @return list<string>
     */
    private function warnings(array $monthly, array $stats): array
    {
        $warnings = [
            'Это предварительная сборка. Она не меняет отчет, PDF, снимки и ссылки.',
        ];
        if ((string) ($monthly['status'] ?? '') === 'finalized') {
            $warnings[] = 'Месячный отчет уже финализирован. Применение черновика будет возможно только отдельным безопасным шагом.';
        }
        if ($stats['total'] === 0) {
            $warnings[] = 'Работ за месяц пока нет. Добавьте работы, затем откройте черновик снова.';
        }

        return $warnings;
    }
}
