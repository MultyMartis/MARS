<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;

/**
 * Read/write access for monthly_report_work_entries — local MVP editor support.
 * No physical delete in application layer.
 */
final class MonthlyReportWorkEntryRepository
{
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
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM monthly_report_work_entries')->fetchColumn();
    }

    public function countByMonthlyReportId(int $monthlyReportId): int
    {
        if ($monthlyReportId <= 0) {
            return 0;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT COUNT(*) FROM monthly_report_work_entries WHERE monthly_report_id = :monthly_report_id'
        );
        $stmt->execute([':monthly_report_id' => $monthlyReportId]);
        return (int) $stmt->fetchColumn();
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE e.id = :id LIMIT 1';
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
            . ' WHERE e.monthly_report_id = :monthly_report_id'
            . ' ORDER BY e.sort_order ASC, e.id ASC';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':monthly_report_id' => $monthlyReportId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listByMonthlyReportIdAndPeriodRole(int $monthlyReportId, string $periodRole): array
    {
        if ($monthlyReportId <= 0 || $periodRole === '') {
            return [];
        }

        $sql = $this->selectSql()
            . ' WHERE e.monthly_report_id = :monthly_report_id'
            . ' AND e.period_role = :period_role'
            . ' ORDER BY e.sort_order ASC, e.id ASC';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':monthly_report_id' => $monthlyReportId,
            ':period_role' => $periodRole,
        ]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @param array{
     *   monthly_report_id:int,
     *   work_item_id:?int,
     *   category_id:?int,
     *   title:string,
     *   description:?string,
     *   status:string,
     *   period_role:string,
     *   client_visibility:string,
     *   client_summary:?string,
     *   internal_note:?string,
     *   evidence_note:?string,
     *   sort_order:int,
     *   created_by_user_id:?int,
     *   updated_by_user_id:?int
     * } $data
     */
    public function create(array $data): int
    {
        $sql = <<<'SQL'
INSERT INTO monthly_report_work_entries (
    monthly_report_id,
    work_item_id,
    category_id,
    title,
    description,
    status,
    period_role,
    client_visibility,
    client_summary,
    internal_note,
    evidence_note,
    sort_order,
    created_by_user_id,
    updated_by_user_id,
    created_at,
    updated_at
) VALUES (
    :monthly_report_id,
    :work_item_id,
    :category_id,
    :title,
    :description,
    :status,
    :period_role,
    :client_visibility,
    :client_summary,
    :internal_note,
    :evidence_note,
    :sort_order,
    :created_by_user_id,
    :updated_by_user_id,
    NOW(),
    NOW()
)
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':monthly_report_id' => (int) $data['monthly_report_id'],
            ':work_item_id' => $data['work_item_id'],
            ':category_id' => $data['category_id'],
            ':title' => (string) $data['title'],
            ':description' => $data['description'],
            ':status' => (string) $data['status'],
            ':period_role' => (string) $data['period_role'],
            ':client_visibility' => (string) $data['client_visibility'],
            ':client_summary' => $data['client_summary'],
            ':internal_note' => $data['internal_note'],
            ':evidence_note' => $data['evidence_note'],
            ':sort_order' => (int) $data['sort_order'],
            ':created_by_user_id' => $data['created_by_user_id'],
            ':updated_by_user_id' => $data['updated_by_user_id'],
        ]);

        return (int) $this->pdo()->lastInsertId();
    }

    /**
     * Updates an entry. Never changes monthly_report_id or created_by_user_id.
     *
     * @param array{
     *   work_item_id:?int,
     *   category_id:?int,
     *   title:string,
     *   description:?string,
     *   status:string,
     *   period_role:string,
     *   client_visibility:string,
     *   client_summary:?string,
     *   internal_note:?string,
     *   evidence_note:?string,
     *   sort_order:int,
     *   updated_by_user_id:?int
     * } $data
     */
    public function update(int $id, array $data): bool
    {
        if ($id <= 0) {
            return false;
        }

        $sql = <<<'SQL'
UPDATE monthly_report_work_entries SET
    work_item_id = :work_item_id,
    category_id = :category_id,
    title = :title,
    description = :description,
    status = :status,
    period_role = :period_role,
    client_visibility = :client_visibility,
    client_summary = :client_summary,
    internal_note = :internal_note,
    evidence_note = :evidence_note,
    sort_order = :sort_order,
    updated_by_user_id = :updated_by_user_id,
    updated_at = NOW()
WHERE id = :id
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([
            ':work_item_id' => $data['work_item_id'],
            ':category_id' => $data['category_id'],
            ':title' => (string) $data['title'],
            ':description' => $data['description'],
            ':status' => (string) $data['status'],
            ':period_role' => (string) $data['period_role'],
            ':client_visibility' => (string) $data['client_visibility'],
            ':client_summary' => $data['client_summary'],
            ':internal_note' => $data['internal_note'],
            ':evidence_note' => $data['evidence_note'],
            ':sort_order' => (int) $data['sort_order'],
            ':updated_by_user_id' => $data['updated_by_user_id'],
            ':id' => $id,
        ]);

        return $stmt->rowCount() >= 0;
    }

    private function selectSql(): string
    {
        return <<<'SQL'
SELECT
    e.id,
    e.monthly_report_id,
    e.work_item_id,
    e.category_id,
    e.title,
    e.description,
    e.status,
    e.period_role,
    e.client_visibility,
    e.client_summary,
    e.internal_note,
    e.evidence_note,
    e.sort_order,
    e.created_by_user_id,
    e.updated_by_user_id,
    e.created_at,
    e.updated_at,
    wi.slug AS work_item_slug,
    wi.name AS work_item_name,
    c.slug AS category_slug,
    c.name AS category_name
FROM monthly_report_work_entries e
LEFT JOIN seo_work_items wi ON wi.id = e.work_item_id
LEFT JOIN seo_work_categories c ON c.id = e.category_id
SQL;
    }
}
