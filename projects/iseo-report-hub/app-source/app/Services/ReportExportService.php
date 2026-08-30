<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportExportRepository;
use Iseo\Repositories\ReportSnapshotRepository;
use Iseo\Support\ReportTemplate;
use Iseo\Support\ReportTemplateRenderer;
use Throwable;

/**
 * Internal-only HTML/PDF export from immutable report snapshots.
 */
final class ReportExportService
{
    private const STORAGE_REL_ROOT = 'storage/exports/reports';

    private const EDGE_EXE = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

    private const CHROME_EXE = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

    private const BROWSER_TEMP_ROOT = 'X:\\AI MARS STORAGE\\incoming\\iseo-report-hub\\pdf-browser-temp';

    private const STYLED_BROWSER_TEMP_ROOT = 'X:\\AI MARS STORAGE\\incoming\\iseo-report-hub\\styling-export-version-apply-01\\pdf-browser-temp';

    private const PDF_TIMEOUT_SECONDS = 90;

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
        private DatabaseService $db,
        private ReportTemplateService $templates = new ReportTemplateService(),
        private ?ReportTemplateRenderer $renderer = null
    ) {
        $this->renderer ??= new ReportTemplateRenderer($this->templates);
    }

    /**
     * Future HTML exports use this code-first default template.
     *
     * @return array{id:string,version:int,render_target:string,source:string,branding:string,display_label:string}
     */
    public function defaultTemplateSummary(): array
    {
        return $this->templates->getDefaultSummary();
    }

    /**
     * Historical export rows have no DB template_id — do not invent one.
     */
    public function legacyTemplateLabel(): string
    {
        return $this->templates->legacyTemplateLabel();
    }

    /**
     * Non-mutating dry-render of snapshot HTML via iseo_default_v1 (no DB/file write).
     *
     * @return array{
     *   ok:bool,
     *   message:string,
     *   html:?string,
     *   template:?array{id:string,version:int,render_target:string,source:string,branding:string,display_label:string},
     *   snapshot:?array<string,mixed>,
     *   errors?:array<string,string>
     * }
     */
    public function dryRenderHtmlForSnapshot(int $snapshotId): array
    {
        $this->assertDb();

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'html' => null,
                'template' => null,
                'snapshot' => null,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $payload = $this->decodePayloadJson($snapshot['payload_json'] ?? null);
        if ($payload === null) {
            return [
                'ok' => false,
                'message' => 'Snapshot payload is missing or invalid.',
                'html' => null,
                'template' => null,
                'snapshot' => $snapshot,
                'errors' => ['payload' => 'Invalid payload.'],
            ];
        }

        $generatedAt = gmdate('Y-m-d\TH:i:s\Z');
        $html = $this->buildHtml($snapshot, $payload, $generatedAt);

        return [
            'ok' => true,
            'message' => 'Dry-render complete.',
            'html' => $html,
            'template' => $this->defaultTemplateSummary(),
            'snapshot' => $snapshot,
        ];
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
     *   can_create_pdf:bool,
     *   has_html_export:bool,
     *   has_pdf_export:bool,
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
                'can_create_pdf' => false,
                'has_html_export' => false,
                'has_pdf_export' => false,
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
                'can_create_pdf' => false,
                'has_html_export' => false,
                'has_pdf_export' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $htmlReady = $this->exports->findReadyBySnapshotAndFormat($snapshotId, 'html');
        $pdfReady = $this->exports->findReadyBySnapshotAndFormat($snapshotId, 'pdf');
        $styledHtml = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'html');
        $styledPdf = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'pdf');
        $canCreate = $this->canCreateExportForSnapshot($snapshot, $actor);
        $exportRows = $this->exports->findBySnapshotId($snapshotId);
        $enriched = [];
        foreach ($exportRows as $row) {
            $enriched[] = $this->withDisplayMetadata($row);
        }

        return [
            'ok' => true,
            'message' => 'Exports loaded.',
            'snapshot' => $snapshot,
            'exports' => $enriched,
            'can_create' => $canCreate,
            'can_create_pdf' => $this->canCreatePdfForSnapshot($snapshot, $actor, $htmlReady),
            'has_html_export' => $htmlReady !== null,
            'has_pdf_export' => $pdfReady !== null,
            'styled_html_export' => $styledHtml !== null ? $this->withDisplayMetadata($styledHtml) : null,
            'styled_pdf_export' => $styledPdf !== null ? $this->withDisplayMetadata($styledPdf) : null,
            'can_create_styled_html' => $canCreate,
            'can_create_styled_pdf' => $canCreate
                && $styledHtml !== null
                && (is_file(self::EDGE_EXE) || is_file(self::CHROME_EXE)),
            'future_template' => $this->defaultTemplateSummary(),
            'legacy_template_label' => $this->legacyTemplateLabel(),
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
            $validation = $this->validateReadyArtifact($existing);
            if (!$validation['ok']) {
                return [
                    'ok' => false,
                    'message' => $validation['message'] . ' Contact an administrator.',
                    'export' => $existing,
                    'idempotent' => false,
                    'errors' => $validation['errors'],
                ];
            }

            $fileChecksum = strtolower((string) ($existing['checksum_sha256'] ?? ''));
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
     * Create PDF export from an existing ready HTML export artifact (Edge headless).
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   idempotent:bool,
     *   errors?:array<string,string>
     * }
     */
    public function createPdfForSnapshot(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canCreate($actor)) {
            $this->auditPdfFailure($actor, $snapshotId, null, null, ['role']);
            return [
                'ok' => false,
                'message' => 'You do not have permission to create PDF exports.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            $this->auditPdfFailure($actor, $snapshotId, null, null, ['snapshot_exists']);
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);

        if ((string) ($snapshot['status'] ?? '') !== 'active') {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['snapshot_active']);
            return [
                'ok' => false,
                'message' => 'PDF export requires an active snapshot.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['status' => 'Snapshot is not active.'],
            ];
        }

        $payload = $this->decodePayloadJson($snapshot['payload_json'] ?? null);
        if ($payload === null) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['payload_valid']);
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
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['checksum_present']);
            return [
                'ok' => false,
                'message' => 'Snapshot checksum is missing.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['checksum' => 'Missing checksum.'],
            ];
        }

        $existingPdf = $this->exports->findReadyBySnapshotFormatAndChecksum($snapshotId, 'pdf', $snapshotChecksum);
        if ($existingPdf !== null) {
            $validation = $this->validateReadyArtifact($existingPdf);
            if (!$validation['ok']) {
                $reasons = array_keys($validation['errors']);
                if ($reasons === []) {
                    $reasons = ['pdf_artifact_invalid'];
                }
                $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($existingPdf['id'] ?? 0), $reasons);
                return [
                    'ok' => false,
                    'message' => $validation['message'] . ' Contact an administrator.',
                    'export' => $existingPdf,
                    'idempotent' => false,
                    'errors' => $validation['errors'],
                ];
            }

            $fileChecksum = strtolower((string) ($existingPdf['checksum_sha256'] ?? ''));
            $htmlExport = $this->exports->findReadyHtmlBySnapshotChecksum($snapshotId, $snapshotChecksum);
            $this->exports->insertAudit('report_export.pdf_idempotent_hit', (int) $actor['id'], (int) $existingPdf['id'], [
                'export_id' => (int) $existingPdf['id'],
                'report_snapshot_id' => $snapshotId,
                'source_html_export_id' => is_array($htmlExport) ? (int) ($htmlExport['id'] ?? 0) : null,
                'monthly_report_content_id' => $monthlyId,
                'format' => 'pdf',
                'storage_path' => (string) $existingPdf['storage_path'],
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'engine' => 'edge',
                'actor_user_id' => (int) $actor['id'],
                'rewritten' => false,
            ]);

            return [
                'ok' => true,
                'message' => 'PDF export already exists for this snapshot checksum (idempotent).',
                'export' => $existingPdf,
                'idempotent' => true,
            ];
        }

        $htmlExport = $this->exports->findReadyHtmlBySnapshotChecksum($snapshotId, $snapshotChecksum);
        if ($htmlExport === null) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['html_export_missing']);
            return [
                'ok' => false,
                'message' => 'A ready HTML export is required before creating a PDF export.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['html' => 'HTML export missing.'],
            ];
        }

        $htmlValidation = $this->validateReadyArtifact($htmlExport);
        if (!$htmlValidation['ok']) {
            $reasons = ['html_source_invalid'];
            foreach (array_keys($htmlValidation['errors']) as $key) {
                $reasons[] = 'html_' . $key;
            }
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), $reasons);
            return [
                'ok' => false,
                'message' => 'HTML export source is not valid for PDF generation: ' . $htmlValidation['message'],
                'export' => null,
                'idempotent' => false,
                'errors' => ['html' => $htmlValidation['message']],
            ];
        }

        if (!is_file(self::EDGE_EXE) && !is_file(self::CHROME_EXE)) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['browser_missing']);
            return [
                'ok' => false,
                'message' => 'No allowed browser PDF engine is available on this host.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['engine' => 'Missing.'],
            ];
        }

        $generated = $this->generatePdfFromHtml($snapshot, $htmlExport);
        if (!$generated['ok']) {
            $this->auditPdfFailure(
                $actor,
                $snapshotId,
                $monthlyId,
                (int) ($htmlExport['id'] ?? 0),
                $generated['reasons'] ?? ['pdf_generation_failed']
            );
            return [
                'ok' => false,
                'message' => $generated['message'] ?? 'PDF generation failed.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['pdf' => 'Generation failed.'],
            ];
        }

        $paths = $generated['paths'] ?? null;
        $fileChecksum = (string) ($generated['checksum_sha256'] ?? '');
        $fileSize = (int) ($generated['file_size_bytes'] ?? 0);
        $engine = (string) ($generated['engine'] ?? 'edge');
        $engineVersion = (string) ($generated['engine_version'] ?? '');
        if (!is_array($paths) || $fileChecksum === '' || $fileSize <= 0) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['pdf_output_invalid']);
            return [
                'ok' => false,
                'message' => 'PDF generation produced an invalid artifact.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['pdf' => 'Invalid output.'],
            ];
        }

        $absolute = (string) $paths['absolute'];
        $relative = (string) $paths['relative'];
        $filename = (string) $paths['filename'];
        $exportKey = 'snapshot-' . $snapshotId . '-pdf-v' . (int) $snapshot['version'];

        try {
            $newId = $this->exports->insert([
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => $monthlyId,
                'export_key' => $exportKey,
                'format' => 'pdf',
                'status' => 'ready',
                'storage_disk' => 'local',
                'storage_path' => $relative,
                'filename' => $filename,
                'mime_type' => 'application/pdf',
                'file_size_bytes' => $fileSize,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'created_by' => (int) $actor['id'],
            ]);

            $this->exports->insertAudit('report_export.pdf_created', (int) $actor['id'], $newId, [
                'export_id' => $newId,
                'report_snapshot_id' => $snapshotId,
                'source_html_export_id' => (int) ($htmlExport['id'] ?? 0),
                'monthly_report_content_id' => $monthlyId,
                'format' => 'pdf',
                'storage_path' => $relative,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'engine' => $engine,
                'engine_version' => $engineVersion !== '' ? $engineVersion : null,
                'actor_user_id' => (int) $actor['id'],
                'export_key' => $exportKey,
            ]);

            $created = $this->exports->findById($newId);
            return [
                'ok' => true,
                'message' => 'PDF export created.',
                'export' => $created,
                'idempotent' => false,
            ];
        } catch (Throwable) {
            if (is_file($absolute)) {
                @unlink($absolute);
            }
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['persist_failed']);
            return [
                'ok' => false,
                'message' => 'Could not save PDF export metadata. Please try again.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }
    }

    /**
     * Create next styled HTML export version using iseo_default_v1 (never overwrites v1).
     * Idempotent: if a ready styled version (v>=2) already validates, return it (no v3 in this wave).
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   idempotent:bool,
     *   errors?:array<string,string>
     * }
     */
    public function createStyledHtmlVersionForSnapshot(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canCreate($actor)) {
            $this->auditFailure($actor, $snapshotId, null, ['role']);
            return [
                'ok' => false,
                'message' => 'You do not have permission to create styled HTML exports.',
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
                'message' => 'Styled HTML export requires an active snapshot.',
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

        $template = $this->defaultTemplateSummary();
        $existingStyled = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'html');
        if ($existingStyled !== null) {
            $validation = $this->validateReadyArtifact($existingStyled);
            if (!$validation['ok']) {
                return [
                    'ok' => false,
                    'message' => $validation['message'] . ' Contact an administrator.',
                    'export' => $existingStyled,
                    'idempotent' => false,
                    'errors' => $validation['errors'],
                ];
            }

            $fileChecksum = strtolower((string) ($existingStyled['checksum_sha256'] ?? ''));
            $this->exports->insertAudit('report_export.html_idempotent_hit', (int) $actor['id'], (int) $existingStyled['id'], [
                'export_id' => (int) $existingStyled['id'],
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => (int) $existingStyled['monthly_report_content_id'],
                'format' => 'html',
                'export_key' => (string) ($existingStyled['export_key'] ?? ''),
                'storage_path' => (string) $existingStyled['storage_path'],
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'template_id' => $template['id'],
                'template_version' => $template['version'],
                'actor_user_id' => (int) $actor['id'],
                'styled_version' => true,
            ]);

            return [
                'ok' => true,
                'message' => 'Styled HTML export already exists (idempotent).',
                'export' => $existingStyled,
                'idempotent' => true,
            ];
        }

        $maxVersion = $this->exports->maxExportVersionForSnapshotFormat($snapshotId, 'html');
        $nextVersion = $maxVersion + 1;
        if ($nextVersion < 2) {
            $nextVersion = 2;
        }

        $exportKey = 'snapshot-' . $snapshotId . '-html-v' . $nextVersion;
        $paths = $this->artifactPathForExportVersion($snapshot, 'html', $nextVersion);
        $absolute = $paths['absolute'];
        $relative = $paths['relative'];
        $filename = $paths['filename'];

        if (is_file($absolute)) {
            $this->auditFailure($actor, $snapshotId, (int) $snapshot['monthly_report_content_id'], ['styled_html_path_exists']);
            return [
                'ok' => false,
                'message' => 'Styled HTML export path already exists unexpectedly.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['path' => 'Exists.'],
            ];
        }

        $generatedAt = gmdate('Y-m-d\TH:i:s\Z');
        $html = $this->buildHtml($snapshot, $payload, $generatedAt);

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
                'message' => 'Could not write styled HTML export artifact.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }

        $fileSize = (int) filesize($absolute);
        $fileChecksum = $this->checksumFile($absolute);

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
                'template_id' => ReportTemplate::ID,
                'template_version' => (string) ReportTemplate::VERSION,
                'render_target' => ReportTemplate::RENDER_TARGET_HTML_EXPORT,
                'render_engine' => ReportTemplate::RENDER_ENGINE_PHP_TEMPLATE,
                'render_options_json' => $this->encodeJsonSafe([
                    'export_version' => $nextVersion,
                    'styled_version' => true,
                ]),
                'source_html_export_id' => null,
                'metadata_json' => $this->encodeJsonSafe([
                    'template_id' => ReportTemplate::ID,
                    'template_version' => ReportTemplate::VERSION,
                    'render_target' => ReportTemplate::RENDER_TARGET_HTML_EXPORT,
                    'render_engine' => ReportTemplate::RENDER_ENGINE_PHP_TEMPLATE,
                    'export_version' => $nextVersion,
                ]),
            ]);

            $this->exports->insertAudit('report_export.html_created', (int) $actor['id'], $newId, [
                'export_id' => $newId,
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => (int) $snapshot['monthly_report_content_id'],
                'format' => 'html',
                'storage_path' => $relative,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'actor_user_id' => (int) $actor['id'],
                'export_key' => $exportKey,
                'template_id' => $template['id'],
                'template_version' => $template['version'],
                'styled_version' => true,
                'export_version' => $nextVersion,
            ]);

            $created = $this->exports->findById($newId);
            return [
                'ok' => true,
                'message' => 'Styled HTML export created.',
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
                'message' => 'Could not save styled HTML export metadata. Please try again.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }
    }

    /**
     * Create next styled PDF export version from ready styled HTML (never overwrites v1).
     * Idempotent: if a ready styled PDF (v>=2) already validates, return it (no v3 in this wave).
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   idempotent:bool,
     *   errors?:array<string,string>
     * }
     */
    public function createStyledPdfVersionForSnapshot(int $snapshotId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canCreate($actor)) {
            $this->auditPdfFailure($actor, $snapshotId, null, null, ['role']);
            return [
                'ok' => false,
                'message' => 'You do not have permission to create styled PDF exports.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $snapshot = $this->snapshots->findById($snapshotId);
        if ($snapshot === null) {
            $this->auditPdfFailure($actor, $snapshotId, null, null, ['snapshot_exists']);
            return [
                'ok' => false,
                'message' => 'Snapshot not found.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);

        if ((string) ($snapshot['status'] ?? '') !== 'active') {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['snapshot_active']);
            return [
                'ok' => false,
                'message' => 'Styled PDF export requires an active snapshot.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['status' => 'Snapshot is not active.'],
            ];
        }

        $snapshotChecksum = (string) ($snapshot['checksum_sha256'] ?? '');
        if ($snapshotChecksum === '') {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['checksum_present']);
            return [
                'ok' => false,
                'message' => 'Snapshot checksum is missing.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['checksum' => 'Missing checksum.'],
            ];
        }

        $template = $this->defaultTemplateSummary();
        $existingStyledPdf = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'pdf');
        if ($existingStyledPdf !== null) {
            $validation = $this->validateReadyArtifact($existingStyledPdf);
            if (!$validation['ok']) {
                $reasons = array_keys($validation['errors']);
                if ($reasons === []) {
                    $reasons = ['pdf_artifact_invalid'];
                }
                $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($existingStyledPdf['id'] ?? 0), $reasons);
                return [
                    'ok' => false,
                    'message' => $validation['message'] . ' Contact an administrator.',
                    'export' => $existingStyledPdf,
                    'idempotent' => false,
                    'errors' => $validation['errors'],
                ];
            }

            $fileChecksum = strtolower((string) ($existingStyledPdf['checksum_sha256'] ?? ''));
            $styledHtml = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'html');
            $this->exports->insertAudit('report_export.pdf_idempotent_hit', (int) $actor['id'], (int) $existingStyledPdf['id'], [
                'export_id' => (int) $existingStyledPdf['id'],
                'report_snapshot_id' => $snapshotId,
                'source_html_export_id' => is_array($styledHtml) ? (int) ($styledHtml['id'] ?? 0) : null,
                'monthly_report_content_id' => $monthlyId,
                'format' => 'pdf',
                'export_key' => (string) ($existingStyledPdf['export_key'] ?? ''),
                'storage_path' => (string) $existingStyledPdf['storage_path'],
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'engine' => 'edge',
                'template_id' => $template['id'],
                'template_version' => $template['version'],
                'actor_user_id' => (int) $actor['id'],
                'rewritten' => false,
                'styled_version' => true,
            ]);

            return [
                'ok' => true,
                'message' => 'Styled PDF export already exists (idempotent).',
                'export' => $existingStyledPdf,
                'idempotent' => true,
            ];
        }

        $htmlExport = $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'html');
        if ($htmlExport === null) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, null, ['styled_html_export_missing']);
            return [
                'ok' => false,
                'message' => 'A ready styled HTML export is required before creating a styled PDF export.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['html' => 'Styled HTML export missing.'],
            ];
        }

        $htmlValidation = $this->validateReadyArtifact($htmlExport);
        if (!$htmlValidation['ok']) {
            $reasons = ['html_source_invalid'];
            foreach (array_keys($htmlValidation['errors']) as $key) {
                $reasons[] = 'html_' . $key;
            }
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), $reasons);
            return [
                'ok' => false,
                'message' => 'Styled HTML export source is not valid for PDF generation: ' . $htmlValidation['message'],
                'export' => null,
                'idempotent' => false,
                'errors' => ['html' => $htmlValidation['message']],
            ];
        }

        if (!is_file(self::EDGE_EXE) && !is_file(self::CHROME_EXE)) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['browser_missing']);
            return [
                'ok' => false,
                'message' => 'No allowed browser PDF engine is available on this host.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['engine' => 'Missing.'],
            ];
        }

        $maxVersion = $this->exports->maxExportVersionForSnapshotFormat($snapshotId, 'pdf');
        $nextVersion = $maxVersion + 1;
        if ($nextVersion < 2) {
            $nextVersion = 2;
        }

        $generated = $this->generatePdfFromHtml(
            $snapshot,
            $htmlExport,
            $nextVersion,
            self::STYLED_BROWSER_TEMP_ROOT
        );
        if (!$generated['ok']) {
            $this->auditPdfFailure(
                $actor,
                $snapshotId,
                $monthlyId,
                (int) ($htmlExport['id'] ?? 0),
                $generated['reasons'] ?? ['pdf_generation_failed']
            );
            return [
                'ok' => false,
                'message' => $generated['message'] ?? 'Styled PDF generation failed.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['pdf' => 'Generation failed.'],
            ];
        }

        $paths = $generated['paths'] ?? null;
        $fileChecksum = (string) ($generated['checksum_sha256'] ?? '');
        $fileSize = (int) ($generated['file_size_bytes'] ?? 0);
        $engine = (string) ($generated['engine'] ?? 'edge');
        $engineVersion = (string) ($generated['engine_version'] ?? '');
        if (!is_array($paths) || $fileChecksum === '' || $fileSize <= 0) {
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['pdf_output_invalid']);
            return [
                'ok' => false,
                'message' => 'Styled PDF generation produced an invalid artifact.',
                'export' => null,
                'idempotent' => false,
                'errors' => ['pdf' => 'Invalid output.'],
            ];
        }

        $absolute = (string) $paths['absolute'];
        $relative = (string) $paths['relative'];
        $filename = (string) $paths['filename'];
        $exportKey = 'snapshot-' . $snapshotId . '-pdf-v' . $nextVersion;

        try {
            $newId = $this->exports->insert([
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => $monthlyId,
                'export_key' => $exportKey,
                'format' => 'pdf',
                'status' => 'ready',
                'storage_disk' => 'local',
                'storage_path' => $relative,
                'filename' => $filename,
                'mime_type' => 'application/pdf',
                'file_size_bytes' => $fileSize,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'created_by' => (int) $actor['id'],
                'template_id' => ReportTemplate::ID,
                'template_version' => (string) ReportTemplate::VERSION,
                'render_target' => ReportTemplate::RENDER_TARGET_PDF_EXPORT,
                'render_engine' => ReportTemplate::RENDER_ENGINE_EDGE_HEADLESS_PDF,
                'render_options_json' => $this->encodeJsonSafe([
                    'export_version' => $nextVersion,
                    'styled_version' => true,
                    'engine' => $engine,
                    'engine_version' => $engineVersion !== '' ? $engineVersion : null,
                ]),
                'source_html_export_id' => (int) ($htmlExport['id'] ?? 0) > 0
                    ? (int) $htmlExport['id']
                    : null,
                'metadata_json' => $this->encodeJsonSafe([
                    'template_id' => ReportTemplate::ID,
                    'template_version' => ReportTemplate::VERSION,
                    'render_target' => ReportTemplate::RENDER_TARGET_PDF_EXPORT,
                    'render_engine' => ReportTemplate::RENDER_ENGINE_EDGE_HEADLESS_PDF,
                    'source_html_export_id' => (int) ($htmlExport['id'] ?? 0) > 0
                        ? (int) $htmlExport['id']
                        : null,
                    'export_version' => $nextVersion,
                ]),
            ]);

            $this->exports->insertAudit('report_export.pdf_created', (int) $actor['id'], $newId, [
                'export_id' => $newId,
                'report_snapshot_id' => $snapshotId,
                'source_html_export_id' => (int) ($htmlExport['id'] ?? 0),
                'monthly_report_content_id' => $monthlyId,
                'format' => 'pdf',
                'storage_path' => $relative,
                'checksum_sha256' => $fileChecksum,
                'source_snapshot_checksum_sha256' => $snapshotChecksum,
                'engine' => $engine,
                'engine_version' => $engineVersion !== '' ? $engineVersion : null,
                'actor_user_id' => (int) $actor['id'],
                'export_key' => $exportKey,
                'template_id' => $template['id'],
                'template_version' => $template['version'],
                'styled_version' => true,
                'export_version' => $nextVersion,
            ]);

            $created = $this->exports->findById($newId);
            return [
                'ok' => true,
                'message' => 'Styled PDF export created.',
                'export' => $created,
                'idempotent' => false,
            ];
        } catch (Throwable) {
            if (is_file($absolute)) {
                @unlink($absolute);
            }
            $this->auditPdfFailure($actor, $snapshotId, $monthlyId, (int) ($htmlExport['id'] ?? 0), ['persist_failed']);
            return [
                'ok' => false,
                'message' => 'Could not save styled PDF export metadata. Please try again.',
                'export' => null,
                'idempotent' => false,
                'errors' => [],
            ];
        }
    }

    /**
     * DB-first template label. Never invent iseo_default_v1 for NULL metadata rows.
     */
    public function templateLabelForExport(array $export): string
    {
        $templateId = trim((string) ($export['template_id'] ?? ''));
        $templateVersion = trim((string) ($export['template_version'] ?? ''));
        if ($templateId !== '' && $templateVersion !== '') {
            return $templateId . ' v' . $templateVersion;
        }
        return $this->legacyTemplateLabel();
    }

    public function renderTargetLabelForExport(array $export): string
    {
        $target = trim((string) ($export['render_target'] ?? ''));
        return match ($target) {
            ReportTemplate::RENDER_TARGET_HTML_EXPORT => 'HTML export',
            ReportTemplate::RENDER_TARGET_PDF_EXPORT => 'PDF export',
            '' => 'not recorded',
            default => $target,
        };
    }

    public function renderEngineLabelForExport(array $export): string
    {
        $engine = trim((string) ($export['render_engine'] ?? ''));
        return match ($engine) {
            ReportTemplate::RENDER_ENGINE_PHP_TEMPLATE => 'PHP template renderer',
            ReportTemplate::RENDER_ENGINE_EDGE_HEADLESS_PDF => 'Edge headless PDF',
            '' => 'not recorded',
            default => $engine,
        };
    }

    /**
     * @return array{id:int,export_key:string,label:string,status:?string}|null
     */
    public function sourceHtmlSummaryForExport(array $export): ?array
    {
        $sourceId = isset($export['source_html_export_id']) ? (int) $export['source_html_export_id'] : 0;
        if ($sourceId <= 0) {
            return null;
        }

        $key = trim((string) ($export['source_html_export_key'] ?? ''));
        $status = isset($export['source_html_export_status'])
            ? (string) $export['source_html_export_status']
            : null;

        if ($key === '') {
            try {
                $source = $this->exports->findById($sourceId);
            } catch (Throwable) {
                $source = null;
            }
            if (is_array($source)) {
                $key = trim((string) ($source['export_key'] ?? ''));
                $status = isset($source['status']) ? (string) $source['status'] : $status;
            }
        }

        $label = '#' . $sourceId;
        if ($key !== '') {
            $label .= ' ' . $key;
        }

        return [
            'id' => $sourceId,
            'export_key' => $key,
            'label' => $label,
            'status' => $status,
        ];
    }

    public function isLegacyTemplateMetadata(array $export): bool
    {
        $templateId = trim((string) ($export['template_id'] ?? ''));
        $templateVersion = trim((string) ($export['template_version'] ?? ''));
        return $templateId === '' || $templateVersion === '';
    }

    /**
     * @param array<string, mixed> $export
     * @return array<string, mixed>
     */
    public function withDisplayMetadata(array $export): array
    {
        $source = $this->sourceHtmlSummaryForExport($export);
        $export['display_template_label'] = $this->templateLabelForExport($export);
        $export['display_render_target_label'] = $this->renderTargetLabelForExport($export);
        $export['display_render_engine_label'] = $this->renderEngineLabelForExport($export);
        $export['display_source_html_label'] = is_array($source) ? $source['label'] : 'not recorded';
        $export['display_source_html'] = $source;
        $export['is_legacy_template_metadata'] = $this->isLegacyTemplateMetadata($export);
        $export['has_recorded_template'] = !$export['is_legacy_template_metadata'];
        return $export;
    }

    public function parseExportVersionFromKey(string $exportKey): ?int
    {
        if (preg_match('/-v(\d+)$/', trim($exportKey), $m) === 1) {
            return (int) $m[1];
        }
        return null;
    }

    /**
     * Prefer DB template metadata; fall back to export_key version for display badges only.
     */
    public function isStyledExport(array $export): bool
    {
        if (!$this->isLegacyTemplateMetadata($export)) {
            return true;
        }
        $version = $this->parseExportVersionFromKey((string) ($export['export_key'] ?? ''));
        return $version !== null && $version >= 2;
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyStyledHtmlForSnapshot(int $snapshotId): ?array
    {
        return $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'html');
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyStyledPdfForSnapshot(int $snapshotId): ?array
    {
        return $this->exports->findReadyStyledVersionForSnapshotFormat($snapshotId, 'pdf');
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
            'export' => $this->withDisplayMetadata($export),
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
        $validation = $this->validateReadyArtifact($export);
        if (!$validation['ok']) {
            return [
                'ok' => false,
                'message' => $validation['message'],
                'export' => $export,
                'absolute_path' => null,
                'errors' => $validation['errors'],
            ];
        }

        return [
            'ok' => true,
            'message' => 'Ready to stream.',
            'export' => $export,
            'absolute_path' => $validation['absolute_path'],
        ];
    }

    /**
     * Validate ready export metadata against on-disk artifact (path/MIME/size/checksum/magic).
     * User-facing messages never include absolute filesystem paths.
     *
     * @param array<string, mixed> $export
     * @return array{
     *   ok:bool,
     *   message:string,
     *   absolute_path:?string,
     *   errors:array<string,string>
     * }
     */
    public function validateReadyArtifact(array $export): array
    {
        if ((string) ($export['status'] ?? '') !== 'ready') {
            return [
                'ok' => false,
                'message' => 'Export is not ready for download.',
                'absolute_path' => null,
                'errors' => ['status' => 'Not ready.'],
            ];
        }

        $format = strtolower(trim((string) ($export['format'] ?? '')));
        if ($format !== 'html' && $format !== 'pdf') {
            return [
                'ok' => false,
                'message' => 'Export format is not supported for download.',
                'absolute_path' => null,
                'errors' => ['format' => 'Unknown.'],
            ];
        }

        $mime = strtolower(trim((string) ($export['mime_type'] ?? '')));
        if (!$this->isAllowedMimeForFormat($format, $mime)) {
            return [
                'ok' => false,
                'message' => 'Export MIME type does not match format.',
                'absolute_path' => null,
                'errors' => ['mime' => 'Mismatch.'],
            ];
        }

        $filename = (string) ($export['filename'] ?? '');
        if (!$this->filenameMatchesFormat($filename, $format)) {
            return [
                'ok' => false,
                'message' => 'Export filename extension does not match format.',
                'absolute_path' => null,
                'errors' => ['filename' => 'Extension mismatch.'],
            ];
        }

        $storagePath = (string) ($export['storage_path'] ?? '');
        if (!$this->isRelativeStoragePath($storagePath)) {
            return [
                'ok' => false,
                'message' => 'Export storage path is invalid.',
                'absolute_path' => null,
                'errors' => ['path' => 'Invalid.'],
            ];
        }

        if (!$this->storagePathExtensionMatchesFormat($storagePath, $format)) {
            return [
                'ok' => false,
                'message' => 'Export storage path extension does not match format.',
                'absolute_path' => null,
                'errors' => ['path' => 'Extension mismatch.'],
            ];
        }

        $absolute = $this->resolveStoragePath($storagePath);
        if ($absolute === null || !is_file($absolute)) {
            return [
                'ok' => false,
                'message' => 'Export artifact file is missing.',
                'absolute_path' => null,
                'errors' => ['file' => 'Missing.'],
            ];
        }

        $expectedSize = isset($export['file_size_bytes']) ? (int) $export['file_size_bytes'] : 0;
        $actualSize = (int) filesize($absolute);
        if ($expectedSize > 0 && $actualSize !== $expectedSize) {
            return [
                'ok' => false,
                'message' => 'Export artifact size does not match metadata.',
                'absolute_path' => null,
                'errors' => ['size' => 'Mismatch.'],
            ];
        }
        if ($actualSize <= 0) {
            return [
                'ok' => false,
                'message' => 'Export artifact is empty.',
                'absolute_path' => null,
                'errors' => ['size' => 'Empty.'],
            ];
        }

        $storedChecksum = strtolower(trim((string) ($export['checksum_sha256'] ?? '')));
        if ($storedChecksum === '') {
            return [
                'ok' => false,
                'message' => 'Export checksum metadata is missing.',
                'absolute_path' => null,
                'errors' => ['checksum' => 'Missing.'],
            ];
        }
        $fileChecksum = strtolower($this->checksumFile($absolute));
        if ($fileChecksum === '' || !hash_equals($storedChecksum, $fileChecksum)) {
            return [
                'ok' => false,
                'message' => 'Export artifact checksum mismatch.',
                'absolute_path' => null,
                'errors' => ['checksum' => 'Mismatch.'],
            ];
        }

        if ($format === 'pdf') {
            $magic = $this->readFileMagic($absolute, 4);
            if ($magic !== '%PDF') {
                return [
                    'ok' => false,
                    'message' => 'PDF artifact magic bytes are invalid.',
                    'absolute_path' => null,
                    'errors' => ['pdf_magic' => 'Invalid.'],
                ];
            }
        }

        return [
            'ok' => true,
            'message' => 'Artifact validated.',
            'absolute_path' => $absolute,
            'errors' => [],
        ];
    }

    /**
     * Safe Content-Type for streaming (never trust arbitrary DB MIME blindly beyond allowlist).
     */
    public function safeDownloadMime(array $export): string
    {
        $format = strtolower(trim((string) ($export['format'] ?? '')));
        if ($format === 'pdf') {
            return 'application/pdf';
        }
        return 'text/html; charset=UTF-8';
    }

    /**
     * Sanitize attachment filename for Content-Disposition (ASCII fallback).
     */
    public function safeDownloadFilename(array $export): string
    {
        $filename = trim((string) ($export['filename'] ?? ''));
        $format = strtolower(trim((string) ($export['format'] ?? '')));
        $fallback = $format === 'pdf' ? 'export.pdf' : 'export.html';
        if ($filename === '') {
            return $fallback;
        }
        $filename = str_replace(['"', "\r", "\n", "\0", '/', '\\'], '', $filename);
        $filename = basename($filename);
        if ($filename === '' || $filename === '.' || $filename === '..') {
            return $fallback;
        }
        if (!$this->filenameMatchesFormat($filename, $format === 'pdf' ? 'pdf' : 'html')) {
            return $fallback;
        }
        return $filename;
    }

    /**
     * @param array<string, mixed> $snapshot
     * @param array<string, mixed> $payload
     */
    public function buildHtml(array $snapshot, array $payload, string $generatedAt): string
    {
        return $this->renderer->render($snapshot, $payload, $generatedAt);
    }

    /**
     * @param array<string, mixed> $snapshot
     * @return array{relative:string,absolute:string,filename:string}
     */
    public function artifactPath(array $snapshot): array
    {
        return $this->artifactPathForFormat($snapshot, 'html');
    }

    /**
     * @param array<string, mixed> $snapshot
     * @return array{relative:string,absolute:string,filename:string}
     */
    public function artifactPathForFormat(array $snapshot, string $format): array
    {
        $version = (int) ($snapshot['version'] ?? 1);
        if ($version < 1) {
            $version = 1;
        }
        return $this->artifactPathForExportVersion($snapshot, $format, $version);
    }

    /**
     * Versioned export artifact paths: monthly-{id}-v{N}.{ext}
     *
     * @param array<string, mixed> $snapshot
     * @return array{relative:string,absolute:string,filename:string}
     */
    public function artifactPathForExportVersion(array $snapshot, string $format, int $exportVersion): array
    {
        $monthlyId = (int) ($snapshot['monthly_report_content_id'] ?? 0);
        $snapshotId = (int) ($snapshot['id'] ?? 0);
        if ($exportVersion < 1) {
            $exportVersion = 1;
        }
        $ext = $format === 'pdf' ? 'pdf' : 'html';
        $filename = 'monthly-' . $monthlyId . '-v' . $exportVersion . '.' . $ext;

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

    /**
     * @param array<string, mixed> $snapshot
     * @param array<string, mixed> $htmlExport
     * @return array{
     *   ok:bool,
     *   message?:string,
     *   reasons?:list<string>,
     *   paths?:array{relative:string,absolute:string,filename:string},
     *   checksum_sha256?:string,
     *   file_size_bytes?:int,
     *   engine?:string,
     *   engine_version?:string
     * }
     */
    public function generatePdfFromHtml(
        array $snapshot,
        array $htmlExport,
        ?int $exportVersion = null,
        ?string $browserTempRoot = null
    ): array {
        $htmlAbsolute = $this->resolveStoragePath((string) ($htmlExport['storage_path'] ?? ''));
        if ($htmlAbsolute === null || !is_file($htmlAbsolute)) {
            return [
                'ok' => false,
                'message' => 'HTML export artifact file is missing.',
                'reasons' => ['html_file_missing'],
            ];
        }

        if ($exportVersion === null) {
            $parsed = $this->parseExportVersionFromKey((string) ($htmlExport['export_key'] ?? ''));
            $exportVersion = $parsed ?? (int) ($snapshot['version'] ?? 1);
        }
        if ($exportVersion < 1) {
            $exportVersion = 1;
        }

        $paths = $this->artifactPathForExportVersion($snapshot, 'pdf', $exportVersion);
        $pdfAbsolute = $paths['absolute'];
        $dir = dirname($pdfAbsolute);
        if (!is_dir($dir) && !mkdir($dir, 0755, true) && !is_dir($dir)) {
            return [
                'ok' => false,
                'message' => 'Could not create PDF export storage directory.',
                'reasons' => ['mkdir_failed'],
            ];
        }

        if (is_file($pdfAbsolute)) {
            @unlink($pdfAbsolute);
        }

        $tempRoot = $browserTempRoot !== null && $browserTempRoot !== ''
            ? $browserTempRoot
            : self::BROWSER_TEMP_ROOT;

        $engines = [];
        if (is_file(self::EDGE_EXE)) {
            $engines[] = ['name' => 'edge', 'exe' => self::EDGE_EXE];
        }
        if (is_file(self::CHROME_EXE)) {
            $engines[] = ['name' => 'chrome', 'exe' => self::CHROME_EXE];
        }

        $lastMessage = 'PDF generation failed.';
        $lastReasons = ['pdf_generation_failed'];
        foreach ($engines as $engine) {
            $unique = bin2hex(random_bytes(8));
            $profileDir = $tempRoot . DIRECTORY_SEPARATOR . $engine['name'] . '-profile-' . $unique;
            if (!is_dir($tempRoot) && !mkdir($tempRoot, 0755, true) && !is_dir($tempRoot)) {
                return [
                    'ok' => false,
                    'message' => 'Could not create browser temp directory.',
                    'reasons' => ['temp_mkdir_failed'],
                ];
            }
            if (!is_dir($profileDir) && !mkdir($profileDir, 0755, true) && !is_dir($profileDir)) {
                return [
                    'ok' => false,
                    'message' => 'Could not create browser profile directory.',
                    'reasons' => ['profile_mkdir_failed'],
                ];
            }

            $cmd = $this->browserPdfCommand(
                (string) $engine['exe'],
                $htmlAbsolute,
                $pdfAbsolute,
                $profileDir
            );
            $run = $this->runBrowserCommand($cmd);
            $this->cleanupDirectory($profileDir);

            if (!$run['ok']) {
                $lastMessage = 'Browser PDF engine failed (' . $engine['name'] . ').';
                $lastReasons = ['browser_failed_' . $engine['name']];
                if (is_file($pdfAbsolute)) {
                    @unlink($pdfAbsolute);
                }
                // Edge first; try Chrome fallback only when Edge path was attempted and failed.
                continue;
            }

            $validation = $this->validatePdf($pdfAbsolute);
            if (!$validation['ok']) {
                $lastMessage = $validation['message'] ?? 'PDF validation failed.';
                $lastReasons = $validation['reasons'] ?? ['pdf_invalid'];
                if (is_file($pdfAbsolute)) {
                    @unlink($pdfAbsolute);
                }
                continue;
            }

            return [
                'ok' => true,
                'paths' => $paths,
                'checksum_sha256' => $this->checksumFile($pdfAbsolute),
                'file_size_bytes' => (int) filesize($pdfAbsolute),
                'engine' => (string) $engine['name'],
                'engine_version' => $this->browserVersion((string) $engine['exe']) ?? '',
            ];
        }

        return [
            'ok' => false,
            'message' => $lastMessage,
            'reasons' => $lastReasons,
        ];
    }

    /**
     * @return list<string>
     */
    public function browserPdfCommand(string $exe, string $htmlPath, string $pdfPath, string $userDataDir): array
    {
        $fileUrl = $this->toFileUrl($htmlPath);
        return [
            $exe,
            '--headless',
            '--disable-gpu',
            '--no-first-run',
            '--disable-extensions',
            '--disable-background-networking',
            '--disable-sync',
            '--no-default-browser-check',
            '--user-data-dir=' . $userDataDir,
            '--print-to-pdf=' . $pdfPath,
            $fileUrl,
        ];
    }

    /**
     * @return array{ok:bool,message?:string,reasons?:list<string>}
     */
    public function validatePdf(string $pdfPath): array
    {
        if (!is_file($pdfPath)) {
            return [
                'ok' => false,
                'message' => 'PDF artifact was not created.',
                'reasons' => ['pdf_missing'],
            ];
        }

        $size = (int) filesize($pdfPath);
        if ($size <= 0) {
            return [
                'ok' => false,
                'message' => 'PDF artifact is empty.',
                'reasons' => ['pdf_empty'],
            ];
        }

        $magic = $this->readFileMagic($pdfPath, 4);
        if ($magic !== '%PDF') {
            return [
                'ok' => false,
                'message' => 'PDF artifact magic bytes are invalid.',
                'reasons' => ['pdf_magic'],
            ];
        }

        $resolved = realpath($pdfPath);
        $storageRoot = realpath(base_path(self::STORAGE_REL_ROOT));
        $publicRoot = realpath(base_path('public'));
        if ($resolved === false) {
            return [
                'ok' => false,
                'message' => 'PDF path could not be resolved.',
                'reasons' => ['pdf_path'],
            ];
        }
        $resolvedNorm = str_replace('\\', '/', $resolved);
        if ($storageRoot !== false) {
            $rootNorm = rtrim(str_replace('\\', '/', $storageRoot), '/');
            if (!str_starts_with($resolvedNorm, $rootNorm . '/') && $resolvedNorm !== $rootNorm) {
                return [
                    'ok' => false,
                    'message' => 'PDF path is outside allowed storage.',
                    'reasons' => ['pdf_outside_storage'],
                ];
            }
        }
        if ($publicRoot !== false) {
            $publicNorm = rtrim(str_replace('\\', '/', $publicRoot), '/');
            if (str_starts_with($resolvedNorm, $publicNorm . '/') || $resolvedNorm === $publicNorm) {
                return [
                    'ok' => false,
                    'message' => 'PDF path must not be under public webroot.',
                    'reasons' => ['pdf_in_public'],
                ];
            }
        }

        return ['ok' => true];
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
     * @param array<string, mixed> $snapshot
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param array<string, mixed>|null $htmlExport
     */
    public function canCreatePdfForSnapshot(array $snapshot, array $actor, ?array $htmlExport = null): bool
    {
        if (!$this->canCreateExportForSnapshot($snapshot, $actor)) {
            return false;
        }
        if ($htmlExport === null) {
            $snapshotId = (int) ($snapshot['id'] ?? 0);
            if ($snapshotId <= 0) {
                return false;
            }
            $htmlExport = $this->exports->findReadyBySnapshotAndFormat($snapshotId, 'html');
        }
        return is_array($htmlExport)
            && (string) ($htmlExport['status'] ?? '') === 'ready'
            && (is_file(self::EDGE_EXE) || is_file(self::CHROME_EXE));
    }

    /**
     * @return array<string, mixed>|null
     */
    public function findReadyHtmlForSnapshot(int $snapshotId): ?array
    {
        return $this->getReadyExportForSnapshotFormat($snapshotId, 'html');
    }

    /**
     * @return array<string, mixed>|null
     */
    public function getReadyExportForSnapshotFormat(int $snapshotId, string $format): ?array
    {
        if ($snapshotId <= 0 || $format === '') {
            return null;
        }
        return $this->exports->findReadyBySnapshotAndFormat($snapshotId, $format);
    }

    /**
     * @param list<string> $command
     * @return array{ok:bool,exit_code:int,stdout:string,stderr:string}
     */
    private function runBrowserCommand(array $command): array
    {
        if ($command === [] || !is_file((string) $command[0])) {
            return [
                'ok' => false,
                'exit_code' => -1,
                'stdout' => '',
                'stderr' => 'Executable missing.',
            ];
        }

        $descriptors = [
            0 => ['pipe', 'r'],
            1 => ['pipe', 'w'],
            2 => ['pipe', 'w'],
        ];

        $process = @proc_open(
            $command,
            $descriptors,
            $pipes,
            null,
            null,
            ['bypass_shell' => true]
        );

        if (!is_resource($process)) {
            return [
                'ok' => false,
                'exit_code' => -1,
                'stdout' => '',
                'stderr' => 'Could not start browser process.',
            ];
        }

        fclose($pipes[0]);
        stream_set_blocking($pipes[1], false);
        stream_set_blocking($pipes[2], false);

        $stdout = '';
        $stderr = '';
        $deadline = microtime(true) + self::PDF_TIMEOUT_SECONDS;
        $status = proc_get_status($process);

        while ($status['running']) {
            $stdout .= (string) stream_get_contents($pipes[1]);
            $stderr .= (string) stream_get_contents($pipes[2]);
            if (microtime(true) >= $deadline) {
                proc_terminate($process, 9);
                $stdout .= (string) stream_get_contents($pipes[1]);
                $stderr .= (string) stream_get_contents($pipes[2]);
                fclose($pipes[1]);
                fclose($pipes[2]);
                proc_close($process);
                return [
                    'ok' => false,
                    'exit_code' => -1,
                    'stdout' => $stdout,
                    'stderr' => trim($stderr . "\nTimeout after " . self::PDF_TIMEOUT_SECONDS . 's'),
                ];
            }
            usleep(100000);
            $status = proc_get_status($process);
        }

        $stdout .= (string) stream_get_contents($pipes[1]);
        $stderr .= (string) stream_get_contents($pipes[2]);
        fclose($pipes[1]);
        fclose($pipes[2]);
        $exitCode = proc_close($process);
        if ($exitCode === -1 && isset($status['exitcode'])) {
            $exitCode = (int) $status['exitcode'];
        }

        $pdfTarget = null;
        foreach ($command as $arg) {
            if (is_string($arg) && str_starts_with($arg, '--print-to-pdf=')) {
                $pdfTarget = substr($arg, strlen('--print-to-pdf='));
                break;
            }
        }

        $ok = is_string($pdfTarget) && is_file($pdfTarget) && filesize($pdfTarget) > 0;
        return [
            'ok' => $ok,
            'exit_code' => $exitCode,
            'stdout' => $stdout,
            'stderr' => $stderr,
        ];
    }

    private function toFileUrl(string $absolutePath): string
    {
        $normalized = str_replace('\\', '/', $absolutePath);
        if (preg_match('#^[A-Za-z]:/#', $normalized) === 1) {
            return 'file:///' . $normalized;
        }
        return 'file://' . $normalized;
    }

    private function browserVersion(string $exe): ?string
    {
        $dir = dirname($exe);
        if (!is_dir($dir)) {
            return null;
        }
        $entries = @scandir($dir);
        if (!is_array($entries)) {
            return null;
        }
        foreach ($entries as $entry) {
            if (preg_match('/^\d+\.\d+\.\d+\.\d+$/', $entry) === 1 && is_dir($dir . DIRECTORY_SEPARATOR . $entry)) {
                return $entry;
            }
        }
        return null;
    }

    private function cleanupDirectory(string $dir): void
    {
        if (!is_dir($dir)) {
            return;
        }
        try {
            $iterator = new \RecursiveIteratorIterator(
                new \RecursiveDirectoryIterator($dir, \FilesystemIterator::SKIP_DOTS),
                \RecursiveIteratorIterator::CHILD_FIRST
            );
            foreach ($iterator as $item) {
                if (!$item instanceof \SplFileInfo) {
                    continue;
                }
                $path = $item->getPathname();
                if ($item->isDir()) {
                    @rmdir($path);
                } else {
                    @unlink($path);
                }
            }
            @rmdir($dir);
        } catch (Throwable) {
            // Temp cleanup is best-effort.
        }
    }

    private function resolveStoragePath(string $storagePath): ?string
    {
        if (!$this->isRelativeStoragePath($storagePath)) {
            return null;
        }

        $normalized = ltrim(str_replace('\\', '/', trim($storagePath)), '/');
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

        $rootNorm = rtrim(str_replace('\\', '/', (string) $root), '/');
        $fileNorm = str_replace('\\', '/', $resolved);
        if ($rootNorm === '' || (!str_starts_with($fileNorm, $rootNorm . '/') && $fileNorm !== $rootNorm)) {
            return null;
        }

        $publicRoot = realpath(base_path('public'));
        if ($publicRoot !== false) {
            $publicNorm = rtrim(str_replace('\\', '/', $publicRoot), '/');
            if (str_starts_with($fileNorm, $publicNorm . '/') || $fileNorm === $publicNorm) {
                return null;
            }
        }

        return $resolved;
    }

    private function isRelativeStoragePath(string $storagePath): bool
    {
        $storagePath = trim(str_replace('\\', '/', $storagePath));
        if ($storagePath === '' || str_contains($storagePath, "\0")) {
            return false;
        }
        if (str_contains($storagePath, '..')) {
            return false;
        }
        // Reject absolute / UNC / drive-letter paths stored in metadata.
        if (str_starts_with($storagePath, '/') || str_starts_with($storagePath, '//')) {
            return false;
        }
        if (preg_match('#^[A-Za-z]:/#', $storagePath) === 1) {
            return false;
        }
        if (str_starts_with($storagePath, 'file:')) {
            return false;
        }
        return str_starts_with($storagePath, self::STORAGE_REL_ROOT . '/');
    }

    private function isAllowedMimeForFormat(string $format, string $mime): bool
    {
        $mime = strtolower(trim($mime));
        if ($format === 'pdf') {
            return $mime === 'application/pdf';
        }
        if ($format === 'html') {
            return $mime === 'text/html' || str_starts_with($mime, 'text/html;');
        }
        return false;
    }

    private function filenameMatchesFormat(string $filename, string $format): bool
    {
        $filename = basename(str_replace('\\', '/', $filename));
        if ($filename === '' || $filename === '.' || $filename === '..') {
            return false;
        }
        $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
        if ($format === 'pdf') {
            return $ext === 'pdf';
        }
        if ($format === 'html') {
            return $ext === 'html' || $ext === 'htm';
        }
        return false;
    }

    private function storagePathExtensionMatchesFormat(string $storagePath, string $format): bool
    {
        $normalized = str_replace('\\', '/', $storagePath);
        return $this->filenameMatchesFormat(basename($normalized), $format);
    }

    private function readFileMagic(string $path, int $length): string
    {
        if ($length <= 0 || !is_file($path)) {
            return '';
        }
        $fh = fopen($path, 'rb');
        if ($fh === false) {
            return '';
        }
        $magic = fread($fh, $length);
        fclose($fh);
        return is_string($magic) ? $magic : '';
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
     * Safe JSON encode for DB-09 metadata columns (no secrets; empty → null).
     *
     * @param array<string, mixed> $data
     */
    private function encodeJsonSafe(array $data): ?string
    {
        if ($data === []) {
            return null;
        }
        unset($data['password'], $data['password_hash'], $data['hash'], $data['token'], $data['session']);
        try {
            $json = json_encode($data, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
            return is_string($json) ? $json : null;
        } catch (Throwable) {
            return null;
        }
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

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param list<string> $reasons
     */
    private function auditPdfFailure(
        array $actor,
        int $snapshotId,
        ?int $monthlyId,
        ?int $sourceHtmlExportId,
        array $reasons
    ): void {
        try {
            $this->exports->insertAudit('report_export.pdf_creation_failed', (int) $actor['id'], null, [
                'report_snapshot_id' => $snapshotId,
                'monthly_report_content_id' => $monthlyId,
                'source_html_export_id' => $sourceHtmlExportId,
                'format' => 'pdf',
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
