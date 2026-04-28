const crypto = require("crypto");
const { executeTask } = require("./execution-bridge");
const { saveRunState } = require("../state/runtime-state-store");

const WORKFLOWS = {
  test_task: {
    tool_id: "n8n_webhook",
  },
};

function createRunId() {
  const randomPart = crypto.randomBytes(4).toString("hex");
  return `run_${Date.now()}_${randomPart}`;
}

async function runTask(task) {
  if (!task || !task.task_id || !task.type) {
    throw new Error("Invalid task: task_id and type are required.");
  }

  const workflow = WORKFLOWS[task.type];
  if (!workflow) {
    throw new Error(`No workflow found for task type: ${task.type}`);
  }

  const run_id = createRunId();
  const started_at = new Date().toISOString();
  console.log("[RUN START]", run_id, task.type);

  await saveRunState(run_id, {
    run_id,
    task_id: task.task_id,
    status: "started",
    timestamps: {
      started_at,
    },
    result: null,
  });

  const context = {
    workflow,
  };

  try {
    const bridgeOutput = await executeTask({ task, context, run_id });
    const finished_at = new Date().toISOString();

    await saveRunState(run_id, {
      run_id,
      task_id: task.task_id,
      status: bridgeOutput.status,
      timestamps: {
        started_at,
        finished_at,
      },
      result: bridgeOutput.result,
    });

    console.log("[RUN END]", run_id, bridgeOutput.status);
    return {
      run_id,
      status: bridgeOutput.status,
      result: bridgeOutput.result,
      signals: bridgeOutput.signals || [],
    };
  } catch (error) {
    const failed_at = new Date().toISOString();

    await saveRunState(run_id, {
      run_id,
      task_id: task.task_id,
      status: "failed",
      timestamps: {
        started_at,
        failed_at,
      },
      result: {
        error: error.message,
      },
    });

    console.log("[RUN ERROR]", run_id, error.message);
    return {
      run_id,
      status: "failed",
      result: {
        error: error.message,
      },
      signals: ["UNKNOWN"],
    };
  }
}

module.exports = {
  runTask,
};
