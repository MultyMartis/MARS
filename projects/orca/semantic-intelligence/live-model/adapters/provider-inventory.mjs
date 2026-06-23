/**
 * Provider inventory — inspect repository and environment for model integrations.
 * Does not expose credential values.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');

export function inspectProviderInventory() {
  const providers = [];

  const openaiKey = process.env.OPENAI_API_KEY;
  const openrouterKey = process.env.OPENROUTER_API_KEY;
  const anthropicKey = process.env.ANTHROPIC_API_KEY;

  providers.push({
    id: 'openai-compatible',
    name: 'OpenAI API',
    classification: openaiKey ? 'AVAILABLE AND CONFIGURED' : 'AVAILABLE — CREDENTIALS REQUIRED',
    adapter_path: 'live-model/adapters/openai-compatible-adapter.mjs',
    structured_output: true,
    credential_env: 'OPENAI_API_KEY',
    credential_present: !!openaiKey,
  });

  providers.push({
    id: 'openrouter',
    name: 'OpenRouter Gateway',
    classification: openrouterKey ? 'AVAILABLE AND CONFIGURED' : 'AVAILABLE — CREDENTIALS REQUIRED',
    adapter_path: 'live-model/adapters/openai-compatible-adapter.mjs',
    structured_output: true,
    credential_env: 'OPENROUTER_API_KEY',
    credential_present: !!openrouterKey,
    notes: 'Documented in MIG/SEO plans; not validated in production semantic path until Wave 3.1',
  });

  providers.push({
    id: 'anthropic',
    name: 'Anthropic API',
    classification: anthropicKey ? 'AVAILABLE — CREDENTIALS REQUIRED' : 'MISSING',
    adapter_path: null,
    structured_output: false,
    credential_env: 'ANTHROPIC_API_KEY',
    credential_present: !!anthropicKey,
    notes: 'No executable adapter in repository',
  });

  providers.push({
    id: 'ollama-local',
    name: 'Ollama Local Runtime',
    classification: 'LOCAL RUNTIME AVAILABLE',
    adapter_path: null,
    structured_output: 'SAFE UNKNOWN',
    credential_env: 'OLLAMA_HOST',
    notes: 'No adapter wired in Wave 3.1',
  });

  const n8nDocs = fs.existsSync(path.join(REPO_ROOT, 'projects/mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md'));
  providers.push({
    id: 'n8n-openrouter-nodes',
    name: 'n8n OpenRouter HTTP nodes',
    classification: 'ADAPTER EXISTS — NOT VALIDATED',
    notes: n8nDocs ? 'Documented in MIG runtime design; credentials in n8n env only' : 'SAFE UNKNOWN',
  });

  const marsModels = fs.existsSync(path.join(REPO_ROOT, 'models/README.md'));
  providers.push({
    id: 'mars-model-layer',
    name: 'MARS Model Layer (documented)',
    classification: marsModels ? 'ADAPTER EXISTS — NOT VALIDATED' : 'MISSING',
    adapter_path: 'models/README.md',
    notes: 'Architecture documentation only; no runtime router in repo',
  });

  const anyConfigured = providers.some((p) => p.classification === 'AVAILABLE AND CONFIGURED');
  return {
    generated_at: new Date().toISOString(),
    any_live_provider_configured: anyConfigured,
    recommended_primary: openaiKey ? 'openai-compatible' : openrouterKey ? 'openrouter' : null,
    providers,
    credential_boundary: 'Operator-supplied via environment; never committed to Git',
    cost_tracking: 'Token estimate per batch; hard cap in controls/cost-rate-controls.mjs',
    retry_logic: 'Exponential backoff; max 3 retries per phrase',
    logging_redaction: 'contracts/PRIVACY-LOGGING-BOUNDARY-v1.md',
  };
}
