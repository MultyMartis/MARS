// Phase Google Sheets instance quota repair — defer skip terminal (Operational.dev)
// SYNC: implementation/patches/SheetsQuotaDeferSkip.google-sheets-429-repair.js

const j = $input.first().json;
return [{
  json: {
    ...j,
    intake_skipped_reason: 'sheets_quota_defer',
    stage: 'sheets_quota_defer',
    message: 'Deferred Google Sheets retry window active — zero quota reads this run.',
  },
}];
