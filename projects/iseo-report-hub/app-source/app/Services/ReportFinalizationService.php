<?php
declare(strict_types=1);

namespace Iseo\Services;

use Iseo\Repositories\MonthlyReportContentRepository;
use Iseo\Repositories\ReportBlockRepository;
use Throwable;

/**
 * Internal monthly report finalization: readiness gates, staged transitions, locks via status.
 */
final class ReportFinalizationService
{
    /** @var list<string> */
    public const REQUIRED_BLOCK_KEYS = [
        'executive_summary',
        'work_completed',
        'results_summary',
        'key_findings',
        'next_month_plan',
    ];

    /** @var list<string> */
    private const SUBMIT_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
        'seo_specialist',
    ];

    /** @var list<string> */
    private const REVIEW_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
    ];

    /** @var list<string> */
    private const FINALIZE_ROLES = [
        'admin_owner',
        'seo_lead_reviewer',
    ];

    /** @var list<string> */
    private const REOPEN_ROLES = [
        'admin_owner',
    ];

    /** @var list<string> */
    private const BLOCK_READY_STATUSES = [
        'reviewed',
        'approved',
    ];

    public function __construct(
        private MonthlyReportContentRepository $monthlyRepo,
        private ReportBlockRepository $blockRepo,
        private ReportPreviewService $preview,
        private DatabaseService $db
    ) {
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{
     *   ok:bool,
     *   ready:bool,
     *   monthly:?array<string,mixed>,
     *   period:?array<string,mixed>,
     *   gates:array<string,array{pass:bool,detail:string}>,
     *   failed_gates:list<string>,
     *   actions:array<string,array{allowed:bool,reason:?string}>,
     *   message?:string
     * }
     */
    public function getReadiness(int $monthlyReportId, array $actor): array
    {
        $this->assertDb();

        $monthly = $this->monthlyRepo->findById($monthlyReportId);
        $period = null;
        if ($monthly !== null) {
            $period = $this->monthlyRepo->findPeriodById((int) $monthly['reporting_period_id']);
        }

        $gates = $this->buildGates($monthly, $period);
        $failed = [];
        foreach ($gates as $key => $gate) {
            if (empty($gate['pass'])) {
                $failed[] = $key;
            }
        }
        $ready = $failed === [];

        return [
            'ok' => true,
            'ready' => $ready,
            'monthly' => $monthly,
            'period' => $period,
            'gates' => $gates,
            'failed_gates' => $failed,
            'actions' => $this->describeActions($actor, $monthly, $ready, $failed),
        ];
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{ok:bool,message:string,errors?:array<string,string>,readiness?:array<string,mixed>}
     */
    public function submitForReview(int $monthlyReportId, array $actor): array
    {
        return $this->transition(
            $monthlyReportId,
            $actor,
            'in_progress',
            'ready_for_review',
            self::SUBMIT_ROLES,
            'monthly_report.submitted_for_review',
            false,
            'Submitted for review.'
        );
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{ok:bool,message:string,errors?:array<string,string>,readiness?:array<string,mixed>}
     */
    public function markReviewed(int $monthlyReportId, array $actor): array
    {
        return $this->transition(
            $monthlyReportId,
            $actor,
            'ready_for_review',
            'reviewed',
            self::REVIEW_ROLES,
            'monthly_report.reviewed',
            false,
            'Marked as reviewed.'
        );
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{ok:bool,message:string,errors?:array<string,string>,readiness?:array<string,mixed>}
     */
    public function finalize(int $monthlyReportId, array $actor): array
    {
        return $this->transition(
            $monthlyReportId,
            $actor,
            'reviewed',
            'finalized',
            self::FINALIZE_ROLES,
            'monthly_report.finalized',
            true,
            'Monthly report finalized.'
        );
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @return array{ok:bool,message:string,errors?:array<string,string>,readiness?:array<string,mixed>}
     */
    public function reopen(int $monthlyReportId, array $actor): array
    {
        return $this->transition(
            $monthlyReportId,
            $actor,
            'finalized',
            'reviewed',
            self::REOPEN_ROLES,
            'monthly_report.reopened',
            false,
            'Monthly report reopened (status reviewed). finalized_at preserved.'
        );
    }

    /**
     * Parent monthly finalized → block all normal content/block mutations until reopen.
     */
    public function isMonthlyFinalizedLocked(array $monthly): bool
    {
        return (string) ($monthly['status'] ?? '') === 'finalized';
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param list<string> $allowedRoles
     * @return array{ok:bool,message:string,errors?:array<string,string>,readiness?:array<string,mixed>}
     */
    private function transition(
        int $monthlyReportId,
        array $actor,
        string $fromStatus,
        string $toStatus,
        array $allowedRoles,
        string $auditEvent,
        bool $requireReadiness,
        string $successMessage
    ): array {
        $this->assertDb();

        if (!$this->userHasAnyRole($actor, $allowedRoles)) {
            return [
                'ok' => false,
                'message' => 'You do not have permission for this finalization action.',
                'errors' => ['role' => 'Insufficient role.'],
            ];
        }

        $monthly = $this->monthlyRepo->findById($monthlyReportId);
        if ($monthly === null) {
            return [
                'ok' => false,
                'message' => 'Monthly report content not found.',
                'errors' => ['id' => 'Not found.'],
            ];
        }

        $oldStatus = (string) $monthly['status'];
        if ($oldStatus !== $fromStatus) {
            $this->auditFailure($actor, $monthly, $oldStatus, $toStatus, ['status_mismatch'], [
                'expected_from' => $fromStatus,
                'actual_from' => $oldStatus,
            ]);
            return [
                'ok' => false,
                'message' => 'Status transition is not allowed from current status.',
                'errors' => [
                    'status' => 'Expected status "' . $fromStatus . '", current is "' . $oldStatus . '".',
                ],
            ];
        }

        $period = $this->monthlyRepo->findPeriodById((int) $monthly['reporting_period_id']);
        $readiness = null;
        if ($requireReadiness) {
            $gates = $this->buildGates($monthly, $period);
            $failed = [];
            foreach ($gates as $key => $gate) {
                if (empty($gate['pass'])) {
                    $failed[] = $key;
                }
            }
            $readiness = [
                'ready' => $failed === [],
                'gates' => $gates,
                'failed_gates' => $failed,
            ];
            if ($failed !== []) {
                $this->auditFailure($actor, $monthly, $oldStatus, $toStatus, $failed, [
                    'gates' => $this->gatePassMap($gates),
                ]);
                return [
                    'ok' => false,
                    'message' => 'Readiness checklist failed. Finalization blocked.',
                    'errors' => ['readiness' => 'Failed gates: ' . implode(', ', $failed)],
                    'readiness' => $readiness,
                ];
            }
        }

        $reviewedAt = $monthly['reviewed_at'] !== null && $monthly['reviewed_at'] !== ''
            ? (string) $monthly['reviewed_at']
            : null;
        $finalizedAt = $monthly['finalized_at'] !== null && $monthly['finalized_at'] !== ''
            ? (string) $monthly['finalized_at']
            : null;

        $now = date('Y-m-d H:i:s');
        if ($toStatus === 'reviewed' && $reviewedAt === null) {
            $reviewedAt = $now;
        }
        if ($toStatus === 'finalized' && $finalizedAt === null) {
            $finalizedAt = $now;
            if ($reviewedAt === null) {
                $reviewedAt = $now;
            }
        }
        // Reopen: preserve finalized_at (MVP).

        $pdo = $this->monthlyRepo->pdo();
        try {
            $pdo->beginTransaction();
            $this->monthlyRepo->updateLifecycle(
                (int) $monthly['id'],
                $toStatus,
                $reviewedAt,
                $finalizedAt,
                (int) $actor['id']
            );

            $meta = [
                'monthly_report_content_id' => (int) $monthly['id'],
                'reporting_period_id' => (int) $monthly['reporting_period_id'],
                'old_status' => $oldStatus,
                'new_status' => $toStatus,
                'actor_user_id' => (int) $actor['id'],
                'finalized_at' => $finalizedAt,
            ];
            if ($readiness !== null) {
                $meta['readiness_ready'] = true;
                $meta['failed_gate_keys'] = [];
            }

            $this->monthlyRepo->insertAudit($auditEvent, (int) $actor['id'], (int) $monthly['id'], $meta);
            $this->monthlyRepo->insertAudit(
                'monthly_report_content.status_changed',
                (int) $actor['id'],
                (int) $monthly['id'],
                [
                    'id' => (int) $monthly['id'],
                    'from' => $oldStatus,
                    'to' => $toStatus,
                    'via' => 'finalization_workflow',
                ]
            );

            $pdo->commit();

            return [
                'ok' => true,
                'message' => $successMessage,
                'readiness' => $readiness,
            ];
        } catch (Throwable) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            $this->auditFailure($actor, $monthly, $oldStatus, $toStatus, ['persist_failed'], []);
            return [
                'ok' => false,
                'message' => 'Could not complete finalization action. Please try again.',
                'errors' => [],
            ];
        }
    }

    /**
     * @param array<string, mixed>|null $monthly
     * @param array<string, mixed>|null $period
     * @return array<string, array{pass:bool,detail:string}>
     */
    private function buildGates(?array $monthly, ?array $period): array
    {
        $gates = [
            'monthly_exists' => [
                'pass' => $monthly !== null,
                'detail' => $monthly !== null ? 'Monthly report found.' : 'Monthly report missing.',
            ],
            'period_exists' => [
                'pass' => $period !== null,
                'detail' => $period !== null ? 'Parent reporting period found.' : 'Parent reporting period missing.',
            ],
            'title_present' => [
                'pass' => false,
                'detail' => 'Title missing.',
            ],
            'preview_renderable' => [
                'pass' => false,
                'detail' => 'Preview not assembled.',
            ],
            'render_mode_valid' => [
                'pass' => false,
                'detail' => 'Render mode invalid for finalize.',
            ],
            'has_non_archived_blocks' => [
                'pass' => false,
                'detail' => 'No non-archived blocks.',
            ],
            'required_blocks_present' => [
                'pass' => false,
                'detail' => 'Required blocks missing.',
            ],
            'required_blocks_reviewed' => [
                'pass' => false,
                'detail' => 'Required blocks not reviewed/approved.',
            ],
            'no_draft_or_in_progress_blocks' => [
                'pass' => false,
                'detail' => 'Draft/in_progress blocks remain.',
            ],
            'source_weekly_refs_resolve' => [
                'pass' => false,
                'detail' => 'Source weekly refs unresolved.',
            ],
        ];

        if ($monthly === null) {
            return $gates;
        }

        $title = trim((string) ($monthly['title'] ?? ''));
        $gates['title_present'] = [
            'pass' => $title !== '',
            'detail' => $title !== '' ? 'Title present.' : 'Title empty.',
        ];

        $renderMode = 'empty';
        $missingWeekly = [];
        $previewOk = false;
        try {
            $payload = $this->preview->assemble((int) $monthly['id']);
            if ($payload !== null) {
                $previewOk = true;
                $renderMode = (string) ($payload['render_mode'] ?? 'empty');
                $missingWeekly = $payload['diagnostics']['missing_weekly_ids'] ?? [];
                if (!is_array($missingWeekly)) {
                    $missingWeekly = [];
                }
            }
        } catch (Throwable) {
            $previewOk = false;
        }

        $gates['preview_renderable'] = [
            'pass' => $previewOk,
            'detail' => $previewOk ? 'Preview assembles successfully.' : 'Preview assembly failed.',
        ];

        $modeValid = in_array($renderMode, ['blocks_primary', 'flat_fallback'], true);
        $gates['render_mode_valid'] = [
            'pass' => $modeValid,
            'detail' => $modeValid
                ? 'Render mode "' . $renderMode . '" is valid.'
                : 'Render mode "' . $renderMode . '" is not allowed for finalize (need blocks_primary or flat_fallback).',
        ];

        $allBlocks = $this->blockRepo->listByMonthlyReportId((int) $monthly['id']);
        $active = [];
        foreach ($allBlocks as $block) {
            if ((string) ($block['status'] ?? '') === 'archived') {
                continue;
            }
            $active[] = $block;
        }

        $gates['has_non_archived_blocks'] = [
            'pass' => $active !== [],
            'detail' => $active !== []
                ? count($active) . ' non-archived block(s).'
                : 'At least one non-archived block is required.',
        ];

        $byKey = [];
        foreach ($active as $block) {
            $byKey[(string) $block['block_key']] = $block;
        }
        $missingRequired = [];
        foreach (self::REQUIRED_BLOCK_KEYS as $key) {
            if (!isset($byKey[$key])) {
                $missingRequired[] = $key;
            }
        }
        $gates['required_blocks_present'] = [
            'pass' => $missingRequired === [],
            'detail' => $missingRequired === []
                ? 'All required blocks present.'
                : 'Missing required blocks: ' . implode(', ', $missingRequired),
        ];

        $notReviewed = [];
        foreach (self::REQUIRED_BLOCK_KEYS as $key) {
            if (!isset($byKey[$key])) {
                $notReviewed[] = $key;
                continue;
            }
            $st = (string) $byKey[$key]['status'];
            if (!in_array($st, self::BLOCK_READY_STATUSES, true)) {
                $notReviewed[] = $key . '=' . $st;
            }
        }
        $gates['required_blocks_reviewed'] = [
            'pass' => $missingRequired === [] && $notReviewed === [],
            'detail' => ($missingRequired === [] && $notReviewed === [])
                ? 'Required blocks are reviewed or approved.'
                : 'Required blocks not ready: ' . implode(', ', $notReviewed),
        ];

        $draftish = [];
        foreach ($active as $block) {
            $st = (string) $block['status'];
            if (in_array($st, ['draft', 'in_progress'], true)) {
                $draftish[] = (string) $block['block_key'] . '=' . $st;
            }
        }
        $gates['no_draft_or_in_progress_blocks'] = [
            'pass' => $draftish === [],
            'detail' => $draftish === []
                ? 'No non-archived draft/in_progress blocks.'
                : 'Blocking blocks: ' . implode(', ', $draftish),
        ];

        $missingList = [];
        foreach ($missingWeekly as $id) {
            $missingList[] = (string) $id;
        }
        $gates['source_weekly_refs_resolve'] = [
            'pass' => $missingList === [],
            'detail' => $missingList === []
                ? 'All source weekly checkpoint refs resolve.'
                : 'Missing weekly ids: ' . implode(', ', $missingList),
        ];

        return $gates;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param array<string, mixed>|null $monthly
     * @param list<string> $failed
     * @return array<string, array{allowed:bool,reason:?string}>
     */
    private function describeActions(array $actor, ?array $monthly, bool $ready, array $failed): array
    {
        $status = $monthly !== null ? (string) $monthly['status'] : '';

        $actions = [
            'submit_review' => [
                'allowed' => false,
                'reason' => null,
            ],
            'mark_reviewed' => [
                'allowed' => false,
                'reason' => null,
            ],
            'finalize' => [
                'allowed' => false,
                'reason' => null,
            ],
            'reopen' => [
                'allowed' => false,
                'reason' => null,
            ],
        ];

        if ($monthly === null) {
            foreach ($actions as $k => $_) {
                $actions[$k]['reason'] = 'Monthly report missing.';
            }
            return $actions;
        }

        if ($this->userHasAnyRole($actor, self::SUBMIT_ROLES) && $status === 'in_progress') {
            $actions['submit_review']['allowed'] = true;
        } elseif (!$this->userHasAnyRole($actor, self::SUBMIT_ROLES)) {
            $actions['submit_review']['reason'] = 'Role cannot submit for review.';
        } else {
            $actions['submit_review']['reason'] = 'Status must be in_progress (current: ' . $status . ').';
        }

        if ($this->userHasAnyRole($actor, self::REVIEW_ROLES) && $status === 'ready_for_review') {
            $actions['mark_reviewed']['allowed'] = true;
        } elseif (!$this->userHasAnyRole($actor, self::REVIEW_ROLES)) {
            $actions['mark_reviewed']['reason'] = 'Role cannot mark reviewed.';
        } else {
            $actions['mark_reviewed']['reason'] = 'Status must be ready_for_review (current: ' . $status . ').';
        }

        if ($this->userHasAnyRole($actor, self::FINALIZE_ROLES) && $status === 'reviewed' && $ready) {
            $actions['finalize']['allowed'] = true;
        } elseif (!$this->userHasAnyRole($actor, self::FINALIZE_ROLES)) {
            $actions['finalize']['reason'] = 'Role cannot finalize.';
        } elseif ($status !== 'reviewed') {
            $actions['finalize']['reason'] = 'Status must be reviewed (current: ' . $status . ').';
        } else {
            $actions['finalize']['reason'] = 'Readiness failed: ' . implode(', ', $failed);
        }

        if ($this->userHasAnyRole($actor, self::REOPEN_ROLES) && $status === 'finalized') {
            $actions['reopen']['allowed'] = true;
        } elseif (!$this->userHasAnyRole($actor, self::REOPEN_ROLES)) {
            $actions['reopen']['reason'] = 'Only admin_owner can reopen.';
        } else {
            $actions['reopen']['reason'] = 'Status must be finalized (current: ' . $status . ').';
        }

        return $actions;
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string} $actor
     * @param array<string, mixed> $monthly
     * @param list<string> $failedGates
     * @param array<string, mixed> $extra
     */
    private function auditFailure(
        array $actor,
        array $monthly,
        string $oldStatus,
        string $attemptedStatus,
        array $failedGates,
        array $extra
    ): void {
        try {
            $meta = array_merge([
                'monthly_report_content_id' => (int) $monthly['id'],
                'reporting_period_id' => (int) $monthly['reporting_period_id'],
                'old_status' => $oldStatus,
                'attempted_status' => $attemptedStatus,
                'failed_gate_keys' => $failedGates,
                'actor_user_id' => (int) $actor['id'],
            ], $extra);
            $this->monthlyRepo->insertAudit(
                'monthly_report.finalization_failed',
                (int) $actor['id'],
                (int) $monthly['id'],
                $meta
            );
        } catch (Throwable) {
            // Audit must not break user-facing error path.
        }
    }

    /**
     * @param array<string, array{pass:bool,detail:string}> $gates
     * @return array<string, bool>
     */
    private function gatePassMap(array $gates): array
    {
        $out = [];
        foreach ($gates as $key => $gate) {
            $out[$key] = !empty($gate['pass']);
        }
        return $out;
    }

    private function assertDb(): void
    {
        if (!$this->db->isConfigured()) {
            throw new \RuntimeException('Database is not configured.');
        }
        $this->db->assertLocalDevDatabase();
    }

    /**
     * @param array{id:int,email:string,name:string,roles:list<string>,authenticated_at:string}|null $user
     * @param list<string> $roles
     */
    private function userHasAnyRole(?array $user, array $roles): bool
    {
        if ($user === null) {
            return false;
        }
        $have = $user['roles'] ?? [];
        if (!is_array($have)) {
            return false;
        }
        foreach ($roles as $role) {
            if (in_array($role, $have, true)) {
                return true;
            }
        }
        return false;
    }
}
