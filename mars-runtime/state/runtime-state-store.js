const fs = require("fs/promises");
const path = require("path");

const RUNS_DIR = path.join(__dirname, "runs");

async function saveRunState(run_id, state) {
  if (!run_id) {
    throw new Error("run_id is required to save state.");
  }

  await fs.mkdir(RUNS_DIR, { recursive: true });

  const filePath = path.join(RUNS_DIR, `${run_id}.json`);
  let states = [];

  try {
    const existing = await fs.readFile(filePath, "utf-8");
    const parsed = JSON.parse(existing);
    states = Array.isArray(parsed) ? parsed : [parsed];
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error;
    }
  }

  states.push(state);
  const payload = JSON.stringify(states, null, 2);
  await fs.writeFile(filePath, payload, "utf-8");
}

module.exports = {
  saveRunState,
};
