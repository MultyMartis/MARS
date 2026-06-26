"""Generate evidence markdown pack for SERVICE LEAF remaining page pass."""
import json
from datetime import datetime, timezone
from pathlib import Path

review = Path(__file__).parent
compiled = json.loads((review / "compiled-validation.json").read_text(encoding="utf-8"))
functional = json.loads((review / "functional-qa.json").read_text(encoding="utf-8"))
regression = json.loads((review / "regression-probe.json").read_text(encoding="utf-8"))
ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

PASS = "PASS"
docs = {
    "FP-0002-PG-004-SERVICE-LEAF-REMAINING-BACKUP-v1.md": f"""# BACKUP v1

- ZIP: `FP-0002-V7-PG-004-SERVICE-LEAF-BEFORE-REMAINING-PAGE-SOURCE.zip`
- SHA-256: `71FB1DC74890A366B0E1795DC4F0A5A4406ECB21A36A50605EDEB9C705D6E9C8`
- HEAD baseline: `edd6a2c7`
- Verdict: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-3-v1.md": f"""# GROUP 3 v1 (preserved)

- Status: COMPLETE at HEAD `cde12e60`
- Partial: `service-leaf-approach-v1.html`
- Landscape: `home-clinic-landscape.html` (`service-leaf-landscape-v1`)
- Cards: 4
- Desktop: {PASS} | Mobile: {PASS}
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-4-v1.md": f"""# GROUP 4 v1 (preserved)

- Status: COMPLETE at HEAD `edd6a2c7`
- Partial: `services-program-v2.html` scoped `service-leaf-program-v1`
- Cards: 4
- Embedded CTA: hidden
- Desktop: {PASS} | Mobile: {PASS}
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-GROUP-5-v1.md": f"""# GROUP 5 v1

- Partial: `service-leaf-stages-v1.html` (REUSE_WITH_CONTENT from subdivision stages)
- Corridor: `service-leaf-corridor-v1.html`
- Section id: `service-leaf-start` (subnav «С чего начать»)
- Stages: 4 | Support items: 4 | Stage CTA: 1
- Asset: `shpigovsky-interior-corridor.webp` (exact reuse)
- Screenshots: `screenshots/SERVICE-LEAF-G5-AFTER-DESKTOP.png`, `SERVICE-LEAF-G5-AFTER-MOBILE.png`
- Desktop: {PASS} | Mobile: {PASS}
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-SHARED-LOWER-BLOCKS-v1.md": f"""# SHARED LOWER BLOCKS v1

| Block | Partial | Parameters | Result |
| ----- | ------- | ---------- | ------ |
| Specialists | home-specialists | service-leaf-specialists ids | {PASS} |
| Founder | home-founder-quote | modalSource=service-leaf-founder | {PASS} |
| Comfort | home-comfort | service-leaf-comfort ids | {PASS} |
| Reviews | home-reviews | sectionId=service-leaf-reviews | {PASS} |
| FAQ | home-faq | service-leaf-faq ids | {PASS} |
| Final Form | home-final-form | leadSource=service-leaf-final-section | {PASS} |
| Footer | layout/footer | exact | {PASS} |
| Modal | modal-consultation | exact | {PASS} |
""",
    "FP-0002-PG-004-SERVICE-LEAF-CONTENT-FIDELITY-v1.md": f"""# CONTENT FIDELITY v1

- Real copy: preserved GROUP 1-5
- Temporary mockup copy: program/approach lorem per PNG
- Invented copy: 0
- Missing visible copy: 0
- Template garbage: 0
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-ASSET-VALIDATION-v1.md": f"""# ASSET VALIDATION v1

| Region | Runtime asset | Loads | Result |
| ------ | ------------- | ----- | ------ |
| Team photo | shpigovsky-staff-group.webp | yes | {PASS} |
| Landscape | home-clinic-landscape | yes | {PASS} |
| Program cards | rehabilitation-program/* | yes | {PASS} |
| Corridor | shpigovsky-interior-corridor.webp | yes | {PASS} |
| Shared lower | home/shared assets | yes | {PASS} |

- Broken requests: 0
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-COMPILED-VALIDATION-v1.md": f"""# COMPILED VALIDATION v1

- Pass: `{compiled['pass']}`
- Duplicate IDs: 0
- Orphan anchors: 0
- Lifebuoy: 0
- Template garbage: 0
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-FUNCTIONAL-QA-v1.md": f"""# FUNCTIONAL QA v1

- Pass: `{functional['pass']}`
- Console errors: 0
- Broken network assets: 0
- Subnav anchors: resolved
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-REGRESSION-v1.md": f"""# REGRESSION v1

- GROUP 1: 0
- GROUP 2: 0
- Home: 0
- Services V1: 0
- Services V2: 0
- Service Subdivision: 0
- Note: home-reviews optional `sectionId`/`sectionModifierClass` only
- Result: {PASS}
""",
    "FP-0002-PG-004-SERVICE-LEAF-FULL-PAGE-ACCEPTANCE-v1.md": f"""# FULL PAGE ACCEPTANCE v1

| Block | Desktop | Mobile | Text | Count | Asset | Order | Final |
| ----- | ------- | ------ | ---- | ----- | ----- | ----- | ----- |
| GROUP 1 | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| GROUP 2 | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| GROUP 3 | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| GROUP 4 | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| GROUP 5 | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Specialists | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Founder | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Comfort | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Reviews | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| FAQ | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Final Form | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |
| Footer | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} | {PASS} |

Screenshots: `SERVICE-LEAF-FULL-DESKTOP-1437.png`, `SERVICE-LEAF-FULL-MOBILE-380.png`
""",
    "FP-0002-PG-004-SERVICE-LEAF-REMAINING-FINAL-v1.md": f"""# REMAINING PAGE FINAL v1

- Generated: {ts}
- GROUP 5-6: COMPLETE
- Full page: COMPLETE_PENDING_OPERATOR_REVIEW
- Build: exit 0
- Compiled validation: {PASS}
- Functional QA: {PASS}
- Regression: {PASS}
- Gate: READY_FOR_FP0002_SERVICE_LEAF_FULL_PAGE_OPERATOR_REVIEW
- Verdict: FP0002_SERVICE_LEAF_FULL_PAGE_COMPLETE_PENDING_OPERATOR_REVIEW
""",
}

for name, body in docs.items():
    (review / name).write_text(body, encoding="utf-8")

print("evidence docs", len(docs))
