<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\ReportingPeriodService;
use Iseo\Support\Response;

final class ReportingPeriodController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private ReportingPeriodService $periods
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function index(): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->periods->canList($user)) {
            $this->denyAccess();
            return;
        }

        $items = $this->periods->listPeriods();
        foreach ($items as &$item) {
            $item['_can_edit'] = $this->periods->canEdit($user, $item);
        }
        unset($item);

        $this->render('reporting-periods/index', [
            'pageTitle' => 'Reporting periods',
            'periods' => $items,
            'canCreate' => $this->periods->canCreate($user),
        ]);
    }

    public function show(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->periods->canList($user)) {
            $this->denyAccess();
            return;
        }

        $period = $this->periods->getPeriod($id);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        $this->render('reporting-periods/show', [
            'pageTitle' => 'Period ' . (string) $period['period_key'],
            'period' => $period,
            'canEdit' => $this->periods->canEdit($user, $period),
        ]);
    }

    public function create(): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->periods->canCreate($user)) {
            $this->denyAccess();
            return;
        }

        $this->render('reporting-periods/create', [
            'pageTitle' => 'Create reporting period',
            'mode' => 'create',
            'period' => null,
            'old' => $this->defaultCreateOld(),
            'errors' => [],
            'projects' => $this->periods->selectableProjects(),
            'users' => $this->periods->selectableInternalUsers(),
            'statuses' => $this->allowedStatusesForUser($user),
            'locks' => [
                'project_id' => false,
                'period_key' => false,
                'dates' => false,
            ],
        ]);
    }

    public function store(): void
    {
        if (!$this->guardMethod(['POST'])) {
            return;
        }

        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->periods->canCreate($user)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/reporting-periods/create');
            return;
        }

        $input = $this->readInput();
        $result = $this->periods->create($user, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Reporting period created.');
            $this->redirect('/reporting-periods/' . (int) $result['id']);
            return;
        }

        $this->render('reporting-periods/create', [
            'pageTitle' => 'Create reporting period',
            'mode' => 'create',
            'period' => null,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'projects' => $this->periods->selectableProjects(),
            'users' => $this->periods->selectableInternalUsers(),
            'statuses' => $this->allowedStatusesForUser($user),
            'locks' => [
                'project_id' => false,
                'period_key' => false,
                'dates' => false,
            ],
        ], 422);
    }

    public function edit(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->periods->getPeriod($id);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->periods->canEdit($user, $period)) {
            $this->denyAccess();
            return;
        }

        $this->render('reporting-periods/edit', [
            'pageTitle' => 'Edit period ' . (string) $period['period_key'],
            'mode' => 'edit',
            'period' => $period,
            'old' => $this->periodToOld($period),
            'errors' => [],
            'projects' => $this->periods->selectableProjects(),
            'users' => $this->periods->selectableInternalUsers(),
            'statuses' => $this->allowedStatusesForUser($user),
            'locks' => $this->locksForPeriod($period),
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

        $period = $this->periods->getPeriod($id);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->periods->canEdit($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/reporting-periods/' . $id . '/edit');
            return;
        }

        $input = $this->readInput();
        // project_id immutable — ignore posted value
        $input['project_id'] = (int) $period['project_id'];

        $result = $this->periods->update($user, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Reporting period updated.');
            $this->redirect('/reporting-periods/' . $id);
            return;
        }

        $this->render('reporting-periods/edit', [
            'pageTitle' => 'Edit period ' . (string) $period['period_key'],
            'mode' => 'edit',
            'period' => $period,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'projects' => $this->periods->selectableProjects(),
            'users' => $this->periods->selectableInternalUsers(),
            'statuses' => $this->allowedStatusesForUser($user),
            'locks' => $this->locksForPeriod($period),
        ], 422);
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
        return [
            'project_id' => $_POST['project_id'] ?? '',
            'period_key' => $_POST['period_key'] ?? '',
            'period_start' => $_POST['period_start'] ?? '',
            'period_end' => $_POST['period_end'] ?? '',
            'status' => $_POST['status'] ?? 'draft',
            'title' => $_POST['title'] ?? '',
            'summary' => $_POST['summary'] ?? '',
            'owner_user_id' => $_POST['owner_user_id'] ?? '',
            'reviewer_user_id' => $_POST['reviewer_user_id'] ?? '',
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function defaultCreateOld(): array
    {
        return [
            'project_id' => 1,
            'period_key' => '',
            'period_start' => '',
            'period_end' => '',
            'status' => 'draft',
            'title' => '',
            'summary' => '',
            'owner_user_id' => '',
            'reviewer_user_id' => '',
        ];
    }

    /**
     * @param array<string, mixed> $period
     * @return array<string, mixed>
     */
    private function periodToOld(array $period): array
    {
        return [
            'project_id' => (int) $period['project_id'],
            'period_key' => (string) $period['period_key'],
            'period_start' => (string) $period['period_start'],
            'period_end' => (string) $period['period_end'],
            'status' => (string) $period['status'],
            'title' => (string) ($period['title'] ?? ''),
            'summary' => (string) ($period['summary'] ?? ''),
            'owner_user_id' => $period['owner_user_id'] !== null ? (string) $period['owner_user_id'] : '',
            'reviewer_user_id' => $period['reviewer_user_id'] !== null ? (string) $period['reviewer_user_id'] : '',
        ];
    }

    /**
     * @param array<string, mixed> $period
     * @return array{project_id:bool,period_key:bool,dates:bool}
     */
    private function locksForPeriod(array $period): array
    {
        $status = (string) $period['status'];
        return [
            'project_id' => true,
            'period_key' => $status !== 'draft',
            'dates' => !in_array($status, ['draft', 'active'], true),
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return list<string>
     */
    private function allowedStatusesForUser(array $user): array
    {
        $out = [];
        foreach (ReportingPeriodService::STATUSES as $status) {
            if ($this->periods->canSetStatus($user, $status)) {
                $out[] = $status;
            }
        }
        return $out;
    }

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this reporting period action.</p>'
            . '<p><a href="' . e(url_path('/')) . '">Dashboard</a></p></body></html>',
            403
        );
    }

    private function notFoundPeriod(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Reporting period not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to list</a></p></body></html>',
            404
        );
    }
}
