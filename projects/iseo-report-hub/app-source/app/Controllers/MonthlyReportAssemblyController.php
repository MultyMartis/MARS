<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\MonthlyReportSummaryApplyService;
use Iseo\Services\MonthlyReportSummaryAssemblyService;
use Iseo\Support\Response;
use Throwable;

/**
 * Assembly preview (GET) and selected-block apply (POST).
 * Apply refuses finalized/archived reports and never touches PDF/export/share.
 */
final class MonthlyReportAssemblyController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private MonthlyReportContentService $monthlyReports,
        private MonthlyReportSummaryAssemblyService $assembly,
        private MonthlyReportSummaryApplyService $apply
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function preview(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        try {
            $payload = $this->assembly->preview($monthlyReportId);
        } catch (Throwable) {
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Error</title></head>'
                . '<body><h1>Assembly preview unavailable</h1>'
                . '<p>Unable to assemble work-entry draft preview.</p>'
                . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
                500
            );
            return;
        }

        if ($payload === null) {
            $this->notFoundReport();
            return;
        }

        /** @var array<string, mixed> $monthly */
        $monthly = $payload['monthly'];
        $periodKey = (string) ($monthly['period_key'] ?? '');
        $parentFinalized = !empty($payload['parent_finalized']);
        $parentArchived = !empty($payload['parent_archived']);
        $canApply = $this->apply->canApply($user);
        $applyLocked = $parentFinalized || $parentArchived;

        $this->render('monthly-reports/assembly-preview', [
            'pageTitle' => 'Черновик отчета из работ',
            'report' => $monthly,
            'periodKey' => $periodKey,
            'stats' => $payload['stats'],
            'drafts' => $payload['drafts'],
            'manual' => $payload['manual'],
            'candidatesKeyFindings' => $payload['candidates_key_findings'],
            'excluded' => $payload['excluded'],
            'existingBlocks' => $payload['existing_blocks'],
            'applyBlocks' => $payload['apply_blocks'] ?? [],
            'warnings' => $payload['warnings'],
            'parentFinalized' => $parentFinalized,
            'parentArchived' => $parentArchived,
            'canApply' => $canApply,
            'applyLocked' => $applyLocked,
            'emitApplyForm' => $canApply && !$applyLocked,
            'finalizedApplyCopy' => MonthlyReportSummaryAssemblyService::FINALIZED_APPLY_COPY,
        ]);
    }

    public function apply(int $monthlyReportId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $previewPath = '/monthly-reports/' . $monthlyReportId . '/assembly-preview';

        if (!$this->apply->canApply($user)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'Сессия устарела. Обновите форму и повторите.');
            $this->redirect($previewPath);
            return;
        }

        $rawKeys = $_POST['block_keys'] ?? [];
        $selected = is_array($rawKeys) ? $rawKeys : [];
        $confirmed = isset($_POST['confirm_overwrite']) && (string) $_POST['confirm_overwrite'] === '1';

        try {
            $result = $this->apply->apply($user, $monthlyReportId, $selected, $confirmed);
        } catch (Throwable) {
            flash_set('warn', 'Не удалось применить черновик. Отчет не изменён.');
            $this->redirect($previewPath);
            return;
        }

        if (!empty($result['ok'])) {
            flash_set('info', (string) ($result['message'] ?? 'Черновик записан.'));
            if (!empty($result['warn_message'])) {
                flash_set('warn', (string) $result['warn_message']);
            }
            $this->redirect('/monthly-reports/' . $monthlyReportId);
            return;
        }

        $code = (string) ($result['code'] ?? '');
        if ($code === 'not_found') {
            $this->notFoundReport();
            return;
        }

        flash_set('warn', (string) ($result['message'] ?? 'Применение черновика отклонено.'));
        $this->redirect($previewPath);
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
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this assembly action.</p>'
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
