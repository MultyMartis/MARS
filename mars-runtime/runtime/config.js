function getConfig() {
  return {
    webhookUrl: process.env.N8N_WEBHOOK_URL,
    seoContentAgentWebhookUrl: process.env.SEO_CONTENT_AGENT_WEBHOOK_URL,
  };
}

function validateConfig(config) {
  if (!config.webhookUrl) {
    throw new Error("Missing webhookUrl in config");
  }
}

module.exports = {
  getConfig,
  validateConfig,
};
