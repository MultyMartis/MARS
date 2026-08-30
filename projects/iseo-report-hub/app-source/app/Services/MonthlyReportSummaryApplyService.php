<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use JsonException;
use Throwable;

/**
 * Selected-block apply of assembly draft text into report_blocks.body.
 * Never mutates work entries, snapshots, exports, shares, or PDFs.
 * Finalized/archived parents are refused before any UPDATE.
 */
final class MonthlyReportSummaryApplyService
{
    private const APPLY_ROLES = ['admin_owner', 'seo_lead_reviewer'];
    private const BODY_MAX_LEN = 50000;

    public function __construct(
        private MonthlyReportSummaryAssemblyService $assembly,
        private MonthlyReportContentRepository $monthlyReports,
        private ReportBlockRepository $blocks,
        private DatabaseService $db
    ) {
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canApply(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::APPLY_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param list<mixed> $selectedKeys
     * @return array<string, mixed>
     */
    public function apply(array $user, int $monthlyReportId, array $selectedKeys, bool $confirmed): array
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();

        if (!$this->canApply($user)) {
            return $this->fail('forbidden', 'Применение черновика доступно руководителю или владельцу.', [], $selectedKeys);
        }

        $monthly = $this->monthlyReports->findById($monthlyReportId);
        if ($monthly === null) {
            return $this->fail('not_found', 'Месячный отчет не найден.', [], $selectedKeys);
        }

        $status = (string) ($monthly['status'] ?? '');
        if ($status === 'finalized' || $status === 'archived') {
            return $this->fail(
                $status === 'archived' ? 'archived' : 'finalized',
                MonthlyReportSummaryAssemblyService::FINALIZED_APPLY_COPY,
                [],
                $selectedKeys
            );
        }

        if ($this->hasActiveShare($monthlyReportId)) {
            return $this->fail(
                'active_share',
                'У отчета есть активная публичная ссылка. Применение черновика заблокировано.',
                [],
                $selectedKeys
            );
        }

        if (!$confirmed) {
            return $this->fail('confirm', 'Подтвердите перезапись выбранных блоков.', [], $selectedKeys);
        }

        $normalized = $this->normalizeSelectedKeys($selectedKeys);
        if ($normalized['forbidden'] !== []) {
            return $this->fail(
                'forbidden_key',
                'Этот раздел нельзя заполнить автосборкой.',
                $normalized['rejected'],
                $normalized['selected']
            );
        }
        if ($normalized['selected'] === []) {
            return $this->fail('empty_selection', 'Выберите хотя бы один раздел.', [], []);
        }

        $payload = $this->assembly->buildApplyPayload($monthlyReportId);
        if ($payload === null) {
            return $this->fail('not_found', 'Месячный отчет не найден.', [], $normalized['selected']);
        }

        $applyBlocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
        $existingRows = $this->indexBlocks($monthlyReportId);

        $updated = [];
        $skipped = [];
        $rejected = [];
        $previous = [];
        $newBodies = [];
        $writes = [];

        foreach ($normalized['selected'] as $key) {
            $plan = is_array($applyBlocks[$key] ?? null) ? $applyBlocks[$key] : null;
            $row = $existingRows[$key] ?? null;

            if ($plan === null) {
                $rejected[] = ['key' => $key, 'reason' => 'unknown_key'];
                continue;
            }

            $body = $plan['body'] ?? null;
            if (!is_string($body) || $body === '') {
                $skipped[] = ['key' => $key, 'reason' => 'empty_draft'];
                continue;
            }
            if (mb_strlen($body) > self::BODY_MAX_LEN) {
                $rejected[] = ['key' => $key, 'reason' => 'body_too_long'];
                continue;
            }
            if (!is_array($row)) {
                $skipped[] = ['key' => $key, 'reason' => 'missing_block'];
                continue;
            }
            if ((string) ($row['status'] ?? '') === 'archived') {
                $rejected[] = ['key' => $key, 'reason' => 'archived_block'];
                continue;
            }

            $oldBody = (string) ($row['body'] ?? '');
            if ($this->normalizeBody($body) === $this->normalizeBody($oldBody)) {
                $skipped[] = ['key' => $key, 'reason' => 'unchanged'];
                continue;
            }

            $fromStatus = (string) ($row['status'] ?? '');
            $sourceIds = is_array($plan['source_entry_ids'] ?? null) ? $plan['source_entry_ids'] : [];
            $dataJson = $this->mergeProvenance($row['data_json'] ?? null, [
                'assembly_applied_at' => date('c'),
                'assembly_source_entry_ids' => $sourceIds,
                'assembly_previous_body_sha256' => hash('sha256', $oldBody),
            ]);

            $writes[] = [
                'key' => $key,
                'id' => (int) $row['id'],
                'from_status' => $fromStatus,
                'old_body' => $oldBody,
                'new_body' => $body,
                'source_entry_ids' => $sourceIds,
                'data_json' => $dataJson,
            ];
        }

        if ($writes === []) {
            $message = $this->skipOnlyMessage($skipped, $rejected);
            return [
                'ok' => true,
                'code' => 'nothing_written',
                'message' => $message,
                'warn_message' => null,
                'selected' => $normalized['selected'],
                'updated' => [],
                'skipped' => $skipped,
                'rejected' => $rejected,
                'previous' => [],
                'new' => [],
            ];
        }

        $pdo = $this->blocks->pdo();
        try {
            $pdo->beginTransaction();
            foreach ($writes as $write) {
                $this->blocks->updateAssemblyApply((int) $write['id'], [
                    'body' => (string) $write['new_body'],
                    'status' => 'in_progress',
                    'updated_by' => (int) $user['id'],
                    'reviewed_at' => null,
                    'approved_at' => null,
                    ...($write['data_json'] !== null ? ['data_json' => $write['data_json']] : []),
                ]);

                $oldBody = (string) $write['old_body'];
                $newBody = (string) $write['new_body'];
                $this->blocks->insertAudit('report_block.assembly_applied', (int) $user['id'], (int) $write['id'], [
                    'monthly_report_content_id' => $monthlyReportId,
                    'block_key' => $write['key'],
                    'from_status' => $write['from_status'],
                    'to_status' => 'in_progress',
                    'old_body_sha256' => hash('sha256', $oldBody),
                    'new_body_sha256' => hash('sha256', $newBody),
                    'old_body_len' => mb_strlen($oldBody),
                    'new_body_len' => mb_strlen($newBody),
                    'source_entry_ids' => $write['source_entry_ids'],
                ]);
                if ((string) $write['from_status'] !== 'in_progress') {
                    $this->blocks->insertAudit('report_block.status_changed', (int) $user['id'], (int) $write['id'], [
                        'monthly_report_content_id' => $monthlyReportId,
                        'block_key' => $write['key'],
                        'from_status' => $write['from_status'],
                        'to_status' => 'in_progress',
                    ]);
                }

                $updated[] = ['key' => $write['key'], 'id' => (int) $write['id']];
                $previous[$write['key']] = $oldBody;
                $newBodies[$write['key']] = $newBody;
            }
            $pdo->commit();
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            return $this->fail('write_failed', 'Не удалось записать черновик. Отчет не изменён.', $rejected, $normalized['selected']);
        }

        $labels = [];
        foreach ($updated as $row) {
            $labels[] = $this->labelForKey((string) $row['key']);
        }

        $warn = null;
        if ($skipped !== []) {
            $warn = 'Пустой черновик раздела не записан.';
            $hasUnchanged = false;
            $hasEmpty = false;
            foreach ($skipped as $skip) {
                if (($skip['reason'] ?? '') === 'unchanged') {
                    $hasUnchanged = true;
                }
                if (($skip['reason'] ?? '') === 'empty_draft' || ($skip['reason'] ?? '') === 'missing_block') {
                    $hasEmpty = true;
                }
            }
            if ($hasUnchanged && !$hasEmpty) {
                $warn = 'Текст совпадает с черновиком — запись пропущена.';
            }
        }

        return [
            'ok' => true,
            'code' => 'applied',
            'message' => 'Черновик записан в блоки: ' . implode(', ', $labels) . '.',
            'warn_message' => $warn,
            'selected' => $normalized['selected'],
            'updated' => $updated,
            'skipped' => $skipped,
            'rejected' => $rejected,
            'previous' => $previous,
            'new' => $newBodies,
        ];
    }

    /**
     * @param list<mixed> $selectedKeys
     * @return array{selected:list<string>,forbidden:list<string>,rejected:list<array{key:string,reason:string}>}
     */
    private function normalizeSelectedKeys(array $selectedKeys): array
    {
        $selected = [];
        $forbidden = [];
        $rejected = [];
        foreach ($selectedKeys as $raw) {
            if (!is_string($raw) && !is_int($raw)) {
                continue;
            }
            $key = trim((string) $raw);
            if ($key === '') {
                continue;
            }
            if (in_array($key, MonthlyReportSummaryAssemblyService::MANUAL_ONLY_KEYS, true)
                || !in_array($key, MonthlyReportSummaryAssemblyService::WRITABLE_KEYS, true)
            ) {
                if (!in_array($key, $forbidden, true)) {
                    $forbidden[] = $key;
                    $rejected[] = ['key' => $key, 'reason' => 'forbidden_key'];
                }
                continue;
            }
            if (!in_array($key, $selected, true)) {
                $selected[] = $key;
            }
        }

        return [
            'selected' => $selected,
            'forbidden' => $forbidden,
            'rejected' => $rejected,
        ];
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

    private function hasActiveShare(int $monthlyReportId): bool
    {
        if ($monthlyReportId <= 0) {
            return false;
        }
        $sql = <<<'SQL'
SELECT COUNT(*)
FROM report_export_shares s
INNER JOIN report_exports e ON e.id = s.report_export_id
WHERE e.monthly_report_content_id = :mid
  AND s.status = 'active'
SQL;
        $stmt = $this->db->connect()->prepare($sql);
        $stmt->execute([':mid' => $monthlyReportId]);
        return (int) $stmt->fetchColumn() > 0;
    }

    private function mergeProvenance(mixed $current, array $meta): ?string
    {
        $decoded = null;
        if ($current === null || $current === '' || $current === '{}') {
            $decoded = [];
        } elseif (is_array($current)) {
            $decoded = $current;
        } elseif (is_string($current)) {
            $decoded = json_decode($current, true);
        }

        if (!is_array($decoded)) {
            return null;
        }
        if ($decoded !== [] && array_is_list($decoded)) {
            return null;
        }

        foreach ($meta as $k => $v) {
            $decoded[(string) $k] = $v;
        }

        try {
            return json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
        } catch (JsonException) {
            return null;
        }
    }

    private function normalizeBody(string $body): string
    {
        $body = str_replace(["\r\n", "\r"], "\n", $body);
        return trim($body);
    }

    /**
     * @param list<array{key:string,reason:string}> $skipped
     * @param list<array{key:string,reason:string}> $rejected
     */
    private function skipOnlyMessage(array $skipped, array $rejected): string
    {
        if ($rejected !== []) {
            return 'Этот раздел нельзя заполнить автосборкой.';
        }
        foreach ($skipped as $skip) {
            if (($skip['reason'] ?? '') === 'empty_draft' || ($skip['reason'] ?? '') === 'missing_block') {
                return 'Пустой черновик раздела не записан.';
            }
        }
        return 'Текст совпадает с черновиком — запись будет пропущена.';
    }

    private function labelForKey(string $key): string
    {
        return match ($key) {
            'work_completed' => 'Что сделали',
            'next_month_plan' => 'План на следующий месяц',
            'risks_and_blockers' => 'Риски и блокеры',
            default => $key,
        };
    }

    /**
     * @param list<array{key:string,reason:string}> $rejected
     * @param list<string> $selected
     * @return array<string, mixed>
     */
    private function fail(string $code, string $message, array $rejected, array $selected): array
    {
        return [
            'ok' => false,
            'code' => $code,
            'message' => $message,
            'warn_message' => null,
            'selected' => $selected,
            'updated' => [],
            'skipped' => [],
            'rejected' => $rejected,
            'previous' => [],
            'new' => [],
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
