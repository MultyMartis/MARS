<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;

/**
 * Read access for seo_work_categories — local MVP catalogue support.
 */
final class SeoWorkCategoryRepository
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
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM seo_work_categories')->fetchColumn();
    }

    public function countActive(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM seo_work_categories WHERE is_active = 1')->fetchColumn();
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT id, slug, name, description, sort_order, is_active, source, created_at, updated_at
             FROM seo_work_categories
             WHERE id = :id
             LIMIT 1'
        );
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

        $stmt = $this->pdo()->prepare(
            'SELECT id, slug, name, description, sort_order, is_active, source, created_at, updated_at
             FROM seo_work_categories
             WHERE slug = :slug
             LIMIT 1'
        );
        $stmt->execute([':slug' => $slug]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listActive(): array
    {
        $sql = 'SELECT id, slug, name, description, sort_order, is_active, source, created_at, updated_at
                FROM seo_work_categories
                WHERE is_active = 1
                ORDER BY sort_order ASC, id ASC';
        $rows = $this->pdo()->query($sql)->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listAll(): array
    {
        $sql = 'SELECT id, slug, name, description, sort_order, is_active, source, created_at, updated_at
                FROM seo_work_categories
                ORDER BY sort_order ASC, id ASC';
        $rows = $this->pdo()->query($sql)->fetchAll();
        return is_array($rows) ? $rows : [];
    }
}
