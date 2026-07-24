<?php
declare(strict_types=1);

namespace Iseo\Controllers;

final class DashboardController extends BaseController
{
    public function index(): void
    {
        if (!$this->auth->isAuthenticated() || !$this->auth->hasInternalRole()) {
            $this->redirect('/login');
            return;
        }

        $user = $this->auth->currentUser();
        $dbConfigured = (bool) $this->config->get('database.configured', false);

        $this->render('dashboard', [
            'pageTitle' => 'Dashboard',
            'user' => $user,
            'cards' => [
                [
                    'title' => 'Auth',
                    'status' => 'ready',
                    'detail' => 'DB-backed login active for internal roles.',
                ],
                [
                    'title' => 'Database',
                    'status' => $dbConfigured ? 'ready' : 'pending',
                    'detail' => $dbConfigured
                        ? 'Configured via runtime .env.local (credentials not shown).'
                        : 'Database not configured.',
                ],
                [
                    'title' => 'Runtime',
                    'status' => 'ready',
                    'detail' => 'Local Laragon runtime at iseo-report-hub.test.',
                ],
                [
                    'title' => 'Reporting CRUD',
                    'status' => 'pending',
                    'detail' => 'Not implemented — auth baseline only.',
                ],
            ],
        ]);
    }
}
