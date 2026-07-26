<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\MonthlyReportContentService;
use Iseo\Support\Response;

final class MonthlyReportContentController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private MonthlyReportContentService $monthlyReports
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function showForPeriod(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        $report = $this->monthlyReports->getByPeriodId($periodId);
        if ($report === null) {
            if ($this->monthlyReports->canCreate($user)
                && $this->monthlyReports->canMutateAgainstParent($user, $period)) {
                $this->redirect('/reporting-periods/' . $periodId . '/monthly-report/create');
                return;
            }
            Response::html(
                '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>No monthly report</title></head>'
                . '<body><h1>No monthly report content</h1>'
                . '<p>No monthly report content exists for this period.</p>'
                . '<p><a href="' . e(url_path('/reporting-periods/' . $periodId)) . '">Back to period</a></p>'
                . '</body></html>',
                404
            );
            return;
        }

        $this->renderShow($user, $report, $period);
    }

    public function show(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->monthlyReports->canList($user)) {
            $this->denyAccess();
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        $this->renderShow($user, $report, $period);
    }

    public function create(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canCreate($user)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $existing = $this->monthlyReports->getByPeriodId($periodId);
        if ($existing !== null) {
            flash_set('warn', 'A monthly report content row already exists for this reporting period.');
            $this->redirect('/monthly-reports/' . (int) $existing['id']);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);

        $this->render('monthly-reports/create', [
            'pageTitle' => 'Create monthly report',
            'mode' => 'create',
            'period' => $period,
            'report' => null,
            'old' => $this->defaultCreateOld($period, $available),
            'errors' => [],
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, null),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'content' => false,
                'source_ids' => false,
            ],
        ]);
    }

    public function store(int $periodId): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->monthlyReports->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canCreate($user)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/reporting-periods/' . $periodId . '/monthly-report/create');
            return;
        }

        $existing = $this->monthlyReports->getByPeriodId($periodId);
        if ($existing !== null) {
            flash_set('warn', 'A monthly report content row already exists for this reporting period.');
            $this->redirect('/monthly-reports/' . (int) $existing['id']);
            return;
        }

        $input = $this->readInput();
        $result = $this->monthlyReports->create($user, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Monthly report content created.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/monthly-reports/' . (int) $result['id']);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);
        $this->render('monthly-reports/create', [
            'pageTitle' => 'Create monthly report',
            'mode' => 'create',
            'period' => $period,
            'report' => null,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, null),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'content' => false,
                'source_ids' => false,
            ],
        ], 422);
    }

    public function edit(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canEdit($user, $report)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints((int) $period['id']);

        $this->render('monthly-reports/edit', [
            'pageTitle' => 'Edit monthly report',
            'mode' => 'edit',
            'period' => $period,
            'report' => $report,
            'old' => $this->reportToOld($report),
            'errors' => [],
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, (string) $report['status']),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => $this->locksForReport($report, $user),
        ]);
    }

    public function update(int $id): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $report = $this->monthlyReports->getById($id);
        if ($report === null) {
            $this->notFoundReport();
            return;
        }

        $period = $this->monthlyReports->getPeriod((int) $report['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->monthlyReports->canEdit($user, $report)
            || !$this->monthlyReports->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/monthly-reports/' . $id . '/edit');
            return;
        }

        $input = $this->readInput();
        $result = $this->monthlyReports->update($user, $report, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Monthly report content updated.');
            if (!empty($result['notice'])) {
                flash_set('warn', (string) $result['notice']);
            }
            $this->redirect('/monthly-reports/' . $id);
            return;
        }

        $available = $this->monthlyReports->selectableWeeklyCheckpoints((int) $period['id']);
        $this->render('monthly-reports/edit', [
            'pageTitle' => 'Edit monthly report',
            'mode' => 'edit',
            'period' => $period,
            'report' => $report,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->monthlyReports->selectableInternalUsers(),
            'statuses' => $this->monthlyReports->allowedStatusesForForm($user, (string) $report['status']),
            'availableCheckpoints' => $available,
            'canAssignUsers' => $this->monthlyReports->canAssignOwnerReviewer($user),
            'locks' => $this->locksForReport($report, $user),
        ], 422);
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @param array<string, mixed> $report
     * @param array<string, mixed>|null $period
     */
    private function renderShow(array $user, array $report, ?array $period): void
    {
        $periodId = (int) $report['reporting_period_id'];
        $available = $this->monthlyReports->selectableWeeklyCheckpoints($periodId);
        $sourceIds = $this->monthlyReports->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);
        $sourceRows = $this->monthlyReports->resolveSourceCheckpointRows($sourceIds, $available);

        $canEdit = $period !== null
            && $this->monthlyReports->canEdit($user, $report)
            && $this->monthlyReports->canMutateAgainstParent($user, $period);

        $this->render('monthly-reports/show', [
            'pageTitle' => 'Monthly report — ' . (string) ($report['period_key'] ?? $report['id']),
            'report' => $report,
            'period' => $period,
            'sourceCheckpoints' => $sourceRows,
            'canEdit' => $canEdit,
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

    private function validateCsrf(): bool
    {
        $token = $_POST['_csrf'] ?? null;
        return $this->csrf->validate(is_string($token) ? $token : null);
    }

    /**
     * @return array<string, mixed>
     */
    private function readInput(): array
    {
        $sourceRaw = $_POST['source_weekly_checkpoint_ids'] ?? [];
        if (!is_array($sourceRaw)) {
            $sourceRaw = [];
        }

        return [
            'status' => $_POST['status'] ?? 'draft',
            'title' => $_POST['title'] ?? '',
            'executive_summary' => $_POST['executive_summary'] ?? '',
            'work_completed' => $_POST['work_completed'] ?? '',
            'results_summary' => $_POST['results_summary'] ?? '',
            'key_findings' => $_POST['key_findings'] ?? '',
            'risks_and_blockers' => $_POST['risks_and_blockers'] ?? '',
            'next_month_plan' => $_POST['next_month_plan'] ?? '',
            'client_notes' => $_POST['client_notes'] ?? '',
            'internal_notes' => $_POST['internal_notes'] ?? '',
            'source_weekly_checkpoint_ids' => $sourceRaw,
            'owner_user_id' => $_POST['owner_user_id'] ?? '',
            'reviewer_user_id' => $_POST['reviewer_user_id'] ?? '',
        ];
    }

    /**
     * @param array<string, mixed> $period
     * @param list<array<string, mixed>> $available
     * @return array<string, mixed>
     */
    private function defaultCreateOld(array $period, array $available): array
    {
        $defaultIds = [];
        foreach ($available as $row) {
            $defaultIds[] = (string) $row['id'];
        }

        return [
            'status' => 'draft',
            'title' => 'Monthly report — ' . (string) $period['period_key'] . ' — LOCAL_FIXTURE_ONLY',
            'executive_summary' => '',
            'work_completed' => '',
            'results_summary' => '',
            'key_findings' => '',
            'risks_and_blockers' => '',
            'next_month_plan' => '',
            'client_notes' => '',
            'internal_notes' => '',
            'source_weekly_checkpoint_ids' => $defaultIds,
            'owner_user_id' => '',
            'reviewer_user_id' => '',
        ];
    }

    /**
     * @param array<string, mixed> $report
     * @return array<string, mixed>
     */
    private function reportToOld(array $report): array
    {
        $ids = $this->monthlyReports->decodeSourceIds($report['source_weekly_checkpoint_ids'] ?? null);
        $idStrings = [];
        foreach ($ids as $id) {
            $idStrings[] = (string) $id;
        }

        return [
            'status' => (string) $report['status'],
            'title' => (string) ($report['title'] ?? ''),
            'executive_summary' => (string) ($report['executive_summary'] ?? ''),
            'work_completed' => (string) ($report['work_completed'] ?? ''),
            'results_summary' => (string) ($report['results_summary'] ?? ''),
            'key_findings' => (string) ($report['key_findings'] ?? ''),
            'risks_and_blockers' => (string) ($report['risks_and_blockers'] ?? ''),
            'next_month_plan' => (string) ($report['next_month_plan'] ?? ''),
            'client_notes' => (string) ($report['client_notes'] ?? ''),
            'internal_notes' => (string) ($report['internal_notes'] ?? ''),
            'source_weekly_checkpoint_ids' => $idStrings,
            'owner_user_id' => $report['owner_user_id'] !== null ? (string) $report['owner_user_id'] : '',
            'reviewer_user_id' => $report['reviewer_user_id'] !== null ? (string) $report['reviewer_user_id'] : '',
        ];
    }

    /**
     * @param array<string, mixed> $report
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array{reporting_period_id:bool,content:bool,source_ids:bool}
     */
    private function locksForReport(array $report, array $user): array
    {
        $status = (string) $report['status'];
        $isAdmin = in_array('admin_owner', $user['roles'], true);
        $lockContent = $status === 'finalized' && !$isAdmin;

        return [
            'reporting_period_id' => true,
            'content' => $lockContent,
            'source_ids' => $lockContent,
        ];
    }

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this monthly report action.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundPeriod(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Reporting period not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
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
