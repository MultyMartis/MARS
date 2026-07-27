<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportExportRepository;
use Iseo\Repositories\ReportSnapshotRepository;
use Throwable;

/**
 * Internal-only HTML export from immutable report snapshots.
 */
final class ReportExportService
{
    private const STORAGE_REL_ROOT = 'storage/exports/reports';

    /** @var list<string> */
    private const VIEW_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    /** @var list<string> */
    private const CREATE_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
    ];

    public function __construct(
        private ReportExportRepository $exports,
        private ReportSnapshotRepository $snapshots,
        private DatabaseService $db
    ) {
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canView(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::VIEW_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function canCreate(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::CREATE_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   snapshot:?array<string,mixed>,
     *   exports:list<array<string,mixed>>,
     *   can_create:bool,
     *   errors?:array<string,string>
     * }
     */
    public function listForSnapshot(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canView($actor)) {
            return [
                'ok' => false,
                'message' => 'You do not have access to report exports.',
                'snapshot' => null,
                'exports' => [],
                'can_create' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'snapshot' => null,
                'exports' => [],
                'can_create' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        return [
            'ok' => true,
            'message' => 'Exports loaded.',
            'snapshot' => $snapshot,
            'exports' => $this->exports->findBySnapshotId($snapshotId),
            'can_create' => $this->canCreateExportForSnapshot($snapshot, $actor),
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   idempotent:bool,
     *   errors?:array<string,string>
     * }
     */
    public function createHtmlForSnapshot(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canCreate($actor)) {
            $this->auditFailure($actor, $snapshotId, null, ['role']);
            return [
                'ok' => false,
                'message' => 'You do not have permission to create HTML exports.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            $this->auditFailure($actor, $snapshotId, null, ['snapshot_exists']);
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        if ((string) ($snapshot['status'] ?? '') !== 'active') {
            $this->auditFailure($actor, $snapshotId, (int) ($snapshot['monthly_report_content_id'] ?? 0), ['snapshot_active']);
            return [
                'ok' => false,
                'message' => 'HTML export requires an active snapshot.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['status' => 'Snapshot is not active.'],
            ];
        }

        $payload = $this->decodePayloadJson($snapshot['payload_json'] ?? null);
        if ($payload === null) {
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['payload_valid']);
            return [
                'ok' => false,
                'message' => 'Snapshot payload is missing or invalid.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['payload' => 'Invalid payload.'],
            ];
        }

        $snapshotChecksum = (string) ($snapshot['checksum_sha256'] ?? '');
        if ($snapshotChecksum === '') {
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['checksum_present']);
            return [
                'ok' => false,
                'message' => 'Snapshot checksum is missing.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['checksum' => 'Missing checksum.'],
            ];
        }

        $existing = $this->exports->findReadyHtmlBySnapshotChecksum($snapshotId, $snapshotChecksum);
        if ($existing !== null) {
            $paths = $this->artifactPath($snapshot);
            $absolute = $paths['absolute'];
            if (!is_file($absolute)) {
                return [
                    'ok' => false,
                    'message' => 'Export metadata exists but artifact file is missing. Contact an administrator.',
                    'export' => $existing,
                    'idempotent' => false,
                    'errors' => ['file' => 'Artifact missing on disk.'],
                ];
            }

            $fileChecksum = $this->checksumFile($absolute);
            $storedChecksum = (string) ($existing['checksum_sha256'] ?? '');
            if ($storedChecksum !== '' && !hash_equals(strtolower($storedChecksum), strtolower($fileChecksum))) {
                return [
                    'ok' => false,
                    'message' => 'Export metadata does not match artifact checksum. Contact an administrator.',
                    'export' => $existing,
                    'idempotent' => false,
                    'errors' => ['checksum' => 'Checksum mismatch.'],
                ];
            }

            $this->exports->insertAudit('report_export.idempotent_hit', (int) $actor['id'], (int) $existing['id'], [
                'export_id' => (int) $existing['id'],
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => (int) $existing['monthly_report_content_id'],
                'format' => 'html',
                'storage_path' => (string) $existing['storage_path'],
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'actor_user_id' => (int) $actor['id'],
            ]);

            return [
                'ok' => true,
                'message' => 'HTML export already exists for this snapshot checksum (idempotent).',
                'export' => $existing,
                'idempotent' => true,
            ];
        }

        $generatedAt = gmdate('Y-m-d\TH:i:s\Z');
        $html = $this->buildHtml($snapshot, $payload, $generatedAt);
        $paths = $this->artifactPath($snapshot);
        $absolute = $paths['absolute'];
        $relative = $paths['relative'];

        $dir = dirname($absolute);
        if (!is_dir($dir) && !mkdir($dir, 0755, true) && !is_dir($dir)) {
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['mkdir_failed']);
            return [
                'ok' => false,
                'message' => 'Could not create export storage directory.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }

        if (file_put_contents($absolute, $html) === false) {
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['write_failed']);
            return [
                'ok' => false,
                'message' => 'Could not write HTML export artifact.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }

        $fileSize = (int) filesize($absolute);
        $fileChecksum = $this->checksumFile($absolute);
        $exportKey = 'snapshot-' . $snapshotId . '-html-v' . (int) $snapshot['version'];
        $filename = (string) $snapshot['snapshot_key'] . '.html';

        try {
            $newId = $this->exports->insert([
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => (int) $snapshot['monthly_report_content_id'],
                'export_key' => $exportKey,
                'format' => 'html',
                'status' => 'ready',
                'storage_disk' => 'local',
                'storage_path' => $relative,
                'filename' => $filename,
                'mime_type' => 'text/html; charset=UTF-8',
                'file_size_bytes' => $fileSize,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'created_by' => (int) $actor['id'],
            ]);

            $this->exports->insertAudit('report_export.created', (int) $actor['id'], $newId, [
                'export_id' => $newId,
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => (int) $snapshot['monthly_report_content_id'],
                'format' => 'html',
                'storage_path' => $relative,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'actor_user_id' => (int) $actor['id'],
                'export_key' => $exportKey,
            ]);

            $created = $this->exports->findById($newId);
            return [
                'ok' => true,
                'message' => 'HTML export created.',
                'export' => $created,
                'idempotent' => false,
            ];
        } catch (Throwable) {
            if (is_file($absolute)) {
                @unlink($absolute);
            }
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['persist_failed']);
            return [
                'ok' => false,
                'message' => 'Could not save export metadata. Please try again.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   errors?:array<string,string>
     * }
     */
    public function getById(int $exportId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canView($actor)) {
            return [
                'ok' => false,
                'message' => 'You do not have access to report exports.',
                'export' => null,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return [
                'ok' => false,
                'message' => 'Export not found.',
                'export' => null,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        return [
            'ok' => true,
            'message' => 'Export loaded.',
            'export' => $export,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   absolute_path:?string,
     *   errors?:array<string,string>
     * }
     */
    public function download(int $exportId, array $actor): array
    {
        $result = $this->getById($exportId, $actor);
        if (!$result['ok'] || $result['export'] === null) {
            return [
                'ok' => false,
                'message' => $result['message'],
                'export' => $result['export'],
                'absolute_path' => null,
                'errors' => $result['errors'] ?? [],
            ];
        }

        $export = $result['export'];
        if ((string) ($export['status'] ?? '') !== 'ready') {
            return [
                'ok' => false,
                'message' => 'Export is not ready for download.',
                'export' => $export,
                'absolute_path' => null,
                'errors' => ['status' => 'Not ready.'],
            ];
        }

        $absolute = $this->resolveStoragePath((string) ($export['storage_path'] ?? ''));
        if ($absolute === null || !is_file($absolute)) {
            return [
                'ok' => false,
                'message' => 'Export artifact file is missing.',
                'export' => $export,
                'absolute_path' => null,
                'errors' => ['file' => 'Missing.'],
            ];
        }

        $storedChecksum = (string) ($export['checksum_sha256'] ?? '');
        if ($storedChecksum !== '') {
            $fileChecksum = $this->checksumFile($absolute);
            if (!hash_equals(strtolower($storedChecksum), strtolower($fileChecksum))) {
                return [
                    'ok' => false,
                    'message' => 'Export artifact checksum mismatch.',
                    'export' => $export,
                    'absolute_path' => null,
                    'errors' => ['checksum' => 'Mismatch.'],
                ];
            }
        }

        return [
            'ok' => true,
            'message' => 'Ready to stream.',
            'export' => $export,
            'absolute_path' => $absolute,
        ];
    }

    /**
     * @param array<string, mixed> $snapshot
     * @param array<string, mixed> $payload
     */
    public function buildHtml(array $snapshot, array $payload, string $generatedAt): string
    {
        $title = (string) ($snapshot['title'] ?? ($payload['monthly_report']['title'] ?? 'Monthly report'));
        $snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');
        $version = (int) ($snapshot['version'] ?? 0);
        $checksum = (string) ($snapshot['checksum_sha256'] ?? '');
        $period = is_array($payload['period'] ?? null) ? $payload['period'] : [];
        $client = is_array($payload['client'] ?? null) ? $payload['client'] : [];
        $project = is_array($payload['project'] ?? null) ? $payload['project'] : [];
        $site = is_array($payload['site'] ?? null) ? $payload['site'] : [];
        $monthly = is_array($payload['monthly_report'] ?? null) ? $payload['monthly_report'] : [];
        $blocks = is_array($payload['blocks'] ?? null) ? $payload['blocks'] : [];
        $weeklySources = is_array($payload['weekly_sources'] ?? null) ? $payload['weekly_sources'] : [];

        $periodKey = (string) ($period['key'] ?? '');
        $renderMode = (string) ($snapshot['render_mode'] ?? ($payload['metadata']['render_mode'] ?? ''));

        $esc = static fn (mixed $v): string => htmlspecialchars((string) $v, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');

        $html = '<!DOCTYPE html>' . "\n";
        $html .= '<html lang="ru">' . "\n";
        $html .= '<head>' . "\n";
        $html .= '<meta charset="UTF-8">' . "\n";
        $html .= '<meta name="viewport" content="width=device-width, initial-scale=1">' . "\n";
        $html .= '<title>' . $esc($title) . ' — export</title>' . "\n";
        $html .= '<style>' . $this->embeddedCss() . '</style>' . "\n";
        $html .= '</head>' . "\n";
        $html .= '<body>' . "\n";
        $html .= '<header class="export-header">' . "\n";
        $html .= '<p class="export-badge">Internal report export — HTML artifact</p>' . "\n";
        $html .= '<h1>' . $esc($title) . '</h1>' . "\n";
        $html .= '<dl class="export-meta">' . "\n";
        $html .= '<dt>Period</dt><dd><code>' . $esc($periodKey) . '</code></dd>' . "\n";
        $html .= '<dt>Client</dt><dd>' . $esc((string) ($client['name'] ?? '—')) . '</dd>' . "\n";
        $html .= '<dt>Project</dt><dd>' . $esc((string) ($project['name'] ?? '—')) . '</dd>' . "\n";
        $html .= '<dt>Site</dt><dd>' . $esc((string) ($site['url'] ?? '—'));
        if (!empty($site['label'])) {
            $html .= ' — ' . $esc((string) $site['label']);
        }
        $html .= '</dd>' . "\n";
        $html .= '<dt>Snapshot key</dt><dd><code>' . $esc($snapshotKey) . '</code></dd>' . "\n";
        $html .= '<dt>Snapshot version</dt><dd>' . $esc((string) $version) . '</dd>' . "\n";
        $html .= '<dt>Snapshot checksum</dt><dd><code class="checksum">' . $esc($checksum) . '</code></dd>' . "\n";
        $html .= '<dt>Render mode</dt><dd><code>' . $esc($renderMode) . '</code></dd>' . "\n";
        $html .= '<dt>Export generated at (UTC)</dt><dd>' . $esc($generatedAt) . '</dd>' . "\n";
        $html .= '<dt>Monthly status</dt><dd>' . $esc((string) ($monthly['status'] ?? '—')) . '</dd>' . "\n";
        $html .= '</dl>' . "\n";
        $html .= '</header>' . "\n";

        if ($weeklySources !== []) {
            $html .= '<section class="export-section">' . "\n";
            $html .= '<h2>Source weekly checkpoints</h2>' . "\n";
            $html .= '<ul>' . "\n";
            foreach ($weeklySources as $wc) {
                if (!is_array($wc)) {
                    continue;
                }
                $html .= '<li><code>' . $esc((string) ($wc['checkpoint_key'] ?? '')) . '</code>';
                $html .= ' — ' . $esc((string) ($wc['title'] ?? ''));
                $html .= ' (' . $esc((string) ($wc['status'] ?? '')) . ')</li>' . "\n";
            }
            $html .= '</ul>' . "\n";
            $html .= '</section>' . "\n";
        }

        $flatFields = is_array($monthly['flat_fields'] ?? null) ? $monthly['flat_fields'] : [];
        if ($flatFields !== []) {
            $html .= '<section class="export-section">' . "\n";
            $html .= '<h2>Monthly summary fields</h2>' . "\n";
            foreach ($flatFields as $key => $value) {
                if (!is_string($key)) {
                    continue;
                }
                $label = str_replace('_', ' ', $key);
                $label = ucwords($label);
                $html .= '<article class="export-block">' . "\n";
                $html .= '<h3>' . $esc($label) . '</h3>' . "\n";
                $html .= '<div class="export-body">' . nl2br($esc((string) $value), false) . '</div>' . "\n";
                $html .= '</article>' . "\n";
            }
            $html .= '</section>' . "\n";
        }

        $html .= '<section class="export-section">' . "\n";
        $html .= '<h2>Report blocks</h2>' . "\n";
        if ($blocks === []) {
            $html .= '<p class="note">No blocks in snapshot payload.</p>' . "\n";
        } else {
            foreach ($blocks as $block) {
                if (!is_array($block)) {
                    continue;
                }
                $html .= '<article class="export-block">' . "\n";
                $html .= '<h3>' . $esc((string) ($block['title'] ?? '')) . '</h3>' . "\n";
                $html .= '<p class="export-block-meta"><code>' . $esc((string) ($block['block_key'] ?? '')) . '</code>';
                $html .= ' · ' . $esc((string) ($block['block_type'] ?? ''));
                $html .= ' · sort ' . $esc((string) ($block['sort_order'] ?? '')) . '</p>' . "\n";
                $summary = trim((string) ($block['summary'] ?? ''));
                if ($summary !== '') {
                    $html .= '<p class="export-summary"><em>' . $esc($summary) . '</em></p>' . "\n";
                }
                $body = trim((string) ($block['body'] ?? ''));
                if ($body !== '') {
                    $html .= '<div class="export-body">' . nl2br($esc($body), false) . '</div>' . "\n";
                }
                $html .= '</article>' . "\n";
            }
        }
        $html .= '</section>' . "\n";

        $html .= '<footer class="export-footer">' . "\n";
        $html .= '<p>Immutable snapshot export. Source: report_snapshots payload only.</p>' . "\n";
        $html .= '</footer>' . "\n";
        $html .= '</body>' . "\n";
        $html .= '</html>';

        return $html;
    }

    /**
     * @param array<string, mixed> $snapshot
     * @return array{relative:string,absolute:string,filename:string}
     */
    public function artifactPath(array $snapshot): array
    {
        $monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);
        $snapshotId = (int) ($snapshot['id'] ?? 0);
        $snapshotKey = (string) ($snapshot['snapshot_key'] ?? '');
        $filename = $snapshotKey . '.html';

        $relative = self::STORAGE_REL_ROOT
            . '/monthly-' . $monthlyId
            . '/snapshot-' . $snapshotId
            . '/' . $filename;

        $absolute = base_path($relative);

        return [
            'relative' => str_replace('\\', '/', $relative),
            'absolute' => $absolute,
            'filename' => $filename,
        ];
    }

    public function checksumFile(string $path): string
    {
        $hash = hash_file('sha256', $path);
        return is_string($hash) ? $hash : '';
    }

    /**
     * @param array<string, mixed> $snapshot
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     */
    public function canCreateExportForSnapshot(array $snapshot, array $actor): bool
    {
        return $this->canCreate($actor)
            && (string) ($snapshot['status'] ?? '') === 'active'
            && $this->decodePayloadJson($snapshot['payload_json'] ?? null) !== null;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyHtmlForSnapshot(int $snapshotId): ?array
    {
        if ($snapshotId <= 0) {
            return null;
        }
        return $this->exports->findReadyBySnapshotAndFormat($snapshotId, 'html');
    }

    private function embeddedCss(): string
    {
        return <<<'CSS'
body { font-family: Georgia, "Times New Roman", serif; color: #1a1a1a; line-height: 1.5; margin: 2rem; max-width: 52rem; }
.export-badge { font-size: 0.85rem; color: #555; text-transform: uppercase; letter-spacing: 0.05em; }
.export-meta { display: grid; grid-template-columns: 12rem 1fr; gap: 0.25rem 1rem; font-size: 0.95rem; }
.export-meta dt { font-weight: 600; margin: 0; }
.export-meta dd { margin: 0; }
.export-section { margin-top: 2rem; border-top: 1px solid #ccc; padding-top: 1rem; }
.export-block { margin-bottom: 1.5rem; }
.export-block-meta { font-size: 0.85rem; color: #444; }
.export-summary { color: #333; }
.export-body { margin-top: 0.5rem; }
.checksum { word-break: break-all; font-size: 0.8rem; }
.export-footer { margin-top: 2rem; font-size: 0.8rem; color: #666; border-top: 1px solid #ddd; padding-top: 1rem; }
.note { color: #666; }
CSS;
    }

    private function resolveStoragePath(string $storagePath): ?string
    {
        $storagePath = trim(str_replace('\\', '/', $storagePath));
        if ($storagePath === '' || str_contains($storagePath, '..')) {
            return null;
        }

        $normalized = ltrim($storagePath, '/');
        $allowedPrefix = self::STORAGE_REL_ROOT . '/';
        if (!str_starts_with($normalized, $allowedPrefix)) {
            return null;
        }

        $absolute = base_path($normalized);
        $root = realpath(base_path(self::STORAGE_REL_ROOT));
        $resolved = realpath($absolute);
        if ($root === false) {
            $root = base_path(self::STORAGE_REL_ROOT);
        }
        if ($resolved === false || !is_file($resolved)) {
            if (!is_file($absolute)) {
                return null;
            }
            $resolved = $absolute;
        }

        $rootReal = realpath(dirname($resolved));
        if ($rootReal !== false && $root !== false) {
            $rootNorm = rtrim(str_replace('\\', '/', $root), '/');
            $fileNorm = str_replace('\\', '/', $resolved);
            if (!str_starts_with($fileNorm, $rootNorm)) {
                return null;
            }
        }

        return $resolved;
    }

    /**
     * @return array<string, mixed>|null
     */
    private function decodePayloadJson(mixed $raw): ?array
    {
        if (is_array($raw)) {
            return $raw;
        }
        if (!is_string($raw) || $raw === '') {
            return null;
        }
        $decoded = json_decode($raw, true);
        return is_array($decoded) ? $decoded : null;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param list<string> $reasons
     */
    private function auditFailure(array $actor, int $snapshotId, ?int $monthlyId, array $reasons): void
    {
        try {
            $this->exports->insertAudit('report_export.creation_failed', (int) $actor['id'], null, [
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => $monthlyId,
                'failed_reasons' => $reasons,
                'actor_user_id' => (int) $actor['id'],
            ]);
        } catch (Throwable) {
            // Audit must not break user-facing error path.
        }
    }

    private function assertDb(): void
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param list<string> $roles
     */
    private function userHasAnyRole(?array $user, array $roles): bool
    {
        if ($user === null) {
            return false;
        }
        $have = $user['roles'] ?? [];
        if (!is_array($have)) {
            return false;
        }
        foreach ($roles as $role) {
            if (in_array($role, $have, true)) {
                return true;
            }
        }
        return false;
    }
}
