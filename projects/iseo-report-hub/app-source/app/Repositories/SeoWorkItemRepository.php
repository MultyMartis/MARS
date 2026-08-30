<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;

/**
 * Read access for seo_work_items — local MVP catalogue support.
 */
final class SeoWorkItemRepository
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
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM seo_work_items')->fetchColumn();
    }

    public function countActive(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM seo_work_items WHERE is_active = 1')->fetchColumn();
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE wi.id = :id LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findBySlug(string $slug): ?array
    {
        $slug = trim($slug);
        if ($slug === '') {
            return null;
        }

        $sql = $this->selectSql() . ' WHERE wi.slug = :slug LIMIT 1';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':slug' => $slug]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listByCategoryId(int $categoryId, bool $activeOnly = true): array
    {
        if ($categoryId <= 0) {
            return [];
        }

        $sql = $this->selectSql() . ' WHERE wi.category_id = :category_id';
        if ($activeOnly) {
            $sql .= ' AND wi.is_active = 1';
        }
        $sql .= ' ORDER BY wi.sort_order ASC, wi.id ASC';
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':category_id' => $categoryId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listActive(): array
    {
        $sql = $this->selectSql()
            . ' WHERE wi.is_active = 1'
            . ' ORDER BY c.sort_order ASC, wi.sort_order ASC, wi.id ASC';
        $rows = $this->pdo()->query($sql)->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    private function selectSql(): string
    {
        return <<<'SQL'
SELECT
    wi.id,
    wi.category_id,
    wi.slug,
    wi.name,
    wi.description,
    wi.site_type,
    wi.cadence,
    wi.visibility,
    wi.fill_mode,
    wi.evidence_required,
    wi.sort_order,
    wi.is_active,
    wi.source,
    wi.created_at,
    wi.updated_at,
    c.slug AS category_slug,
    c.name AS category_name
FROM seo_work_items wi
INNER JOIN seo_work_categories c ON c.id = wi.category_id
SQL;
    }
}
