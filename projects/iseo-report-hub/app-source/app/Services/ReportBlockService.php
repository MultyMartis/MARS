<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportBlockRepository;
use JsonException;
use Throwable;

/**
 * Report block CRUD — validation, locks, status workflow, audit.
 */
final class ReportBlockService
{
    /** @var list<string> */
    public const STATUSES = [
        'draft',
        'in_progress',
        'ready_for_review',
        'reviewed',
        'approved',
        'archived',
    ];

    /** @var list<string> */
    public const BLOCK_TYPES = [
        'executive_summary',
        'work_completed',
        'results_summary',
        'key_findings',
        'risks_and_blockers',
        'next_month_plan',
        'client_notes',
        'internal_notes',
        'custom_text',
        'metric_snapshot',
        'weekly_summary',
    ];

    private const BODY_MAX_LEN = 50000;
    private const SUMMARY_MAX_LEN = 10000;

    /** @var list<string> */
    private const CREATE_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    /** @var list<string> */
    private const FULL_EDIT_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    /** Raw block editor is admin/lead only — not specialist demo UI. */
    /** @var list<string> */
    private const SPECIALIST_EDIT_ROLES = [];

    /** @var list<string> */
    private const READ_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    /** @var list<string> */
    private const OWNER_REVIEWER_ASSIGN_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    public function __construct(
        private ReportBlockRepository $repo,
        private DatabaseService $db
    ) {
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canList(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::READ_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canCreate(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::CREATE_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param array<string, mixed>|null $block
     */
    public function canEdit(?array $user, ?array $block = null): bool
    {
        if ($user === null) {
            return false;
        }

        if ($this->userHasAnyRole($user, self::FULL_EDIT_ROLES)) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            if ($block === null) {
                return true;
            }
            $status = (string) ($block['status'] ?? '');
            return in_array($status, ['draft', 'in_progress', 'ready_for_review'], true);
        }

        return false;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canAssignOwnerReviewer(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::OWNER_REVIEWER_ASSIGN_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canSetStatus(?array $user, string $status): bool
    {
        if ($user === null || !in_array($status, self::STATUSES, true)) {
            return false;
        }

        if ($this->userHasAnyRole($user, ['admin_owner', 'seo_lead_reviewer'])) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            return in_array($status, ['draft', 'in_progress', 'ready_for_review'], true);
        }

        return false;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getById(int $id): ?array
    {
        $this->assertDb();
        return $this->repo->findById($id);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getMonthlyReport(int $monthlyReportId): ?array
    {
        $this->assertDb();
        return $this->repo->findMonthlyReportById($monthlyReportId);
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listForMonthlyReport(int $monthlyReportId): array
    {
        $this->assertDb();
        return $this->repo->listByMonthlyReportId($monthlyReportId);
    }

    public function countBlocks(): int
    {
        $this->assertDb();
        return $this->repo->countAll();
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function selectableWeeklyCheckpoints(int $periodId): array
    {
        $this->assertDb();
        return $this->repo->listWeeklyCheckpointsForPeriod($periodId);
    }

    /**
     * @return list<array{id:int,name:string,email:string}>
     */
    public function selectableInternalUsers(): array
    {
        $this->assertDb();
        return $this->repo->listInternalUsers();
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

    /**
     * Pretty-print JSON column for forms; empty → ''.
     */
    public function jsonFieldToForm(mixed $raw): string
    {
        if ($raw === null || $raw === '') {
            return '';
        }
        if (is_array($raw)) {
            try {
                return json_encode($raw, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_THROW_ON_ERROR);
            } catch (JsonException) {
                return '';
            }
        }
        if (!is_string($raw)) {
            return '';
        }
        $decoded = json_decode($raw, true);
        if (!is_array($decoded)) {
            return $raw;
        }
        try {
            return json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_THROW_ON_ERROR);
        } catch (JsonException) {
            return $raw;
        }
    }

    /**
     * @param list<int> $ids
     * @param list<array<string, mixed>> $available
     * @return list<array<string, mixed>>
     */
    public function resolveSourceCheckpointRows(array $ids, array $available): array
    {
        if ($ids === []) {
            return [];
        }
        $byId = [];
        foreach ($available as $row) {
            $byId[(int) $row['id']] = $row;
        }
        $out = [];
        foreach ($ids as $id) {
            if (isset($byId[$id])) {
                $out[] = $byId[$id];
            }
        }
        return $out;
    }

    /**
     * Parent monthly report locks create/edit for non-privileged users.
     *
     * @param array<string, mixed> $monthly
     */
    public function parentMonthlyLockedForNonAdmin(array $monthly): bool
    {
        $status = (string) ($monthly['status'] ?? '');
        return in_array($status, ['archived', 'finalized'], true);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $monthly
     */
    public function canMutateAgainstParent(array $user, array $monthly): bool
    {
        $status = (string) ($monthly['status'] ?? '');
        if ($status === 'archived' || $status === 'finalized') {
            // MVP: reopen required before any block create/edit, including admin_owner.
            return false;
        }
        return true;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $monthly
     * @param array<string, mixed> $input
     * @return array{ok:bool,id?:int,errors?:array<string,string>,message?:string,notice?:string}
     */
    public function create(array $user, array $monthly, array $input): array
    {
        $this->assertDb();

        if (!$this->canCreate($user)) {
            return ['ok' => false, 'message' => 'You do not have permission to create report blocks.', 'errors' => []];
        }

        if (!$this->canMutateAgainstParent($user, $monthly)) {
            return [
                'ok' => false,
                'message' => 'Parent monthly report is archived or finalized.',
                'errors' => ['monthly_report_content_id' => 'Parent monthly report is locked for create.'],
            ];
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $normalized = $this->normalizeInput($input, null, (int) $monthly['id']);
        $errors = $this->validateForCreate($normalized, $monthly, $user, $periodId);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $reviewedAt = null;
        $approvedAt = null;
        if (in_array($normalized['status'], ['reviewed', 'approved'], true)) {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($normalized['status'] === 'approved') {
            $approvedAt = date('Y-m-d H:i:s');
        }

        $pdo = $this->repo->pdo();
        try {
            $pdo->beginTransaction();
            $id = $this->repo->insert([
                'monthly_report_content_id' => (int) $monthly['id'],
                'block_key' => $normalized['block_key'],
                'block_type' => $normalized['block_type'],
                'sort_order' => $normalized['sort_order'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'body' => $normalized['body'],
                'summary' => $normalized['summary'],
                'data_json' => $normalized['data_json'],
                'source_weekly_checkpoint_ids' => $normalized['source_weekly_checkpoint_ids_json'],
                'source_metric_refs' => $normalized['source_metric_refs'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'created_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'approved_at' => $approvedAt,
            ]);

            $this->repo->insertAudit('report_block.created', (int) $user['id'], $id, [
                'id' => $id,
                'monthly_report_content_id' => (int) $monthly['id'],
                'block_key' => $normalized['block_key'],
                'status' => $normalized['status'],
            ]);

            if ($normalized['status'] === 'reviewed') {
                $this->repo->insertAudit('report_block.reviewed', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'reviewed',
                ]);
            }
            if ($normalized['status'] === 'approved') {
                $this->repo->insertAudit('report_block.approved', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'approved',
                ]);
            }
            if ($normalized['status'] === 'archived') {
                $this->repo->insertAudit('report_block.archived', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'archived',
                ]);
            }

            $pdo->commit();

            $result = ['ok' => true, 'id' => $id];
            if ($normalized['source_ids'] === []) {
                $result['notice'] = 'No source weekly checkpoints selected.';
            }
            return $result;
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            if ($this->repo->isUniqueViolation($e)) {
                return [
                    'ok' => false,
                    'errors' => [
                        'block_key' => 'A block with this key already exists for this monthly report.',
                    ],
                    'message' => 'Duplicate block key for this monthly report.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not create report block. Please try again.',
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $monthly
     * @param array<string, mixed> $input
     * @return array{ok:bool,errors?:array<string,string>,message?:string,notice?:string}
     */
    public function update(array $user, array $existing, array $monthly, array $input): array
    {
        $this->assertDb();

        if (!$this->canEdit($user, $existing)) {
            return ['ok' => false, 'message' => 'You do not have permission to edit this report block.', 'errors' => []];
        }

        if (!$this->canMutateAgainstParent($user, $monthly)) {
            return [
                'ok' => false,
                'message' => 'Parent monthly report is archived or finalized.',
                'errors' => ['monthly_report_content_id' => 'Parent monthly report is locked for edit.'],
            ];
        }

        $periodId = (int) $monthly['reporting_period_id'];
        $normalized = $this->normalizeInput($input, $existing, (int) $existing['monthly_report_content_id']);
        $errors = $this->validateForUpdate($normalized, $existing, $monthly, $user, $periodId);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $oldStatus = (string) $existing['status'];
        $newStatus = $normalized['status'];

        $reviewedAt = $existing['reviewed_at'] !== null && $existing['reviewed_at'] !== ''
            ? (string) $existing['reviewed_at']
            : null;
        $approvedAt = $existing['approved_at'] !== null && $existing['approved_at'] !== ''
            ? (string) $existing['approved_at']
            : null;

        if (in_array($newStatus, ['reviewed', 'approved'], true) && $reviewedAt === null) {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($newStatus === 'approved' && $approvedAt === null) {
            $approvedAt = date('Y-m-d H:i:s');
            if ($reviewedAt === null) {
                $reviewedAt = $approvedAt;
            }
        }

        $changed = [];
        $trackFields = [
            'block_key', 'block_type', 'sort_order', 'status', 'title', 'body', 'summary',
            'data_json', 'source_metric_refs', 'source_weekly_checkpoint_ids',
            'owner_user_id', 'reviewer_user_id',
        ];
        foreach ($trackFields as $field) {
            if ($field === 'source_weekly_checkpoint_ids') {
                $oldIds = $this->decodeSourceIds($existing['source_weekly_checkpoint_ids'] ?? null);
                $newIds = $normalized['source_ids'];
                sort($oldIds);
                sort($newIds);
                if ($oldIds !== $newIds) {
                    $changed[] = $field;
                }
                continue;
            }
            if ($field === 'data_json' || $field === 'source_metric_refs') {
                $oldNorm = $this->normalizeJsonCompare($existing[$field] ?? null);
                $newNorm = $this->normalizeJsonCompare($normalized[$field] ?? null);
                if ($oldNorm !== $newNorm) {
                    $changed[] = $field;
                }
                continue;
            }
            $old = $existing[$field] ?? null;
            $new = $normalized[$field] ?? null;
            if ((string) ($old ?? '') !== (string) ($new ?? '')) {
                $changed[] = $field;
            }
        }

        $pdo = $this->repo->pdo();
        try {
            $pdo->beginTransaction();
            $this->repo->update((int) $existing['id'], [
                'block_key' => $normalized['block_key'],
                'block_type' => $normalized['block_type'],
                'sort_order' => $normalized['sort_order'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'body' => $normalized['body'],
                'summary' => $normalized['summary'],
                'data_json' => $normalized['data_json'],
                'source_weekly_checkpoint_ids' => $normalized['source_weekly_checkpoint_ids_json'],
                'source_metric_refs' => $normalized['source_metric_refs'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'updated_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'approved_at' => $approvedAt,
            ]);

            if ($changed !== []) {
                $this->repo->insertAudit('report_block.updated', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'monthly_report_content_id' => (int) $existing['monthly_report_content_id'],
                    'changed' => $changed,
                ]);
            }

            if (in_array('sort_order', $changed, true)) {
                $this->repo->insertAudit('report_block.reordered', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'sort_order' => $normalized['sort_order'],
                ]);
            }

            if ($oldStatus !== $newStatus) {
                $this->repo->insertAudit('report_block.status_changed', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'from' => $oldStatus,
                    'to' => $newStatus,
                ]);
                if ($newStatus === 'reviewed') {
                    $this->repo->insertAudit('report_block.reviewed', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'reviewed',
                    ]);
                }
                if ($newStatus === 'approved') {
                    $this->repo->insertAudit('report_block.approved', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'approved',
                    ]);
                }
                if ($newStatus === 'archived') {
                    $this->repo->insertAudit('report_block.archived', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'archived',
                    ]);
                }
            }

            $pdo->commit();

            $result = ['ok' => true];
            if ($normalized['source_ids'] === []) {
                $result['notice'] = 'No source weekly checkpoints selected.';
            }
            return $result;
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            if ($this->repo->isUniqueViolation($e)) {
                return [
                    'ok' => false,
                    'errors' => [
                        'block_key' => 'A block with this key already exists for this monthly report.',
                    ],
                    'message' => 'Duplicate block key for this monthly report.',
                ];
            }
            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not update report block. Please try again.',
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return list<string>
     */
    public function allowedStatusesForForm(array $user, ?string $fromStatus): array
    {
        $out = [];
        foreach (self::STATUSES as $status) {
            if ($fromStatus === null || $fromStatus === $status) {
                if ($this->canSetStatus($user, $status)) {
                    $out[] = $status;
                }
                continue;
            }
            if ($this->isTransitionAllowed($fromStatus, $status, $user)
                && $this->canSetStatus($user, $status)) {
                $out[] = $status;
            }
        }
        if ($fromStatus !== null && in_array($fromStatus, self::STATUSES, true) && !in_array($fromStatus, $out, true)) {
            array_unshift($out, $fromStatus);
        }
        return array_values(array_unique($out));
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     */
    public function isTransitionAllowed(string $from, string $to, array $user): bool
    {
        if ($from === $to) {
            return true;
        }

        $forward = [
            'draft' => ['in_progress'],
            'in_progress' => ['ready_for_review'],
            'ready_for_review' => ['reviewed'],
            'reviewed' => ['approved'],
        ];

        if (isset($forward[$from]) && in_array($to, $forward[$from], true)) {
            return true;
        }

        // any non-approved → archived
        if ($from !== 'approved' && $to === 'archived') {
            return true;
        }

        // approved reopen / archive by admin_owner or seo_lead_reviewer
        if ($from === 'approved' && $this->userHasAnyRole($user, ['admin_owner', 'seo_lead_reviewer'])) {
            return true;
        }

        // archived reopen by admin_owner or seo_lead_reviewer
        if ($from === 'archived' && $this->userHasAnyRole($user, ['admin_owner', 'seo_lead_reviewer'])) {
            return true;
        }

        return false;
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{
     *   monthly_report_content_id:int,
     *   block_key:string,
     *   block_type:string,
     *   sort_order:int,
     *   status:string,
     *   title:string,
     *   body:?string,
     *   summary:?string,
     *   data_json:?string,
     *   data_json_error:?string,
     *   source_ids:list<int>,
     *   source_weekly_checkpoint_ids_json:?string,
     *   source_metric_refs:?string,
     *   source_metric_refs_error:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * }
     */
    public function normalizeInput(array $input, ?array $existing, int $monthlyReportId): array
    {
        $status = isset($input['status']) && is_string($input['status'])
            ? trim($input['status'])
            : (string) ($existing['status'] ?? 'draft');

        $blockKey = isset($input['block_key']) && is_string($input['block_key'])
            ? trim($input['block_key'])
            : (string) ($existing['block_key'] ?? '');

        $blockType = isset($input['block_type']) && is_string($input['block_type'])
            ? trim($input['block_type'])
            : (string) ($existing['block_type'] ?? '');

        $sortRaw = $input['sort_order'] ?? ($existing['sort_order'] ?? 0);
        if (is_string($sortRaw) && trim($sortRaw) === '') {
            $sortOrder = 0;
        } else {
            $sortOrder = (int) $sortRaw;
        }

        $title = isset($input['title']) && is_string($input['title']) ? trim($input['title']) : '';
        if ($existing !== null && $title === '' && isset($existing['title'])) {
            $title = (string) $existing['title'];
        }

        $body = array_key_exists('body', $input)
            ? $this->nullableText($input['body'] ?? null)
            : ($existing !== null ? $this->nullableText($existing['body'] ?? null) : null);

        $summary = array_key_exists('summary', $input)
            ? $this->nullableText($input['summary'] ?? null)
            : ($existing !== null ? $this->nullableText($existing['summary'] ?? null) : null);

        $dataJsonResult = $this->normalizeJsonObjectOrArrayField(
            $input,
            $existing,
            'data_json'
        );
        $metricRefsResult = $this->normalizeJsonObjectOrArrayField(
            $input,
            $existing,
            'source_metric_refs'
        );

        $sourceIds = $this->normalizeSourceIdsInput($input, $existing);

        $ownerRaw = $input['owner_user_id'] ?? ($existing['owner_user_id'] ?? '');
        $ownerId = ($ownerRaw === '' || $ownerRaw === null) ? null : (int) $ownerRaw;
        if ($ownerId !== null && $ownerId <= 0) {
            $ownerId = null;
        }

        $reviewerRaw = $input['reviewer_user_id'] ?? ($existing['reviewer_user_id'] ?? '');
        $reviewerId = ($reviewerRaw === '' || $reviewerRaw === null) ? null : (int) $reviewerRaw;
        if ($reviewerId !== null && $reviewerId <= 0) {
            $reviewerId = null;
        }

        $sourceJson = null;
        if ($sourceIds !== []) {
            $sourceJson = json_encode(array_values($sourceIds), JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
        }

        return [
            'monthly_report_content_id' => $monthlyReportId,
            'block_key' => $blockKey,
            'block_type' => $blockType,
            'sort_order' => $sortOrder,
            'status' => $status,
            'title' => $title,
            'body' => $body,
            'summary' => $summary,
            'data_json' => $dataJsonResult['json'],
            'data_json_error' => $dataJsonResult['error'],
            'source_ids' => $sourceIds,
            'source_weekly_checkpoint_ids_json' => $sourceJson,
            'source_metric_refs' => $metricRefsResult['json'],
            'source_metric_refs_error' => $metricRefsResult['error'],
            'owner_user_id' => $ownerId,
            'reviewer_user_id' => $reviewerId,
        ];
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{json:?string,error:?string}
     */
    private function normalizeJsonObjectOrArrayField(array $input, ?array $existing, string $field): array
    {
        if (!array_key_exists($field, $input)) {
            if ($existing === null) {
                return ['json' => null, 'error' => null];
            }
            $existingRaw = $existing[$field] ?? null;
            if ($existingRaw === null || $existingRaw === '') {
                return ['json' => null, 'error' => null];
            }
            if (is_array($existingRaw)) {
                try {
                    return [
                        'json' => json_encode($existingRaw, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR),
                        'error' => null,
                    ];
                } catch (JsonException) {
                    return ['json' => null, 'error' => 'Invalid JSON.'];
                }
            }
            if (is_string($existingRaw)) {
                return ['json' => $existingRaw, 'error' => null];
            }
            return ['json' => null, 'error' => null];
        }

        $raw = $input[$field];
        if (!is_string($raw)) {
            return ['json' => null, 'error' => 'Invalid JSON.'];
        }
        $trimmed = trim($raw);
        if ($trimmed === '') {
            return ['json' => null, 'error' => null];
        }

        try {
            $decoded = json_decode($trimmed, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException) {
            return ['json' => null, 'error' => 'Invalid JSON.'];
        }

        if (!is_array($decoded)) {
            return ['json' => null, 'error' => 'JSON must be an object or array.'];
        }

        try {
            return [
                'json' => json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR),
                'error' => null,
            ];
        } catch (JsonException) {
            return ['json' => null, 'error' => 'Invalid JSON.'];
        }
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return list<int>
     */
    private function normalizeSourceIdsInput(array $input, ?array $existing): array
    {
        if (array_key_exists('source_weekly_checkpoint_ids', $input)) {
            $raw = $input['source_weekly_checkpoint_ids'];
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
            if (is_string($raw)) {
                $trimmed = trim($raw);
                if ($trimmed === '') {
                    return [];
                }
                if (str_starts_with($trimmed, '[')) {
                    return $this->decodeSourceIds($trimmed);
                }
                $parts = preg_split('/\s*,\s*/', $trimmed) ?: [];
                $out = [];
                foreach ($parts as $part) {
                    if ($part === '') {
                        continue;
                    }
                    $id = (int) $part;
                    if ($id > 0) {
                        $out[] = $id;
                    }
                }
                return array_values(array_unique($out));
            }
            return [];
        }

        if ($existing !== null) {
            return $this->decodeSourceIds($existing['source_weekly_checkpoint_ids'] ?? null);
        }

        return [];
    }

    /**
     * @param array<string, mixed> $data
     * @param array<string, mixed> $monthly
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForCreate(array $data, array $monthly, array $user, int $periodId): array
    {
        $errors = $this->validateCommon($data, $periodId);

        if ($this->repo->existsForParentKey((int) $monthly['id'], $data['block_key'])) {
            $errors['block_key'] = 'A block with this key already exists for this monthly report.';
        }

        if (!$this->canSetStatus($user, $data['status'])) {
            $errors['status'] = 'Invalid status for your role.';
        }

        return $errors;
    }

    /**
     * @param array<string, mixed> $data
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $monthly
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForUpdate(array $data, array $existing, array $monthly, array $user, int $periodId): array
    {
        $errors = $this->validateCommon($data, $periodId);
        $existingStatus = (string) $existing['status'];
        $isAdmin = $this->userHasAnyRole($user, ['admin_owner']);
        $isPrivileged = $this->userHasAnyRole($user, ['admin_owner', 'seo_lead_reviewer']);
        $monthlyStatus = (string) ($monthly['status'] ?? '');

        // block_key / block_type editable while draft; admin_owner override
        if ($existingStatus !== 'draft' && !$isAdmin) {
            if ($data['block_key'] !== (string) $existing['block_key']) {
                $errors['block_key'] = 'Block key can only be changed while draft (or by admin_owner).';
            }
            if ($data['block_type'] !== (string) $existing['block_type']) {
                $errors['block_type'] = 'Block type can only be changed while draft (or by admin_owner).';
            }
        }

        // Approved content editable only by privileged reopen roles
        if ($existingStatus === 'approved' && !$isPrivileged) {
            $contentFields = ['title', 'body', 'summary', 'data_json', 'source_metric_refs', 'sort_order'];
            foreach ($contentFields as $field) {
                if ($field === 'data_json' || $field === 'source_metric_refs') {
                    $oldNorm = $this->normalizeJsonCompare($existing[$field] ?? null);
                    $newNorm = $this->normalizeJsonCompare($data[$field] ?? null);
                    if ($oldNorm !== $newNorm) {
                        $errors[$field] = 'Approved block content can only be edited by admin_owner or seo_lead_reviewer.';
                    }
                    continue;
                }
                $old = (string) ($existing[$field] ?? '');
                $new = (string) ($data[$field] ?? '');
                if ($old !== $new) {
                    $errors[$field] = 'Approved block content can only be edited by admin_owner or seo_lead_reviewer.';
                }
            }
            $oldIds = $this->decodeSourceIds($existing['source_weekly_checkpoint_ids'] ?? null);
            $newIds = $data['source_ids'];
            sort($oldIds);
            sort($newIds);
            if ($oldIds !== $newIds) {
                $errors['source_weekly_checkpoint_ids'] = 'Source weekly checkpoints can only be changed by privileged roles when approved.';
            }
        }

        // Parent finalized locks content unless admin_owner
        if ($monthlyStatus === 'finalized' && !$isAdmin) {
            $contentFields = ['title', 'body', 'summary', 'data_json', 'source_metric_refs', 'sort_order', 'block_key', 'block_type'];
            foreach ($contentFields as $field) {
                if ($field === 'data_json' || $field === 'source_metric_refs') {
                    $oldNorm = $this->normalizeJsonCompare($existing[$field] ?? null);
                    $newNorm = $this->normalizeJsonCompare($data[$field] ?? null);
                    if ($oldNorm !== $newNorm) {
                        $errors[$field] = 'Parent monthly report is finalized; only admin_owner can edit.';
                    }
                    continue;
                }
                $old = (string) ($existing[$field] ?? '');
                $new = (string) ($data[$field] ?? '');
                if ($old !== $new) {
                    $errors[$field] = 'Parent monthly report is finalized; only admin_owner can edit.';
                }
            }
        }

        if ($this->repo->existsForParentKey(
            (int) $existing['monthly_report_content_id'],
            $data['block_key'],
            (int) $existing['id']
        )) {
            $errors['block_key'] = 'A block with this key already exists for this monthly report.';
        }

        if (!$this->canAssignOwnerReviewer($user)) {
            $oldOwner = $existing['owner_user_id'] !== null ? (int) $existing['owner_user_id'] : null;
            $oldReviewer = $existing['reviewer_user_id'] !== null ? (int) $existing['reviewer_user_id'] : null;
            if ($data['owner_user_id'] !== $oldOwner) {
                $errors['owner_user_id'] = 'Owner can only be assigned by admin_owner or seo_lead_reviewer.';
            }
            if ($data['reviewer_user_id'] !== $oldReviewer) {
                $errors['reviewer_user_id'] = 'Reviewer can only be assigned by admin_owner or seo_lead_reviewer.';
            }
        }

        if ($data['status'] !== $existingStatus) {
            if (!$this->isTransitionAllowed($existingStatus, $data['status'], $user)) {
                $errors['status'] = 'Status transition is not allowed.';
            } elseif (!$this->canSetStatus($user, $data['status'])) {
                $errors['status'] = 'Invalid status for your role.';
            }
        }

        return $errors;
    }

    /**
     * @param array<string, mixed> $data
     * @return array<string, string>
     */
    private function validateCommon(array $data, int $periodId): array
    {
        $errors = [];

        if (!in_array($data['status'], self::STATUSES, true)) {
            $errors['status'] = 'Invalid status.';
        }

        if ($data['block_key'] === '') {
            $errors['block_key'] = 'Block key is required.';
        } elseif (mb_strlen($data['block_key']) > 64) {
            $errors['block_key'] = 'Block key is too long (max 64 characters).';
        } elseif (preg_match('/^[a-z0-9_\-]+$/', $data['block_key']) !== 1) {
            $errors['block_key'] = 'Block key must be slug-like: lowercase letters, digits, underscore, hyphen.';
        }

        if (!in_array($data['block_type'], self::BLOCK_TYPES, true)) {
            $errors['block_type'] = 'Invalid block type.';
        }

        if ($data['sort_order'] < 0) {
            $errors['sort_order'] = 'Sort order must be an integer >= 0.';
        }

        if ($data['title'] === '') {
            $errors['title'] = 'Title is required.';
        } elseif (mb_strlen($data['title']) > 255) {
            $errors['title'] = 'Title is too long (max 255 characters).';
        }

        if ($data['body'] !== null && mb_strlen($data['body']) > self::BODY_MAX_LEN) {
            $errors['body'] = 'Body is too long (max ' . self::BODY_MAX_LEN . ' characters).';
        }

        if ($data['summary'] !== null && mb_strlen($data['summary']) > self::SUMMARY_MAX_LEN) {
            $errors['summary'] = 'Summary is too long (max ' . self::SUMMARY_MAX_LEN . ' characters).';
        }

        if ($data['data_json_error'] !== null) {
            $errors['data_json'] = (string) $data['data_json_error'];
        }

        if ($data['source_metric_refs_error'] !== null) {
            $errors['source_metric_refs'] = (string) $data['source_metric_refs_error'];
        }

        if ($data['source_ids'] !== []) {
            $valid = $this->repo->filterCheckpointIdsBelongingToPeriod($periodId, $data['source_ids']);
            sort($valid);
            $requested = $data['source_ids'];
            sort($requested);
            if ($valid !== $requested) {
                $errors['source_weekly_checkpoint_ids'] = 'All source weekly checkpoint IDs must exist and belong to the parent reporting period.';
            }
        }

        if ($data['owner_user_id'] !== null && !$this->repo->isInternalUser($data['owner_user_id'])) {
            $errors['owner_user_id'] = 'Owner must be an internal user.';
        }

        if ($data['reviewer_user_id'] !== null && !$this->repo->isInternalUser($data['reviewer_user_id'])) {
            $errors['reviewer_user_id'] = 'Reviewer must be an internal user.';
        }

        return $errors;
    }

    private function normalizeJsonCompare(mixed $raw): string
    {
        if ($raw === null || $raw === '') {
            return '';
        }
        if (is_array($raw)) {
            try {
                return json_encode($raw, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR) ?: '';
            } catch (JsonException) {
                return '';
            }
        }
        if (!is_string($raw)) {
            return '';
        }
        $decoded = json_decode($raw, true);
        if (!is_array($decoded)) {
            return trim($raw);
        }
        try {
            return json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR) ?: '';
        } catch (JsonException) {
            return trim($raw);
        }
    }

    private function nullableText(mixed $value): ?string
    {
        if (!is_string($value)) {
            return null;
        }
        $trimmed = trim($value);
        return $trimmed === '' ? null : $trimmed;
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
        $this->db->assertLocalDevDatabase();
    }
}
