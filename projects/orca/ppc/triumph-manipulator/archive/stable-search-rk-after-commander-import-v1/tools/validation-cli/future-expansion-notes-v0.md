# Future expansion notes — Validation CLI v0.1+

**Scope:** Ideas only. Not implemented without explicit charter.

## Full rule parity

- Implement remaining ST / NG / SY / SE / LM / CM / SV / EX from [rule-registry-v1.md](../../validation/rule-registry-v1.md)  
- Align v0.1 simplified semantics with registry prose or version ruleset  

## Report diffing

- `node compare-fixture.js` — diff output vs golden, ignore timestamp option  
- Structured diff for `blocking_errors` only  

## Regression suite

- Multiple instance fixtures under `fixtures/`  
- Expected reports per fixture  
- Still human-triggered local runs  

## CI hooks (human-wired later)

- Exit code contract already defined (0 / 1)  
- Upload `validation-report.output.json` as artifact  
- **Not** auto-launch, **not** auto-export  

## Batch validation

- Directory glob; summary table for operator  
- No watcher, no daemon  

## Exporter handshake

- Exporter reads report path; stops if `export_allowed: false`  
- Separate module — no merged “ORCA runtime”  

## Explicit non-goals

- GitHub Actions / CI templates in-repo (unless separate charter)  
- Services, queues, workers, schedulers  
- `launch_allowed: true` from validator — **forbidden**  
- Direct API integration  

## Honesty

Preserve post–Cycle 8 operational-first posture: documentation-first, human authority, fail-closed survivability.
