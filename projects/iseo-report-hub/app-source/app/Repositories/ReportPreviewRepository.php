<?php
declare(strict_types=1);

namespace Iseo\Repositories;

use Iseo\Services\DatabaseService;
use PDO;

/**
 * Read-only composition queries for monthly report preview.
 */
final class ReportPreviewRepository
{
    public function __construct(
        private DatabaseService $db
    ) {
    }

    public function pdo(): PDO
    {
        return $this->db->connect();
    }

    /**
     * Monthly report + period / client / project / primary site context.
     *
     * @return array<string, mixed>|null
     */
    public function findMonthlyWithContext(int $monthlyReportId): ?array
    {
        if ($monthlyReportId <= 0) {
            return null;
        }

        $sql = <<<'SQL'
SELECT
    mrc.id,
    mrc.reporting_period_id,
    mrc.status,
    mrc.title,
    mrc.executive_summary,
    mrc.work_completed,
    mrc.results_summary,
    mrc.key_findings,
    mrc.risks_and_blockers,
    mrc.next_month_plan,
    mrc.client_notes,
    mrc.internal_notes,
    mrc.source_weekly_checkpoint_ids,
    mrc.owner_user_id,
    mrc.reviewer_user_id,
    mrc.created_by,
    mrc.updated_by,
    mrc.reviewed_at,
    mrc.finalized_at,
    mrc.created_at,
    mrc.updated_at,
    rp.period_key,
    rp.period_start,
    rp.period_end,
    rp.status AS period_status,
    rp.title AS period_title,
    p.id AS project_id,
    p.name AS project_name,
    p.slug AS project_slug,
    c.id AS client_id,
    c.name AS client_name,
    c.slug AS client_slug,
    s.id AS primary_site_id,
    s.url AS primary_site_url,
    s.label AS primary_site_label
FROM monthly_report_contents mrc
INNER JOIN reporting_periods rp ON rp.id = mrc.reporting_period_id
INNER JOIN projects p ON p.id = rp.project_id
INNER JOIN clients c ON c.id = p.client_id
LEFT JOIN sites s ON s.project_id = p.id AND s.is_primary = 1
WHERE mrc.id = :id
LIMIT 1
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':id' => $monthlyReportId]);
        $row = $stmt->fetch();
        return is_array($row) ? $row : null;
    }

    /**
     * All blocks for monthly report ordered by sort_order ASC, id ASC.
     *
     * @return list<array<string, mixed>>
     */
    public function listBlocksByMonthlyReportId(int $monthlyReportId): array
    {
        if ($monthlyReportId <= 0) {
            return [];
        }

        $sql = <<<'SQL'
SELECT
    rb.id,
    rb.monthly_report_content_id,
    rb.block_key,
    rb.block_type,
    rb.sort_order,
    rb.status,
    rb.title,
    rb.summary,
    rb.body,
    rb.data_json,
    rb.source_metric_refs,
    rb.source_weekly_checkpoint_ids
FROM report_blocks rb
WHERE rb.monthly_report_content_id = :mrc_id
ORDER BY rb.sort_order ASC, rb.id ASC
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':mrc_id' => $monthlyReportId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }

    /**
     * @return list<array<string, mixed>>
     */
    public function listWeeklyCheckpointsForPeriod(int $periodId): array
    {
        if ($periodId <= 0) {
            return [];
        }

        $sql = <<<'SQL'
SELECT
    wc.id,
    wc.reporting_period_id,
    wc.week_index,
    wc.checkpoint_key,
    wc.status,
    wc.title
FROM weekly_checkpoints wc
WHERE wc.reporting_period_id = :period_id
ORDER BY wc.week_index ASC, wc.id ASC
SQL;
        $stmt = $this->pdo()->prepare($sql);
        $stmt->execute([':period_id' => $periodId]);
        $rows = $stmt->fetchAll();
        return is_array($rows) ? $rows : [];
    }
}
