/* R1 experimental adapter dispatch only — not the full v0 Execution Bridge contract and not an orchestration runtime. */
const { invokeTool: invokeN8nWebhook } = require("../adapters/n8n-adapter");
const {
  invokeTool: invokeSeoContentAgent,
} = require("../adapters/seo-content-agent-adapter");
const { validateTool, checkPermissions } = require("./tool-registry");

async function executeTask({ task, context, run_id }) {
  if (!task || !context || !run_id) {
    throw new Error("executeTask requires task, context, and run_id.");
  }

  const tool_id = context.workflow.tool_id;
  if (!tool_id) {
    throw new Error("Workflow does not define tool_id.");
  }

  const tool = validateTool(tool_id);
  checkPermissions(tool, context);

  let toolResponse;
  if (tool_id === "n8n_webhook") {
    toolResponse = await invokeN8nWebhook({
      task_id: task.task_id,
      payload: task.payload,
      run_id,
    });
  } else if (tool_id === "seo_content_agent") {
    toolResponse = await invokeSeoContentAgent({
      task_id: task.task_id,
      payload: task.payload,
      run_id,
    });
  } else {
    throw new Error(`No adapter registered for tool_id: ${tool_id}`);
  }

  return {
    status: "completed",
    result: toolResponse,
    signals: [],
  };
}

module.exports = {
  executeTask,
};
