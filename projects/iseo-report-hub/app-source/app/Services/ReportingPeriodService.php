<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportingPeriodRepository;
use PDOException;
use Throwable;

/**
 * Reporting period CRUD orchestration — validation, locks, roles, audit.
 */
final class ReportingPeriodService
{
    /** @var list<string> */
    public const STATUSES = [
        'draft',
        'active',
        'weekly_review',
        'monthly_review',
        'finalized',
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

    public function __construct(
        private ReportingPeriodRepository $repo,
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
     * @param array<string, mixed>|null $period
     */
    public function canEdit(?array $user, ?array $period = null): bool
    {
        if ($user === null) {
            return false;
        }

        if ($this->userHasAnyRole($user, self::FULL_EDIT_ROLES)) {
            return true;
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            if ($period === null) {
                return true;
            }
            $status = (string) ($period['status'] ?? '');
            return !in_array($status, ['finalized', 'archived'], true);
        }

        // SAFE SIMPLIFICATION: account_client_manager is read-only in MVP
        // (title/summary-only edit deferred).
        return false;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canSetStatus(?array $user, string $status): bool
    {
        if ($user === null) {
            return false;
        }

        if ($this->userHasAnyRole($user, self::FULL_EDIT_ROLES)) {
            return in_array($status, self::STATUSES, true);
        }

        if ($this->userHasAnyRole($user, self::SPECIALIST_EDIT_ROLES)) {
            return in_array($status, [
                'draft',
                'active',
                'weekly_review',
                'monthly_review',
            ], true);
        }

        return false;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listPeriods(): array
    {
        $this->assertDb();
        return $this->repo->listWithContext();
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getPeriod(int $id): ?array
    {
        $this->assertDb();
        return $this->repo->findById($id);
    }

    public function countPeriods(): int
    {
        $this->assertDb();
        return $this->repo->countAll();
    }

    /**
     * @return list<array{id:int,name:string,slug:string,client_name:string}>
     */
    public function selectableProjects(): array
    {
        $this->assertDb();
        return $this->repo->listSelectableProjects();
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
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $input
     * @return array{ok:bool,id?:int,errors?:array<string,string>,message?:string}
     */
    public function create(array $user, array $input): array
    {
        $this->assertDb();

        if (!$this->canCreate($user)) {
            return ['ok' => false, 'message' => 'You do not have permission to create reporting periods.', 'errors' => []];
        }

        $normalized = $this->normalizeInput($input, null);
        $errors = $this->validateForCreate($normalized, $user);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $finalizedAt = null;
        if ($normalized['status'] === 'finalized') {
            $finalizedAt = date('Y-m-d H:i:s');
        }

        $pdo = $this->repo->pdo();
        try {
            $pdo->beginTransaction();
            $id = $this->repo->insert([
                'project_id' => $normalized['project_id'],
                'period_key' => $normalized['period_key'],
                'period_start' => $normalized['period_start'],
                'period_end' => $normalized['period_end'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'summary' => $normalized['summary'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'created_by' => (int) $user['id'],
                'finalized_at' => $finalizedAt,
            ]);
            $this->repo->insertAudit('reporting_period.created', (int) $user['id'], $id, [
                'id' => $id,
                'project_id' => $normalized['project_id'],
                'period_key' => $normalized['period_key'],
                'status' => $normalized['status'],
            ]);
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
                        'period_key' => 'A reporting period for this project and month already exists.',
                    ],
                    'message' => 'Please correct the form errors.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not create reporting period. Please try again.',
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $existing
     * @param array<string, mixed> $input
     * @return array{ok:bool,errors?:array<string,string>,message?:string}
     */
    public function update(array $user, array $existing, array $input): array
    {
        $this->assertDb();

        if (!$this->canEdit($user, $existing)) {
            return ['ok' => false, 'message' => 'You do not have permission to edit this reporting period.', 'errors' => []];
        }

        $normalized = $this->normalizeInput($input, $existing);
        $errors = $this->validateForUpdate($normalized, $existing, $user);
        if ($errors !== []) {
            return ['ok' => false, 'errors' => $errors, 'message' => 'Please correct the form errors.'];
        }

        $oldStatus = (string) $existing['status'];
        $newStatus = $normalized['status'];
        $finalizedAt = $existing['finalized_at'] !== null && $existing['finalized_at'] !== ''
            ? (string) $existing['finalized_at']
            : null;

        if ($newStatus === 'finalized') {
            if ($finalizedAt === null) {
                $finalizedAt = date('Y-m-d H:i:s');
            }
        } elseif ($oldStatus === 'finalized' && $newStatus !== 'finalized') {
            $finalizedAt = null;
        }

        $changed = [];
        foreach (['period_key', 'period_start', 'period_end', 'status', 'title', 'summary', 'owner_user_id', 'reviewer_user_id'] as $field) {
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
                'period_key' => $normalized['period_key'],
                'period_start' => $normalized['period_start'],
                'period_end' => $normalized['period_end'],
                'status' => $normalized['status'],
                'title' => $normalized['title'],
                'summary' => $normalized['summary'],
                'owner_user_id' => $normalized['owner_user_id'],
                'reviewer_user_id' => $normalized['reviewer_user_id'],
                'updated_by' => (int) $user['id'],
                'finalized_at' => $finalizedAt,
            ]);

            if ($changed !== []) {
                $this->repo->insertAudit('reporting_period.updated', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'changed' => $changed,
                ]);
            }

            if ($oldStatus !== $newStatus) {
                $this->repo->insertAudit('reporting_period.status_changed', (int) $user['id'], (int) $existing['id'], [
                    'id' => (int) $existing['id'],
                    'from' => $oldStatus,
                    'to' => $newStatus,
                ]);
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
                        'period_key' => 'A reporting period for this project and month already exists.',
                    ],
                    'message' => 'Please correct the form errors.',
                ];
            }

            return [
                'ok' => false,
                'errors' => [],
                'message' => 'Could not update reporting period. Please try again.',
            ];
        }
    }

    /**
     * @param array<string, mixed> $input
     * @param array<string, mixed>|null $existing
     * @return array{
     *   project_id:int,
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * }
     */
    public function normalizeInput(array $input, ?array $existing): array
    {
        $projectId = isset($input['project_id']) ? (int) $input['project_id'] : (int) ($existing['project_id'] ?? 0);
        if ($existing !== null) {
            $projectId = (int) $existing['project_id'];
        }

        $periodKey = isset($input['period_key']) && is_string($input['period_key'])
            ? trim($input['period_key'])
            : (string) ($existing['period_key'] ?? '');

        $periodStart = isset($input['period_start']) && is_string($input['period_start'])
            ? trim($input['period_start'])
            : (string) ($existing['period_start'] ?? '');

        $periodEnd = isset($input['period_end']) && is_string($input['period_end'])
            ? trim($input['period_end'])
            : (string) ($existing['period_end'] ?? '');

        $status = isset($input['status']) && is_string($input['status'])
            ? trim($input['status'])
            : (string) ($existing['status'] ?? 'draft');

        $title = isset($input['title']) && is_string($input['title']) ? trim($input['title']) : null;
        if ($title === '') {
            $title = null;
        }

        $summary = isset($input['summary']) && is_string($input['summary']) ? trim($input['summary']) : null;
        if ($summary === '') {
            $summary = null;
        }

        $ownerRaw = $input['owner_user_id'] ?? '';
        $ownerId = ($ownerRaw === '' || $ownerRaw === null) ? null : (int) $ownerRaw;
        if ($ownerId !== null && $ownerId <= 0) {
            $ownerId = null;
        }

        $reviewerRaw = $input['reviewer_user_id'] ?? '';
        $reviewerId = ($reviewerRaw === '' || $reviewerRaw === null) ? null : (int) $reviewerRaw;
        if ($reviewerId !== null && $reviewerId <= 0) {
            $reviewerId = null;
        }

        return [
            'project_id' => $projectId,
            'period_key' => $periodKey,
            'period_start' => $periodStart,
            'period_end' => $periodEnd,
            'status' => $status,
            'title' => $title,
            'summary' => $summary,
            'owner_user_id' => $ownerId,
            'reviewer_user_id' => $reviewerId,
        ];
    }

    /**
     * @param array{
     *   project_id:int,
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForCreate(array $data, array $user): array
    {
        $errors = $this->validateCommon($data);

        if ($data['project_id'] <= 0 || !$this->repo->projectExists($data['project_id'])) {
            $errors['project_id'] = 'Selected project was not found.';
        }

        if (!isset($errors['period_key']) && $data['project_id'] > 0
            && $this->repo->periodKeyExists($data['project_id'], $data['period_key'])) {
            $errors['period_key'] = 'A reporting period for this project and month already exists.';
        }

        if (!$this->canSetStatus($user, $data['status'])) {
            $errors['status'] = 'Invalid status.';
        }

        return $errors;
    }

    /**
     * @param array{
     *   project_id:int,
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @param array<string, mixed> $existing
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array<string, string>
     */
    private function validateForUpdate(array $data, array $existing, array $user): array
    {
        $errors = $this->validateCommon($data);
        $existingStatus = (string) $existing['status'];

        if ($data['period_key'] !== (string) $existing['period_key'] && $existingStatus !== 'draft') {
            $errors['period_key'] = 'Period key can only be changed while draft.';
        }

        $datesChanged = $data['period_start'] !== (string) $existing['period_start']
            || $data['period_end'] !== (string) $existing['period_end'];
        if ($datesChanged && !in_array($existingStatus, ['draft', 'active'], true)) {
            $errors['period_start'] = 'Dates can only be changed while draft or active.';
        }

        if (!isset($errors['period_key'])
            && $this->repo->periodKeyExists((int) $existing['project_id'], $data['period_key'], (int) $existing['id'])) {
            $errors['period_key'] = 'A reporting period for this project and month already exists.';
        }

        if (!$this->canSetStatus($user, $data['status'])) {
            $errors['status'] = 'Invalid status.';
        }

        return $errors;
    }

    /**
     * @param array{
     *   project_id:int,
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int
     * } $data
     * @return array<string, string>
     */
    private function validateCommon(array $data): array
    {
        $errors = [];

        if ($data['period_key'] === '' || !preg_match('/^\d{4}-(0[1-9]|1[0-2])$/', $data['period_key'])) {
            $errors['period_key'] = 'Period key must be YYYY-MM.';
        }

        if ($data['period_start'] === '' || !$this->isValidDate($data['period_start'])) {
            $errors['period_start'] = 'Period start must be a valid date.';
        }

        if ($data['period_end'] === '' || !$this->isValidDate($data['period_end'])) {
            $errors['period_end'] = 'Period end must be a valid date.';
        }

        if (!isset($errors['period_start'], $errors['period_end'])
            && $data['period_start'] !== '' && $data['period_end'] !== ''
            && $data['period_start'] > $data['period_end']) {
            $errors['period_start'] = 'Period start must be on or before period end.';
        }

        if (!isset($errors['period_key'], $errors['period_start'])
            && $data['period_key'] !== '' && $data['period_start'] !== ''
            && substr($data['period_start'], 0, 7) !== $data['period_key']) {
            $errors['period_key'] = 'Period key must match the start month.';
        }

        if (!in_array($data['status'], self::STATUSES, true)) {
            $errors['status'] = 'Invalid status.';
        }

        if ($data['title'] !== null && mb_strlen($data['title']) > 255) {
            $errors['title'] = 'Title is too long (max 255 characters).';
        }

        if ($data['summary'] !== null && mb_strlen($data['summary']) > 10000) {
            $errors['summary'] = 'Summary is too long.';
        }

        if ($data['owner_user_id'] !== null && !$this->repo->isInternalUser($data['owner_user_id'])) {
            $errors['owner_user_id'] = 'Owner/reviewer must be an internal user.';
        }

        if ($data['reviewer_user_id'] !== null && !$this->repo->isInternalUser($data['reviewer_user_id'])) {
            $errors['reviewer_user_id'] = 'Owner/reviewer must be an internal user.';
        }

        return $errors;
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
