#!/usr/bin/env node
/** Deterministic MIG corpus normalization — clean room v1 */
import { spawnSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const pipeline = path.join(__dirname, 'run-clean-room-semantic-pipeline-v1.mjs');
const r = spawnSync(process.execPath, [pipeline], { stdio: 'inherit' });
process.exit(r.status ?? 1);
