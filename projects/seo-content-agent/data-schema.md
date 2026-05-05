# SEO Content Agent — Data schema

**Status:** **documentation** — intended JSON shapes. **SAFE UNKNOWN:** strict validation tooling (JSON Schema file, AJV, etc.) until implementation.

All examples are **illustrative**; no real client data.

---

## Conventions

- **ISO-8601** dates in UTC preferred: `2026-05-04T12:00:00Z`.
- **Enumerations** may expand; treat unknown values as **validation errors** at runtime (**planned**).
- Use the string `SAFE_UNKNOWN` where a scalar is required but undetermined (MARS alignment).

### System signals vs JSON fields (convention)

- **System signal** (workflow branches, logs, UI labels): `MISSING_DATA` and similar — **SCREAMING_SNAKE_CASE**.
- **JSON field** on artefacts (`task`, `outline`, etc.): `missing_data` — **snake_case** array of human-readable gap strings.

Other signals may follow the same pattern when added (**SAFE UNKNOWN:** full enum at runtime).

---

## MVP-1 schema compatibility

**Plan:** [runtime-mvp-outline.md](runtime-mvp-outline.md) describes a **minimal** normalized task shape for the first n8n MVP. That shape uses a single keyword list:

```json
{
  "keywords": []
}
```

**Later (plan):** Full `task` documents in this file use split lists:

```json
{
  "primary_keywords": [],
  "secondary_keywords": []
}
```

**Mapping (plan):** Until an explicit primary/secondary split is captured (from user or model), map **`keywords[]` → `primary_keywords[]`** by default; `secondary_keywords` remains `[]` or **SAFE UNKNOWN** unless the brief distinguishes tiers. **Do not** invent a split from URLs or external SERP data in MVP-1.

---

## `task`

Normalized unit of work from Telegram.

```json
{
  "task_id": "string (uuid or stable id)",
  "created_at": "ISO-8601 datetime",
  "locale": "ru-RU",
  "command": "outline | text | factcheck | seoqa | freshness",
  "brief_raw": "string — original user text",
  "page_type": "landing | blog | category | comparison | SAFE_UNKNOWN",
  "primary_keywords": ["string"],
  "secondary_keywords": ["string"],
  "audience": "string | SAFE_UNKNOWN",
  "brand_voice": "string | SAFE_UNKNOWN",
  "constraints": ["string"],
  "cta_goal": "string | SAFE_UNKNOWN",
  "source_refs": [
    {
      "kind": "url | paste | file_id",
      "ref": "string",
      "label": "string | null"
    }
  ],
  "company_facts_ref": "string | null — pointer to corpus version, not the secret",
  "telegram": {
    "chat_id": "string | SAFE_UNKNOWN",
    "user_id": "string | SAFE_UNKNOWN"
  },
  "assumptions": [
    {
      "text": "string",
      "needs_confirmation": true
    }
  ],
  "missing_data": ["string"]
}
```

---

## `source`

Raw capture of user-provided material.

```json
{
  "source_id": "string",
  "task_id": "string",
  "kind": "url | paste | upload",
  "uri_or_excerpt": "string",
  "fetched_at": "ISO-8601 datetime | null",
  "content_sha256": "string | null",
  "language_detected": "string | SAFE_UNKNOWN"
}
```

---

## `source_analysis`

Structured extraction from one source.

```json
{
  "source_id": "string",
  "task_id": "string",
  "summary": "string",
  "entities": ["string"],
  "facts": [
    {
      "statement": "string",
      "confidence": "high | medium | low",
      "span_hint": "string | null — quote fragment or location hint"
    }
  ],
  "limitations": ["string — e.g. paywall, partial text"],
  "notes": "string"
}
```

---

## `outline`

SEO outline / copywriter brief.

```json
{
  "outline_id": "string",
  "task_id": "string",
  "status": "draft | approved | rejected | SAFE_UNKNOWN",
  "approved_at": "ISO-8601 datetime | null",
  "approved_by": "string | null — internal user id",
  "title_options": ["string"],
  "h1": "string",
  "meta_description_plan": "string — intent, not final copy if policy differs",
  "sections": [
    {
      "level": 2,
      "heading": "string",
      "intent": "string",
      "key_points": ["string"],
      "target_keywords": ["string"],
      "content_notes": ["string — e.g. REQUIRES_DATA: ..."]
    }
  ],
  "faq": [
    {
      "question": "string",
      "answer_brief": "string — notes only; not final copy unless policy says otherwise"
    }
  ],
  "cta": {
    "placement": "string",
    "copy_direction": "string"
  },
  "missing_data": ["string"],
  "internal_risks": ["string — e.g. legal, competitive sensitivity"]
}
```

**Note:** Nested `level` accepts `2` or `3` for H2/H3 under the single H1 (**validation rules TBD**).

---

## `generated_text`

Draft article output.

```json
{
  "text_id": "string",
  "task_id": "string",
  "outline_id": "string",
  "version": 1,
  "locale": "ru-RU",
  "title": "string",
  "meta_description": "string",
  "slug_suggestion": "string | SAFE_UNKNOWN",
  "body_markdown": "string",
  "faq_markdown": "string | null",
  "word_count": 0,
  "writer_notes": ["string — e.g. omitted claims due to missing data"],
  "evidence_bundle_ref": "string | null — pointer to hashes/ids used"
}
```

---

## `factcheck_report`

```json
{
  "report_id": "string",
  "task_id": "string",
  "text_id": "string",
  "created_at": "ISO-8601 datetime",
  "overall_risk": "low | medium | high",
  "claims": [
    {
      "claim_id": "string",
      "quote": "string — excerpt from draft",
      "status": "supported | unsupported | needs_source | contradicts_source",
      "evidence": [
        {
          "source_id": "string | null",
          "note": "string"
        }
      ],
      "recommendation": "string | SAFE_UNKNOWN"
    }
  ],
  "coverage_gaps": ["string"],
  "methodology_notes": "string | null"
}
```

---

## `seoqa_report`

```json
{
  "report_id": "string",
  "task_id": "string",
  "text_id": "string",
  "created_at": "ISO-8601 datetime",
  "verdict": "pass | pass_with_warnings | fail",
  "heading_structure_ok": true,
  "h1_h3_issues": ["string"],
  "intent_coverage": {
    "commercial_intent_addressed": true,
    "notes": "string"
  },
  "faq_relevance": {
    "score": "good | mixed | poor",
    "notes": "string"
  },
  "keyword_spam_risk": "low | medium | high",
  "water_detected": true,
  "issues": [
    {
      "issue_id": "string",
      "severity": "info | warn | fail",
      "category": "structure | intent | spam | tone | other",
      "detail": "string",
      "suggested_fix": "string | SAFE_UNKNOWN"
    }
  ],
  "summary": "string"
}
```

---

## Cross-artifact integrity (plan)

- `generated_text.outline_id` **must** reference an `outline` with `status: approved` before publication workflows (**enforcement SAFE UNKNOWN**).
- Hash or version references (`evidence_bundle_ref`) are **recommended** for audit; format **SAFE UNKNOWN**.
