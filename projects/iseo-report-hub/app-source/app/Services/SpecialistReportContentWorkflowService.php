<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Support\FieldHelp;
use Iseo\Support\UiLabels;
use Throwable;

/**
 * Friendly specialist report-content workflow (Option D hybrid MVP).
 * Writes report_blocks.body and mirrors flat monthly_report_contents columns.
 * Never creates PDF/export/share/snapshot; never exposes raw block editor fields.
 */
final class SpecialistReportContentWorkflowService
{
    public const FINALIZED_READONLY_COPY = 'Отчет финализирован. Тексты доступны только для просмотра.';

    private const BODY_MAX_LEN = 20000;

    /** @var list<string> */
    public const SECTION_KEYS = [
        'executive_summary',
        'work_completed',
        'results_summary',
        'key_findings',
        'risks_and_blockers',
        'next_month_plan',
    ];

    /** @var list<string> */
    private const VIEW_ROLES = ['admin_owner', 'seo_lead_reviewer', 'seo_specialist'];

    /** @var list<string> */
    private const EDIT_ROLES = ['admin_owner', 'seo_lead_reviewer', 'seo_specialist'];

    /** @var list<string> */
    private const EDITABLE_PARENT_STATUSES = ['draft', 'in_progress', 'ready_for_review'];

    public function __construct(
        private MonthlyReportContentRepository $monthlyReports,
        private ReportBlockRepository $blocks,
        private MonthlyReportSummaryAssemblyService $assembly,
        private DatabaseService $db
    ) {
    }

    public function isAllowedSectionKey(string $sectionKey): bool
    {
        return in_array($sectionKey, self::SECTION_KEYS, true);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canView(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::VIEW_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param array<string, mixed>|null $report
     */
    public function canEdit(?array $user, ?array $report = null): bool
    {
        if (!$this->userHasAnyRole($user, self::EDIT_ROLES)) {
            return false;
        }
        if ($report === null) {
            return true;
        }
        $status = (string) ($report['status'] ?? '');
        return in_array($status, self::EDITABLE_PARENT_STATUSES, true);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, mixed>|null
     */
    public function loadPage(array $user, int $monthlyReportId): ?array
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();

        if (!$this->canView($user)) {
            return [
                'ok' => false,
                'code' => 'forbidden',
                'message' => 'Редактор текстов отчета недоступен для вашей роли.',
            ];
        }

        $report = $this->monthlyReports->findById($monthlyReportId);
        if ($report === null) {
            return null;
        }

        $status = (string) ($report['status'] ?? '');
        $editable = $this->canEdit($user, $report);
        $readOnlyReason = null;
        if ($status === 'finalized') {
            $readOnlyReason = self::FINALIZED_READONLY_COPY;
        } elseif ($status === 'archived') {
            $readOnlyReason = 'Отчет в архиве. Тексты доступны только для просмотра.';
        } elseif (!$editable) {
            $readOnlyReason = 'Редактирование текстов сейчас недоступно для статуса отчета.';
        }

        $blocksByKey = $this->indexBlocks($monthlyReportId);
        $hints = $this->buildHints($monthlyReportId);

        $sections = [];
        foreach (self::SECTION_KEYS as $key) {
            $help = FieldHelp::get(FieldHelp::keyForMonthlyField($key));
            $block = $blocksByKey[$key] ?? null;
            $flatValue = isset($report[$key]) ? (string) $report[$key] : '';
            $blockBody = is_array($block) ? (string) ($block['body'] ?? '') : '';
            $text = $blockBody !== '' ? $blockBody : $flatValue;
            $hint = $hints[$key] ?? null;

            $sections[] = [
                'key' => $key,
                'label' => UiLabels::blockKey($key),
                'helper' => is_array($help) ? (string) ($help['hint'] ?? '') : '',
                'text' => $text,
                'missing_block' => !is_array($block),
                'hint_available' => is_string($hint) && trim($hint) !== '',
                'hint_text' => is_string($hint) ? $hint : '',
            ];
        }

        return [
            'ok' => true,
            'code' => 'ok',
            'report' => $report,
            'editable' => $editable,
            'read_only_reason' => $readOnlyReason,
            'sections' => $sections,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, mixed>
     */
    public function saveSection(array $user, int $monthlyReportId, string $sectionKey, string $rawText): array
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();

        if (!$this->canView($user)) {
            return $this->fail('forbidden', 'Редактор текстов отчета недоступен для вашей роли.');
        }

        if (!$this->isAllowedSectionKey($sectionKey)) {
            return $this->fail('invalid_section', 'Недопустимый раздел отчета.');
        }

        $report = $this->monthlyReports->findById($monthlyReportId);
        if ($report === null) {
            return $this->fail('not_found', 'Месячный отчет не найден.');
        }

        if (!$this->canEdit($user, $report)) {
            $status = (string) ($report['status'] ?? '');
            if ($status === 'finalized') {
                return $this->fail('finalized', self::FINALIZED_READONLY_COPY);
            }
            if ($status === 'archived') {
                return $this->fail('archived', 'Отчет в архиве. Сохранение текстов недоступно.');
            }
            return $this->fail('locked', 'Редактирование текстов сейчас недоступно.');
        }

        $block = $this->findBlockByKey($monthlyReportId, $sectionKey);
        if ($block === null) {
            return $this->fail(
                'missing_block',
                'Раздел пока не найден в структуре отчета. Сохранение невозможно без существующего блока.'
            );
        }

        if ((string) ($block['status'] ?? '') === 'archived') {
            return $this->fail('archived_block', 'Раздел архивирован и недоступен для записи.');
        }

        $text = $this->normalizeBody($rawText);
        if (mb_strlen($text) > self::BODY_MAX_LEN) {
            return $this->fail('too_long', 'Текст раздела слишком длинный.');
        }

        $oldBody = (string) ($block['body'] ?? '');
        $oldFlat = isset($report[$sectionKey]) ? (string) $report[$sectionKey] : '';
        if ($this->normalizeBody($oldBody) === $text && $this->normalizeBody($oldFlat) === $text) {
            return [
                'ok' => true,
                'code' => 'unchanged',
                'message' => 'Текст раздела без изменений.',
                'section_key' => $sectionKey,
            ];
        }

        $pdo = $this->blocks->pdo();
        try {
            $pdo->beginTransaction();

            $fromStatus = (string) ($block['status'] ?? '');
            $this->blocks->updateBodyOnly((int) $block['id'], [
                'body' => $text,
                'status' => 'in_progress',
                'updated_by' => (int) $user['id'],
            ]);

            $this->monthlyReports->updateFlatSectionText($monthlyReportId, $sectionKey, $text, (int) $user['id']);

            $this->blocks->insertAudit('report_block.specialist_content_saved', (int) $user['id'], (int) $block['id'], [
                'monthly_report_content_id' => $monthlyReportId,
                'section_key' => $sectionKey,
                'from_status' => $fromStatus,
                'to_status' => 'in_progress',
                'old_body_sha256' => hash('sha256', $oldBody),
                'new_body_sha256' => hash('sha256', $text),
                'old_body_len' => mb_strlen($oldBody),
                'new_body_len' => mb_strlen($text),
                'flat_mirrored' => true,
            ]);

            if ($fromStatus !== 'in_progress') {
                $this->blocks->insertAudit('report_block.status_changed', (int) $user['id'], (int) $block['id'], [
                    'monthly_report_content_id' => $monthlyReportId,
                    'section_key' => $sectionKey,
                    'from_status' => $fromStatus,
                    'to_status' => 'in_progress',
                ]);
            }

            $this->monthlyReports->insertAudit('monthly_report_content.specialist_section_mirrored', (int) $user['id'], $monthlyReportId, [
                'section_key' => $sectionKey,
                'new_len' => mb_strlen($text),
            ]);

            $pdo->commit();
        } catch (Throwable) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            return $this->fail('write_failed', 'Не удалось сохранить раздел. Отчет не изменён.');
        }

        return [
            'ok' => true,
            'code' => 'saved',
            'message' => 'Раздел отчета сохранен.',
            'section_key' => $sectionKey,
        ];
    }

    /**
     * @return array<string, string|null>
     */
    private function buildHints(int $monthlyReportId): array
    {
        $out = [];
        foreach (self::SECTION_KEYS as $key) {
            $out[$key] = null;
        }

        try {
            $preview = $this->assembly->preview($monthlyReportId);
        } catch (Throwable) {
            return $out;
        }

        if ($preview === null) {
            return $out;
        }

        $applyBlocks = is_array($preview['apply_blocks'] ?? null) ? $preview['apply_blocks'] : [];
        foreach (MonthlyReportSummaryAssemblyService::WRITABLE_KEYS as $key) {
            $plan = is_array($applyBlocks[$key] ?? null) ? $applyBlocks[$key] : null;
            $body = is_array($plan) ? ($plan['body'] ?? null) : null;
            if (is_string($body) && trim($body) !== '') {
                $out[$key] = $body;
            }
        }

        $candidates = is_array($preview['candidates_key_findings'] ?? null)
            ? $preview['candidates_key_findings']
            : [];
        if ($candidates !== []) {
            $lines = [];
            foreach ($candidates as $item) {
                if (!is_array($item)) {
                    continue;
                }
                $title = trim((string) ($item['title'] ?? ''));
                if ($title === '') {
                    continue;
                }
                $lines[] = '- ' . $title;
            }
            if ($lines !== []) {
                $out['key_findings'] = "Кандидаты из работ за месяц:\n" . implode("\n", $lines);
            }
        }

        return $out;
    }

    /**
     * @return array<string, array<string, mixed>>
     */
    private function indexBlocks(int $monthlyReportId): array
    {
        $out = [];
        foreach ($this->blocks->listByMonthlyReportId($monthlyReportId) as $row) {
            $key = (string) ($row['block_key'] ?? '');
            if ($key !== '') {
                $out[$key] = $row;
            }
        }
        return $out;
    }

    /**
     * @return array<string, mixed>|null
     */
    private function findBlockByKey(int $monthlyReportId, string $sectionKey): ?array
    {
        foreach ($this->blocks->listByMonthlyReportId($monthlyReportId) as $row) {
            if ((string) ($row['block_key'] ?? '') === $sectionKey) {
                return $row;
            }
        }
        return null;
    }

    private function normalizeBody(string $body): string
    {
        $body = str_replace(["\r\n", "\r"], "\n", $body);
        return trim($body);
    }

    /**
     * @return array<string, mixed>
     */
    private function fail(string $code, string $message): array
    {
        return [
            'ok' => false,
            'code' => $code,
            'message' => $message,
            'section_key' => null,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param list<string> $roles
     */
    private function userHasAnyRole(?array $user, array $roles): bool
    {
        if ($user === null) {
            return false;
        }
        foreach ($user['roles'] as $role) {
            if (in_array($role, $roles, true)) {
                return true;
            }
        }
        return false;
    }
}
