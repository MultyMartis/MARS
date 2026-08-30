# FP-0003 — OVERSEO Design artifacts

**Factory Project:** FP-0003 — OVERSEO  
**Domain:** overseo.ru  
**Active version:** `v1`  
**Status:** Design wave D1A — Hero candidate ready / awaiting operator approval  

---

## Active version pointer

| Field | Value |
|-------|-------|
| Active design version | **v1** |
| Production frontend | **NOT STARTED** |
| Design render role | **PROTOTYPE / RENDER SOURCE ONLY** — not production Gulp source |

---

## Structure

```text
DESIGN/
├── README.md                 ← this file
├── v1/
│   ├── exports/              ← operator-facing PNG targets
│   ├── render/               ← HTML/CSS design render sources (isolated)
│   ├── implementation-pack/  ← screen metadata for frontend handoff
│   └── validation/           ← (reserved)
```

---

## D1A deliverable

| Artifact | Path |
|----------|------|
| Hero desktop target PNG | [v1/exports/SCREEN-01-HERO-DESKTOP-v1.png](v1/exports/SCREEN-01-HERO-DESKTOP-v1.png) |
| Hero render source | [v1/render/screen-01-hero/](v1/render/screen-01-hero/) |
| Hero metadata | [v1/implementation-pack/SCREEN-01-HERO-METADATA-v1.md](v1/implementation-pack/SCREEN-01-HERO-METADATA-v1.md) |

---

*Design artifacts are governance targets for PIXEL_PERFECT mode. Intake originals remain in `INCOMING/`.*
