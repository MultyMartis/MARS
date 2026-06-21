/**
 * Throttled SERP resume orchestrator — mig-20260622-corv01
 * Batch size 2; 90–120s inter-query delay; 5min batch cooldown; stop on CAPTCHA.
 */
import { spawnSync } from "child_process";
import { readFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION_ROOT = join(__dirname, "..");
const CAPTURE_SCRIPT = join(__dirname, "capture-serp-zpm-workflow.mjs");
const UPDATE_SCRIPT = join(__dirname, "update-registries-throttled-serp.mjs");

const COOLDOWN_MS = Number(process.env.BATCH_COOLDOWN_MS || "300000");
const BATCHES = [
  { label: "batch1", ids: ["r1q02", "r1q03"] },
  { label: "batch2", ids: ["r1q04", "r1q06"] },
  { label: "batch3", ids: ["r1q08", "r1q10"] },
  { label: "batch4", ids: ["r1q09"] },
  { label: "retry-batch", ids: ["r1q07"] },
];

const startFrom = process.argv[2] || BATCHES[0].label;
const onlyBatch = process.argv[3] === "only";

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function runCapture(batch) {
  const env = {
    ...process.env,
    CAPTURE_HEADLESS: "false",
    CAPTURE_DELAY_MS: "90000",
    CAPTURE_DELAY_JITTER_MS: "30000",
    STOP_ON_CAPTCHA: "1",
    SKIP_EXISTING_GRADE_B: "1",
    MERGE_SUMMARY: "1",
  };
  const args = [CAPTURE_SCRIPT, "batch", batch.label, ...batch.ids];
  console.log(`\n=== RUN ${batch.label}: ${batch.ids.join(", ")} ===\n`);
  const result = spawnSync(process.execPath, args, {
    cwd: __dirname,
    env,
    stdio: "inherit",
  });
  return result.status ?? 1;
}

function runUpdate(batchLabel) {
  const result = spawnSync(process.execPath, [UPDATE_SCRIPT, batchLabel], {
    cwd: __dirname,
    stdio: "inherit",
  });
  return result.status ?? 1;
}

function readSummary() {
  const path = join(
    SESSION_ROOT,
    "evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json"
  );
  if (!existsSync(path)) return { meta: {} };
  return JSON.parse(readFileSync(path, "utf8"));
}

async function main() {
  let started = startFrom === "all";
  for (let i = 0; i < BATCHES.length; i++) {
    const batch = BATCHES[i];
    if (!started) {
      if (batch.label === startFrom) started = true;
      else continue;
    }
    if (i > 0 && !onlyBatch) {
      console.log(`\n--- Cooldown ${COOLDOWN_MS / 1000}s before ${batch.label} ---\n`);
      await sleep(COOLDOWN_MS);
    }
    const code = runCapture(batch);
    runUpdate(batch.label);
    if (code !== 0) {
      console.error(`Capture exited ${code} on ${batch.label}`);
      process.exit(code);
    }
    const summary = readSummary();
    if (summary.meta?.stopped_on_captcha) {
      console.log(`\nSTOP: CAPTCHA after ${summary.meta.stopped_after} in ${batch.label}\n`);
      process.exit(0);
    }
    if (onlyBatch) break;
  }
  console.log("\nAll permitted batches complete.\n");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
