# WP Forge DOCX Article Importer Module Spec v1

**Class:** B  
**Maturity:** PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Reference:** FP-0002 P13 DocxImporter

---

## Behavior

- `.docx` only; multi-file; safe zip/XML extraction.
- Import images to media; rewrite src in HTML.
- Clean HTML (no Word junk namespaces).
- Title rules documented (filename vs first heading).
- **Draft-first**; human review; scheduling via core.
- Template `.docx` download for editors.
- Temp-file cleanup always.
- **No auto-publish.**

## Security

Admin capability; MIME/size limits; no XXE; delete temp dirs.

## Integration

Writes `post_content` + featured image as designed; SEO/TOC/typography apply later via other modules.

## Extraction

**B** — isolate brand strings and template asset.

---

*Spec v1.*
