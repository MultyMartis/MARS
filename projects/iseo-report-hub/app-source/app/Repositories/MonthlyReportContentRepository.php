<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use PDOException;
use Throwable;

/**
 * PDO access for monthly_report_contents — local MVP only.
 */
final class MonthlyReportContentRepository
{
    /** @var list<string> */
    public const INTERNAL_ROLE_CODES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    public function __construct(
        private DatabaseService $db
    ) {
    }

    public function pdo(): PDO
    {
        return $this->db->connect();
    }

    public function countAll(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM monthly_report_contents')->fetchColumn();
    }

    public function existsForPeriod(int $periodId, ?int $excludeId = null): bool
    {
        if ($periodId <= 0) {
            return false;
        }

        $sql = 'SELECT 1 FROM monthly_report_contents WHERE reporting_period_id = :period_id';
        $params = [':period_id' => $periodId];
        if ($excludeId !== null && $excludeId > 0) {
            $sql .= ' AND id <> :exclude_id';
            $params[':exclude_id'] = $excludeId;
        }
        $sql .= ' LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute($params);
        return (bool) $stmt->fetchColumn();
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE mrc.id = :id LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findByPeriodId(int $periodId): ?array
    {
        if ($periodId <= 0) {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE mrc.reporting_period_id = :period_id LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':period_id' => $periodId]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findPeriodById(int $periodId): ?array
    {
        if ($periodId <= 0) {
            return null;
        }

        $sql = <<<'SQL'
SELECT
    rp.id,
    rp.project_id,
    rp.period_key,
    rp.period_start,
    rp.period_end,
    rp.status,
    rp.title,
    rp.summary,
    p.name AS project_name,
    p.slug AS project_slug,
    c.id AS client_id,
    c.name AS client_name,
    c.slug AS client_slug
FROM reporting_periods rp
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
WHERE rp.id = :id
LIMIT 1
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $periodId]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listWeeklyCheckpointsForPeriod(int $periodId): array
    {
        if ($periodId <= 0) {
            return [];
        }

        $sql = <<<'SQL'
SELECT
    wc.id,
    wc.reporting_period_id,
    wc.week_index,
    wc.checkpoint_key,
    wc.status,
    wc.title
FROM weekly_checkpoints wc
WHERE wc.reporting_period_id = :period_id
ORDER BY wc.week_index ASC, wc.id ASC
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':period_id' => $periodId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @param list<int> $ids
     * @return list<int>
     */
    public function filterCheckpointIdsBelongingToPeriod(int $periodId, array $ids): array
    {
        if ($periodId <= 0 || $ids === []) {
            return [];
        }

        $placeholders = implode(',', array_fill(0, count($ids), '?'));
        $sql = "SELECT id FROM weekly_checkpoints WHERE reporting_period_id = ? AND id IN ({$placeholders})";
        $params = array_merge([$periodId], $ids);
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute($params);
        $rows = $stmt->fetchAll(PDO::FETCH_COLUMN);
        if (!is_array($rows)) {
            return [];
        }
        $out = [];
        foreach ($rows as $id) {
            $out[] = (int) $id;
        }
        return $out;
    }

    /**
     * @return list<array{id:int,name:string,email:string}>
     */
    public function listInternalUsers(): array
    {
        $placeholders = implode(',', array_fill(0, count(self::INTERNAL_ROLE_CODES), '?'));
        $sql = <<<SQL
SELECT DISTINCT u.id, u.name, u.email
FROM users u
INNER JOIN user_roles ur ON ur.user_id = u.id
INNER JOIN roles r ON r.id = ur.role_id
WHERE u.status = 'active'
  AND r.code IN ({$placeholders})
ORDER BY u.name ASC, u.email ASC
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute(self::INTERNAL_ROLE_CODES);
        $rows = $stmt->fetchAll();
        $out = [];
        foreach ($rows as $row) {
            if (!is_array($row)) {
                continue;
            }
            $out[] = [
                'id' => (int) $row['id'],
                'name' => (string) $row['name'],
                'email' => (string) $row['email'],
            ];
        }
        return $out;
    }

    public function isInternalUser(int $userId): bool
    {
        if ($userId <= 0) {
            return false;
        }
        $placeholders = implode(',', array_fill(0, count(self::INTERNAL_ROLE_CODES), '?'));
        $sql = <<<SQL
SELECT 1
FROM users u
INNER JOIN user_roles ur ON ur.user_id = u.id
INNER JOIN roles r ON r.id = ur.role_id
WHERE u.id = ?
  AND u.status = 'active'
  AND r.code IN ({$placeholders})
LIMIT 1
SQL;
        $params = array_merge([$userId], self::INTERNAL_ROLE_CODES);
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute($params);
        return (bool) $stmt->fetchColumn();
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
     *   source_weekly_checkpoint_ids:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   created_by:int,
     *   reviewed_at:?string,
     *   finalized_at:?string
     * } $data
     */
    public function insert(array $data): int
    {
        $sql = <<<'SQL'
INSERT INTO monthly_report_contents (
    reporting_period_id, status, title,
    executive_summary, work_completed, results_summary, key_findings,
    risks_and_blockers, next_month_plan, client_notes, internal_notes,
    source_weekly_checkpoint_ids, owner_user_id, reviewer_user_id,
    created_by, updated_by, reviewed_at, finalized_at
) VALUES (
    :reporting_period_id, :status, :title,
    :executive_summary, :work_completed, :results_summary, :key_findings,
    :risks_and_blockers, :next_month_plan, :client_notes, :internal_notes,
    CAST(:source_weekly_checkpoint_ids AS JSON), :owner_user_id, :reviewer_user_id,
    :created_by, NULL, :reviewed_at, :finalized_at
)
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':reporting_period_id' => $data['reporting_period_id'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':executive_summary' => $data['executive_summary'],
            ':work_completed' => $data['work_completed'],
            ':results_summary' => $data['results_summary'],
            ':key_findings' => $data['key_findings'],
            ':risks_and_blockers' => $data['risks_and_blockers'],
            ':next_month_plan' => $data['next_month_plan'],
            ':client_notes' => $data['client_notes'],
            ':internal_notes' => $data['internal_notes'],
            ':source_weekly_checkpoint_ids' => $data['source_weekly_checkpoint_ids'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':created_by' => $data['created_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':finalized_at' => $data['finalized_at'],
        ]);

        return (int) $this->pdo()->lastInsertId();
    }

    /**
     * Lifecycle-only update for finalization workflow (status / timestamps).
     */
    public function updateLifecycle(
        int $id,
        string $status,
        ?string $reviewedAt,
        ?string $finalizedAt,
        int $updatedBy
    ): void {
        $sql = <<<'SQL'
UPDATE monthly_report_contents SET
    status = :status,
    updated_by = :updated_by,
    reviewed_at = :reviewed_at,
    finalized_at = :finalized_at
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':status' => $status,
            ':updated_by' => $updatedBy,
            ':reviewed_at' => $reviewedAt,
            ':finalized_at' => $finalizedAt,
            ':id' => $id,
        ]);
    }

    /**
     * @param array{
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
     *   source_weekly_checkpoint_ids:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   updated_by:int,
     *   reviewed_at:?string,
     *   finalized_at:?string
     * } $data
     */
    public function update(int $id, array $data): void
    {
        $sql = <<<'SQL'
UPDATE monthly_report_contents SET
    status = :status,
    title = :title,
    executive_summary = :executive_summary,
    work_completed = :work_completed,
    results_summary = :results_summary,
    key_findings = :key_findings,
    risks_and_blockers = :risks_and_blockers,
    next_month_plan = :next_month_plan,
    client_notes = :client_notes,
    internal_notes = :internal_notes,
    source_weekly_checkpoint_ids = CAST(:source_weekly_checkpoint_ids AS JSON),
    owner_user_id = :owner_user_id,
    reviewer_user_id = :reviewer_user_id,
    updated_by = :updated_by,
    reviewed_at = :reviewed_at,
    finalized_at = :finalized_at
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':executive_summary' => $data['executive_summary'],
            ':work_completed' => $data['work_completed'],
            ':results_summary' => $data['results_summary'],
            ':key_findings' => $data['key_findings'],
            ':risks_and_blockers' => $data['risks_and_blockers'],
            ':next_month_plan' => $data['next_month_plan'],
            ':client_notes' => $data['client_notes'],
            ':internal_notes' => $data['internal_notes'],
            ':source_weekly_checkpoint_ids' => $data['source_weekly_checkpoint_ids'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':updated_by' => $data['updated_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':finalized_at' => $data['finalized_at'],
            ':id' => $id,
        ]);
    }

    /**
     * Narrow flat-column mirror for specialist content workflow.
     * Only allowlisted section columns may be updated.
     */
    public function updateFlatSectionText(int $id, string $sectionKey, string $text, int $updatedBy): void
    {
        $allowed = [
            'executive_summary',
            'work_completed',
            'results_summary',
            'key_findings',
            'risks_and_blockers',
            'next_month_plan',
        ];
        if (!in_array($sectionKey, $allowed, true)) {
            throw new \InvalidArgumentException('Unsupported flat section key.');
        }

        $sql = "UPDATE monthly_report_contents SET `{$sectionKey}` = :text, updated_by = :updated_by WHERE id = :id";
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':text' => $text,
            ':updated_by' => $updatedBy,
            ':id' => $id,
        ]);
    }

    /**
     * @param array<string, mixed>|null $metadata
     */
    public function insertAudit(
        string $eventType,
        ?int $actorUserId,
        ?int $entityId,
        ?array $metadata = null
    ): void {
        try {
            if (is_array($metadata)) {
                unset($metadata['password'], $metadata['password_hash'], $metadata['hash']);
            }

            $metaJson = null;
            if (is_array($metadata) && $metadata !== []) {
                $metaJson = json_encode($metadata, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
            }

            $stmt = $this->pdo()->prepare(
                'INSERT INTO audit_log
                    (actor_user_id, event_type, entity_type, entity_id, metadata_json, ip_address, user_agent)
                 VALUES
                    (:actor_user_id, :event_type, :entity_type, :entity_id, :metadata_json, :ip_address, :user_agent)'
            );

            $ip = $_SERVER['REMOTE_ADDR'] ?? null;
            $ua = $_SERVER['HTTP_USER_AGENT'] ?? null;

            $stmt->execute([
                ':actor_user_id' => $actorUserId,
                ':event_type' => $eventType,
                ':entity_type' => 'monthly_report_content',
                ':entity_id' => $entityId,
                ':metadata_json' => $metaJson,
                ':ip_address' => is_string($ip) ? substr($ip, 0, 45) : null,
                ':user_agent' => is_string($ua) ? substr($ua, 0, 255) : null,
            ]);
        } catch (Throwable) {
            // Audit must not break CRUD writes.
        }
    }

    public function isUniqueViolation(Throwable $e): bool
    {
        if ($e instanceof PDOException) {
            if (($e->errorInfo[1] ?? null) === 1062) {
                return true;
            }
            $msg = $e->getMessage();
            if (str_contains($msg, 'uniq_monthly_report_contents_period')) {
                return true;
            }
        }
        return false;
    }

    private function selectSql(): string
    {
        return <<<'SQL'
SELECT
    mrc.id,
    mrc.reporting_period_id,
    mrc.status,
    mrc.title,
    mrc.executive_summary,
    mrc.work_completed,
    mrc.results_summary,
    mrc.key_findings,
    mrc.risks_and_blockers,
    mrc.next_month_plan,
    mrc.client_notes,
    mrc.internal_notes,
    mrc.source_weekly_checkpoint_ids,
    mrc.owner_user_id,
    mrc.reviewer_user_id,
    mrc.created_by,
    mrc.updated_by,
    mrc.reviewed_at,
    mrc.finalized_at,
    mrc.created_at,
    mrc.updated_at,
    rp.period_key,
    rp.period_start,
    rp.period_end,
    rp.status AS period_status,
    rp.title AS period_title,
    p.id AS project_id,
    p.name AS project_name,
    p.slug AS project_slug,
    c.id AS client_id,
    c.name AS client_name,
    c.slug AS client_slug,
    ou.name AS owner_name,
    ou.email AS owner_email,
    ru.name AS reviewer_name,
    ru.email AS reviewer_email,
    cu.name AS created_by_name,
    cu.email AS created_by_email,
    uu.name AS updated_by_name,
    uu.email AS updated_by_email
FROM monthly_report_contents mrc
INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN users ou ON ou.id = mrc.owner_user_id
LEFT JOIN users ru ON ru.id = mrc.reviewer_user_id
LEFT JOIN users cu ON cu.id = mrc.created_by
LEFT JOIN users uu ON uu.id = mrc.updated_by
SQL;
    }
}
