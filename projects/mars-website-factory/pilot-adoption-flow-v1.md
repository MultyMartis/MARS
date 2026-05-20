# Pilot production adoption flow v1 (Wave 6)

**Status:** **documented** — first real-world procedure for adopting Factory library into a client workspace.  
**Template:** [workspaces/_template-client-v1/](../../workspaces/_template-client-v1/) · **Charter:** [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md).

**Not:** automated provisioning, **not** runtime orchestration.

---

## 1. Choose pilot project

| Criterion | Prefer |
|-----------|--------|
| Scope | Single landing or ≤3 pages |
| Risk | Internal/staging before paid traffic |
| Handoff | `site_type_id` + block list from registry |
| Operator | One human owner for freeze REPORTs |

**Avoid as first pilot:** full ecommerce, multi-locale, heavy third-party widgets.

Record: project slug, workspace path, charter date.

---

## 2. Bootstrap from `_template-client-v1`

```powershell
# Copy template to new slug (operator renames folder)
Copy-Item -Recurse workspaces\_template-client-v1 workspaces\<client-slug>
cd workspaces\<client-slug>
npm install
npm run build
```

| Step | Action |
|------|--------|
| 1 | Rename workspace folder + `package.json` name field |
| 2 | Edit `_tokens.scss` brand colors only (L3 prep) |
| 3 | Copy `partials/layout/` from reference if template layout stale |
| 4 | Add `@@include` rows per handoff block list |
| 5 | First build REPORT |

---

## 3. Adopt foundations safely

Copy wholesale from reference:

- `src/scss/foundations/`  
- `src/js/core/` (lifecycle, modal, form)

**Do not** copy entire reference `index.html` block stack unless handoff requires — avoids unvalidated blocks.

Rules: [foundation-adoption-rules-v1.md](foundation-adoption-rules-v1.md).

---

## 4. Validate survivability

Before L2 freeze:

1. [section-replacement-contract-v1.md](section-replacement-contract-v1.md) — read §5  
2. Run swap on **one** adopted block (prefer `hero` or `faq`)  
3. Modal + form still work after swap  
4. [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md) checklist  

Record **SAFE UNKNOWN** for untested blocks.

---

## 5. First freeze

| Order | Level | Scope |
|-------|-------|-------|
| 1 | L1 | Each block after QA PASS |
| 2 | L3 | After token + core JS verified |
| 3 | L2 | When all handoff blocks integrated |

Doc: [freeze-discipline-v1.md](freeze-discipline-v1.md).

---

## 6. First extraction cycle (optional)

If pilot surfaces reusable pattern **not** in [curated-library-index-v1.md](curated-library-index-v1.md):

1. [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md)  
2. Neutralize in reference workspace  
3. Extraction REPORT in `operational-examples/`  
4. Update curated index + tier  

**Do not** extract during hotfix or mid-L2 freeze without unfreeze.

---

## 7. Record lessons learned

Minimum pilot closeout REPORT:

```markdown
# REPORT — <slug> pilot adoption
- Blocks adopted:
- Freeze levels reached:
- QA: operational-qa-entry-v1 — PASS | gaps
- Survivability: swap tested on:
- Extractions promoted:
- Friction (max 5 bullets):
- SAFE UNKNOWN:
- Recommend:
```

No git required; store as project markdown under `projects/<slug>/` or client docs folder per operator habit.

---

## Pilot block pick list (validated+ default)

| Priority | block_id | Why |
|----------|----------|-----|
| 1 | `hero` | battle-tested |
| 2 | `lead_form` or `contact_block` | conversion path |
| 3 | `faq` or `pricing` | real extract patterns |
| 4 | `cases` | social proof depth |

Defer `social_proof` until extracted or HITL accepts experimental tier.

---

*Wave 6 — pilot adoption flow.*
