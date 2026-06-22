import { RUNTIME_VERSION } from './lib.mjs';

export function buildConsumptionReport(loadResult, meta = {}) {
  const timestamp = new Date().toISOString();
  const entries = (loadResult.evidence || []).map((e) => ({
    contract_id: e.contract_id,
    canonical_path: e.canonical_path,
    expected_checksum: e.expected_checksum,
    actual_checksum: e.actual_checksum,
    declared_version: e.declared_version,
    actual_version: e.actual_version,
    consumer: e.consumer,
    load_status: e.load_status,
    usage_evidence: e.usage_evidence || null,
    blocking_result: e.blocking ? loadResult.message : null,
  }));

  return {
    report_id: 'orca-contract-consumption-report',
    report_version: 'v1',
    generated_at: timestamp,
    manifest_version: loadResult.manifest?.lock_version || loadResult.manifest?.bundle_version,
    bundle_version: loadResult.bundleVersion,
    runtime_version: RUNTIME_VERSION,
    command_invoked: meta.command || null,
    overall_blocked: !!loadResult.blocked,
    overall_message: loadResult.message || null,
    contracts: entries,
    summary: summarize(entries),
  };
}

function summarize(entries) {
  const counts = {};
  for (const e of entries) {
    counts[e.load_status] = (counts[e.load_status] || 0) + 1;
  }
  return counts;
}

export function consumptionReportMarkdown(report) {
  const lines = [
    '# ORCA Contract Consumption Report',
    '',
    `**Generated:** ${report.generated_at}`,
    `**Runtime:** ${report.runtime_version}`,
    `**Bundle:** ${report.bundle_version}`,
    `**Command:** ${report.command_invoked || 'n/a'}`,
    `**Blocked:** ${report.overall_blocked}`,
    '',
    '| Contract | Status | Consumer | Checksum OK |',
    '|----------|--------|----------|-------------|',
  ];
  for (const c of report.contracts) {
    const checksumOk = !c.expected_checksum || c.expected_checksum === c.actual_checksum ? 'yes' : 'no';
    lines.push(`| ${c.contract_id} | ${c.load_status} | ${c.consumer} | ${checksumOk} |`);
  }
  lines.push('');
  return lines.join('\n');
}
