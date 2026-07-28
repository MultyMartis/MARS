<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Cryptographic opaque tokens for public share links.
 * Plaintext is never persisted; only SHA-256 hashes are stored.
 */
final class SafeToken
{
    public const BYTE_LENGTH = 32;

    /**
     * Generate a URL-safe hex token (>=32 bytes entropy).
     */
    public static function generate(): string
    {
        return bin2hex(random_bytes(self::BYTE_LENGTH));
    }

    public static function hash(string $token): string
    {
        return hash('sha256', $token);
    }

    public static function equalsHash(string $storedHash, string $token): bool
    {
        $stored = strtolower(trim($storedHash));
        $computed = strtolower(self::hash($token));
        if ($stored === '' || $computed === '' || strlen($stored) !== 64 || strlen($computed) !== 64) {
            return false;
        }

        return hash_equals($stored, $computed);
    }
}
