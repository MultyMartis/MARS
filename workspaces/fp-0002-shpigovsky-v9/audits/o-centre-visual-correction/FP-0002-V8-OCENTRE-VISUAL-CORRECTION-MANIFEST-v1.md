# FP-0002 V8 O-Centre Visual Correction Manifest v1

**Task:** FP-0002 V8 O-CENTRE VISUAL CORRECTION IMPLEMENTATION  
**HEAD at manifest:** `df7fe7d8f8155bdfa16e4f8dc8a9cd4aee38901b`  
**Backup:** `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-OCENTRE-VISUAL-CORRECTION.zip`  
**SHA-256:** `C3F4B995C0A3D88DFAF061DD16BA13225D1C43FD259328F8AD8AD67B60F47E32`

| Region | Current source | Required action | Files | Shared risk | Acceptance gate |
|---|---|---|---|---|---|
| Include order | Wrong sequence; founder late; CTA misplaced; no clinic-landscape | Reorder to canonical reconciliation | `o-centre.html` | LOW | DOM order matches audit |
| Institutional | Text-only partial | Restructure G0 lead vs body groups | `institutional-narrative.html`, SCSS | LOW | Founder context adjacent |
| Founder quote | After program CTA | Move after institutional | `o-centre.html`, SCSS modifier | MEDIUM | CF-004 base unchanged |
| Who-we-treat | Text-only category section | Add galleryHtml staff photo + 4 cards | `o-centre.html`, SCSS | LOW | VD-003 closed |
| CTA #1 | Missing | Insert program-cta-band before approach | `o-centre.html` | LOW | VD-002 closed |
| Approach | Inline band with misplaced photo/cards | Text-only band; photo/cards to who-we-treat | `o-centre.html`, SCSS | LOW | VD-004 closed |
| Clinic landscape | Not included | Reuse `clinic-landscape.html` after approach | `o-centre.html`, SCSS spacing | MEDIUM | VD-005 closed; consumers unchanged |
| Program | Before misplaced CTA | After clinic-landscape | `o-centre.html` | LOW | VD-009 closed |
| Infrastructure | Flat auto-grid | 7 semantic subgroups + text interleave | `infrastructure-narrative.html`, SCSS | LOW | VD-006/015 closed |
| DEC-01 | Not wired | Pseudo-element opacity 0.1 | SCSS only | LOW | VD-007 closed |
| CTA #2 | Mid-CTA before founder | Guest CTA after infrastructure only | `o-centre.html` | LOW | Single tail CTA |
| Shared tail | OK | Preserve specialists/reviews/final-form | — | LOW | Regression guard |
| Mobile | Wrong flow | Subgroup mobile rules + asset visibility | SCSS | LOW | Mobile gate |
