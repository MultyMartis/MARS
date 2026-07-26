<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportPreviewRepository;
use Throwable;

/**
 * Read-only monthly report preview composition.
 */
final class ReportPreviewService
{
    /** @var list<string> */
    public const FLAT_FIELD_KEYS = [
        'executive_summary',
        'work_completed',
        'results_summary',
        'key_findings',
        'risks_and_blockers',
        'next_month_plan',
        'client_notes',
        'internal_notes',
    ];

    /** @var list<string> */
    private const READ_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    public function __construct(
        private ReportPreviewRepository $repo,
        private DatabaseService $db
    ) {
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canPreview(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::READ_ROLES);
    }

    /**
     * Assemble preview payload (SELECT-only). Returns null if monthly report missing.
     *
     * @return array{
     *   report: array<string, mixed>,
     *   blocks: list<array<string, mixed>>,
     *   render_mode: string,
     *   flat_fields: array<string, string>,
     *   flat_present: bool,
     *   source_weekly: list<array<string, mixed>>,
     *   diagnostics: array<string, mixed>,
     *   generated_at: string
     * }|null
     */
    public function assemble(int $monthlyReportId): ?array
    {
        $this->assertDb();

        $report = $this->repo->findMonthlyWithContext($monthlyReportId);
        if ($report === null) {
            return null;
        }

        $periodId = (int) ($report['reporting_period_id'] ?? 0);
        if ($periodId <= 0 || (string) ($report['period_key'] ?? '') === '') {
            return null;
        }

        $allBlocks = $this->repo->listBlocksByMonthlyReportId($monthlyReportId);
        $blocks = [];
        $archivedExcluded = 0;
        foreach ($allBlocks as $block) {
            if ((string) ($block['status'] ?? '') === 'archived') {
                $archivedExcluded++;
                continue;
            }
            $blocks[] = $block;
        }

        $flatFields = [];
        $flatPresent = false;
        foreach (self::FLAT_FIELD_KEYS as $key) {
            $value = trim((string) ($report[$key] ?? ''));
            $flatFields[$key] = $value;
            if ($value !== '') {
                $flatPresent = true;
            }
        }

        if ($blocks !== []) {
            $renderMode = 'blocks_primary';
        } elseif ($flatPresent) {
            $renderMode = 'flat_fallback';
        } else {
            $renderMode = 'empty';
        }

        $monthlySourceIds = $this->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);
        $available = $this->repo->listWeeklyCheckpointsForPeriod($periodId);
        $byId = [];
        foreach ($available as $row) {
            $byId[(int) $row['id']] = $row;
        }

        $sourceWeekly = [];
        $missingWeeklyIds = [];
        foreach ($monthlySourceIds as $id) {
            if (isset($byId[$id])) {
                $sourceWeekly[] = $byId[$id];
            } else {
                $missingWeeklyIds[] = $id;
            }
        }

        foreach ($blocks as &$block) {
            $blockIds = $this->decodeSourceIds($block['source_weekly_checkpoint_ids'] ?? null);
            $block['_source_ids'] = $blockIds;
            $block['_source_rows'] = [];
            foreach ($blockIds as $bid) {
                if (isset($byId[$bid])) {
                    $block['_source_rows'][] = $byId[$bid];
                }
            }
            $block['_has_metric_refs'] = $this->jsonFieldNonEmpty($block['source_metric_refs'] ?? null);
            $block['_has_data_json'] = $this->jsonFieldNonEmpty($block['data_json'] ?? null);
        }
        unset($block);

        $metricRefsPresent = false;
        foreach ($blocks as $block) {
            if (!empty($block['_has_metric_refs'])) {
                $metricRefsPresent = true;
                break;
            }
        }

        $generatedAt = date('Y-m-d H:i:s T');

        return [
            'report' => $report,
            'blocks' => $blocks,
            'render_mode' => $renderMode,
            'flat_fields' => $flatFields,
            'flat_present' => $flatPresent,
            'source_weekly' => $sourceWeekly,
            'diagnostics' => [
                'render_mode' => $renderMode,
                'block_count' => count($blocks),
                'archived_excluded_count' => $archivedExcluded,
                'flat_fallback_available' => $flatPresent,
                'flat_fallback_active' => $renderMode === 'flat_fallback',
                'source_weekly_ids' => $monthlySourceIds,
                'missing_weekly_ids' => $missingWeeklyIds,
                'metric_refs_present' => $metricRefsPresent,
                'generated_at' => $generatedAt,
            ],
            'generated_at' => $generatedAt,
        ];
    }

    /**
     * Escape HTML then preserve newlines as <br>.
     */
    public static function safeMultiline(?string $text): string
    {
        $raw = (string) ($text ?? '');
        if ($raw === '') {
            return '';
        }

        return nl2br(e($raw), false);
    }

    /**
     * @return list<int>
     */
    public function decodeSourceIds(mixed $raw): array
    {
        if ($raw === null || $raw === '') {
            return [];
        }

        if (is_array($raw)) {
            $out = [];
            foreach ($raw as $v) {
                $id = (int) $v;
                if ($id > 0) {
                    $out[] = $id;
                }
            }
            return array_values(array_unique($out));
        }

        if (!is_string($raw)) {
            return [];
        }

        $decoded = json_decode($raw, true);
        if (!is_array($decoded)) {
            return [];
        }

        $out = [];
        foreach ($decoded as $v) {
            $id = (int) $v;
            if ($id > 0) {
                $out[] = $id;
            }
        }
        return array_values(array_unique($out));
    }

    private function jsonFieldNonEmpty(mixed $raw): bool
    {
        if ($raw === null || $raw === '') {
            return false;
        }
        if (is_string($raw)) {
            $trim = trim($raw);
            return $trim !== '' && $trim !== 'null' && $trim !== '[]' && $trim !== '{}';
        }
        if (is_array($raw)) {
            return $raw !== [];
        }
        return true;
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

    private function assertDb(): void
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        try {
            $this->db->connect();
        } catch (Throwable $e) {
            throw new \RuntimeException('Database connection failed.', 0, $e);
        }
    }
}
