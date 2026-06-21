# FP-0002 v2 — Foundation Typography Report v1

**Task:** FP-0002 v2 FOUNDATION START · FND-03  
**Date:** 2026-06-22  
**Files:** `src/scss/base/_typography.scss` · `src/scss/base/_base.scss` · `src/scss/abstracts/_tokens-typography.scss`

---

## 1. Implemented tiers

| Class / element | Desktop | Mobile | Weight | Line-height | Source |
|-----------------|---------|--------|--------|-------------|--------|
| `h1` / `.h1` | 70px | 42px | 500 | 84px / 50px | Normalization TY-01 |
| `h2` / `.h2` | 36px | 22px | 500 | 44px / 28px | Olga §2 |
| `h3` / `.h3` | 30px | 22px | 500 | 36px / 28px | Normalization |
| `h4` / `.h4` | 20px | 18px | 400 | 28px / 26px | Normalization |
| `.body-text` / `body` | 18px | 16px | 300 | 28px / 24px | Olga §2 |
| `.body-sm` | 16px | 16px | 300 | 24px | Normalization |
| `.caption` | 12px | 12px | 400 | 16px | Normalization |
| `.link` | inherits body | inherits | 400 | inherits | v3 link pattern |

---

## 2. Text Fidelity Contract compliance

| Rule | Status |
|------|--------|
| No invented hierarchy beyond v3 §4.1 | **PASS** |
| Desktop-first base + mobile `@max-width: 1023px` | **PASS** |
| `letter-spacing` forbidden | **PASS** — absent from source |
| `word-break` forbidden | **PASS** — absent |
| `overflow-wrap` forbidden | **PASS** — absent |
| `hyphens` forbidden | **PASS** — absent |
| Russian Typography Rules (OL-06) | **PASS** — no break CSS |

---

## 3. Font loading

| Item | Value | Status |
|------|-------|--------|
| Family | Inter | v3 §4 |
| Weights loaded | 300, 400, 500 | Google Fonts on demo page |
| Self-host | TBD | **SAFE UNKNOWN** — v3 notes self-host optional |

---

## 4. H1 weight note

H1 weight 500 is **production default** per v3 §4.1 — PDF weight marked **SAFE UNKNOWN** (TY-01). Not invented — sourced from Normalization table.

---

## 5. Demo evidence

Rendered on `src/pages/desktop-foundation.html` § Typography — all tiers visible.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
