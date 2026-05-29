# Draft Export Rules v1

**Role:** How exporter handles `draft` vs `active` ads (and mixed states) without semantic decisions.  
**JSON field:** `ads[].status` — values `draft` | `active`.

---

## Principles

| Principle | Rule |
|-----------|------|
| Draft is visible | Draft ads are **not** silently dropped unless operator selects exclude mode |
| Draft is marked | Transport row uses template **draft** marker — not active |
| No auto-promotion | Exporter never changes `draft` → `active` |
| Validation first | Symbol/semantic rules already ran; exporter copies status |

---

## Export modes (operator / future CLI flag)

| Mode | `draft` ads | `active` ads |
|------|-------------|--------------|
| **active_only** (default for launch prep) | **Omit** from ad rows | Export |
| **include_drafts** | Export with draft marker | Export |
| **drafts_only** | Export | Omit |

Default for Triumph launch prep: **`active_only`** — aligns with EX-06 warn when zero active ads.

---

## Status → Commander transport

| `ads[].status` | Logical transport |
|----------------|-------------------|
| `active` | Template **active** literal (verify from xlsx) |
| `draft` | Template **draft** literal |

**SAFE UNKNOWN:** Exact Russian/English status strings in template — read from `triumph-manipulator-commander-template-v0.xlsx` examples, not guessed.

---

## Mixed states in one group

Allowed: some ads `active`, some `draft` in same group.

| Mode | Behavior |
|------|----------|
| `active_only` | Export only active ads; draft ads absent from sheet |
| `include_drafts` | All ads present; statuses differ per row |

Exporter does **not** warn about mixed state — `ValidationReport` / operator checklist handles it.

---

## Keywords and draft ads

Keywords export **independently** of ad draft state unless operator policy links them.

| Policy | Behavior |
|--------|----------|
| default | Export all `keyword_cluster.keywords[]` with `status: active` |
| conservative | If group has zero active ads, still export keywords but manifest notes `KEYWORDS_WITHOUT_ACTIVE_AD` |

Keyword pause/draft at keyword level — follow `keywords[].status` when present.

---

## Extensions on draft ads

| Mode | Fastlinks / callouts on draft ad |
|------|--------------------------------|
| `active_only` | Not exported (parent ad omitted) |
| `include_drafts` | Exported attached to draft ad row |

---

## Human workflow in Commander

1. Operator exports with `include_drafts` during creative iteration.  
2. Import → review draft rows in Commander UI.  
3. Activate in Commander **or** fix JSON and re-export.  
4. Launch path: re-validate → `active_only` export → import.

Exporter does **not** perform Commander-side activation.

---

## Manifest fields (future)

```yaml
export_mode: active_only | include_drafts | drafts_only
ads_exported: { active: N, draft: M, omitted_draft: K }
```

---

## Related

- [export-preconditions-v1.md](export-preconditions-v1.md)  
- [validation/rule-registry-v1.md](../validation/rule-registry-v1.md) EX-06
