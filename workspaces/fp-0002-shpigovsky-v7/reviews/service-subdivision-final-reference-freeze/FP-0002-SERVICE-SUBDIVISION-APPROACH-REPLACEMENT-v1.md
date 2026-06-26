# FP-0002 SERVICE SUBDIVISION — APPROACH REPLACEMENT v1

- Old component: `service-subdivision-approach-v1`
- Old runtime count (pre-fix): 1 section + gallery classes
- Shared replacement: `home-clinic-landscape`
- Source partial: `src/partials/sections/home-clinic-landscape.html`
- Page include: `@@include('partials/sections/home-clinic-landscape.html', {"class": ""})`
- Position: after `service-subdivision-team-stats-v1`, before `home-specialists`
- Old partial physically deleted: **no** (`service-subdivision-approach-v1.html` retained)
- Home output changed: **no**
- New `section.home-clinic-landscape` count: **1**
- New `service-subdivision-approach-v1` count: **0**
- Status: `SUPERSEDED_NOT_IN_RUNTIME`
- Verdict: **PASS**
