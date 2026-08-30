<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use PDOException;
use Throwable;

/**
 * PDO access for weekly_checkpoints — local MVP only.
 */
final class WeeklyCheckpointRepository
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
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM weekly_checkpoints')->fetchColumn();
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listByPeriodId(int $periodId): array
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
    wc.checkpoint_start,
    wc.checkpoint_end,
    wc.status,
    wc.title,
    wc.summary,
    wc.work_done,
    wc.findings,
    wc.next_steps,
    wc.risks,
    wc.owner_user_id,
    wc.reviewer_user_id,
    wc.created_by,
    wc.updated_by,
    wc.reviewed_at,
    wc.completed_at,
    wc.created_at,
    wc.updated_at,
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
    ru.email AS reviewer_email
FROM weekly_checkpoints wc
INNER JOIN reporting_periods rp ON rp.id = wc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN users ou ON ou.id = wc.owner_user_id
LEFT JOIN users ru ON ru.id = wc.reviewer_user_id
WHERE wc.reporting_period_id = :period_id
ORDER BY wc.week_index ASC, wc.id ASC
SQL;

        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':period_id' => $periodId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $sql = <<<'SQL'
SELECT
    wc.id,
    wc.reporting_period_id,
    wc.week_index,
    wc.checkpoint_key,
    wc.checkpoint_start,
    wc.checkpoint_end,
    wc.status,
    wc.title,
    wc.summary,
    wc.work_done,
    wc.findings,
    wc.next_steps,
    wc.risks,
    wc.owner_user_id,
    wc.reviewer_user_id,
    wc.created_by,
    wc.updated_by,
    wc.reviewed_at,
    wc.completed_at,
    wc.created_at,
    wc.updated_at,
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
FROM weekly_checkpoints wc
INNER JOIN reporting_periods rp ON rp.id = wc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN users ou ON ou.id = wc.owner_user_id
LEFT JOIN users ru ON ru.id = wc.reviewer_user_id
LEFT JOIN users cu ON cu.id = wc.created_by
LEFT JOIN users uu ON uu.id = wc.updated_by
WHERE wc.id = :id
LIMIT 1
SQL;

        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $id]);
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

    public function weekIndexExists(int $periodId, int $weekIndex, ?int $excludeId = null): bool
    {
        $sql = 'SELECT 1 FROM weekly_checkpoints WHERE reporting_period_id = :period_id AND week_index = :week_index';
        $params = [
            ':period_id' => $periodId,
            ':week_index' => $weekIndex,
        ];
        if ($excludeId !== null && $excludeId > 0) {
            $sql .= ' AND id <> :exclude_id';
            $params[':exclude_id'] = $excludeId;
        }
        $sql .= ' LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute($params);
        return (bool) $stmt->fetchColumn();
    }

    public function checkpointKeyExists(int $periodId, string $checkpointKey, ?int $excludeId = null): bool
    {
        $sql = 'SELECT 1 FROM weekly_checkpoints WHERE reporting_period_id = :period_id AND checkpoint_key = :checkpoint_key';
        $params = [
            ':period_id' => $periodId,
            ':checkpoint_key' => $checkpointKey,
        ];
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
     *   reviewer_user_id:?int,
     *   created_by:int,
     *   reviewed_at:?string,
     *   completed_at:?string
     * } $data
     */
    public function insert(array $data): int
    {
        $sql = <<<'SQL'
INSERT INTO weekly_checkpoints (
    reporting_period_id, week_index, checkpoint_key, checkpoint_start, checkpoint_end, status,
    title, summary, work_done, findings, next_steps, risks,
    owner_user_id, reviewer_user_id, created_by, updated_by, reviewed_at, completed_at
) VALUES (
    :reporting_period_id, :week_index, :checkpoint_key, :checkpoint_start, :checkpoint_end, :status,
    :title, :summary, :work_done, :findings, :next_steps, :risks,
    :owner_user_id, :reviewer_user_id, :created_by, NULL, :reviewed_at, :completed_at
)
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':reporting_period_id' => $data['reporting_period_id'],
            ':week_index' => $data['week_index'],
            ':checkpoint_key' => $data['checkpoint_key'],
            ':checkpoint_start' => $data['checkpoint_start'],
            ':checkpoint_end' => $data['checkpoint_end'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':summary' => $data['summary'],
            ':work_done' => $data['work_done'],
            ':findings' => $data['findings'],
            ':next_steps' => $data['next_steps'],
            ':risks' => $data['risks'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':created_by' => $data['created_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':completed_at' => $data['completed_at'],
        ]);

        return (int) $this->pdo()->lastInsertId();
    }

    /**
     * @param array{
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
     *   reviewer_user_id:?int,
     *   updated_by:int,
     *   reviewed_at:?string,
     *   completed_at:?string
     * } $data
     */
    public function update(int $id, array $data): void
    {
        $sql = <<<'SQL'
UPDATE weekly_checkpoints SET
    week_index = :week_index,
    checkpoint_key = :checkpoint_key,
    checkpoint_start = :checkpoint_start,
    checkpoint_end = :checkpoint_end,
    status = :status,
    title = :title,
    summary = :summary,
    work_done = :work_done,
    findings = :findings,
    next_steps = :next_steps,
    risks = :risks,
    owner_user_id = :owner_user_id,
    reviewer_user_id = :reviewer_user_id,
    updated_by = :updated_by,
    reviewed_at = :reviewed_at,
    completed_at = :completed_at
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':week_index' => $data['week_index'],
            ':checkpoint_key' => $data['checkpoint_key'],
            ':checkpoint_start' => $data['checkpoint_start'],
            ':checkpoint_end' => $data['checkpoint_end'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':summary' => $data['summary'],
            ':work_done' => $data['work_done'],
            ':findings' => $data['findings'],
            ':next_steps' => $data['next_steps'],
            ':risks' => $data['risks'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':updated_by' => $data['updated_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':completed_at' => $data['completed_at'],
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
                ':entity_type' => 'weekly_checkpoint',
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
            if (str_contains($msg, 'uniq_weekly_checkpoints_period_week')
                || str_contains($msg, 'uniq_weekly_checkpoints_period_key')) {
                return true;
            }
        }
        return false;
    }
}
