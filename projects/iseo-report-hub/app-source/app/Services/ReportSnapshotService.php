<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Iseo\Repositories\ReportSnapshotRepository;
use Throwable;

/**
 * Internal-only report snapshot create/view with checksum idempotency.
 */
final class ReportSnapshotService
{
    public const PAYLOAD_SCHEMA_VERSION = '1';

    /** @var list<string> */
    private const VIEW_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    /** @var list<string> */
    private const CREATE_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
    ];

    /** @var list<string> */
    private const BLOCK_READY_STATUSES = [
        'reviewed',
        'approved',
    ];

    public function __construct(
        private ReportSnapshotRepository $snapshots,
        private MonthlyReportContentRepository $monthlyRepo,
        private ReportBlockRepository $blockRepo,
        private ReportPreviewService $preview,
        private DatabaseService $db
    ) {
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
     */
    public function canCreate(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::CREATE_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   monthly:?array<string,mixed>,
     *   snapshot:?array<string,mixed>,
     *   can_create:bool,
     *   errors?:array<string,string>
     * }
     */
    public function getActiveForMonthly(int $monthlyReportId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canView($actor)) {
            return [
                'ok' => false,
                'message' => 'You do not have access to report snapshots.',
                'monthly' => null,
                'snapshot' => null,
                'can_create' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $monthly = $this->monthlyRepo->findById($monthlyReportId);
        if ($monthly === null) {
            return [
                'ok' => false,
                'message' => 'Monthly report content not found.',
                'monthly' => null,
                'snapshot' => null,
                'can_create' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $snapshot = $this->snapshots->findActiveByMonthlyId($monthlyReportId);
        $canCreate = $this->canCreate($actor)
            && (string) ($monthly['status'] ?? '') === 'finalized'
            && ($monthly['finalized_at'] ?? null) !== null
            && ($monthly['finalized_at'] ?? '') !== '';

        return [
            'ok' => true,
            'message' => $snapshot !== null ? 'Active snapshot found.' : 'No snapshot yet.',
            'monthly' => $monthly,
            'snapshot' => $snapshot,
            'can_create' => $canCreate && $snapshot === null,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   snapshot:?array<string,mixed>,
     *   idempotent:bool,
     *   errors?:array<string,string>,
     *   failed_gates?:list<string>
     * }
     */
    public function createForMonthly(int $monthlyReportId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canCreate($actor)) {
            $this->auditFailure($actor, $monthlyReportId, null, ['role'], [
                'reason' => 'insufficient_role',
            ]);
            return [
                'ok' => false,
                'message' => 'You do not have permission to create a report snapshot.',
                'snapshot' => null,
                'idempotent' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $monthly = $this->monthlyRepo->findById($monthlyReportId);
        if ($monthly === null) {
            $this->auditFailure($actor, $monthlyReportId, null, ['monthly_exists'], []);
            return [
                'ok' => false,
                'message' => 'Monthly report content not found.',
                'snapshot' => null,
                'idempotent' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $gates = $this->buildCreateGates($monthly);
        $failed = [];
        foreach ($gates as $key => $gate) {
            if (empty($gate['pass'])) {
                $failed[] = $key;
            }
        }
        if ($failed !== []) {
            $this->auditFailure($actor, $monthlyReportId, (int) $monthly['reporting_period_id'], $failed, [
                'gates' => $this->gatePassMap($gates),
            ]);
            return [
                'ok' => false,
                'message' => 'Snapshot creation blocked by readiness gates.',
                'snapshot' => null,
                'idempotent' => false,
                'errors' => ['gates' => 'Failed: ' . implode(', ', $failed)],
                'failed_gates' => $failed,
            ];
        }

        try {
            $composition = $this->preview->assemble($monthlyReportId);
        } catch (Throwable) {
            $composition = null;
        }
        if ($composition === null) {
            $this->auditFailure($actor, $monthlyReportId, (int) $monthly['reporting_period_id'], ['preview_renderable'], []);
            return [
                'ok' => false,
                'message' => 'Could not assemble preview composition for snapshot.',
                'snapshot' => null,
                'idempotent' => false,
                'errors' => ['preview' => 'Assemble failed.'],
            ];
        }

        $payload = $this->buildPayload($composition);
        $checksum = $this->checksumPayload($payload);
        $active = $this->snapshots->findActiveByMonthlyId($monthlyReportId);

        if ($active !== null && strtolower((string) $active['checksum_sha256']) === strtolower($checksum)) {
            $this->snapshots->insertAudit('report_snapshot.idempotent_hit', (int) $actor['id'], (int) $active['id'], [
                'snapshot_id' => (int) $active['id'],
                'monthly_report_content_id' => $monthlyReportId,
                'reporting_period_id' => (int) $monthly['reporting_period_id'],
                'version' => (int) $active['version'],
                'checksum_sha256' => $checksum,
                'actor_user_id' => (int) $actor['id'],
            ]);

            return [
                'ok' => true,
                'message' => 'Active snapshot already matches current checksum (idempotent).',
                'snapshot' => $active,
                'idempotent' => true,
            ];
        }

        $version = $this->snapshots->nextVersion($monthlyReportId);
        $snapshotKey = 'monthly-' . $monthlyReportId . '-v' . $version;
        $renderedText = $this->buildRenderedText($payload);
        $sourceBlockIds = [];
        foreach ($payload['blocks'] as $block) {
            $sourceBlockIds[] = (int) $block['id'];
        }
        $sourceWeeklyIds = $payload['monthly_report']['source_weekly_checkpoint_ids'] ?? [];
        if (!is_array($sourceWeeklyIds)) {
            $sourceWeeklyIds = [];
        }

        $pdo = $this->snapshots->pdo();
        try {
            $pdo->beginTransaction();

            if ($active !== null) {
                $this->snapshots->supersedeActive($monthlyReportId);
            }

            $newId = $this->snapshots->insert([
                'monthly_report_content_id' => $monthlyReportId,
                'reporting_period_id' => (int) $monthly['reporting_period_id'],
                'snapshot_key' => $snapshotKey,
                'version' => $version,
                'status' => 'active',
                'title' => (string) $monthly['title'],
                'render_mode' => (string) ($payload['metadata']['render_mode'] ?? $composition['render_mode']),
                'payload_json' => $this->encodeCanonicalJson($payload),
                'rendered_text' => $renderedText,
                'rendered_html' => null,
                'checksum_sha256' => $checksum,
                'source_block_ids' => json_encode(array_values($sourceBlockIds), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
                'source_weekly_checkpoint_ids' => json_encode(array_values($sourceWeeklyIds), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
                'created_by' => (int) $actor['id'],
            ]);

            $this->snapshots->insertAudit('report_snapshot.created', (int) $actor['id'], $newId, [
                'snapshot_id' => $newId,
                'monthly_report_content_id' => $monthlyReportId,
                'reporting_period_id' => (int) $monthly['reporting_period_id'],
                'version' => $version,
                'checksum_sha256' => $checksum,
                'actor_user_id' => (int) $actor['id'],
                'snapshot_key' => $snapshotKey,
                'superseded_prior' => $active !== null,
            ]);

            if ($active !== null) {
                $this->snapshots->insertAudit('report_snapshot.superseded', (int) $actor['id'], (int) $active['id'], [
                    'snapshot_id' => (int) $active['id'],
                    'monthly_report_content_id' => $monthlyReportId,
                    'reporting_period_id' => (int) $monthly['reporting_period_id'],
                    'version' => (int) $active['version'],
                    'checksum_sha256' => (string) $active['checksum_sha256'],
                    'replaced_by_snapshot_id' => $newId,
                    'actor_user_id' => (int) $actor['id'],
                ]);
            }

            $pdo->commit();

            $created = $this->snapshots->findById($newId);
            return [
                'ok' => true,
                'message' => 'Snapshot created.',
                'snapshot' => $created,
                'idempotent' => false,
            ];
        } catch (Throwable) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            $this->auditFailure($actor, $monthlyReportId, (int) $monthly['reporting_period_id'], ['persist_failed'], [
                'checksum_sha256' => $checksum,
            ]);
            return [
                'ok' => false,
                'message' => 'Could not create snapshot. Please try again.',
                'snapshot' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   snapshot:?array<string,mixed>,
     *   payload:?array<string,mixed>,
     *   errors?:array<string,string>
     * }
     */
    public function getById(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canView($actor)) {
            return [
                'ok' => false,
                'message' => 'You do not have access to report snapshots.',
                'snapshot' => null,
                'payload' => null,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'snapshot' => null,
                'payload' => null,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $payload = $this->decodePayloadJson($snapshot['payload_json'] ?? null);

        return [
            'ok' => true,
            'message' => 'Snapshot loaded.',
            'snapshot' => $snapshot,
            'payload' => $payload,
        ];
    }

    /**
     * @param array{
     *   report: array<string, mixed>,
     *   blocks: list<array<string, mixed>>,
     *   render_mode: string,
     *   flat_fields: array<string, string>,
     *   flat_present: bool,
     *   source_weekly: list<array<string, mixed>>,
     *   diagnostics: array<string, mixed>,
     *   generated_at: string
     * } $previewComposition
     * @return array<string, mixed>
     */
    public function buildPayload(array $previewComposition): array
    {
        $report = $previewComposition['report'];
        $blocksIn = $previewComposition['blocks'];
        $renderMode = (string) $previewComposition['render_mode'];

        $blocks = [];
        foreach ($blocksIn as $block) {
            $sourceIds = $block['_source_ids'] ?? $this->preview->decodeSourceIds($block['source_weekly_checkpoint_ids'] ?? null);
            if (!is_array($sourceIds)) {
                $sourceIds = [];
            }
            $metricRefs = $this->decodeJsonField($block['source_metric_refs'] ?? null);
            $blocks[] = [
                'id' => (int) $block['id'],
                'block_key' => (string) $block['block_key'],
                'block_type' => (string) $block['block_type'],
                'title' => (string) ($block['title'] ?? ''),
                'status' => (string) ($block['status'] ?? ''),
                'sort_order' => (int) ($block['sort_order'] ?? 0),
                'body' => (string) ($block['body'] ?? ''),
                'summary' => (string) ($block['summary'] ?? ''),
                'source_weekly_checkpoint_ids' => array_values(array_map('intval', $sourceIds)),
                'metric_refs' => $metricRefs,
            ];
        }

        usort($blocks, static function (array $a, array $b): int {
            if ($a['sort_order'] === $b['sort_order']) {
                return $a['id'] <=> $b['id'];
            }
            return $a['sort_order'] <=> $b['sort_order'];
        });

        $weeklySources = [];
        foreach ($previewComposition['source_weekly'] as $wc) {
            $weeklySources[] = [
                'id' => (int) $wc['id'],
                'checkpoint_key' => (string) ($wc['checkpoint_key'] ?? ''),
                'week_index' => isset($wc['week_index']) ? (int) $wc['week_index'] : null,
                'status' => (string) ($wc['status'] ?? ''),
                'title' => (string) ($wc['title'] ?? ''),
            ];
        }

        $sourceWeeklyIds = $this->preview->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);

        $diagnostics = $previewComposition['diagnostics'];
        unset($diagnostics['generated_at']);

        return [
            'metadata' => [
                'schema_version' => self::PAYLOAD_SCHEMA_VERSION,
                'snapshot_version' => null,
                'render_mode' => $renderMode,
                'source' => 'report_preview_composition',
                'monthly_report_content_id' => (int) $report['id'],
                'reporting_period_id' => (int) $report['reporting_period_id'],
            ],
            'period' => [
                'id' => (int) $report['reporting_period_id'],
                'key' => (string) ($report['period_key'] ?? ''),
                'period_start' => (string) ($report['period_start'] ?? ''),
                'period_end' => (string) ($report['period_end'] ?? ''),
                'status' => (string) ($report['period_status'] ?? ''),
                'title' => (string) ($report['period_title'] ?? ''),
            ],
            'client' => [
                'id' => isset($report['client_id']) ? (int) $report['client_id'] : null,
                'name' => (string) ($report['client_name'] ?? ''),
                'slug' => (string) ($report['client_slug'] ?? ''),
            ],
            'project' => [
                'id' => isset($report['project_id']) ? (int) $report['project_id'] : null,
                'name' => (string) ($report['project_name'] ?? ''),
                'slug' => (string) ($report['project_slug'] ?? ''),
            ],
            'site' => [
                'id' => isset($report['primary_site_id']) ? (int) $report['primary_site_id'] : null,
                'url' => (string) ($report['primary_site_url'] ?? ''),
                'label' => (string) ($report['primary_site_label'] ?? ''),
            ],
            'monthly_report' => [
                'id' => (int) $report['id'],
                'title' => (string) ($report['title'] ?? ''),
                'status' => (string) ($report['status'] ?? ''),
                'finalized_at' => $report['finalized_at'] !== null ? (string) $report['finalized_at'] : null,
                'source_weekly_checkpoint_ids' => array_values($sourceWeeklyIds),
                'flat_fields' => $previewComposition['flat_fields'],
            ],
            'blocks' => $blocks,
            'weekly_sources' => $weeklySources,
            'diagnostics' => $diagnostics,
            'render' => [
                'mode' => $renderMode,
                'block_count' => count($blocks),
                'outline' => $this->buildOutline($blocks, $renderMode),
            ],
        ];
    }

    /**
     * @param array<string, mixed> $payload
     */
    public function checksumPayload(array $payload): string
    {
        $normalized = $payload;
        if (isset($normalized['metadata']) && is_array($normalized['metadata'])) {
            // snapshot_version filled at insert time; checksum excludes volatile version stamp.
            $normalized['metadata']['snapshot_version'] = null;
        }
        $json = $this->encodeCanonicalJson($this->sortKeysRecursive($normalized));
        return hash('sha256', $json);
    }

    /**
     * @param array<string, mixed> $monthly
     * @return array<string, array{pass:bool,detail:string}>
     */
    private function buildCreateGates(array $monthly): array
    {
        $gates = [
            'monthly_exists' => ['pass' => true, 'detail' => 'Monthly report found.'],
            'status_finalized' => ['pass' => false, 'detail' => 'Status must be finalized.'],
            'finalized_at_present' => ['pass' => false, 'detail' => 'finalized_at required.'],
            'preview_renderable' => ['pass' => false, 'detail' => 'Preview not assembled.'],
            'render_mode_valid' => ['pass' => false, 'detail' => 'Render mode invalid.'],
            'has_non_archived_blocks' => ['pass' => false, 'detail' => 'No non-archived blocks.'],
            'required_blocks_present' => ['pass' => false, 'detail' => 'Required blocks missing.'],
            'no_draft_or_in_progress_blocks' => ['pass' => false, 'detail' => 'Draft/in_progress remain.'],
            'source_weekly_refs_resolve' => ['pass' => false, 'detail' => 'Weekly refs unresolved.'],
        ];

        $status = (string) ($monthly['status'] ?? '');
        $gates['status_finalized'] = [
            'pass' => $status === 'finalized',
            'detail' => $status === 'finalized' ? 'Status is finalized.' : 'Status is "' . $status . '".',
        ];

        $finalizedAt = $monthly['finalized_at'] ?? null;
        $hasFinalizedAt = $finalizedAt !== null && (string) $finalizedAt !== '';
        $gates['finalized_at_present'] = [
            'pass' => $hasFinalizedAt,
            'detail' => $hasFinalizedAt ? 'finalized_at present.' : 'finalized_at missing.',
        ];

        $previewOk = false;
        $renderMode = 'empty';
        $missingWeekly = [];
        try {
            $payload = $this->preview->assemble((int) $monthly['id']);
            if ($payload !== null) {
                $previewOk = true;
                $renderMode = (string) ($payload['render_mode'] ?? 'empty');
                $missingWeekly = $payload['diagnostics']['missing_weekly_ids'] ?? [];
                if (!is_array($missingWeekly)) {
                    $missingWeekly = [];
                }
            }
        } catch (Throwable) {
            $previewOk = false;
        }

        $gates['preview_renderable'] = [
            'pass' => $previewOk,
            'detail' => $previewOk ? 'Preview assembles successfully.' : 'Preview assembly failed.',
        ];

        $modeValid = in_array($renderMode, ['blocks_primary', 'flat_fallback'], true);
        $gates['render_mode_valid'] = [
            'pass' => $modeValid,
            'detail' => $modeValid
                ? 'Render mode "' . $renderMode . '" is valid.'
                : 'Render mode "' . $renderMode . '" not allowed.',
        ];

        $allBlocks = $this->blockRepo->listByMonthlyReportId((int) $monthly['id']);
        $active = [];
        foreach ($allBlocks as $block) {
            if ((string) ($block['status'] ?? '') === 'archived') {
                continue;
            }
            $active[] = $block;
        }

        $gates['has_non_archived_blocks'] = [
            'pass' => $active !== [],
            'detail' => $active !== []
                ? count($active) . ' non-archived block(s).'
                : 'At least one non-archived block is required.',
        ];

        $byKey = [];
        foreach ($active as $block) {
            $byKey[(string) $block['block_key']] = $block;
        }
        $missingRequired = [];
        foreach (ReportFinalizationService::REQUIRED_BLOCK_KEYS as $key) {
            if (!isset($byKey[$key])) {
                $missingRequired[] = $key;
            }
        }
        $gates['required_blocks_present'] = [
            'pass' => $missingRequired === [],
            'detail' => $missingRequired === []
                ? 'All required blocks present.'
                : 'Missing: ' . implode(', ', $missingRequired),
        ];

        $draftish = [];
        foreach ($active as $block) {
            $st = (string) $block['status'];
            if (in_array($st, ['draft', 'in_progress'], true)) {
                $draftish[] = (string) $block['block_key'] . '=' . $st;
            }
        }
        $gates['no_draft_or_in_progress_blocks'] = [
            'pass' => $draftish === [],
            'detail' => $draftish === []
                ? 'No non-archived draft/in_progress blocks.'
                : 'Blocking: ' . implode(', ', $draftish),
        ];

        $missingList = [];
        foreach ($missingWeekly as $id) {
            $missingList[] = (string) $id;
        }
        $gates['source_weekly_refs_resolve'] = [
            'pass' => $missingList === [],
            'detail' => $missingList === []
                ? 'All source weekly checkpoint refs resolve.'
                : 'Missing weekly ids: ' . implode(', ', $missingList),
        ];

        return $gates;
    }

    /**
     * @param list<array<string, mixed>> $blocks
     */
    private function buildOutline(array $blocks, string $renderMode): string
    {
        $lines = ['Render mode: ' . $renderMode];
        foreach ($blocks as $block) {
            $lines[] = sprintf(
                '%d. [%s] %s',
                (int) $block['sort_order'],
                (string) $block['block_key'],
                (string) $block['title']
            );
        }
        return implode("\n", $lines);
    }

    /**
     * @param array<string, mixed> $payload
     */
    private function buildRenderedText(array $payload): string
    {
        $lines = [];
        $mr = $payload['monthly_report'] ?? [];
        $period = $payload['period'] ?? [];
        $lines[] = (string) ($mr['title'] ?? 'Monthly report');
        $lines[] = 'Period: ' . (string) ($period['key'] ?? '');
        $lines[] = 'Status: ' . (string) ($mr['status'] ?? '');
        $lines[] = 'Render: ' . (string) ($payload['metadata']['render_mode'] ?? '');
        $lines[] = '';
        $blocks = $payload['blocks'] ?? [];
        if (is_array($blocks)) {
            foreach ($blocks as $block) {
                if (!is_array($block)) {
                    continue;
                }
                $lines[] = '## ' . (string) ($block['title'] ?? $block['block_key'] ?? 'Block');
                $lines[] = 'Key: ' . (string) ($block['block_key'] ?? '');
                $summary = trim((string) ($block['summary'] ?? ''));
                $body = trim((string) ($block['body'] ?? ''));
                if ($summary !== '') {
                    $lines[] = $summary;
                }
                if ($body !== '') {
                    $lines[] = $body;
                }
                $lines[] = '';
            }
        }
        return rtrim(implode("\n", $lines));
    }

    /**
     * @param array<string, mixed> $payload
     */
    private function encodeCanonicalJson(array $payload): string
    {
        $sorted = $this->sortKeysRecursive($payload);
        $json = json_encode($sorted, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR);
        return $json;
    }

    /**
     * @param mixed $value
     * @return mixed
     */
    private function sortKeysRecursive(mixed $value): mixed
    {
        if (!is_array($value)) {
            return $value;
        }

        $isList = array_is_list($value);
        if ($isList) {
            $out = [];
            foreach ($value as $item) {
                $out[] = $this->sortKeysRecursive($item);
            }
            return $out;
        }

        $keys = array_keys($value);
        sort($keys, SORT_STRING);
        $out = [];
        foreach ($keys as $key) {
            $out[$key] = $this->sortKeysRecursive($value[$key]);
        }
        return $out;
    }

    /**
     * @return array<string, mixed>|list<mixed>|null
     */
    private function decodeJsonField(mixed $raw): mixed
    {
        if ($raw === null || $raw === '') {
            return null;
        }
        if (is_array($raw)) {
            return $raw;
        }
        if (!is_string($raw)) {
            return null;
        }
        $decoded = json_decode($raw, true);
        return is_array($decoded) ? $decoded : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    private function decodePayloadJson(mixed $raw): ?array
    {
        if (is_array($raw)) {
            return $raw;
        }
        if (!is_string($raw) || $raw === '') {
            return null;
        }
        $decoded = json_decode($raw, true);
        return is_array($decoded) ? $decoded : null;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param list<string> $failedGates
     * @param array<string, mixed> $extra
     */
    private function auditFailure(array $actor, int $monthlyReportId, ?int $periodId, array $failedGates, array $extra): void
    {
        try {
            $meta = array_merge([
                'monthly_report_content_id' => $monthlyReportId,
                'reporting_period_id' => $periodId,
                'failed_gate_keys' => $failedGates,
                'actor_user_id' => (int) $actor['id'],
            ], $extra);
            $this->snapshots->insertAudit(
                'report_snapshot.creation_failed',
                (int) $actor['id'],
                null,
                $meta
            );
        } catch (Throwable) {
            // Audit must not break user-facing error path.
        }
    }

    /**
     * @param array<string, array{pass:bool,detail:string}> $gates
     * @return array<string, bool>
     */
    private function gatePassMap(array $gates): array
    {
        $out = [];
        foreach ($gates as $key => $gate) {
            $out[$key] = !empty($gate['pass']);
        }
        return $out;
    }

    private function assertDb(): void
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();
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
        $have = $user['roles'] ?? [];
        if (!is_array($have)) {
            return false;
        }
        foreach ($roles as $role) {
            if (in_array($role, $have, true)) {
                return true;
            }
        }
        return false;
    }
}
