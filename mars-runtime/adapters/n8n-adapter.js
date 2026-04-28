const WEBHOOK_URL = "http://localhost:5678/webhook/test";

async function invokeTool({ task_id, payload, run_id }) {
  if (typeof fetch !== "function") {
    throw new Error("Global fetch is not available. Use Node.js 18+ for MARS R1 runtime.");
  }

  const response = await fetch(WEBHOOK_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      task_id,
      payload,
      run_id,
    }),
  });

  if (!response.ok) {
    const bodyText = await response.text();
    throw new Error(
      `n8n webhook call failed: ${response.status} ${response.statusText}; body=${bodyText}`
    );
  }

  const contentType = response.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    return response.json();
  }

  return {
    raw_response: await response.text(),
  };
}

module.exports = {
  invokeTool,
};
