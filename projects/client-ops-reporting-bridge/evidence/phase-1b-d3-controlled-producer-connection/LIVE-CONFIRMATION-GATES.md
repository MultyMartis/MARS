# LIVE-CONFIRMATION-GATES

Exact phrases required (no other phrase enables live HTTP):

1. `ENABLE CLIENT OPS CONTROLLED PRODUCER HTTP D3 BZPM`
2. `ACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM`
3. `SEND ONE CLIENT OPS PRODUCER FIRST SEEN D3 BZPM`
4. `SEND ONE CLIENT OPS PRODUCER EXACT REPLAY D3 BZPM` (optional replay only)
5. `DEACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM`
6. `EMERGENCY DEACTIVATE CLIENT OPS PRODUCER D3 BZPM`

Also required: `--apply`, `environment` in `{sandbox, sandbox_controlled}`, concurrency=1, max_retries=0, ignored profile+secret present, D3 producer marker, workflow inactive before activation.
