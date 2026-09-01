// Phase Google Sheets 429 repair — CONFIG Route Prep (Operational.dev)
// SYNC: implementation/patches/ConfigRoutePrep.google-sheets-429-repair.js
// Single-output Code: sets __config_cache_fresh for IF routing (no multi-output return).

const TTL_MS = 5 * 60 * 1000;
const sd = $getWorkflowStaticData('global');
const now = Date.now();
const cache = sd.configSheetRows;
const fetchedAt = Number(sd.configSheetFetchedAt || 0);
const fresh =
  Array.isArray(cache) &&
  cache.length > 0 &&
  Number.isFinite(fetchedAt) &&
  now - fetchedAt < TTL_MS;

const lead = $input.first().json;
return [{ json: { ...lead, __config_cache_fresh: fresh } }];
