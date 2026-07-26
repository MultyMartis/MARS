<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportPreviewService;
use Iseo\Services\ReportSnapshotService;
use Iseo\Support\Response;
use Throwable;

final class ReportPreviewController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportPreviewService $preview,
        private ReportSnapshotService $snapshots
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function show(int $monthlyReportId): void
    {
        $this->renderPreview($monthlyReportId, 'report-preview/show', false);
    }

    public function print(int $monthlyReportId): void
    {
        $this->renderPreview($monthlyReportId, 'report-preview/print', true);
    }

    private function renderPreview(int $monthlyReportId, string $view, bool $printMode): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->preview->canPreview($user)) {
            $this->denyAccess();
            return;
        }

        try {
            $payload = $this->preview->assemble($monthlyReportId);
        } catch (Throwable) {
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Error</title></head>'
                . '<body><h1>Preview unavailable</h1>'
                . '<p>Unable to assemble report preview.</p>'
                . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
                500
            );
            return;
        }

        if ($payload === null) {
            $this->notFoundReport();
            return;
        }

        $report = $payload['report'];
        $title = (string) ($report['title'] ?? ('Monthly report #' . $monthlyReportId));
        $pageTitle = ($printMode ? 'Print preview — ' : 'Preview — ') . $title;

        $activeSnapshot = null;
        try {
            $snapState = $this->snapshots->getActiveForMonthly($monthlyReportId, $user);
            if (!empty($snapState['ok'])) {
                $activeSnapshot = $snapState['snapshot'] ?? null;
            }
        } catch (Throwable) {
            $activeSnapshot = null;
        }

        $this->render($view, [
            'pageTitle' => $pageTitle,
            'printMode' => $printMode,
            'report' => $report,
            'blocks' => $payload['blocks'],
            'renderMode' => $payload['render_mode'],
            'flatFields' => $payload['flat_fields'],
            'flatPresent' => $payload['flat_present'],
            'sourceWeekly' => $payload['source_weekly'],
            'diagnostics' => $payload['diagnostics'],
            'generatedAt' => $payload['generated_at'],
            'canEdit' => $this->preview->canPreview($user),
            'activeSnapshot' => $activeSnapshot,
        ]);
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

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this report preview.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundReport(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Monthly report content not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}
