const TOOLS = {
  n8n_webhook: {
    id: "n8n_webhook",
    type: "webhook",
    enabled: true,
  },
};

function getTool(tool_id) {
  return TOOLS[tool_id];
}

function validateTool(tool_id) {
  const tool = getTool(tool_id);

  if (!tool) {
    throw new Error(`Unknown tool_id: ${tool_id}`);
  }

  if (!tool.enabled) {
    throw new Error(`Tool disabled: ${tool_id}`);
  }

  return tool;
}

module.exports = {
  getTool,
  validateTool,
};
