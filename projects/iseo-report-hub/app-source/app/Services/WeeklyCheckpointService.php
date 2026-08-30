<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\WeeklyCheckpointRepository;
use Throwable;

/**
 * Weekly checkpoint CRUD — validation, locks, status workflow, audit.
 */
final class WeeklyCheckpointService
{
    /** @var list<string> */
    public const STATUSES = [
        'draft',
        'in_progress',
        'ready_for_review',
        'reviewed',
        'completed',
        'skipped',
        'archived',
    ];

    /** @var list<string> */
    private const CREATE_ROLES = ['admin_owner', 'seo_lead_reviewer', 'seo_specialist'];

    /** @var list<string> */
    private const FULL_EDIT_ROLES = ['admin_owner', 'seo_lead_reviewer'];

    /** @var list<string> */
    private const SPECIALIST_EDIT_ROLES = ['seo_specialist'];

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
        private WeeklyCheckpointRepository $repo,
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
     * @param array<string, mixed>|null $checkpoint
     * @param array<string, mixed>|null $period
     */
    public function canEdit(?array $user, ?array $checkpoint = null, ?array $period = null): bool
    {
        if ($user === null) {
            return false;
        }

        if ($this->userHasAnyRole($user, self::FULL_EDIT_ROLES)) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            if ($checkpoint === null) {
                return true;
            }
            $status = (string) ($checkpoint['status'] ?? '');
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
     * Whether user may set a target status (role gate only — transitions checked separately).
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canSetStatus(?array $user, string $status, ?string $fromStatus = null): bool
    {
        if ($user === null || !in_array($status, self::STATUSES, true)) {
            return false;
        }

        if ($this->userHasAnyRole($user, ['admin_owner'])) {
            return true;
        }

        if ($this->userHasAnyRole($user, ['seo_lead_reviewer'])) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            // Specialist: draft/in_progress/ready_for_review only; no reviewed/completed/skipped/archived.
            return in_array($status, ['draft', 'in_progress', 'ready_for_review'], true);
        }

        return false;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listForPeriod(int $periodId): array
    {
        $this->assertDb();
        return $this->repo->listByPeriodId($periodId);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getCheckpoint(int $id): ?array
    {
        $this->assertDb();
        return $this->repo->findById($id);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getPeriod(int $periodId): ?array
    {
        $this->assertDb();
        return $this->repo->findPeriodById($periodId);
    }

    public function countCheckpoints(): int
    {
        $this->assertDb();
        return $this->repo->countAll();
    }

    /**
     * @return list<array{id:int,name:string,email:string}>
     */
    public function selectableInternalUsers(): array
    {
        $this->assertDb();
        return $this->repo->listInternalUsers();
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
     * @return array{ok:bool,id?:int,errors?:array<string,string>,message?:string}
     */
    public function create(array $user, array $period, array $input): array
    {
        $this->assertDb();

        if (!$this->canCreate($user)) {
            return ['ok' => false, 'message' => 'You do not have permission to create weekly checkpoints.', 'errors' => []];
        }

        if (!$this->canMutateAgainstParent($user, $period)) {
            return [
                'ok' => false,
                'message' => 'Parent reporting period is archived or finalized.',
                'errors' => ['reporting_period_id' => 'Parent period is locked for create.'],
            ];
        }

        $normalized = $this->normalizeInput($input, null, (int) $period['id']);
        $errors = $this->validateForCreate($normalized, $period, $user);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $reviewedAt = null;
        $completedAt = null;
        if ($normalized['status'] === 'reviewed') {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($normalized['status'] === 'completed') {
            $completedAt = date('Y-m-d H:i:s');
            if ($reviewedAt === null) {
                $reviewedAt = $completedAt;
            }
        }

        $pdo = $this->repo->pdo();
        try {
            $pdo->beginTransaction();
            $id = $this->repo->insert([
                'reporting_period_id' => (int) $period['id'],
                'week_index' => $normalized['week_index'],
                'checkpoint_key' => $normalized['checkpoint_key'],
                'checkpoint_start' => $normalized['checkpoint_start'],
                'checkpoint_end' => $normalized['checkpoint_end'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'summary' => $normalized['summary'],
                'work_done' => $normalized['work_done'],
                'findings' => $normalized['findings'],
                'next_steps' => $normalized['next_steps'],
                'risks' => $normalized['risks'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'created_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'completed_at' => $completedAt,
            ]);

            $this->repo->insertAudit('weekly_checkpoint.created', (int) $user['id'], $id, [
                'id' => $id,
                'reporting_period_id' => (int) $period['id'],
                'checkpoint_key' => $normalized['checkpoint_key'],
                'week_index' => $normalized['week_index'],
                'status' => $normalized['status'],
            ]);

            if ($normalized['status'] === 'reviewed') {
                $this->repo->insertAudit('weekly_checkpoint.reviewed', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'reviewed',
                ]);
            }
            if ($normalized['status'] === 'completed') {
                $this->repo->insertAudit('weekly_checkpoint.completed', (int) $user['id'], $id, [
                    'id' => $id,
                    'status' => 'completed',
                ]);
            }

            $pdo->commit();
            return ['ok' => true, 'id' => $id];
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            if ($this->repo->isUniqueViolation($e)) {
                return [
                    'ok' => false,
                    'errors' => [
                        'week_index' => 'A weekly checkpoint for this period and week/key already exists.',
                        'checkpoint_key' => 'A weekly checkpoint for this period and week/key already exists.',
                    ],
                    'message' => 'Please correct the form errors.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not create weekly checkpoint. Please try again.',
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $period
     * @param array<string, mixed> $input
     * @return array{ok:bool,errors?:array<string,string>,message?:string}
     */
    public function update(array $user, array $existing, array $period, array $input): array
    {
        $this->assertDb();

        if (!$this->canEdit($user, $existing, $period)) {
            return ['ok' => false, 'message' => 'You do not have permission to edit this weekly checkpoint.', 'errors' => []];
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
        $completedAt = $existing['completed_at'] !== null && $existing['completed_at'] !== ''
            ? (string) $existing['completed_at']
            : null;

        // Keep timestamps as history on reopen (SAFE SIMPLIFICATION documented).
        if ($newStatus === 'reviewed' && $reviewedAt === null) {
            $reviewedAt = date('Y-m-d H:i:s');
        }
        if ($newStatus === 'completed' && $completedAt === null) {
            $completedAt = date('Y-m-d H:i:s');
            if ($reviewedAt === null) {
                $reviewedAt = $completedAt;
            }
        }

        $changed = [];
        $trackFields = [
            'week_index', 'checkpoint_key', 'checkpoint_start', 'checkpoint_end', 'status',
            'title', 'summary', 'work_done', 'findings', 'next_steps', 'risks',
            'owner_user_id', 'reviewer_user_id',
        ];
        foreach ($trackFields as $field) {
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
                'week_index' => $normalized['week_index'],
                'checkpoint_key' => $normalized['checkpoint_key'],
                'checkpoint_start' => $normalized['checkpoint_start'],
                'checkpoint_end' => $normalized['checkpoint_end'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'summary' => $normalized['summary'],
                'work_done' => $normalized['work_done'],
                'findings' => $normalized['findings'],
                'next_steps' => $normalized['next_steps'],
                'risks' => $normalized['risks'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'updated_by' => (int) $user['id'],
                'reviewed_at' => $reviewedAt,
                'completed_at' => $completedAt,
            ]);

            if ($changed !== []) {
                $this->repo->insertAudit('weekly_checkpoint.updated', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'reporting_period_id' => (int) $existing['reporting_period_id'],
                    'changed' => $changed,
                ]);
            }

            if ($oldStatus !== $newStatus) {
                $this->repo->insertAudit('weekly_checkpoint.status_changed', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'from' => $oldStatus,
                    'to' => $newStatus,
                ]);
                if ($newStatus === 'reviewed') {
                    $this->repo->insertAudit('weekly_checkpoint.reviewed', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'reviewed',
                    ]);
                }
                if ($newStatus === 'completed') {
                    $this->repo->insertAudit('weekly_checkpoint.completed', (int) $user['id'], (int) $existing['id'], [
                        'id' => (int) $existing['id'],
                        'status' => 'completed',
                    ]);
                }
            }

            $pdo->commit();
            return ['ok' => true];
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            if ($this->repo->isUniqueViolation($e)) {
                return [
                    'ok' => false,
                    'errors' => [
                        'week_index' => 'A weekly checkpoint for this period and week/key already exists.',
                        'checkpoint_key' => 'A weekly checkpoint for this period and week/key already exists.',
                    ],
                    'message' => 'Please correct the form errors.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not update weekly checkpoint. Please try again.',
            ];
        }
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{
     *   reporting_period_id:int,
     *   week_index:int,
     *   checkpoint_key:string,
     *   checkpoint_start:string,
     *   checkpoint_end:string,
     *   status:string,
     *   title:string,
     *   summary:?string,
     *   work_done:?string,
     *   findings:?string,
     *   next_steps:?string,
     *   risks:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * }
     */
    public function normalizeInput(array $input, ?array $existing, int $periodId): array
    {
        $weekRaw = $input['week_index'] ?? ($existing['week_index'] ?? 0);
        $weekIndex = (int) $weekRaw;

        $key = isset($input['checkpoint_key']) && is_string($input['checkpoint_key'])
            ? trim($input['checkpoint_key'])
            : (string) ($existing['checkpoint_key'] ?? '');

        $start = isset($input['checkpoint_start']) && is_string($input['checkpoint_start'])
            ? trim($input['checkpoint_start'])
            : (string) ($existing['checkpoint_start'] ?? '');

        $end = isset($input['checkpoint_end']) && is_string($input['checkpoint_end'])
            ? trim($input['checkpoint_end'])
            : (string) ($existing['checkpoint_end'] ?? '');

        $status = isset($input['status']) && is_string($input['status'])
            ? trim($input['status'])
            : (string) ($existing['status'] ?? 'draft');

        $title = isset($input['title']) && is_string($input['title']) ? trim($input['title']) : '';
        if ($existing !== null && $title === '' && isset($existing['title'])) {
            $title = (string) $existing['title'];
        }

        $summary = $this->nullableText($input['summary'] ?? null);
        $workDone = $this->nullableText($input['work_done'] ?? null);
        $findings = $this->nullableText($input['findings'] ?? null);
        $nextSteps = $this->nullableText($input['next_steps'] ?? null);
        $risks = $this->nullableText($input['risks'] ?? null);

        if ($existing !== null) {
            if (!array_key_exists('summary', $input)) {
                $summary = $this->nullableText($existing['summary'] ?? null);
            }
            if (!array_key_exists('work_done', $input)) {
                $workDone = $this->nullableText($existing['work_done'] ?? null);
            }
            if (!array_key_exists('findings', $input)) {
                $findings = $this->nullableText($existing['findings'] ?? null);
            }
            if (!array_key_exists('next_steps', $input)) {
                $nextSteps = $this->nullableText($existing['next_steps'] ?? null);
            }
            if (!array_key_exists('risks', $input)) {
                $risks = $this->nullableText($existing['risks'] ?? null);
            }
        }

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

        return [
            'reporting_period_id' => $periodId,
            'week_index' => $weekIndex,
            'checkpoint_key' => $key,
            'checkpoint_start' => $start,
            'checkpoint_end' => $end,
            'status' => $status,
            'title' => $title,
            'summary' => $summary,
            'work_done' => $workDone,
            'findings' => $findings,
            'next_steps' => $nextSteps,
            'risks' => $risks,
            'owner_user_id' => $ownerId,
            'reviewer_user_id' => $reviewerId,
        ];
    }

    /**
     * Allowed status options for forms given current user + existing status.
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return list<string>
     */
    public function allowedStatusesForForm(array $user, ?string $fromStatus): array
    {
        $out = [];
        foreach (self::STATUSES as $status) {
            if ($fromStatus === null || $fromStatus === $status) {
                if ($this->canSetStatus($user, $status, $fromStatus)) {
                    $out[] = $status;
                }
                continue;
            }
            if ($this->isTransitionAllowed($fromStatus, $status, $user)
                && $this->canSetStatus($user, $status, $fromStatus)) {
                $out[] = $status;
            }
        }
        // Always include current status so the select can render.
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
            'reviewed' => ['completed'],
        ];

        if (isset($forward[$from]) && in_array($to, $forward[$from], true)) {
            return true;
        }

        // any non-completed → skipped / archived
        if ($from !== 'completed' && in_array($to, ['skipped', 'archived'], true)) {
            return true;
        }

        // reopen reviewed/completed only by admin_owner
        if (in_array($from, ['reviewed', 'completed'], true)
            && $this->userHasAnyRole($user, ['admin_owner'])) {
            return true;
        }

        return false;
    }

    /**
     * @param array{
     *   reporting_period_id:int,
     *   week_index:int,
     *   checkpoint_key:string,
     *   checkpoint_start:string,
     *   checkpoint_end:string,
     *   status:string,
     *   title:string,
     *   summary:?string,
     *   work_done:?string,
     *   findings:?string,
     *   next_steps:?string,
     *   risks:?string,
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

        if (!isset($errors['week_index'])
            && $this->repo->weekIndexExists((int) $period['id'], $data['week_index'])) {
            $errors['week_index'] = 'A weekly checkpoint for this week index already exists in the period.';
        }

        if (!isset($errors['checkpoint_key'])
            && $this->repo->checkpointKeyExists((int) $period['id'], $data['checkpoint_key'])) {
            $errors['checkpoint_key'] = 'A weekly checkpoint with this key already exists in the period.';
        }

        if (!$this->canSetStatus($user, $data['status'], null)) {
            $errors['status'] = 'Invalid status for your role.';
        }

        return $errors;
    }

    /**
     * @param array{
     *   reporting_period_id:int,
     *   week_index:int,
     *   checkpoint_key:string,
     *   checkpoint_start:string,
     *   checkpoint_end:string,
     *   status:string,
     *   title:string,
     *   summary:?string,
     *   work_done:?string,
     *   findings:?string,
     *   next_steps:?string,
     *   risks:?string,
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
        $isAdmin = $this->userHasAnyRole($user, ['admin_owner']);

        if ($data['week_index'] !== (int) $existing['week_index'] && $existingStatus !== 'draft') {
            $errors['week_index'] = 'Week index can only be changed while draft.';
        }

        if ($data['checkpoint_key'] !== (string) $existing['checkpoint_key'] && $existingStatus !== 'draft') {
            $errors['checkpoint_key'] = 'Checkpoint key can only be changed while draft.';
        }

        $datesChanged = $data['checkpoint_start'] !== (string) $existing['checkpoint_start']
            || $data['checkpoint_end'] !== (string) $existing['checkpoint_end'];
        if ($datesChanged && !in_array($existingStatus, ['draft', 'in_progress'], true)) {
            $errors['checkpoint_start'] = 'Dates can only be changed while draft or in_progress.';
        }

        // Text fields on completed: admin_owner only
        if ($existingStatus === 'completed' && !$isAdmin) {
            foreach (['title', 'summary', 'work_done', 'findings', 'next_steps', 'risks'] as $field) {
                $old = (string) ($existing[$field] ?? '');
                $new = (string) ($data[$field] ?? '');
                if ($old !== $new) {
                    $errors[$field] = 'Completed checkpoint text fields can only be edited by admin_owner.';
                }
            }
        }

        // Owner/reviewer assign roles
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

        if (!isset($errors['week_index'])
            && $this->repo->weekIndexExists((int) $period['id'], $data['week_index'], (int) $existing['id'])) {
            $errors['week_index'] = 'A weekly checkpoint for this week index already exists in the period.';
        }

        if (!isset($errors['checkpoint_key'])
            && $this->repo->checkpointKeyExists((int) $period['id'], $data['checkpoint_key'], (int) $existing['id'])) {
            $errors['checkpoint_key'] = 'A weekly checkpoint with this key already exists in the period.';
        }

        if ($data['status'] !== $existingStatus) {
            if (!$this->isTransitionAllowed($existingStatus, $data['status'], $user)) {
                $errors['status'] = 'Status transition is not allowed.';
            } elseif (!$this->canSetStatus($user, $data['status'], $existingStatus)) {
                $errors['status'] = 'Invalid status for your role.';
            }
        }

        return $errors;
    }

    /**
     * @param array{
     *   reporting_period_id:int,
     *   week_index:int,
     *   checkpoint_key:string,
     *   checkpoint_start:string,
     *   checkpoint_end:string,
     *   status:string,
     *   title:string,
     *   summary:?string,
     *   work_done:?string,
     *   findings:?string,
     *   next_steps:?string,
     *   risks:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array<string, mixed> $period
     * @return array<string, string>
     */
    private function validateCommon(array $data, array $period): array
    {
        $errors = [];

        if ($data['week_index'] < 1 || $data['week_index'] > 6) {
            $errors['week_index'] = 'Week index must be between 1 and 6.';
        }

        if ($data['checkpoint_key'] === '' || mb_strlen($data['checkpoint_key']) > 32) {
            $errors['checkpoint_key'] = 'Checkpoint key is required (max 32 characters).';
        } elseif (!preg_match('/^\d{4}-(0[1-9]|1[0-2])-W[1-6]$/', $data['checkpoint_key'])) {
            $errors['checkpoint_key'] = 'Checkpoint key must match YYYY-MM-WN.';
        } else {
            $periodPart = substr($data['checkpoint_key'], 0, 7);
            if ($periodPart !== (string) $period['period_key']) {
                $errors['checkpoint_key'] = 'Checkpoint key period part must match parent period_key.';
            }
            $weekFromKey = (int) substr($data['checkpoint_key'], -1);
            if (!isset($errors['week_index']) && $weekFromKey !== $data['week_index']) {
                $errors['checkpoint_key'] = 'Checkpoint key week number must match week_index.';
            }
        }

        if ($data['checkpoint_start'] === '' || !$this->isValidDate($data['checkpoint_start'])) {
            $errors['checkpoint_start'] = 'Checkpoint start must be a valid date.';
        }

        if ($data['checkpoint_end'] === '' || !$this->isValidDate($data['checkpoint_end'])) {
            $errors['checkpoint_end'] = 'Checkpoint end must be a valid date.';
        }

        if (!isset($errors['checkpoint_start'], $errors['checkpoint_end'])
            && $data['checkpoint_start'] !== '' && $data['checkpoint_end'] !== ''
            && $data['checkpoint_start'] > $data['checkpoint_end']) {
            $errors['checkpoint_start'] = 'Checkpoint start must be on or before checkpoint end.';
        }

        $periodStart = (string) $period['period_start'];
        $periodEnd = (string) $period['period_end'];
        if (!isset($errors['checkpoint_start']) && $data['checkpoint_start'] !== ''
            && ($data['checkpoint_start'] < $periodStart || $data['checkpoint_start'] > $periodEnd)) {
            $errors['checkpoint_start'] = 'Checkpoint start must be inside the parent period date range.';
        }
        if (!isset($errors['checkpoint_end']) && $data['checkpoint_end'] !== ''
            && ($data['checkpoint_end'] < $periodStart || $data['checkpoint_end'] > $periodEnd)) {
            $errors['checkpoint_end'] = 'Checkpoint end must be inside the parent period date range.';
        }

        if (!in_array($data['status'], self::STATUSES, true)) {
            $errors['status'] = 'Invalid status.';
        }

        if ($data['title'] === '') {
            $errors['title'] = 'Title is required.';
        } elseif (mb_strlen($data['title']) > 255) {
            $errors['title'] = 'Title is too long (max 255 characters).';
        }

        foreach (['summary' => $data['summary'], 'work_done' => $data['work_done'], 'findings' => $data['findings'], 'next_steps' => $data['next_steps'], 'risks' => $data['risks']] as $field => $value) {
            if ($value !== null && mb_strlen($value) > 10000) {
                $errors[$field] = ucfirst(str_replace('_', ' ', $field)) . ' is too long.';
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

    private function isValidDate(string $value): bool
    {
        if (!preg_match('/^\d{4}-\d{2}-\d{2}$/', $value)) {
            return false;
        }
        [$y, $m, $d] = array_map('intval', explode('-', $value));
        return checkdate($m, $d, $y);
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
