async function checkNode() {
  const version = process.versions.node;
  const major = parseInt(version.split(".")[0], 10);

  if (major < 18) {
    throw new Error(`Node.js 18+ required, current: ${version}`);
  }

  return `Node OK (${version})`;
}

function checkEnv() {
  if (!process.env.N8N_WEBHOOK_URL) {
    throw new Error("N8N_WEBHOOK_URL is not set");
  }

  return "ENV OK";
}

async function checkWebhook() {
  const url = process.env.N8N_WEBHOOK_URL;

  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      task_id: "health_check",
      payload: { ping: true },
      run_id: "health_check",
    }),
  });

  if (!res.ok) {
    throw new Error(`Webhook failed: ${res.status}`);
  }

  return "WEBHOOK OK";
}

async function main() {
  const results = [];

  try {
    results.push(await checkNode());
    results.push(checkEnv());
    results.push(await checkWebhook());

    console.log("\n=== HEALTH CHECK ===");
    results.forEach((r) => console.log(r));

    console.log("\nSTATUS: OK");
  } catch (e) {
    console.log("\n=== HEALTH CHECK FAILED ===");
    console.error(e.message);

    console.log("\nSTATUS: FAIL");
    process.exitCode = 1;
  }
}

main();
