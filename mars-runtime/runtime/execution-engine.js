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

function validateTask(task) {
  if (!task) {
    throw new Error("Task is required");
  }

  if (!task.task_id) {
    throw new Error("task_id is required");
  }

  if (!task.type) {
    throw new Error("task type is required");
  }

  if (!task.payload || typeof task.payload !== "object") {
    throw new Error("payload must be an object");
  }

  return true;
}

async function runTask(task) {
  try {
    validateTask(task);
  } catch (error) {
    return {
      run_id: null,
      status: "failed",
      result: { error: error.message },
      signals: ["UNKNOWN"],
    };
  }

  if (!process.env.N8N_WEBHOOK_URL) {
    throw new Error("Missing N8N_WEBHOOK_URL");
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
    permissions: [], // minimal default
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
