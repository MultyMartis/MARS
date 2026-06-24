# AG-WP-001 — Content Model and Editor Governance Contract v1

**Document type:** Content and editor contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Aligns with:** FW-S-01, FW-S-02, FW-S-05, [FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md](../standards/FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md)

---

## 1. Decision sequence

```text
content type
  → field model
  → ownership
  → editability
  → validation
  → rendering
  → migration
```

No field may skip ownership and sanitization definition.

---

## 2. Implementation classes (supported)

| Class | When to use |
|-------|-------------|
| WordPress core fields | Title, excerpt, featured image — prefer when sufficient |
| Post meta | Simple scoped data |
| Options/settings | Global site settings |
| CPT | Distinct content types |
| Taxonomies | Classification |
| ACF Free | Structured fields without repeaters (project-dependent) |
| ACF Pro | Repeaters, options pages, flexible content — **operator-approved only** |
| Custom blocks | Reusable editor components |
| Patterns | Curated layouts |
| Locked blocks | Protect layout shell |
| Content-only editing | Client edits text in fixed regions |
| Custom admin screens | Complex workflows — rare |

**ACF is a mode, not a universal requirement.**

---

## 3. Per-field requirements

Every field or editable region must document:

| Attribute | Required |
|-----------|----------|
| field owner | Yes |
| data type | Yes |
| required/optional | Yes |
| validation rules | Yes |
| default value | Yes |
| fallback rendering | Yes |
| sanitization | Yes |
| escaping on output | Yes |
| REST exposure | Yes (explicit allow/deny) |
| editor visibility | Yes |
| migration rule | Yes |

---

## 4. Curated editor principles

1. Client edits **content**, not system architecture
2. Critical layout cannot be accidentally destroyed
3. Reusable sections have explicit boundaries
4. Global settings remain global — not per-page duplicates
5. Field labels and help text are **operator-approved**
6. No giant unstructured WYSIWYG as substitute for architecture
7. No universal flexible-content page builder unless **explicitly approved**

---

## 5. Version control

Field definitions (ACF JSON or equivalent) must be **version-controlled** in project `WORDPRESS/` tree — not database-only.

---

## 6. AG-WP-001 behaviour

- Propose content model in **REVIEWABLE** state only
- Block implementation if editable regions from frontend handoff are unmapped
- Escalate BLOCKING UNKNOWN on legal/medical/compliance copy ownership

---

*Content model contract v1 — curated editor, not page builder default.*
