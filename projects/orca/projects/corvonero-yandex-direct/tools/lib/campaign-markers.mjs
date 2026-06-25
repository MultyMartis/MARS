/** Logical direction markers for unified campaign export and future split. */
export const DIRECTION_MARKERS = {
  'CORV-C01': '[C01]',
  'CORV-C02': '[C02]',
  'CORV-C03': '[C03]',
  'CORV-C04': '[C04]',
  'CORV-C05': '[C05]',
  'CORV-C06': '[C06]',
  'CORV-C07': '[C07]',
  'CORV-C08': '[C08]',
};

export const DIRECTION_LABELS = {
  'CORV-C01': 'общие услуги 1С',
  'CORV-C02': 'доработки',
  'CORV-C03': 'отчёты, формы, РМК',
  'CORV-C04': 'управленческие задачи',
  'CORV-C05': 'интеграции и обмены',
  'CORV-C06': 'маркировка и Честный знак',
  'CORV-C07': 'ошибки и восстановление',
  'CORV-C08': 'ТС ПИОТ',
};

export const UNIFIED_UTM_CAMPAIGN = 'corvonero_1c_search_nsk';
export const UNIFIED_CAMPAIGN_ID = 'CORV-UNIFIED-01';
export const UNIFIED_CAMPAIGN_NAME = 'Корво Неро — 1С услуги (Новосибирск)';

export function formatGroupExportName(campaignId, groupName) {
  const marker = DIRECTION_MARKERS[campaignId] || '[C??]';
  return `${marker} ${groupName}`;
}

export function markerFromCampaignId(campaignId) {
  return DIRECTION_MARKERS[campaignId] || null;
}
