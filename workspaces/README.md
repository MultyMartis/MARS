# MARS — `workspaces/`

This directory holds **local frontend workspaces** and similar operator sandboxes. **Default policy:** ignore everything except explicitly allow-listed documentation placeholders (see repository `.gitignore`).

Do **not** treat this tree as authoritative production source unless a project explicitly approves commits into MARS.

## Registered workspace placeholders

| Project | Path |
|---------|------|
| Triumph Manipulator Landing (V1) | [`triumph-manipulator-landing/`](triumph-manipulator-landing/README.md) |
| Triumph Manipulator Landing V2 — active local frontend workspace | [`triumph-manipulator-landing-v2/`](triumph-manipulator-landing-v2/README.md) |
| Website Factory reference (Wave 3–6) | [`website-factory-reference-v1/`](website-factory-reference-v1/README.md) — **git-tracked** canonical `src/` |
| Website Factory client template (Wave 5) | [`_template-client-v1/`](_template-client-v1/README.md) — **git-tracked** minimal starter |

**Triumph:** V2 vs frozen V1, where to edit vs where mockups live — [`../projects/triumph-manipulator-landing/V2-CANONICAL-STATE.md`](../projects/triumph-manipulator-landing/V2-CANONICAL-STATE.md).

**Website Factory:** after clone, `npm install` + `npm run build` in each tracked workspace; see [mars-website-factory/onboarding-flow-v1.md](../projects/mars-website-factory/onboarding-flow-v1.md).
