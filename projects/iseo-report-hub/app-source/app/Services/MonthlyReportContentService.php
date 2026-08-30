<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Throwable;

/**
 * Monthly report content CRUD — validation, locks, status workflow, audit.
 */
final class MonthlyReportContentService
{
    /** @var list<string> */
    public const STATUSES = [
        'draft',
        'in_progress',
        'ready_for_review',
        'reviewed',
        'finalized',
        'archived',
    ];

    /** @var list<string> */
    private const TEXT_FIELDS = [
        'executive_summary',
        'work_completed',
        'results_summary',
        'key_findings',
        'risks_and_blockers',
        'next_month_plan',
        'client_notes',
        'internal_notes',
    ];

    private const TEXT_MAX_LEN = 20000;

    /** @var list<string> */
    private const CREATE_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    /** @var list<string> */
    private const FULL_EDIT_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    /** Specialists edit work entries, not the raw monthly report form. */
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
        private MonthlyReportContentRepository $repo,
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
     * @param array<string, mixed>|null $report
     */
    public function canEdit(?array $user, ?array $report = null): bool
    {
        if ($user === null) {
            return false;
        }

        if ($this->userHasAnyRole($user, self::FULL_EDIT_ROLES)) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            if ($report === null) {
                return true;
            }
            $status = (string) ($report['status'] ?? '');
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
    public function getByPeriodId(int $periodId): ?array
    {
        $this->assertDb();
        return $this->repo->findByPeriodId($periodId);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getPeriod(int $periodId): ?array
    {
        $this->assertDb();
        return $this->repo->findPeriodById($periodId);
    }

    public function countReports(): int
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
     * Decode source IDs from DB JSON / string / array into list of ints.
     *
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

    public function parentPeriodLockedForNonAdmin(array $period): bool
    {
        $status = (string) ($period['status'] ?? '');
        return in_array($status, ['archived', 'finalized'], true);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $period
     */
    public function canMutateAgainstParent(array $user, array $period): bool
    {
        if (!$this->parentPeriodLockedForNonAdmin($period)) {
            return true;
        }
        return $this->userHasAnyRole($user, ['admin_owner']);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $period
     * @param array<string, mixed> $input
     * @return array{ok:bool,id?:int,errors?:array<string,string>,message?:string,notice?:string}
     */
    public function create(array $user, array $period, array $input): array
    {
        $this->assertDb();

        if (!$this->canCreate($user)) {
            return ['ok' => false, 'message' => 'You do not have permission to create monthly report content.', 'errors' => []];
        }

        if (!$this->canMutateAgainstParent($user, $period)) {
            return [
                'ok' => false,
                'message' => 'Parent reporting period is archived or finalized.',
                'errors' => ['reporting_period_id' => 'Parent period is locked for create.'],
            ];
        }

        if ($this->repo->existsForPeriod((int) $period['id'])) {
            return [
                'ok' => false,
                'message' => 'A monthly report content row already exists for this reporting period.',
                'errors' => ['reporting_period_id' => 'Only one monthly report content row is allowed per reporting period.'],
            ];
        }

        $normalized = $this->normalizeInput($input, null, (int) $period['id']);
        $errors = $this->validateForCreate($normalized, $period, $user);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $reviewedAt = null;
        $finalizedAt = null;
        if ($normalized['status'] === 'reviewed' || $normalized['status'] === 'finalized') {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($normalized['status'] === 'finalized') {
            $finalizedAt = date('Y-m-d H:i:s');
        }

        $pdo = $this->repo->pdo();
        try {
            $pdo->beginTransaction();
            $id = $this->repo->insert([
                'reporting_period_id' => (int) $period['id'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'executive_summary' => $normalized['executive_summary'],
                'work_completed' => $normalized['work_completed'],
                'results_summary' => $normalized['results_summary'],
                'key_findings' => $normalized['key_findings'],
                'risks_and_blockers' => $normalized['risks_and_blockers'],
                'next_month_plan' => $normalized['next_month_plan'],
                'client_notes' => $normalized['client_notes'],
                'internal_notes' => $normalized['internal_notes'],
                'source_weekly_checkpoint_ids' => $normalized['source_weekly_checkpoint_ids_json'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'created_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'finalized_at' => $finalizedAt,
            ]);

            $this->repo->insertAudit('monthly_report_content.created', (int) $user['id'], $id, [
                'id' => $id,
                'reporting_period_id' => (int) $period['id'],
                'status' => $normalized['status'],
            ]);

            if ($normalized['status'] === 'reviewed') {
                $this->repo->insertAudit('monthly_report_content.reviewed', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'reviewed',
                ]);
            }
            if ($normalized['status'] === 'finalized') {
                $this->repo->insertAudit('monthly_report_content.finalized', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'finalized',
                ]);
            }
            if ($normalized['status'] === 'archived') {
                $this->repo->insertAudit('monthly_report_content.archived', (int) $user['id'], $id, [
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
                        'reporting_period_id' => 'Only one monthly report content row is allowed per reporting period.',
                    ],
                    'message' => 'A monthly report content row already exists for this reporting period.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not create monthly report content. Please try again.',
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $period
     * @param array<string, mixed> $input
     * @return array{ok:bool,errors?:array<string,string>,message?:string,notice?:string}
     */
    public function update(array $user, array $existing, array $period, array $input): array
    {
        $this->assertDb();

        if (!$this->canEdit($user, $existing)) {
            return ['ok' => false, 'message' => 'You do not have permission to edit this monthly report.', 'errors' => []];
        }

        if ((string) ($existing['status'] ?? '') === 'finalized') {
            return [
                'ok' => false,
                'message' => 'Monthly report is finalized. Reopen before editing content.',
                'errors' => ['status' => 'Finalized reports are locked for normal edit. Use reopen first.'],
            ];
        }

        if (!$this->canMutateAgainstParent($user, $period)) {
            return [
                'ok' => false,
                'message' => 'Parent reporting period is archived or finalized.',
                'errors' => ['reporting_period_id' => 'Parent period is locked for edit.'],
            ];
        }

        $normalized = $this->normalizeInput($input, $existing, (int) $existing['reporting_period_id']);
        $errors = $this->validateForUpdate($normalized, $existing, $period, $user);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $oldStatus = (string) $existing['status'];
        $newStatus = $normalized['status'];

        $reviewedAt = $existing['reviewed_at'] !== null && $existing['reviewed_at'] !== ''
            ? (string) $existing['reviewed_at']
            : null;
        $finalizedAt = $existing['finalized_at'] !== null && $existing['finalized_at'] !== ''
            ? (string) $existing['finalized_at']
            : null;

        // Keep timestamps as history on reopen (SAFE SIMPLIFICATION).
        if ($newStatus === 'reviewed' && $reviewedAt === null) {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($newStatus === 'finalized' && $finalizedAt === null) {
            $finalizedAt = date('Y-m-d H:i:s');
            if ($reviewedAt === null) {
                $reviewedAt = $finalizedAt;
            }
        }

        $changed = [];
        $trackFields = array_merge(
            ['status', 'title', 'owner_user_id', 'reviewer_user_id', 'source_weekly_checkpoint_ids'],
            self::TEXT_FIELDS
        );
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
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'executive_summary' => $normalized['executive_summary'],
                'work_completed' => $normalized['work_completed'],
                'results_summary' => $normalized['results_summary'],
                'key_findings' => $normalized['key_findings'],
                'risks_and_blockers' => $normalized['risks_and_blockers'],
                'next_month_plan' => $normalized['next_month_plan'],
                'client_notes' => $normalized['client_notes'],
                'internal_notes' => $normalized['internal_notes'],
                'source_weekly_checkpoint_ids' => $normalized['source_weekly_checkpoint_ids_json'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'updated_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'finalized_at' => $finalizedAt,
            ]);

            if ($changed !== []) {
                $this->repo->insertAudit('monthly_report_content.updated', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'reporting_period_id' => (int) $existing['reporting_period_id'],
                    'changed' => $changed,
                ]);
            }

            if ($oldStatus !== $newStatus) {
                $this->repo->insertAudit('monthly_report_content.status_changed', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'from' => $oldStatus,
                    'to' => $newStatus,
                ]);
                if ($newStatus === 'reviewed') {
                    $this->repo->insertAudit('monthly_report_content.reviewed', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'reviewed',
                    ]);
                }
                if ($newStatus === 'finalized') {
                    $this->repo->insertAudit('monthly_report_content.finalized', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'finalized',
                    ]);
                }
                if ($newStatus === 'archived') {
                    $this->repo->insertAudit('monthly_report_content.archived', (int) $user['id'], (int) $existing['id'], [
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
        } catch (Throwable) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not update monthly report content. Please try again.',
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

        // Finalized reopen / finalize must use explicit finalization routes.
        if ($from === 'finalized' || $to === 'finalized') {
            return false;
        }

        $forward = [
            'draft' => ['in_progress'],
            'in_progress' => ['ready_for_review'],
            'ready_for_review' => ['reviewed'],
            'reviewed' => [],
        ];

        if (isset($forward[$from]) && in_array($to, $forward[$from], true)) {
            return true;
        }

        // any non-finalized → archived
        if ($from !== 'finalized' && $to === 'archived') {
            return true;
        }

        // reopen archived by admin_owner
        if ($from === 'archived' && $this->userHasAnyRole($user, ['admin_owner'])) {
            return true;
        }

        return false;
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{
     *   reporting_period_id:int,
     *   status:string,
     *   title:string,
     *   executive_summary:?string,
     *   work_completed:?string,
     *   results_summary:?string,
     *   key_findings:?string,
     *   risks_and_blockers:?string,
     *   next_month_plan:?string,
     *   client_notes:?string,
     *   internal_notes:?string,
     *   source_ids:list<int>,
     *   source_weekly_checkpoint_ids_json:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * }
     */
    public function normalizeInput(array $input, ?array $existing, int $periodId): array
    {
        $status = isset($input['status']) && is_string($input['status'])
            ? trim($input['status'])
            : (string) ($existing['status'] ?? 'draft');

        $title = isset($input['title']) && is_string($input['title']) ? trim($input['title']) : '';
        if ($existing !== null && $title === '' && isset($existing['title'])) {
            $title = (string) $existing['title'];
        }

        $texts = [];
        foreach (self::TEXT_FIELDS as $field) {
            if (array_key_exists($field, $input)) {
                $texts[$field] = $this->nullableText($input[$field] ?? null);
            } elseif ($existing !== null) {
                $texts[$field] = $this->nullableText($existing[$field] ?? null);
            } else {
                $texts[$field] = null;
            }
        }

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

        $json = null;
        if ($sourceIds !== []) {
            $json = json_encode(array_values($sourceIds), JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
        }

        return [
            'reporting_period_id' => $periodId,
            'status' => $status,
            'title' => $title,
            'executive_summary' => $texts['executive_summary'],
            'work_completed' => $texts['work_completed'],
            'results_summary' => $texts['results_summary'],
            'key_findings' => $texts['key_findings'],
            'risks_and_blockers' => $texts['risks_and_blockers'],
            'next_month_plan' => $texts['next_month_plan'],
            'client_notes' => $texts['client_notes'],
            'internal_notes' => $texts['internal_notes'],
            'source_ids' => $sourceIds,
            'source_weekly_checkpoint_ids_json' => $json,
            'owner_user_id' => $ownerId,
            'reviewer_user_id' => $reviewerId,
        ];
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
                // Allow JSON string or comma-separated.
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
     * @param array{
     *   reporting_period_id:int,
     *   status:string,
     *   title:string,
     *   executive_summary:?string,
     *   work_completed:?string,
     *   results_summary:?string,
     *   key_findings:?string,
     *   risks_and_blockers:?string,
     *   next_month_plan:?string,
     *   client_notes:?string,
     *   internal_notes:?string,
     *   source_ids:list<int>,
     *   source_weekly_checkpoint_ids_json:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array<string, mixed> $period
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForCreate(array $data, array $period, array $user): array
    {
        $errors = $this->validateCommon($data, $period);

        if (!$this->canSetStatus($user, $data['status'])) {
            $errors['status'] = 'Invalid status for your role.';
        }

        return $errors;
    }

    /**
     * @param array{
     *   reporting_period_id:int,
     *   status:string,
     *   title:string,
     *   executive_summary:?string,
     *   work_completed:?string,
     *   results_summary:?string,
     *   key_findings:?string,
     *   risks_and_blockers:?string,
     *   next_month_plan:?string,
     *   client_notes:?string,
     *   internal_notes:?string,
     *   source_ids:list<int>,
     *   source_weekly_checkpoint_ids_json:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $period
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForUpdate(array $data, array $existing, array $period, array $user): array
    {
        $errors = $this->validateCommon($data, $period);
        $existingStatus = (string) $existing['status'];

        // Finalized content is locked for all roles until reopen.
        if ($existingStatus === 'finalized') {
            $errors['status'] = 'Finalized reports are locked. Use reopen first.';
            return $errors;
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
     * @param array{
     *   reporting_period_id:int,
     *   status:string,
     *   title:string,
     *   executive_summary:?string,
     *   work_completed:?string,
     *   results_summary:?string,
     *   key_findings:?string,
     *   risks_and_blockers:?string,
     *   next_month_plan:?string,
     *   client_notes:?string,
     *   internal_notes:?string,
     *   source_ids:list<int>,
     *   source_weekly_checkpoint_ids_json:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array<string, mixed> $period
     * @return array<string, string>
     */
    private function validateCommon(array $data, array $period): array
    {
        $errors = [];

        if (!in_array($data['status'], self::STATUSES, true)) {
            $errors['status'] = 'Invalid status.';
        }

        if ($data['title'] === '') {
            $errors['title'] = 'Title is required.';
        } elseif (mb_strlen($data['title']) > 255) {
            $errors['title'] = 'Title is too long (max 255 characters).';
        }

        foreach (self::TEXT_FIELDS as $field) {
            $value = $data[$field] ?? null;
            if ($value !== null && mb_strlen($value) > self::TEXT_MAX_LEN) {
                $errors[$field] = ucfirst(str_replace('_', ' ', $field)) . ' is too long (max ' . self::TEXT_MAX_LEN . ' characters).';
            }
        }

        if ($data['source_ids'] !== []) {
            $valid = $this->repo->filterCheckpointIdsBelongingToPeriod(
                (int) $period['id'],
                $data['source_ids']
            );
            sort($valid);
            $requested = $data['source_ids'];
            sort($requested);
            if ($valid !== $requested) {
                $errors['source_weekly_checkpoint_ids'] = 'All source weekly checkpoint IDs must exist and belong to this reporting period.';
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
