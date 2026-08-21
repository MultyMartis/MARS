/**
 * Collapse multi-row ACCESS success into one item before REMINDER_DELIVERIES read.
 * Prevents Sheets read fan-out / empty paired artifacts under retry storms.
 */
const rows = $input.all().map((i) => i.json).filter((r) => r && typeof r === 'object');
const err = rows.some((r) => r.error || r.errorMessage || r.errorDescription);
if (err) {
  return [{ json: { error: true, errorMessage: 'ACCESS_CONTROL read error', stage: 'ACCESS_CONTROL' } }];
}
return [{ json: { access_collapsed: true, access_row_count: rows.length, access_ok: true } }];
