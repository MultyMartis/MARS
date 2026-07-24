<?php
declare(strict_types=1);

namespace Iseo\Services;

/**
 * Config loader — defaults + optional future .env.local.
 * Phase 1A: no secrets required; no DB connection.
 */
final class ConfigService
{
    /** @var array<string, mixed> */
    private array $config = [];

    /** @var array<string, string> */
    private array $env = [];

    private bool $envLocalPresent = false;

    public function __construct(
        private string $basePath,
        private string $configPath
    ) {
    }

    public function load(): void
    {
        $this->env = [];
        $this->envLocalPresent = false;

        // Optional future local env — do not require; do not create.
        $envLocal = $this->basePath . DIRECTORY_SEPARATOR . '.env.local';
        if (is_file($envLocal) && is_readable($envLocal)) {
            $this->envLocalPresent = true;
            $this->env = $this->parseEnvFile($envLocal);
            $this->applyEnvToProcess($this->env);
        }

        $appDefaults = $this->loadPhpConfig($this->configPath . DIRECTORY_SEPARATOR . 'app.example.php', [
            'name' => 'i-SEO Report Hub',
            'env' => 'local',
            'debug' => true,
            'url' => 'http://iseo-report-hub.test',
            'timezone' => 'Europe/Moscow',
        ]);

        $databaseDefaults = $this->loadPhpConfig($this->configPath . DIRECTORY_SEPARATOR . 'database.example.php', [
            'driver' => 'mysql',
            'host' => '127.0.0.1',
            'port' => 3306,
            'database' => 'iseo_report_hub_dev',
            'username' => 'CHANGE_ME',
            'password' => 'CHANGE_ME',
            'charset' => 'utf8mb4',
        ]);

        $this->config = [
            'app' => [
                'name' => $this->envValue('APP_NAME', (string) ($appDefaults['name'] ?? 'i-SEO Report Hub')),
                'env' => $this->envValue('APP_ENV', (string) ($appDefaults['env'] ?? 'local')),
                'debug' => $this->envBool('APP_DEBUG', (bool) ($appDefaults['debug'] ?? true)),
                'url' => $this->envValue('APP_URL', (string) ($appDefaults['url'] ?? 'http://iseo-report-hub.test')),
                'timezone' => (string) ($appDefaults['timezone'] ?? 'Europe/Moscow'),
                'phase' => '1A',
                'phase_label' => 'Phase 1A — App skeleton (source-only)',
            ],
            'database' => [
                'driver' => (string) ($databaseDefaults['driver'] ?? 'mysql'),
                'host' => $this->envValue('DB_HOST', (string) ($databaseDefaults['host'] ?? '127.0.0.1')),
                'port' => (int) $this->envValue('DB_PORT', (string) ($databaseDefaults['port'] ?? 3306)),
                'database' => $this->envValue('DB_DATABASE', (string) ($databaseDefaults['database'] ?? 'iseo_report_hub_dev')),
                'username' => $this->envValue('DB_USERNAME', (string) ($databaseDefaults['username'] ?? 'CHANGE_ME')),
                'password' => $this->envValue('DB_PASSWORD', (string) ($databaseDefaults['password'] ?? 'CHANGE_ME')),
                'charset' => (string) ($databaseDefaults['charset'] ?? 'utf8mb4'),
                'configured' => false,
                'connected' => false,
                'phase_1a_note' => 'DB not configured / not tested in Phase 1A',
            ],
            'auth' => [
                'implemented' => false,
                'status' => 'Auth persistence not implemented in Phase 1A',
            ],
            'meta' => [
                'env_local_present' => $this->envLocalPresent,
                'env_required' => false,
            ],
        ];
    }

    /**
     * @return array<string, mixed>
     */
    public function all(): array
    {
        return $this->config;
    }

    public function get(string $key, mixed $default = null): mixed
    {
        $segments = explode('.', $key);
        $value = $this->config;
        foreach ($segments as $segment) {
            if (!is_array($value) || !array_key_exists($segment, $value)) {
                return $default;
            }
            $value = $value[$segment];
        }

        return $value;
    }

    public function appName(): string
    {
        return (string) $this->get('app.name', 'i-SEO Report Hub');
    }

    public function debug(): bool
    {
        return (bool) $this->get('app.debug', false);
    }

    public function envLocalPresent(): bool
    {
        return $this->envLocalPresent;
    }

    /**
     * @return array<string, mixed>
     */
    private function loadPhpConfig(string $file, array $fallback): array
    {
        if (!is_file($file)) {
            return $fallback;
        }

        $loaded = require $file;
        if (!is_array($loaded)) {
            return $fallback;
        }

        return array_merge($fallback, $loaded);
    }

    /**
     * Minimal .env parser (KEY=VALUE). No shell expansion. No secrets invented.
     *
     * @return array<string, string>
     */
    private function parseEnvFile(string $file): array
    {
        $lines = file($file, FILE_IGNORE_NEW_LINES);
        if ($lines === false) {
            return [];
        }

        $out = [];
        foreach ($lines as $line) {
            $line = trim($line);
            if ($line === '' || str_starts_with($line, '#')) {
                continue;
            }
            if (!str_contains($line, '=')) {
                continue;
            }
            [$key, $value] = explode('=', $line, 2);
            $key = trim($key);
            if ($key === '' || !preg_match('/^[A-Z_][A-Z0-9_]*$/', $key)) {
                continue;
            }
            $value = trim($value);
            if (
                (str_starts_with($value, '"') && str_ends_with($value, '"'))
                || (str_starts_with($value, "'") && str_ends_with($value, "'"))
            ) {
                $value = substr($value, 1, -1);
            }
            $out[$key] = $value;
        }

        return $out;
    }

    /**
     * @param array<string, string> $env
     */
    private function applyEnvToProcess(array $env): void
    {
        foreach ($env as $key => $value) {
            if (getenv($key) === false) {
                putenv($key . '=' . $value);
                $_ENV[$key] = $value;
            }
        }
    }

    private function envValue(string $key, string $default): string
    {
        if (array_key_exists($key, $this->env)) {
            return $this->env[$key];
        }
        $fromProcess = getenv($key);
        if ($fromProcess !== false && $fromProcess !== '') {
            return (string) $fromProcess;
        }

        return $default;
    }

    private function envBool(string $key, bool $default): bool
    {
        $raw = $this->envValue($key, $default ? 'true' : 'false');
        $normalized = strtolower(trim($raw));
        if (in_array($normalized, ['1', 'true', 'yes', 'on'], true)) {
            return true;
        }
        if (in_array($normalized, ['0', 'false', 'no', 'off'], true)) {
            return false;
        }

        return $default;
    }
}
