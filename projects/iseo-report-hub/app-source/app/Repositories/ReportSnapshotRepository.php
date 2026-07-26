<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use Throwable;

/**
 * Persistence for immutable report snapshots (insert + read; no hard delete).
 */
final class ReportSnapshotRepository
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
     * @return array<string, mixed>|null
     */
    public function findById(int $id): ?array
    {
        if ($id <= 0) {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT rs.*, u.name AS created_by_name, u.email AS created_by_email
             FROM report_snapshots rs
             LEFT JOIN users u ON u.id = rs.created_by
             WHERE rs.id = :id
             LIMIT 1'
        );
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findActiveByMonthlyId(int $monthlyReportId): ?array
    {
        if ($monthlyReportId <= 0) {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT rs.*, u.name AS created_by_name, u.email AS created_by_email
             FROM report_snapshots rs
             LEFT JOIN users u ON u.id = rs.created_by
             WHERE rs.monthly_report_content_id = :mid
               AND rs.status = \'active\'
             ORDER BY rs.version DESC, rs.id DESC
             LIMIT 1'
        );
        $stmt->execute([':mid' => $monthlyReportId]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    public function nextVersion(int $monthlyReportId): int
    {
        $stmt = $this->pdo()->prepare(
            'SELECT COALESCE(MAX(version), 0) + 1
             FROM report_snapshots
             WHERE monthly_report_content_id = :mid'
        );
        $stmt->execute([':mid' => $monthlyReportId]);
        return max(1, (int) $stmt->fetchColumn());
    }

    public function countAll(): int
    {
        return (int) $this->pdo()->query('SELECT COUNT(*) FROM report_snapshots')->fetchColumn();
    }

    /**
     * Mark current active row(s) for monthly as superseded (scaffolding for v2+).
     */
    public function supersedeActive(int $monthlyReportId): int
    {
        $stmt = $this->pdo()->prepare(
            'UPDATE report_snapshots
             SET status = \'superseded\'
             WHERE monthly_report_content_id = :mid
               AND status = \'active\''
        );
        $stmt->execute([':mid' => $monthlyReportId]);
        return $stmt->rowCount();
    }

    /**
     * @param array{
     *   monthly_report_content_id:int,
     *   reporting_period_id:int,
     *   snapshot_key:string,
     *   version:int,
     *   status:string,
     *   title:string,
     *   render_mode:string,
     *   payload_json:string,
     *   rendered_text:?string,
     *   rendered_html:?string,
     *   checksum_sha256:string,
     *   source_block_ids:?string,
     *   source_weekly_checkpoint_ids:?string,
     *   created_by:?int
     * } $data
     */
    public function insert(array $data): int
    {
        $stmt = $this->pdo()->prepare(
            'INSERT INTO report_snapshots
                (monthly_report_content_id, reporting_period_id, snapshot_key, version, status,
                 title, render_mode, payload_json, rendered_text, rendered_html, checksum_sha256,
                 source_block_ids, source_weekly_checkpoint_ids, created_by)
             VALUES
                (:monthly_report_content_id, :reporting_period_id, :snapshot_key, :version, :status,
                 :title, :render_mode, CAST(:payload_json AS JSON), :rendered_text, :rendered_html, :checksum_sha256,
                 CAST(:source_block_ids AS JSON), CAST(:source_weekly_checkpoint_ids AS JSON), :created_by)'
        );

        $stmt->execute([
            ':monthly_report_content_id' => $data['monthly_report_content_id'],
            ':reporting_period_id' => $data['reporting_period_id'],
            ':snapshot_key' => $data['snapshot_key'],
            ':version' => $data['version'],
            ':status' => $data['status'],
            ':title' => $data['title'],
            ':render_mode' => $data['render_mode'],
            ':payload_json' => $data['payload_json'],
            ':rendered_text' => $data['rendered_text'],
            ':rendered_html' => $data['rendered_html'],
            ':checksum_sha256' => $data['checksum_sha256'],
            ':source_block_ids' => $data['source_block_ids'],
            ':source_weekly_checkpoint_ids' => $data['source_weekly_checkpoint_ids'],
            ':created_by' => $data['created_by'],
        ]);

        return (int) $this->pdo()->lastInsertId();
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
                ':entity_type' => 'report_snapshot',
                ':entity_id' => $entityId,
                ':metadata_json' => $metaJson,
                ':ip_address' => is_string($ip) ? substr($ip, 0, 45) : null,
                ':user_agent' => is_string($ua) ? substr($ua, 0, 255) : null,
            ]);
        } catch (Throwable) {
            // Audit must not break snapshot writes.
        }
    }
}
