import fs from 'node:fs';
import path from 'node:path';
import { loadJson, writeJson, sha256Text, nowIso } from './utils.mjs';

function readSourceRows(sourcePath) {
  const ext = path.extname(sourcePath).toLowerCase();
  const raw = fs.readFileSync(sourcePath, 'utf8');
  if (ext === '.json') {
    const data = JSON.parse(raw);
    if (Array.isArray(data)) return { rows: data, rejected: 0 };
    if (Array.isArray(data.rows)) return { rows: data.rows, rejected: 0 };
    return { rows: [], rejected: 1 };
  }
  const lines = raw.split(/\r?\n/).filter((l) => l.trim());
  const header = lines[0]?.toLowerCase() || '';
  const start = header.includes('phrase') || header.includes('keyword') ? 1 : 0;
  const rows = [];
  let rejected = 0;
  for (let i = start; i < lines.length; i += 1) {
    const cols = lines[i].split(/[,;\t]/);
    const phrase = (cols[0] || '').trim();
    if (!phrase) {
      rejected += 1;
      continue;
    }
    const freq = cols[1] ? Number(cols[1].replace(/\s/g, '')) : null;
    rows.push({ raw_phrase: phrase, frequency: Number.isFinite(freq) ? freq : null, source_row: i + 1 });
  }
  return { rows, rejected };
}

export function intakeCorpus({ sources, outputDir }) {
  const inventory = [];
  const allRows = [];
  const duplicateSourceRows = [];
  const unmatchedRows = [];
  let rejectedTechnical = 0;

  for (const src of sources) {
    if (!fs.existsSync(src.source_path)) {
      unmatchedRows.push({ source_id: src.source_id, reason: 'file not found' });
      continue;
    }
    const { rows, rejected } = readSourceRows(src.source_path);
    rejectedTechnical += rejected;
    inventory.push({
      source_id: src.source_id,
      source_path: src.source_path,
      extracted_row_count: rows.length,
      rejected_technical_rows: rejected,
      declared_raw_row_count: src.raw_row_count ?? null,
    });
    for (const row of rows) {
      allRows.push({
        ...row,
        source_id: src.source_id,
        provenance_key: `${src.source_id}:${row.source_row}:${row.raw_phrase}`,
      });
    }
  }

  const seen = new Map();
  const accepted = [];
  for (const row of allRows) {
    const key = row.provenance_key;
    if (seen.has(key)) {
      duplicateSourceRows.push(row);
      continue;
    }
    seen.set(key, true);
    accepted.push(row);
  }

  const sourceFileTotal = inventory.reduce((s, i) => s + i.extracted_row_count + i.rejected_technical_rows, 0);
  const reconciled = accepted.length + duplicateSourceRows.length + rejectedTechnical;
  const sourceReadableTotal = allRows.length + rejectedTechnical;

  const perSourceMismatch = inventory.some((i) => {
    if (i.declared_raw_row_count == null) return false;
    const actual = i.extracted_row_count + i.rejected_technical_rows;
    return i.declared_raw_row_count !== actual;
  });

  const report = {
    schema_version: '1.0.0',
    generated_at: nowIso(),
    source_file_inventory: inventory,
    extracted_row_count: allRows.length,
    rejected_technical_rows: rejectedTechnical,
    accepted_raw_rows: accepted.length,
    duplicate_source_rows: duplicateSourceRows.length,
    unmatched_rows: unmatchedRows,
    final_raw_corpus_count: accepted.length,
    checksum: sha256Text(JSON.stringify(accepted)),
    reconciled,
    source_readable_total: sourceReadableTotal,
    counts_reconcile: sourceReadableTotal === reconciled && !perSourceMismatch,
  };

  if (!report.counts_reconcile) {
    return {
      ok: false,
      blockers: ['BLOCKED — FULL PRODUCTION CORPUS SOURCE COUNTS DO NOT RECONCILE'],
      report,
    };
  }

  fs.mkdirSync(outputDir, { recursive: true });
  writeJson(path.join(outputDir, 'raw-corpus.json'), { rows: accepted });
  writeJson(path.join(outputDir, 'intake-report.json'), report);

  return { ok: true, report, corpus_path: path.join(outputDir, 'raw-corpus.json') };
}
