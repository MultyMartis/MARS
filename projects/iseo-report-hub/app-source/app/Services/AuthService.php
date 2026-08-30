<?php
declare(strict_types=1);

namespace Iseo\Services;

use PDO;
use Throwable;

/**
 * DB-backed local auth — password_verify only; no secrets in audit/session.
 */
final class AuthService
{
    private const SESSION_USER_ID = 'auth_user_id';
    private const SESSION_EMAIL = 'auth_email';
    private const SESSION_NAME = 'auth_name';
    private const SESSION_ROLES = 'auth_roles';
    private const SESSION_AUTHENTICATED_AT = 'auth_authenticated_at';

    /** @var list<string> */
    private const INTERNAL_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
        'account_client_manager',
        'internal_viewer',
    ];

    public function __construct(
        private DatabaseService $db,
        private ConfigService $config
    ) {
    }

    /**
     * @return array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null
     */
    public function currentUser(): ?array
    {
        $id = $_SESSION[self::SESSION_USER_ID] ?? null;
        if ($id === null || $id === '' || (int) $id <= 0) {
            return null;
        }

        $roles = $_SESSION[self::SESSION_ROLES] ?? [];
        if (!is_array($roles)) {
            $roles = [];
        }

        $roleCodes = [];
        foreach ($roles as $role) {
            if (is_string($role) && $role !== '') {
                $roleCodes[] = $role;
            }
        }

        return [
            'id' => (int) $id,
            'email' => (string) ($_SESSION[self::SESSION_EMAIL] ?? ''),
            'name' => (string) ($_SESSION[self::SESSION_NAME] ?? ''),
            'roles' => $roleCodes,
            'authenticated_at' => (string) ($_SESSION[self::SESSION_AUTHENTICATED_AT] ?? ''),
        ];
    }

    public function check(): bool
    {
        return $this->currentUser() !== null;
    }

    public function isAuthenticated(): bool
    {
        return $this->check();
    }

    public function hasInternalRole(?array $user = null): bool
    {
        $user ??= $this->currentUser();
        if ($user === null) {
            return false;
        }

        foreach ($user['roles'] as $role) {
            if (in_array($role, self::INTERNAL_ROLES, true)) {
                return true;
            }
        }

        return false;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function hasRole(string $role, ?array $user = null): bool
    {
        $user ??= $this->currentUser();
        if ($user === null || $role === '') {
            return false;
        }

        return in_array($role, $user['roles'], true);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param list<string> $roles
     */
    public function hasAnyRole(array $roles, ?array $user = null): bool
    {
        $user ??= $this->currentUser();
        if ($user === null || $roles === []) {
            return false;
        }

        foreach ($roles as $role) {
            if (is_string($role) && $role !== '' && in_array($role, $user['roles'], true)) {
                return true;
            }
        }

        return false;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function isAdminOwner(?array $user = null): bool
    {
        return $this->hasRole('admin_owner', $user);
    }

    /**
     * Admin / lead surfaces (period create, raw block edit, finalization UI).
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function isPrivilegedEditor(?array $user = null): bool
    {
        return $this->hasAnyRole(['admin_owner', 'seo_lead_reviewer'], $user);
    }

    /**
     * Specialist-only (no admin/lead). Used to narrow demo UX.
     *
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     */
    public function isSpecialistFlow(?array $user = null): bool
    {
        $user ??= $this->currentUser();
        if ($user === null) {
            return false;
        }

        return $this->hasRole('seo_specialist', $user) && !$this->isPrivilegedEditor($user);
    }

    /**
     * @param array{ip?:?string,user_agent?:?string} $context
     * @return array{ok:bool,status:string,message:string}
     */
    public function login(string $email, string $password, array $context = []): array
    {
        $email = strtolower(trim($email));
        $genericFail = [
            'ok' => false,
            'status' => 'invalid_credentials',
            'message' => 'Invalid email or password.',
        ];

        if ($email === '' || $password === '') {
            $this->writeAudit('auth.login.failed', null, 'user', null, [
                'reason' => 'empty_credentials',
            ], $context);
            return $genericFail;
        }

        if (!$this->db->isConfigured()) {
            $this->writeAudit('auth.login.failed', null, 'user', null, [
                'reason' => 'db_not_configured',
            ], $context);
            return [
                'ok' => false,
                'status' => 'db_unavailable',
                'message' => 'Authentication temporarily unavailable.',
            ];
        }

        try {
            $pdo = $this->db->connect();
            $stmt = $pdo->prepare(
                'SELECT id, name, email, password_hash, status
                 FROM users
                 WHERE email = :email
                 LIMIT 1'
            );
            $stmt->execute([':email' => $email]);
            $row = $stmt->fetch();

            if (!is_array($row)) {
                $this->writeAudit('auth.login.failed', null, 'user', null, [
                    'reason' => 'unknown_user',
                ], $context);
                return $genericFail;
            }

            $userId = (int) $row['id'];
            $status = (string) ($row['status'] ?? '');
            $hash = (string) ($row['password_hash'] ?? '');

            if ($status !== 'active' || $hash === '' || !password_verify($password, $hash)) {
                $this->writeAudit('auth.login.failed', $userId, 'user', $userId, [
                    'reason' => $status !== 'active' ? 'inactive' : 'credential_mismatch',
                ], $context);
                return $genericFail;
            }

            $roles = $this->loadRoleCodes($pdo, $userId);
            $internal = array_values(array_intersect($roles, self::INTERNAL_ROLES));
            if ($internal === []) {
                $this->writeAudit('auth.login.failed', $userId, 'user', $userId, [
                    'reason' => 'no_internal_role',
                ], $context);
                return $genericFail;
            }

            session_regenerate_id(true);

            $authenticatedAt = date('c');
            $_SESSION[self::SESSION_USER_ID] = $userId;
            $_SESSION[self::SESSION_EMAIL] = (string) $row['email'];
            $_SESSION[self::SESSION_NAME] = \Iseo\Support\UiLabels::decodeLiteralUnicodeEscapes((string) $row['name']);
            $_SESSION[self::SESSION_ROLES] = $internal;
            $_SESSION[self::SESSION_AUTHENTICATED_AT] = $authenticatedAt;

            // Clear legacy stub keys if present.
            unset($_SESSION['auth_demo_flag'], $_SESSION['auth_user']);

            $upd = $pdo->prepare('UPDATE users SET last_login_at = CURRENT_TIMESTAMP WHERE id = :id');
            $upd->execute([':id' => $userId]);

            $this->writeAudit('auth.login.success', $userId, 'user', $userId, [
                'roles' => $internal,
            ], $context);

            return [
                'ok' => true,
                'status' => 'authenticated',
                'message' => 'Login successful.',
            ];
        } catch (Throwable) {
            $this->writeAudit('auth.login.failed', null, 'user', null, [
                'reason' => 'exception',
            ], $context);

            return [
                'ok' => false,
                'status' => 'error',
                'message' => 'Authentication temporarily unavailable.',
            ];
        }
    }

    /**
     * @param array{ip?:?string,user_agent?:?string} $context
     */
    public function logout(array $context = []): void
    {
        $user = $this->currentUser();
        if ($user !== null) {
            $this->writeAudit('auth.logout', $user['id'], 'user', $user['id'], [
                'roles' => $user['roles'],
            ], $context);
        }

        unset(
            $_SESSION[self::SESSION_USER_ID],
            $_SESSION[self::SESSION_EMAIL],
            $_SESSION[self::SESSION_NAME],
            $_SESSION[self::SESSION_ROLES],
            $_SESSION[self::SESSION_AUTHENTICATED_AT],
            $_SESSION['auth_demo_flag'],
            $_SESSION['auth_user']
        );
    }

    public function statusMessage(): string
    {
        if ($this->check()) {
            return 'Вход выполнен';
        }

        if ($this->db->isConfigured()) {
            return 'Вход доступен';
        }

        return 'Вход недоступен — база не настроена';
    }

    /**
     * @param array<string, mixed>|null $metadata
     * @param array{ip?:?string,user_agent?:?string} $context
     */
    public function writeAudit(
        string $eventType,
        ?int $actorUserId,
        ?string $entityType = null,
        ?int $entityId = null,
        ?array $metadata = null,
        array $context = []
    ): void {
        if (!$this->db->isConfigured()) {
            return;
        }

        // Never allow password/hash keys into audit metadata.
        if (is_array($metadata)) {
            unset($metadata['password'], $metadata['password_hash'], $metadata['hash']);
        }

        try {
            $pdo = $this->db->connect();
            $stmt = $pdo->prepare(
                'INSERT INTO audit_log
                    (actor_user_id, event_type, entity_type, entity_id, metadata_json, ip_address, user_agent)
                 VALUES
                    (:actor_user_id, :event_type, :entity_type, :entity_id, :metadata_json, :ip_address, :user_agent)'
            );

            $metaJson = null;
            if (is_array($metadata) && $metadata !== []) {
                $metaJson = json_encode($metadata, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
            }

            $ip = isset($context['ip']) && is_string($context['ip']) ? substr($context['ip'], 0, 45) : null;
            $ua = isset($context['user_agent']) && is_string($context['user_agent'])
                ? substr($context['user_agent'], 0, 255)
                : null;

            $stmt->execute([
                ':actor_user_id' => $actorUserId,
                ':event_type' => $eventType,
                ':entity_type' => $entityType,
                ':entity_id' => $entityId,
                ':metadata_json' => $metaJson,
                ':ip_address' => $ip,
                ':user_agent' => $ua,
            ]);
        } catch (Throwable) {
            // Audit must not break login/logout flows.
        }
    }

    /**
     * @return list<string>
     */
    private function loadRoleCodes(PDO $pdo, int $userId): array
    {
        $stmt = $pdo->prepare(
            'SELECT r.code
             FROM user_roles ur
             INNER JOIN roles r ON r.id = ur.role_id
             WHERE ur.user_id = :user_id
             ORDER BY r.code ASC'
        );
        $stmt->execute([':user_id' => $userId]);
        $rows = $stmt->fetchAll();
        $codes = [];
        foreach ($rows as $row) {
            if (isset($row['code']) && is_string($row['code']) && $row['code'] !== '') {
                $codes[] = $row['code'];
            }
        }

        return $codes;
    }
}
