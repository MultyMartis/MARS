<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportContentService;
use Iseo\Services\SpecialistReportContentWorkflowService;
use Iseo\Support\Response;
use Throwable;

/**
 * Friendly specialist content workflow for monthly report section texts.
 */
final class MonthlyReportContentWorkflowController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private MonthlyReportContentService $monthlyReports,
        private SpecialistReportContentWorkflowService $workflow
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function show(int $monthlyReportId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user) || !$this->workflow->canView($user)) {
            $this->denyAccess();
            return;
        }

        try {
            $payload = $this->workflow->loadPage($user, $monthlyReportId);
        } catch (Throwable) {
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Error</title></head>'
                . '<body><h1>Content workflow unavailable</h1>'
                . '<p>Unable to load report content workflow.</p>'
                . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
                500
            );
            return;
        }

        if ($payload === null) {
            $this->notFoundReport();
            return;
        }

        if (empty($payload['ok'])) {
            $this->denyAccess((string) ($payload['message'] ?? 'Доступ ограничен.'));
            return;
        }

        /** @var array<string, mixed> $report */
        $report = $payload['report'];
        $periodKey = (string) ($report['period_key'] ?? '');

        $this->render('monthly-reports/content-workflow', [
            'pageTitle' => 'Тексты отчета',
            'report' => $report,
            'periodKey' => $periodKey,
            'editable' => !empty($payload['editable']),
            'readOnlyReason' => $payload['read_only_reason'] ?? null,
            'sections' => $payload['sections'] ?? [],
            'isSpecialistFlow' => $this->auth->isSpecialistFlow($user),
        ]);
    }

    public function saveSection(int $monthlyReportId, string $sectionKey): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $workflowPath = '/monthly-reports/' . $monthlyReportId . '/content-workflow';

        if (!$this->monthlyReports->canList($user) || !$this->workflow->canView($user)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'Сессия устарела. Обновите форму и повторите.');
            $this->redirect($workflowPath);
            return;
        }

        if (!$this->workflow->isAllowedSectionKey($sectionKey)) {
            flash_set('warn', 'Недопустимый раздел отчета.');
            $this->redirect($workflowPath);
            return;
        }

        $raw = $_POST['section_text'] ?? '';
        $text = is_string($raw) ? $raw : '';

        try {
            $result = $this->workflow->saveSection($user, $monthlyReportId, $sectionKey, $text);
        } catch (Throwable) {
            flash_set('warn', 'Не удалось сохранить раздел. Отчет не изменён.');
            $this->redirect($workflowPath);
            return;
        }

        if (!empty($result['ok'])) {
            flash_set('info', (string) ($result['message'] ?? 'Раздел отчета сохранен.'));
            $this->redirect($workflowPath . '#section-' . $sectionKey);
            return;
        }

        $code = (string) ($result['code'] ?? '');
        if ($code === 'not_found') {
            $this->notFoundReport();
            return;
        }
        if ($code === 'forbidden') {
            $this->denyAccess((string) ($result['message'] ?? 'Доступ ограничен.'));
            return;
        }

        flash_set('warn', (string) ($result['message'] ?? 'Сохранение отклонено.'));
        $this->redirect($workflowPath . '#section-' . $sectionKey);
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

    private function denyAccess(?string $message = null): void
    {
        $this->renderAccessDenied(
            $message ?? 'У вас нет доступа к этой странице.',
            [
                'showPeriodsLink' => true,
                'backHref' => url_path('/reporting-periods'),
                'backLabel' => 'К периодам',
            ]
        );
    }

    private function notFoundReport(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Not found</title></head>'
            . '<body><h1>Месячный отчет не найден</h1>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">К периодам</a></p></body></html>',
            404
        );
    }

    private function validateCsrf(): bool
    {
        $token = $_POST['_csrf'] ?? null;
        return $this->csrf->validate(is_string($token) ? $token : null);
    }
}
