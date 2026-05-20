# MARS Website Factory — Source Confidence Model

**Status:** **documented** — confidence vocabulary for human-supervised source interpretation.  
**Not:** automated confidence scoring, source-understanding AI, validation engine, CV model, or universal certainty framework.

**Purpose:** make implementation confidence explicit before frontend work turns a source read into HTML, SCSS, responsive behavior, interaction, or freeze claims.

**Companion documents:** [source-interpretation-governance.md](source-interpretation-governance.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/source-interpretation-checklist.md`](../../agents/mars-forge/source-interpretation-checklist.md).

---

## 1. Confidence Levels

| Level | Meaning | Implementation posture |
|-------|---------|--------------------------|
| **Explicit** | Source directly states or visibly proves the decision: copy, order, CTA role, section purpose, asset, state, or responsive rule. | Implement normally; cite source path / charter when material. |
| **Strongly implied** | Source does not state it directly, but repeated pattern, pack rule, or adjacent authoritative evidence makes one read clearly dominant. | Implement with confidence label; report if the decision affects hierarchy, grouping, responsive behavior, or freeze. |
| **Weakly implied** | Source suggests a plausible read, but alternatives remain credible. | Do not present as fact; proceed only for low-risk details or with disclosed approximation. |
| **Ambiguous** | Multiple credible interpretations exist and source does not decide. | Use SAFE UNKNOWN or HITL when material; no full PASS based on hidden choice. |
| **Unknown** | Required source authority is missing or unreadable. | Stop, request source, or record SAFE UNKNOWN; approximation only when low-risk and disclosed. |
| **Contradictory** | Approved-looking sources conflict and priority rules do not resolve the conflict. | Stop material implementation; HITL or source priority decision required. |

---

## 2. Decision Rules

| Confidence level | SAFE UNKNOWN required? | HITL required? | Implementation should stop? | Approximation acceptable? |
|------------------|------------------------|----------------|-----------------------------|---------------------------|
| **Explicit** | No, unless source conflicts elsewhere. | No, unless requested by workflow. | No. | Usually unnecessary. |
| **Strongly implied** | No for low/medium-risk decisions; yes if report cannot state evidence. | Sometimes for structural, semantic, responsive, or interaction decisions. | Only if decision would change meaning, structure, or behavior materially. | Acceptable with confidence label. |
| **Weakly implied** | Yes when decision affects semantics, hierarchy, CTA, grouping, interaction, assets, or freeze. | Required for material structure, interaction, or responsive redesign. | Stop if implementation would invent source truth. | Acceptable only for low-risk visual approximation with disclosure. |
| **Ambiguous** | Yes. | Required when ambiguity affects user-facing meaning, structure, responsive behavior, interaction, or delivery readiness. | Stop when choice would become hard to unwind or would be reported as full fidelity. | Only if explicitly marked PARTIAL / approximation. |
| **Unknown** | Yes. | Required when source is needed to continue safely. | Stop for meaning, copy, CTA, interaction, structure, asset, and responsive intent gaps. | Only for non-material placeholder decisions, disclosed. |
| **Contradictory** | Yes. | Required unless current charter has clear priority. | Stop material implementation until contradiction is resolved. | Not acceptable for the contradictory field. |

---

## 3. When SAFE UNKNOWN Is Required

Use **SAFE UNKNOWN** when:

- Active source path, version, or authority is missing.
- Source is unreadable, cropped, low-resolution, or partially hidden in a way that affects implementation.
- Mobile, tablet, hover, focus, modal, form, slider, accordion, or animation states are absent but required.
- Approved-looking sources contradict one another.
- Grouping, hierarchy, CTA role, entity count, section purpose, or interaction logic cannot be proven.
- An implementation decision would require inventing semantics, assets, UX, responsive behavior, or structure.
- A screenshot detail may be raster artifact, compression noise, export artifact, or accidental alignment.

SAFE UNKNOWN must state:

```text
Unknown:
Affected decision:
Current confidence:
Why source is insufficient:
Resolver:
Disposition: stop | HITL | approximate with disclosure | defer
```

---

## 4. When HITL Escalation Is Required

HITL is required when interpretation uncertainty affects:

- Section meaning, page story, entity count, CTA meaning, offer logic, trust/proof claims, or legal/commercial detail.
- DOM grouping, section split/merge, wrapper structure, or source-authority-driven structural change.
- Mobile collapse pattern when no breakpoint source exists.
- Interaction logic, hidden states, animation, form validation, modal behavior, or sticky behavior.
- Asset substitution, icon semantics, brand assets, or custom illustration replacement.
- Contradictory source priorities.
- Freeze decision where PASS would imply fidelity that source cannot support.

---

## 5. When Implementation Should Stop

Stop implementation instead of guessing when:

- The active version or source path is not chartered.
- The source contradiction is material and unresolved.
- The next step would invent UX, structure, hierarchy, semantics, responsive behavior, or assets.
- Missing source prevents meaningful QA or freeze.
- Approximation would be indistinguishable from redesign.
- The report would need to pretend certainty to declare completion.

---

## 6. When Approximation Is Acceptable

Approximation may be acceptable only when all are true:

- The decision is not semantic, legal, commercial, interaction-critical, or structural.
- Approximation is reversible and local.
- The source is explicit or strongly implied for the surrounding intent.
- The report discloses the approximation and confidence level.
- The result does not claim pixel-perfect, full parity, or automated source understanding.

Examples:

- Minor spacing approximation when the implementation pack provides a spacing scale but screenshot resolution is weak.
- Decorative shadow/radius approximation when design system intent is clear but exact token is absent.
- Low-risk icon size tuning when icon semantic identity and family are source-authorized.

---

## 7. Reporting Format

Use this shape in Forge or Website Factory reports when source confidence matters:

```text
SOURCE CONFIDENCE — <section or block_id> — <source ref>

Explicit:
- <observed facts>

Strongly implied:
- <decisions + evidence>

Weakly implied / ambiguous:
- <risk + resolver>

Unknown / contradictory:
- <SAFE UNKNOWN or HITL item>

Implementation disposition:
- proceed | approximate with disclosure | PARTIAL | HITL required | stop
```

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial source confidence model: explicit, strongly implied, weakly implied, ambiguous, unknown, contradictory. |
