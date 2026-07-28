<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use Throwable;

/**
 * Persistence for report_export_shares (token hash only; no plaintext token column).
 */
final class ReportExportShareRepository
{
    public function __construct(
        private DatabaseService $db
    ) {
    }

    public function pdo(): PDO
    {
        return $this->db->connect();
    }

    /**
     * @param array{
     *   report_export_id:int,
     *   token_hash:string,
     *   token_label:?string,
     *   status:string,
     *   expires_at:string,
     *   created_by:?int,
     *   max_access_count:?int,
     *   metadata_json:?string
     * } $data
     * @return array<string, mixed>|null
     */
    public function createShare(array $data): ?array
    {
        $stmt = $this->pdo()->prepare(
            'INSERT INTO report_export_shares (
                report_export_id, token_hash, token_label, status, expires_at,
                created_by, max_access_count, metadata_json, access_count, created_at
             ) VALUES (
                :export_id, :token_hash, :token_label, :status, :expires_at,
                :created_by, :max_access_count, :metadata_json, 0, NOW()
             )'
        );
        $stmt->execute([
            ':export_id' => (int) $data['report_export_id'],
            ':token_hash' => (string) $data['token_hash'],
            ':token_label' => $data['token_label'],
            ':status' => (string) $data['status'],
            ':expires_at' => (string) $data['expires_at'],
            ':created_by' => $data['created_by'],
            ':max_access_count' => $data['max_access_count'],
            ':metadata_json' => $data['metadata_json'],
        ]);

        $id = (int) $this->pdo()->lastInsertId();
        return $id > 0 ? $this->findById($id) : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findByTokenHash(string $hash): ?array
    {
        $hash = strtolower(trim($hash));
        if ($hash === '' || strlen($hash) !== 64) {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT s.*,
                    u.name AS created_by_name, u.email AS created_by_email,
                    ru.name AS revoked_by_name, ru.email AS revoked_by_email
             FROM report_export_shares s
             LEFT JOIN users u ON u.id = s.created_by
             LEFT JOIN users ru ON ru.id = s.revoked_by
             WHERE s.token_hash = :hash
             LIMIT 1'
        );
        $stmt->execute([':hash' => $hash]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
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
            'SELECT s.*,
                    u.name AS created_by_name, u.email AS created_by_email,
                    ru.name AS revoked_by_name, ru.email AS revoked_by_email
             FROM report_export_shares s
             LEFT JOIN users u ON u.id = s.created_by
             LEFT JOIN users ru ON ru.id = s.revoked_by
             WHERE s.id = :id
             LIMIT 1'
        );
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function findForExport(int $exportId): array
    {
        if ($exportId <= 0) {
            return [];
        }

        $stmt = $this->pdo()->prepare(
            'SELECT s.*,
                    u.name AS created_by_name, u.email AS created_by_email,
                    ru.name AS revoked_by_name, ru.email AS revoked_by_email
             FROM report_export_shares s
             LEFT JOIN users u ON u.id = s.created_by
             LEFT JOIN users ru ON ru.id = s.revoked_by
             WHERE s.report_export_id = :export_id
             ORDER BY s.id DESC'
        );
        $stmt->execute([':export_id' => $exportId]);
        $rows = $stmt->fetchAll();
        if (!is_array($rows)) {
            return [];
        }

        $out = [];
        foreach ($rows as $row) {
            if (is_array($row)) {
                $out[] = $row;
            }
        }
        return $out;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findActiveForExport(int $exportId): ?array
    {
        if ($exportId <= 0) {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT s.*,
                    u.name AS created_by_name, u.email AS created_by_email
             FROM report_export_shares s
             LEFT JOIN users u ON u.id = s.created_by
             WHERE s.report_export_id = :export_id
               AND s.status = \'active\'
               AND s.expires_at > NOW()
             ORDER BY s.id DESC
             LIMIT 1'
        );
        $stmt->execute([':export_id' => $exportId]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    public function revoke(int $shareId, int $userId): bool
    {
        if ($shareId <= 0) {
            return false;
        }

        $stmt = $this->pdo()->prepare(
            'UPDATE report_export_shares
             SET status = \'revoked\',
                 revoked_at = NOW(),
                 revoked_by = :user_id
             WHERE id = :id
               AND status = \'active\''
        );
        $stmt->execute([
            ':user_id' => $userId > 0 ? $userId : null,
            ':id' => $shareId,
        ]);

        return $stmt->rowCount() > 0;
    }

    public function recordSuccessfulAccess(int $shareId, ?string $ipHash, ?string $uaHash): bool
    {
        if ($shareId <= 0) {
            return false;
        }

        $stmt = $this->pdo()->prepare(
            'UPDATE report_export_shares
             SET access_count = access_count + 1,
                 last_accessed_at = NOW(),
                 last_access_ip_hash = :ip_hash,
                 last_user_agent_hash = :ua_hash
             WHERE id = :id
               AND status = \'active\'
               AND expires_at > NOW()
               AND (max_access_count IS NULL OR access_count < max_access_count)'
        );
        $stmt->execute([
            ':ip_hash' => $ipHash,
            ':ua_hash' => $uaHash,
            ':id' => $shareId,
        ]);

        return $stmt->rowCount() > 0;
    }

    public function countAll(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM report_export_shares')->fetchColumn();
    }

    /**
     * @return array<string, int>
     */
    public function countByStatus(): array
    {
        $stmt = $this->pdo()->query(
            'SELECT status, COUNT(*) AS cnt FROM report_export_shares GROUP BY status'
        );
        $rows = $stmt->fetchAll();
        $out = [
            'active' => 0,
            'revoked' => 0,
            'expired' => 0,
        ];
        if (!is_array($rows)) {
            return $out;
        }
        foreach ($rows as $row) {
            if (!is_array($row)) {
                continue;
            }
            $status = (string) ($row['status'] ?? '');
            if ($status !== '') {
                $out[$status] = (int) ($row['cnt'] ?? 0);
            }
        }
        return $out;
    }

    public function countActiveForExport(int $exportId): int
    {
        if ($exportId <= 0) {
            return 0;
        }
        $stmt = $this->pdo()->prepare(
            'SELECT COUNT(*) FROM report_export_shares
             WHERE report_export_id = :export_id
               AND status = \'active\'
               AND expires_at > NOW()'
        );
        $stmt->execute([':export_id' => $exportId]);
        return (int) $stmt->fetchColumn();
    }
}
