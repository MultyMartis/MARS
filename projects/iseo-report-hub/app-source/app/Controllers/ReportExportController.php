<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportExportService;
use Iseo\Support\Response;

final class ReportExportController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportExportService $exports
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function listForSnapshot(int $snapshotId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->exports->listForSnapshot($snapshotId, $user);
        if (!$result['ok'] && isset($result['errors']['role'])) {
            $this->denyAccess();
            return;
        }
        if (!$result['ok'] || $result['snapshot'] === null) {
            $this->notFoundSnapshot();
            return;
        }

        $snapshot = $result['snapshot'];
        $title = (string) ($snapshot['title'] ?? ('Snapshot #' . $snapshotId));

        $this->render('report-exports/index', [
            'pageTitle' => 'Exports — ' . $title,
            'snapshot' => $snapshot,
            'exports' => $result['exports'],
            'canCreate' => !empty($result['can_create']),
            'message' => $result['message'],
        ]);
    }

    public function createHtmlForSnapshot(int $snapshotId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('error', 'Invalid CSRF token. Please try again.');
            $this->redirect('/report-snapshots/' . $snapshotId . '/exports');
            return;
        }

        $result = $this->exports->createHtmlForSnapshot($snapshotId, $user);
        if (!$result['ok']) {
            if (isset($result['errors']['role'])) {
                $this->denyAccess();
                return;
            }
            if (isset($result['errors']['id'])) {
                $this->notFoundSnapshot();
                return;
            }
            flash_set('error', $result['message']);
            $this->redirect('/report-snapshots/' . $snapshotId . '/exports');
            return;
        }

        $export = $result['export'];
        $exportId = is_array($export) ? (int) ($export['id'] ?? 0) : 0;
        if (!empty($result['idempotent'])) {
            flash_set('info', $result['message']);
        } else {
            flash_set('success', $result['message']);
        }

        if ($exportId > 0) {
            $this->redirect('/report-exports/' . $exportId);
            return;
        }

        $this->redirect('/report-snapshots/' . $snapshotId . '/exports');
    }

    public function show(int $exportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->exports->getById($exportId, $user);
        if (!$result['ok'] && isset($result['errors']['role'])) {
            $this->denyAccess();
            return;
        }
        if (!$result['ok'] || $result['export'] === null) {
            $this->notFoundExport();
            return;
        }

        $export = $result['export'];
        $key = (string) ($export['export_key'] ?? ('#' . $exportId));

        $this->render('report-exports/show', [
            'pageTitle' => 'Export — ' . $key,
            'export' => $export,
            'message' => $result['message'],
        ]);
    }

    public function download(int $exportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->exports->download($exportId, $user);
        if (!$result['ok']) {
            if (isset($result['errors']['role'])) {
                $this->denyAccess();
                return;
            }
            if (isset($result['errors']['id'])) {
                $this->notFoundExport();
                return;
            }
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Export unavailable</title></head>'
                . '<body><h1>Export unavailable</h1><p>' . e($result['message']) . '</p>'
                . '<p><a href="' . e(url_path('/report-exports/' . $exportId)) . '">Back to export</a></p></body></html>',
                404
            );
            return;
        }

        $export = $result['export'];
        $absolute = $result['absolute_path'];
        if (!is_array($export) || !is_string($absolute) || $absolute === '') {
            $this->notFoundExport();
            return;
        }

        $filename = (string) ($export['filename'] ?? 'export.html');
        $mime = (string) ($export['mime_type'] ?? 'text/html; charset=UTF-8');

        http_response_code(200);
        header('Content-Type: ' . $mime);
        header('Content-Disposition: attachment; filename="' . str_replace('"', '', $filename) . '"');
        header('Content-Length: ' . (string) filesize($absolute));
        header('X-Content-Type-Options: nosniff');
        readfile($absolute);
        exit;
    }

    /**
     * @return array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null
     */
    private function requireInternalUser(): ?array
    {
        if (!$this->auth->isAuthenticated() || !$this->auth->hasInternalRole()) {
            $this->redirect('/login');
            return null;
        }

        $user = $this->auth->currentUser();
        if ($user === null) {
            $this->redirect('/login');
            return null;
        }

        return $user;
    }

    private function validateCsrf(): bool
    {
        $token = $_POST['_csrf'] ?? null;
        return $this->csrf->validate(is_string($token) ? $token : null);
    }

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to report exports.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundSnapshot(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Report snapshot not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }

    private function notFoundExport(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Report export not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}
