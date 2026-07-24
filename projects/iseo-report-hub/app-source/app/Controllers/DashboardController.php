<?php
declare(strict_types=1);

namespace Iseo\Controllers;

final class DashboardController extends BaseController
{
    public function index(): void
    {
        $this->render('dashboard', [
            'pageTitle' => 'Dashboard',
            'cards' => [
                [
                    'title' => 'Source skeleton',
                    'status' => 'ready',
                    'detail' => 'Bootstrap, router, views, controllers, services present in app-source.',
                ],
                [
                    'title' => 'Runtime sync',
                    'status' => 'pending',
                    'detail' => 'Not synced to X:\\MARS-Localhost in Phase 1A.',
                ],
                [
                    'title' => 'Database',
                    'status' => 'pending',
                    'detail' => (string) $this->config->get('database.phase_1a_note', 'DB not configured / not tested in Phase 1A'),
                ],
                [
                    'title' => 'Auth',
                    'status' => 'stub',
                    'detail' => $this->auth->statusMessage(),
                ],
            ],
        ]);
    }
}
