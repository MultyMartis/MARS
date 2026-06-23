/**
 * OpenAI-compatible live semantic adapter (OpenAI / OpenRouter).
 */
import { PROMPT_VERSION, buildSystemPrompt, buildUserPrompt } from '../contracts/prompt-contract.mjs';
import { contextChecksum } from './model-adapter-interface.mjs';

const DEFAULT_MODEL = process.env.ORCA_SEMANTIC_MODEL || 'gpt-4o-mini';
const DEFAULT_TIMEOUT_MS = Number(process.env.ORCA_SEMANTIC_TIMEOUT_MS || 30000);

export function createOpenAICompatibleAdapter(options = {}) {
  const provider = options.provider || resolveProvider();
  const apiKey = options.apiKey || resolveApiKey(provider);
  const modelId = options.modelId || DEFAULT_MODEL;
  const baseUrl = options.baseUrl || resolveBaseUrl(provider);

  return {
    provider,
    modelId,
    async assess(context) {
      if (!apiKey) {
        return { ok: false, blocker: 'BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE', errors: ['missing API key'] };
      }

      const systemPrompt = buildSystemPrompt(context);
      const userPrompt = buildUserPrompt(context);
      const started = Date.now();

      try {
        const response = await fetchWithTimeout(`${baseUrl}/chat/completions`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${apiKey}`,
            ...(provider === 'openrouter' ? { 'HTTP-Referer': 'https://mars.local/orca', 'X-Title': 'ORCA Semantic Wave 3.1' } : {}),
          },
          body: JSON.stringify({
            model: modelId,
            temperature: 0.1,
            response_format: { type: 'json_object' },
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: userPrompt },
            ],
          }),
        }, options.timeoutMs || DEFAULT_TIMEOUT_MS);

        if (!response.ok) {
          const errText = await response.text();
          const sanitized = sanitizeProviderError(errText, response.status);
          return { ok: false, blocker: classifyHttpError(response.status), errors: [sanitized] };
        }

        const data = await response.json();
        const content = data.choices?.[0]?.message?.content;
        let parsed;
        try {
          parsed = JSON.parse(content);
        } catch {
          return { ok: false, blocker: 'MALFORMED_MODEL_OUTPUT', errors: ['JSON parse failed'], raw: content };
        }

        parsed.blind_assessment = true;
        parsed.model_metadata = {
          provider,
          model_id: modelId,
          prompt_version: PROMPT_VERSION,
          context_checksum: contextChecksum(context),
          latency_ms: Date.now() - started,
          usage: data.usage || null,
        };

        return {
          ok: true,
          output: parsed,
          raw: content,
          metadata: parsed.model_metadata,
        };
      } catch (e) {
        return { ok: false, blocker: 'MODEL_API_ERROR', errors: [e.message] };
      }
    },
  };
}

function resolveProvider() {
  if (process.env.ORCA_SEMANTIC_PROVIDER) return process.env.ORCA_SEMANTIC_PROVIDER;
  if (process.env.OPENROUTER_API_KEY) return 'openrouter';
  return 'openai';
}

function resolveApiKey(provider) {
  if (provider === 'openrouter') return process.env.OPENROUTER_API_KEY;
  return process.env.OPENAI_API_KEY;
}

function resolveBaseUrl(provider) {
  if (provider === 'openrouter') return 'https://openrouter.ai/api/v1';
  return process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1';
}

async function fetchWithTimeout(url, options, timeoutMs) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, { ...options, signal: controller.signal });
  } finally {
    clearTimeout(timer);
  }
}

function sanitizeProviderError(errText, status) {
  const truncated = String(errText || '').slice(0, 200);
  return `HTTP ${status}: ${truncated.replace(/sk-[a-zA-Z0-9_-]+/g, '[REDACTED]').replace(/Bearer\s+\S+/gi, 'Bearer [REDACTED]')}`;
}

function classifyHttpError(status) {
  if (status === 401 || status === 403) return 'AUTH_FAILED';
  if (status === 404) return 'MODEL_NOT_FOUND';
  if (status === 429) return 'RATE_LIMITED';
  return 'ENDPOINT_FAILED';
}

/** Test-only mock adapter for bypass audit and pipeline validation */
export function createMockLiveAdapter(responses = {}) {
  return {
    provider: 'mock-live-v1',
    modelId: 'mock-semantic-v1',
    async assess(context) {
      const key = context.phrase.normalized_query || context.phrase.raw_query;
      const template = responses[key] || responses.default || defaultMockResponse(context);
      return {
        ok: true,
        output: { ...template, blind_assessment: true, model_metadata: { provider: 'mock-live-v1', model_id: 'mock-semantic-v1', prompt_version: PROMPT_VERSION } },
        metadata: { provider: 'mock-live-v1' },
      };
    },
  };
}

function defaultMockResponse(context) {
  const q = (context.phrase.raw_query || '').toLowerCase();
  let decision = 'ABSTAIN';
  let primary = 'UNKNOWN';
  if (/ваканс|работа программист|резюме/.test(q)) {
    decision = 'REJECT'; primary = 'CAREER_INTENT';
  } else if (/курс|обучен|с нуля/.test(q)) {
    decision = 'REJECT'; primary = 'EDUCATION_INTENT';
  } else if (/как |самостоятельно|своими руками/.test(q)) {
    decision = 'REJECT'; primary = 'DIY_INTENT';
  } else if (/скачать|торрент|бесплатно/.test(q)) {
    decision = 'REJECT'; primary = 'DOWNLOAD_INTENT';
  } else if (/личный кабинет|войти|официальный сайт/.test(q)) {
    decision = 'REJECT'; primary = 'NAVIGATION_INTENT';
  } else if (/найти|заказать|стоимость|цена|внедрен|доработк|аутсорс|специалист/.test(q)) {
    decision = 'ACCEPT'; primary = 'PROVIDER_SEARCH';
  } else if (/купить|лицензи|программ/.test(q) && !/найти|заказать/.test(q)) {
    decision = 'ABSTAIN'; primary = 'PRODUCT_SOFTWARE_INTENT';
  }
  return {
    primary_intent: primary,
    secondary_intent: null,
    likely_next_action: primary,
    commercial_eligibility: { decision, confidence: decision === 'ABSTAIN' ? 0.45 : 0.82 },
    provider_hire_likelihood: decision === 'ACCEPT' ? 0.85 : 0.2,
    diy_likelihood: /как |самостоятельно/.test(q) ? 0.8 : 0.15,
    career_likelihood: /ваканс/.test(q) ? 0.9 : 0.05,
    education_likelihood: /курс/.test(q) ? 0.85 : 0.05,
    informational_likelihood: 0.2,
    navigation_likelihood: /кабинет|войти/.test(q) ? 0.9 : 0.05,
    product_only_likelihood: /купить|лицензи/.test(q) ? 0.7 : 0.1,
    protected_intent_class: decision === 'REJECT' ? `PROTECTED_${primary}` : null,
    commercial_evidence: decision === 'ACCEPT' ? ['explicit_service_request_signal'] : [],
    non_commercial_evidence: decision === 'REJECT' ? ['protected_intent_signal'] : [],
    ambiguity: decision === 'ABSTAIN' ? 'HIGH' : 'LOW',
    confidence: decision === 'ABSTAIN' ? 0.45 : 0.82,
    decision,
    rationale: `Mock assessment for pipeline validation: ${primary}`,
    alternative_interpretation: null,
    missing_context: [],
  };
}
