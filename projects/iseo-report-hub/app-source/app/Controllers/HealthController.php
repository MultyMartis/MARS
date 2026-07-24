<?php
declare(strict_types=1);

namespace Iseo\Controllers;

final class HealthController extends BaseController
{
    /**
     * @return array<string, mixed>
     */
    public function collectStatus(): array
    {
        $required = [
            'pdo',
            'pdo_mysql',
            'mbstring',
            'json',
            'openssl',
            'fileinfo',
            'session',
        ];

        $optional = [
            'gd',
            'curl',
            'intl',
            'mysqli',
            'imagick',
        ];

        $loaded = get_loaded_extensions();
        $loadedLower = array_map('strtolower', $loaded);

        $check = static function (array $names) use ($loadedLower): array {
            $out = [];
            foreach ($names as $name) {
                $out[$name] = in_array(strtolower($name), $loadedLower, true);
            }
            return $out;
        };

        $requiredStatus = $check($required);
        $optionalStatus = $check($optional);

        return [
            'php_version' => PHP_VERSION,
            'sapi' => PHP_SAPI,
            'required' => $requiredStatus,
            'optional' => $optionalStatus,
            'all_required_ok' => !in_array(false, $requiredStatus, true),
            'app_skeleton' => 'Phase 1A source skeleton',
            'db_status' => 'DB not configured / not tested in Phase 1A',
            'env_local_present' => $this->config->envLocalPresent(),
            'env_required' => false,
            'wordpress' => 'not used',
        ];
    }

    public function index(): void
    {
        $status = $this->collectStatus();
        $this->render('health', [
            'pageTitle' => 'Health',
            'status' => $status,
        ]);
    }

    public function notFound(): void
    {
        $this->render('not-found', [
            'pageTitle' => 'Not Found',
            'path' => request_path(),
        ], 404);
    }
}
