const TOOLS = {
  n8n_webhook: {
    id: "n8n_webhook",
    type: "webhook",
    enabled: true,
    risk_level: "low",
    required_permissions: [],
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

function checkPermissions(tool, context) {
  const permissions = context?.permissions || [];

  for (const required of tool.required_permissions) {
    if (!permissions.includes(required)) {
      throw new Error(
        `Missing permission "${required}" for tool ${tool.id}`
      );
    }
  }

  return true;
}

module.exports = {
  getTool,
  validateTool,
  checkPermissions,
};
