<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportSummaryAssemblyService;
use Iseo\Services\ReportPreviewService;
use Iseo\Services\ReportSnapshotService;
use Iseo\Support\ClientReportDocument;
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
        private ReportSnapshotService $snapshots,
        private MonthlyReportSummaryAssemblyService $assembly
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

        $localDemo = (string) $this->config->get('app.env', 'local') === 'local';
        $assemblyBodies = $this->loadShowReadyAssemblyBodies($monthlyReportId, $localDemo);
        $document = ClientReportDocument::fromAssemble($payload, $localDemo, $assemblyBodies);

        $this->render($view, [
            'pageTitle' => (string) ($document['page_title'] ?? 'SEO-отчёт'),
            'printMode' => $printMode,
            'document' => $document,
            'monthlyReportId' => $monthlyReportId,
        ], 200, 'layouts/layout-client-report');
    }

    /**
     * Read-only work-entry assembly text for local demo report 1 auto sections.
     * Never writes DB. Empty map for all other reports / non-local env.
     *
     * @return array<string, string>
     */
    private function loadShowReadyAssemblyBodies(int $monthlyReportId, bool $localDemo): array
    {
        if (
            !$localDemo
            || $monthlyReportId !== ClientReportDocument::SHOW_READY_DEMO_REPORT_ID
        ) {
            return [];
        }

        try {
            $preview = $this->assembly->preview($monthlyReportId);
        } catch (Throwable) {
            return [];
        }

        if ($preview === null || !is_array($preview['drafts'] ?? null)) {
            return [];
        }

        $bodies = [];
        foreach (['work_completed', 'risks_and_blockers', 'next_month_plan'] as $key) {
            $draft = is_array($preview['drafts'][$key] ?? null) ? $preview['drafts'][$key] : [];
            $items = is_array($draft['items'] ?? null) ? $draft['items'] : [];
            if ($items === []) {
                continue;
            }
            $body = $this->assembly->formatBlockBody($key, $items);
            if ($body === null || trim($body) === '') {
                continue;
            }
            // Skip calm empty-risks apply copy — prefer show-ready demo fallback instead.
            if (
                $key === 'risks_and_blockers'
                && trim($body) === MonthlyReportSummaryAssemblyService::EMPTY_RISKS_APPLY_COPY
            ) {
                continue;
            }
            $bodies[$key] = $body;
        }

        return $bodies;
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
