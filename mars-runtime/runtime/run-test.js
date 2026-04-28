const { runTask } = require("./execution-engine");

async function main() {
  const testTask = {
    task_id: "task_test_001",
    type: "test_task",
    payload: {
      message: "Hello from MARS R1",
    },
  };

  const result = await runTask(testTask);
  console.log("Run result:");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((error) => {
  console.error("run-test failed:", error);
  process.exitCode = 1;
});
