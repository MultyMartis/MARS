/**
 * Phase 1B-D6F1A — import / offers report classification (JS twin of import_condition.py).
 * Factual only. Canonical offers family is offers0_*.xml (not bare offer.xml).
 */

export const REPORT_CLASS = Object.freeze({
  FULL_SUCCESS: 'FULL_SUCCESS',
  CATALOG_SUCCESS_OFFERS_INPUT_MISSING: 'CATALOG_SUCCESS_OFFERS_INPUT_MISSING',
  CATALOG_AND_OFFERS_SUCCESS: 'CATALOG_AND_OFFERS_SUCCESS',
  COMPLETED_WITH_WARNINGS: 'COMPLETED_WITH_WARNINGS',
  IMPORT_ERROR: 'IMPORT_ERROR',
  NO_FRESH_IMPORT: 'NO_FRESH_IMPORT',
  MONITOR_COULD_NOT_CONFIRM_COMPLETION: 'MONITOR_COULD_NOT_CONFIRM_COMPLETION',
  CONFLICT_OR_INCOMPLETE_FILE_SET: 'CONFLICT_OR_INCOMPLETE_FILE_SET',
  RECOVERY_CONDITION_RESOLVED: 'RECOVERY_CONDITION_RESOLVED',
});

export const OFFERS_STATE = Object.freeze({
  OFFERS_INPUT_PRESENT_AND_PROCESSED: 'OFFERS_INPUT_PRESENT_AND_PROCESSED',
  OFFERS_INPUT_ABSENT: 'OFFERS_INPUT_ABSENT',
  OFFERS_INPUT_PRESENT_NOT_PROCESSED: 'OFFERS_INPUT_PRESENT_NOT_PROCESSED',
  OFFERS_INPUT_STATE_AMBIGUOUS: 'OFFERS_INPUT_STATE_AMBIGUOUS',
});

function normNames(names) {
  return (names || []).map((n) => String(n || '').trim()).filter(Boolean);
}

export function offersFilesPresent(names) {
  return normNames(names).some((n) => {
    const lower = n.toLowerCase();
    return lower.startsWith('offers0_') && lower.endsWith('.xml');
  });
}

export function catalogFilesPresent(names) {
  return normNames(names).some((n) => {
    const lower = n.toLowerCase();
    return lower.startsWith('import0_') && lower.endsWith('.xml');
  });
}

export function classifyOffersState({
  offers_input_files = null,
  offers_phase_status = null,
  offers_processed_count = null,
} = {}) {
  const present = offersFilesPresent(offers_input_files);
  const status = String(offers_phase_status || '').trim().toUpperCase();
  const processed = offers_processed_count;
  if (
    present &&
    ((Number.isInteger(processed) && processed > 0) ||
      ['PASS', 'OK', 'SUCCESS', 'PROCESSED'].includes(status))
  ) {
    if (present && (processed == null || processed > 0)) {
      return OFFERS_STATE.OFFERS_INPUT_PRESENT_AND_PROCESSED;
    }
  }
  if (present && (processed === 0 || ['SKIP', 'EMPTY', 'NO_INPUT'].includes(status))) {
    return OFFERS_STATE.OFFERS_INPUT_PRESENT_NOT_PROCESSED;
  }
  if (!present) return OFFERS_STATE.OFFERS_INPUT_ABSENT;
  return OFFERS_STATE.OFFERS_INPUT_STATE_AMBIGUOUS;
}

export function classifyImportReport(input = {}) {
  const {
    fresh_import_confirmed = false,
    catalog_input_files = null,
    offers_input_files = null,
    catalog_phase_ok = null,
    offers_phase_ok = null,
    offers_processed_count = null,
    import_error = false,
    warnings_present = false,
    monitor_completion_confirmed = true,
    conflict_or_incomplete = false,
    recovery_resolved = false,
  } = input;

  let offers_state = classifyOffersState({
    offers_input_files,
    offers_phase_status: offers_phase_ok ? 'PASS' : null,
    offers_processed_count,
  });
  if (
    offers_phase_ok &&
    !offersFilesPresent(offers_input_files) &&
    (offers_processed_count == null || offers_processed_count === 0)
  ) {
    offers_state = OFFERS_STATE.OFFERS_INPUT_ABSENT;
  }

  if (!monitor_completion_confirmed) {
    return {
      report_class: REPORT_CLASS.MONITOR_COULD_NOT_CONFIRM_COMPLETION,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'MONITOR_COMPLETION_UNCONFIRMED',
      reason_codes: ['MONITOR_COMPLETION_EVIDENCE_MISSING'],
      action_code: 'REVIEW_MONITOR_COMPLETION',
      action_text:
        'Проверить завершение монитора и повторный запуск при необходимости',
    };
  }
  if (conflict_or_incomplete) {
    return {
      report_class: REPORT_CLASS.CONFLICT_OR_INCOMPLETE_FILE_SET,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT',
      reason_codes: ['IMPORT_SOURCE_SET_CONFLICT'],
      action_code: 'REVIEW_IMPORT_FILE_SET',
      action_text: 'Проверить комплект файлов обмена 1С (каталог, цены и остатки)',
    };
  }
  if (import_error) {
    return {
      report_class: REPORT_CLASS.IMPORT_ERROR,
      severity: 'ERROR',
      offers_state,
      summary_code: 'IMPORT_ERROR',
      reason_codes: ['IMPORT_PHASE_ERROR'],
      action_code: 'REVIEW_IMPORT_ERROR',
      action_text: 'Разбрать ошибку импорта 1С по фазе и журналу',
    };
  }
  if (!fresh_import_confirmed) {
    return {
      report_class: REPORT_CLASS.NO_FRESH_IMPORT,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'NO_FRESH_1C_IMPORT',
      reason_codes: ['NO_FRESH_IMPORT_IN_EXPECTED_WINDOW'],
      action_code: 'REVIEW_MISSING_IMPORT',
      action_text:
        'Подтвердить, почему не было свежего обмена с 1С в ожидаемом окне',
    };
  }

  const catalog_ok = Boolean(catalog_phase_ok) && catalogFilesPresent(catalog_input_files);
  const offers_ok = offers_state === OFFERS_STATE.OFFERS_INPUT_PRESENT_AND_PROCESSED;

  if (catalog_ok && offers_state === OFFERS_STATE.OFFERS_INPUT_ABSENT) {
    return {
      report_class: REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'OFFERS_INPUT_MISSING',
      reason_codes: [
        'CATALOG_IMPORT_COMPLETED',
        'OFFERS0_XML_ABSENT',
        'PRICES_STOCK_MAY_NOT_UPDATE',
      ],
      action_code: 'REVIEW_MISSING_OFFERS',
      action_text:
        'Каталог импортирован; файл offers0_*.xml не получен — цены и остатки могли не обновиться',
      factual_claims: [
        'catalog import completed',
        'offers0_*.xml was not received/found',
        'prices and stock may not have been updated',
        'this is not a full successful 1C exchange',
      ],
      forbidden_claims: [
        'products were disabled because offers were absent',
        'prices changed without offers evidence',
      ],
    };
  }

  if (catalog_ok && offers_ok && warnings_present) {
    return {
      report_class: REPORT_CLASS.COMPLETED_WITH_WARNINGS,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'IMPORT_COMPLETED_WITH_WARNINGS',
      reason_codes: ['IMPORT_WARNINGS_PRESENT'],
      action_code: 'REVIEW_IMPORT_WARNINGS',
      action_text: 'Импорт завершён с предупреждениями — проверить журнал',
    };
  }

  if (catalog_ok && offers_ok) {
    let report_class =
      offers_processed_count && offers_processed_count > 0
        ? REPORT_CLASS.CATALOG_AND_OFFERS_SUCCESS
        : REPORT_CLASS.FULL_SUCCESS;
    if (recovery_resolved) report_class = REPORT_CLASS.RECOVERY_CONDITION_RESOLVED;
    return {
      report_class,
      severity: 'OK',
      offers_state,
      summary_code:
        report_class === REPORT_CLASS.RECOVERY_CONDITION_RESOLVED
          ? 'CONDITION_RESOLVED'
          : 'FULL_IMPORT_SUCCESS',
      reason_codes: ['CATALOG_PROCESSED', 'OFFERS_PROCESSED'],
      action_code: 'NONE',
      action_text: 'Полный обмен 1С завершён без критических ошибок',
    };
  }

  if (catalog_ok && offers_state === OFFERS_STATE.OFFERS_INPUT_PRESENT_NOT_PROCESSED) {
    return {
      report_class: REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
      severity: 'ATTENTION',
      offers_state,
      summary_code: 'OFFERS_PRESENT_NOT_PROCESSED',
      reason_codes: ['OFFERS_INPUT_PRESENT_NOT_PROCESSED'],
      action_code: 'REVIEW_OFFERS_PROCESSING',
      action_text: 'Файл с ценами и остатками найден, но обработка не подтверждена',
    };
  }

  return {
    report_class: REPORT_CLASS.CONFLICT_OR_INCOMPLETE_FILE_SET,
    severity: 'ATTENTION',
    offers_state,
    summary_code: 'IMPORT_CONDITION_INCOMPLETE',
    reason_codes: ['IMPORT_CONDITION_UNCLASSIFIED_INCOMPLETE'],
    action_code: 'REVIEW_IMPORT_CONDITION',
    action_text: 'Проверить комплект и результаты фаз импорта 1С',
  };
}

/**
 * Parse a sanitized MARS 1C import report text extract.
 */
export function parseImportReportText(text) {
  const raw = String(text || '');
  const catalogMatch = raw.match(
    /Step 1[\s\S]*?status:\s*\n?\s*([A-Z]+)/i,
  );
  const offersMatch = raw.match(
    /Step 2[\s\S]*?status:\s*\n?\s*([A-Z]+)/i,
  );
  const catalogInputs = [];
  const offersInputs = [];
  const catBlock = raw.match(/Step 1[\s\S]*?input files:\s*\n([\s\S]*?)(?:duration:|errors:)/i);
  const offBlock = raw.match(/Step 2[\s\S]*?input files:\s*\n([\s\S]*?)(?:duration:|errors:)/i);
  if (catBlock) {
    for (const line of catBlock[1].split(/\r?\n/)) {
      const m = line.match(/^\s*-\s*(\S+\.xml)/i);
      if (m) catalogInputs.push(m[1]);
    }
  }
  if (offBlock) {
    for (const line of offBlock[1].split(/\r?\n/)) {
      const m = line.match(/^\s*-\s*(\S+\.xml)/i);
      if (m) offersInputs.push(m[1]);
      if (/none listed/i.test(line)) {
        /* keep empty */
      }
    }
  }
  const started = (raw.match(/Started:\s*\n?\s*([^\n]+)/i) || [])[1] || null;
  const finished = (raw.match(/Finished:\s*\n?\s*([^\n]+)/i) || [])[1] || null;
  const finalStatus = (raw.match(/Final status:\s*\n?\s*([A-Z]+)/i) || [])[1] || null;
  const catalog_phase_ok = String(catalogMatch?.[1] || '').toUpperCase() === 'PASS';
  const offers_phase_ok = String(offersMatch?.[1] || '').toUpperCase() === 'PASS';
  return {
    fresh_import_confirmed: Boolean(started && finished),
    catalog_input_files: catalogInputs,
    offers_input_files: offersInputs,
    catalog_phase_ok,
    offers_phase_ok,
    offers_processed_count: offersInputs.length,
    import_error: String(finalStatus || '').toUpperCase() === 'FAIL',
    started_at: started?.trim() || null,
    finished_at: finished?.trim() || null,
    final_status: finalStatus,
  };
}
