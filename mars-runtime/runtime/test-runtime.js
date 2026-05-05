const { runTask } = require("./execution-engine");

function sanitize(result) {
  if (!result || typeof result !== "object") return result;

  const clean = {
    run_id: result.run_id,
    status: result.status,
    signals: result.signals,
  };

  if (result.result?.error) {
    clean.error = result.result.error;
  }

  if (result.status === "completed") {
    clean.result = "OK";
  }

  return clean;
}

function log(title, data) {
  console.log(`\n=== ${title} ===`);
  console.log(JSON.stringify(sanitize(data), null, 2));
}

async function testValidTask() {
  const task = {
    task_id: "test_valid",
    type: "test_task",
    payload: { msg: "ok" },
  };

  const res = await runTask(task);
  log("VALID TASK", res);
}

async function testInvalidTask() {
  const task = {
    type: "test_task",
  };

  const res = await runTask(task);
  log("INVALID TASK", res);
}

async function testUnknownWorkflow() {
  const task = {
    task_id: "test_unknown",
    type: "unknown_type",
    payload: {},
  };

  const res = await runTask(task);
  log("UNKNOWN WORKFLOW", res);
}

async function main() {
  if (!process.env.N8N_WEBHOOK_URL) {
    console.log("WARNING: N8N_WEBHOOK_URL not set — valid test may fail");
  }

  await testValidTask();
  await testInvalidTask();
  await testUnknownWorkflow();
}

main().catch((e) => {
  console.error("TEST SUITE FAILED:", e);
  process.exitCode = 1;
});
