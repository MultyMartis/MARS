<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use PDOException;
use Throwable;

// PDOException kept for isUniqueViolation()

/**
 * PDO access for reporting_periods — local MVP only.
 */
final class ReportingPeriodRepository
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

    /**
     * @return list<array<string, mixed>>
     */
    public function listWithContext(): array
    {
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
    rp.owner_user_id,
    rp.reviewer_user_id,
    rp.created_by,
    rp.updated_by,
    rp.finalized_at,
    rp.created_at,
    rp.updated_at,
    p.name AS project_name,
    p.slug AS project_slug,
    c.id AS client_id,
    c.name AS client_name,
    c.slug AS client_slug,
    ou.name AS owner_name,
    ou.email AS owner_email,
    ru.name AS reviewer_name,
    ru.email AS reviewer_email
FROM reporting_periods rp
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN users ou ON ou.id = rp.owner_user_id
LEFT JOIN users ru ON ru.id = rp.reviewer_user_id
ORDER BY rp.period_key DESC, rp.id DESC
SQL;

        $stmt = $this->pdo()->query($sql);
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
    rp.id,
    rp.project_id,
    rp.period_key,
    rp.period_start,
    rp.period_end,
    rp.status,
    rp.title,
    rp.summary,
    rp.owner_user_id,
    rp.reviewer_user_id,
    rp.created_by,
    rp.updated_by,
    rp.finalized_at,
    rp.created_at,
    rp.updated_at,
    p.name AS project_name,
    p.slug AS project_slug,
    c.id AS client_id,
    c.name AS client_name,
    c.slug AS client_slug,
    s.id AS primary_site_id,
    s.url AS primary_site_url,
    s.label AS primary_site_label,
    ou.name AS owner_name,
    ou.email AS owner_email,
    ru.name AS reviewer_name,
    ru.email AS reviewer_email,
    cu.name AS created_by_name,
    cu.email AS created_by_email,
    uu.name AS updated_by_name,
    uu.email AS updated_by_email
FROM reporting_periods rp
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN sites s ON s.project_id = p.id AND s.is_primary = 1
LEFT JOIN users ou ON ou.id = rp.owner_user_id
LEFT JOIN users ru ON ru.id = rp.reviewer_user_id
LEFT JOIN users cu ON cu.id = rp.created_by
LEFT JOIN users uu ON uu.id = rp.updated_by
WHERE rp.id = :id
LIMIT 1
SQL;

        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    public function countAll(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM reporting_periods')->fetchColumn();
    }

    public function projectExists(int $projectId): bool
    {
        if ($projectId <= 0) {
            return false;
        }
        $stmt = $this->pdo()->prepare('SELECT 1 FROM projects WHERE id = :id LIMIT 1');
        $stmt->execute([':id' => $projectId]);
        return (bool) $stmt->fetchColumn();
    }

    public function periodKeyExists(int $projectId, string $periodKey, ?int $excludeId = null): bool
    {
        $sql = 'SELECT 1 FROM reporting_periods WHERE project_id = :project_id AND period_key = :period_key';
        $params = [
            ':project_id' => $projectId,
            ':period_key' => $periodKey,
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
     * @return list<array{id:int,name:string,slug:string,client_name:string}>
     */
    public function listSelectableProjects(): array
    {
        $sql = <<<'SQL'
SELECT p.id, p.name, p.slug, c.name AS client_name
FROM projects p
INNER JOIN clients c ON c.id = p.client_id
WHERE p.status = 'active'
ORDER BY c.name ASC, p.name ASC
SQL;
        $stmt = $this->pdo()->query($sql);
        $rows = $stmt->fetchAll();
        $out = [];
        foreach ($rows as $row) {
            if (!is_array($row)) {
                continue;
            }
            $out[] = [
                'id' => (int) $row['id'],
                'name' => (string) $row['name'],
                'slug' => (string) $row['slug'],
                'client_name' => (string) $row['client_name'],
            ];
        }
        return $out;
    }

    /**
     * Internal users for owner/reviewer selects.
     *
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
     *   project_id:int,
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   created_by:int,
     *   finalized_at:?string
     * } $data
     */
    public function insert(array $data): int
    {
        $sql = <<<'SQL'
INSERT INTO reporting_periods (
    project_id, period_key, period_start, period_end, status,
    title, summary, owner_user_id, reviewer_user_id,
    created_by, updated_by, finalized_at
) VALUES (
    :project_id, :period_key, :period_start, :period_end, :status,
    :title, :summary, :owner_user_id, :reviewer_user_id,
    :created_by, NULL, :finalized_at
)
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':project_id' => $data['project_id'],
            ':period_key' => $data['period_key'],
            ':period_start' => $data['period_start'],
            ':period_end' => $data['period_end'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':summary' => $data['summary'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':created_by' => $data['created_by'],
            ':finalized_at' => $data['finalized_at'],
        ]);

        return (int) $this->pdo()->lastInsertId();
    }

    /**
     * @param array{
     *   period_key:string,
     *   period_start:string,
     *   period_end:string,
     *   status:string,
     *   title:?string,
     *   summary:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   updated_by:int,
     *   finalized_at:?string
     * } $data
     */
    public function update(int $id, array $data): void
    {
        $sql = <<<'SQL'
UPDATE reporting_periods SET
    period_key = :period_key,
    period_start = :period_start,
    period_end = :period_end,
    status = :status,
    title = :title,
    summary = :summary,
    owner_user_id = :owner_user_id,
    reviewer_user_id = :reviewer_user_id,
    updated_by = :updated_by,
    finalized_at = :finalized_at
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':period_key' => $data['period_key'],
            ':period_start' => $data['period_start'],
            ':period_end' => $data['period_end'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':summary' => $data['summary'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':updated_by' => $data['updated_by'],
            ':finalized_at' => $data['finalized_at'],
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
                ':entity_type' => 'reporting_period',
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
            // MySQL duplicate key
            if (($e->errorInfo[1] ?? null) === 1062) {
                return true;
            }
            if (str_contains($e->getMessage(), 'uniq_reporting_periods_project_period')) {
                return true;
            }
        }
        return false;
    }
}
