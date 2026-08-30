<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\ReportExportRepository;
use Iseo\Repositories\ReportExportShareRepository;
use Iseo\Support\SafeToken;
use Throwable;

/**
 * MVP tokenized public share for ready styled PDF exports.
 */
final class ReportExportShareService
{
    private const DEFAULT_EXPIRY_DAYS = 30;

    /** @var list<string> */
    private const VIEW_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    /** @var list<string> */
    private const MANAGE_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
    ];

    public function __construct(
        private ReportExportShareRepository $shares,
        private ReportExportRepository $exports,
        private ReportExportService $exportService,
        private DatabaseService $db,
        private ConfigService $config
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
    public function canManage(?array $user): bool
    {
        return $this->userHasAnyRole($user, self::MANAGE_ROLES);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   shares:list<array<string,mixed>>,
     *   active_share:?array<string,mixed>,
     *   eligibility:array{eligible:bool,reason:string,code:string},
     *   can_manage:bool,
     *   plaintext_share_url:?string,
     *   errors?:array<string,string>
     * }
     */
    public function listForExport(int $exportId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canView($actor)) {
            return [
                'ok' => false,
                'message' => 'Недостаточно прав.',
                'export' => null,
                'shares' => [],
                'active_share' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Недостаточно прав.', 'code' => 'role'],
                'can_manage' => false,
                'plaintext_share_url' => null,
                'errors' => ['role' => 'Недостаточно прав.'],
            ];
        }

        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return [
                'ok' => false,
                'message' => 'Файл отчета не найден.',
                'export' => null,
                'shares' => [],
                'active_share' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Файл отчета не найден.', 'code' => 'missing'],
                'can_manage' => $this->canManage($actor),
                'plaintext_share_url' => null,
                'errors' => ['id' => 'Не найдено.'],
            ];
        }

        $eligibility = $this->evaluateEligibility($export);
        $shareRows = array_map(
            fn (array $row): array => $this->sanitizeShareRowForUi($row),
            $this->shares->findForExport($exportId)
        );
        $activeRaw = $this->shares->findActiveForExport($exportId);
        $active = $activeRaw !== null ? $this->sanitizeShareRowForUi($activeRaw) : null;
        $onceUrl = $this->consumeOnceShareUrl($exportId);
        $handoff = $this->buildHandoffState($export, $active, $onceUrl, $actor);

        return [
            'ok' => true,
            'message' => 'Shares loaded.',
            'export' => $export,
            'shares' => $shareRows,
            'active_share' => $active,
            'eligibility' => $eligibility,
            'can_manage' => $this->canManage($actor),
            'plaintext_share_url' => $onceUrl,
            'handoff' => $handoff,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   export:?array<string,mixed>,
     *   share:?array<string,mixed>,
     *   plaintext_token:?string,
     *   plaintext_share_url:?string,
     *   eligibility:array{eligible:bool,reason:string,code:string},
     *   errors?:array<string,string>
     * }
     */
    public function createShare(int $exportId, array $actor, ?string $tokenLabel = null): array
    {
        $this->assertDb();

        if (!$this->canManage($actor)) {
            return [
                'ok' => false,
                'message' => 'Недостаточно прав.',
                'export' => null,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Недостаточно прав.', 'code' => 'role'],
                'errors' => ['role' => 'Недостаточно прав.'],
            ];
        }

        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return [
                'ok' => false,
                'message' => 'Файл отчета не найден.',
                'export' => null,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Файл отчета не найден.', 'code' => 'missing'],
                'errors' => ['id' => 'Не найдено.'],
            ];
        }

        $eligibility = $this->evaluateEligibility($export);
        if (!$eligibility['eligible']) {
            return [
                'ok' => false,
                'message' => 'Файл нельзя отправлять клиенту: ' . $eligibility['reason'],
                'export' => $export,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => $eligibility,
                'errors' => ['eligibility' => $eligibility['code']],
            ];
        }

        $existing = $this->shares->findActiveForExport($exportId);
        if ($existing !== null) {
            return [
                'ok' => false,
                'message' => 'Уже есть активная ссылка для этого файла. Отзовите её, прежде чем создавать новую.',
                'export' => $export,
                'share' => $this->sanitizeShareRowForUi($existing),
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => $eligibility,
                'errors' => ['active' => 'Exists.'],
            ];
        }

        $token = SafeToken::generate();
        $tokenHash = SafeToken::hashPublicToken($token);
        if ($tokenHash === null) {
            return [
                'ok' => false,
                'message' => 'Could not create share link.',
                'export' => $export,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => $eligibility,
                'errors' => ['create' => 'Token format.'],
            ];
        }
        $label = $this->normalizeLabel($tokenLabel);
        $expiresAt = date('Y-m-d H:i:s', time() + (self::DEFAULT_EXPIRY_DAYS * 86400));
        $userId = (int) ($actor['id'] ?? 0);

        try {
            $share = $this->shares->createShare([
                'report_export_id' => $exportId,
                'token_hash' => $tokenHash,
                'token_label' => $label,
                'status' => 'active',
                'expires_at' => $expiresAt,
                'created_by' => $userId > 0 ? $userId : null,
                'max_access_count' => null,
                'metadata_json' => null,
            ]);
        } catch (Throwable $e) {
            return [
                'ok' => false,
                'message' => 'Could not create share link.',
                'export' => $export,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => $eligibility,
                'errors' => ['create' => 'Failed.'],
            ];
        }

        if ($share === null) {
            return [
                'ok' => false,
                'message' => 'Share row was not created.',
                'export' => $export,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => $eligibility,
                'errors' => ['create' => 'Empty.'],
            ];
        }

        $url = $this->buildPublicShareUrl($token);
        $this->storeOnceShareUrl($exportId, $url);
        // Plaintext token is returned only for this create response / once-session URL.
        // Controllers must not log it; views show URL once then consume session value.

        return [
            'ok' => true,
            'message' => 'Public share link created. Copy it now — it will not be shown again.',
            'export' => $export,
            'share' => $this->sanitizeShareRowForUi($share),
            'plaintext_token' => $token,
            'plaintext_share_url' => $url,
            'eligibility' => $eligibility,
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   message:string,
     *   share:?array<string,mixed>,
     *   export_id:int,
     *   errors?:array<string,string>
     * }
     */
    public function revokeShare(int $shareId, array $actor): array
    {
        $this->assertDb();

        if (!$this->canManage($actor)) {
            return [
                'ok' => false,
                'message' => 'Недостаточно прав.',
                'share' => null,
                'export_id' => 0,
                'errors' => ['role' => 'Недостаточно прав.'],
            ];
        }

        $share = $this->shares->findById($shareId);
        if ($share === null) {
            return [
                'ok' => false,
                'message' => 'Ссылка не найдена.',
                'share' => null,
                'export_id' => 0,
                'errors' => ['id' => 'Не найдено.'],
            ];
        }

        $exportId = (int) ($share['report_export_id'] ?? 0);
        if ((string) ($share['status'] ?? '') !== 'active') {
            return [
                'ok' => false,
                'message' => 'Ссылка не активна.',
                'share' => $this->sanitizeShareRowForUi($share),
                'export_id' => $exportId,
                'errors' => ['status' => 'Не активна.'],
            ];
        }

        $userId = (int) ($actor['id'] ?? 0);
        $ok = $this->shares->revoke($shareId, $userId);
        $updated = $this->shares->findById($shareId);

        return [
            'ok' => $ok,
            'message' => $ok ? 'Share link revoked.' : 'Could not revoke share.',
            'share' => $updated !== null ? $this->sanitizeShareRowForUi($updated) : null,
            'export_id' => $exportId,
            'errors' => $ok ? [] : ['revoke' => 'Failed.'],
        ];
    }

    /**
     * Resolve a public token to a validated PDF artifact path.
     *
     * @return array{
     *   ok:bool,
     *   http_status:int,
     *   message:string,
     *   export:?array<string,mixed>,
     *   share:?array<string,mixed>,
     *   absolute_path:?string,
     *   deny_code:?string
     * }
     */
    public function resolvePublicToken(string $token): array
    {
        $this->assertDb();

        // Format gate before any hashing / DB lookup.
        $token = trim($token);
        if (!SafeToken::isValidPublicToken($token)) {
            return $this->denyPublic(404, 'not_found', 'Not found.');
        }

        $hash = SafeToken::hashPublicToken($token);
        if ($hash === null) {
            return $this->denyPublic(404, 'not_found', 'Not found.');
        }

        $share = $this->shares->findByTokenHash($hash);
        if ($share === null || !SafeToken::equalsHash((string) ($share['token_hash'] ?? ''), $token)) {
            return $this->denyPublic(404, 'not_found', 'Not found.');
        }

        $status = (string) ($share['status'] ?? '');
        if ($status === 'revoked' || $status === 'expired') {
            return $this->denyPublic(410, $status, 'Gone.');
        }
        if ($status !== 'active') {
            return $this->denyPublic(404, 'not_found', 'Not found.');
        }

        $expiresAt = (string) ($share['expires_at'] ?? '');
        if ($expiresAt !== '' && strtotime($expiresAt) !== false && strtotime($expiresAt) <= time()) {
            return $this->denyPublic(410, 'expired', 'Gone.');
        }

        $maxAccess = $share['max_access_count'] ?? null;
        if ($maxAccess !== null && (int) $maxAccess > 0) {
            $accessCount = (int) ($share['access_count'] ?? 0);
            if ($accessCount >= (int) $maxAccess) {
                return $this->denyPublic(410, 'max_access', 'Gone.');
            }
        }

        $exportId = (int) ($share['report_export_id'] ?? 0);
        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return $this->denyPublic(404, 'export_missing', 'Not found.');
        }

        $eligibility = $this->evaluateEligibility($export);
        if (!$eligibility['eligible']) {
            return $this->denyPublic(404, 'not_eligible', 'Not found.');
        }

        $validation = $this->exportService->validateReadyArtifact($export);
        if (!$validation['ok'] || !is_string($validation['absolute_path']) || $validation['absolute_path'] === '') {
            return $this->denyPublic(404, 'artifact_invalid', 'Not found.');
        }

        // Access is recorded by the public controller only after stream preflight succeeds.
        return [
            'ok' => true,
            'http_status' => 200,
            'message' => 'Ready.',
            'export' => $export,
            'share' => $share,
            'absolute_path' => $validation['absolute_path'],
            'deny_code' => null,
        ];
    }

    /**
     * Record a successful public stream access (hash-only IP/UA). Does not increment on denials.
     */
    public function recordSuccessfulPublicAccess(int $shareId): bool
    {
        if ($shareId <= 0) {
            return false;
        }
        $this->assertDb();
        $ipHash = $this->hashOptional($_SERVER['REMOTE_ADDR'] ?? null);
        $uaHash = $this->hashOptional($_SERVER['HTTP_USER_AGENT'] ?? null);

        return $this->shares->recordSuccessfulAccess($shareId, $ipHash, $uaHash);
    }

    /**
     * @param array<string, mixed> $export
     * @return array{eligible:bool,reason:string,code:string}
     */
    public function evaluateEligibility(array $export): array
    {
        if ((string) ($export['format'] ?? '') !== 'pdf') {
            return ['eligible' => false, 'reason' => 'Отправлять клиенту можно только оформленный PDF.', 'code' => 'format'];
        }
        if ((string) ($export['status'] ?? '') !== 'ready') {
            return ['eligible' => false, 'reason' => 'Файл должен быть в статусе «Готово».', 'code' => 'status'];
        }
        if (!empty($export['archived_at'])) {
            return ['eligible' => false, 'reason' => 'Архивные файлы нельзя отправлять.', 'code' => 'archived'];
        }
        $templateId = trim((string) ($export['template_id'] ?? ''));
        if ($templateId === '') {
            return ['eligible' => false, 'reason' => 'Нужен сохранённый шаблон; старый PDF отправлять нельзя.', 'code' => 'template'];
        }
        if ((string) ($export['render_target'] ?? '') !== 'pdf_export') {
            return ['eligible' => false, 'reason' => 'Тип генерации должен быть pdf_export.', 'code' => 'render_target'];
        }

        $validation = $this->exportService->validateReadyArtifact($export);
        if (!$validation['ok']) {
            return [
                'eligible' => false,
                'reason' => $validation['message'] !== '' ? $validation['message'] : 'Проверка файла не пройдена.',
                'code' => 'artifact',
            ];
        }

        return ['eligible' => true, 'reason' => 'Можно создать ссылку для клиента.', 'code' => 'ok'];
    }

    public function isShareableExport(array $export): bool
    {
        return $this->evaluateEligibility($export)['eligible'];
    }

    public function activeShareCountForExport(int $exportId): int
    {
        return $this->shares->countActiveForExport($exportId);
    }

    public function buildPublicShareUrl(string $token): string
    {
        $path = '/share/report/' . rawurlencode($token);
        $base = rtrim((string) $this->config->get('app.url', ''), '/');
        if ($base !== '') {
            return $base . $path;
        }

        $scheme = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') ? 'https' : 'http';
        $host = (string) ($_SERVER['HTTP_HOST'] ?? '');
        if ($host !== '') {
            return $scheme . '://' . $host . $path;
        }

        return $path;
    }

    /**
     * @return array{eligible:bool,reason:string,code:string}
     */
    public function eligibilityForExportId(int $exportId): array
    {
        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return ['eligible' => false, 'reason' => 'Файл не найден.', 'code' => 'missing'];
        }
        return $this->evaluateEligibility($export);
    }

    /**
     * Build operator handoff readiness + optional copy pack (once URL only).
     *
     * @param array<string, mixed> $export
     * @param array<string, mixed>|null $activeShare sanitized UI row or null
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $actor
     * @return array<string, mixed>
     */
    public function buildHandoffState(
        array $export,
        ?array $activeShare = null,
        ?string $onceShareUrl = null,
        ?array $actor = null
    ): array {
        $exportId = (int) ($export['id'] ?? 0);
        $eligibility = $this->evaluateEligibility($export);
        $ctxRow = $exportId > 0 ? $this->shares->findHandoffContext($exportId) : null;

        $clientName = trim((string) ($ctxRow['client_name'] ?? ''));
        $projectName = trim((string) ($ctxRow['project_name'] ?? ''));
        $period = $this->formatPeriodLabel(
            is_array($ctxRow) ? (string) ($ctxRow['period_key'] ?? '') : '',
            is_array($ctxRow) ? (string) ($ctxRow['period_start'] ?? '') : '',
            is_array($ctxRow) ? (string) ($ctxRow['period_title'] ?? '') : ''
        );
        $reportStatus = trim((string) ($ctxRow['monthly_status'] ?? ''));
        $snapshotKey = trim((string) ($ctxRow['snapshot_key'] ?? ($export['snapshot_key'] ?? '')));
        $snapshotStatus = trim((string) ($ctxRow['snapshot_status'] ?? ($export['snapshot_status'] ?? '')));
        $templateId = trim((string) ($export['template_id'] ?? ($ctxRow['template_id'] ?? '')));
        $templateVersion = trim((string) ($export['template_version'] ?? ($ctxRow['template_version'] ?? '')));
        $templateLabel = ($templateId !== '' && $templateVersion !== '')
            ? ($templateId . ' v' . $templateVersion)
            : 'устаревший / не записан';
        $specialist = trim((string) ($actor['name'] ?? ''));
        if ($specialist === '') {
            $specialist = trim((string) ($ctxRow['specialist_name'] ?? ''));
        }
        if ($specialist === '') {
            $specialist = 'специалист i-SEO';
        }

        if ($clientName === '') {
            $clientName = 'SAFE UNKNOWN';
        }
        if ($projectName === '') {
            $projectName = 'SAFE UNKNOWN';
        }
        if ($period === '') {
            $period = 'SAFE UNKNOWN';
        }

        if ($activeShare === null && $exportId > 0) {
            $activeRaw = $this->shares->findActiveForExport($exportId);
            $activeShare = $activeRaw !== null ? $this->sanitizeShareRowForUi($activeRaw) : null;
        }

        $hasActive = is_array($activeShare);
        $expiresAt = $hasActive ? (string) ($activeShare['expires_at'] ?? '') : '';
        $expiresDisplay = $expiresAt !== '' ? $this->formatExpiresAt($expiresAt) : '';
        $revokedCount = $exportId > 0 ? $this->shares->countRevokedForExport($exportId) : 0;
        $onceAvailable = is_string($onceShareUrl) && $onceShareUrl !== '';

        $reportFinalized = $reportStatus === 'finalized';
        $snapshotOk = $snapshotKey !== '' && ($snapshotStatus === '' || $snapshotStatus === 'active');
        $styledPdfReady = $eligibility['eligible'] === true
            || (
                (string) ($export['format'] ?? '') === 'pdf'
                && (string) ($export['status'] ?? '') === 'ready'
                && $templateId !== ''
                && (string) ($export['render_target'] ?? '') === 'pdf_export'
            );
        $shareable = !empty($eligibility['eligible']);
        $activeOk = $hasActive && $expiresAt !== '' && strtotime($expiresAt) !== false && strtotime($expiresAt) > time();
        $urlCopiedOnce = $onceAvailable;
        $notSendingBadLink = true;

        $checklist = [
            ['id' => 'report_finalized', 'label' => 'Отчет финализирован', 'pass' => $reportFinalized, 'note' => $reportStatus !== '' ? $reportStatus : 'SAFE UNKNOWN'],
            ['id' => 'snapshot_exists', 'label' => 'Снимок отчета есть', 'pass' => $snapshotOk, 'note' => $snapshotKey !== '' ? $snapshotKey : 'SAFE UNKNOWN'],
            ['id' => 'styled_pdf_ready', 'label' => 'PDF для клиента готов', 'pass' => $styledPdfReady && (string) ($export['status'] ?? '') === 'ready', 'note' => (string) ($export['status'] ?? '')],
            ['id' => 'shareable_export', 'label' => 'Файл можно отправлять', 'pass' => $shareable, 'note' => $eligibility['reason']],
            ['id' => 'active_share', 'label' => 'Есть активная неистекшая ссылка', 'pass' => $activeOk, 'note' => $activeOk ? ('до ' . $expiresAt) : 'активной ссылки нет'],
            ['id' => 'url_copied', 'label' => 'Ссылка доступна для копирования (только после создания)', 'pass' => $urlCopiedOnce, 'note' => $urlCopiedOnce ? 'показана сейчас' : 'не на этом экране'],
            ['id' => 'no_bad_link', 'label' => 'Не отправлять отозванные или просроченные ссылки', 'pass' => $notSendingBadLink, 'note' => 'ответственность оператора'],
        ];

        $warnings = [
            'Ссылка показывается только один раз при создании.',
            'Если ссылку не скопировали — отзовите активную и создайте новую.',
            'Не отправляйте отозванные или просроченные ссылки.',
            'Не отправляйте старые PDF или HTML-файлы.',
            'Не отправляйте внутренний путь к файлу на диске.',
        ];

        $urlLostGuidance = null;
        if ($shareable && $activeOk && !$onceAvailable) {
            $urlLostGuidance = 'Ссылка уже создана, но полный URL был показан только один раз. Если ссылка не была скопирована, отзовите текущую ссылку и создайте новую.';
        }

        $copyPack = null;
        if ($onceAvailable && $shareable) {
            $copyPack = $this->buildCopyPack([
                'client_name' => $clientName,
                'project_name' => $projectName,
                'period' => $period,
                'share_url' => $onceShareUrl,
                'expires_at' => $expiresDisplay !== '' ? $expiresDisplay : $expiresAt,
                'specialist_name' => $specialist,
                'export_id' => (string) $exportId,
                'export_key' => (string) ($export['export_key'] ?? ''),
                'template_label' => $templateLabel,
                'share_id' => $hasActive ? (string) (int) ($activeShare['id'] ?? 0) : '',
                'share_status' => $hasActive ? (string) ($activeShare['status'] ?? 'active') : 'active',
            ]);
        }

        $deliveryReady = $reportFinalized && $snapshotOk && $shareable && $activeOk && $onceAvailable;

        return [
            'context' => [
                'client_name' => $clientName,
                'project_name' => $projectName,
                'period' => $period,
                'report_status' => $reportStatus !== '' ? $reportStatus : 'SAFE UNKNOWN',
                'snapshot_key' => $snapshotKey !== '' ? $snapshotKey : 'SAFE UNKNOWN',
                'snapshot_status' => $snapshotStatus !== '' ? $snapshotStatus : 'SAFE UNKNOWN',
                'export_id' => $exportId,
                'export_key' => (string) ($export['export_key'] ?? ''),
                'format' => (string) ($export['format'] ?? ''),
                'template_label' => $templateLabel,
                'specialist_name' => $specialist,
            ],
            'share_status' => [
                'has_active' => $hasActive,
                'active_share_id' => $hasActive ? (int) ($activeShare['id'] ?? 0) : 0,
                'expires_at' => $expiresAt,
                'expires_display' => $expiresDisplay,
                'revoked_count' => $revokedCount,
                'active_count' => $activeOk ? 1 : 0,
            ],
            'checklist' => $checklist,
            'warnings' => $warnings,
            'copy_pack' => $copyPack,
            'once_url_available' => $onceAvailable,
            'url_lost_guidance' => $urlLostGuidance,
            'eligible' => $shareable,
            'eligibility_reason' => $eligibility['reason'],
            'eligibility_code' => $eligibility['code'],
            'delivery_ready' => $deliveryReady,
        ];
    }

    /**
     * @param array<string, string> $vars
     * @return array{short_message:string,email_subject:string,email_body:string,internal_note:string,share_url:string}
     */
    public function buildCopyPack(array $vars): array
    {
        $client = $vars['client_name'] ?? 'SAFE UNKNOWN';
        $project = $vars['project_name'] ?? 'SAFE UNKNOWN';
        $period = $vars['period'] ?? 'SAFE UNKNOWN';
        $url = $vars['share_url'] ?? '';
        $expires = $vars['expires_at'] ?? '';
        $specialist = $vars['specialist_name'] ?? 'специалист i-SEO';
        if (trim($specialist) === '') {
            $specialist = 'команда i-SEO';
        }

        $short = 'Здравствуйте! Подготовили отчет по проекту ' . $project . ' за ' . $period
            . '. Скачать PDF можно по ссылке: ' . $url
            . '. Ссылка будет доступна до ' . $expires . '.'
            . "\n\nЕсли будут вопросы по отчету — напишите, пожалуйста. " . $specialist;

        $emailSubject = 'Отчет по проекту ' . $project . ' за ' . $period;
        $emailBody = "Здравствуйте!\n\n"
            . 'Направляем отчет по проекту ' . $project . ' за ' . $period . ".\n\n"
            . "PDF-файл доступен по защищенной ссылке:\n"
            . $url . "\n\n"
            . 'Ссылка действует до ' . $expires . ".\n\n"
            . "Если потребуется пояснение по отчету или комментарии по следующему периоду, напишите нам.\n\n"
            . "С уважением,\n"
            . $specialist;

        $internal = "HANDOFF / INTERNAL\n"
            . 'Client: ' . $client . "\n"
            . 'Project: ' . $project . "\n"
            . 'Period: ' . $period . "\n"
            . 'Export: id ' . ($vars['export_id'] ?? '') . ' / ' . ($vars['export_key'] ?? '')
            . ' / template ' . ($vars['template_label'] ?? '') . " (styled PDF only)\n"
            . 'Share: id ' . ($vars['share_id'] ?? '') . ' / status ' . ($vars['share_status'] ?? '') . "\n"
            . 'Expires: ' . $expires . "\n"
            . "URL: available only on create-success screen (once)\n"
            . "Sent channel: [Telegram | Email | Other]\n"
            . "Sent at: [operator fills manually]\n"
            . "Warnings:\n"
            . "- do not send revoked/expired link\n"
            . "- do not send HTML or legacy export\n"
            . "- do not reconstruct URL from DB\n"
            . "- if URL lost → revoke + recreate share\n"
            . "- never include internal storage path in client messages";

        return [
            'short_message' => $short,
            'email_subject' => $emailSubject,
            'email_body' => $emailBody,
            'internal_note' => $internal,
            'share_url' => $url,
        ];
    }

    private function formatPeriodLabel(string $periodKey, string $periodStart, string $periodTitle): string
    {
        $months = [
            1 => 'январь', 2 => 'февраль', 3 => 'март', 4 => 'апрель',
            5 => 'май', 6 => 'июнь', 7 => 'июль', 8 => 'август',
            9 => 'сентябрь', 10 => 'октябрь', 11 => 'ноябрь', 12 => 'декабрь',
        ];
        if ($periodStart !== '' && preg_match('/^(\d{4})-(\d{2})/', $periodStart, $m) === 1) {
            $monthNum = (int) $m[2];
            $year = $m[1];
            if (isset($months[$monthNum])) {
                return $months[$monthNum] . ' ' . $year;
            }
        }
        if ($periodKey !== '' && preg_match('/^(\d{4})-(\d{2})$/', $periodKey, $m) === 1) {
            $monthNum = (int) $m[2];
            $year = $m[1];
            if (isset($months[$monthNum])) {
                return $months[$monthNum] . ' ' . $year;
            }
        }
        if ($periodTitle !== '') {
            return $periodTitle;
        }
        if ($periodKey !== '') {
            return $periodKey;
        }
        return '';
    }

    private function formatExpiresAt(string $expiresAt): string
    {
        $ts = strtotime($expiresAt);
        if ($ts === false) {
            return $expiresAt;
        }
        $months = [
            1 => 'января', 2 => 'февраля', 3 => 'марта', 4 => 'апреля',
            5 => 'мая', 6 => 'июня', 7 => 'июля', 8 => 'августа',
            9 => 'сентября', 10 => 'октября', 11 => 'ноября', 12 => 'декабря',
        ];
        $monthNum = (int) date('n', $ts);
        $month = $months[$monthNum] ?? date('m', $ts);
        return (int) date('j', $ts) . ' ' . $month . ' ' . date('Y', $ts) . ', ' . date('H:i', $ts);
    }

    /**
     * @return array{
     *   ok:bool,
     *   http_status:int,
     *   message:string,
     *   export:?array<string,mixed>,
     *   share:?array<string,mixed>,
     *   absolute_path:?string,
     *   deny_code:?string
     * }
     */
    private function denyPublic(int $status, string $code, string $message): array
    {
        return [
            'ok' => false,
            'http_status' => $status,
            'message' => $message,
            'export' => null,
            'share' => null,
            'absolute_path' => null,
            'deny_code' => $code,
        ];
    }

    private function normalizeLabel(?string $label): ?string
    {
        if ($label === null) {
            return null;
        }
        $label = trim($label);
        if ($label === '') {
            return null;
        }
        if (strlen($label) > 150) {
            $label = substr($label, 0, 150);
        }
        return $label;
    }

    /**
     * Strip sensitive columns before internal UI rendering (no hash/path/IP leakage).
     *
     * @param array<string, mixed> $row
     * @return array<string, mixed>
     */
    private function sanitizeShareRowForUi(array $row): array
    {
        unset(
            $row['token_hash'],
            $row['last_access_ip_hash'],
            $row['last_user_agent_hash'],
            $row['metadata_json']
        );

        return $row;
    }

    private function hashOptional(mixed $value): ?string
    {
        if (!is_string($value)) {
            return null;
        }
        $value = trim($value);
        if ($value === '') {
            return null;
        }
        return hash('sha256', $value);
    }

    private function storeOnceShareUrl(int $exportId, string $url): void
    {
        if (!isset($_SESSION['_share_url_once']) || !is_array($_SESSION['_share_url_once'])) {
            $_SESSION['_share_url_once'] = [];
        }
        $_SESSION['_share_url_once'][(string) $exportId] = $url;
    }

    private function consumeOnceShareUrl(int $exportId): ?string
    {
        if (!isset($_SESSION['_share_url_once']) || !is_array($_SESSION['_share_url_once'])) {
            return null;
        }
        $key = (string) $exportId;
        if (!isset($_SESSION['_share_url_once'][$key])) {
            return null;
        }
        $url = (string) $_SESSION['_share_url_once'][$key];
        unset($_SESSION['_share_url_once'][$key]);
        return $url !== '' ? $url : null;
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

    private function assertDb(): void
    {
        $this->db->connect();
    }
}
