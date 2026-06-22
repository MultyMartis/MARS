import { localTimestampParts } from './utils.mjs';

function parseTime(t) {
  const [h, m] = String(t).split(':').map(Number);
  return h * 60 + (m || 0);
}

function inWindow(localMinutes, window) {
  const start = parseTime(window.start);
  const end = parseTime(window.end);
  if (start <= end) return localMinutes >= start && localMinutes <= end;
  return localMinutes >= start || localMinutes <= end;
}

export function validateBusinessHoursWindow({
  projectTimezone,
  currentTimestamp,
  observationWindows,
  weekdayPolicy,
  approvedExceptions = [],
}) {
  if (!projectTimezone) {
    return { status: 'TIMEZONE UNRESOLVED', allowed: false, blocker: 'BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED' };
  }
  if (!observationWindows?.length) {
    return { status: 'WINDOW NOT CONFIGURED', allowed: false, blocker: 'BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED' };
  }

  const date = currentTimestamp ? new Date(currentTimestamp) : new Date();
  const local = localTimestampParts(date, projectTimezone);
  const localMinutes = parseTime(local.local_time);

  for (const ex of approvedExceptions) {
    if (ex.date === local.local_date && ex.approved === true) {
      return { status: 'APPROVED EXCEPTION', allowed: true, local };
    }
  }

  if (weekdayPolicy?.allowed_weekdays?.length) {
    const day = local.weekday?.toLowerCase();
    const allowed = weekdayPolicy.allowed_weekdays.map((d) => d.toLowerCase());
    if (!allowed.includes(day)) {
      return {
        status: 'OUTSIDE APPROVED WINDOW',
        allowed: false,
        blocker: 'BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED',
        local,
      };
    }
  }

  const matched = observationWindows.some((w) => inWindow(localMinutes, w));
  if (!matched) {
    return {
      status: 'OUTSIDE APPROVED WINDOW',
      allowed: false,
      blocker: 'BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED',
      local,
    };
  }

  return { status: 'WITHIN APPROVED BUSINESS-HOURS WINDOW', allowed: true, local };
}
