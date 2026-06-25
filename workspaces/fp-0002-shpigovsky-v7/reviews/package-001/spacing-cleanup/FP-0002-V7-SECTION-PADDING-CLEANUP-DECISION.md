# FP-0002 V7 — Section Padding Cleanup Decision Map

**Phase:** Package #001 Phase 4A  
**Date:** 2026-06-24  
**Status:** APPROVED FOR IMPLEMENTATION

## Classification counts

| Classification | Count |
|----------------|------:|
| ACCIDENTAL_OVERRIDE | 13 |
| DUPLICATE_BASE_VALUE | 1 |
| MEASURED_EXCEPTION | 0 |
| INTERNAL_COMPONENT_PADDING | preserved (non-root) |
| WRONG_OWNER | 0 |
| STRUCTURAL_EXCEPTION | 1 (`.hero` — no change) |
| SAFE_UNKNOWN | 0 |

## Decision table

| Selector | Classification | Action | Evidence | Expected visual effect |
| -------- | -------------- | ------ | -------- | ---------------------- |
| `.home-gallery` | ACCIDENTAL_OVERRIDE | REMOVE | Task brief example; computed 30px vs base 50px; no Figma root exception | Section adopts `var(--pad-y)` (+20px top/bottom) |
| `.home-why-us` padding-top | ACCIDENTAL_OVERRIDE | REMOVE | Asymmetric 30/50 pattern; no Figma measured root gap | Top padding becomes 50px |
| `.home-why-us` padding-bottom | DUPLICATE_BASE_VALUE | REMOVE_REDUNDANT | Value equals base `--pad-y` | No change (base already 50px) |
| `.home-staff-photo` | ACCIDENTAL_OVERRIDE | REMOVE | Task brief example; full-bleed image is inner `__bleed`, not root | Section adopts `var(--pad-y)` |
| `.home-feature-grid` | ACCIDENTAL_OVERRIDE | REMOVE | pad-gap copy pattern | Section adopts `var(--pad-y)` |
| `.home-rehabilitation-requirements` | ACCIDENTAL_OVERRIDE | REMOVE | pad-gap copy pattern | Section adopts `var(--pad-y)` |
| `.home-rehabilitation-program` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block pad-gap; Home + Services | Section adopts `var(--pad-y)` |
| `.home-genotyping` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block | Section adopts `var(--pad-y)` |
| `.home-comfort` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block; Home + Services | Section adopts `var(--pad-y)` |
| `.home-videos` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block | Section adopts `var(--pad-y)` |
| `.home-specialists` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block | Section adopts `var(--pad-y)` |
| `.home-articles` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block | Section adopts `var(--pad-y)` |
| `.home-faq` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block; Home + Services | Section adopts `var(--pad-y)` |
| `.home-final-form` | ACCIDENTAL_OVERRIDE | REMOVE | Shared block; Home + Services | Section adopts `var(--pad-y)` |
| `.hero` | STRUCTURAL_EXCEPTION | KEEP_WITH_REASON | Outside `<main>`; viewport-height block | UNCHANGED |
| `.home-clinic-landscape` | — | KEEP | Override already commented out; uses base | UNCHANGED |
| `.home-recovery-life` | — | KEEP | No root override (Phase 3C) | UNCHANGED |
| All other Home sections on base rhythm | — | KEEP | Already inherit `main > section` | UNCHANGED |

## Action summary

### REMOVE (13 selectors)

`.home-gallery`, `.home-why-us` (top only), `.home-staff-photo`, `.home-feature-grid`, `.home-rehabilitation-requirements`, `.home-rehabilitation-program`, `.home-genotyping`, `.home-comfort`, `.home-videos`, `.home-specialists`, `.home-articles`, `.home-faq`, `.home-final-form`

### REMOVE_REDUNDANT (1)

`.home-why-us` padding-bottom

### MOVE_TO_INNER_OWNER

NONE

### KEEP / KEEP_WITH_EVIDENCE / DO_NOT_CHANGE

`.hero`, `.home-recovery-intro`, `.home-founder-quote`, `.home-treatment-prevention`, `.home-clinic-landscape`, `.home-recovery-life`, `.home-reviews`, all internal `__*` padding
