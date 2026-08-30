<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;
use Throwable;

/**
 * Persistence for report export metadata (insert + read; no delete).
 */
final class ReportExportRepository
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
            'SELECT re.*, u.name AS created_by_name, u.email AS created_by_email,
                    rs.snapshot_key, rs.version AS snapshot_version, rs.status AS snapshot_status,
                    src.export_key AS source_html_export_key,
                    src.format AS source_html_export_format,
                    src.status AS source_html_export_status
             FROM report_exports re
             LEFT JOIN users u ON u.id = re.created_by
             LEFT JOIN report_snapshots rs ON rs.id = re.report_snapshot_id
             LEFT JOIN report_exports src ON src.id = re.source_html_export_id
             WHERE re.id = :id
             LIMIT 1'
        );
        $stmt->execute([':id' => $id]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * Detail fetch with optional source-HTML lineage columns (DB-09).
     *
     * @return array<string, mixed>|null
     */
    public function findByIdWithSourceHtml(int $id): ?array
    {
        return $this->findById($id);
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function findBySnapshotId(int $snapshotId): array
    {
        if ($snapshotId <= 0) {
            return [];
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.*, u.name AS created_by_name, u.email AS created_by_email,
                    src.export_key AS source_html_export_key,
                    src.format AS source_html_export_format,
                    src.status AS source_html_export_status
             FROM report_exports re
             LEFT JOIN users u ON u.id = re.created_by
             LEFT JOIN report_exports src ON src.id = re.source_html_export_id
             WHERE re.report_snapshot_id = :sid
             ORDER BY re.id DESC'
        );
        $stmt->execute([':sid' => $snapshotId]);
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
    public function findReadyBySnapshotAndFormat(int $snapshotId, string $format): ?array
    {
        if ($snapshotId <= 0 || $format === '') {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.*
             FROM report_exports re
             WHERE re.report_snapshot_id = :sid
               AND re.format = :format
               AND re.status = \'ready\'
             ORDER BY re.id DESC
             LIMIT 1'
        );
        $stmt->execute([
            ':sid' => $snapshotId,
            ':format' => $format,
        ]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyHtmlBySnapshotChecksum(int $snapshotId, string $snapshotChecksum): ?array
    {
        return $this->findReadyBySnapshotFormatAndChecksum($snapshotId, 'html', $snapshotChecksum);
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyBySnapshotFormatAndChecksum(
        int $snapshotId,
        string $format,
        string $snapshotChecksum
    ): ?array {
        if ($snapshotId <= 0 || $format === '' || $snapshotChecksum === '') {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.*
             FROM report_exports re
             WHERE re.report_snapshot_id = :sid
               AND re.format = :format
               AND re.status = \'ready\'
               AND re.source_snapshot_checksum_sha256 = :checksum
             ORDER BY re.id DESC
             LIMIT 1'
        );
        $stmt->execute([
            ':sid' => $snapshotId,
            ':format' => $format,
            ':checksum' => $snapshotChecksum,
        ]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyByExportKey(string $exportKey): ?array
    {
        $exportKey = trim($exportKey);
        if ($exportKey === '') {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.*
             FROM report_exports re
             WHERE re.export_key = :export_key
               AND re.status = \'ready\'
             ORDER BY re.id DESC
             LIMIT 1'
        );
        $stmt->execute([':export_key' => $exportKey]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * Max export version parsed from export_key suffix `-vN` for snapshot+format.
     */
    public function maxExportVersionForSnapshotFormat(int $snapshotId, string $format): int
    {
        if ($snapshotId <= 0 || $format === '') {
            return 0;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.export_key
             FROM report_exports re
             WHERE re.report_snapshot_id = :sid
               AND re.format = :format'
        );
        $stmt->execute([
            ':sid' => $snapshotId,
            ':format' => $format,
        ]);
        $rows = $stmt->fetchAll();
        if (!is_array($rows)) {
            return 0;
        }

        $max = 0;
        foreach ($rows as $row) {
            if (!is_array($row)) {
                continue;
            }
            $key = (string) ($row['export_key'] ?? '');
            if (preg_match('/-v(\d+)$/', $key, $m) === 1) {
                $version = (int) $m[1];
                if ($version > $max) {
                    $max = $version;
                }
            }
        }

        return $max;
    }

    /**
     * Latest ready export with version >= 2 (styled restyle versions).
     *
     * @return array<string, mixed>|null
     */
    public function findReadyStyledVersionForSnapshotFormat(int $snapshotId, string $format): ?array
    {
        if ($snapshotId <= 0 || $format === '') {
            return null;
        }

        $stmt = $this->pdo()->prepare(
            'SELECT re.*
             FROM report_exports re
             WHERE re.report_snapshot_id = :sid
               AND re.format = :format
               AND re.status = \'ready\'
             ORDER BY re.id DESC'
        );
        $stmt->execute([
            ':sid' => $snapshotId,
            ':format' => $format,
        ]);
        $rows = $stmt->fetchAll();
        if (!is_array($rows)) {
            return null;
        }

        foreach ($rows as $row) {
            if (!is_array($row)) {
                continue;
            }
            $key = (string) ($row['export_key'] ?? '');
            if (preg_match('/-v(\d+)$/', $key, $m) === 1 && (int) $m[1] >= 2) {
                return $row;
            }
        }

        return null;
    }

    /**
     * @param array{
     *   report_snapshot_id:int,
     *   monthly_report_content_id:int,
     *   export_key:string,
     *   format:string,
     *   status:string,
     *   storage_disk:string,
     *   storage_path:string,
     *   filename:string,
     *   mime_type:string,
     *   file_size_bytes:int,
     *   checksum_sha256:string,
     *   source_snapshot_checksum_sha256:string,
     *   created_by:?int,
     *   template_id?:?string,
     *   template_version?:?string,
     *   render_target?:?string,
     *   render_engine?:?string,
     *   render_options_json?:?string,
     *   source_html_export_id?:?int,
     *   metadata_json?:?string
     * } $data
     */
    public function insert(array $data): int
    {
        $stmt = $this->pdo()->prepare(
            'INSERT INTO report_exports
                (report_snapshot_id, monthly_report_content_id, export_key, format, status,
                 storage_disk, storage_path, filename, mime_type, file_size_bytes,
                 checksum_sha256, source_snapshot_checksum_sha256, created_by,
                 template_id, template_version, render_target, render_engine,
                 render_options_json, source_html_export_id, metadata_json)
             VALUES
                (:report_snapshot_id, :monthly_report_content_id, :export_key, :format, :status,
                 :storage_disk, :storage_path, :filename, :mime_type, :file_size_bytes,
                 :checksum_sha256, :source_snapshot_checksum_sha256, :created_by,
                 :template_id, :template_version, :render_target, :render_engine,
                 :render_options_json, :source_html_export_id, :metadata_json)'
        );

        $stmt->execute([
            ':report_snapshot_id' => $data['report_snapshot_id'],
            ':monthly_report_content_id' => $data['monthly_report_content_id'],
            ':export_key' => $data['export_key'],
            ':format' => $data['format'],
            ':status' => $data['status'],
            ':storage_disk' => $data['storage_disk'],
            ':storage_path' => $data['storage_path'],
            ':filename' => $data['filename'],
            ':mime_type' => $data['mime_type'],
            ':file_size_bytes' => $data['file_size_bytes'],
            ':checksum_sha256' => $data['checksum_sha256'],
            ':source_snapshot_checksum_sha256' => $data['source_snapshot_checksum_sha256'],
            ':created_by' => $data['created_by'],
            ':template_id' => $data['template_id'] ?? null,
            ':template_version' => $data['template_version'] ?? null,
            ':render_target' => $data['render_target'] ?? null,
            ':render_engine' => $data['render_engine'] ?? null,
            ':render_options_json' => $data['render_options_json'] ?? null,
            ':source_html_export_id' => $data['source_html_export_id'] ?? null,
            ':metadata_json' => $data['metadata_json'] ?? null,
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
                ':entity_type' => 'report_export',
                ':entity_id' => $entityId,
                ':metadata_json' => $metaJson,
                ':ip_address' => is_string($ip) ? substr($ip, 0, 45) : null,
                ':user_agent' => is_string($ua) ? substr($ua, 0, 255) : null,
            ]);
        } catch (Throwable) {
            // Audit must not break export writes.
        }
    }
}
