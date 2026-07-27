# I-SEO Report Hub — Report Styling / Client Template Design v0.1

**Status:** DESIGN / POLICY ONLY — no code; no runtime; no DB  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Styling / Client Template Charter 01  
**Parent:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md)

---

## 1. Template source of truth

| Layer | Role |
|-------|------|
| `report_snapshots` payload | **Content** source of truth (immutable) |
| Template id + version | **Render policy** source of truth |
| HTML export artifact | Styled document produced from snapshot + template |
| PDF export artifact | Print rendering of that HTML via Edge headless |
| Admin UI CSS (`app.css`) | Internal app chrome — **not** export visual SoT |

MVP template lives in **versioned app-source code** (constants + embedded CSS / optional small template helper). Git is the template registry for MVP. DB is not the template SoT until a later DB-09/registry charter.

---

## 2. Template identity

| Field | MVP value |
|-------|-----------|
| `template_id` | `iseo_default_v1` |
| `template_version` | `1` (integer) |
| Display label | i-SEO Default Report Template v1 |
| Locale | `ru` primary; Cyrillic-safe fonts |
| Theme | light |

Every newly generated HTML artifact SHOULD include:

- HTML comment or meta tags: `template_id`, `template_version`;
- optional visible footer line with the same ids (small, non-dominant).

---

## 3. Visual hierarchy

Top → bottom for export document:

1. **Header brand band** — text “i-SEO” / report product mark (no binary logo MVP).
2. **Report title (H1)** — one H1; from snapshot/monthly title.
3. **Meta grid** — period, client, project, site, snapshot key/version/checksum, render mode, generated-at.
4. **Source weekly** (if present).
5. **Monthly summary fields** (flat fields).
6. **Report blocks** — each block = section article with title, meta, summary, body.
7. **Footer** — immutability note + template id/version.

Rules:

- one composition per page flow — not a SaaS dashboard;
- no hero media overlays;
- no floating badges/chips on content;
- cards only where they aid scanning of KPI/risk blocks later — default **no card chrome** for body text.

---

## 4. Typography

| Token | MVP guidance |
|-------|--------------|
| Body | System / local stack with Cyrillic: `"Segoe UI", "Helvetica Neue", Arial, sans-serif` (prefer readable UI sans for reports; avoid decorative display fonts) |
| Optional serif for long body | Allowed only if Edge print proves Cyrillic coverage; Georgia fallback already exists — may be kept for body if verified |
| H1 | ~22–28px equivalent; strong weight; not overpowering brand line |
| H2 | section titles; clear separation |
| H3 | block titles |
| Meta / code | monospace for keys/checksums; smaller size; wrap checksums |
| Line height | ~1.45–1.55 body |
| Color text | near-black `#1a1a1a` on white/off-white |

Avoid: Inter/Roboto as remote CDN fonts; icon fonts; emoji as structure.

---

## 5. Spacing and layout tokens

| Token | MVP |
|-------|-----|
| Page background | `#ffffff` |
| Content max width (screen HTML) | ~48–56rem |
| Section gap | ~1.5–2rem |
| Block gap | ~1.25–1.5rem |
| Border accent | 1px solid `#cccccc` / `#dddddd` — hairlines only |
| Radius | **0** default (no rounded SaaS look unless later approved) |
| Shadow | **none** for export |

---

## 6. Section / block styles

- `.export-section` — top border + padding; clear H2.
- `.export-block` — spacing only; optional left rule for risk/status types later.
- Escape all text; preserve `nl2br` for body as today.
- Do not inject live HTML from blocks without escaping (current safe path preserved).

---

## 7. KPI / card styles (future-ready)

MVP may not have dedicated KPI widgets. When introduced:

- simple definition list or compact metric row;
- no multi-layer shadows;
- no pill clusters;
- numbers readable in print (avoid tiny grey labels only).

Defer complex card grids until content architecture needs them.

---

## 8. Table styles (future-ready)

When tables appear:

- `border-collapse: collapse`;
- 1px borders;
- header background light grey (`#f5f5f5`);
- avoid fixed layouts that clip in A4;
- allow horizontal wrap; prefer stacked mobile later for preview only.

---

## 9. Risk / status visual language

| Status class (future) | Visual |
|-----------------------|--------|
| ok / positive | text + optional left bar muted green — not neon |
| warn | muted amber left bar |
| risk / blocker | muted red left bar + stronger H3 weight |
| info | neutral grey |

No emoji-only status. Color is secondary to text labels.

---

## 10. A4 PDF print rules

| Rule | Value |
|------|-------|
| Page size | **A4** via `@page { size: A4; margin: 14mm 12mm; }` (tune in implementation) |
| Color | light; print backgrounds minimal |
| Page breaks | avoid breaking inside `.export-block` where possible (`break-inside: avoid` with Edge caveats) |
| Headers/footers | browser default Edge footers acceptable unless later suppressed via flags; do not invent JS print hacks |
| Width | avoid fixed px wider than printable area |
| Images | none in MVP export |

CSS must stay **Edge print-safe**: no complex grid for critical meta if it collapses badly — prefer simple block/table for print meta if needed.

---

## 11. HTML / PDF parity

| Principle | Rule |
|-----------|------|
| Single style source | Embedded CSS in HTML artifact drives both screen open and PDF |
| No PDF-only layout fork in MVP | Prefer one stylesheet with `@media print` |
| Preview route | May share token subset later; must not silently change existing export files |
| Parity check | Future smoke: open HTML + PDF side-by-side for title/meta/blocks order |

Known acceptable deltas: Edge margin chrome, font substitution, page-break placement.

---

## 12. No external assets / no JS

Export HTML MUST NOT contain:

- `<script>` (inline or external);
- `http(s)://` stylesheet/font/image links;
- tracking pixels;
- remote CDN.

Allowed:

- embedded `<style>`;
- data-URI only if later explicitly chartered (not MVP for logos).

---

## 13. Client branding — MVP vs later

### MVP

- i-SEO default branding only (text header).
- Client / project / site **names** from snapshot payload.
- No custom logo upload.
- No client color picker.
- No client-specific CSS columns in DB.
- No external brand assets.

### Later (not this wave)

- client brand profile;
- logo storage outside public or controlled asset path;
- template assignment per client/project;
- admin template preview;
- DB-backed registry / assignment UI.

---

## 14. Rendering metadata

Future exports (implementation or DB-09) SHOULD record:

| Field | Purpose |
|-------|---------|
| `template_id` | e.g. `iseo_default_v1` |
| `template_version` | e.g. `1` |
| `render_engine` | e.g. `edge-headless` for PDF; `php-html-builder` for HTML |
| `render_options` / JSON | margins, page size, flags |
| `source_snapshot_checksum` | already present conceptually |
| `source_html_export_id` | for PDF (already used in PDF path) |

MVP Implementation 01 may embed metadata in HTML first; DB columns can wait for DB-09.

---

## 15. Immutability / versioning

| Object | Rule |
|--------|------|
| Snapshot payload | Immutable; styling does not rewrite snapshot |
| Existing HTML id 1 / PDF id 2 | Historical; do not silently rewrite files or checksums |
| Template change | Bump `template_version` (or new `template_id`) |
| Need restyle of published export | New export version **or** explicit repair/regeneration charter — never silent overwrite |
| Idempotent create | Continues to return existing ready row when key matches |

---

## 16. Model options (summary)

| Option | MVP? | Notes |
|--------|------|-------|
| A. Code-only static template | **YES** | Recommended |
| B. Git config template registry | Later optional | No DB; versioned in Git |
| C. DB-backed templates | No | Needs schema + admin UI |
| D. Client-level assignment | No | Needs client relation fields |

---

## 17. Design non-goals

- SaaS marketing landing look;
- dark mode export;
- purple/glow trends;
- rounded-full pills;
- public branded portal chrome;
- WordPress theme coupling.
