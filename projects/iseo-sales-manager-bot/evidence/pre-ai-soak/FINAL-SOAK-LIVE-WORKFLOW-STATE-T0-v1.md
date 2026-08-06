# FINAL SOAK LIVE WORKFLOW STATE T0 v1

| Field | Value |
|---|---|
| Observed | 2026-08-06 ~19:43–19:52 Europe/Moscow |
| Canonical tip inspected | `0d29cc24` (= origin/mars/canonical-post-recovery) |
| Required ancestors present | `63385c13`, `610500fd`, `0d29cc24` |

## Workflow inventory (i-SEO Sales Manager)

| Name | ID | Active | Nodes | Notes |
|---|---|---:|---:|---|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | unchanged ID; schedule minutesInterval=2 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | unchanged ID |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | unchanged ID; inactive |

## Gmail roles

| Workflow | Gmail nodes | Intake? |
|---|---|---|
| Operational.dev | Fetch Leads; Add PROCESSED; Remove Incoming; Add ERROR | **Yes — sole intake (Fetch)** |
| Admin.dev | Gmail Health Probe only | **No** |

**Gmail intake workflows active:** 1  
**Workflows created during checkpoint:** 0  
**ID replacement:** none  

Other active n8n workflows on the instance belong to unrelated MARS/SEO agents and have **0** Gmail nodes — not i-SEO Sales Manager intakes.

## Activation

No unexpected deactivation of Ops/Admin. v2 remains inactive.
