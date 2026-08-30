<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use PDOException;
use Throwable;

/**
 * PDO access for report_blocks — local MVP only.
 */
final class ReportBlockRepository
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
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM report_blocks')->fetchColumn();
    }

    public function existsForParentKey(int $monthlyReportId, string $blockKey, ?int $excludeId = null): bool
    {
        if ($monthlyReportId <= 0 || $blockKey === '') {
            return false;
        }

        $sql = 'SELECT 1 FROM report_blocks WHERE monthly_report_content_id = :mrc_id AND block_key = :block_key';
        $params = [
            ':mrc_id' => $monthlyReportId,
            ':block_key' => $blockKey,
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
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE rb.id = :id LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listByMonthlyReportId(int $monthlyReportId): array
    {
        if ($monthlyReportId <= 0) {
            return [];
        }

        $sql = $this->selectSql()
            . ' WHERE rb.monthly_report_content_id = :mrc_id'
            . ' ORDER BY rb.sort_order ASC, rb.id ASC';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':mrc_id' => $monthlyReportId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findMonthlyReportById(int $monthlyReportId): ?array
    {
        if ($monthlyReportId <= 0) {
            return null;
        }

        $sql = <<<'SQL'
SELECT
    mrc.id,
    mrc.reporting_period_id,
    mrc.status,
    mrc.title,
    mrc.source_weekly_checkpoint_ids,
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
    c.slug AS client_slug
FROM monthly_report_contents mrc
INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
WHERE mrc.id = :id
LIMIT 1
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $monthlyReportId]);
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
     *   monthly_report_content_id:int,
     *   block_key:string,
     *   block_type:string,
     *   sort_order:int,
     *   status:string,
     *   title:string,
     *   body:?string,
     *   summary:?string,
     *   data_json:?string,
     *   source_weekly_checkpoint_ids:?string,
     *   source_metric_refs:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   created_by:int,
     *   reviewed_at:?string,
     *   approved_at:?string
     * } $data
     */
    public function insert(array $data): int
    {
        $sql = <<<'SQL'
INSERT INTO report_blocks (
    monthly_report_content_id, block_key, block_type, sort_order, status,
    title, body, summary, data_json, source_weekly_checkpoint_ids, source_metric_refs,
    owner_user_id, reviewer_user_id, created_by, updated_by, reviewed_at, approved_at
) VALUES (
    :monthly_report_content_id, :block_key, :block_type, :sort_order, :status,
    :title, :body, :summary,
    CAST(:data_json AS JSON),
    CAST(:source_weekly_checkpoint_ids AS JSON),
    CAST(:source_metric_refs AS JSON),
    :owner_user_id, :reviewer_user_id, :created_by, NULL, :reviewed_at, :approved_at
)
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':monthly_report_content_id' => $data['monthly_report_content_id'],
            ':block_key' => $data['block_key'],
            ':block_type' => $data['block_type'],
            ':sort_order' => $data['sort_order'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':body' => $data['body'],
            ':summary' => $data['summary'],
            ':data_json' => $data['data_json'],
            ':source_weekly_checkpoint_ids' => $data['source_weekly_checkpoint_ids'],
            ':source_metric_refs' => $data['source_metric_refs'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':created_by' => $data['created_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':approved_at' => $data['approved_at'],
        ]);

        return (int) $this->pdo()->lastInsertId();
    }

    /**
     * @param array{
     *   block_key:string,
     *   block_type:string,
     *   sort_order:int,
     *   status:string,
     *   title:string,
     *   body:?string,
     *   summary:?string,
     *   data_json:?string,
     *   source_weekly_checkpoint_ids:?string,
     *   source_metric_refs:?string,
     *   owner_user_id:?int,
     *   reviewer_user_id:?int,
     *   updated_by:int,
     *   reviewed_at:?string,
     *   approved_at:?string
     * } $data
     */
    public function update(int $id, array $data): void
    {
        $sql = <<<'SQL'
UPDATE report_blocks SET
    block_key = :block_key,
    block_type = :block_type,
    sort_order = :sort_order,
    status = :status,
    title = :title,
    body = :body,
    summary = :summary,
    data_json = CAST(:data_json AS JSON),
    source_weekly_checkpoint_ids = CAST(:source_weekly_checkpoint_ids AS JSON),
    source_metric_refs = CAST(:source_metric_refs AS JSON),
    owner_user_id = :owner_user_id,
    reviewer_user_id = :reviewer_user_id,
    updated_by = :updated_by,
    reviewed_at = :reviewed_at,
    approved_at = :approved_at
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':block_key' => $data['block_key'],
            ':block_type' => $data['block_type'],
            ':sort_order' => $data['sort_order'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':body' => $data['body'],
            ':summary' => $data['summary'],
            ':data_json' => $data['data_json'],
            ':source_weekly_checkpoint_ids' => $data['source_weekly_checkpoint_ids'],
            ':source_metric_refs' => $data['source_metric_refs'],
            ':owner_user_id' => $data['owner_user_id'],
            ':reviewer_user_id' => $data['reviewer_user_id'],
            ':updated_by' => $data['updated_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':approved_at' => $data['approved_at'],
            ':id' => $id,
        ]);
    }

    /**
     * Narrow assembly apply write: body + status + actor + review timestamps + optional data_json.
     * Does not touch title, key, sort, summary, or source refs.
     *
     * @param array{
     *   body:string,
     *   status:string,
     *   updated_by:int,
     *   reviewed_at:?string,
     *   approved_at:?string,
     *   data_json?:?string
     * } $data
     */
    public function updateAssemblyApply(int $id, array $data): void
    {
        $params = [
            ':body' => $data['body'],
            ':status' => $data['status'],
            ':updated_by' => $data['updated_by'],
            ':reviewed_at' => $data['reviewed_at'],
            ':approved_at' => $data['approved_at'],
            ':id' => $id,
        ];

        $sql = 'UPDATE report_blocks SET
            body = :body,
            status = :status,
            updated_by = :updated_by,
            reviewed_at = :reviewed_at,
            approved_at = :approved_at';

        if (array_key_exists('data_json', $data)) {
            $sql .= ', data_json = CAST(:data_json AS JSON)';
            $params[':data_json'] = $data['data_json'];
        }

        $sql .= ' WHERE id = :id';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute($params);
    }

    /**
     * Narrow specialist content write: body + status + actor only.
     * Does not touch title, key, sort, summary, data_json, or source refs.
     *
     * @param array{body:string,status:string,updated_by:int} $data
     */
    public function updateBodyOnly(int $id, array $data): void
    {
        $sql = <<<'SQL'
UPDATE report_blocks SET
    body = :body,
    status = :status,
    updated_by = :updated_by,
    reviewed_at = NULL,
    approved_at = NULL
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':body' => $data['body'],
            ':status' => $data['status'],
            ':updated_by' => $data['updated_by'],
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
                ':entity_type' => 'report_block',
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
            if (str_contains($msg, 'uniq_report_blocks_parent_key')) {
                return true;
            }
        }
        return false;
    }

    private function selectSql(): string
    {
        return <<<'SQL'
SELECT
    rb.id,
    rb.monthly_report_content_id,
    rb.block_key,
    rb.block_type,
    rb.sort_order,
    rb.status,
    rb.title,
    rb.body,
    rb.summary,
    rb.data_json,
    rb.source_weekly_checkpoint_ids,
    rb.source_metric_refs,
    rb.owner_user_id,
    rb.reviewer_user_id,
    rb.created_by,
    rb.updated_by,
    rb.reviewed_at,
    rb.approved_at,
    rb.created_at,
    rb.updated_at,
    mrc.title AS monthly_title,
    mrc.status AS monthly_status,
    mrc.reporting_period_id,
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
FROM report_blocks rb
INNER JOIN monthly_report_contents mrc ON mrc.id = rb.monthly_report_content_id
INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN users ou ON ou.id = rb.owner_user_id
LEFT JOIN users ru ON ru.id = rb.reviewer_user_id
LEFT JOIN users cu ON cu.id = rb.created_by
LEFT JOIN users uu ON uu.id = rb.updated_by
SQL;
    }
}
