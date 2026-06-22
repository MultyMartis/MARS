# Implementation Spec — {PROJECT_NAME}

**Template ID:** FW-T-15  
**Version:** v1  
**Artifact:** IMPLEMENTATION-SPEC  
**Authority:** Theme Specialist / Forge Architect

---

## Scope

| Field | Value |
|-------|-------|
| FP-ID | |
| Mode | A \| B \| C \| D |
| WAD reference | |
| In-scope pages | |
| Out of scope | |

---

## Theme structure

```text
theme/{slug}/
  style.css
  functions.php
  template-parts/
  assets/          # from Gulp dist sync
  acf-json/
```

---

## Build integration

| Step | Command / action |
|------|------------------|
| Frontend build | `npm run build` in FRONTEND/ |
| Asset sync | dist → theme/assets/ |
| Version bump | THEME_VERSION constant |

---

## Plugin boundary

| In theme | In functionality plugin |
|----------|-------------------------|
| | |

---

## Validation plan reference

Link: VALIDATION-PLAN (FW-T-16)

---

## Sign-off

| Role | Date |
|------|------|
| Forge Architect | |
| Operator | |

---

*Template — pilot use only.*
