# {PROJECT-ID} — Page Editability Map v1

**Artifact ID:** PAGE-EDITABILITY-MAP  
**Project:**  
**Date:**  
**Standard:** [CMS ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [DESIGN-TO-CMS](../standards/FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md)

Complements EDITABLE-REGIONS-MAP (frozen vs editable zones). This artefact is **per-route field ownership**.

---

## Page index

| Route / template | H1 owner | Hero | Page-local sections | Pulls entities | Pulls globals | Flex? | Gutenberg? |
|------------------|----------|------|---------------------|----------------|---------------|-------|------------|
| Home | | | | | | no | no |
| About | | | | | | | |
| Contacts | | | | | | | |
| Legal | | | | | | | |
| Hub (e.g. services) | | | | CPT collection | | | |
| Landing (unique) | | | | | | | |

---

## Per-page field list

### {Page name}

| Element | Class (STATIC/GLOBAL/PAGE-LOCAL/ENTITY/REL/REPEATING/MEDIA/CTA) | Storage | Empty behavior | Editor group |
|---------|-------------------------------------------------------------------|---------|----------------|--------------|
| | | | hide / fallback / required | |

---

## Optional sections

| Section | `enabled` field? | Or derive from content? |
|---------|------------------|-------------------------|
| | yes/no | |

---

## Intentionally hardcoded

| String / control | Reason |
|------------------|--------|
| | system label / invariant |

---

*Do not start frontend wiring until this map has no dual owners.*
