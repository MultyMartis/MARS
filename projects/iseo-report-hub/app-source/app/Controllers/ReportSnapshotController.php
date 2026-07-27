<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportExportService;
use Iseo\Services\ReportSnapshotService;
use Iseo\Support\Response;

final class ReportSnapshotController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportSnapshotService $snapshots,
        private ReportExportService $exports
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function monthlySnapshot(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->snapshots->getActiveForMonthly($monthlyReportId, $user);
        if (!$result['ok'] && isset($result['errors']['role'])) {
            $this->denyAccess();
            return;
        }
        if (!$result['ok'] && ($result['monthly'] ?? null) === null) {
            $this->notFoundMonthly();
            return;
        }

        $exportState = $this->exportStateForSnapshot($result['snapshot'], $user);

        $this->render('report-snapshots/show', [
            'pageTitle' => 'Report snapshot — monthly #' . $monthlyReportId,
            'mode' => 'monthly',
            'monthly' => $result['monthly'],
            'snapshot' => $result['snapshot'],
            'payload' => null,
            'canCreate' => !empty($result['can_create']),
            'message' => $result['message'],
            'htmlExport' => $exportState['htmlExport'],
            'pdfExport' => $exportState['pdfExport'],
            'canCreateExport' => $exportState['canCreateExport'],
            'canCreatePdfExport' => $exportState['canCreatePdfExport'],
        ]);
    }

    public function createForMonthly(int $monthlyReportId): void
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
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/snapshot');
            return;
        }

        $result = $this->snapshots->createForMonthly($monthlyReportId, $user);
        if (!$result['ok']) {
            if (isset($result['errors']['role'])) {
                $this->denyAccess();
                return;
            }
            if (isset($result['errors']['id'])) {
                $this->notFoundMonthly();
                return;
            }
            flash_set('error', $result['message']);
            $this->redirect('/monthly-reports/' . $monthlyReportId . '/snapshot');
            return;
        }

        $snapshot = $result['snapshot'];
        $id = is_array($snapshot) ? (int) ($snapshot['id'] ?? 0) : 0;
        if (!empty($result['idempotent'])) {
            flash_set('info', $result['message']);
        } else {
            flash_set('success', $result['message']);
        }

        if ($id > 0) {
            $this->redirect('/report-snapshots/' . $id);
            return;
        }

        $this->redirect('/monthly-reports/' . $monthlyReportId . '/snapshot');
    }

    public function show(int $snapshotId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $result = $this->snapshots->getById($snapshotId, $user);
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

        $exportState = $this->exportStateForSnapshot($snapshot, $user);

        $this->render('report-snapshots/show', [
            'pageTitle' => 'Snapshot — ' . $title,
            'mode' => 'detail',
            'monthly' => null,
            'snapshot' => $snapshot,
            'payload' => $result['payload'],
            'canCreate' => false,
            'message' => $result['message'],
            'htmlExport' => $exportState['htmlExport'],
            'pdfExport' => $exportState['pdfExport'],
            'canCreateExport' => $exportState['canCreateExport'],
            'canCreatePdfExport' => $exportState['canCreatePdfExport'],
        ]);
    }

    /**
     * @param array<string, mixed>|null $snapshot
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array{
     *   htmlExport:?array<string,mixed>,
     *   pdfExport:?array<string,mixed>,
     *   canCreateExport:bool,
     *   canCreatePdfExport:bool
     * }
     */
    private function exportStateForSnapshot(?array $snapshot, array $user): array
    {
        if (!is_array($snapshot)) {
            return [
                'htmlExport' => null,
                'pdfExport' => null,
                'canCreateExport' => false,
                'canCreatePdfExport' => false,
            ];
        }

        $htmlExport = null;
        $pdfExport = null;
        $snapshotId = (int) ($snapshot['id'] ?? 0);
        if ($snapshotId > 0) {
            try {
                $htmlExport = $this->exports->findReadyHtmlForSnapshot($snapshotId);
            } catch (\Throwable) {
                $htmlExport = null;
            }
            try {
                $pdfExport = $this->exports->getReadyExportForSnapshotFormat($snapshotId, 'pdf');
            } catch (\Throwable) {
                $pdfExport = null;
            }
        }

        $canCreateExport = false;
        $canCreatePdfExport = false;
        try {
            $canCreateExport = $this->exports->canCreateExportForSnapshot($snapshot, $user);
        } catch (\Throwable) {
            $canCreateExport = false;
        }
        try {
            $canCreatePdfExport = $this->exports->canCreatePdfForSnapshot($snapshot, $user, $htmlExport);
        } catch (\Throwable) {
            $canCreatePdfExport = false;
        }

        return [
            'htmlExport' => $htmlExport,
            'pdfExport' => $pdfExport,
            'canCreateExport' => $canCreateExport,
            'canCreatePdfExport' => $canCreatePdfExport,
        ];
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
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this report snapshot.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundMonthly(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Monthly report content not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
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
}
