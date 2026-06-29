import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const REPO_ROOT = path.resolve(__dirname, '../../../../..');
export const PROJECT_ROOT = path.resolve(__dirname, '../../..');
export const TOOL_ROOT = path.resolve(__dirname, '..');

export const STORAGE_EXPORT_ROOT = path.join('X:', 'AI MARS STORAGE', 'exports', 'corvonero');
export const STORAGE_BACKUP_ROOT = path.join('X:', 'AI MARS STORAGE', 'backups', 'corvonero');

/** Writes allowed for this tool implementation task */
export const APPROVED_WRITE_ROOT = PROJECT_ROOT;

export const REQUIRED_VOLUME_LABEL = 'AI WS';
export const REQUIRED_DRIVE = 'X:';

export const COMMANDER_TEMPLATE_PATH = path.join(
  REPO_ROOT,
  'projects',
  'orca',
  'ppc',
  'triumph-manipulator',
  'assets',
  'direct-commander-template',
  'triumph-manipulator-commander-template-v1.xlsx'
);

export const EXPECTED_TEMPLATE_SHA256 =
  '1112793a888ac2e0762317fa0bf728a116e36a143fc72fa0f5fe729c56c3f1fa';

export const COMMANDER_SHEET_TEXTS = 'Тексты';
export const COMMANDER_SHEET_REGIONS = 'Регионы';
export const COMMANDER_HEADER_ROW = 14;
export const COMMANDER_COLUMN_COUNT = 78;
export const REQUIRED_REGION_VALUE = 'Новосибирская область';

export const FORBIDDEN_REGION_VALUES = [
  'Новосибирск и Новосибирская область',
  'Все',
  '',
];

export const FORBIDDEN_ORGANIZATION_ID = '29500847237';
export const REQUIRED_ORGANIZATION_VALUE = '';

export const MAX_PHRASES_PER_GROUP = 200;
export const GROUP_LIMIT_STOP_CODE = 'STOP — CAMPAIGN ARCHITECTURE EXCEEDS COMMANDER GROUP LIMIT';
export const TEMPLATE_MISMATCH_STOP = 'STOP — COMMANDER TEMPLATE IDENTITY MISMATCH';
export const EXPLICIT_MODE_REQUIRED = 'STOP — EXPLICIT MODE REQUIRED';

export const ALLOWED_AUTHORITY_ROLES = [
  'phrase_allocation',
  'campaign_architecture',
  'primary_ads',
  'callouts',
  'campaign_negatives',
  'group_negatives',
  'cross_campaign_rules',
  'utm_map',
  'campaign_settings',
  'transport_config',
];

export const FORBIDDEN_AUTHORITY_ROLES = [
  'semantic_cache',
  'semantic_run',
  'lock',
  'checkpoint_resume',
  'raw_mig_corpus',
  'openrouter_output',
  'generated_commander_xlsx',
];

export const APPROVED_AD_STATES = ['OPERATOR_APPROVED', 'UNCHANGED_OPERATOR_APPROVED'];
export const REJECTED_AD_STATES = ['DERIVED_REQUIRES_OPERATOR_REVIEW', 'DRAFT', 'UNKNOWN'];

export const APPROVED_OPERATOR_APPROVAL_STATES = ['OPERATOR_APPROVED', 'APPROVED'];

export const ROW_TYPE_AD = 'AD';
export const ROW_TYPE_KEYWORD = 'KEYWORD';

export const CLI_MODES = ['validate', 'build-payload', 'generate', 'verify-output'];
export const TASK_ALLOWED_MODES = ['validate', 'build-payload'];

export const OUTPUT_POLICY_FAIL_IF_EXISTS = 'FAIL_IF_OUTPUT_EXISTS';

export const DEPRECATED_DRIVES = ['C:', 'D:', 'E:'];

export const FORBIDDEN_PATH_SEGMENTS = [
  'semantic_cache',
  'semantic-run',
  'checkpoint_resume',
  'openrouter',
  '.git',
];

export const SYNTHETIC_TEST_OUTPUT_DIR = path.join(PROJECT_ROOT, '.tools-test-output');

export const TRIUMPH_EXPORTER_CLI = path.join(
  REPO_ROOT,
  'projects',
  'orca',
  'ppc',
  'triumph-manipulator',
  'tools',
  'exporter-cli'
);

export const TRIUMPH_HEADER_MAP = path.join(TRIUMPH_EXPORTER_CLI, 'commander-header-map-v0.json');
