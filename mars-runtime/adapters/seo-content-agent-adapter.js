const { getConfig } = require("../runtime/config");

function validateSeoAdapterConfig(config) {
  if (!config.seoContentAgentWebhookUrl) {
    throw new Error("Missing seoContentAgentWebhookUrl (SEO_CONTENT_AGENT_WEBHOOK_URL)");
  }
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
    body: JSON.stringify({
      task_id,
      payload,
      run_id,
    }),
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
