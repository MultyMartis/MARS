<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportExportService;
use Iseo\Services\ReportExportShareService;
use Iseo\Support\Response;

/**
 * Unauthenticated public PDF stream by opaque share token.
 */
final class PublicReportShareController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportExportShareService $shares,
        private ReportExportService $exports
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function download(string $token): void
    {
        if (!$this->guardMethod(['GET'])) {
            return;
        }

        $result = $this->shares->resolvePublicToken($token);
        if (!$result['ok']) {
            $status = (int) ($result['http_status'] ?? 404);
            if ($status !== 410) {
                $status = 404;
            }
            $this->safeDeny($status);
            return;
        }

        $export = $result['export'];
        $absolute = $result['absolute_path'];
        if (!is_array($export) || !is_string($absolute) || $absolute === '' || !is_file($absolute)) {
            $this->safeDeny(404);
            return;
        }

        $filename = $this->exports->safeDownloadFilename($export);
        $size = (int) filesize($absolute);
        if ($size <= 0) {
            $this->safeDeny(404);
            return;
        }

        http_response_code(200);
        header('Content-Type: application/pdf');
        header('Content-Disposition: attachment; filename="' . $filename . '"');
        header('Content-Length: ' . (string) $size);
        header('X-Content-Type-Options: nosniff');
        header('Cache-Control: private, no-store');
        header('X-Robots-Tag: noindex, nofollow');
        readfile($absolute);
        exit;
    }

    private function safeDeny(int $status): void
    {
        $title = $status === 410 ? '410 Gone' : '404 Not Found';
        $heading = $status === 410 ? '410 Gone' : '404 Not Found';
        $message = $status === 410
            ? 'This share link is no longer available.'
            : 'Share link not found.';

        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">'
            . '<meta name="robots" content="noindex, nofollow">'
            . '<title>' . e($title) . '</title></head>'
            . '<body><h1>' . e($heading) . '</h1><p>' . e($message) . '</p></body></html>',
            $status,
            [
                'Cache-Control' => 'private, no-store',
                'X-Robots-Tag' => 'noindex, nofollow',
                'X-Content-Type-Options' => 'nosniff',
            ]
        );
    }
}
