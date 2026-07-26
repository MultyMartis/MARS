<?php
declare(strict_types=1);

namespace Iseo\Controllers;

use Iseo\Services\WeeklyCheckpointService;
use Iseo\Support\Response;

final class WeeklyCheckpointController extends BaseController
{
    public function __construct(
        array $app,
        \Iseo\Support\View $view,
        \Iseo\Services\ConfigService $config,
        \Iseo\Services\AuthService $auth,
        \Iseo\Services\CsrfService $csrf,
        private WeeklyCheckpointService $checkpoints
    ) {
        parent::__construct($app, $view, $config, $auth, $csrf);
    }

    public function indexForPeriod(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->checkpoints->canList($user)) {
            $this->denyAccess();
            return;
        }

        $period = $this->checkpoints->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        $items = $this->checkpoints->listForPeriod($periodId);
        foreach ($items as &$item) {
            $item['_can_edit'] = $this->checkpoints->canEdit($user, $item, $period);
        }
        unset($item);

        $this->render('weekly-checkpoints/index', [
            'pageTitle' => 'Weekly checkpoints — ' . (string) $period['period_key'],
            'period' => $period,
            'checkpoints' => $items,
            'canCreate' => $this->checkpoints->canCreate($user)
                && $this->checkpoints->canMutateAgainstParent($user, $period),
        ]);
    }

    public function show(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        if (!$this->checkpoints->canList($user)) {
            $this->denyAccess();
            return;
        }

        $checkpoint = $this->checkpoints->getCheckpoint($id);
        if ($checkpoint === null) {
            $this->notFoundCheckpoint();
            return;
        }

        $period = $this->checkpoints->getPeriod((int) $checkpoint['reporting_period_id']);

        $this->render('weekly-checkpoints/show', [
            'pageTitle' => 'Checkpoint ' . (string) $checkpoint['checkpoint_key'],
            'checkpoint' => $checkpoint,
            'period' => $period,
            'canEdit' => $this->checkpoints->canEdit($user, $checkpoint, $period),
        ]);
    }

    public function create(int $periodId): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $period = $this->checkpoints->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->checkpoints->canCreate($user)
            || !$this->checkpoints->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $this->render('weekly-checkpoints/create', [
            'pageTitle' => 'Create weekly checkpoint',
            'mode' => 'create',
            'period' => $period,
            'checkpoint' => null,
            'old' => $this->defaultCreateOld($period),
            'errors' => [],
            'users' => $this->checkpoints->selectableInternalUsers(),
            'statuses' => $this->checkpoints->allowedStatusesForForm($user, null),
            'canAssignUsers' => $this->checkpoints->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'week_index' => false,
                'checkpoint_key' => false,
                'dates' => false,
                'text' => false,
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

        $period = $this->checkpoints->getPeriod($periodId);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->checkpoints->canCreate($user)
            || !$this->checkpoints->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/reporting-periods/' . $periodId . '/weekly-checkpoints/create');
            return;
        }

        $input = $this->readInput();
        $result = $this->checkpoints->create($user, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Weekly checkpoint created.');
            $this->redirect('/weekly-checkpoints/' . (int) $result['id']);
            return;
        }

        $this->render('weekly-checkpoints/create', [
            'pageTitle' => 'Create weekly checkpoint',
            'mode' => 'create',
            'period' => $period,
            'checkpoint' => null,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->checkpoints->selectableInternalUsers(),
            'statuses' => $this->checkpoints->allowedStatusesForForm($user, null),
            'canAssignUsers' => $this->checkpoints->canAssignOwnerReviewer($user),
            'locks' => [
                'reporting_period_id' => true,
                'week_index' => false,
                'checkpoint_key' => false,
                'dates' => false,
                'text' => false,
            ],
        ], 422);
    }

    public function edit(int $id): void
    {
        $user = $this->requireInternalUser();
        if ($user === null) {
            return;
        }

        $checkpoint = $this->checkpoints->getCheckpoint($id);
        if ($checkpoint === null) {
            $this->notFoundCheckpoint();
            return;
        }

        $period = $this->checkpoints->getPeriod((int) $checkpoint['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->checkpoints->canEdit($user, $checkpoint, $period)
            || !$this->checkpoints->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        $this->render('weekly-checkpoints/edit', [
            'pageTitle' => 'Edit checkpoint ' . (string) $checkpoint['checkpoint_key'],
            'mode' => 'edit',
            'period' => $period,
            'checkpoint' => $checkpoint,
            'old' => $this->checkpointToOld($checkpoint),
            'errors' => [],
            'users' => $this->checkpoints->selectableInternalUsers(),
            'statuses' => $this->checkpoints->allowedStatusesForForm($user, (string) $checkpoint['status']),
            'canAssignUsers' => $this->checkpoints->canAssignOwnerReviewer($user),
            'locks' => $this->locksForCheckpoint($checkpoint, $user),
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

        $checkpoint = $this->checkpoints->getCheckpoint($id);
        if ($checkpoint === null) {
            $this->notFoundCheckpoint();
            return;
        }

        $period = $this->checkpoints->getPeriod((int) $checkpoint['reporting_period_id']);
        if ($period === null) {
            $this->notFoundPeriod();
            return;
        }

        if (!$this->checkpoints->canEdit($user, $checkpoint, $period)
            || !$this->checkpoints->canMutateAgainstParent($user, $period)) {
            $this->denyAccess();
            return;
        }

        if (!$this->validateCsrf()) {
            flash_set('warn', 'CSRF token invalid or missing. Please try again.');
            $this->redirect('/weekly-checkpoints/' . $id . '/edit');
            return;
        }

        $input = $this->readInput();
        $result = $this->checkpoints->update($user, $checkpoint, $period, $input);

        if (!empty($result['ok'])) {
            flash_set('info', 'Weekly checkpoint updated.');
            $this->redirect('/weekly-checkpoints/' . $id);
            return;
        }

        $this->render('weekly-checkpoints/edit', [
            'pageTitle' => 'Edit checkpoint ' . (string) $checkpoint['checkpoint_key'],
            'mode' => 'edit',
            'period' => $period,
            'checkpoint' => $checkpoint,
            'old' => $input,
            'errors' => $result['errors'] ?? [],
            'formMessage' => $result['message'] ?? 'Please correct the form errors.',
            'users' => $this->checkpoints->selectableInternalUsers(),
            'statuses' => $this->checkpoints->allowedStatusesForForm($user, (string) $checkpoint['status']),
            'canAssignUsers' => $this->checkpoints->canAssignOwnerReviewer($user),
            'locks' => $this->locksForCheckpoint($checkpoint, $user),
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
            'week_index' => $_POST['week_index'] ?? '',
            'checkpoint_key' => $_POST['checkpoint_key'] ?? '',
            'checkpoint_start' => $_POST['checkpoint_start'] ?? '',
            'checkpoint_end' => $_POST['checkpoint_end'] ?? '',
            'status' => $_POST['status'] ?? 'draft',
            'title' => $_POST['title'] ?? '',
            'summary' => $_POST['summary'] ?? '',
            'work_done' => $_POST['work_done'] ?? '',
            'findings' => $_POST['findings'] ?? '',
            'next_steps' => $_POST['next_steps'] ?? '',
            'risks' => $_POST['risks'] ?? '',
            'owner_user_id' => $_POST['owner_user_id'] ?? '',
            'reviewer_user_id' => $_POST['reviewer_user_id'] ?? '',
        ];
    }

    /**
     * @param array<string, mixed> $period
     * @return array<string, mixed>
     */
    private function defaultCreateOld(array $period): array
    {
        $periodKey = (string) $period['period_key'];
        return [
            'week_index' => '4',
            'checkpoint_key' => $periodKey . '-W4',
            'checkpoint_start' => (string) $period['period_start'],
            'checkpoint_end' => (string) $period['period_end'],
            'status' => 'draft',
            'title' => '',
            'summary' => '',
            'work_done' => '',
            'findings' => '',
            'next_steps' => '',
            'risks' => '',
            'owner_user_id' => '',
            'reviewer_user_id' => '',
        ];
    }

    /**
     * @param array<string, mixed> $checkpoint
     * @return array<string, mixed>
     */
    private function checkpointToOld(array $checkpoint): array
    {
        return [
            'week_index' => (string) $checkpoint['week_index'],
            'checkpoint_key' => (string) $checkpoint['checkpoint_key'],
            'checkpoint_start' => (string) $checkpoint['checkpoint_start'],
            'checkpoint_end' => (string) $checkpoint['checkpoint_end'],
            'status' => (string) $checkpoint['status'],
            'title' => (string) ($checkpoint['title'] ?? ''),
            'summary' => (string) ($checkpoint['summary'] ?? ''),
            'work_done' => (string) ($checkpoint['work_done'] ?? ''),
            'findings' => (string) ($checkpoint['findings'] ?? ''),
            'next_steps' => (string) ($checkpoint['next_steps'] ?? ''),
            'risks' => (string) ($checkpoint['risks'] ?? ''),
            'owner_user_id' => $checkpoint['owner_user_id'] !== null ? (string) $checkpoint['owner_user_id'] : '',
            'reviewer_user_id' => $checkpoint['reviewer_user_id'] !== null ? (string) $checkpoint['reviewer_user_id'] : '',
        ];
    }

    /**
     * @param array<string, mixed> $checkpoint
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $user
     * @return array{reporting_period_id:bool,week_index:bool,checkpoint_key:bool,dates:bool,text:bool}
     */
    private function locksForCheckpoint(array $checkpoint, array $user): array
    {
        $status = (string) $checkpoint['status'];
        $isAdmin = in_array('admin_owner', $user['roles'], true);

        return [
            'reporting_period_id' => true,
            'week_index' => $status !== 'draft',
            'checkpoint_key' => $status !== 'draft',
            'dates' => !in_array($status, ['draft', 'in_progress'], true),
            'text' => $status === 'completed' && !$isAdmin,
        ];
    }

    private function denyAccess(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>403</title></head>'
            . '<body><h1>403 Forbidden</h1><p>You do not have access to this weekly checkpoint action.</p>'
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

    private function notFoundCheckpoint(): void
    {
        Response::html(
            '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>404</title></head>'
            . '<body><h1>404 Not Found</h1><p>Weekly checkpoint not found.</p>'
            . '<p><a href="' . e(url_path('/reporting-periods')) . '">Back to periods</a></p></body></html>',
            404
        );
    }
}
