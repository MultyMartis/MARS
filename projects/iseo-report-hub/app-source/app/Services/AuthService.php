<?php
declare(strict_types=1);

namespace Iseo\Services;

/**
 * Auth baseline scaffolding — no DB, no password auth yet.
 */
final class AuthService
{
    private const SESSION_DEMO_FLAG = 'auth_demo_flag';
    private const SESSION_USER_KEY = 'auth_user';

    /**
     * @return array{id:int,name:string,role:string,source:string}|null
     */
    public function currentUser(): ?array
    {
        if (empty($_SESSION[self::SESSION_DEMO_FLAG])) {
            return null;
        }

        $user = $_SESSION[self::SESSION_USER_KEY] ?? null;
        if (is_array($user) && isset($user['name'])) {
            return [
                'id' => (int) ($user['id'] ?? 0),
                'name' => (string) $user['name'],
                'role' => (string) ($user['role'] ?? 'operator'),
                'source' => (string) ($user['source'] ?? 'placeholder'),
            ];
        }

        // Placeholder local operator when demo flag is set without full payload.
        return [
            'id' => 0,
            'name' => 'Local Operator (placeholder)',
            'role' => 'operator',
            'source' => 'placeholder',
        ];
    }

    public function check(): bool
    {
        return $this->currentUser() !== null;
    }

    /**
     * Login is not implemented in Phase 1A.
     *
     * @return array{ok:bool,status:string,message:string}
     */
    public function login(string $email, string $password): array
    {
        unset($email, $password);

        return [
            'ok' => false,
            'status' => 'not_implemented',
            'message' => 'Auth persistence not implemented in Phase 1A',
        ];
    }

    /**
     * Clears placeholder session keys only.
     */
    public function logout(): void
    {
        unset($_SESSION[self::SESSION_DEMO_FLAG], $_SESSION[self::SESSION_USER_KEY]);
    }

    public function statusMessage(): string
    {
        return 'Auth not implemented — no DB login in Phase 1A';
    }
}
