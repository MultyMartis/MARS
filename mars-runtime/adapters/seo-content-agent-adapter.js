const { getConfig } = require("../runtime/config");

function validateSeoAdapterConfig(config) {
  if (!config.seoContentAgentWebhookUrl) {
    throw new Error("Missing seoContentAgentWebhookUrl (SEO_CONTENT_AGENT_WEBHOOK_URL)");
  }
}

/** Map legacy/test payload.mode to contract action (see `projects/metabot-seo-content-agent/integration-contract-legacy.md`). */
function resolveAction(payload) {
  if (!payload || typeof payload !== "object") {
    return "outline";
  }
  if (typeof payload.action === "string" && payload.action.trim()) {
    return payload.action.trim().toLowerCase();
  }
  const mode = typeof payload.mode === "string" ? payload.mode.trim().toLowerCase() : "";
  if (mode === "brief" || mode === "outline") return "outline";
  if (["run", "text", "seoqa", "factcheck", "get"].includes(mode)) return mode;
  return "outline";
}

function buildWebhookBody({ task_id, payload, run_id }) {
  const p =
    payload && typeof payload === "object" ? { ...payload } : {};
  const action = resolveAction(p);
  delete p.action;
  delete p.mode;

  return {
    action,
    payload: p,
    meta: {
      run_id,
      task_id,
      source: "mars",
    },
    task_id,
    run_id,
  };
}

async function invokeTool({ task_id, payload, run_id }) {
  const config = getConfig();
  validateSeoAdapterConfig(config);

  const WEBHOOK_URL = config.seoContentAgentWebhookUrl;

  if (typeof fetch !== "function") {
    throw new Error("Global fetch is not available. Use Node.js 18+ for MARS R1 runtime.");
  }

  const response = await fetch(WEBHOOK_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(buildWebhookBody({ task_id, payload, run_id })),
  });

  if (!response.ok) {
    const bodyText = await response.text();
    throw new Error(
      `SEO content agent webhook failed: ${response.status} ${response.statusText}; body=${bodyText}`
    );
  }

  try {
    return await response.json();
  } catch (err) {
    throw new Error(
      `SEO content agent webhook returned non-JSON body: ${err.message}`
    );
  }
}

module.exports = {
  invokeTool,
};
