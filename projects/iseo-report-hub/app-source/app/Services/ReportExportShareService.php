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
                'message' => 'Forbidden.',
                'export' => null,
                'shares' => [],
                'active_share' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Forbidden.', 'code' => 'role'],
                'can_manage' => false,
                'plaintext_share_url' => null,
                'errors' => ['role' => 'Forbidden.'],
            ];
        }

        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return [
                'ok' => false,
                'message' => 'Export not found.',
                'export' => null,
                'shares' => [],
                'active_share' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Export not found.', 'code' => 'missing'],
                'can_manage' => $this->canManage($actor),
                'plaintext_share_url' => null,
                'errors' => ['id' => 'Not found.'],
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

        return [
            'ok' => true,
            'message' => 'Shares loaded.',
            'export' => $export,
            'shares' => $shareRows,
            'active_share' => $active,
            'eligibility' => $eligibility,
            'can_manage' => $this->canManage($actor),
            'plaintext_share_url' => $onceUrl,
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
                'message' => 'Forbidden.',
                'export' => null,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Forbidden.', 'code' => 'role'],
                'errors' => ['role' => 'Forbidden.'],
            ];
        }

        $export = $this->exports->findById($exportId);
        if ($export === null) {
            return [
                'ok' => false,
                'message' => 'Export not found.',
                'export' => null,
                'share' => null,
                'plaintext_token' => null,
                'plaintext_share_url' => null,
                'eligibility' => ['eligible' => false, 'reason' => 'Export not found.', 'code' => 'missing'],
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $eligibility = $this->evaluateEligibility($export);
        if (!$eligibility['eligible']) {
            return [
                'ok' => false,
                'message' => 'Export is not eligible for public share: ' . $eligibility['reason'],
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
                'message' => 'An active share already exists for this export. Revoke it before creating a new link.',
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
                'message' => 'Forbidden.',
                'share' => null,
                'export_id' => 0,
                'errors' => ['role' => 'Forbidden.'],
            ];
        }

        $share = $this->shares->findById($shareId);
        if ($share === null) {
            return [
                'ok' => false,
                'message' => 'Share not found.',
                'share' => null,
                'export_id' => 0,
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $exportId = (int) ($share['report_export_id'] ?? 0);
        if ((string) ($share['status'] ?? '') !== 'active') {
            return [
                'ok' => false,
                'message' => 'Share is not active.',
                'share' => $this->sanitizeShareRowForUi($share),
                'export_id' => $exportId,
                'errors' => ['status' => 'Not active.'],
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
            return ['eligible' => false, 'reason' => 'Only PDF exports are shareable in MVP.', 'code' => 'format'];
        }
        if ((string) ($export['status'] ?? '') !== 'ready') {
            return ['eligible' => false, 'reason' => 'Export status must be ready.', 'code' => 'status'];
        }
        if (!empty($export['archived_at'])) {
            return ['eligible' => false, 'reason' => 'Archived exports cannot be shared.', 'code' => 'archived'];
        }
        $templateId = trim((string) ($export['template_id'] ?? ''));
        if ($templateId === '') {
            return ['eligible' => false, 'reason' => 'Template metadata is required (legacy exports are not shareable).', 'code' => 'template'];
        }
        if ((string) ($export['render_target'] ?? '') !== 'pdf_export') {
            return ['eligible' => false, 'reason' => 'Render target must be pdf_export.', 'code' => 'render_target'];
        }

        $validation = $this->exportService->validateReadyArtifact($export);
        if (!$validation['ok']) {
            return [
                'eligible' => false,
                'reason' => $validation['message'] !== '' ? $validation['message'] : 'Artifact validation failed.',
                'code' => 'artifact',
            ];
        }

        return ['eligible' => true, 'reason' => 'Eligible for public PDF share.', 'code' => 'ok'];
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
            return ['eligible' => false, 'reason' => 'Export not found.', 'code' => 'missing'];
        }
        return $this->evaluateEligibility($export);
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
