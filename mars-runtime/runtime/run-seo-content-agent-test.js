const { runTask } = require("./execution-engine");

async function main() {
  const task = {
    task_id: "seo_content_agent_test_001",
    type: "seo_content_agent_task",
    payload: {
      action: "outline",
      topic: "SEO-аудит сайта",
      language: "ru",
    },
  };

  const res = await runTask(task);
  console.log("\n=== SEO CONTENT AGENT TASK ===");
  console.log(JSON.stringify(res, null, 2));
}

main().catch((e) => {
  console.error("SEO CONTENT AGENT TEST FAILED:", e);
  process.exitCode = 1;
});
