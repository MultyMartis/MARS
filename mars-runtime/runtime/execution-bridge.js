const { invokeTool } = require("../adapters/n8n-adapter");

async function executeTask({ task, context, run_id }) {
  if (!task || !context || !run_id) {
    throw new Error("executeTask requires task, context, and run_id.");
  }

  const tool_id = context.workflow.tool_id;
  if (!tool_id) {
    throw new Error("Workflow does not define tool_id.");
  }

  if (tool_id !== "n8n_webhook") {
    throw new Error(`Unsupported tool_id: ${tool_id}`);
  }

  const toolResponse = await invokeTool({
    task_id: task.task_id,
    payload: task.payload,
    run_id,
  });

  return {
    status: "completed",
    result: toolResponse,
    signals: [],
  };
}

module.exports = {
  executeTask,
};
