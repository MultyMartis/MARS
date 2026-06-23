/**
 * Strategist model adapter — separate from ORCA semantic prompts
 */
import { loadLocalSecrets, getSafeConfigSummary } from '../../../../orca/semantic-intelligence/live-model/runtime/local-secret-loader.mjs';
import { buildStrategistSystemPrompt, buildStrategistUserPrompt, STRATEGIST_PROMPT_VERSION } from '../../strategist/prompts/strategist-prompt-v1.mjs';

const DEFAULT_TIMEOUT_MS = 60000;

export function createStrategistModelAdapter(options = {}) {
  if (options.mock) {
    return {
      provider: 'mock',
      modelId: 'mock-strategist',
      async strategize(pack, constraints) {
        return {
          ok: true,
          output: {
            strategic_summary: 'Mock strategist output for regression',
            tier_recommendations: pack.tier_distribution,
            blockers_preserved: pack.blockers,
            evidence_citations: pack.evidence_inventory?.map((e) => e.artifact_id) || [],
            prompt_version: STRATEGIST_PROMPT_VERSION,
          },
        };
      },
    };
  }

  loadLocalSecrets();
  const provider = process.env.ORCA_SEMANTIC_PROVIDER || (process.env.OPENROUTER_API_KEY ? 'openrouter' : 'openai');
  const apiKey = provider === 'openrouter' ? process.env.OPENROUTER_API_KEY : process.env.OPENAI_API_KEY;
  const modelId = process.env.ORCA_SEMANTIC_MODEL || 'openai/gpt-5-mini';
  const baseUrl = provider === 'openrouter' ? 'https://openrouter.ai/api/v1' : (process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1');

  return {
    provider,
    modelId,
    configSummary: getSafeConfigSummary(),
    async strategize(pack, constraints = {}) {
      if (!apiKey) {
        return { ok: false, blocker: 'BLOCKED — STRATEGIST MODEL UNAVAILABLE', errors: ['missing API key'] };
      }
      const systemPrompt = buildStrategistSystemPrompt();
      const userPrompt = buildStrategistUserPrompt(pack, constraints);
      const started = Date.now();

      try {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), options.timeoutMs || DEFAULT_TIMEOUT_MS);
        const response = await fetch(`${baseUrl}/chat/completions`, {
          method: 'POST',
          signal: controller.signal,
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${apiKey}`,
            ...(provider === 'openrouter' ? { 'HTTP-Referer': 'https://mars.local/sppc-strategist', 'X-Title': 'MARS PPC Strategist Wave 4' } : {}),
          },
          body: JSON.stringify({
            model: modelId,
            temperature: 0.2,
            response_format: { type: 'json_object' },
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: userPrompt },
            ],
          }),
        });
        clearTimeout(timer);

        if (!response.ok) {
          const errText = await response.text();
          return { ok: false, blocker: 'STRATEGIST_API_ERROR', errors: [sanitize(errText)] };
        }

        const data = await response.json();
        const content = data.choices?.[0]?.message?.content;
        let parsed;
        try {
          parsed = JSON.parse(content);
        } catch {
          return { ok: false, blocker: 'MALFORMED_STRATEGIST_OUTPUT', errors: ['JSON parse failed'] };
        }

        return {
          ok: true,
          output: {
            ...parsed,
            prompt_version: STRATEGIST_PROMPT_VERSION,
            model_metadata: {
              provider,
              model_id: modelId,
              latency_ms: Date.now() - started,
              usage: data.usage || null,
            },
          },
        };
      } catch (e) {
        return { ok: false, blocker: 'STRATEGIST_API_ERROR', errors: [e.message] };
      }
    },
  };
}

function sanitize(text) {
  return String(text || '').slice(0, 200).replace(/sk-[a-zA-Z0-9_-]+/g, '[REDACTED]');
}
